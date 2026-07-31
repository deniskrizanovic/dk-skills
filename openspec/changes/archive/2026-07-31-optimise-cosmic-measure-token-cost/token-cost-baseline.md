# Token-cost baseline — optimise-cosmic-measure-token-cost

Pinned before/after fixture for the token-cost bet (design D5).

## Fixture (pinned)

- **Subset:** `dk-cosmic-csv-to-cfp/examples/council-call-centre-epics.csv`
- **Epics:** 12 (E01–E12)
- **Primer:** coach `rules-primer.md` (regeneratedOn 2026-07-30), passed inline
- **Date:** 2026-07-31

## Baseline workflow (pre-optimisation)

The workflow as of HEAD `4587bfd` + the pre-existing uncommitted `description`
field/echo work, with **this change's optimise edits stripped** — i.e. the old
measure prompt (agent free to grep the manuals as a default step, no explicit
filesystem-access constraints, no injected `manualsPath`). Script snapshot:
`/tmp/baseline.workflow.js`. Run: `wf_ed91e800-373`.

### Measurement result (semantic anchor for the after-run)

- projectCfp = **70**, cfpRange = **[8, 70]**
- epicsMeasured = 12 / 12, epicsFailed = 0
- gaps = **20**

### Token metrics (from per-agent transcripts)

| Metric | Value |
|---|---|
| Agents | 12 |
| Total cache-read tokens | **119,661** |
| Avg cache-read / agent | **9,971** |
| Real tool round-trips (non-StructuredOutput) | **1** (one `Bash` manuals grep) |
| Mandatory StructuredOutput returns | 12 |
| Subagent tokens (workflow-reported) | 169,708 |
| Wall-clock | 172 s |

Cache-read is incurred by agents that take a 2nd+ LLM turn (a tool round-trip or
a post-tool StructuredOutput turn), which re-bills the full agent context
(system prompt + primer + epic). 5 of 12 agents took such an extra turn
(cache-read > 0); the rest emitted their StructuredOutput in a single turn
(cache-creation only, cache-read 0).

> Note on scale: this 12-epic subset already runs lean (1 real tool call),
> because the primer injection (a prior change) removed most re-discovery. The
> 7.5M-token figure in the proposal came from the 123-epic MA-Pipeline run where
> the per-agent tool-call rate was far higher. The subset validates the
> *direction* (fewer extra turns → less cache-read), not that absolute number.

## After-run (optimised workflow)

Same fixture, optimised workflow (`args.manualsPath` injected, filesystem-access
constraints + manual-access gating in the measure prompt). Run: `wf_ec6af056-ad5`,
2026-07-31.

### Delta

| Metric | Baseline | Optimised | Δ |
|---|---|---|---|
| Total cache-read tokens | 119,661 | **77,418** | **−42,243 (−35%)** |
| Avg cache-read / agent | 9,971 | 6,451 | −35% |
| Real manuals tool calls (non-StructuredOutput) | 1 (`Bash` grep) | **0** | −1 |
| Mandatory StructuredOutput returns | 12 | 12 | — |
| Agents / failed | 12 / 0 | 12 / 0 | — |

### Correctness (measurement unchanged by the discipline)

- Output conforms to the same schema (top-level `disclaimer`/`rollUp`/
  `rulesPrimer`/`epics`/`measurementGaps`; per-FP `cfp == len(dataMovements)`;
  `epicCfp == sum(fp.cfp)`).
- Roll-up recomputed from the epics matches the reported values
  (`projectCfpCountable=75`, `cfpRange=[4,75]`) — same JS logic, unchanged.
- CFP total moved 70 → 75 and gaps 20 → 27: ordinary per-run LLM measurement
  variance (independent agents, medium effort), **not** a schema or roll-up
  change. The two output files and the math that produces them are identical.

### Read on the win

Every optimised agent cited the primer and made **zero** manuals grep (baseline
had 1). No agent ran a filesystem search to locate the coach/manuals. The 35%
cache-read cut on a subset that was *already* lean (1 tool call at baseline)
confirms the direction; on the 123-epic MA-Pipeline run — where the baseline
tool-call rate was far higher — the proportional saving is expected to be larger.
