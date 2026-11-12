#!/usr/bin/env python3
"""AstroAI Today: collect new arXiv papers that apply machine learning to astronomy.

Each run
  1. reads every astro-ph paper announced in the last days from the arXiv OAI-PMH interface
     (the search API is the fallback) and keeps those whose title or abstract mentions a
     machine learning term, and adds recent cs and stat.ML papers from the search API whose
     title or abstract mentions an astronomy term,
  2. asks a language model which of the new papers use machine learning as a central part
     of their method, and writes a one-sentence summary and a topic for each of them,
  3. stores the result in data/today/daily/<date>.json, and
  4. refreshes the digest of the current week and month in data/today/weekly/ and
     data/today/monthly/, finalising the previous week or month once it has ended.

The summaries are written by Claude when ANTHROPIC_API_KEY is set, otherwise by GitHub
Models with the GITHUB_TOKEN of the workflow. Without either, papers are kept with a short
excerpt of the abstract and no relevance check.

Usage:
    python scripts/today.py                      # daily update
    python scripts/today.py --backfill 7         # first run: collect the last seven days
    python scripts/today.py --lookup 2611.14479  # print arXiv metadata, write nothing
"""
import argparse
import datetime as dt
import email.utils
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "today"
REPO = "https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy"
UA = f"AstroAI Today ({REPO})"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

ASTRO_CATS = ["astro-ph.GA", "astro-ph.CO", "astro-ph.EP", "astro-ph.HE", "astro-ph.IM", "astro-ph.SR"]
ML_RE = re.compile(
    r"\b(machine[- ]learn\w*|deep[- ]learn\w*|neural[- ]\w+|foundation models?|language models?|LLMs?|"
    r"transformers?|simulation[- ]based inference|normali[sz]ing[- ]flows?|diffusion models?|score[- ]based|"
    r"convolutional|self[- ]supervised|contrastive|graph neural|random forests?|gradient[- ]boost\w*|XGBoost|"
    r"autoencoders?|variational auto\w*|reinforcement learning|artificial intelligence|generative (?:model|adversarial)\w*|"
    r"emulat\w+|k-means|clustering algorithm|anomaly detection|U-Net|ResNet|multi-?layer perceptrons?|"
    r"agentic|(?:AI|LLM) agents?|supervised learning|unsupervised learning|representation learning|"
    r"Gaussian process(?:es)? regression|support vector)\b", re.I)
ML_CATS = ["cs.LG", "cs.CV", "cs.AI", "cs.CL", "cs.IR", "stat.ML"]
ASTRO_TERMS = ["astronomy", "astronomical", "astrophysics", "astrophysical", "galaxy", "galaxies", "telescope",
               "cosmology", "cosmological", "exoplanet", "exoplanets", "solar flare", "gravitational wave",
               "supernova", "stellar", "light curves", "sky survey"]
ASTRO_RE = re.compile(r"\b(" + "|".join(re.escape(t) for t in ASTRO_TERMS) + r")", re.I)
LINK = re.compile(r"https?://(?:github\.com|gitlab\.com|huggingface\.co|zenodo\.org)/[^\s,;)\]}>]+", re.I)

SECTIONS = [s["title"] for s in yaml.safe_load((ROOT / "data" / "entries.yml").read_text(encoding="utf-8"))["sections"]
            if s.get("kind") != "links"]


# arXiv ---------------------------------------------------------------------------

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def http(url, data=None, headers=None, timeout=90):
    """GET, or POST when data is given. Redirects are followed with the same method and body."""
    for _ in range(4):
        req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, **(headers or {})})
        try:
            with _opener.open(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (301, 302, 303, 307, 308) and exc.headers.get("Location"):
                url = urllib.parse.urljoin(url, exc.headers["Location"])
                continue
            raise
    raise urllib.error.URLError(f"too many redirects for {url}")


def clause(field, terms):
    return "(" + " OR ".join(f'{field}:"{t}"' if " " in t or "-" in t else f"{field}:{t}" for t in terms) + ")"


def arxiv_api(params):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            body = http(url)
            time.sleep(3)  # arXiv asks for no more than one request every three seconds
            return parse(body)
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"arXiv request failed ({exc}), retrying", file=sys.stderr)
            time.sleep(10 * (attempt + 1))
    sys.exit("The arXiv API did not respond.")


