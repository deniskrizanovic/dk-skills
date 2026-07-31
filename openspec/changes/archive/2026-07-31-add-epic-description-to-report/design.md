## Context

The epics CSV `Description` column is parsed by `epics_csv_to_args.py` into `epic.description` and reaches every measure agent inside `measurePrompt` (as part of the JSON-serialized epic). But the measure agent's output schema (`EPIC_SCHEMA`) has no `description` field, and the report schema's epic definition sets `additionalProperties: false`, so the requirement text is never persisted. The markdown renderer therefore has nothing to show.

Constraint: the workflow's core value is that the roll-up is JS-computed and the agent only serializes measurement. Adding a field the agent must echo verbatim is a small deviation but acceptable — it is not a computed value, and echoing free text is low risk.

## Goals / Non-Goals

**Goals:**
- Persist the source description in the count JSON per epic.
- Show it in the markdown report next to the epic's measurement.
- Keep the change non-breaking: old JSON without the field still validates and renders.

**Non-Goals:**
- Changing how CFP is measured or rolled up.
- Reformatting the CSV parsing (`epic.description` already exists).
- Adding the description to the per-epic *summary* table (would bloat the table; detail section is the right home).

## Decisions

**Carry the description via the agent echo, not by JS join.** The synthesize step returns `measured` (the agents' outputs) as `epics`. The cleanest path is: add `description` to `EPIC_SCHEMA`, instruct the agent to echo `epic.description` verbatim (same pattern already used for `epicName`), and it flows through untouched.
- *Alternative considered:* have the synthesize JS merge `epics[i].description` from `args.epics` back onto each measured result by index. Rejected — pipeline nulls shift nothing (order preserved) but coupling the merge to index is more fragile than an echo, and the agent already receives the text.

**Placement in markdown:** render the description as a blockquote immediately under the epic heading / CFP line, before functional processes. Omit the block entirely when absent/empty.

**Schema:** add `description` as an optional string on the epic definition. It must be added to `EPIC_SCHEMA` in the workflow too, and — because `additionalProperties: false` — to `cosmic_count_report.schema.json`'s epic definition, or validation rejects it.

## Risks / Trade-offs

- [Agent drops or paraphrases the description] → Prompt instructs verbatim echo, mirroring the existing `epicName`/`epicId` echo instruction; low risk for free text.
- [Long descriptions bloat the report] → Detail-section blockquote only, not the summary table; acceptable.

## Migration Plan

Additive and optional — no migration. Regenerate the example artifacts to demonstrate the field. Old count JSON continues to validate and render (renderer treats missing description as "omit").

## Open Questions

None.
