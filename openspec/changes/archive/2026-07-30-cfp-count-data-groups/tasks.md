## 1. Schema

- [x] 1.1 Add optional `dataGroups[]` to `cosmic_measure_output.schema.json` — array of objects `{ name (required), description (required) }`, `additionalProperties:false`; document it as schema-additive.

## 2. Workflow

- [x] 2.1 Add `dataGroups[]` to the measure-agent structured-output schema in `cosmic-cfp-count.workflow.js`.
- [x] 2.2 Update the measure-agent prompt to author one `{name, description}` entry per distinct data group and keep `dataGroupRef` values aligned with those names.
- [x] 2.3 Carry `dataGroups[]` through the synthesize step into each functional-process block, without LLM re-serialization.

## 3. Render

- [x] 3.1 Add a top-level Data groups catalog in `render_markdown.py`, placed after the per-epic summary and before per-epic detail, listing epic, FP, name, description.
- [x] 3.2 Omit the section cleanly when no functional process carries `dataGroups[]`.

## 4. Tests & docs

- [x] 4.1 Extend `tests/test_render_markdown.py` to cover the Data groups section (present and absent cases).
- [x] 4.2 Update `SKILL.md` to document the `dataGroups[]` field and the report section.
- [x] 4.3 Run the render script against `data/cosmic-count.json` to confirm no regression when the field is absent.
