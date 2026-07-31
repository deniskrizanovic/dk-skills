## 0. Baseline: capture pre-change token cost

- [x] 0.1 Choose a small fixed epics subset as the before/after fixture (e.g. the `examples/council-call-centre-epics` set) and pin it for both runs
- [x] 0.2 Run the current (unoptimised) workflow on the subset; record total cache-read tokens, per-measure-agent average, and tool-call count from the run transcripts/journal
- [x] 0.3 Store the baseline (subset id, total + avg cache-read, tool-call count, date) in the change dir as `token-cost-baseline.md`

## 1. Thread the manuals path into the workflow

- [x] 1.1 In `dk-cosmic-csv-to-cfp/scripts/cosmic-csv-to-cfp.workflow.js`, read `args.manualsPath` alongside `args.primer`
- [x] 1.2 Hard-fail with a clear error when `args.manualsPath` is missing or blank, mirroring the existing `args.primer` guard (reference ADR 0002 rationale)
- [x] 1.3 Update the `args` documentation comment block to describe `manualsPath` (resolved absolute path to the coach's `manuals-indexed/`, supplied by the main thread)

## 2. Constrain and gate filesystem access in the measure prompt

- [x] 2.1 Add explicit filesystem-access constraints to `measurePrompt`: the injected epic JSON is self-contained; the agent MUST NOT re-read the source CSV, MUST NOT read the output JSON, and MUST NOT re-resolve the coach/skill directories
- [x] 2.2 Inject `manualsPath` into `measurePrompt` and direct any manual grep to use that path directly (no filesystem search to locate `manuals-indexed/`)
- [x] 2.3 Reframe manual access as an exception: cite the injected primer for its covered recurring patterns; grep the manuals ONLY for an adjudication the primer does not cover, recording the exact `manuals-indexed/<slug>/<file>.md#L..` citation
- [x] 2.4 Confirm the movement-counting method, `EPIC_SCHEMA`, and the JS roll-up are left unchanged

## 3. Update the skill to resolve and pass the manuals path

- [x] 3.1 In `dk-cosmic-csv-to-cfp/SKILL.md` Step 2, have the main thread resolve the absolute `manuals-indexed/` path and pass it as `args.manualsPath` alongside `args.primer`

## 4. Verify

- [x] 4.1 `node --check dk-cosmic-csv-to-cfp/scripts/cosmic-csv-to-cfp.workflow.js` passes
- [x] 4.2 Dry-review the injected prompt for a sample epic: constraints present, `manualsPath` interpolated, gating language present
- [x] 4.3 Re-run the same pinned subset (task 0.1) on the optimised workflow; confirm output JSON conforms to the same schema and the roll-up numbers are computed by the same logic; capture the same token metrics and compare against `token-cost-baseline.md`, recording the delta; sanity-check that measure agents make no manuals search for primer-covered epics
