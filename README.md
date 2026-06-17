# dk-skills

A collection of Claude Code skills for Salesforce development and COSMIC functional-size measurement.

## Skills

### `diff-org-changes`

Diffs a Salesforce org against local source and presents results as grouped, interpreted tables — not raw diff output.

**What it does:**
- Runs `diff_org_changes.py` against a target org alias
- Normalises known noise (flow coordinates, CDATA encoding, dashboard owners, etc.) before comparing
- Groups changes by type: Apex, Flows, Object fields, Flexipages, Validation Rules, and more
- Produces an impact summary (cosmetic / functional / metadata) and lists org-only / local-only files

**Script:** `diff-org-changes/scripts/diff_org_changes.py`

---

### `dk-cosmic-counting-coach`

Answers COSMIC functional-size measurement questions grounded exclusively in the official COSMIC manuals. No web fallback, no invented citations.

**Four modes:**
| Mode | When to use |
|---|---|
| Q&A oracle | "How should X be measured?", "Is X a Read or an Entry?" |
| Validator | Validate measurer JSON against the original source artifact |
| Rule lookup | "Quote §X.Y.Z", "Show me the rule about ..." |
| Tutor | "Teach me about ...", "Walk me through ..." |

**Setup:** Index the PDFs in `manuals/` before first use:

```bash
SKILL_DIR=$(realpath ~/.claude/skills/dk-cosmic-counting-coach)
PYTHONPATH=$SKILL_DIR python3 -m scripts.index_manuals \
  $SKILL_DIR/manuals \
  $SKILL_DIR/manuals-indexed
```

The indexer is idempotent — re-running skips PDFs whose mtime predates their existing index.

**Scripts:** `dk-cosmic-counting-coach/scripts/`
- `index_manuals.py` — indexes PDFs into heading-chunked markdown
- `chunk_by_section.py` — heading-aware PDF chunker

## Requirements

- Python 3.13+
- See `dk-cosmic-counting-coach/requirements-dev.txt` for dev dependencies

## Structure

```
dk-skills/
├── diff-org-changes/
│   ├── SKILL.md
│   └── scripts/
│       └── diff_org_changes.py
└── dk-cosmic-counting-coach/
    ├── SKILL.md
    ├── manuals/          # drop COSMIC PDFs here
    ├── manuals-indexed/  # generated index (git-ignored per PDF size)
    ├── scripts/
    │   ├── index_manuals.py
    │   └── chunk_by_section.py
    └── tests/
```
