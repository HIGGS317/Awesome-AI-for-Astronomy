"""Query public Awesome AI for Astronomy and AstroAI Today data."""
import argparse
from datetime import date
import json
import re
import sys
from urllib.request import Request, urlopen


BASE = "https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/"
PAGE_DATA = re.compile(r'<script id="data" type="application/json">(.*?)</script>', re.DOTALL)


def fetch(path):
    request = Request(BASE + path, headers={"User-Agent": "astroai-research-skill/1.0"})
    with urlopen(request, timeout=15) as response:
        return response.read().decode("utf-8")


def today_page():
    match = PAGE_DATA.search(fetch("today.html"))
    if match is None:
        raise ValueError("AstroAI Today page data is unavailable")
    return json.loads(match.group(1))


def iso_date(value):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() == value:
            return value
    except ValueError:
        pass
    raise argparse.ArgumentTypeError("use YYYY-MM-DD for a calendar date")


def iso_month(value):
    iso_date(value + "-01")
    return value


def positive_int(value):
    count = int(value)
    if count < 1:
        raise argparse.ArgumentTypeError("limit must be positive")
    return count


def matches(record, terms, fields):
    searchable = " ".join(str(record.get(field, "")) for field in fields).casefold()
    return all(term.casefold() in searchable for term in terms)


def result(path, records, limit, **metadata):
    return {"source": BASE + path, **metadata, "matched": len(records), "records": records[:limit]}


def catalog(args):
    path = "entries.json"
    data = json.loads(fetch(path))
    fields = ("title", "name", "arxiv_id", "doi", "section", "subsection", "summary", "description")
    records = [
        row for row in data[args.kind]
        if matches(row, args.terms, fields)
        and (not args.section or matches(row, [args.section], ("section", "subsection")))
        and (not args.modality or args.modality.casefold() in [m.casefold() for m in row.get("modality", [])])
        and (not args.resource or args.resource in row.get("resources", []))
    ]
    return result(path, records, args.limit, kind=args.kind, generated=data["meta"]["generated"])


def today(args):
    month = args.date[:7] if args.date else args.month
    if month:
        path = f"today/archive/{month}.json"
        days = json.loads(fetch(path))["days"]
        period = args.date or month
    else:
        path = "today.html"
        days = today_page()["days"][:1]
        period = days[0]["date"] if days else None

    if args.date:
        days = [day for day in days if day["date"] == args.date]
    fields = ("id", "title", "authors", "topic", "summary", "tldr", "excerpt")
    records = [
        {**paper, "batch_date": day["date"], "url": f"https://arxiv.org/abs/{paper['id']}"}
        for day in days
        for paper in day["papers"]
        if matches(paper, args.terms, fields)
        and (not args.topic or matches(paper, [args.topic], ("topic",)))
    ]
    return result(path, records, args.limit, period=period, dates=[day["date"] for day in days])


def digest(args):
    key, anchor = ("weekly", "week") if args.kind == "week" else ("monthly", "month")
    summaries = today_page()[key]
    selected = next((item for item in summaries if not args.period or item["period"] == args.period), None)
    return {"source": BASE + "today.html#" + anchor, "period": args.period, "digest": selected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, handler in (("catalog", catalog), ("today", today)):
        command = commands.add_parser(name)
        command.add_argument("terms", nargs="*", help="case-insensitive search terms")
        command.add_argument("--limit", type=positive_int, default=10)
        command.set_defaults(handler=handler)

    catalogue = commands.choices["catalog"]
    catalogue.add_argument("--kind", choices=("papers", "links"), default="papers")
    catalogue.add_argument("--section")
    catalogue.add_argument("--modality")
    catalogue.add_argument("--resource", choices=("code", "model", "data"))

    recent = commands.choices["today"]
    period = recent.add_mutually_exclusive_group()
    period.add_argument("--date", type=iso_date)
    period.add_argument("--month", type=iso_month)
    recent.add_argument("--topic")

    summaries = commands.add_parser("digest")
    summaries.add_argument("kind", choices=("week", "month"))
    summaries.add_argument("--period", help="YYYY-Www for weeks or YYYY-MM for months")
    summaries.set_defaults(handler=digest)

    args = parser.parse_args()
    if args.command == "catalog" and args.kind == "links" and (args.modality or args.resource):
        catalogue.error("--modality and --resource apply to papers")
    try:
        data = args.handler(args)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Could not read the source: {error}\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
