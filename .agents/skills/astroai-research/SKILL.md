---
name: astroai-research
description: Find AI and machine learning papers, datasets, benchmarks, and software in Awesome AI for Astronomy and track recent arXiv papers with AstroAI Today. Use for astronomy literature discovery, finding reusable research resources, or checking daily, weekly, and monthly AI for Astronomy updates.
---

# AstroAI Research

Use the [curated catalogue](https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/) for existing work and reusable resources. Use [AstroAI Today](https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/today.html) for new arXiv candidates and period digests. The two sources have different inclusion processes, and appearing in Today does not imply an entry in the curated catalogue or peer review.

## Query the sources

Run [scripts/query.py](scripts/query.py) from the skill directory with Python 3.9+ and access to the public site. The script uses the standard library and needs no credentials. Pass separate search terms to match all of them, and quote a phrase to match it as written. Search English titles and terminology, using the researcher's language for the answer.

```sh
python scripts/query.py catalog "photometric redshift" --resource code --limit 5
python scripts/query.py catalog "light curve" --modality "Time series"
python scripts/query.py catalog "light curve" --kind links --section "Tools and Libraries"
python scripts/query.py today --limit 5
python scripts/query.py today --date 2026-11-10 --topic "Gravitational Waves"
python scripts/query.py today --month 2026-11 "weak lensing"
python scripts/query.py digest week
python scripts/query.py digest month --period 2026-11
```

- **Catalogue.** Search by task, object, survey, or method. Filter by section, modality, or linked resource when needed. Some entries have no modality tag, so retry without that filter when coverage matters. The `links` kind searches resources such as tools and communities.
- **Today.** Without a date, the script returns the latest available batch and reports its date. Date and month filters use the public archive. A missing batch is distinct from a published batch with no matching papers.
- **Digests.** Use the week or month summary to orient a literature scan. Retain the reported dates and whether the period is final. Open highlighted arXiv records before relying on the digest's interpretation.
- **Browser fallback.** Use the catalogue's search or its [JSON export](https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/entries.json), and the Today page's Today, This week, This month, or Archive tabs. The [RSS feed](https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/today/feed.xml) covers recent entries only.

## Use results in research

For a shortlist, include the paper title, primary link, research task, and relevant public code, data, or model links. Identify whether each candidate came from the curated catalogue or Today, and deduplicate by arXiv ID or DOI when combining them. Treat source summaries as discovery aids. Verify methods, data, metrics, numerical results, and publication status against the primary paper or publisher before making claims. Say when the answer is based on an abstract or catalogue entry.

If asked to propose a catalogue change, follow the repository's [contribution guide](https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy/blob/main/CONTRIBUTING.md). Check for duplicates before proposing an entry.
