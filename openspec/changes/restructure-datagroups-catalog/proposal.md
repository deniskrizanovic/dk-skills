## Why

The Data groups catalog in `cosmic-count.md` is keyed by epic + functional process, so a data group touched by several processes repeats once per row (e.g. `Booking` appears three times). This makes the catalog read as a movement list rather than a catalog of distinct data groups. Leading with a deduplicated data group name — and collecting every process that uses it in one cell — turns it into the reference table it was meant to be.

## What Changes

- **BREAKING** (render layout only): Restructure the `## Data groups` table in `render_markdown.py`.
  - Data group **name** becomes the first column.
  - Rows are **deduplicated by name only** — one row per distinct data group name across the whole report.
  - When data groups share a name but carry different descriptions, **all distinct descriptions are joined with ` / `** (document order) into the single description cell.
  - The functional processes that use a data group are **comma-joined as `Epic/FP`** references in a single cell.
  - Rows are sorted **alphabetically** by data group name.
  - New column order: `Data group | Functional processes | Description`.
- Update the SKILL.md prose describing the catalog to match the new layout.
- No change to `cosmic-count.json`, the JSON schemas, or the workflow — this is a render-only change.

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `cfp-count-output`: The "Data-groups catalog in markdown report" requirement changes — the catalog is keyed by deduplicated data group name (first column), with using processes collected into one comma-joined `Epic/FP` cell, distinct descriptions joined with ` / `, and rows sorted alphabetically, replacing the prior per-(epic, FP) row layout.

## Impact

- `dk-cosmic-csv-to-cfp/scripts/render_markdown.py` — the `## Data groups` catalog block (~lines 91-107).
- `dk-cosmic-csv-to-cfp/SKILL.md` — the prose describing the catalog layout (~lines 143-147).
- `dk-cosmic-csv-to-cfp/examples/cosmic-count.md` — regenerated example output.
- `dk-cosmic-csv-to-cfp/tests/` — any test asserting the old catalog header/rows.
