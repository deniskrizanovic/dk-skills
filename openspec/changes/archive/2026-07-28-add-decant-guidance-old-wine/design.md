## Context

The `wine-tasting-coach` skill is a prompt (`SKILL.md`) executed by Claude on the web — there is no code, only the instructions the model follows. Step 2 already builds a grounded expectation sheet and performs a vintage-climate and **bottle-age** adjustment, so by the time the walkthrough starts the coach has already assessed whether the wine is young or mature. Decanting sits between "bottle assessed" and "wine tasted": it is a preparation variable that materially changes what the taster perceives, and for older wines the correct call is non-obvious (sediment separation plus short aeration, versus the long aeration young tannic wines want). Nothing in the skill currently surfaces it.

## Goals / Non-Goals

**Goals:**
- Ask how long an *old* wine was decanted, before the sensory walkthrough, so the answer can inform interpretation.
- Give grounded, retrospective decant guidance reasoned from age + structure, and compare it to what the user actually did.
- Keep the guidance framed as learning feedback, never a grade, consistent with the calibration philosophy.

**Non-Goals:**
- Triggering the check for young wines (the user's request is scoped to old wines; young-wine aeration advice is out of scope).
- Adding a Google Sheet column for decant time or changing the log schema.
- Letting decant context alter the Perception Alignment metric.
- Prescribing exact minute counts as universal rules — guidance is per-bottle reasoning, not a lookup table.

## Decisions

- **Trigger on the coach's own age assessment, reusing Step 2.** The decant check fires when the coach has judged the wine old/mature during the bottle-age adjustment — no new age heuristic is introduced, so "old" stays consistent with the rest of the skill. Alternative (a fixed year threshold) rejected: age-worthiness depends on grape/structure, which the coach already reasons about.
- **Place the step after the expectation sheet, before the walkthrough.** Decanting is a serving decision that shapes the nose and palate the user is about to describe, so asking first lets the coach flag "a faded nose here may be over-decanting, not a palate miss" during calibration. Asking after the walkthrough would lose that framing.
- **Ask first, then advise (retrospective "should've").** The wine is already open, so the guidance is comparative: capture the user's actual decant time, then state the recommended approach and the likely sensory consequence of the delta. This matches the user's framing ("how long it thinks I should've decanted for").
- **Guidance leans to short/gentle for fragile old wines.** Mature bottles throw sediment (decant gently off the lees) and can lose delicate tertiary aromatics to excess air, so the default recommendation for an old wine trends toward a short decant / decant-and-serve, scaled up only when the wine is still structured/tannic. Framed as reasoning, not a fixed number.
- **Decant context informs calibration but never the metric.** Consistent with the honesty guardrail: a preparation artifact (over-/under-decanting) is explanatory context for divergence, recorded qualitatively — it does not lower Perception Alignment.
- **Graceful degradation when age is unknown.** If the wine is ungrounded or the coach cannot confidently judge maturity, it either asks the user or notes it cannot advise on decanting rather than guessing.

## Risks / Trade-offs

- **The model may give a decant number as if it were a hard rule.** → Mitigated by phrasing guidance as age-plus-structure reasoning and by a scenario asserting it is per-bottle, not a universal minute count.
- **Over-triggering on borderline-age wines.** → The trigger is tied to the coach's existing maturity assessment; borderline cases fall to the graceful/ask path rather than a forced check.
- **Scope creep into young-wine aeration advice.** → Explicit non-goal; the requirement and scenarios only cover old wines.

## Migration Plan

Edit `wine-tasting-coach/SKILL.md` only: insert the decant-check step after Step 2 and before the walkthrough, renumbering later steps. No data migration, no schema change; the `Wine Tasting Log` sheet and existing rows are untouched.
