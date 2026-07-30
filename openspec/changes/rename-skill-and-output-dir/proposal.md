## Why

The skill writes its outputs (`data/cosmic-count.json`, `outputs/artifacts/cosmic-count.md`) to relative paths that resolve inside the skill's own directory, polluting the installed skill with per-run artifacts. It also carries a name (`dk-cosmic-cfp-count`) that undersells what it does — turn an epics CSV into a CFP count.

## What Changes

- **BREAKING** Rename the skill `dk-cosmic-cfp-count` → `dk-cosmic-csv-to-cfp`. The old invocation name `cosmic-cfp-count` stops resolving.
  - Rename the skill directory (via `git mv` to preserve history).
  - Update `SKILL.md` frontmatter `name:` and the `SKILL_DIR` path.
  - Update the workflow `meta.name` in `scripts/cosmic-cfp-count.workflow.js`.
  - Update `README.md` entry and script paths.
  - Repoint the `~/.claude/skills/` symlinks to the new directory.
- Change output writing so nothing lands inside the skill directory:
  - Default output directory is the **parent directory of the input CSV**.
  - The user may override the output directory.
  - Flatten the layout: both `cosmic-count.json` and `cosmic-count.md` write directly into the chosen output directory (drop the `data/` + `outputs/artifacts/` split).
  - Remove the leaked `dk-cosmic-cfp-count/data/` and `dk-cosmic-cfp-count/outputs/` directories.

## Capabilities

### New Capabilities
- `cfp-count-output-location`: how the skill chooses where to write its two output artifacts (CSV-parent default, user override, flattened single directory, never inside the skill).

### Modified Capabilities
- `cfp-count-output`: scenarios that hardcode the output file path `data/cosmic-count.json` must reference the resolved output directory instead, and the flattened `cosmic-count.json` / `cosmic-count.md` filenames.

## Impact

- Skill directory rename: `dk-cosmic-cfp-count/` → `dk-cosmic-csv-to-cfp/`.
- `SKILL.md` (name, SKILL_DIR, output-path instructions in Steps 1–3, output-format section).
- `scripts/cosmic-cfp-count.workflow.js` (`meta.name`; workflow filename optionally renamed).
- `scripts/render_markdown.py` (invoked with a resolved output path — already parameterized, but docstring paths reference `data/`).
- `README.md` (skill entry + script paths).
- `~/.claude/skills/` symlinks (`cosmic-cfp-count`, `dk-cosmic-cfp-count`).
- Downstream consumers invoking the skill by its old name break (accepted).