def parse(body):
    out = []
    for e in ET.fromstring(body).findall("a:entry", NS):
        m = re.search(r"abs/([^v\s]+)(v\d+)?$", e.findtext("a:id", "", NS))
        if not m:
            continue
        text = lambda tag: " ".join(e.findtext(tag, "", NS).split())
        abstract = text("a:summary")
        comment = text("x:comment")
        out.append({
            "id": m.group(1),
            "title": text("a:title"),
            "authors": [" ".join(a.findtext("a:name", "", NS).split()) for a in e.findall("a:author", NS)],
            "abstract": abstract,
            "comment": comment,
            "journal_ref": text("x:journal_ref"),
            "doi": text("x:doi"),
            "primary": (e.find("x:primary_category", NS).get("term") if e.find("x:primary_category", NS) is not None else ""),
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "published": text("a:published"),
            "links": sorted({u.rstrip(".") for u in LINK.findall(abstract + " " + comment)}),
        })
    return out


def recent(query, since, page=200):
    """All papers matching `query` submitted after `since`, newest first.

    The arXiv API sometimes returns fewer entries than requested, so paging continues from
    the number actually received until a paper older than `since` appears.
    """
    out, start, empty = [], 0, 0
    while start < 8000:
        batch = arxiv_api({"search_query": query, "sortBy": "submittedDate", "sortOrder": "descending",
                           "start": start, "max_results": page})
        if not batch:
            empty += 1
            if empty == 3:
                break
            continue
        empty = 0
        out += [p for p in batch if p["published"] >= since]
        if batch[-1]["published"] < since:
            break
        start += len(batch)
    return out


# arXiv OAI-PMH ---------------------------------------------------------------------

OAI = "https://oaipmh.arxiv.org/oai"
OAI_NS = {"o": "http://www.openarchives.org/OAI/2.0/", "r": "http://arxiv.org/OAI/arXivRaw/"}
TEX_ACCENT = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303", "=": "\u0304",
              ".": "\u0307", "c": "\u0327", "v": "\u030c", "u": "\u0306", "H": "\u030b", "k": "\u0328"}
TEX_LETTER = {"ss": "\u00df", "o": "\u00f8", "O": "\u00d8", "aa": "\u00e5", "AA": "\u00c5", "l": "\u0142",
              "L": "\u0141", "ae": "\u00e6", "AE": "\u00c6", "i": "i", "j": "j"}


def detex(text):
    """Turn the TeX accents that arXiv keeps in author names into Unicode."""
    text = re.sub(r"\\([\"'`^~=.])\s*\{?\\?([A-Za-z])\}?", lambda m: m.group(2) + TEX_ACCENT[m.group(1)], text)
    text = re.sub(r"\\([cvuHk])(?:\{\\?([A-Za-z])\}|\s+([A-Za-z]))",
                  lambda m: (m.group(2) or m.group(3)) + TEX_ACCENT[m.group(1)], text)
    text = re.sub(r"\\(ss|aa|AA|ae|AE|[oOlLij])(?![A-Za-z])\s*", lambda m: TEX_LETTER[m.group(1)], text)
    return unicodedata.normalize("NFC", text.replace("{", "").replace("}", ""))


def split_authors(text):
    text = re.sub(r"\([^()]*\)", "", detex(" ".join(text.split())))
    names = re.split(r",\s*(?:and\s+)?|\s+and\s+", text)
    return [n.strip() for n in names if n.strip()]


def oai_page(params):
    for attempt in range(6):
        try:
            body = http(OAI + "?" + urllib.parse.urlencode(params), timeout=180)
            time.sleep(3)
            return ET.fromstring(body)
        except urllib.error.HTTPError as exc:
            if exc.code != 503:
                raise
            wait = int(exc.headers.get("Retry-After") or 20)
            print(f"OAI-PMH asks to wait {wait} s", file=sys.stderr)
            time.sleep(min(wait, 120))
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"OAI-PMH request failed ({exc}), retrying", file=sys.stderr)
            time.sleep(15 * (attempt + 1))
    raise RuntimeError("the OAI-PMH interface did not respond")


