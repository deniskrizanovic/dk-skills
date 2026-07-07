## Why

The tasting grid has **two** attributes both named **"Intensity"** — one under
Sight → Color (colour intensity) and one under Nose → Impression (aromatic intensity).
When each grid attribute becomes a column in the `Wine Tasting Log` sheet (and the new
tab-delimited row), the two produce **identical column headers**. "Map each observation
to the existing column by header name" is then ambiguous, and a header row would carry a
duplicate `Intensity` — a latent misalignment risk in the persistence schema.

## What Changes

- Rename the two colliding grid attributes to unique names so both the walkthrough and
  the persisted column schema are unambiguous:
  - Sight → Color: `Intensity` → **`Color Intensity`**
  - Nose → Impression: `Intensity` → **`Aroma Intensity`**
- Apply the rename in **both** grid copies: the source-of-truth
  `reference/wine-tasting-grid.md` and the embedded grid in `SKILL.md` (they must stay in
  sync).
- Update the Step 5 column-schema description in `SKILL.md` where it lists example
  attribute names, so the enumerated columns match the renamed attributes.
- Note the migration nuance for existing sheets: because the schema rule only ever
  **appends** columns and never renames in place, an existing `Wine Tasting Log` created
  before this change keeps its single `Intensity` column; the coach treats
  `Color Intensity` / `Aroma Intensity` as the current names and appends any genuinely
  new column at the end rather than reordering.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `wine-tasting-coach`: The "Persist each tasting to a Google Sheet library" requirement
  is refined so grid-attribute column headers are **unique** — the two "Intensity"
  attributes map to distinct `Color Intensity` and `Aroma Intensity` columns, removing
  the duplicate-header ambiguity in both append and tab-delimited output.

## Impact

- `wine-tasting-coach/reference/wine-tasting-grid.md` — rename both `Intensity` rows.
- `wine-tasting-coach/SKILL.md` — rename both `Intensity` rows in the embedded grid and
  update the Step 5 schema example enumeration.
- `openspec/specs/wine-tasting-coach/spec.md` — persist requirement refined on archive.
- No code dependencies. Prompt/skill behavior + reference-doc change only.
