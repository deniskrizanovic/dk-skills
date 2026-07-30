## MODIFIED Requirements

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
