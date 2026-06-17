# COSMIC Manuals

Drop official COSMIC PDFs into this folder, then run the indexer.

**From any directory using the SKILL_DIR pattern:**

```bash
SKILL_DIR=$(realpath ~/.claude/skills/dk-cosmic-counting-coach)
PYTHONPATH=$SKILL_DIR python3 -m scripts.index_manuals \
  $SKILL_DIR/manuals \
  $SKILL_DIR/manuals-indexed
```

The skill is non-functional until at least one PDF here has been indexed.

## Recommended manuals

Use the bootstrap command above to index PDFs in this directory

| Filename (any name works) | Source |
|---|---|
| `cosmic-measurement-manual-v5.0.pdf` | https://cosmic-sizing.org — *The COSMIC Functional Size Measurement Method, Measurement Manual v5.0* |
| `cosmic-glossary-of-terms.pdf` | https://cosmic-sizing.org — *Glossary of Terms* |
| `cosmic-guideline-salesforce.pdf` | https://cosmic-sizing.org — *Guideline for sizing Salesforce.com applications* |

Filenames are used (slugified) as the manual short-name in citations. Pick names that read well in references such as `[cosmic-measurement-manual-v5.0 §3.2.1]`.

## Notes

- PDFs are committed to the repo for convenient cloning and CI; manuals are freely distributed by COSMIC.
- The indexer is idempotent — re-running it skips PDFs whose mtime predates their existing index.
- To force a re-index, delete the corresponding subfolder under `manuals-indexed/`.
