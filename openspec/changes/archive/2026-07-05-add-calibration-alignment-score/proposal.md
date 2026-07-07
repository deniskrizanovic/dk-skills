## Why

The wine-tasting-coach gives rich qualitative calibration feedback but deliberately withholds any number, so a taster has no way to see whether their palate is actually calibrating over time. A carefully-scoped calibration alignment metric — tracked session over session — turns "am I getting better?" from a feeling into visible progress, without reintroducing the judgemental "grade" the skill rightly banned.

## What Changes

- Introduce a per-session **Perception Alignment** metric: of the *high-confidence* expected markers (where the tech sheet and style archetype agree), how many the taster registered.
- **BREAKING (principle reversal):** the existing "no numeric grade" rule is amended. A number is now permitted, but it MUST be a calibration mirror (you vs. your past self), never a grade of the taster and never a quality verdict on the session.
- Score **only high-confidence attributes**; divergent, atypical, or low-confidence attributes are excluded from the count and remain qualitative.
- Add an **honesty guardrail**: reporting something the expectation missed, contradicting a wrong expectation, or flagging the bottle as off/atypical NEVER lowers the metric. Honest divergence is neutral, not a miss.
- Show the metric at the close of every session **alongside** the existing Matched/Missed/Focus-next feedback (not replacing it), and **paired with its trend** across recent sessions rather than as a standalone verdict.
- Persist the metric to the `Wine Tasting Log` Google Sheet as a new trailing column so the trend can be computed from history.

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `wine-tasting-coach`: amend the "Calibration feedback at close" requirement to permit a calibration alignment metric (removing the blanket "no numeric grade" prohibition, replacing it with a "no grade of the taster" rule); add a new requirement defining the Perception Alignment metric (scope, exclusions, honesty guardrail, trend display); extend the Google Sheet persistence requirement with the new trailing column.

## Impact

- **Specs:** `openspec/specs/wine-tasting-coach/spec.md` (delta).
- **Skill runtime:** `wine-tasting-coach/SKILL.md` — Step 4 (compute + display the metric with trend) and Step 5 (new Sheet column, schema-evolution note).
- **Data:** the `Wine Tasting Log` sheet gains one trailing column; existing rows leave it blank per the established add-at-end evolution rule.
- No new external dependencies; relies on the Google Drive connector already required.
