## 1. Rename the skill

- [x] 1.1 `git mv dk-cosmic-cfp-count dk-cosmic-csv-to-cfp`.
- [x] 1.2 `git mv` the workflow file `scripts/cosmic-cfp-count.workflow.js` → `scripts/cosmic-csv-to-cfp.workflow.js`.
- [x] 1.3 Update `SKILL.md` frontmatter `name:` to `dk-cosmic-csv-to-cfp` and the `SKILL_DIR=$(realpath ~/.claude/skills/…)` line.
- [x] 1.4 Update `meta.name` in the renamed workflow file to `dk-cosmic-csv-to-cfp` (or its workflow slug).
- [x] 1.5 Update the SKILL.md Step 2 `scriptPath` to the renamed workflow file.
- [x] 1.6 Update `README.md` skill entry and script paths.

## 2. Rework output location

- [x] 2.1 Rewrite SKILL.md Step 1 to resolve `OUT_DIR` = dirname of the input CSV by default, and prompt/accept a user override.
- [x] 2.2 Rewrite SKILL.md Step 2 to write the JSON to `$OUT_DIR/cosmic-count.json` (flat, no `data/`).
- [x] 2.3 Rewrite SKILL.md Step 3 to render markdown to `$OUT_DIR/cosmic-count.md` (flat, no `outputs/artifacts/`).
- [x] 2.4 Update the output-format section and any `data/cosmic-count.json` / `outputs/artifacts/` mentions in SKILL.md to the flat resolved paths.
- [x] 2.5 Update `render_markdown.py` docstring/usage references that name `data/cosmic-count.json`.
- [x] 2.6 Confirm the final "surface both output paths" instruction reports absolute `$OUT_DIR/*` paths.

## 3. Clean up leaked artifacts

- [x] 3.1 Delete the leaked `data/` and `outputs/` directories under the (renamed) skill.
- [x] 3.2 SKIPPED (optional) — outputs now default to the CSV parent dir; in-skill writes cannot recur by design, so no ignore rule needed.

## 4. Repoint installation

- [x] 4.1 Remove the old `~/.claude/skills/cosmic-cfp-count` and `~/.claude/skills/dk-cosmic-cfp-count` symlinks.
- [x] 4.2 Create `~/.claude/skills/dk-cosmic-csv-to-cfp` → renamed repo dir; verify `SKILL_DIR` resolves.

## 5. Verify

- [x] 5.1 Repo-wide grep for `cosmic-cfp-count` / `dk-cosmic-cfp-count`; confirm no stale references remain (outside this change's archive history).
- [x] 5.2 Run the existing test suite (`tests/test_render_markdown.py`) to confirm the render still passes.
- [x] 5.3 Dry-run: parse a sample CSV, confirm outputs land in the CSV's parent dir and nothing writes inside the skill.
