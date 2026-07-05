# wine-tasting-coach

## Purpose

A tasting coach for study mode (known bottle, not blind) that runs on Claude web. The coach embeds a wine tasting grid, fetches authoritative sources to build an expectation sheet, walks the user through structured observation, captures their notes into the grid, provides calibration feedback, and persists each session to a Google Sheet library for long-term tracking.

## Requirements

### Requirement: Runs on Claude web with embedded grid

The skill SHALL be self-contained for use inside Claude on the web: the tasting grid content SHALL be embedded in `SKILL.md` rather than read from an external file, and the skill SHALL rely on web search/browse and the Google Drive connector rather than a local filesystem.

#### Scenario: No external grid file needed

- **WHEN** the skill runs on Claude web with no repo checkout
- **THEN** the coach uses the grid content embedded in `SKILL.md` and does not attempt to read `wine-tasting-grid.md` from a filesystem path

#### Scenario: Google Drive connector unavailable

- **WHEN** the Google Drive connector is not available at save time
- **THEN** the coach completes the tasting and calibration, tells the user it could not save to the library, and offers the filled results inline so nothing is lost

### Requirement: Bottle intake in study mode

The coach SHALL require the user to name the wine and vintage up front before any tasting begins. The coach SHALL NOT support blind tasting; the wine's identity is a required input, not something the user withholds.

#### Scenario: User provides bottle and vintage

- **WHEN** the user starts a session with a wine name and vintage (e.g. "2018 Catena Zapata Malbec, Mendoza")
- **THEN** the coach accepts it as the session subject and proceeds to build the expectation sheet

#### Scenario: User omits the vintage

- **WHEN** the user names a wine but gives no vintage
- **THEN** the coach asks for the vintage (or explicit "non-vintage") before proceeding, because vintage affects the expected profile

### Requirement: Grounded expectation sheet from web sources

The coach SHALL build a per-session expectation sheet by fetching real web sources, following a trust gradient: the winery's tech sheet for the exact bottle is preferred; a grape/region/vintage style archetype is the fallback; crowd-sourced notes (Vivino, CellarTracker) MUST NOT be used as primary evidence. The coach SHALL always cross-check the specific bottle against a grape/region/vintage style profile — even when a tech sheet is found — and reconcile the two. The coach SHALL cite every source it used.

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

### Requirement: Vintage and bottle-age adjustment

The coach SHALL adjust expectations for the vintage's climate and for the wine's current age at tasting time, rather than repeating grape stereotypes. For aged reds this includes anticipating color shift toward garnet and loss of anthocyanin; for hot vintages, riper fruit and higher alcohol.

#### Scenario: Aged red

- **WHEN** the wine is a red several years past its vintage
- **THEN** the coach's color and aroma expectations reflect aging (garnet shift, more tertiary/dried-fruit notes) rather than the young-wine profile

#### Scenario: Hot vintage

- **WHEN** the named vintage was an unusually warm year for the region
- **THEN** the coach adjusts expected fruit ripeness, alcohol, and acidity accordingly and notes why

### Requirement: Grid-driven walkthrough with category-priming questions

The coach SHALL walk the user through the embedded tasting grid in its published order (Sight → Nose → Palate), section by section. For each attribute the coach SHALL ask a leading question that names what is typical for this wine but requires the user to confirm or deny its presence — it MUST NOT assert that a specific flavour or marker is present.

#### Scenario: Section-by-section progression

- **WHEN** a tasting is in progress
- **THEN** the coach presents grid sections in order and does not skip ahead to a later section until the current one is answered

#### Scenario: Category-priming question

- **WHEN** the coach reaches an attribute (e.g. Nose → Flower)
- **THEN** it names the typical marker as a possibility and asks the user to verify (e.g. "Mendoza Malbec often shows violet — do you get florals, and if so which? If not, what is on the nose?") rather than stating the marker is present

#### Scenario: User reports something unexpected

- **WHEN** the user reports a note not in the expectation sheet
- **THEN** the coach records it faithfully without overriding it to match the expected profile

### Requirement: Capture answers into a filled grid

The coach SHALL capture the user's answers into a copy of the tasting grid structure, preserving the grid's sections and attributes and recording the user's stated observations under each.

#### Scenario: Completed walkthrough produces a filled grid

- **WHEN** the user has answered through the end of the Palate section
- **THEN** the coach outputs a filled-in grid reflecting the user's own observations attribute by attribute

### Requirement: Calibration feedback at close

At the end of a session the coach SHALL provide a short calibration comparison between the user's captured notes and the expected profile, framed as learning feedback (what lined up, what was missed, what to focus on next) and NOT as a score or grade.

#### Scenario: Notes compared to expectation

- **WHEN** the walkthrough is complete
- **THEN** the coach summarises where the user's notes matched the expected profile, where they diverged, and offers one or two concrete focus points for next time

#### Scenario: No numeric grade

- **WHEN** the coach gives calibration feedback
- **THEN** it does not assign a numeric score or pass/fail verdict

### Requirement: Persist each tasting to a Google Sheet library

The coach SHALL append each completed session as a single row to a Google Sheet named exactly **"Wine Tasting Log"** in the user's Google Drive, so the user accumulates a filterable, sortable history over time. The sheet SHALL use a stable column schema: identity columns (wine, vintage, tasting date, region/producer), one column per grid attribute holding the user's observation, columns for the cited expectation-sheet sources, and a calibration-summary column. If a sheet named "Wine Tasting Log" does not yet exist, the coach SHALL create it with that exact name and a header row.

#### Scenario: Completed session appended as a row

- **WHEN** a walkthrough completes through calibration feedback and the Google Drive connector is available
- **THEN** the coach appends one row to the "Wine Tasting Log" sheet capturing the identity fields, the per-attribute observations, the cited sources, and the calibration summary

#### Scenario: Library sheet does not exist yet

- **WHEN** no sheet named "Wine Tasting Log" is found in the user's Drive
- **THEN** the coach creates a sheet named exactly "Wine Tasting Log" with the defined header row before appending the first tasting

#### Scenario: Column schema is stable across sessions

- **WHEN** the coach appends a tasting to an existing library sheet
- **THEN** it maps each observation to the existing columns by header and does not reorder or duplicate columns, so rows stay aligned across sessions
