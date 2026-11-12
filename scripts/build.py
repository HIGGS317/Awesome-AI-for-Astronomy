#!/usr/bin/env python3
"""Generate README.md and the web page from data/entries.yml.

Usage:
    python scripts/build.py                 # write README.md and the web page in _site/
    python scripts/build.py --check         # exit with status 1 if README.md is out of date

Besides index.html, the site directory receives style.css, entries.json, papers.csv, sitemap.xml
and the AstroAI Today page (today.html, today/feed.xml and today/archive/<month>.json),
built from data/today/ by scripts/today.py.

Requires PyYAML (pip install pyyaml).
"""
import argparse
import csv
import email.utils
import shutil
import datetime
import html
import json
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy"
PAGE = "https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/"
ARXIV = re.compile(r"arxiv\.org/abs/(\d{2})(\d{2})\.\d{4,5}")
YEAR = re.compile(r"(?:19|20)\d{2}")
MDLINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
ARXIV_ID = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
DOI = re.compile(r"doi\.org/(10\.\d{4,9}/\S+)$")
CONFERENCES = re.compile(r"^(NeurIPS|ICML|ICLR|ACL|EMNLP|NAACL|AAAI|IJCAI|CVPR|ICCV|ECCV|COLM|KDD|ICECET|EUSIPCO)\b")
# Observation or data modalities accepted in the optional modality field.
MODALITIES = ["Images", "Spectra", "Data cubes", "Time series", "Tabular", "Text", "Point clouds", "Simulations"]
HF_MODEL = re.compile(r"huggingface\.co/(?!datasets/|spaces/|papers/)[^/]+(/[^/]+)?/?$")


def slug(text):
    s = re.sub(r"[^\w\- ]", "", text.lower()).strip()
    return s.replace(" ", "-")


def date_of(e):
    """Return (year, month) from the first arXiv link, else (year, 0) from the venue."""
    for url in e["links"].values():
        m = ARXIV.search(url)
        if m:
            return 2000 + int(m.group(1)), int(m.group(2))
    y = YEAR.search(e["venue"])
    return (int(y.group(0)), 0) if y else (0, 0)


def primary_label(e):
    for lab in ("Paper", "Journal"):
        if lab in e["links"]:
            return lab
    return next(iter(e["links"]))


def is_code(label):
    return "code" in label.lower()


def pub_type(venue):
    """Classify a venue string as Preprint, Workshop, Conference or Journal."""
    if venue.lower().startswith("arxiv"):
        return "Preprint"
    if "workshop" in venue.lower():
        return "Workshop"
    if CONFERENCES.match(venue):
        return "Conference"
    return "Journal"


def resources(e):
    """Return the kinds of public artifacts linked from a paper: code, model and data."""
    out = set()
    for label, url in e["links"].items():
        low = label.lower()
        if is_code(label):
            out.add("code")
        if re.search(r"model|weights|checkpoint", low) or (not is_code(label) and HF_MODEL.search(url)):
            out.add("model")
        if re.search(r"data|kaggle", low) or (not is_code(label) and re.search(r"huggingface\.co/datasets/|zenodo\.org|kaggle\.com", url)):
            out.add("data")
    return [k for k in ("code", "model", "data") if k in out]


def arxiv_id(e):
    m = ARXIV_ID.search(e["links"].get("Paper", ""))
    return m.group(1) if m else ""


def doi_of(e):
    m = DOI.search(e["links"].get("Journal", ""))
    return m.group(1) if m else ""


def md_escape(text):
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text)


def plain(text):
    return MDLINK.sub(r"\1", text).replace("`", "")


def tooltip(text):
    return plain(text).replace('"', "'").replace("|", "/")


def walk(data):
    """Yield (section, subsection or None) nodes in order."""
    for sec in data["sections"]:
        yield sec, None
        for sub in sec.get("subsections", []):
            yield sec, sub


