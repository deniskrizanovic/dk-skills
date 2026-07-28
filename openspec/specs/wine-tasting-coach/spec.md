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

### Requirement: Vintage and bottle-age adjustment

The coach SHALL adjust expectations for the vintage's climate and for the wine's current age at tasting time, rather than repeating grape stereotypes. For aged reds this includes anticipating color shift toward garnet and loss of anthocyanin; for hot vintages, riper fruit and higher alcohol.

#### Scenario: Aged red

- **WHEN** the wine is a red several years past its vintage
- **THEN** the coach's color and aroma expectations reflect aging (garnet shift, more tertiary/dried-fruit notes) rather than the young-wine profile

#### Scenario: Hot vintage

- **WHEN** the named vintage was an unusually warm year for the region
- **THEN** the coach adjusts expected fruit ripeness, alcohol, and acidity accordingly and notes why

### Requirement: Decant check and guidance for aged wines

When the coach has assessed the wine as **old/mature** during its bottle-age adjustment, the coach SHALL, before beginning the sensory walkthrough, ask the user **how long the wine has been decanted for**, accepting "not decanted" / "poured straight from the bottle" as valid answers. The coach SHALL then provide grounded, **retrospective** guidance on how long the wine ideally should have been decanted, reasoning from the wine's age and tannic structure rather than a fixed rule: fragile older wines are typically decanted gently off their sediment with short or minimal aeration to preserve delicate tertiary aromatics, while sturdier mature wines tolerate more air. The coach SHALL compare the user's actual decant time to its recommendation and explain the likely sensory effect of the difference. The coach SHALL NOT run this check for young wines.

The guidance SHALL be framed as learning feedback, NOT a grade or quality verdict. The decant context MAY inform how the coach interprets divergence during calibration (e.g. a faded nose attributable to over-decanting rather than a missed marker) but SHALL NOT change the Perception Alignment metric.

#### Scenario: Old wine triggers the decant question before tasting

- **WHEN** the coach has assessed the wine as old/mature and is about to start the sensory walkthrough
- **THEN** the coach first asks how long the wine has been decanted (accepting "not decanted") before presenting the first grid section

#### Scenario: Retrospective guidance reasoned from age and structure

- **WHEN** the user reports how long an old wine was decanted
- **THEN** the coach states the decant approach it would have recommended for a wine of that age and structure (e.g. decant off the sediment with short aeration for a fragile old red), compares it to what the user did, and explains the likely sensory effect — as per-bottle reasoning, not a universal minute count

#### Scenario: Over-decanting explained as context, not a scored miss

- **WHEN** the user over- or under-decanted an old wine and the nose or palate reads faded or closed
- **THEN** the coach may note the decant as the likely cause when interpreting divergence at calibration, but does not lower the Perception Alignment metric on account of it

#### Scenario: Young wine skips the check

- **WHEN** the coach has assessed the wine as young rather than old/mature
- **THEN** the coach does not ask the decant question and proceeds directly to the sensory walkthrough

#### Scenario: Age cannot be confidently assessed

- **WHEN** the wine is ungrounded or the coach cannot confidently judge whether it is old/mature
- **THEN** the coach asks the user or notes that it cannot advise on decanting rather than guessing, and does not force the check

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

### Requirement: Perception alignment metric

The coach SHALL compute a per-session **Perception Alignment** metric that measures, of the **high-confidence** expected markers, how many the taster registered. A marker SHALL be counted toward the metric ONLY IF the expectation for that attribute is high-confidence — i.e. the winery tech sheet and the grape/region/vintage style archetype **agree** on it. Attributes that are divergent, atypical, low-confidence, or ungrounded SHALL be **excluded** from both the numerator and the denominator and SHALL remain purely qualitative. The metric is a calibration mirror (the taster versus their own past sessions), NOT a grade of the taster and NOT a quality verdict on the session or the wine.

The coach SHALL apply an **honesty guardrail**: reporting a note the expectation did not predict, contradicting an expectation that proves wrong for this bottle, or flagging the bottle as flawed/atypical SHALL NEVER lower the metric. Honest divergence is neutral information, not a miss.

#### Scenario: Only high-confidence markers are counted

- **WHEN** the coach computes the alignment metric for a session
- **THEN** the denominator includes only attributes where the tech sheet and style archetype agree, and divergent, atypical, low-confidence, or ungrounded attributes are excluded from both numerator and denominator

#### Scenario: Honest divergence never lowers the metric

- **WHEN** the taster reports a note the expectation missed, contradicts an expectation that is wrong for this bottle, or flags the bottle as off/atypical
- **THEN** the metric is not reduced as a result, and the divergence is recorded qualitatively rather than scored as a miss

