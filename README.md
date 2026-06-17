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

---

### `tokencost-setup`

Installs per-session Claude Code token cost tracking into any project. Records token usage and USD cost to `tokencost/cost.csv` via SessionEnd/SessionStart hooks. Generates a Markdown cost report grouped by branch.

**Usage:**

```bash
# From the root of the target project:
bash /path/to/dk-skills/tokencost-setup/install.sh
```

The script is idempotent — safe to run multiple times.

**What it does:**
1. Copies `cost-tracker.py`, `generate_token_tracker.py`, `sum-cost.py` to `~/.claude/hooks/` (once, shared across all projects)
2. Creates `tokencost/cost.csv` with correct headers in the target project
3. Prompts for `branch_pattern`, `output_path`, `repo_url` and writes `tokencost/config.json`
4. Wires `SessionEnd` and `SessionStart` hooks in `.claude/settings.json`

**After install:**

```bash
# Generate the cost report
python3 ~/.claude/hooks/generate_token_tracker.py

# Quick per-branch cost summary
python3 ~/.claude/hooks/sum-cost.py
```

**Scripts:** `tokencost-setup/scripts/`
- `cost-tracker.py` — hook handler (finalize / backfill modes)
- `generate_token_tracker.py` — Markdown report generator; reads config from `tokencost/config.json`
- `sum-cost.py` — CLI aggregator; prints cost table by branch

**Note:** Add `tokencost/cost.csv` to `.gitignore` if you don't want to commit session data.

---

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
├── dk-cosmic-counting-coach/
│   ├── SKILL.md
│   ├── manuals/          # drop COSMIC PDFs here
│   ├── manuals-indexed/  # generated index (git-ignored per PDF size)
│   ├── scripts/
│   │   ├── index_manuals.py
│   │   └── chunk_by_section.py
│   └── tests/
└── tokencost-setup/
    ├── install.sh
    └── scripts/
        ├── cost-tracker.py
        ├── generate_token_tracker.py
        └── sum-cost.py
```
