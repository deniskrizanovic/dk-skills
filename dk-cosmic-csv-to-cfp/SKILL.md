---
name: dk-cosmic-csv-to-cfp
description: >
  Measures the COSMIC functional size (CFP) of a delivery scope from a CSV of
  epics. Runs a multi-agent workflow: reads the cosmic-coach's shipped COSMIC
  v5.0 rules primer, measures every epic in parallel (one agent per epic, grounded
  in the coach's indexed manuals), computes the roll-up, and renders a markdown
  report. Use when
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
> SKILL_DIR=$(realpath ~/.claude/skills/dk-cosmic-csv-to-cfp)
> ```
> All `scripts/` references below mean `$SKILL_DIR/scripts/`.

## Dependency

Requires the **`dk-cosmic-counting-coach`** skill (invoked as `cosmic-coach`) —
its indexed COSMIC v5.0 manuals are the sole rule authority, and its shipped
`rules-primer.md` grounds the recurring rules. It must be installed (symlinked in
`~/.claude/skills/`); the workflow **hard-fails** without the coach's primer.

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

### Step 1 — CSV → workflow args, and resolve the output directory

```bash
python3 "$SKILL_DIR/scripts/epics_csv_to_args.py" <path/to/epics.csv> > /tmp/cfp-args.json
```

This emits `{"epics":[...]}`. Read the file and confirm the epic count with the
user before the (token-heavy) run.

**Resolve `OUT_DIR` — where the outputs go.** Default to the parent directory of
the input CSV:

```bash
OUT_DIR=$(dirname "<path/to/epics.csv>")
```

If the user named an output directory, use that instead (`mkdir -p` it). Both
artifacts write **directly** into `OUT_DIR` — `cosmic-count.json` and
`cosmic-count.md`, side by side. **Never** write inside the skill directory
(`$SKILL_DIR`) and **never** recreate the old `data/` or `outputs/artifacts/`
subdirectories. If `OUT_DIR` is not writable, surface the error and ask the user
for an alternate directory.

### Step 2 — read the coach primer, then run the measurement workflow

**Read the coach's rules primer on the main thread.** Workflow scripts have no
filesystem access, so the main thread reads the file and passes its contents in.
Resolve the coach skill directory and read its primer:

```bash
COACH_DIR=$(realpath ~/.claude/skills/dk-cosmic-counting-coach)
cat "$COACH_DIR/rules-primer.md"
```

Capture the full file contents as the `primer` string. If the file is missing,
the coach is not installed or its primer was never generated — stop and install
the coach / regenerate its primer (see the coach's *Regenerate the rules primer*
step). Do **not** invent a primer.

Invoke the Workflow tool with the script and the parsed args **plus the primer**:

```
Workflow({
  scriptPath: "<SKILL_DIR>/scripts/cosmic-csv-to-cfp.workflow.js",
  args: { epics: [...], primer: "<full contents of the coach's rules-primer.md>" }
})
```

(Pass `args` as the actual JSON value, not a string.) The workflow **hard-fails**
before any measure agent if `args.primer` is absent or empty. It then:

1. **Measure** — one agent per epic (medium effort, auto-throttled fan-out)
   decomposes each functional process into E/X/R/W movements, applying the
   supplied primer (the coach's shipped, version-stamped rules) and grepping the
   manuals only for adjudications the primer doesn't cover. Vague requirements
   become `CG-<epic>-NN` measurement gaps, never invented numbers. Injecting the
   primer once into every agent — instead of re-deriving it per run — is the main
   token saver and makes `rulesPrimer` provenance deterministic (see the coach's
   ADR 0002).
2. **Synthesize** — JS computes the roll-up (Confirmed floor → measured total,
   gap count) and assembles the full report object. The workflow returns it as
   `result.cosmicCount` — no agent re-serializes it (an LLM echoing the whole
   object costs tokens twice and can silently alter a value).

After the workflow returns, write `result.cosmicCount` **verbatim** to
`$OUT_DIR/cosmic-count.json` (pretty-printed, 2-space indent) with the Write tool.
If `result.epicsFailed` is non-empty, surface those epic IDs to the user — they
were excluded from the roll-up and the count is partial.

### Output format — two schemas (camelCase)

`$OUT_DIR/cosmic-count.json` is governed by two JSON Schemas that ship in the skill
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
  `dataGroupRef`, and optional rule `note`/`citation`), and an optional
  `dataGroups[]` — one `{name, description}` per DISTINCT data group / object of
  interest the process touches (deduplicated by name; `name` aligns with the
  `dataMovements[].dataGroupRef` values, `description` is an authored gloss). The
  parent `$ref`s the child so every FP block validates on its own.

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
python3 "$SKILL_DIR/scripts/render_markdown.py" "$OUT_DIR/cosmic-count.json" "$OUT_DIR/cosmic-count.md"
```

The report includes a top-level **Data groups** catalog (after the per-epic
summary, before per-epic detail). It is keyed by data group **name** — one row
per distinct name, sorted alphabetically. Each row lists the using functional
processes as comma-joined `Epic/FP` refs in one cell, and joins distinct
descriptions with ` / ` when names collide. Omitted when no process carries the
`dataGroups[]` field.

Surface both output paths (`$OUT_DIR/cosmic-count.json` and
`$OUT_DIR/cosmic-count.md`) to the user as inline-backtick absolute paths.

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
