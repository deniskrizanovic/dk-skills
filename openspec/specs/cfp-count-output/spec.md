# Capability: cfp-count-output

## Purpose

Define the intermediate JSON output format for COSMIC Function Point counting, structured as a two-schema system with a parent report envelope and child functional-process measurements.

## Requirements

### Requirement: Two-schema report structure

The skill's intermediate JSON output SHALL be governed by two JSON Schemas: a
child `CosmicMeasureOutput` (`cosmic_measure_output.schema.json`) describing one
functional process, and a parent `CosmicCountReport`
(`cosmic_count_report.schema.json`) describing the whole scope. The parent's
`epics[].functionalProcesses[]` items MUST `$ref` the child schema so that each
functional-process block validates as a standalone `CosmicMeasureOutput`.

#### Scenario: Functional-process block validates as child schema

- **WHEN** the skill emits `data/cosmic-count.json`
- **THEN** each entry under any `epics[].functionalProcesses[]` array validates
  against `cosmic_measure_output.schema.json` on its own

#### Scenario: Whole report validates as parent schema

- **WHEN** the skill emits `data/cosmic-count.json`
- **THEN** the entire file validates against `cosmic_count_report.schema.json`

### Requirement: Child schema optional code-analysis fields

The child schema SHALL treat `implementationType` and `isApiCall` as optional
rather than required, so a proposal-grain measurement that has no code artifact
can omit them without producing invalid output.

#### Scenario: Proposal-grain movement omits code fields

- **WHEN** a data movement is measured from an epic description with no source code
- **THEN** the movement object omits `implementationType` and `isApiCall`
- **AND** the movement still validates against the child schema

#### Scenario: Code-analysis measurer still emits code fields

- **WHEN** the code-analysis COSMIC measurer produces a movement
- **THEN** it MAY still include `implementationType` and `isApiCall`
- **AND** the movement validates against the same child schema

### Requirement: camelCase report vocabulary

All keys in the parent report SHALL use camelCase to match the child schema, so
a single output file has one consistent casing convention. This replaces the
prior snake_case output.

#### Scenario: Report uses camelCase keys

- **WHEN** the skill emits `data/cosmic-count.json`
- **THEN** roll-up appears under `rollUp`, per-epic size under `epicCfp`,
  movement type under `movementType`, and data group under `dataGroupRef`
- **AND** no snake_case keys (e.g. `epic_cfp`, `roll_up`, `data_group`) appear

### Requirement: Report envelope content

The parent report SHALL carry the skill's report-level fields that the child
schema does not model: `disclaimer`, `rollUp` (project CFP, CFP range, epic
counts, epics resting on assumptions), `rulesPrimer`, `epics[]` (each with
`epicId`, `epicName`, `confidence`, `epicCfp`, `caveats`, `functionalProcesses`,
`gaps`), and `measurementGaps[]`.

#### Scenario: Roll-up preserved in parent

- **WHEN** the workflow computes the JS roll-up
- **THEN** the emitted report contains `rollUp` with the project CFP total, the
  CFP range `[confirmedFloor, measuredTotal]`, epics measured/total counts, and
  the list of epics resting on assumptions

#### Scenario: Measurement gaps preserved

- **WHEN** an epic is too vague to size and produces a measurement gap
- **THEN** the gap appears both under its epic's `gaps[]` and in the top-level
  `measurementGaps[]`, with a deterministic `gapId` (e.g. `CG-E01-01`)

### Requirement: Per-process CFP available in report

The report SHALL make each functional process's CFP recoverable. Since the child
schema is the movement list, per-process CFP is either an optional field on the
child or derived as the count of `dataMovements`; each `epicCfp` equals the sum
of its processes' CFP.

#### Scenario: Epic CFP equals sum of process CFP

- **WHEN** an epic has functional processes with CFP values c1, c2, ... cn
- **THEN** the epic's `epicCfp` equals c1 + c2 + ... + cn

#### Scenario: Process CFP equals movement count

- **WHEN** a functional process lists m data movements and carries no explicit CFP
- **THEN** its CFP is m (1 movement = 1 CFP)
