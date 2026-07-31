## Why

The `dk-cosmic-csv-to-cfp` workflow re-derives the same generic COSMIC v5.0 rules
primer on **every** run via a live `Prime` agent that queries the coach. The primer
is CSV-blind and scope-independent — identical for any Salesforce scope — so
re-deriving it each run spends an agent round-trip, yields non-deterministic
`rulesPrimer` provenance, and ships an unreviewed distillation of the manuals. The
distillation is a product of the **coach's** manuals, not of any one consumer, and
belongs where its source and its rot-trigger (manual re-indexing) live.

## What Changes

- The **coach** ships a distilled, version-stamped COSMIC rules primer as a
  first-class artifact (`rules-primer.md`), regenerated from `manuals-indexed/`
  when the manuals change — human-reviewed, deterministic, cited.
- The coach gains a **regenerate-primer** procedure wired to the same event that
  causes primer rot (re-indexing), stamping the coach manual version/date it was
  derived from.
- **BREAKING**: `dk-cosmic-csv-to-cfp` drops the every-run `Prime` phase. The main
  thread reads the coach's `rules-primer.md` and passes it as `args.primer`; the
  workflow **hard-fails** if `args.primer` is absent (no silent live derivation).
- Add ADR `0002` to the coach documenting distilled-primer-over-live-re-derivation,
  consistent with ADR `0001` (small fixed corpus → no heavy infra; pre-answer the
  predictable questions rather than index for them).

## Capabilities

### New Capabilities
- `coach-rules-primer`: the coach ships and maintains a distilled, version-stamped
  COSMIC rules primer derived from its indexed manuals, with a documented
  regeneration procedure and an ADR recording the decision.
- `cfp-primer-consumption`: `dk-cosmic-csv-to-cfp` consumes the coach's shipped
  primer via `args.primer` (main-thread read, hard-fail if absent) instead of a
  live per-run `Prime` phase.

### Modified Capabilities
<!-- No existing spec captures the primer flow; both are new capabilities. -->

## Impact

- **Coach skill** (`dk-cosmic-counting-coach/`): new `rules-primer.md` artifact,
  new regeneration step in SKILL.md, new `docs/adr/0002-*.md`. Possible new script
  under `scripts/` for regeneration.
- **CSV-to-CFP skill** (`dk-cosmic-csv-to-cfp/`): `scripts/cosmic-csv-to-cfp.workflow.js`
  loses the `Prime` phase and adds an `args.primer` hard-fail guard; SKILL.md Step 2
  gains a main-thread primer read + pass.
- **Dependency**: the csv skill's hard dependency on the coach becomes a dependency
  on a coach *file*, not just coach behavior.
- **Reproducibility**: `rulesPrimer` in output JSON becomes deterministic across runs.