def oai_recent(since, today):
    """New astro-ph papers announced on or after `since`, newest first.

    A record counts as new when it has a single version, or when its first version was
    submitted in the window; this leaves out replacements of older papers. The date used is
    the OAI datestamp, which for a new paper is the day it was announced.
    """
    params = {"verb": "ListRecords", "metadataPrefix": "arXivRaw", "set": "physics:astro-ph", "from": since}
    out, records = [], 0
    while True:
        root = oai_page(params)
        error = root.find("o:error", OAI_NS)
        if error is not None:
            if error.get("code") == "noRecordsMatch":
                break
            raise RuntimeError(f"OAI-PMH error {error.get('code')}: {error.text}")
        listing = root.find("o:ListRecords", OAI_NS)
        for rec in listing.findall("o:record", OAI_NS):
            records += 1
            head, meta = rec.find("o:header", OAI_NS), rec.find("o:metadata/r:arXivRaw", OAI_NS)
            if head.get("status") == "deleted" or meta is None:
                continue
            text = lambda tag: " ".join((meta.findtext(f"r:{tag}", "", OAI_NS) or "").split())
            versions = meta.findall("r:version", OAI_NS)
            try:
                first = email.utils.parsedate_to_datetime(versions[0].findtext("r:date", "", OAI_NS)).date().isoformat()
            except (IndexError, TypeError, ValueError):
                first = ""
            stamp = head.findtext("o:datestamp", "", OAI_NS)
            if len(versions) > 1 and first < since:
                continue
            cats = text("categories").split()
            abstract, comment = text("abstract"), text("comments")
            out.append({
                "id": text("id"),
                "title": text("title") if "$" in text("title") else detex(text("title")),
                "authors": split_authors(meta.findtext("r:authors", "", OAI_NS)),
                "abstract": abstract,
                "comment": comment,
                "journal_ref": text("journal-ref"),
                "doi": text("doi"),
                "primary": cats[0] if cats else "",
                "categories": cats,
                "published": min(stamp, today) if stamp else first,
                "links": sorted({u.rstrip(".") for u in LINK.findall(abstract + " " + comment)}),
            })
        token = listing.find("o:resumptionToken", OAI_NS)
        if token is None or not (token.text or "").strip():
            break
        params = {"verb": "ListRecords", "resumptionToken": token.text.strip()}
    print(f"OAI-PMH returned {records} astro-ph records, {len(out)} of them new papers")
    return sorted(out, key=lambda p: p["published"], reverse=True)


def candidates(since, today):
    """Recent astro-ph papers that mention machine learning, and recent ML papers that mention astronomy.

    Keyword matching is done here rather than in the arXiv query, which is less complete for long queries.
    """
    try:
        astro = oai_recent(since, today)
    except Exception as exc:
        print(f"warning: OAI-PMH harvest failed ({exc}); using the search API", file=sys.stderr)
        astro = recent("(" + " OR ".join(f"cat:{c}" for c in ASTRO_CATS) + ")", since)
    ml = recent("(" + " OR ".join(f"cat:{c}" for c in ML_CATS) + ") AND " + clause("abs", ASTRO_TERMS), since)
    seen = {}
    for p in astro:
        if ML_RE.search(p["title"] + " " + p["abstract"]):
            seen.setdefault(p["id"], p)
    for p in ml:
        if ASTRO_RE.search(p["title"] + " " + p["abstract"]):
            seen.setdefault(p["id"], p)
    print(f"scanned {len(astro)} astro-ph and {len(ml)} cs or stat.ML papers; {len(seen)} match the keywords")
    return sorted(seen.values(), key=lambda p: p["published"], reverse=True)


# Language model --------------------------------------------------------------------

