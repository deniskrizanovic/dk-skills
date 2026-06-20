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

### `dod`

Full Definition of Done check for a completed implementation step. Runs traceability, Apex tests with coverage, Playwright e2e suite, and static analysis.

**Usage:** `dod step 4` or `dod capability-tag-object.md`

**What it runs:**
| Step | What |
|---|---|
| 1 | Traceability check (via `check-traceability` logic) |
| 1.5 | Playwright verification preview (`parse_playwright_assertions.py`) |
| 2 | Apex tests + coverage (`sf apex run test … \| parse_apex_results.py`) |
| 3 | Full Playwright e2e suite (`npx playwright test tests/e2e/`) |
| 4 | Static analysis (`sf code-analyzer run -s 2`) |
| 5 | FP count prompt if step unlocks new functional processes |

**Scripts:**
- `dod/parse_apex_results.py` — parses `sf apex run test --result-format json` output into Tests/Coverage/Failures tables
- `dod/parse_playwright_assertions.py` — extracts assertions from a Playwright spec file for a pre-run preview
- `dod/OUTPUT_FORMAT.md` — canonical output format reference

---

### `check-traceability`

Checks bi-directional traceability between spec files and test code for all completed implementation steps.

**What it checks:**
| Check | Direction | Description |
|---|---|---|
| All covered | Forward | Every spec scenario has `> Tested by:` or `> Deferred:` — no bare scenarios |
| Apex refs valid | Forward | Every `Tested by:` Apex reference resolves to a real method in the `.cls` file |
| e2e refs valid | Forward | Every `Tested by:` e2e reference resolves to an exact test description in the spec file |
| @spec back-refs | Reverse | Every `// @spec` comment in Apex resolves to a real feature + scenario in the named spec |
| No banned markers | Format | Flags `not yet covered` and `UI only` markers |

**No scripts** — pure Claude reasoning over spec and test files.

---

### `check-doc-consistency`

Verifies documentation layers stay in sync after a plan, design doc, or spec changes.

**What it checks:**
| Layer | Check |
|---|---|
| COSMIC arithmetic | Row sums match grand total; each FP row E+X+R+W = CFP |
| Plan FP table | Every FP in the plan exists in the COSMIC doc with matching CFP |
| LWC architecture — components | All `lwc/` dirs have a row in the architecture table |
| LWC architecture — Apex | All `@AuraEnabled` methods documented |
| Spec coverage markers | No bare/banned scenarios (`not yet covered`, `UI only`) |
| New FP coverage | Every new `@AuraEnabled` method has a corresponding FP |
| CONTEXT.md glossary | New terms from plans/specs have glossary entries |

**No scripts** — pure Claude reasoning over the project files.

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
├── check-doc-consistency/
│   └── SKILL.md
├── check-traceability/
│   └── SKILL.md
├── dod/
│   ├── SKILL.md
│   ├── OUTPUT_FORMAT.md
│   ├── parse_apex_results.py
│   └── parse_playwright_assertions.py
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
