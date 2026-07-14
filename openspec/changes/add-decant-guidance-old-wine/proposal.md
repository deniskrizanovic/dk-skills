## Why

The coach already reasons about a wine's age when it builds the expectation sheet (aged reds shift to garnet, gain tertiary/dried-fruit notes, etc.), but it never asks how the bottle was *served*. For an older wine, decanting is a make-or-break decision: mature bottles throw sediment that must be separated, and their fragile tertiary aromatics can be blown off by too much air. A user who over-decants a 25-year-old red may taste a faded, hollow wine and wrongly conclude their palate missed the expected aromas — when the real cause was preparation. Capturing decant time and giving grounded guidance turns an invisible variable into a coaching moment and keeps calibration honest.

## What Changes

- Add a **decant check** to the walkthrough that triggers **only when the coach assesses the wine as old/mature** (using the same bottle-age reasoning already in the vintage/bottle-age adjustment step). Young wines skip the check.
- When triggered, the coach asks the user **how long the wine has been decanted for** (accepting "not decanted" / "poured straight from the bottle" as valid answers) before the sensory walkthrough.
- The coach then provides **grounded, retrospective guidance** on how long it thinks the wine *should* have been decanted — reasoning from the wine's age and tannic structure (older, fragile wines: decant off the sediment with short/minimal aeration; sturdier mature wines tolerate more), and **compares** the user's actual decant time to the recommendation, explaining the likely sensory effect.
- The guidance is framed as **learning feedback, not a grade**, consistent with the rest of the skill; the decant context MAY inform how divergence is interpreted at calibration but MUST NOT change the Perception Alignment metric.
- Handle the **age-unknown / ungrounded** case gracefully (ask or note the uncertainty rather than guessing).
- Update `wine-tasting-coach/SKILL.md` to add the step.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `wine-tasting-coach`: gains a **decant-check** behavior for aged wines — asking decant duration and giving grounded, retrospective decant guidance before the sensory walkthrough. Related to the existing "Vintage and bottle-age adjustment" and "Grid-driven walkthrough" requirements.

## Impact

- `wine-tasting-coach/SKILL.md` — a new step inserted after Step 2 (expectation sheet / bottle-age adjustment) and before the grid-driven walkthrough; subsequent step numbering shifts accordingly.
- Behavior only; no new tools or dependencies.
- **No new Google Sheet column** — this is an in-conversation coaching step, so the log schema is unchanged and existing rows are unaffected.
