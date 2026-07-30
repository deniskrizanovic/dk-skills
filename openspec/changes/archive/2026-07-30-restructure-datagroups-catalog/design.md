## Context

`render_markdown.py` builds the `## Data groups` catalog by flattening every
`epics[].functionalProcesses[].dataGroups[]` entry into one row keyed by
`(epicId, fpLabel, name, description)` (script lines ~91-107). A data group
touched by multiple processes therefore appears once per process. In the current
example dataset only two names collide — `Booking` (3 refs) and
`SMS Confirmation` (2 refs) — and both have conflicting descriptions.

The change is render-only: the JSON output and both schemas are untouched. The
`dataGroups[]` field on each functional process already carries the
`{name, description}` pairs the catalog needs; only the aggregation and column
layout change.

## Goals / Non-Goals

**Goals:**
- One row per distinct data group name, deduplicated across the whole report.
- Data group name is the first column; using processes collected into one cell
  as comma-joined `Epic/FP` references; description last.
- Rows sorted alphabetically by data group name.
- Distinct descriptions joined with ` / ` on conflict; graceful omission when no data groups.

**Non-Goals:**
- No change to `cosmic-count.json`, the JSON schemas, or the workflow.
- No semantic reconciliation of conflicting descriptions — distinct variants are
  concatenated verbatim with ` / `, not rewritten or merged in meaning.
- No change to the per-FP `dataMovements` tables (which legitimately repeat data
  group names per movement).

## Decisions

**Aggregate into an insertion-ordered map keyed by name.** Iterate epics and
functional processes in document order; for each `dataGroups[]` entry, if the
name is unseen, record `{descriptions: [], refs: []}`; always append the
`Epic/FP` ref and append the description if not already present (distinct only).
Python `dict` preserves insertion order, so descriptions and refs stay in
document order. Join descriptions with ` / ` at render time.
- _Alternative:_ `group_by(name)` then pick a description — same result, more
  code; the single-pass map is simplest.

**Ref format `Epic/FP`.** Use `epicId + "/" + fpLabel`, where `fpLabel` is the
existing `functionalProcessId or artifact.name` (same label used elsewhere in
the renderer). Comma-join with `, `.

**Sort alphabetically at render time.** Sort the map's items by name (default
string order) when emitting rows; aggregation order is only used to fix
description and ref order within a cell.

**Column header.** `| Data group | Functional processes | Description |`.

## Risks / Trade-offs

- [Joining conflicting descriptions can produce a long cell — e.g. `Booking` in
  E06 (create) vs E12 (read) shows both glosses joined with ` / `] → Accepted;
  no detail is lost, and the per-FP movement tables still carry full per-process
  context.
- [Alphabetical sort changes row order vs the old epic-ordered table] → Intended;
  a name-keyed catalog is easier to scan alphabetically.
- [A test may assert the old header/row shape] → Update the test alongside the
  renderer and regenerate the example `cosmic-count.md`.

## Migration Plan

1. Edit the catalog block in `render_markdown.py`.
2. Update the SKILL.md prose describing the catalog.
3. Regenerate `examples/cosmic-count.md` from `examples/cosmic-count.json`.
4. Update/add tests; run the test suite.

Rollback: revert the renderer and SKILL.md edits; regenerate the example. No
data migration since the JSON is unchanged.
