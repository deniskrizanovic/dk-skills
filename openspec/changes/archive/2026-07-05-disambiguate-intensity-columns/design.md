## Context

The tasting grid lists attributes in tables; each attribute becomes a column in the
`Wine Tasting Log` sheet and a field in the tab-delimited row. Two attributes share the
name **"Intensity"**: Sight → Color (colour intensity) and Nose → Impression (aromatic
intensity). Identical headers make "map each observation to the existing column by header
name" ambiguous and risk a duplicate header in the emitted header row. This is a latent
schema bug surfaced by the new TSV output; the fix is a rename in the grid itself.

## Goals / Non-Goals

**Goals:**
- Give every grid-attribute column a unique header.
- Keep the two grid copies (reference source-of-truth + embedded in `SKILL.md`) in sync.
- Preserve alignment for `Wine Tasting Log` sheets created before the rename.

**Non-Goals:**
- Renaming any other attribute or restructuring the grid.
- Migrating data in existing sheets (no automated rename of old columns).
- Changing the walkthrough flow or calibration logic.

## Decisions

**Decision: Rename the attributes, don't alias at the persistence layer.** The cleanest
fix is unique names at the source — `Color Intensity` and `Aroma Intensity` — so the
walkthrough, the header row, and column mapping all agree with no special-casing.
Alternative considered: keep "Intensity" in the grid but disambiguate only when building
headers (e.g. prefix by section) — rejected because it splits naming logic between the
grid and Step 5, and the coach speaks the attribute names aloud during the walkthrough
anyway, so clarity there is a bonus.

**Decision: Names chosen to match how each is spoken.** "Color Intensity" and
"Aroma Intensity" read naturally in the walkthrough ("how intense is the colour?" /
"how intense is the nose?") and sort near their sibling attributes.

**Decision: No in-place migration; rely on the append-only schema rule.** The existing
schema rule already forbids renaming/reordering existing columns. A pre-rename sheet
keeps its lone "Intensity" column; the coach uses the new names going forward and only
appends genuinely new columns at the end. This keeps old rows aligned without a
data-migration step. (In practice sheets are pasted manually today, so users control
their own headers regardless.)

## Risks / Trade-offs

- **Existing sheet has a legacy "Intensity" header** → The append-only rule and the
  "predates the rename" scenario cover it: no in-place rename, older rows stay aligned.
  Trade-off: a long-lived sheet could carry both a legacy "Intensity" and the new columns
  if the user pastes a new header; acceptable and user-controlled given manual paste.
- **Grid copies drift** → The rename must land in both `reference/wine-tasting-grid.md`
  (source of truth) and the embedded `SKILL.md` grid; a task explicitly verifies both.

## Migration Plan

Prompt/reference-doc edit only. No data migration. Rollback is reverting the grid edits.
