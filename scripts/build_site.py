#!/usr/bin/env python3
"""Build the searchable web page from README.md.

Usage: python scripts/build_site.py [--out _site/index.html]

The README is the single source of truth. This script parses its sections,
paper entries and link lists into JSON and embeds them in site/template.html.
"""
import argparse
import datetime
import html
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {"Contents", "Contributing", "License"}

PAPER = re.compile(r"^- (?:\*\*\((?P<name>.+?)\)\*\* )?\*(?P<title>.+)\* `(?P<venue>[^`]+)`\s*$")
LINK = re.compile(r"\[\[([^\]]+)\]\(([^)\s]+)\)\]")
ITEM = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)\s*(?P<desc>.*)$")
ARXIV = re.compile(r"arxiv\.org/abs/(\d{2})(\d{2})\.\d{4,5}")
YEAR = re.compile(r"(19|20)\d{2}")


def inline_md(text):
    """Escape text and render inline links and code spans."""
    out = html.escape(text.strip(), quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: '<a href="%s">%s</a>' % (html.escape(m.group(2)), m.group(1)),
        out,
    )
    return out


def slug(text):
    s = re.sub(r"[^a-z0-9 -]", "", text.lower()).strip()
    return re.sub(r"[ -]+", "-", s)


def parse(readme):
    lines = readme.splitlines()
    title = lines[0].lstrip("# ").strip()
    intro = next(l for l in lines[1:] if l and not l.startswith("[!") and not l.startswith("!["))

    sections, h2, cur = [], None, None
    blocks, buf = [], []

    def flush_block():
        if buf and cur is not None:
            cur["_blocks"].append(list(buf))
        buf.clear()

    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            flush_block()
            level = 2 if line.startswith("## ") else 3
            name = line.split(" ", 1)[1].strip()
            if level == 2:
                h2 = name
                if name in SKIP:
                    cur = None
                    continue
            elif h2 in SKIP:
                continue
            cur = {"id": slug(name), "title": name, "level": level,
                   "parent": slug(h2) if level == 3 else None,
                   "intro": "", "entries": [], "_blocks": []}
            sections.append(cur)
            continue
        if not line.strip():
            flush_block()
        else:
            buf.append(line)
    flush_block()

    for sec in sections:
        for blk in sec.pop("_blocks"):
            m = PAPER.match(blk[0])
            if m:
                links = LINK.findall(blk[1]) if len(blk) > 1 else []
                desc = " ".join(l.strip() for l in blk[2:]) if len(blk) > 2 else ""
                venue = m.group("venue")
                year = None
                for _, url in links:
                    a = ARXIV.search(url)
                    if a:
                        year = 2000 + int(a.group(1))
                        break
                if year is None:
                    y = YEAR.search(venue)
                    year = int(y.group(0)) if y else None
                sec["entries"].append({
                    "kind": "paper",
                    "name": m.group("name") or "",
                    "title": m.group("title"),
                    "venue": venue,
                    "reviewed": not venue.lower().startswith("arxiv"),
                    "year": year,
                    "links": [{"label": l, "url": u} for l, u in links],
                    "desc": inline_md(desc),
                })
                continue
            items = [ITEM.match(l) for l in blk]
            if all(items):
                for it in items:
                    sec["entries"].append({
                        "kind": "link",
                        "name": it.group("name"),
                        "url": it.group("url"),
                        "desc": inline_md(it.group("desc")),
                    })
                continue
            if not blk[0].startswith("- ") and not blk[0].startswith("[!"):
                sec["intro"] += ("<p>%s</p>" % inline_md(" ".join(blk)))
    return title, intro, sections


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site" / "index.html"))
    args = ap.parse_args()

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    title, intro, sections = parse(readme)
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        commit = ""
    data = {
        "title": title,
        "intro": inline_md(intro),
        "repo": "https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy",
        "built": datetime.date.today().isoformat(),
        "commit": commit,
        "sections": sections,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(template.replace("/*__DATA__*/null", payload), encoding="utf-8")
    papers = sum(1 for s in sections for e in s["entries"] if e["kind"] == "paper")
    links = sum(1 for s in sections for e in s["entries"] if e["kind"] == "link")
    print(f"wrote {out} with {papers} papers and {links} links in {len(sections)} sections")


if __name__ == "__main__":
    main()
