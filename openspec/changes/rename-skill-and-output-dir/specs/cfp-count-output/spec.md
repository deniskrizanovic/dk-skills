## MODIFIED Requirements

### Requirement: Two-schema report structure

The skill's intermediate JSON output SHALL be governed by two JSON Schemas: a
child `CosmicMeasureOutput` (`cosmic_measure_output.schema.json`) describing one
functional process, and a parent `CosmicCountReport`
(`cosmic_count_report.schema.json`) describing the whole scope. The parent's
`epics[].functionalProcesses[]` items MUST `$ref` the child schema so that each
functional-process block validates as a standalone `CosmicMeasureOutput`.

#### Scenario: Functional-process block validates as child schema

- **WHEN** the skill emits `cosmic-count.json` in the resolved output directory
- **THEN** each entry under any `epics[].functionalProcesses[]` array validates
  against `cosmic_measure_output.schema.json` on its own

#### Scenario: Whole report validates as parent schema

- **WHEN** the skill emits `cosmic-count.json` in the resolved output directory
- **THEN** the entire file validates against `cosmic_count_report.schema.json`

### Requirement: camelCase report vocabulary

All keys in the parent report SHALL use camelCase to match the child schema, so
a single output file has one consistent casing convention. This replaces the
prior snake_case output.

#### Scenario: Report uses camelCase keys

- **WHEN** the skill emits `cosmic-count.json` in the resolved output directory
- **THEN** roll-up appears under `rollUp`, per-epic size under `epicCfp`,
  movement type under `movementType`, and data group under `dataGroupRef`
- **AND** no snake_case keys (e.g. `epic_cfp`, `roll_up`, `data_group`) appear
