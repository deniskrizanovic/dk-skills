## Why

The epics CSV carries a `Description` column — the requirement text the whole measurement rests on — but it is dropped after measurement: the count JSON never stores it, so the markdown report can't show the reader WHAT each epic was measured against. A reviewer sizing an epic's CFP has no way, in the report, to see the source requirement without re-opening the CSV.

## What Changes

- Carry each epic's `description` (from the CSV, already reaching the measure agent) through into the count JSON's `epics[]` objects.
- Surface the description in the markdown report's per-epic detail section (and optionally summary), so the requirement text sits next to its measurement.
- Widen the `CosmicCountReport` epic schema to allow the new `description` field (currently `additionalProperties: false`).

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `cfp-count-output`: the report envelope's per-epic object gains a `description` field, and the markdown renderer must display it per epic.

## Impact

- `dk-cosmic-csv-to-cfp/cosmic_count_report.schema.json` — epic definition gains optional `description`.
- `dk-cosmic-csv-to-cfp/scripts/cosmic-csv-to-cfp.workflow.js` — `EPIC_SCHEMA` gains `description`; measure agent echoes the input description into its output; synthesize passes it through.
- `dk-cosmic-csv-to-cfp/scripts/render_markdown.py` — per-epic detail renders the description.
- `dk-cosmic-csv-to-cfp/SKILL.md` — output-format docs note the new field.
- Example artifacts under `dk-cosmic-csv-to-cfp/examples/` may be regenerated.
- Non-breaking: `description` is optional; existing count JSON without it still validates and renders.
