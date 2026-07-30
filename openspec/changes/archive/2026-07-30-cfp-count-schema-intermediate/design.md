# Design — CFP count two-schema intermediate format

## Context

`dk-cosmic-cfp-count` measures COSMIC functional size from an epics CSV via a
multi-agent workflow, emitting `data/cosmic-count.json` in an ad-hoc snake_case
shape. Separately, a code-analysis COSMIC measurer emits
`cosmic_measure_output.schema.json` (`CosmicMeasureOutput`) — one document per
functional process, camelCase, with code-provenance fields (`sourceLine`,
`isApiCall`, `implementationType`, `mergedFrom`, `viaArtifact`, `tier`). Both
describe COSMIC data movements but share no field vocabulary.

The child schema's `$id` (`sf-cosmic-measurer`) and `shared/output.py` origin
mark it as a shared, code-analysis artifact. We want to reuse it — not
repurpose it.

## Goals / Non-Goals

**Goals**
- Reuse `CosmicMeasureOutput` verbatim as the per-functional-process atom.
- Give the whole `cosmic-count.json` a validatable schema.
- One consistent casing (camelCase) across the file.

**Non-Goals**
- Changing the code-analysis measurer.
- Making this skill produce code-provenance fields it cannot know.
- Backward compatibility with the old snake_case file (breaking migration).

## Decisions

### D1 — Two schemas, parent references child (not one merged schema)

```
cosmic_count_report.schema.json   (PARENT, new $id, camelCase)
  CosmicCountReport
  ├─ disclaimer
  ├─ rollUp {projectCfpCountable, cfpRange[2], epicsMeasured, epicsTotal,
  │          countableEpics, epicsRestingOnAssumptions[]}
  ├─ rulesPrimer
  ├─ epics[]
  │   ├─ epicId, epicName, confidence(enum), epicCfp, caveats[]
  │   ├─ functionalProcesses[]  ── $ref ──► cosmic_measure_output.schema.json
  │   └─ gaps[]  {gapId, category, gapOrQuestion, impactOrNotes}
  └─ measurementGaps[]

cosmic_measure_output.schema.json (CHILD, unchanged $id)
  CosmicMeasureOutput  {functionalProcessId, artifact, dataMovements[], traversalWarnings[]}
```

**Why over alternatives:**
- *Option A (nested, wrapper unschematized)*: child stays clean but the report
  envelope has no contract — can't validate the whole file. Rejected.
- *Option B (one schema becomes whole-count root)*: couples the shared schema to
  this skill's report shape; the code measurer would never emit epics/rollUp.
  Rejected — fights the child's origin.
- *D1 (two schemas)*: child untouched + reused by code measurer; parent owns the
  report vocabulary; whole file validates. Best of A and B.

### D2 — Relax child required fields, don't fabricate

Drop `implementationType` and `isApiCall` from the child's `required` array.
Proposal-grain epics have no source code, so these are unknowable; the skill
omits them rather than inventing values (honors gaps-over-guesses). The code
measurer keeps emitting them — optional means "may include", so both are valid.

### D3 — camelCase everywhere

Parent adopts the child's camelCase. Workflow's assembled `fileObject` and
`EPIC_SCHEMA`, plus `render_markdown.py` key reads, migrate from snake_case.
Rejected keeping snake_case parent: mixed casing in one file is a smell.

### D4 — Per-process CFP: add optional `cfp` to child

Child schema has no CFP field. Options: (a) add optional `cfp` integer to the
child, or (b) derive from `dataMovements.length` everywhere. Choose **(a)** —
explicit is safer than implicit; a reader shouldn't have to know the 1-movement-
=-1-CFP rule to get the number, and derivation still works as a fallback/check.
Keep it optional so the code measurer isn't forced to populate it.

## Field mapping (old → new)

```
roll_up                       → rollUp
project_cfp_countable         → rollUp.projectCfpCountable
cfp_range                     → rollUp.cfpRange
epics[].epic_id / epic_name   → epicId / epicName
epics[].epic_cfp              → epicCfp
functional_processes          → functionalProcesses
  process.name                → (child) functionalProcessId + artifact{type,name}
  process.movements[]         → (child) dataMovements[]
    move.type                 → movementType
    move.data_group           → dataGroupRef
    (new)                     → name, order
    note / citation           → note / citation  (already in child, additive v2)
  process.process_cfp         → (child, optional) cfp
gaps[].gap_id ...             → gapId, category, gapOrQuestion, impactOrNotes
measurement_gaps              → measurementGaps
rules_primer                  → rulesPrimer
```

## Risks / Trade-offs

- [Breaking change to `cosmic-count.json` consumers] → this is a standalone
  skill artifact; no in-repo consumer beyond `render_markdown.py`, updated in
  lockstep. Document the break in SKILL.md.
- [Cross-file `$ref` resolution] → parent references child by relative path /
  `$id`; both ship in the same skill dir. Validate with a draft-07 resolver that
  supports local refs.
- [Child schema now has `cfp`] → additive + optional, no impact on code measurer.

## Migration Plan

1. Relax child `required`; add optional `cfp`.
2. Author parent schema with `$ref` to child.
3. Update workflow `EPIC_SCHEMA` + `fileObject` assembly to camelCase + child shape.
4. Update `render_markdown.py` key reads.
5. Update SKILL.md to document the two-schema intermediate format.
6. No rollback concern — no persisted historical `cosmic-count.json` to migrate.

## Open Questions

- Does the target JSON-Schema validator resolve relative-path `$ref` across the
  two files, or should the parent inline the child as a `$defs` copy? (Prefer
  `$ref`; fall back to inlined `$defs` if the runtime validator can't resolve.)
