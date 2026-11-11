#!/usr/bin/env python3
"""Generate README.md and the web page from data/entries.yml.

Usage:
    python scripts/build.py                 # write README.md and _site/index.html
    python scripts/build.py --check         # exit with status 1 if README.md is out of date

Requires PyYAML (pip install pyyaml).
"""
import argparse
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
ARXIV = re.compile(r"arxiv\.org/abs/(\d{2})(\d{2})\.\d{4,5}")
YEAR = re.compile(r"(?:19|20)\d{2}")
MDLINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


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
    errors = []
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
                "reviewed": not e["venue"].lower().startswith("arxiv"),
                "year": y or None,
                "date": f"{y}.{m:02d}" if m else str(y),
                "sort": y * 100 + m,
                "primary": e["links"][primary_label(e)],
                "links": [{"label": k, "url": v} for k, v in e["links"].items()],
                "desc": inline_html(e["desc"]),
            })
        entries.sort(key=lambda x: x.get("sort", 0), reverse=True)
        secs.append({
            "id": slug(node["title"]), "title": node["title"], "level": 3 if sub else 2,
            "parent": slug(sec["title"]) if sub else None,
            "intro": inline_html(node["intro"]) if node.get("intro") else "",
            "entries": entries,
        })
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        commit = ""
    return {"repo": REPO, "built": datetime.date.today().isoformat(), "commit": commit, "sections": secs}


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

    payload = json.dumps(site_data(data), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    out = pathlib.Path(args.site)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(template.replace("/*__DATA__*/null", payload), encoding="utf-8")
    print(f"wrote README.md and {out}")


if __name__ == "__main__":
    main()