def validate(data):
    """Check required fields and reject papers listed twice (same title, arXiv link or DOI)."""
    errors = []
    seen = {}
    for sec, sub in walk(data):
        node = sub or sec
        for e in node.get("entries", []):
            where = f"{sec['title']}{' / ' + sub['title'] if sub else ''}"
            if sec.get("kind") == "links":
                for k in ("name", "url", "desc"):
                    if not e.get(k):
                        errors.append(f"{where}: link entry missing {k}: {e}")
            else:
                for k in ("title", "venue", "links", "desc"):
                    if not e.get(k):
                        errors.append(f"{where}: paper missing {k}: {e.get('title', e)}")
                if e.get("title"):
                    key = re.sub(r"[^a-z0-9]", "", e["title"].lower())
                    seen.setdefault(("title", key), []).append(where)
                mods = e.get("modality", [])
                if not isinstance(mods, list) or any(m not in MODALITIES for m in mods):
                    errors.append(f"{where}: modality must be a list drawn from {MODALITIES}: {e['title']}")
                for lab in ("Paper", "Journal"):
                    url = (e.get("links") or {}).get(lab)
                    if url:
                        key = url.lower().rstrip("/").replace("http://", "https://")
                        seen.setdefault((lab, key), []).append(where)
    for (kind, key), places in seen.items():
        if len(places) > 1:
            errors.append(f"duplicate {kind} {key} in: {'; '.join(places)}")
    if errors:
        sys.exit("\n".join(errors))


# README ----------------------------------------------------------------------

def paper_table(entries):
    rows = ["| Date | Paper | Venue | Code | Links |", "|:--|:--|:--|:--|:--|"]
    for e in sorted(entries, key=date_of, reverse=True):
        y, m = date_of(e)
        date = f"{y}.{m:02d}" if m else str(y)
        show = e.get("name") and not e["title"].lower().startswith(e["name"].lower())
        name = f"**{md_escape(e['name'])}** " if show else ""
        p = primary_label(e)
        title = f"[{md_escape(e['title'])}]({e['links'][p]} \"{tooltip(e['desc'])}\")"
        code = " ".join(f"[{lab}]({u})" for lab, u in e["links"].items() if is_code(lab))
        other = " ".join(f"[{lab}]({u})" for lab, u in e["links"].items() if lab != p and not is_code(lab))
        venue = md_escape(e["venue"])
        if not e["venue"].lower().startswith("arxiv"):
            venue = f"**{venue}**"
        if e.get("note"):
            venue += f" `{md_escape(e['note'])}`"
        rows.append(f"| {date} | {name}{title} | {venue} | {code or '-'} | {other or '-'} |")
    return "\n".join(rows)


def link_table(entries):
    rows = ["| Name | Description |", "|:--|:--|"]
    for e in entries:
        rows.append(f"| [{md_escape(e['name'])}]({e['url']}) | {e['desc'].replace('|', '/')} |")
    return "\n".join(rows)


def readme(data):
    papers = sum(len(n.get("entries", [])) for s, sub in walk(data) for n in [sub or s] if s.get("kind") != "links")
    tools = next(len(s["entries"]) for s in data["sections"] if s["title"] == "Tools and Libraries")
    head = (ROOT / "templates" / "README.head.md").read_text(encoding="utf-8")
    head = head.replace("{{PAPERS}}", str(papers)).replace("{{TOOLS}}", str(tools))
    tail = (ROOT / "templates" / "README.tail.md").read_text(encoding="utf-8")

    toc = ["## Contents", ""]
    for sec in data["sections"]:
        toc.append(f"- [{sec['title']}](#{slug(sec['title'])})")
        for sub in sec.get("subsections", []):
            toc.append(f"  - [{sub['title']}](#{slug(sub['title'])})")
    body = []
    top = '<p align="right"><a href="#contents">Back to contents</a></p>'
    for i, sec in enumerate(data["sections"]):
        if i:
            body += [top, ""]
        body += [f"## {sec['title']}", ""]
        if sec.get("intro"):
            body += [sec["intro"], ""]
        if sec.get("entries"):
            table = link_table if sec.get("kind") == "links" else paper_table
            body += [table(sec["entries"]), ""]
        for sub in sec.get("subsections", []):
            body += [f"### {sub['title']}", ""]
            if sub.get("intro"):
                body += [sub["intro"], ""]
            body += [paper_table(sub["entries"]), ""]
    return head.rstrip("\n") + "\n\n" + "\n".join(toc) + "\n\n" + "\n".join(body) + "\n" + tail


# Web page ----------------------------------------------------------------------

