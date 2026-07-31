## ADDED Requirements

### Requirement: Epic description carried into report

The report envelope's per-epic object SHALL carry the source `description` — the requirement text from the input CSV that the measurement rests on — as an optional string field on `epics[]`. The `CosmicCountReport` epic schema SHALL permit this field. The measure agent SHALL echo the input epic's description verbatim into its output, and the synthesize step SHALL pass it through unchanged. The field is optional so that pre-existing count JSON without a description still validates.

#### Scenario: Measure agent echoes the input description

- **WHEN** an epic with a non-empty `description` is measured
- **THEN** the measured epic object carries a `description` field equal to the input epic's description text

#### Scenario: Epic object with description validates against parent schema

- **WHEN** a count report's `epics[]` object includes a `description` string
- **THEN** the whole report still validates against `cosmic_count_report.schema.json`

#### Scenario: Missing description still validates

- **WHEN** an epic object omits `description` (e.g. a report produced before this change)
- **THEN** the report validates against the parent schema unchanged

### Requirement: Epic description shown in markdown report

The markdown renderer SHALL display each epic's `description` in that epic's per-epic detail section, positioned so the requirement text sits with its measurement. When an epic has no `description`, the renderer SHALL omit the description block for that epic rather than emit an empty one.

#### Scenario: Description rendered in per-epic detail

- **WHEN** rendering an epic whose object carries a non-empty `description`
- **THEN** the epic's detail section includes the description text

#### Scenario: No description present

- **WHEN** rendering an epic whose object has no `description` (or an empty one)
- **THEN** the epic's detail section is rendered without a description block
