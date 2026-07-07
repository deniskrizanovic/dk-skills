## Context

The `wine-tasting-coach` skill is a prompt (`SKILL.md`) executed by Claude on the web — there is no code to change, only the instructions the model follows. Step 2 asks the coach to "cite every source" and Step 5 persists those citations into a `Wine Tasting Log` Google Sheet. Neither step requires the coach to have actually fetched a URL before recording it, so fabricated or rotted links reach the sheet and later 404 for the user.

## Goals / Non-Goals

**Goals:**
- Guarantee that any URL written to the log (or shown inline) was actually fetched this session.
- Provide a graceful, honest fallback (descriptive reference) when no verifiable URL exists.
- Make future link rot distinguishable from fabrication via a capture date.

**Non-Goals:**
- Re-validating or repairing URLs in rows written by prior sessions.
- Adding an external link-checking service, tool, or dependency.
- Changing the trust gradient, cross-check, or any tasting/calibration behavior.

## Decisions

- **Verify-before-cite as a hard rule, phrased for a prompt.** Add explicit MUST/ MUST NOT language to Step 2: only a successfully fetched URL may be cited as a URL; otherwise use a descriptive reference (producer + bottle + document type). Chosen over a soft "prefer to verify" because the failure mode (confabulated URLs) only stops under an unambiguous prohibition. Alternative — a post-hoc link-checker tool — rejected as out of scope and unavailable in the web runtime.
- **Descriptive reference as the fallback, not omission.** Keeps the evidence trail (the user still knows *what* informed the sheet) without presenting a dead link as authoritative.
- **New `Source Captured Date` column appended at the end.** Follows the skill's existing schema-evolution rule (append, never reorder) so old rows stay aligned. A single per-row capture date is sufficient because all of a session's sources are fetched in one sitting.

## Risks / Trade-offs

- **Fewer clickable links in the log.** → Acceptable and intended: a truthful descriptive reference beats a plausible dead URL. The whole point is honesty over the appearance of citation.
- **The model may still occasionally emit an unverified URL despite the rule.** → Mitigated by stating the rule in both Step 2 and Step 5 and adding scenarios that make the prohibition testable; residual risk is inherent to prompt-based control.
- **Existing sheets won't have the capture-date column.** → The append-at-end rule handles this; older rows simply have an empty capture-date cell.

## Migration Plan

Edit `wine-tasting-coach/SKILL.md` only (Step 2, Step 5, column schema). No data migration. Prior log rows are untouched; the new column appears the next time the coach appends or creates the sheet.