#### Scenario: Atypical bottle excludes its divergent attributes from the score

- **WHEN** the cross-check flagged the bottle as diverging from its style archetype on certain attributes
- **THEN** those attributes are excluded from the alignment metric and remain qualitative notes, so a correct palate on an atypical bottle is not penalised

### Requirement: Calibration feedback at close

At the end of a session the coach SHALL provide a short calibration comparison between the user's captured notes and the expected profile, framed as learning feedback (what lined up, what was missed, what to focus on next). The coach MAY accompany this with the Perception Alignment metric, but MUST NOT assign a grade of the taster, a letter grade, or a pass/fail verdict on the session. When the coach shows the alignment metric, it SHALL present it **alongside** the qualitative Matched/Missed/Focus-next feedback (not as a replacement) and **paired with its trend across recent sessions**, so the number reads as a calibration mirror rather than a standalone verdict.

#### Scenario: Notes compared to expectation

- **WHEN** the walkthrough is complete
- **THEN** the coach summarises where the user's notes matched the expected profile, where they diverged, and offers one or two concrete focus points for next time

#### Scenario: Metric shown as a calibration mirror, not a grade

- **WHEN** the coach shows the Perception Alignment metric at the close of a session
- **THEN** it presents the metric alongside the qualitative Matched/Missed/Focus-next feedback and paired with the trend across recent sessions, and does not assign a letter grade, pass/fail verdict, or any judgement of the taster

### Requirement: Persist each tasting to a Google Sheet library

The coach SHALL persist each completed session as a single row in a Google Sheet named exactly **"Wine Tasting Log"** in the user's Google Drive, so the user accumulates a filterable, sortable history over time. The sheet SHALL use a stable column schema: identity columns (wine, vintage, tasting date, region/producer), one column per grid attribute holding the user's observation, columns for the cited expectation-sheet sources, a source-capture-date column, a calibration-summary column, and a Perception Alignment column. Every grid-attribute column header SHALL be **unique**; in particular the grid's two intensity attributes SHALL map to the distinct headers **"Color Intensity"** (Sight → Color) and **"Aroma Intensity"** (Nose → Impression) rather than a shared "Intensity" header, so mapping an observation to a column by header name is unambiguous. Each source column SHALL contain only a URL the coach fetched successfully during the session or a descriptive reference; it MUST NOT contain an unverified URL. The source-capture-date column SHALL record the date the sources were fetched, so later link rot is explainable as drift.

The coach SHALL append the row directly via the Google Sheet connector ONLY IF that connector supports appending. Because the current connector can read a sheet but cannot append to one, the coach SHALL instead emit a **tab-delimited (TSV) row** for the user to copy and paste into the "Wine Tasting Log" sheet. The connector SHALL still be used to **read** prior rows for computing the Perception Alignment trend.

The tab-delimited row SHALL obey strict format rules so a pasted line lands as exactly one column-aligned row:
- The field order SHALL match the column schema exactly.
- The row SHALL be exactly one line (one session per line).
- Tab and newline characters occurring inside any cell value SHALL be replaced with a space before the row is emitted, so no cell can split the row across columns.
- The data row SHALL contain the same number of fields as the header, including empty fields for blank cells (e.g. an empty Perception Alignment or an unanswered attribute).

The coach SHALL emit only the data row by default, and SHALL make the tab-delimited header row available on request so a first-time user can seed a new sheet with the correct columns. If a sheet named "Wine Tasting Log" does not yet exist, the coach SHALL provide the header row (and instruct the user to create the sheet with that exact name) before the first data row is pasted.

#### Scenario: Intensity attributes use distinct column headers

- **WHEN** the coach produces the header row or maps observations to columns
- **THEN** the Sight → Color intensity uses the header "Color Intensity" and the Nose → Impression intensity uses the header "Aroma Intensity", so no two grid-attribute columns share a header

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

#### Scenario: Existing sheet predates the intensity rename

- **WHEN** the coach appends to a "Wine Tasting Log" whose header still has a single legacy "Intensity" column from before this rename
- **THEN** the coach does not rename or reorder the existing column in place; it treats "Color Intensity" and "Aroma Intensity" as the current names and appends any genuinely new column at the end, keeping older rows aligned

#### Scenario: Source column never stores an unverified URL

- **WHEN** the coach writes a source column for a session
- **THEN** the cell contains either a URL the coach fetched successfully this session or a descriptive reference, never a guessed or unverified URL

#### Scenario: Existing library sheet lacks the capture-date column

- **WHEN** the coach produces a row for a "Wine Tasting Log" that predates the source-capture-date column
- **THEN** the coach adds the capture-date column at the end of the schema rather than reordering existing columns, keeping older rows aligned
