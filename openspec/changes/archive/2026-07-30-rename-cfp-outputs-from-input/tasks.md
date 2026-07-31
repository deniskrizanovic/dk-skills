## 1. Derive the stem

- [x] 1.1 In `SKILL.md` Step 1, add a step that derives `STEM` from the input CSV basename with the extension removed (e.g. `STEM=$(basename "<path/to/epics.csv>" .csv)`), alongside the existing `OUT_DIR` resolution.

## 2. Rewrite output paths

- [x] 2.1 In `SKILL.md` Step 2, change the main-thread `Write` target from `$OUT_DIR/cosmic-count.json` to `$OUT_DIR/$STEM-cosmic-count.json`.
- [x] 2.2 In `SKILL.md` Step 3, change the `render_markdown.py` invocation to read `$OUT_DIR/$STEM-cosmic-count.json` and write `$OUT_DIR/$STEM-cosmic-count.md`.
- [x] 2.3 Update the "surface both output paths" line and any output-format prose in `SKILL.md` that names `cosmic-count.json` / `cosmic-count.md` to the derived `<stem>-cosmic-count.*` naming.

## 3. Renderer usage

- [x] 3.1 Confirm `render_markdown.py` takes both input and output paths as arguments (no hard-coded `cosmic-count.*` default); adjust its usage/help text if it references the fixed name.

## 4. Verify

- [x] 4.1 Run the skill (or a dry equivalent) on `examples/council-call-centre-epics.csv` and confirm outputs are named `council-call-centre-epics-cosmic-count.json` / `.md`.
- [x] 4.2 Confirm no `cosmic-count.json` / `cosmic-count.md` fixed-name references remain in `SKILL.md` or `scripts/`.
