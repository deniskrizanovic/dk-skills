## Context

The wine-tasting-coach deliberately gives only qualitative calibration feedback — its spec explicitly forbids a numeric grade, on the principle that "divergence from the expectation is information, not failure." The user wants a **calibration-over-time** signal: a way to see their palate improving session over session. This is spirit-aligned (it serves the learning goal) but sits directly on top of the banned "score," so the design's whole job is to build a number that is a *mirror* (you vs. your past self) and never a *judge* (grade of the taster).

The skill runs on Claude web with an embedded grid and a `Wine Tasting Log` Google Sheet as durable state. The Sheet already anticipates additive schema evolution (the `Source Captured Date` column precedent), which the trend feature reuses.

## Goals / Non-Goals

**Goals:**

- A per-session **Perception Alignment** metric that trends over sessions.
- Keep the metric honest: it measures *detection of what was genuinely there to detect*, not *agreement with a possibly-wrong expectation*.
- Show it every session, but framed as a calibration mirror beside the existing qualitative feedback.
- Persist it to the Sheet so the trend is computable from history.

**Non-Goals:**

- Grading the taster, the session, or the wine. No letter grades, pass/fail, or quality verdict.
- Changing the priming-first walkthrough flow (see decision below).
- Scoring bottle typicality (an alternative interpretation, explicitly out of scope).
- Any local-filesystem or non-Sheet storage.

## Decisions

**Decision: Count only high-confidence markers (tech sheet ∧ archetype agree).**
The metric's denominator is limited to attributes where both grounded sources agree. Rationale: this is the load-bearing guardrail. Because the walkthrough primes the category before the user answers, a naive score would largely measure *agreement/suggestibility*. Restricting to high-confidence markers means "agreeing" is usually agreeing with something genuinely present, so the incentive to just say "yes" is far less corrosive. It also reuses the trust gradient already in the skill.
_Alternative considered:_ score the full expectation sheet — rejected, it penalises a correct palate on an atypical bottle and fights the skill's own "expectations can be wrong" stance. _Also considered:_ self-consistency only (no comparison) — rejected as too fuzzy to trend meaningfully.

**Decision: Keep the current priming-first flow.**
We do not add a blind pre-priming pass. Rationale: the user chose to preserve the existing flow; the high-confidence-only guardrail is what keeps the metric honest instead. Trade-off acknowledged below.

**Decision: Show the number every session, paired with its trend.**
Display at close, alongside Matched/Missed/Focus-next, always with the recent-session trend ("6/8 — up from your last three") rather than as a standalone figure. Rationale: the user wants immediate feedback; pairing with trend + qualitative feedback keeps it a mirror, not a headline grade.
_Alternative considered:_ log silently / show only as trend — more conservative but denies the immediate feedback the user asked for.

**Decision: Persist as one trailing column, computed trend.**
Add a single `Perception Alignment` column at the end of the Sheet schema. The trend is derived at display time from prior rows; no separate running-average column. Rationale: matches the established add-at-end evolution rule, keeps the schema simple, and avoids storing a derived value that could drift from the raw history.

## Risks / Trade-offs

- **Priming contaminates the signal** → the metric partly measures agreement/suggestibility rather than unaided detection. Mitigation: high-confidence-only denominator; frame explicitly as calibration-over-time, and the trend (not the absolute value) is what matters.
- **A visible number re-gamifies the session** → tasters chase the number by agreeing. Mitigation: honesty guardrail (divergence never lowers it), small honest denominator, and always shown beside qualitative feedback + trend, never as a verdict.
- **This reverses a stated principle** → the "no numeric grade" rule. Mitigation: the change amends that requirement openly in the spec rather than sneaking a number past it; the amended rule still bans grades of the taster.
- **Small/empty denominator** → some sessions have few or zero high-confidence markers (ungrounded bottles). Mitigation: when the denominator is empty, the coach shows no metric for that session and says why, rather than emitting a misleading 0.
- **Trend needs history** → early sessions have no trend. Mitigation: show the raw count and note that the trend accrues as more sessions are logged.

## Open Questions

- Exact display format of the trend (last-N average vs. sparkline-style list) — left to implementation; spec only requires "paired with its trend across recent sessions."
- How many recent sessions define "the trend" — a reasonable default (e.g. last 3–5) can be chosen at implementation without a spec change.
