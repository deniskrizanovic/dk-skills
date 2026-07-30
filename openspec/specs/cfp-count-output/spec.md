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

- **WHEN** the skill emits `<stem>-cosmic-count.json` in the resolved output directory
- **THEN** each entry under any `epics[].functionalProcesses[]` array validates
  against `cosmic_measure_output.schema.json` on its own

#### Scenario: Whole report validates as parent schema

- **WHEN** the skill emits `<stem>-cosmic-count.json` in the resolved output directory
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

- **WHEN** the skill emits `<stem>-cosmic-count.json` in the resolved output directory
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

### Requirement: Functional-process data-groups list

The child `CosmicMeasureOutput` schema SHALL support an optional `dataGroups[]`
array on each functional process. Each entry SHALL be an object with a required
`name` and a required `description`. The array lists the distinct data groups
(objects of interest and transient data groups) that the functional process's
data movements touch, deduplicated by name. The field is optional so that an
output which omits it still validates.

#### Scenario: Functional process carries its data groups

- **WHEN** the skill emits `<stem>-cosmic-count.json`
- **THEN** a functional process MAY include a `dataGroups[]` array
- **AND** each entry has a `name` and a `description`
- **AND** the block still validates against `cosmic_measure_output.schema.json`

#### Scenario: Output without data groups still validates

- **WHEN** a functional-process block omits `dataGroups[]`
- **THEN** it still validates against the child schema

### Requirement: Measure agent authors data groups

The measure agent SHALL author `dataGroups[]` for each functional process it
measures. It SHALL emit one entry per distinct object of interest / data group,
supply an authored `description` for each, and keep the movement `dataGroupRef`
values consistent with the `dataGroups[].name` values so the two align by
construction. The workflow synthesize step SHALL carry `dataGroups[]` through
into the canonical report without an LLM re-serializing it.

#### Scenario: Agent emits a description per data group

- **WHEN** the measure agent decomposes an epic into data movements
- **THEN** it also emits a `dataGroups[]` entry per distinct data group
- **AND** each entry's `description` is authored text describing that object

#### Scenario: Data-group names align with movement refs

- **WHEN** a functional process references data group names in its
  `dataMovements[].dataGroupRef` values
- **THEN** each distinct referenced data group appears once in `dataGroups[]`
  with a matching `name`

#### Scenario: Synthesize passes data groups through

- **WHEN** the workflow synthesize step assembles the report
- **THEN** each functional process's `dataGroups[]` is carried through verbatim
  from the measure agent's output, not regenerated by an LLM

### Requirement: Data-groups catalog in markdown report

The rendered markdown report SHALL include a top-level Data groups catalog,
placed after the per-epic summary and before the per-epic detail sections. The
catalog SHALL be keyed by data group name: rows are deduplicated by name only
(one row per distinct data group name across the whole report), sorted
alphabetically by name. Each row SHALL carry three columns in this order — the
data group name, the functional processes that use it (each formatted as
`Epic/FP` and comma-joined into a single cell), and a description. When data
groups share a name but carry different descriptions, all distinct descriptions
SHALL be joined with ` / ` (in document order) into the single description cell.

#### Scenario: Catalog keyed by deduplicated name

- **WHEN** `render_markdown.py` renders a report whose functional processes
  carry `dataGroups[]`
- **THEN** a Data groups section appears after the per-epic summary
- **AND** each distinct data group name appears in exactly one row
- **AND** the columns are, in order: data group name, using functional processes, description

#### Scenario: Using processes collected into one cell

- **WHEN** a single data group name is carried by more than one functional process
- **THEN** the row lists every using process as an `Epic/FP` reference
  comma-joined within the single "Functional processes" cell

#### Scenario: Conflicting descriptions joined

- **WHEN** two functional processes carry data groups that share a name but have
  different descriptions
- **THEN** the catalog renders one row for that name
- **AND** the description cell shows all distinct descriptions joined with ` / `
  in document order

#### Scenario: Rows sorted alphabetically

- **WHEN** the catalog contains more than one distinct data group name
- **THEN** the rows appear in ascending alphabetical order of the data group name

#### Scenario: No data groups present

- **WHEN** no functional process in the report carries `dataGroups[]`
- **THEN** the renderer omits the Data groups section (or renders it empty)
  without error
