## 1. Renderer

- [x] 1.1 In `dk-cosmic-csv-to-cfp/scripts/render_markdown.py`, replace the catalog aggregation (lines ~94-100): build an insertion-ordered `dict` keyed by data group `name`; on first sight record `{"descriptions": [], "refs": []}`; always append the `Epic/FP` ref (`epicId + "/" + fpLabel`); append the description only if not already in `descriptions` (distinct only).
- [x] 1.2 Emit the table with header `| Data group | Functional processes | Description |`, iterating the map's items sorted alphabetically by name; comma-join (`, `) the refs into one cell and join distinct descriptions with ` / ` into the description cell; keep the `if <rows>` guard so the section is omitted when empty.

## 2. Docs & example

- [x] 2.1 Update the SKILL.md catalog prose (~lines 143-147) to describe the new layout: name-keyed, deduplicated, comma-joined `Epic/FP` cell, alphabetical.
- [x] 2.2 Regenerate `dk-cosmic-csv-to-cfp/examples/cosmic-count.md` from `examples/cosmic-count.json` via `render_markdown.py`; confirm `Booking` and `SMS Confirmation` each collapse to one row.

## 3. Tests

- [x] 3.1 Update `tests/test_render_markdown.py::test_render_data_groups_section_present` to assert the new header and a deduplicated row (e.g. a name used by two FPs shows both `Epic/FP` refs in one cell); keep the omit-when-absent test.
- [x] 3.2 Add a test for conflicting descriptions: two FPs carry the same data group name with different descriptions → one row, description cell shows both joined with ` / ` in document order.
- [x] 3.3 Run the test suite (`pytest dk-cosmic-csv-to-cfp/tests/`) and confirm green.
