## Why

The intermediate `cosmic-count.json` records data groups only as an inline
`dataGroupRef` string on each data movement, repeated wherever the same object
of interest moves. There is no consolidated view of the distinct data groups a
functional process touches, so the count cannot be audited for object-of-interest
consistency and the distinct objects cannot be handed off as candidate entities
for data modelling.

## What Changes

- Add an optional `dataGroups[]` array to the child `CosmicMeasureOutput`
  schema — one entry per distinct data group the functional process touches,
  each `{ name, description }`.
- The measure agent authors `dataGroups[]` alongside its data movements: it
  emits a `{name, description}` entry per distinct object of interest and keeps
  the movement `dataGroupRef` values consistent with those names. `description`
  is authored (new information the agent supplies), not derivable from the
  movement strings.
- The workflow synthesize step passes `dataGroups[]` through into each
  functional-process block of the canonical `cosmic-count.json`. The workflow
  remains the sole writer of that file.
- The markdown report gains a top-level **Data groups** catalog rendered after
  the per-epic summary, listing every functional process's data groups
  (epic, FP, name, description).
- Additive and backward compatible: `dataGroups[]` is optional; an output that
  omits it still validates.

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `cfp-count-output`: the child schema gains an optional `dataGroups[]` array of
  `{name, description}` per functional process, authored by the measure agent
  and carried through into the canonical report.

## Impact

- `dk-cosmic-cfp-count/cosmic_measure_output.schema.json` — add optional
  `dataGroups[]`.
- `dk-cosmic-cfp-count/scripts/cosmic-cfp-count.workflow.js` — measure-agent
  structured-output schema gains `dataGroups[]`; synthesize passes it through.
- `dk-cosmic-cfp-count/scripts/render_markdown.py` — new top-level Data groups
  section after the per-epic summary.
- `dk-cosmic-cfp-count/tests/test_render_markdown.py` — cover the new section.
- `dk-cosmic-cfp-count/SKILL.md` — document the field and section.
