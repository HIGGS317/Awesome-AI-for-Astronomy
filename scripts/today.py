#!/usr/bin/env python3
"""AstroAI Today: collect new arXiv papers that apply machine learning to astronomy.

Each run
  1. queries the arXiv API for recent astro-ph papers that mention machine learning terms,
     and for recent cs and stat.ML papers that mention astronomy terms,
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
import json
import os
import pathlib
import re
import sys
import time
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
ML_TERMS = ["machine learning", "deep learning", "neural network", "neural networks", "foundation model",
            "language model", "language models", "transformer", "simulation-based inference",
            "normalizing flow", "normalising flow", "diffusion model", "convolutional", "self-supervised",
            "graph neural", "random forest", "gradient boosting", "autoencoder", "reinforcement learning",
            "artificial intelligence", "emulator", "generative model", "contrastive learning", "LLM"]
ML_CATS = ["cs.LG", "cs.CV", "cs.AI", "cs.CL", "cs.IR", "stat.ML"]
ASTRO_TERMS = ["astronomy", "astronomical", "astrophysics", "astrophysical", "galaxy", "galaxies", "telescope",
               "cosmology", "cosmological", "exoplanet", "exoplanets", "solar flare", "gravitational wave",
               "supernova", "stellar", "light curves", "sky survey"]
LINK = re.compile(r"https?://(?:github\.com|gitlab\.com|huggingface\.co|zenodo\.org)/[^\s,;)\]}>]+", re.I)

SECTIONS = [s["title"] for s in yaml.safe_load((ROOT / "data" / "entries.yml").read_text(encoding="utf-8"))["sections"]
            if s.get("kind") != "links"]


# arXiv ---------------------------------------------------------------------------

def http(url, data=None, headers=None, timeout=90):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


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


def candidates(since):
    """Recent papers that match either query, newest first, submitted after `since`."""
    queries = [
        "(" + " OR ".join(f"cat:{c}" for c in ASTRO_CATS) + ") AND (" + clause("abs", ML_TERMS) + " OR " + clause("ti", ML_TERMS) + ")",
        "(" + " OR ".join(f"cat:{c}" for c in ML_CATS) + ") AND " + clause("abs", ASTRO_TERMS),
    ]
    seen = {}
    for q in queries:
        for start in (0, 200):
            batch = arxiv_api({"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending",
                               "start": start, "max_results": 200})
            for p in batch:
                if p["published"] >= since:
                    seen.setdefault(p["id"], p)
            if not batch or batch[-1]["published"] < since:
                break
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
            body = json.dumps({"model": self.name, "temperature": 0.2, "max_tokens": max_tokens,
                               "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}]}).encode()
            r = json.loads(http("https://models.github.ai/inference/chat/completions", body, {
                "Authorization": f"Bearer {self.github}", "Content-Type": "application/json",
                "Accept": "application/vnd.github+json"}))
            return r["choices"][0]["message"]["content"]
        except Exception as exc:
            detail = exc.read().decode(errors="replace")[:300] if isinstance(exc, urllib.error.HTTPError) else ""
            print(f"warning: the model request failed ({exc}) {detail}; continuing without summaries", file=sys.stderr)
            self.name = None
            return None


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
    new = [p for p in candidates(since) if p["id"] not in known]
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
