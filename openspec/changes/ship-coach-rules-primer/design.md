## Context

`dk-cosmic-csv-to-cfp` runs a 3-phase workflow: **Prime** (one agent asks the coach
for the recurring COSMIC rules, returns a compact primer), **Measure** (one agent
per epic, primer injected into each), **Synthesize** (JS roll-up). The Prime agent
runs on every invocation.

Established during exploration:
- The primer is **CSV-blind and scope-independent** — Prime never sees epic data;
  primer and epics meet only at the measure agent. So it is identical for any
  Salesforce scope.
- The primer is a **distillation of the coach's `manuals-indexed/` corpus**; its
  citations point into the coach. It rots only when the coach re-indexes.
- Therefore its natural owner is the **coach**, as a shared artifact reusable by any
  COSMIC measurer — not a private cache inside one consumer.
- Workflow scripts have **no filesystem access** (Workflow tool constraint), so the
  workflow cannot read a shipped file itself; the main thread must.
- Coach ADR 0001 rejected a vector DB: small fixed corpus → LLM-translate-then-grep,
  no heavy infra. A pre-computed primer is the same philosophy taken further.

## Goals / Non-Goals

**Goals:**
- Move primer authorship from a live per-run agent to a shipped, version-stamped,
  human-reviewed coach artifact.
- Make `rulesPrimer` provenance deterministic across runs.
- Remove one agent round-trip per run.
- Record the decision in a coach ADR alongside 0001.

**Non-Goals:**
- No runtime auto-detection of primer staleness (no manual hashing at run time). The
  operator owns regeneration; a version stamp makes drift visible, nothing more.
- No change to how the primer is *injected* into measure agents — same text, same
  place in the prompt.
- No fallback to live derivation. Missing primer is a hard fail.
- No change to the coach's Q&A / validator / lookup / tutor modes.

## Decisions

### D1 — Primer lives in the coach, not the csv skill
The primer distills the coach's manuals and is reusable by every measurer. Owning it
in the coach puts the artifact next to its source and its rot-trigger (re-indexing).
*Alternative:* cache inside `dk-cosmic-csv-to-cfp` — rejected: hides a shared asset
in one consumer, and violates that skill's own "never write inside the skill dir"
guardrail if cached at runtime.

### D2 — Main thread reads the file; workflow consumes `args.primer`
Workflow scripts cannot touch the filesystem. The main thread (SKILL.md step) reads
`rules-primer.md` and passes it as `args.primer` alongside `{epics}`. The workflow
injects it exactly as it injected the Prime agent's return value today.
*Alternative:* keep a Prime phase but have it read the file — impossible; the
workflow has no fs access.

### D3 — Hard-fail on missing primer (no live fallback)
If `args.primer` is empty, throw before any measure agent runs. A missing primer
means unmeasured/under-grounded epics — worse than stopping. This is a conscious
departure from the coach-degradation "never blocks" ethos, justified because the
primer is load-bearing for citation grounding, and per the user's explicit "stop"
choice during exploration.
*Alternative:* fall back to a live Prime agent when the file is absent — rejected by
the user; reintroduces non-determinism and the very round-trip we are removing.

### D4 — Version-stamp the primer; regen wired to re-indexing
Primer frontmatter records the coach manual version / index date it was derived
from. The coach's regeneration step is documented next to the `index_manuals`
bootstrap, so the person who re-indexes is prompted to regen. Drift stays visible
without runtime machinery.
*Alternative:* runtime hash comparison of the manuals — rejected as over-engineered
for a rarely-changing corpus, consistent with ADR 0001's reasoning.

### D5 — Reuse the existing Prime prompt as the regeneration source
The current Prime agent prompt (workflow lines ~101-120) already derives exactly this
primer. Repurpose it as the coach's regeneration procedure (a documented one-shot),
so there is a single source of the primer-derivation prompt rather than two.

### D6 — Domain-neutral primer
The primer is authored neutral (pure COSMIC rules), not Salesforce-flavored. Consumers
carry domain context via the epic JSON and their own measure prompt. Keeps ownership
clean and the artifact reusable beyond Salesforce scopes.

## Risks / Trade-offs

- **Silent staleness if operator forgets to regen** → version stamp in frontmatter
  makes the derived-from version visible; regen step documented at the re-index site.
- **Citation line-number rot after re-index** → same mitigation; the stamp flags a
  mismatch, and measure agents still grep manuals for anything the primer misses, so
  it degrades safe (missing coverage), not wrong.
- **Tighter coupling: csv skill now depends on a coach *file*** → the dependency was
  already hard ("sole rule authority"); this makes it explicit and honest. Hard-fail
  surfaces a missing file loudly.
- **Neutral primer may miss domain-specific adjudications** → measure agents grep the
  manuals for anything the primer does not cover; primer is the hot-path cache, live
  grep remains the cold-path (mirrors ADR 0001's retrieval for the unpredictable tail).

## Migration Plan

1. Author `rules-primer.md` in the coach (run the repurposed Prime prompt once,
   review, commit with version stamp).
2. Add regeneration procedure + ADR 0002 to the coach.
3. Update `dk-cosmic-csv-to-cfp` SKILL.md Step 2: main thread reads the coach primer,
   passes `args.primer`.
4. Edit the workflow: delete the Prime phase, add the `args.primer` hard-fail guard,
   inject `args.primer` where the Prime return value was used.
5. Update the csv skill's docs/tests referencing the Prime phase.

Rollback: restore the Prime phase block in the workflow and drop the `args.primer`
guard; the coach artifact can remain (harmless if unused).

## Open Questions

- Exact filename/location convention for the primer within the coach (root vs a
  `docs/` or `primer/` subdir) — decide at apply time to match coach conventions.
- Whether the regeneration step becomes a script under `scripts/` or stays a
  documented manual agent invocation in SKILL.md.
