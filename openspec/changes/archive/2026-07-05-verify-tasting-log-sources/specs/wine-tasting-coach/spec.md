## MODIFIED Requirements

### Requirement: Grounded expectation sheet from web sources

The coach SHALL build a per-session expectation sheet by fetching real web sources, following a trust gradient: the winery's tech sheet for the exact bottle is preferred; a grape/region/vintage style archetype is the fallback; crowd-sourced notes (Vivino, CellarTracker) MUST NOT be used as primary evidence. The coach SHALL always cross-check the specific bottle against a grape/region/vintage style profile — even when a tech sheet is found — and reconcile the two. The coach SHALL cite every source it used. A source citation MAY be recorded as a URL ONLY IF the coach actually fetched that URL successfully during the session; the coach MUST NOT record a guessed, pattern-constructed, or otherwise unverified URL. When a source informed the expectation sheet but no URL could be fetched or verified, the coach SHALL record a descriptive reference (producer, bottle, and document type) instead of a URL.

#### Scenario: Tech sheet found, cross-checked against style profile

- **WHEN** the coach locates the producer's tech sheet for the named bottle
- **THEN** the expectation sheet is built from that sheet (oak regime, blend, ABV, aging) AND cross-checked against a grape/region/vintage style archetype for expected sensory markers, with both sources cited

#### Scenario: Bottle is atypical for its style

- **WHEN** the cross-check reveals the specific bottle diverges from the style archetype
- **THEN** the coach flags the divergence in the expectation sheet rather than silently favouring one source

#### Scenario: Tech sheet not found, fall back to archetype

- **WHEN** the coach cannot find a tech sheet for the specific bottle
- **THEN** the coach builds the expectation sheet from a reliable grape/region/vintage style profile AND explicitly states that it is coaching from the style archetype, not the specific bottle

#### Scenario: Crowd notes are the only source

- **WHEN** only crowd-sourced tasting notes are available
- **THEN** the coach does not treat them as authoritative and says the expectation is low-confidence

#### Scenario: Only verified URLs are cited

- **WHEN** the coach used information from a source it could not open or whose URL it could not confirm this session
- **THEN** the coach cites that source as a descriptive reference (producer, bottle, document type) rather than emitting a URL, and does not present an unverified URL as a citation

### Requirement: Persist each tasting to a Google Sheet library

The coach SHALL append each completed session as a single row to a Google Sheet named exactly **"Wine Tasting Log"** in the user's Google Drive, so the user accumulates a filterable, sortable history over time. The sheet SHALL use a stable column schema: identity columns (wine, vintage, tasting date, region/producer), one column per grid attribute holding the user's observation, columns for the cited expectation-sheet sources, a source-capture-date column, and a calibration-summary column. Each source column SHALL contain only a URL the coach fetched successfully during the session or a descriptive reference; it MUST NOT contain an unverified URL. The source-capture-date column SHALL record the date the sources were fetched, so later link rot is explainable as drift. If a sheet named "Wine Tasting Log" does not yet exist, the coach SHALL create it with that exact name and a header row.

#### Scenario: Completed session appended as a row

- **WHEN** a walkthrough completes through calibration feedback and the Google Drive connector is available
- **THEN** the coach appends one row to the "Wine Tasting Log" sheet capturing the identity fields, the per-attribute observations, the cited sources (verified URLs or descriptive references), the source-capture date, and the calibration summary

#### Scenario: Library sheet does not exist yet

- **WHEN** no sheet named "Wine Tasting Log" is found in the user's Drive
- **THEN** the coach creates a sheet named exactly "Wine Tasting Log" with the defined header row before appending the first tasting

#### Scenario: Column schema is stable across sessions

- **WHEN** the coach appends a tasting to an existing library sheet
- **THEN** it maps each observation to the existing columns by header and does not reorder or duplicate columns, so rows stay aligned across sessions

#### Scenario: Source column never stores an unverified URL

- **WHEN** the coach writes a source column for a session
- **THEN** the cell contains either a URL the coach fetched successfully this session or a descriptive reference, never a guessed or unverified URL

#### Scenario: Existing library sheet lacks the capture-date column

- **WHEN** the coach appends to a "Wine Tasting Log" that predates the source-capture-date column
- **THEN** the coach adds the capture-date column at the end of the schema rather than reordering existing columns, keeping older rows aligned
