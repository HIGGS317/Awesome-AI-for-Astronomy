#!/usr/bin/env python3
"""Report entries whose metadata may be out of date.

For every paper still listed as an arXiv preprint, the script reads the arXiv
record and reports
  * a journal reference or DOI added on arXiv since the entry was written,
  * a Crossref journal or proceedings record whose title and first author match,
  * a title that differs from the latest arXiv version.

The findings are candidates for a maintainer to confirm by hand. The script never
edits data/entries.yml.

Usage:
    python scripts/audit.py                  # print the Markdown report
    python scripts/audit.py --out report.md  # also write it to a file
    python scripts/audit.py --no-crossref    # skip the Crossref title search
"""
import argparse
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy"
UA = f"Awesome-AI-for-Astronomy metadata audit ({REPO})"
ARXIV_ID = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def norm(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", text.lower())


def get(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as exc:  # network errors are reported, not fatal
            if attempt == retries - 1:
                print(f"warning: {url} failed: {exc}", file=sys.stderr)
                return None
            time.sleep(5 * (attempt + 1))


def preprints(data):
    """Yield (section, entry, arXiv id) for entries still listed as arXiv preprints."""
    for sec in data["sections"]:
        if sec.get("kind") == "links":
            continue
        for node in [sec] + sec.get("subsections", []):
            for e in node.get("entries", []):
                m = ARXIV_ID.search(e["links"].get("Paper", ""))
                if m and e["venue"].lower().startswith("arxiv"):
                    yield node["title"], e, m.group(1)


def arxiv_records(ids):
    """Return ({id: {title, journal_ref, doi, first_author}}, ids whose request failed)."""
    out, failed = {}, set()
    for i in range(0, len(ids), 50):
        batch = ids[i:i + 50]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(batch), "max_results": len(batch)})
        body = get(url)
        if body:
            out.update(parse_arxiv(body))
        else:
            failed.update(batch)
        time.sleep(3)  # arXiv asks for at most one request every three seconds
    return out, failed


def parse_arxiv(body):
    out = {}
    for entry in ET.fromstring(body).findall("a:entry", NS):
        m = re.search(r"abs/(\d{4}\.\d{4,5})", entry.findtext("a:id", "", NS))
        if not m:
            continue
        author = entry.find("a:author/a:name", NS)
        out[m.group(1)] = {
            "title": " ".join(entry.findtext("a:title", "", NS).split()),
            "journal_ref": " ".join(entry.findtext("x:journal_ref", "", NS).split()),
            "doi": entry.findtext("x:doi", "", NS).strip(),
            "first_author": author.text.strip() if author is not None else "",
        }
    return out


def crossref_match(title, first_author):
    """Return a Crossref record whose title and first author family name both match."""
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
        "query.bibliographic": title, "rows": 5,
        "select": "DOI,title,container-title,type,published,author"})
    body = get(url)
    if not body:
        return None
    family = norm(first_author.split()[-1]) if first_author else ""
    for item in json.loads(body)["message"]["items"]:
        if item.get("type") not in ("journal-article", "proceedings-article"):
            continue
        if norm((item.get("title") or [""])[0]) != norm(title):
            continue
        authors = item.get("author") or []
        if family and authors and norm(authors[0].get("family", "")) != family:
            continue
        year = (item.get("published") or {}).get("date-parts", [[None]])[0][0]
        return {"doi": item["DOI"], "journal": (item.get("container-title") or [""])[0], "year": year}
    return None


def report(rows, checked, failed):
    lines = ["## Metadata audit", "",
             f"Checked {checked} entries that are listed as arXiv preprints. "
             "Each finding is a candidate; confirm it on the publisher page before editing `data/entries.yml`.", ""]
    if failed:
        lines += [f"{failed} entries could not be checked because the arXiv API did not respond.", ""]
    if not rows:
        return "\n".join(lines + ["No candidate updates were found."]) + "\n"
    lines += ["| Entry | Section | Finding |", "|:--|:--|:--|"]
    for sec, e, aid, finding in rows:
        label = e.get("name") or e["title"]
        lines.append(f"| [{label.replace('|', '/')}](https://arxiv.org/abs/{aid}) | {sec} | {finding.replace('|', '/')} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--no-crossref", action="store_true")
    args = ap.parse_args()

    data = yaml.safe_load((ROOT / "data" / "entries.yml").read_text(encoding="utf-8"))
    items = list(preprints(data))
    records, failed = arxiv_records([aid for _, _, aid in items])
    if items and not records:
        sys.exit("The arXiv API returned no records, so no report was written.")

    rows = []
    for sec, e, aid in items:
        rec = records.get(aid)
        if aid in failed:
            continue
        if not rec:
            rows.append((sec, e, aid, "No arXiv record was returned for this identifier."))
            continue
        if rec["doi"] or rec["journal_ref"]:
            parts = []
            if rec["journal_ref"]:
                parts.append(f"arXiv journal reference: {rec['journal_ref']}")
            if rec["doi"]:
                parts.append(f"arXiv DOI: [{rec['doi']}](https://doi.org/{rec['doi']})")
            rows.append((sec, e, aid, "; ".join(parts)))
        elif not args.no_crossref:
            hit = crossref_match(rec["title"], rec["first_author"])
            if hit:
                rows.append((sec, e, aid, f"Crossref match: {hit['journal']} {hit['year']}, "
                                          f"[{hit['doi']}](https://doi.org/{hit['doi']})"))
            time.sleep(0.5)
        if norm(rec["title"]) != norm(e["title"]):
            rows.append((sec, e, aid, f"Latest arXiv title: {rec['title']}"))

    text = report(rows, len(items) - len(failed), len(failed))
    print(text)
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
