## 1. Define the metric in SKILL.md

- [x] 1.1 Add a "Perception Alignment metric" definition to Step 4: what it counts (high-confidence markers where tech sheet and archetype agree), what it excludes (divergent/atypical/low-confidence/ungrounded attributes), and that it is a calibration mirror, not a grade
- [x] 1.2 Document the honesty guardrail: unexpected notes, contradicting a wrong expectation, or flagging the bottle as off/atypical never lower the metric
- [x] 1.3 Document the empty-denominator case: when no high-confidence markers exist, show no metric and explain why rather than emitting a misleading 0

## 2. Update calibration output flow (Step 4)

- [x] 2.1 Amend the "no score" language so it forbids a grade of the taster (letter grade / pass-fail / quality verdict) but permits the alignment metric
- [x] 2.2 Specify that the metric is shown at close alongside Matched/Missed/Focus-next, never replacing it
- [x] 2.3 Specify that the metric is paired with its trend across recent sessions, computed from prior Sheet rows; note trend accrues as sessions are logged

## 3. Update Google Sheet persistence (Step 5)

- [x] 3.1 Add the `Perception Alignment` column to the documented column schema as a trailing column
- [x] 3.2 Add the schema-evolution note: existing sheets lacking the column get it appended at the end, older rows left blank; never reorder existing columns
- [x] 3.3 Confirm the row-append procedure writes the metric value for each new session

## 4. Verify against spec

- [x] 4.1 Walk each spec scenario (high-confidence-only, honesty guardrail, atypical exclusion, metric-as-mirror, alignment-column append) and confirm SKILL.md covers it
- [x] 4.2 Run `openspec validate add-calibration-alignment-score` and resolve any issues
