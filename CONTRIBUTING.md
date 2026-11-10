# Contributing

Thank you for helping improve this list.

## Inclusion criteria

1. The work applies machine learning or AI methods to astronomy, astrophysics, cosmology or planetary science.
2. The paper is publicly available (arXiv, journal or proceedings).
3. At least one artifact is public, such as code, model weights, a dataset or a hosted service.
4. The work is not already listed.

Software without an accompanying paper can be added to the Tools and Libraries section as a single line linking to its official repository.

## Entry format

Place the entry in the most specific subsection and keep chronological order within it.

```markdown
- **(ShortName)** *Full Paper Title* `Venue Year`  
  [[Paper](https://arxiv.org/abs/XXXX.XXXXX)] [[GitHub](https://github.com/owner/repo)] [[Model](https://huggingface.co/owner/model)]  
  One sentence stating the method, the data and the scale.
```

Rules for the entry

- Use the arXiv abstract page for `[Paper]` when one exists.
- Confirm the arXiv identifier against the paper page or the official repository README.
- Use the confirmed peer-reviewed venue in the venue tag. Use `arXiv Year` when no venue is confirmed.
- Keep the description to one factual sentence. Report data scale and model size when available.
- End the first two lines with two spaces to force a line break.

## Pull request checklist

- [ ] Every link resolves.
- [ ] The venue and year match the paper.
- [ ] The entry follows the template above.
- [ ] One pull request adds or edits entries for one topic.
