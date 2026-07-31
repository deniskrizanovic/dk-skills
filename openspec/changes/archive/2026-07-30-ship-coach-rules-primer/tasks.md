## 1. Coach: author and ship the primer

- [x] 1.1 Run the existing Prime-agent prompt once (workflow.js ~L101-120) against the current `manuals-indexed/` to derive the primer text
- [x] 1.2 Review the derived primer for correctness — verify each `manuals-indexed/<slug>/<file>.md#L..` citation resolves to the cited rule
- [x] 1.3 Author the primer domain-neutral (pure COSMIC rules, no Salesforce flavor)
- [x] 1.4 Add frontmatter version stamp (coach manual version and/or index date it was derived from)
- [x] 1.5 Commit `rules-primer.md` to the coach skill directory

## 2. Coach: regeneration procedure and ADR

- [x] 2.1 Document the regeneration procedure in coach SKILL.md, next to the `index_manuals` bootstrap step, including updating the version stamp
- [x] 2.2 Decide regen mechanism (documented manual agent invocation vs a `scripts/` helper) and record it
- [x] 2.3 Write `docs/adr/0002-distilled-primer-over-live-rederivation.md` — frame consistent with 0001, contrast primer (pre-computed answer set) vs vector DB (retrieval index)
- [x] 2.4 Add a pointer to the primer + ADR 0002 in the coach's "Out of scope"/docs references as appropriate

## 3. CSV-to-CFP: consume the shipped primer

- [x] 3.1 Update SKILL.md Step 2: main thread resolves the coach dir, reads `rules-primer.md`, passes contents as `args.primer` alongside `{epics}`
- [x] 3.2 In `scripts/cosmic-csv-to-cfp.workflow.js`, add a hard-fail guard: `if (!args.primer) throw` with a message pointing at the coach primer
- [x] 3.3 Delete the `Prime` phase (agent + `phase('Prime')`) and the `Prime` entry in `meta.phases`
- [x] 3.4 Replace `${primer}` in `measurePrompt` with `args.primer`, and set `rulesPrimer: args.primer` in the assembled report object
- [x] 3.5 Update the SKILL.md Execution narrative (the numbered "Prime/Measure/Synthesize" description) to drop Prime and describe the primer-read step

## 4. Verify

- [x] 4.1 Run the workflow with a valid `args.primer` + sample epics; confirm measure agents receive the primer and output validates against the schemas
- [x] 4.2 Run without `args.primer`; confirm it hard-fails before any measure agent
- [x] 4.3 Run twice with the same primer + epics; confirm `rulesPrimer` is byte-identical across both outputs
- [x] 4.4 Update/adjust any coach or csv-skill tests that referenced the Prime phase
