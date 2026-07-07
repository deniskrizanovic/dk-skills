## Context

The wine-tasting-coach runs inside Claude on the web and persists each session to a
`Wine Tasting Log` Google Sheet. The spec's Step 5 was written assuming the Google
Sheet connector could append a row. In the current runtime the connector can **read**
a sheet but has **no append capability**. As a result the described automated save
path cannot run, and users have no reliable way to get a clean, column-aligned row
into their sheet.

The Perception Alignment trend (Step 4) already depends on the connector *reading*
prior rows — that part works today. Only the *write* is blocked.

## Goals / Non-Goals

**Goals:**
- Give the user a reliable way to persist a session as one aligned sheet row despite
  the connector's lack of append.
- Keep the connector's working read path (for the trend) intact and clearly separated
  from writing.
- Define a TSV format precise enough that a paste never misaligns columns.
- Preserve the option to append automatically if a future connector supports it.

**Non-Goals:**
- Building or modifying any connector. This is a skill/prompt behavior change only.
- Changing the column schema, the calibration logic, or the Perception Alignment
  metric definition.
- Replacing the existing Drive-unavailable fallback (connector entirely absent), which
  remains its own branch.

## Decisions

**Decision: TSV, not CSV.** Tab-separated values paste into Google Sheets as a single
row with cells landing in adjacent columns, no import dialog. CSV would trigger paste
ambiguity and comma-in-prose escaping. The calibration summary is free prose full of
commas, so tabs are the safer delimiter.

**Decision: Frame TSV as the practical path, not an error branch.** Because the
connector *cannot* append (a known present limitation, not an intermittent failure),
the spec is worded "append only if the connector supports it; otherwise emit the TSV
row." This keeps the append instruction alive for a future capable connector while
making the TSV row the real behavior today. Alternative considered: delete append
entirely — rejected because it discards a valid future path and overstates the change.

**Decision: Data row by default, header on request.** Default output is lean (just the
one line to paste). The header block is produced on request or when no sheet exists
yet, so a first-time user can seed correct columns. Alternative considered: always emit
header+data — rejected as noisy for the common repeat-session case.

**Decision: Sanitize cells; enforce field count.** Two load-bearing rules:
tab/newline characters inside any cell are replaced with spaces (a stray tab/newline
would shatter or wrap the row), and the data row must have the same field count as the
header including blanks (so empty Perception Alignment / unanswered attributes still
occupy their column). Together these guarantee "one line, N-1 tabs, aligned."

## Risks / Trade-offs

- **User forgets to paste, session lost** → The coach explicitly instructs the user to
  paste the row into "Wine Tasting Log" and, as today, keeps returning the filled grid
  + calibration inline so nothing is silently dropped.
- **Sanitizing prose loses formatting** → Replacing tabs/newlines with spaces slightly
  flattens the calibration summary text; acceptable, since column integrity outranks
  in-cell formatting.
- **Trend lag** → This session's row isn't in the sheet until the user pastes it, so the
  trend reflects prior sessions only. This is correct: the trend is "across recent
  sessions" and this session is the new point being added.
- **Schema drift between header and row** → Both derive from the same Step 5 schema; the
  field-count rule catches misalignment. If the grid gains attributes later, header and
  row grow together by appending at the end.

## Migration Plan

Prompt-only change to `SKILL.md` Step 5. No data migration; existing `Wine Tasting Log`
sheets keep their schema. Rollback is reverting the SKILL.md edit.
