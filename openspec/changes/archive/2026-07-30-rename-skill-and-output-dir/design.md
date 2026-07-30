## Context

`dk-cosmic-cfp-count` is a workflow-driven skill: `SKILL.md` orchestrates a CSV
parse, a multi-agent measurement workflow, and a markdown render. Two problems:

1. Output paths in `SKILL.md` are relative (`data/cosmic-count.json`,
   `outputs/artifacts/cosmic-count.md`). Because `SKILL_DIR` resolves to the
   installed skill and cwd drifts there, artifacts land inside the skill and get
   committed as untracked junk (`dk-cosmic-cfp-count/data/`, `/outputs/`).
2. The name is opaque. `dk-cosmic-csv-to-cfp` states the transform.

The skill is installed via two symlinks in `~/.claude/skills/`
(`cosmic-cfp-count` and `dk-cosmic-cfp-count`) pointing at the repo directory.
`render_markdown.py` already takes an output path argument, so only the SKILL.md
invocation and docstring reference `data/`.

## Goals / Non-Goals

**Goals:**
- Rename skill + repoint symlinks; old invocation name intentionally breaks.
- Outputs default to the CSV's parent dir, overridable, flattened to one dir.
- Nothing writes inside the skill directory.

**Non-Goals:**
- No change to measurement logic, schemas' field contracts, or the workflow's
  agent structure.
- No backward-compat alias for the old skill name (break is confirmed).

## Decisions

**Rename via `git mv`.** Preserves history for the directory and its files.
Update in the same change: `SKILL.md` `name:` + `SKILL_DIR` line,
`scripts/cosmic-cfp-count.workflow.js` `meta.name`, `README.md`. Rename the
workflow file `cosmic-cfp-count.workflow.js` → `cosmic-csv-to-cfp.workflow.js`
and update the SKILL.md `scriptPath` reference — keeps the filename consistent
with the new name. Alternative (keep old filename): rejected, leaves a stale
name that confuses future readers.

**Output dir resolved in SKILL.md instructions, not in scripts.** The workflow
returns `result.cosmicCount` in memory; the main agent writes it with the Write
tool. So the output-location logic is an instruction: "default `OUT_DIR` to the
CSV's parent directory; if the user named a directory, use that." The main agent
already computes the CSV path in Step 1, so `dirname` is trivial. `render_markdown.py`
is then invoked with `$OUT_DIR/cosmic-count.md`. Alternative (bake path logic
into a script): rejected — the write is agent-driven by design (SKILL.md line
86–89), and a script can't prompt the user for an override.

**Flatten to `OUT_DIR/cosmic-count.{json,md}`.** Drop `data/` and
`outputs/artifacts/`. Simpler for the user to find both files; the split bought
nothing once artifacts leave the skill dir.

**Delete leaked dirs.** `git rm`/`rm` the untracked `data/` and `outputs/` under
the skill after the move.

## Risks / Trade-offs

- **Symlink repoint missed** → skill fails to load under new name. Mitigation:
  recreate both symlinks pointing at the renamed dir; verify `SKILL_DIR` resolves.
- **CSV parent dir not writable** (read-only mount, odd path) → write fails.
  Mitigation: the user-override path exists precisely for this; surface the
  error and prompt for an alternate dir.
- **Old name referenced elsewhere** (other skills, docs) → dangling reference.
  Mitigation: repo-wide grep for `cosmic-cfp-count` as part of tasks.
- **In-flight `cfp-count-data-groups` change** touches the same skill files.
  Mitigation: this change is mechanical rename + path; low collision risk, but
  archive/land ordering should be noted.

## Migration Plan

1. `git mv` skill dir + workflow file.
2. Edit name references (SKILL.md, workflow meta, README).
3. Rewrite SKILL.md output steps for OUT_DIR default + override + flat layout.
4. Delete leaked `data/`, `outputs/`.
5. Repoint `~/.claude/skills/` symlinks.
6. Repo-wide grep to confirm no stale `cosmic-cfp-count` refs.

Rollback: `git mv` back and restore symlinks.
