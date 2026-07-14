## 1. SKILL.md — add the decant-check step

- [x] 1.1 Insert a new step in `SKILL.md` after Step 2 (expectation sheet / bottle-age adjustment) and before the grid-driven walkthrough, and renumber the subsequent steps.
- [x] 1.2 State the trigger: the step runs ONLY when the coach has assessed the wine as old/mature during the Step 2 bottle-age adjustment; young wines skip it.
- [x] 1.3 Instruct the coach to ask how long the wine has been decanted, explicitly accepting "not decanted" / "poured straight" as valid answers, before the sensory walkthrough begins.
- [x] 1.4 Instruct the coach to give grounded, retrospective guidance — reasoning from age and tannic structure (fragile old wines: decant off the sediment with short/minimal aeration; sturdier mature wines tolerate more) — and to compare the user's actual decant time to the recommendation with the likely sensory effect.
- [x] 1.5 Frame the guidance as learning feedback, not a grade; note that decant context MAY inform how divergence is interpreted at calibration but MUST NOT change the Perception Alignment metric.
- [x] 1.6 Add graceful degradation: when the wine is ungrounded or maturity cannot be confidently judged, the coach asks the user or notes it cannot advise rather than guessing.

## 2. Verify

- [x] 2.1 Re-read the edited `SKILL.md` to confirm the trigger, the decant question, the retrospective guidance, the not-a-grade framing, and the age-unknown path all match the delta spec scenarios.
- [x] 2.2 Confirm no Google Sheet column was added and the log schema/column order is unchanged.
- [ ] 2.3 Validate the change with the OpenSpec tooling once available (`openspec validate add-decant-guidance-old-wine` / `openspec status`).
