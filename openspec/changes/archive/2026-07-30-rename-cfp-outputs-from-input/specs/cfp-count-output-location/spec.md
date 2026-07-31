## MODIFIED Requirements

### Requirement: Flattened single output directory

The skill SHALL write both output artifacts — the canonical JSON and the
markdown report — directly into the resolved output directory, named from the
input CSV's stem: `<stem>-cosmic-count.json` and `<stem>-cosmic-count.md`, where
`<stem>` is the input CSV's filename with its extension removed. It MUST NOT
split them across separate `data/` and `outputs/artifacts/` subdirectories, and
MUST NOT use the fixed `cosmic-count.*` base name.

#### Scenario: Both artifacts in one directory, named from CSV stem

- **WHEN** the skill runs on input CSV `council-call-centre-epics.csv` and writes
  its outputs to resolved directory `OUT`
- **THEN** the JSON is at `OUT/council-call-centre-epics-cosmic-count.json`
- **AND** the markdown is at `OUT/council-call-centre-epics-cosmic-count.md`
- **AND** no `data/` or `outputs/artifacts/` subdirectory is created

#### Scenario: Stem strips only the file extension

- **WHEN** the input CSV filename is `<stem>.csv`
- **THEN** the derived filenames are exactly `<stem>-cosmic-count.json` and
  `<stem>-cosmic-count.md`
- **AND** only the trailing `.csv` extension is removed to form `<stem>` (no
  other suffix is stripped)

#### Scenario: Distinct CSVs do not collide

- **WHEN** the skill is run on two different CSVs `a-epics.csv` and `b-epics.csv`
  targeting the same output directory
- **THEN** the outputs are `a-epics-cosmic-count.*` and `b-epics-cosmic-count.*`
- **AND** neither run overwrites the other's artifacts

### Requirement: Resolved output paths surfaced to user

The skill SHALL report both written artifact paths to the user as absolute
paths after the run, using the derived `<stem>-cosmic-count.json` /
`<stem>-cosmic-count.md` filenames.

#### Scenario: Paths reported

- **WHEN** the run completes and both artifacts are written
- **THEN** the skill shows the absolute paths of the derived
  `<stem>-cosmic-count.json` and `<stem>-cosmic-count.md`
