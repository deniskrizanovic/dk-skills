---
name: dk-cosmic-cfp-count
description: >
  Measures the COSMIC functional size (CFP) of a delivery scope from a CSV of
  epics. Runs a multi-agent workflow: derives the COSMIC v5.0 rules once, measures
  every epic in parallel (one agent per epic, grounded in the cosmic-coach's
  indexed manuals), computes the roll-up, and renders a markdown report. Use when
  someone hands you an epics CSV and wants a COSMIC/CFP count, functional-size
  measurement, or a movement-level sizing of a Salesforce scope.
metadata:
  category: Salesforce / COSMIC
  version: 0.1.0
---

# COSMIC CFP Count (from an epics CSV)

Turn a CSV of epics into a full COSMIC functional-size measurement: a
`cosmic-count.json` (canonical) plus a human-readable markdown report, with
every data movement enumerated, cited to the official COSMIC v5.0 manuals, and
gaps surfaced instead of guessed.

> **Path resolution.** At session start resolve the skill directory once:
> ```bash
> SKILL_DIR=$(realpath ~/.claude/skills/dk-cosmic-cfp-count)
> ```
> All `scripts/` references below mean `$SKILL_DIR/scripts/`.

## Dependency

Requires the **`dk-cosmic-counting-coach`** skill (invoked as `cosmic-coach`) —
its indexed COSMIC v5.0 manuals are the sole rule authority. It must be installed
(symlinked in `~/.claude/skills/`) or the Prime stage cannot ground the rules.

## Input

A CSV of epics with (at least) these columns — header names are matched
case-insensitively, aliases accepted:

| Column | Required | Notes |
|---|---|---|
| Epic ID | yes | e.g. `E01` |
| Epic Name | yes | |
| Description | yes | the requirement text the measurement rests on — richer is better |
| Confidence | no | `Confirmed` / `Assumed` / `Unknown`; default `Assumed` |
| Depends On | no | `;`- or `,`-separated epic IDs |

Any extra columns pass through as context to the measuring agent.

## Execution

### Step 1 — CSV → workflow args

```bash
python3 "$SKILL_DIR/scripts/epics_csv_to_args.py" <path/to/epics.csv> > /tmp/cfp-args.json
```

This emits `{"epics":[...]}`. Read the file and confirm the epic count with the
user before the (token-heavy) run.

### Step 2 — run the measurement workflow

Invoke the Workflow tool with the script and the parsed args:

```
Workflow({
  scriptPath: "<SKILL_DIR>/scripts/cosmic-cfp-count.workflow.js",
  args: <the parsed {epics:[...]} object>
})
```

(Pass `args` as the actual JSON value, not a string.) The workflow:

1. **Prime** — one agent asks the coach for the recurring COSMIC rules
   (external round-trip, CRUD movements, single confirmation/error Exit,
   functional-process boundaries, single-triggering-Entry) with verbatim
   citations, and returns a compact primer. Derived **once**, injected into
   every measure agent — the main token saver.
2. **Measure** — one agent per epic (medium effort, auto-throttled fan-out)
   decomposes each functional process into E/X/R/W
   movements, applying the primer and grepping the manuals only for
   adjudications the primer doesn't cover. Vague requirements become
   `CG-<epic>-NN` measurement gaps, never invented numbers.
3. **Synthesize** — JS computes the roll-up (Confirmed floor → measured total,
   gap count) and assembles the full report object. The workflow returns it as
   `result.cosmicCount` — no agent re-serializes it (an LLM echoing the whole
   object costs tokens twice and can silently alter a value).

After the workflow returns, write `result.cosmicCount` **verbatim** to
`data/cosmic-count.json` (pretty-printed, 2-space indent) with the Write tool.
If `result.epicsFailed` is non-empty, surface those epic IDs to the user — they
were excluded from the roll-up and the count is partial.

### Output format — two schemas (camelCase)

`data/cosmic-count.json` is governed by two JSON Schemas that ship in the skill
directory:

- **`cosmic_count_report.schema.json`** (`CosmicCountReport`) — the report
  envelope for the whole scope: `disclaimer`, `rulesPrimer`, `rollUp`
  (`projectCfpCountable`, `cfpRange` `[confirmedFloor, measuredTotal]`,
  `epicsMeasured`, `epicsTotal`, `countableEpics`, `epicsRestingOnAssumptions`),
  `epics[]` (`epicId`, `epicName`, `confidence`, `epicCfp`, `caveats`,
  `functionalProcesses`, `gaps`), and `measurementGaps[]`.
- **`cosmic_measure_output.schema.json`** (`CosmicMeasureOutput`) — the child
  unit, reused **verbatim** from the code-analysis COSMIC measurer. Each
  `epics[].functionalProcesses[]` item is a standalone `CosmicMeasureOutput`:
  `functionalProcessId`, `artifact` `{type, name}`, optional `cfp`, and
  `dataMovements[]` (each `name`, `order`, `movementType` E/X/R/W,
  `dataGroupRef`, and optional rule `note`/`citation`). The parent `$ref`s the
  child so every FP block validates on its own.

> **Breaking change.** The output migrated from ad-hoc snake_case to camelCase
> aligned with the child schema: `roll_up`→`rollUp`, `epic_cfp`→`epicCfp`,
> `functional_processes`→`functionalProcesses`, movement `type`→`movementType`,
> `data_group`→`dataGroupRef`, `gap_id`→`gapId`, `rules_primer`→`rulesPrimer`,
> etc. Per-process CFP is the child's optional `cfp` field, falling back to
> `len(dataMovements)` (1 movement = 1 CFP). Proposal-grain measurements omit
> the child's `implementationType`/`isApiCall` (now optional — no source code to
> derive them from). Any pre-existing snake_case reader must migrate.

### Step 3 — render the markdown report

```bash
python3 "$SKILL_DIR/scripts/render_markdown.py" data/cosmic-count.json outputs/artifacts/cosmic-count.md
```

Surface both output paths to the user as inline-backtick absolute paths.

## Guardrails

- **The manuals are the only rule authority.** Agents never decide a COSMIC rule
  from training — they cite `manuals-indexed/<slug>/<file>.md#L..` via the coach.
- **Gaps over guesses.** A requirement too vague to size becomes a measurement
  gap with a CFP swing, not a fabricated number.
- **Roll-up computed in code**, not by an LLM — the JS sums it; the agent only
  serializes. Numbers are reproducible from the JSON.
- **Approximate early measurement.** CFP from proposal-grain requirements is per
  COSMIC Part 2 — not a code-verified count. The disclaimer travels in the output.
- This is a standalone measurement; it does **not** touch other project data
  files (e.g. gaps, estimates).