def inline_html(text):
    out = html.escape(text.strip(), quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return MDLINK.sub(lambda m: '<a href="%s">%s</a>' % (html.escape(m.group(2)), m.group(1)), out)


def built_info():
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        commit = ""
    return datetime.date.today().isoformat(), commit


def site_data(data):
    secs = []
    for sec, sub in walk(data):
        node = sub or sec
        entries = []
        for e in node.get("entries", []):
            if sec.get("kind") == "links":
                entries.append({"kind": "link", "name": e["name"], "url": e["url"], "desc": inline_html(e["desc"])})
                continue
            y, m = date_of(e)
            entries.append({
                "kind": "paper",
                "name": e.get("name", ""),
                "title": e["title"],
                "venue": e["venue"],
                "type": pub_type(e["venue"]),
                "reviewed": pub_type(e["venue"]) != "Preprint",
                "note": e.get("note", ""),
                "year": y or None,
                "date": f"{y}.{m:02d}" if m else str(y),
                "sort": y * 100 + m,
                "primary": e["links"][primary_label(e)],
                "links": [{"label": k, "url": v} for k, v in e["links"].items()],
                "res": resources(e),
                "mod": e.get("modality", []),
                "desc": inline_html(e["desc"]),
            })
        entries.sort(key=lambda x: x.get("sort", 0), reverse=True)
        secs.append({
            "id": slug(node["title"]), "title": node["title"], "level": 3 if sub else 2,
            "parent": slug(sec["title"]) if sub else None,
            "intro": inline_html(node["intro"]) if node.get("intro") else "",
            "entries": entries,
        })
    built, commit = built_info()
    return {"repo": REPO, "built": built, "commit": commit, "modalities": MODALITIES, "sections": secs}


def static_html(site):
    """Render the full list as plain HTML so the page is readable and indexable without JavaScript.

    The markup mirrors the rows that the script in site/template.html renders, so the
    page does not change appearance when the script takes over.
    """
    esc = lambda t: html.escape(str(t), quote=True)
    cols = ('<div class="cols" aria-hidden="true"><span>Date</span><span>Paper</span><span>Venue</span>'
            '<span class="h-links">Code and resources</span></div>')

    def paper_row(e):
        name = e["name"] if e["name"] and not e["title"].lower().startswith(e["name"].lower()) else ""
        pills = [f'<a class="pill code" href="{esc(l["url"])}">{esc(l["label"])}</a>' for l in e["links"] if is_code(l["label"])]
        pills += [f'<a class="pill" href="{esc(l["url"])}">{esc(l["label"])}</a>' for l in e["links"] if not is_code(l["label"])]
        tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in e["mod"])
        return ('<div class="row"><span class="date">' + esc(e["date"]) + '</span><div class="paper">'
                + (f'<span class="nm">{esc(name)}</span>' if name else "")
                + f'<a class="ttl" href="{esc(e["primary"])}">{esc(e["title"])}</a>'
                + (f'<span class="tags">{tags}</span>' if tags else "")
                + f'<p class="sum">{e["desc"]}</p></div>'
                + f'<div class="vcell"><span class="venue{" rev" if e["reviewed"] else ""}">{esc(e["venue"])}</span>'
                + (f'<span class="note">{esc(e["note"])}</span>' if e["note"] else "")
                + '</div><div class="links">' + "".join(pills) + "</div></div>")

    def link_row(e):
        return f'<div class="lrow"><a href="{esc(e["url"])}">{esc(e["name"])}</a><span>{e["desc"]}</span></div>'

    def block(entries):
        paper = entries[0]["kind"] == "paper"
        return (cols if paper else "") + '<div class="rows">' + "".join(paper_row(e) if paper else link_row(e) for e in entries) + "</div>"

    def n(k):
        return f"{k} {'entry' if k == 1 else 'entries'}"

    out = []
    secs = site["sections"]
    for top in [s for s in secs if not s["parent"]]:
        subs = [s for s in secs if s["parent"] == top["id"]]
        k = len(top["entries"]) + sum(len(s["entries"]) for s in subs)
        if not k:
            continue
        out.append(f'<section class="sec" id="{top["id"]}"><div class="sechead"><h2>{esc(top["title"])}</h2><span class="n">{n(k)}</span></div>')
        if top["intro"]:
            out.append(f'<p class="secintro">{top["intro"]}</p>')
        if top["entries"]:
            out.append(block(top["entries"]))
        for sub in subs:
            if sub["entries"]:
                out.append(f'<div class="subhead" id="{sub["id"]}"><h3>{esc(sub["title"])}</h3><span class="n">{n(len(sub["entries"]))}</span></div>')
                out.append(block(sub["entries"]))
        out.append("</section>")
    return "".join(out)