class Writer:
    """Thin client for Claude or GitHub Models. `name` is None when no model is available."""

    def __init__(self):
        self.anthropic = os.environ.get("ANTHROPIC_API_KEY")
        self.github = os.environ.get("GITHUB_TOKEN") if os.environ.get("TODAY_GITHUB_MODELS", "on") != "off" else None
        if self.anthropic:
            self.name = os.environ.get("TODAY_ANTHROPIC_MODEL", "claude-haiku-5-5")
        elif self.github:
            self.name = os.environ.get("TODAY_GITHUB_MODEL", "openai/gpt-4.1-mini")
        else:
            self.name = None
        self.last = 0.0

    def ask(self, system, prompt, max_tokens=1500):
        if not self.name:
            return None
        wait = 4.5 - (time.time() - self.last)  # stay under 15 requests a minute
        if wait > 0:
            time.sleep(wait)
        self.last = time.time()
        try:
            if self.anthropic:
                body = json.dumps({"model": self.name, "max_tokens": max_tokens, "system": system,
                                   "messages": [{"role": "user", "content": prompt}]}).encode()
                r = json.loads(http("https://api.anthropic.com/v1/messages", body, {
                    "x-api-key": self.anthropic, "anthropic-version": "2023-06-01", "content-type": "application/json"}))
                return "".join(b.get("text", "") for b in r.get("content", []))
            return self.ask_github(system, prompt, max_tokens)
        except Exception as exc:
            detail = exc.read().decode(errors="replace")[:400] if isinstance(exc, urllib.error.HTTPError) else ""
            print(f"warning: the model request failed ({exc}) {detail}; continuing without summaries", file=sys.stderr)
            self.name = None
            return None

    GITHUB_MODELS = "https://models.github.ai/inference/chat/completions"
    GITHUB_FALLBACK = ["openai/gpt-4.1-mini", "openai/gpt-4o-mini"]

    def ask_github(self, system, prompt, max_tokens):
        """Call GitHub Models with curl, as in the GitHub documentation, trying a second model on failure."""
        models = [self.name] + [m for m in self.GITHUB_FALLBACK if m != self.name]
        errors = []
        with tempfile.NamedTemporaryFile("w", suffix=".headers") as hf:
            hf.write(f"Authorization: Bearer {self.github}\nAccept: application/vnd.github+json\n"
                     "X-GitHub-Api-Version: 2022-11-28\nContent-Type: application/json\n")
            hf.flush()
            for model in models:
                body = json.dumps({"model": model, "temperature": 0.2, "max_tokens": max_tokens,
                                   "messages": [{"role": "system", "content": system},
                                                {"role": "user", "content": prompt}]}).encode()
                res = subprocess.run(["curl", "-sS", "-L", "--max-time", "180", "-X", "POST", self.GITHUB_MODELS,
                                      "-H", f"@{hf.name}", "--data-binary", "@-", "-w", "\n%{http_code} %{content_type}"],
                                     input=body, capture_output=True, timeout=200)
                raw, _, status = res.stdout.decode(errors="replace").rpartition("\n")
                try:
                    text = json.loads(raw)["choices"][0]["message"]["content"]
                except (json.JSONDecodeError, KeyError, IndexError, TypeError):
                    errors.append(f"{model}: status {status or 'none'}, body {raw[:240]!r} {res.stderr.decode(errors='replace')[:160]}")
                    continue
                if model != self.name:
                    print(f"switching to {model}")
                    self.name = model
                return text
        raise RuntimeError("; ".join(errors))


def first_json(text, opener):
    if not text:
        return None
    start = text.find(opener)
    end = text.rfind("]" if opener == "[" else "}")
    if start < 0 or end <= start:
        return None
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        return None


ASSESS_SYSTEM = """You curate a daily list of new research papers that apply machine learning to astronomy.
For every paper you are given, decide three things.
relevant: true when machine learning or artificial intelligence (neural networks, foundation or language models, agents, learned emulators, neural simulation-based inference, normalizing flows, diffusion models, tree ensembles, learned clustering or representation learning, and similar) is a central part of the method or the contribution, and the work concerns astronomy, astrophysics, cosmology, solar or space physics, or planetary science. false when machine learning is only mentioned or plays a minor role, or when the subject is not astronomy.
summary: one plain sentence of at most 32 words saying what was done, with which method and data, and the main result if stated. Do not start with "This paper" or "The authors". No praise or hype.
topic: the single best matching section title from the list provided, copied exactly.
Answer with a JSON array only, one object per paper: {"id": ..., "relevant": ..., "summary": ..., "topic": ...}."""


def assess(writer, papers):
    """Fill relevant, summary and topic for each paper, eight at a time."""
    for i in range(0, len(papers), 8):
        batch = papers[i:i + 8]
        prompt = "Section titles:\n" + "\n".join(SECTIONS) + "\n\nPapers:\n\n" + "\n\n".join(
            f"id: {p['id']}\ntitle: {p['title']}\ncategories: {', '.join(p['categories'])}\nabstract: {p['abstract'][:1800]}"
            for p in batch)
        answer = first_json(writer.ask(ASSESS_SYSTEM, prompt, 1800), "[")
        by_id = {str(a.get("id", "")).strip(): a for a in answer or [] if isinstance(a, dict)}
        for p in batch:
            a = by_id.get(p["id"])
            if a and isinstance(a.get("relevant"), bool) and a.get("summary"):
                p["relevant"] = a["relevant"]
                p["summary"] = " ".join(str(a["summary"]).split())
                p["topic"] = a.get("topic") if a.get("topic") in SECTIONS else ""
                p["model"] = writer.name
    return papers


