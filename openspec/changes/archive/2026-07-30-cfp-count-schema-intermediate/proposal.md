## Why

The `dk-cosmic-cfp-count` skill emits an ad-hoc, snake_case JSON blob (`data/cosmic-count.json`) that shares no contract with the existing `cosmic_measure_output.schema.json` produced by the code-analysis COSMIC measurer. The two artifacts describe the same domain (COSMIC data movements) with divergent field names, so nothing downstream can consume both. Adopting the existing schema as the per-functional-process intermediate format aligns the two measurers and makes the skill's output validatable.

## What Changes

- Adopt `cosmic_measure_output.schema.json` (`CosmicMeasureOutput`) **verbatim as the child** unit — one document per functional process — inside the skill's output. Each `functionalProcesses[]` entry becomes a valid `CosmicMeasureOutput`.
- **Relax the child schema**: drop `implementationType` and `isApiCall` from `required` (proposal-grain epics have no code artifact to derive them from). **BREAKING** for any consumer that assumed those keys always present.
- Add a **new parent schema** `cosmic_count_report.schema.json` (`CosmicCountReport`) modeling the whole scope: `disclaimer`, `rollUp`, `rulesPrimer`, `epics[]`, `measurementGaps[]`. Its `epics[].functionalProcesses[]` uses `$ref` to the child schema.
- **camelCase the entire report** — the skill's output migrates from snake_case (`epic_cfp`, `roll_up`, `data_group`, `type`) to camelCase (`epicCfp`, `rollUp`, `dataGroupRef`, `movementType`) to match the child. **BREAKING** for existing `cosmic-count.json` readers.
- Update the workflow's `EPIC_SCHEMA` (movement shape → child field names; add `functionalProcessId`, `artifact`, `name`, `order` per process/movement) and `render_markdown.py` (read camelCase keys).
- Resolve per-process CFP: child schema has no CFP field — either add an optional `cfp` to the child or compute from `dataMovements.length`. Decided in design.

## Capabilities

### New Capabilities
- `cfp-count-output`: the intermediate JSON contract for the `dk-cosmic-cfp-count` skill — the parent `CosmicCountReport` report envelope and its use of the child `CosmicMeasureOutput` per functional process.

### Modified Capabilities
<!-- none — no existing openspec spec governs cfp output today -->

## Impact

- `dk-cosmic-cfp-count/cosmic_measure_output.schema.json` (relax required fields)
- `dk-cosmic-cfp-count/cosmic_count_report.schema.json` (new)
- `dk-cosmic-cfp-count/scripts/cosmic-cfp-count.workflow.js` (EPIC_SCHEMA + assembled fileObject)
- `dk-cosmic-cfp-count/scripts/render_markdown.py` (camelCase key reads)
- `dk-cosmic-cfp-count/SKILL.md` (document the two-schema intermediate format)
- Downstream consumers of `data/cosmic-count.json` — breaking field renames.
