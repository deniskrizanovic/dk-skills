## Context

The 123-epic MA-Pipeline run cost ~7.5M cache-read tokens. Per-agent transcript
instrumentation showed 99% of that came from tool-call round-trips: 137 of 142
measure agents made tool calls (avg 54.9K cache-read each) while the 5 that made
none averaged 2.4K. Only 42 of 162 grep/bash calls actually touched the COSMIC
manuals — the rest re-discovered data the agent already held inline: re-`realpath`
of the coach skill dir, re-reading the source CSV and output JSON, `rg`-ing the
whole project for the epic id, `fd`-ing the filesystem for `manuals-indexed`.

Every tool round-trip re-reads the full agent context (system prompt + injected
primer + epic + prior turns) as cache-read. So each needless turn is not a small
read — it re-bills the whole agent context. The agent already has everything it
needs for the common case; it just isn't told to trust that.

`cfp-primer-consumption` already governs that the primer is injected (no live
Prime agent). This change adds the *access discipline* around that injection.

## Goals / Non-Goals

**Goals:**
- Cut needless measure-agent tool round-trips to near zero for primer-covered
  epics.
- Make manual access an explicit exception path with a pre-resolved location, so
  no agent spends a turn locating the manuals.
- Keep the measurement itself byte-for-byte comparable: same rules, schema,
  roll-up, output files.

**Non-Goals:**
- Changing movement-counting rules, the schema, or the roll-up math.
- Removing the manuals path entirely — genuinely uncovered adjudications still
  need the manuals as the sole rule authority.
- Touching the primer's content or the `cfp-primer-consumption` contract.

## Decisions

**D1 — Add explicit filesystem-access constraints to the measure prompt.**
The prompt states the epic JSON is self-contained and forbids re-reading the CSV,
the output JSON, and re-resolving the coach/skill directories. Rationale: the
agent's default instinct is to "go verify" against the filesystem; naming the
inputs as complete removes that instinct. Alternative considered: a tool
allow-list / sandbox — rejected as heavier plumbing than the win needs, and it
would also block the legitimate exception grep.

**D2 — Pass the resolved absolute `manuals-indexed/` path as `args.manualsPath`.**
The main thread already resolves the coach dir to read the primer; it resolves
the manuals path in the same step and threads it in. Rationale: the workflow
script has no filesystem access, and agents were each independently `fd`-ing for
the manuals. One resolution on the main thread replaces N filesystem searches.
Alternative: let each agent discover it — that is exactly the cost being removed.

**D3 — Gate manual-grepping to uncovered adjudications only.**
The prompt reframes manual access from a default step into an exception: cite the
primer for recurring patterns; grep the manuals only for what the primer does not
cover, recording the exact citation. Rationale: 120 of 162 tool calls were
avoidable; the 42 that touched manuals are the pattern to preserve, not the norm
to encourage.

**D4 — Hard-fail on a missing `manualsPath`, mirroring the primer guard.**
Same reasoning as ADR 0002 for the primer: a missing manuals path means an agent
would fall back to searching, reintroducing the cost. Fail fast on the main
thread rather than silently degrade.

**D5 — Validate the win with a pinned before/after token measurement.**
Run a small fixed epics subset on the unoptimised workflow first, store its
cache-read cost in the change dir, then re-run the same subset post-change and
diff. Rationale: the whole change is a token-cost bet; a pinned fixture makes the
saving an observed number, not an assertion. Alternative — trust the next full
MA-Pipeline run — rejected: too many other variables, no clean baseline.

## Risks / Trade-offs

- [An agent under-consults the manuals for a genuinely uncovered case, guessing
  instead] → The prompt keeps the explicit exception path and the standing rule
  that COSMIC rules are never decided from training; gaps (`CG-<epic>-NN`) remain
  the sanctioned output when uncertain, so the pressure is toward a gap, not a
  guess.
- [The primer drifts and no longer covers a pattern it used to, silently pushing
  more epics onto the exception path] → Acceptable and self-correcting: agents
  fall back to the manuals path (still provided), so correctness holds; only the
  token win erodes, and that surfaces in the next run's cost review.
- [`manualsPath` resolves wrong / stale coach layout] → Hard-fail guard (D4)
  plus the existing hard dependency on the coach's `manuals-indexed/` layout.

## Migration Plan

Prompt/plumbing only — no data migration.
1. Add `args.manualsPath` resolution + validation in the workflow, injected into
   `measurePrompt`.
2. Add the access-constraint + gating language to the measure prompt.
3. Update `SKILL.md` Step 2 so the main thread resolves and passes the manuals
   path alongside the primer.

Rollback: revert the workflow + SKILL.md edits; the previous prompt (agent
free to search) is fully compatible with the same inputs.

## Open Questions

None blocking. The manuals path shape is fixed by the coach's existing
`manuals-indexed/` layout.
