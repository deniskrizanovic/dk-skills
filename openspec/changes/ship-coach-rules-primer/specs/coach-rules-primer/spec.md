## ADDED Requirements

### Requirement: Coach ships a distilled rules primer artifact

The `dk-cosmic-counting-coach` skill SHALL ship a distilled COSMIC v5.0 rules
primer as a first-class artifact (`rules-primer.md`) in the skill directory. The
primer SHALL be a compact, scope-independent reference covering the recurring
movement-pattern rules (external-system round-trip, CRUD on a persistent object,
confirmation/error Exit, functional-process distinctness, single-triggering-Entry),
each with the rule stated concisely PLUS an exact citation of the form
`manuals-indexed/<slug>/<file>.md#L<start>-L<end>`.

The primer SHALL be CSV-blind and free of any consumer-specific or scope-specific
data — it derives only from the coach's indexed manuals.

#### Scenario: Primer exists and is cited

- **WHEN** the coach skill is installed
- **THEN** `rules-primer.md` exists in the skill directory
- **AND** every rule in it carries a `manuals-indexed/<slug>/<file>.md#L<start>-L<end>` citation
- **AND** the file contains no epic, CSV, or scope-specific content

#### Scenario: Primer covers the recurring rules

- **WHEN** a consumer reads the primer
- **THEN** it finds rules for external-system round-trip, CRUD movements, confirmation/error Exit, functional-process distinctness, and the single-triggering-Entry rule

### Requirement: Primer is version-stamped to the manual index

The primer SHALL carry frontmatter recording the coach manual version and/or the
index generation date it was derived from, so that drift between the primer and a
re-indexed manual corpus is visible to a human reader.

#### Scenario: Version stamp present

- **WHEN** the primer is opened
- **THEN** its frontmatter states the coach manual version and/or index date it was derived from

### Requirement: Documented regeneration procedure

The coach SHALL document a procedure to regenerate `rules-primer.md` from the
current `manuals-indexed/` corpus, wired to the same event that causes primer rot
(manual re-indexing). The procedure SHALL be a deliberate, human-invoked step —
not an automatic per-consumer-run derivation.

#### Scenario: Regeneration is documented next to re-indexing

- **WHEN** a maintainer re-indexes the manuals
- **THEN** the coach SKILL.md documents the step to regenerate the primer and update its version stamp

### Requirement: ADR records the primer decision

The coach SHALL include an architecture decision record (`docs/adr/0002-*.md`)
documenting the choice of a distilled, pre-computed primer over live per-run
re-derivation, framed consistently with ADR 0001 (small fixed corpus favors no
heavy infrastructure; pre-answer predictable questions rather than index for them).

#### Scenario: ADR 0002 exists and references 0001

- **WHEN** the coach `docs/adr/` directory is listed
- **THEN** an ADR file records the distilled-primer decision
- **AND** it distinguishes the primer (pre-computed answer set for predictable questions) from a retrieval index like the vector DB rejected in ADR 0001
