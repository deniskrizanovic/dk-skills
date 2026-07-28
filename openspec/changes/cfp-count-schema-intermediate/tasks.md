## 1. Child schema (cosmic_measure_output.schema.json)

- [x] 1.1 Remove `implementationType` and `isApiCall` from the `dataMovement.required` array (keep them in `properties`)
- [x] 1.2 Add optional `cfp` integer to `dataMovement`'s parent object (functional-process level) or to the root — decide placement so per-process CFP is expressible
- [x] 1.3 Bump the schema's description/version note to record the additive v-change

## 2. Parent schema (cosmic_count_report.schema.json — new)

- [x] 2.1 Author `CosmicCountReport` root: `disclaimer`, `rulesPrimer`, `rollUp`, `epics[]`, `measurementGaps[]`
- [x] 2.2 Define `rollUp` (projectCfpCountable, cfpRange[2], epicsMeasured, epicsTotal, countableEpics, epicsRestingOnAssumptions[])
- [x] 2.3 Define `epic` (epicId, epicName, confidence enum, epicCfp, caveats[], functionalProcesses[], gaps[])
- [x] 2.4 `$ref` the child schema for `functionalProcesses[]` items; confirm the validator resolves the relative ref (fall back to inlined `$defs` if not)
- [x] 2.5 Define `gap` (gapId, category, gapOrQuestion, impactOrNotes)

## 3. Workflow (scripts/cosmic-cfp-count.workflow.js)

- [x] 3.1 Update `EPIC_SCHEMA`: camelCase keys; movements → child shape (name, order, movementType, dataGroupRef, note, citation); each process carries functionalProcessId + artifact + optional cfp
- [x] 3.2 Update measure-agent prompt to emit the child-shaped functional processes
- [x] 3.3 Update the assembled `fileObject` to camelCase parent shape (rollUp, rulesPrimer, epics, measurementGaps)
- [x] 3.4 Keep gaps deterministic (CG-<epic>-NN) and roll-up computed in JS

## 4. Renderer (scripts/render_markdown.py)

- [x] 4.1 Read camelCase keys (rollUp, epicCfp, movementType, dataGroupRef, functionalProcesses, gapId, ...)
- [x] 4.2 Handle per-process CFP from `cfp` field or `len(dataMovements)` fallback

## 5. Docs & validation

- [x] 5.1 Update SKILL.md to describe the two-schema intermediate format and the breaking field renames
- [x] 5.2 Validate a sample `cosmic-count.json` against the parent schema and each FP block against the child
- [x] 5.3 `openspec validate cfp-count-schema-intermediate` passes
