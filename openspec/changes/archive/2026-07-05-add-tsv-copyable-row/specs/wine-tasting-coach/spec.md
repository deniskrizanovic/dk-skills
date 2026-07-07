## MODIFIED Requirements

### Requirement: Persist each tasting to a Google Sheet library

The coach SHALL persist each completed session as a single row in a Google Sheet named exactly **"Wine Tasting Log"** in the user's Google Drive, so the user accumulates a filterable, sortable history over time. The sheet SHALL use a stable column schema: identity columns (wine, vintage, tasting date, region/producer), one column per grid attribute holding the user's observation, columns for the cited expectation-sheet sources, a source-capture-date column, a calibration-summary column, and a Perception Alignment column. Each source column SHALL contain only a URL the coach fetched successfully during the session or a descriptive reference; it MUST NOT contain an unverified URL. The source-capture-date column SHALL record the date the sources were fetched, so later link rot is explainable as drift.

The coach SHALL append the row directly via the Google Sheet connector ONLY IF that connector supports appending. Because the current connector can read a sheet but cannot append to one, the coach SHALL instead emit a **tab-delimited (TSV) row** for the user to copy and paste into the "Wine Tasting Log" sheet. The connector SHALL still be used to **read** prior rows for computing the Perception Alignment trend.

The tab-delimited row SHALL obey strict format rules so a pasted line lands as exactly one column-aligned row:
- The field order SHALL match the column schema exactly.
- The row SHALL be exactly one line (one session per line).
- Tab and newline characters occurring inside any cell value SHALL be replaced with a space before the row is emitted, so no cell can split the row across columns.
- The data row SHALL contain the same number of fields as the header, including empty fields for blank cells (e.g. an empty Perception Alignment or an unanswered attribute).

The coach SHALL emit only the data row by default, and SHALL make the tab-delimited header row available on request so a first-time user can seed a new sheet with the correct columns. If a sheet named "Wine Tasting Log" does not yet exist, the coach SHALL provide the header row (and instruct the user to create the sheet with that exact name) before the first data row is pasted.

#### Scenario: Connector cannot append, coach emits a copyable TSV row

- **WHEN** a walkthrough completes through calibration feedback and the Google Sheet connector can read the sheet but cannot append to it
- **THEN** the coach emits a single tab-delimited row capturing the identity fields, the per-attribute observations, the cited sources (verified URLs or descriptive references), the source-capture date, the calibration summary, and the Perception Alignment value, and instructs the user to paste it into the "Wine Tasting Log" sheet

#### Scenario: Connector append is supported

- **WHEN** a walkthrough completes and the Google Sheet connector does support appending
- **THEN** the coach appends one row to the "Wine Tasting Log" sheet mapping each observation to the existing column by header, without requiring a manual paste

#### Scenario: Tab-delimited row is column-aligned and single-line

- **WHEN** the coach emits a tab-delimited row and a cell value (e.g. the calibration summary or an observation) contains a tab or newline character
- **THEN** the coach replaces those characters with spaces so the emitted row is exactly one line with the same field count as the header, and pastes into a single aligned sheet row

#### Scenario: Header row offered for a new sheet

- **WHEN** no sheet named "Wine Tasting Log" exists yet, or the user asks for the header
- **THEN** the coach provides the tab-delimited header row matching the column schema so the user can seed a new sheet with the correct columns before pasting data rows

#### Scenario: Perception Alignment trend read from prior rows

- **WHEN** the coach computes the Perception Alignment trend for a session
- **THEN** it reads the Perception Alignment values from prior rows of the "Wine Tasting Log" sheet via the connector, independent of how the current session's row is written

#### Scenario: Column schema is stable across sessions

- **WHEN** the coach produces a row (appended or tab-delimited) for an existing library sheet
- **THEN** it maps each observation to the existing columns by header order and does not reorder or duplicate columns, so rows stay aligned across sessions

#### Scenario: Source column never stores an unverified URL

- **WHEN** the coach writes a source column for a session
- **THEN** the cell contains either a URL the coach fetched successfully this session or a descriptive reference, never a guessed or unverified URL

#### Scenario: Existing library sheet lacks the capture-date column

- **WHEN** the coach produces a row for a "Wine Tasting Log" that predates the source-capture-date column
- **THEN** the coach adds the capture-date column at the end of the schema rather than reordering existing columns, keeping older rows aligned
