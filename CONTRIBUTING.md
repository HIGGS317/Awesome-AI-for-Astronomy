# Contributing

Thank you for helping improve this list.

## Inclusion criteria

1. The work applies machine learning or AI methods to astronomy, astrophysics, cosmology, heliophysics or planetary science.
2. The paper is publicly available (arXiv, journal or proceedings).
3. At least one artifact is public, such as code, model weights, a dataset or a hosted service, or the paper is a survey or benchmark of clear value to the field.
4. The work is not already listed.

Software without an accompanying paper can be added to the Tools and Libraries section, linking to its official repository.

## How the list is built

All entries live in [`data/entries.yml`](data/entries.yml). `README.md` and the web page are generated from that file by [`scripts/build.py`](scripts/build.py), so please do not edit the tables in `README.md` by hand.

```bash
pip install pyyaml
python scripts/build.py          # regenerate README.md and _site/index.html
python scripts/build.py --check  # confirm README.md matches data/entries.yml
```

Pull requests are checked with `--check`, so commit the regenerated `README.md` together with your change to `data/entries.yml`.

## Entry format

Add the entry to the most specific section or subsection in `data/entries.yml`. The order inside the file does not matter, since the tables are sorted newest first by the date of the first arXiv version.

```yaml
- name: ShortName               # optional model, dataset or benchmark name
  title: 'Full Paper Title'
  venue: NeurIPS 2025           # or arXiv 2025 when no venue is confirmed
  links:
    Paper: https://arxiv.org/abs/XXXX.XXXXX
    Code: https://github.com/owner/repo
    Model: https://huggingface.co/owner/model
  desc: One sentence stating the method, the data and the scale.
  note: Oral                    # optional: Oral, Spotlight or an award, shown as a separate tag
```

Rules for the entry

- Use the arXiv abstract page for `Paper` when one exists. The date column is derived from this identifier.
- Confirm the arXiv identifier against the paper page or the official repository README.
- Use the confirmed peer-reviewed venue. Use `arXiv Year` when no venue is confirmed.
- Use a label containing `Code` for source code links, so they appear in the code column and in the code filter of the web page. Other labels such as `Journal`, `Data`, `Model` or `Project` are shown as additional links.
- Keep the description to one factual sentence. Report data scale and model size when available.
- Quote the title with single quotes when it contains a colon.

Entries in Tools and Libraries, Communities and Groups and Related Awesome Lists use `name`, `url` and `desc`.

## Pull request checklist

- [ ] Every link resolves.
- [ ] The venue and year match the paper.
- [ ] `python scripts/build.py --check` passes.
- [ ] One pull request adds or edits entries for one topic.