def json_ld(site, papers):
    built = site["built"]
    doc = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "Awesome AI for Astronomy",
        "description": ("A curated index of papers, models, datasets, benchmarks and software for machine learning "
                        f"in astronomy, astrophysics, cosmology, heliophysics and planetary science, with {papers} papers."),
        "url": PAGE,
        "sameAs": REPO,
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "isAccessibleForFree": True,
        "creator": {"@type": "Person", "name": "Xin-Yu Xiao", "url": "https://github.com/Xin-YuXiao"},
        "keywords": ["astronomy", "astrophysics", "machine learning", "deep learning", "foundation models", "benchmarks"],
        "dateModified": built,
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": PAGE + "entries.json"},
            {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": PAGE + "papers.csv"},
        ],
    }
    return json.dumps(doc, ensure_ascii=False, indent=1).replace("</", "<\\/")


# Data export -------------------------------------------------------------------

def export_records(data):
    """Return (papers, links) as flat records for entries.json and papers.csv."""
    papers, links = [], []
    for sec, sub in walk(data):
        node = sub or sec
        for e in node.get("entries", []):
            if sec.get("kind") == "links":
                links.append({"section": sec["title"], "name": e["name"], "url": e["url"], "description": plain(e["desc"])})
                continue
            y, m = date_of(e)
            papers.append({
                "section": sec["title"],
                "subsection": sub["title"] if sub else "",
                "name": e.get("name", ""),
                "title": e["title"],
                "venue": e["venue"],
                "publication_type": pub_type(e["venue"]),
                "note": e.get("note", ""),
                "year": y or None,
                "month": m or None,
                "arxiv_id": arxiv_id(e),
                "doi": doi_of(e),
                "url": e["links"][primary_label(e)],
                "code": [u for k, u in e["links"].items() if is_code(k)],
                "links": e["links"],
                "resources": resources(e),
                "modality": e.get("modality", []),
                "summary": plain(e["desc"]),
            })
    return papers, links


