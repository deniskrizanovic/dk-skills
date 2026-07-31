## 1. Schema

- [x] 1.1 Add optional `description` (string) to the epic definition in `cosmic_count_report.schema.json` (keep `additionalProperties: false` valid by declaring the property).

## 2. Workflow

- [x] 2.1 Add `description: { type: 'string' }` to `EPIC_SCHEMA.properties` in `cosmic-csv-to-cfp.workflow.js` (optional — not in `required`).
- [x] 2.2 In `measurePrompt`, instruct the agent to echo `epic.description` verbatim into the output `description` field, mirroring the existing `epicName`/`epicId` echo instruction.

## 3. Renderer

- [x] 3.1 In `render_markdown.py` per-epic detail loop, render `e.get("description")` as a blockquote under the epic heading/CFP line, before functional processes; omit the block when absent/empty.

## 4. Docs & examples

- [x] 4.1 Update `SKILL.md` output-format section to list the new `epics[].description` field.
- [x] 4.2 Regenerate the example artifacts under `examples/` to include the description (or hand-add to demonstrate).

## 5. Verify

- [x] 5.1 Validate a sample count JSON (with and without `description`) against `cosmic_count_report.schema.json`.
- [x] 5.2 Run `render_markdown.py` on both samples; confirm description renders when present and is omitted when absent.
