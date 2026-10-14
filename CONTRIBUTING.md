# Contributing

New papers, corrected metadata and better resource links are welcome. Please open an issue or pull request with an original publication, author project page or other primary source.

## Adding a paper

1. Add one entry to `data/papers.json`. Use a unique stable `id` and an existing topic. Keep the full original title, an accurate year and venue, and an HTTPS paper URL.
2. Set `publication_status` to `published`, `accepted`, `workshop` or `preprint`. Do not turn an arXiv preprint into a conference paper without a source confirming acceptance. Use `publication_note` for online, issue and preprint date differences.
3. Add a repository or project link only when its relationship to the paper is supported by the author page, paper or repository README. Empty or guessed links should be omitted. Record repository availability in `data/repository-checks.json`, including the check date and scope. Repository existence does not establish released weights, a permissive license or reproducibility.
4. Write short Chinese notes about the method, contribution and limitations in `notes_zh`. Set `review_status` honestly: selected paper sections reviewed or abstract only. Keep a method claim within the scope actually reviewed. For uncertain candidates, use `data/watchlist.json` instead of the main list.
5. Classify `downstream_evidence_type`: `construction`, `predicted`, `gt`, `payload`, `joint`, `generation`, `uncertain` or `survey`. State clearly whether a downstream method uses manual graphs, visual features or the original video.
6. Regenerate and check the lists:

```sh
python scripts/build_catalog.py
python scripts/build_catalog.py --check
```

Commit the JSON change and its generated Markdown together. Add a source-derived BibTeX entry to `references.bib` when available; do not invent missing authors or venues.

## Corrections and resources

Please provide the paper ID, the incorrect field or broken link, and a primary source for the correction. When reporting code availability, distinguish implementation files, trained weights, dataset access and licensing. A repository containing only annotations should not be described as a complete model release.

This repository links to publications and resources. Please contribute catalogue text and links rather than paper PDFs, extracted full text, datasets, model weights, credentials, private correspondence or personal research plans.