def write_exports(data, outdir):
    papers, links = export_records(data)
    built, commit = built_info()
    meta = {"title": "Awesome AI for Astronomy", "source": REPO, "page": PAGE, "license": "CC0-1.0",
            "generated": built, "commit": commit, "papers": len(papers), "links": len(links)}
    (outdir / "entries.json").write_text(
        json.dumps({"meta": meta, "papers": papers, "links": links}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    fields = ["section", "subsection", "name", "title", "venue", "publication_type", "note", "year", "month",
              "arxiv_id", "doi", "url", "code", "other_links", "resources", "modality", "summary"]
    with open(outdir / "papers.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for p in papers:
            row = {k: p.get(k, "") for k in fields}
            row["code"] = " ".join(p["code"])
            row["other_links"] = " ".join(f"{k}={u}" for k, u in p["links"].items() if not is_code(k) and u != p["url"])
            row["resources"] = ";".join(p["resources"])
            row["modality"] = ";".join(p["modality"])
            row["year"] = p["year"] or ""
            row["month"] = p["month"] or ""
            w.writerow(row)

    (outdir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{PAGE}</loc><lastmod>{built}</lastmod></url>\n"
        f"  <url><loc>{PAGE}today.html</loc><lastmod>{built}</lastmod></url>\n"
        "</urlset>\n", encoding="utf-8")
    return len(papers)


# AstroAI Today ------------------------------------------------------------------

TODAY = ROOT / "data" / "today"
GREEK = dict(zip("alpha beta gamma delta epsilon varepsilon zeta eta theta lambda mu nu xi pi rho sigma tau phi varphi chi psi omega "
                 "Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega".split(), "αβγδεεζηθλμνξπρστφφχψωΓΔΘΛΞΠΣΦΨΩ"))
TEX_SYMBOLS = {"sim": "~", "approx": "≈", "times": "×", "pm": "±", "odot": "⊙", "leq": "≤", "geq": "≥", "le": "≤", "ge": "≥",
               "rm": "", "mathrm": "", "textrm": "", "it": "", "mathit": "", ",": " ", "!": "", "-": "-"}


def tex_title(text):
    """Render the simple inline math of arXiv titles, such as Ly$\\alpha$ or $z\\sim2$, as plain Unicode.
    Math that still contains a TeX command after the substitutions is left as it is."""
    def inline(m):
        body = re.sub(r"\\([A-Za-z]+|[,!-])", lambda c: GREEK.get(c.group(1), TEX_SYMBOLS.get(c.group(1), c.group(0))), m.group(1))
        body = re.sub(r"[_^]\{?([^{}]*)\}?", r"\1", body).replace("{", "").replace("}", "")
        return m.group(0) if "\\" in body else body
    return re.sub(r"\$([^$]{1,60})\$", inline, text)
TODAY_FIELDS = ("id", "title", "authors", "n_authors", "primary", "topic", "summary", "model", "tldr", "excerpt",
                "links", "published")


def today_site(data, outdir):
    """Write today.html, the monthly archive files and the RSS feed. Returns the number of days."""
    load = lambda f: json.loads(f.read_text(encoding="utf-8"))
    days = []
    for f in sorted((TODAY / "daily").glob("*.json"), reverse=True):
        day = load(f)
        papers = [{k: p[k] for k in TODAY_FIELDS if k in p} for p in day["papers"] if p.get("relevant") is not False]
        for p in papers:
            p["title"] = tex_title(p["title"])
        days.append({"date": day["date"], "papers": papers, "model": day.get("model")})
    weekly = [load(f) for f in sorted((TODAY / "weekly").glob("*.json"), reverse=True)]
    monthly = [load(f) for f in sorted((TODAY / "monthly").glob("*.json"), reverse=True)]

    arch = outdir / "today" / "archive"
    arch.mkdir(parents=True, exist_ok=True)
    months = sorted({d["date"][:7] for d in days}, reverse=True)
    for m in months:
        (arch / f"{m}.json").write_text(json.dumps(
            {"month": m, "days": [{"date": d["date"], "papers": d["papers"]} for d in days if d["date"].startswith(m)]},
            ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    items = []
    for d in days[:7]:
        for p in d["papers"]:
            when = email.utils.format_datetime(datetime.datetime.fromisoformat(d["date"] + "T06:00:00+00:00"))
            short = p.get("summary") or p.get("tldr")
            text = f"TL;DR {short}" if short else p.get("excerpt", "")
            items.append(
                f"<item><title>{html.escape(p['title'])}</title><link>https://arxiv.org/abs/{p['id']}</link>"
                f"<guid isPermaLink=\"true\">https://arxiv.org/abs/{p['id']}</guid><pubDate>{when}</pubDate>"
                f"<description>{html.escape(text)}</description></item>")
    (outdir / "today" / "feed.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
        f"<title>AstroAI Today</title><link>{PAGE}today.html</link>"
        "<description>New arXiv papers that apply machine learning to astronomy, with one-sentence summaries.</description>"
        + "".join(items) + "</channel></rss>\n", encoding="utf-8")

    built, _ = built_info()
    sections = [s["title"] for s in data["sections"] if s.get("kind") != "links"]
    payload = {"built": built, "model": next((d["model"] for d in days if d.get("model")), None),
               "sections": sections, "days": days[:45], "weekly": weekly, "monthly": monthly, "months": months}
    page = (ROOT / "site" / "today.html").read_text(encoding="utf-8")
    key = "/*__TODAY__*/null"
    assert key in page, key
    page = page.replace(key, json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    (outdir / "today.html").write_text(page, encoding="utf-8")
    return len(days)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if README.md is out of date")
    ap.add_argument("--site", default=str(ROOT / "_site" / "index.html"))
    args = ap.parse_args()

    data = yaml.safe_load((ROOT / "data" / "entries.yml").read_text(encoding="utf-8"))
    validate(data)
    text = readme(data)
    target = ROOT / "README.md"
    if args.check:
        if target.read_text(encoding="utf-8") != text:
            sys.exit("README.md is out of date. Run python scripts/build.py and commit the result.")
        print("README.md is up to date.")
        return
    target.write_text(text, encoding="utf-8")

    out = pathlib.Path(args.site)
    out.parent.mkdir(parents=True, exist_ok=True)
    papers = write_exports(data, out.parent)
    site = site_data(data)
    payload = json.dumps(site, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    for key, value in (("/*__DATA__*/null", payload), ("<!--__STATIC__-->", static_html(site)),
                       ("/*__LD__*/", json_ld(site, papers))):
        assert key in page, key
        page = page.replace(key, value)
    out.write_text(page, encoding="utf-8")
    shutil.copyfile(ROOT / "site" / "style.css", out.parent / "style.css")
    n = today_site(data, out.parent)
    print(f"wrote README.md, {out}, today.html ({n} days) and the data files in {out.parent}")


if __name__ == "__main__":
    main()
