## Why

The wine-tasting-coach's Step 5 persists each session by appending a row to the
`Wine Tasting Log` Google Sheet. But the current Google Sheet connector can only
**read** a sheet — it cannot append to one. So today the automated save path
described in the spec cannot actually run, and there is no reliable way for the
user to get a completed session into their sheet as a clean, column-aligned row.

## What Changes

- Reframe Step 5 persistence: the coach attempts a connector append **only if the
  connector supports appending**; because the current connector does not, the coach
  emits a **tab-delimited (TSV) row** the user copies and pastes into the
  `Wine Tasting Log` sheet.
- The connector's real, working job today is **reading prior rows** to compute the
  Perception Alignment trend — this is unchanged and now clearly separated from
  writing.
- Define strict TSV format rules so a pasted line lands as exactly one aligned row:
  - Column order matches the existing Step 5 schema exactly.
  - Exactly one line per session.
  - Tab and newline characters inside any cell are replaced with spaces so they
    cannot shatter the row across columns.
  - The data row has the same field count as the header, including blank cells
    (e.g. empty Perception Alignment, unanswered attributes).
- Offer the tab-delimited **header row on request** so a first-time user can seed a
  brand-new sheet with correct columns; the default output is just the data row.

## Capabilities

### New Capabilities
<!-- None. This extends existing persistence behavior. -->

### Modified Capabilities
- `wine-tasting-coach`: The "Persist each tasting to a Google Sheet library"
  requirement changes — persistence no longer assumes connector append. It adds a
  tab-delimited copyable-row output (with strict format rules and an on-request
  header) as the practical save path while the connector lacks append, and keeps
  connector reads for the Perception Alignment trend.

## Impact

- `wine-tasting-coach/SKILL.md` — Step 5 (persist) reworded to describe the
  connector's read-only reality, the TSV row output, format rules, and on-request
  header. The Step 4 trend computation (reads prior rows) is unaffected.
- `openspec/specs/wine-tasting-coach/spec.md` — the persist requirement and its
  scenarios updated on archive.
- No code dependencies; this is a prompt/skill behavior change. The existing
  Drive-unavailable fallback (connector entirely absent) remains a separate branch.
