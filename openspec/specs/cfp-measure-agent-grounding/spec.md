# cfp-measure-agent-grounding Specification

## Purpose

Define how per-epic COSMIC measure agents ground themselves so they work from
self-contained injected inputs, minimising tool-call round-trips without altering
measurement results.

## Requirements

### Requirement: Measure agent works from its self-contained injected inputs

Each per-epic measure agent SHALL treat the injected epic JSON and the injected
rules primer as its complete, self-contained working set. The agent MUST NOT
re-read the source epics CSV, MUST NOT read the workflow's output JSON, and MUST
NOT re-resolve the coach or skill directories — every field it needs (epic id,
name, description) is present in the injected epic object, and every recurring
rule is present in the injected primer.

#### Scenario: Agent has all epic fields inline

- **WHEN** a measure agent is prompted with an epic that includes `epic_id`,
  `epic_name`, and `description`
- **THEN** the agent produces its measurement without issuing any filesystem read
  of the source CSV, the output JSON, or the project tree to recover those fields

#### Scenario: Agent does not re-discover its own grounding location

- **WHEN** a measure agent needs the coach's rules
- **THEN** it cites the injected primer directly and does NOT run a filesystem
  search (`fd`, `rg`, `realpath`) to locate the coach skill or its manuals

### Requirement: Resolved manuals path is provided, not searched

The workflow SHALL receive the resolved absolute path to the coach's
`manuals-indexed/` directory from the main thread (as `args.manualsPath`) and
inject it into each measure agent's prompt. A measure agent that needs to grep
the manuals MUST use the provided path directly and MUST NOT run a filesystem
search to locate `manuals-indexed/`.

#### Scenario: Main thread supplies the manuals path

- **WHEN** the skill invokes the workflow
- **THEN** it passes the resolved absolute `manuals-indexed/` path as
  `args.manualsPath` alongside `args.primer`

#### Scenario: Agent greps the manuals at the given path

- **WHEN** a measure agent must consult the manuals for an adjudication
- **THEN** it greps under the injected `manualsPath` directly, issuing no prior
  search to discover where the manuals live

### Requirement: Manual access is an exception, not a default

The measure prompt SHALL direct agents to cite the injected primer for the
recurring movement patterns it already covers, and to consult the manuals ONLY
for an adjudication the primer does not cover. Consulting the manuals for a
pattern the primer already states is prohibited.

#### Scenario: Primer-covered pattern is cited without a manual read

- **WHEN** an epic's movements are all covered by the primer's recurring patterns
  (external round-trip, CRUD, single confirmation/error Exit, process boundaries,
  single triggering Entry)
- **THEN** the agent cites the primer and performs no manual grep

#### Scenario: Uncovered adjudication justifies a manual read

- **WHEN** an epic raises a COSMIC adjudication the primer does not cover
- **THEN** the agent may grep the manuals at the provided path and MUST record the
  exact `manuals-indexed/<slug>/<file>.md#L..` citation

### Requirement: Measurement outputs are unchanged by the grounding discipline

The agent-grounding discipline SHALL NOT alter the movement-counting rules, the
output schema, the roll-up math, or the two produced files. For a given input the
measurement result stays semantically the same; only the number of tool-call
round-trips changes.

#### Scenario: Same input yields the same measurement shape

- **WHEN** the same epics and primer are measured before and after this change
- **THEN** the produced `<stem>-cosmic-count.json` conforms to the same schema and
  the roll-up (CFP total, ranges, gaps) is computed by the same JS logic