def excerpt(abstract, limit=260):
    sentence = re.split(r"(?<=[.!?])\s+", abstract.strip(), maxsplit=1)[0]
    return sentence if len(sentence) <= limit else sentence[:limit].rsplit(" ", 1)[0] + "..."


def stored(p):
    """The fields kept for a paper. Abstracts are not stored; papers without a model summary keep one sentence."""
    out = {k: p[k] for k in ("id", "title", "primary", "categories", "published", "comment", "journal_ref", "doi", "links")}
    out["authors"] = p["authors"][:6]
    out["n_authors"] = len(p["authors"])
    out["relevant"] = p.get("relevant")
    out["summary"] = p.get("summary", "")
    out["topic"] = p.get("topic", "")
    out["model"] = p.get("model")
    if not out["summary"]:
        out["excerpt"] = excerpt(p["abstract"])
    return out


# Storage -----------------------------------------------------------------------------

def load(path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def daily_files():
    return sorted((DATA / "daily").glob("*.json"))


def known_ids():
    ids = set()
    for f in daily_files():
        day = load(f)
        ids.update(p["id"] for p in day["papers"])
        ids.update(p["id"] for p in day.get("excluded", []))
    return ids


def write_day(date, papers, writer):
    path = DATA / "daily" / f"{date}.json"
    day = load(path) or {"date": date, "papers": [], "excluded": []}
    for p in papers:
        if p.get("relevant") is False:
            day["excluded"].append({"id": p["id"], "title": p["title"]})
        else:
            day["papers"].append(stored(p))
    day["papers"].sort(key=lambda p: p["published"], reverse=True)
    day["updated"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    day["model"] = writer.name
    save(path, day)
    return path


def resummarise(writer, days=7):
    """Give recent papers that were stored without a model summary a second chance."""
    if not writer.name:
        return
    for f in daily_files()[-days:]:
        day = load(f)
        todo = [p for p in day["papers"] if not p.get("summary")]
        if not todo:
            continue
        meta = {p["id"]: p for p in arxiv_api({"id_list": ",".join(p["id"] for p in todo), "max_results": len(todo)})}
        fresh = assess(writer, [meta[p["id"]] for p in todo if p["id"] in meta])
        kept = []
        for p in day["papers"]:
            q = next((x for x in fresh if x["id"] == p["id"] and "relevant" in x), None)
            if q is None:
                kept.append(p)
            elif q["relevant"] is False:
                day.setdefault("excluded", []).append({"id": p["id"], "title": p["title"]})
            else:
                p.update({"relevant": q["relevant"], "summary": q["summary"], "topic": q["topic"], "model": q["model"]})
                p.pop("excerpt", None)
                kept.append(p)
        day["papers"] = kept
        save(f, day)


# Digests ---------------------------------------------------------------------------------

DIGEST_SYSTEM = """You write the digest of a period of new arXiv papers that apply machine learning to astronomy.
Write for astronomers and machine learning researchers. Be factual, specific and plain; no hype, no praise, no rhetorical questions.
Answer with a JSON object only:
{"overview": a paragraph of at most WORDS words describing the main directions of the period, naming concrete methods, data sets or surveys,
 "themes": three to five short noun phrases,
 "highlights": three to six arXiv ids, choosing papers that release data, benchmarks, code or models, or that introduce broadly useful methods}"""


def period_papers(start, end):
    out = []
    for f in daily_files():
        if start <= f.stem <= end:
            out += [p for p in load(f)["papers"] if p.get("relevant") is not False]
    return out


def digest(writer, kind, key, start, end, final, context=""):
    path = DATA / kind / f"{key}.json"
    old = load(path)
    if old and old.get("final"):
        return
    papers = period_papers(start, end)
    if not papers:
        return
    topics = {}
    for p in papers:
        topics[p.get("topic") or "Other"] = topics.get(p.get("topic") or "Other", 0) + 1
    doc = {"period": key, "start": start, "end": end, "final": final, "count": len(papers),
           "topics": dict(sorted(topics.items(), key=lambda kv: -kv[1])),
           "overview": "", "themes": [], "highlights": [], "model": None,
           "updated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
    if old and old.get("count") == len(papers) and old.get("overview"):
        doc.update({k: old[k] for k in ("overview", "themes", "highlights", "model")})
    elif writer.name:
        lines = [f"{p['id']} | {p['title']} | {p.get('summary') or p.get('excerpt', '')}" for p in papers[:90]]
        lines += [f"{p['id']} | {p['title']}" for p in papers[90:160]]
        words = 120 if kind == "weekly" else 170
        prompt = (f"Period: {start} to {end}, {len(papers)} papers.\nTopic counts: {json.dumps(doc['topics'])}\n"
                  + (f"\nEarlier weekly digests in this period:\n{context}\n" if context else "")
                  + "\nPapers (id | title | summary):\n" + "\n".join(lines))
        answer = first_json(writer.ask(DIGEST_SYSTEM.replace("WORDS", str(words)), prompt, 900), "{")
        if isinstance(answer, dict) and answer.get("overview"):
            ids = {p["id"] for p in papers}
            doc["overview"] = " ".join(str(answer["overview"]).split())
            doc["themes"] = [str(t) for t in answer.get("themes", [])][:5]
            doc["highlights"] = [i for i in (str(x).strip() for x in answer.get("highlights", [])) if i in ids][:6]
            doc["model"] = writer.name
    save(path, doc)


def iso_week(day):
    y, w, _ = day.isocalendar()
    monday = day - dt.timedelta(days=day.weekday())
    return f"{y}-W{w:02d}", monday, monday + dt.timedelta(days=6)


def digests(writer, today):
    # Finalise the previous week and month, then refresh the current ones.
    for day, final in ((today - dt.timedelta(days=7), True), (today, False)):
        key, start, end = iso_week(day)
        digest(writer, "weekly", key, start.isoformat(), end.isoformat(), final or end < today)
    last_month_end = today.replace(day=1) - dt.timedelta(days=1)
    for first, final in ((last_month_end.replace(day=1), True), (today.replace(day=1), False)):
        nxt = (first.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        end = nxt - dt.timedelta(days=1)
        weeks = [load(f) for f in sorted((DATA / "weekly").glob("*.json"))]
        context = "\n".join(f"{w['period']}: {w['overview']}" for w in weeks
                            if w and w.get("overview") and first.isoformat() <= w["end"] and w["start"] <= end.isoformat())
        digest(writer, "monthly", first.strftime("%Y-%m"), first.isoformat(), end.isoformat(), final, context)


# Main --------------------------------------------------------------------------------------

def lookup(ids):
    for p in arxiv_api({"id_list": ",".join(ids), "max_results": len(ids)}):
        print(f"## {p['id']}: {p['title']}\n")
        print(f"- Authors: {', '.join(p['authors'][:12])}{' et al.' if len(p['authors']) > 12 else ''}")
        print(f"- Submitted: {p['published']}; categories: {', '.join(p['categories'])}")
        for k in ("comment", "journal_ref", "doi"):
            if p[k]:
                print(f"- {k}: {p[k]}")
        print(f"\n{p['abstract']}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backfill", type=int, default=0, help="collect the last N days, filed under their submission dates")
    ap.add_argument("--lookup", help="comma-separated arXiv ids to print; nothing is written")
    ap.add_argument("--date", help="file today's papers under this date (YYYY-MM-DD) instead of the current UTC date")
    args = ap.parse_args()

    if args.lookup:
        lookup([i.strip() for i in args.lookup.replace(" ", ",").split(",") if i.strip()])
        return

    today = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(dt.timezone.utc).date()
    writer = Writer()
    print(f"model: {writer.name or 'none'}")
    window = max(args.backfill, 4)
    since = (today - dt.timedelta(days=window)).isoformat()
    known = known_ids()
    new = [p for p in candidates(since, today.isoformat()) if p["id"] not in known]
    print(f"{len(new)} new candidate papers since {since}")
    assess(writer, new)
    if args.backfill:
        by_day = {}
        for p in new:
            by_day.setdefault(p["published"][:10], []).append(p)
        for day, papers in sorted(by_day.items()):
            print("wrote", write_day(day, papers, writer))
    elif new:
        print("wrote", write_day(today.isoformat(), new, writer))
    resummarise(writer)
    digests(writer, today)


if __name__ == "__main__":
    main()
