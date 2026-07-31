## ADDED Requirements

### Requirement: CSV-to-CFP consumes the shipped primer via args

The `dk-cosmic-csv-to-cfp` skill SHALL obtain the COSMIC rules primer by reading
the coach's shipped `rules-primer.md` on the main thread and passing its contents
to the measurement workflow as `args.primer`. The workflow SHALL inject
`args.primer` into every measure agent, unchanged from the prior injection
behavior. The workflow itself SHALL NOT read the file (workflow scripts have no
filesystem access).

#### Scenario: Primer read on main thread and injected

- **WHEN** the skill runs a measurement
- **THEN** the main thread reads the coach's `rules-primer.md`
- **AND** passes its contents as `args.primer` to the workflow
- **AND** each measure agent receives the same primer text in its prompt

### Requirement: Live Prime phase removed

The workflow SHALL NOT contain an every-run `Prime` phase that re-derives the
primer from the coach. Primer derivation SHALL happen only in the coach's
deliberate regeneration step, never per measurement run.

#### Scenario: No Prime agent runs during measurement

- **WHEN** the measurement workflow executes
- **THEN** no agent queries the coach to derive the recurring rules primer
- **AND** the workflow phases are the measurement fan-out and synthesis only

### Requirement: Hard-fail on missing primer

If `args.primer` is absent or empty, the workflow SHALL throw immediately with a
message instructing the operator to supply the coach's primer, rather than
silently deriving one or measuring without it.

#### Scenario: Missing primer aborts the run

- **WHEN** the workflow is invoked without a non-empty `args.primer`
- **THEN** it throws before any measure agent runs
- **AND** the error message directs the operator to the coach's `rules-primer.md`

### Requirement: Deterministic primer provenance in output

The `rulesPrimer` field carried in the output report SHALL be identical across
runs of the same primer version against the same epics, because the primer is a
shipped, version-stamped file rather than a per-run derivation.

#### Scenario: Repeated runs carry identical rulesPrimer

- **WHEN** the skill runs twice with the same primer file and the same epics
- **THEN** the `rulesPrimer` value in both output reports is identical
