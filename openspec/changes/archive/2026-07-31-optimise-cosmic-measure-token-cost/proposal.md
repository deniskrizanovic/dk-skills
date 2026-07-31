## Why

The 123-epic MA-Pipeline run cost ~7.5M cache-read tokens, and instrumentation of
the run's per-agent transcripts showed 99% of that came from tool-call
round-trips: 137 of 142 measure agents made tool calls (avg 54.9K cache-read
each) while the 5 that made none averaged 2.4K. Only 42 of 162 grep/bash calls
touched the COSMIC manuals — the rest re-discovered data the agent had already
been handed inline (re-`realpath`-ing the coach skill dir, re-reading the source
CSV and output JSON, `rg`-ing the whole project for the epic ID, `fd`-ing the
filesystem for `manuals-indexed`). Each such round-trip re-reads the full agent
context, so eliminating needless tool turns is the single largest available token
saving.

## What Changes

- Add explicit filesystem-access constraints to the measure agent prompt in
  `dk-cosmic-csv-to-cfp/scripts/cosmic-csv-to-cfp.workflow.js`: the epic JSON is
  self-contained; the agent MUST NOT re-read the source CSV, the output JSON, or
  re-resolve the coach/skill directories.
- Provide the resolved absolute `manuals-indexed/` path to each measure agent
  (passed in from the main thread) so no agent runs a filesystem search to locate
  the manuals.
- Gate manual-grepping: the prompt directs agents to cite the injected primer
  directly for the recurring patterns it already covers, and to grep the manuals
  ONLY for an adjudication the primer does not cover — turning manual access from
  a default into an exception.
- These are prompt/plumbing changes only; the movement-counting rules, schema, and
  roll-up math are unchanged. Output for a given input stays semantically the same.

## Capabilities

### New Capabilities
- `cfp-measure-agent-grounding`: defines the measure agent's data-access
  discipline — that each agent measures from its self-contained injected epic +
  primer, is given the resolved manuals path rather than searching for it, and
  reaches for the manuals only for adjudications the primer does not cover.

### Modified Capabilities
<!-- None. cfp-primer-consumption governs that the primer is injected; this change
     adds the agent-grounding discipline around that injection without altering the
     primer-injection requirements themselves. -->

## Impact

- **Code**: `dk-cosmic-csv-to-cfp/scripts/cosmic-csv-to-cfp.workflow.js`
  (measure-prompt text; a new `args.manualsPath` threaded from the main thread).
- **Docs**: `dk-cosmic-csv-to-cfp/SKILL.md` Step 2 (main thread resolves and passes
  the manuals path alongside the primer).
- **Behavior**: fewer tool-call round-trips per measure agent; cache-read reduction
  quantified by a before/after run on a pinned small epics subset. No change to CFP
  numbers, schema, or the two output files.
- **Dependency**: relies on the coach's `manuals-indexed/` layout (already a hard
  dependency of the skill).
