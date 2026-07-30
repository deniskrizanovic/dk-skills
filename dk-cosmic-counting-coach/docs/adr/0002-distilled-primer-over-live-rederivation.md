# Distilled pre-computed primer instead of live per-run re-derivation

A handful of COSMIC v5.0 movement rules recur in *every* functional-size
measurement of *any* scope: the external-system round-trip (Exit + Entry), CRUD
on a persistent object of interest, the single Exit for all confirmation/error
messages, what makes two functional processes distinct, and the
single-triggering-Entry rule. Consumers of the coach (notably
`dk-cosmic-csv-to-cfp`) re-derived these same rules by asking the coach *on every
run*, via a live "Prime" agent. The rules are scope-independent and CSV-blind —
identical no matter the input — so re-deriving them each run spent an agent
round-trip, produced non-deterministic provenance for the primer that travels in
the output, and shipped an unreviewed distillation of the manuals.

We ship the distillation instead as a first-class coach artifact,
`rules-primer.md`: version-stamped, human-reviewed, cited into `manuals-indexed/`,
and regenerated only when the manuals are re-indexed. This is the same philosophy
as ADR 0001 taken one step further. ADR 0001 rejected a vector database because a
small, fixed, rarely-updated corpus does not justify a retrieval index — LLM
vocabulary translation plus grep is sufficient. Here the observation is stronger:
the *questions* are fixed too. When both the corpus and the recurring questions
are known in advance, you do not need a retrieval index **or** a live derivation —
you pre-compute the answer set once and ship it.

## Considered Options

- **Pre-computed distilled primer shipped by the coach (chosen)** — derive once,
  review, version-stamp, commit. Deterministic provenance, no per-run round-trip,
  the distillation is auditable, and the artifact lives next to its source and its
  rot-trigger (re-indexing). Consumers read the file (via the main thread) and
  pass it into their agents unchanged.
- **Live "Prime" agent on every consumer run (rejected)** — re-derives identical
  text each run; non-deterministic `rulesPrimer` provenance, one extra agent
  round-trip per run, and an unreviewed distillation. This is what we are
  replacing.
- **A vector DB / retrieval index over the manuals (rejected in ADR 0001, and
  even less warranted here)** — a primer is a *pre-computed answer set for
  predictable questions*, categorically different from a *retrieval index for
  unpredictable ones*. The recurring rules are predictable; indexing for them is
  strictly more machinery for a strictly narrower need.

## Consequences

- The coach owns the primer and its regeneration procedure (documented in
  SKILL.md next to the `index_manuals` bootstrap). The person who re-indexes is
  prompted to regenerate and re-stamp; the frontmatter `derivedFrom` makes drift
  between primer and corpus visible to a human reader.
- Provenance is deterministic: the `rulesPrimer` carried in a consumer's output is
  byte-identical across runs of the same primer version.
- The primer is the **hot-path cache** for the predictable rules; live grep of the
  manuals remains the **cold-path** for the unpredictable tail — consumers still
  query the coach or grep `manuals-indexed/` for adjudications the primer does not
  cover, so coverage gaps degrade *safe* (missing), never *wrong*.
- Staleness is a human responsibility, not runtime machinery. We deliberately do
  **not** hash-compare the manuals at run time (over-engineered for a rarely-
  changing corpus, consistent with ADR 0001). If the recurring-rule set grows or
  the manuals start changing often, revisit whether regeneration should become an
  automated step.
