# Capability: cfp-count-output-location

## Purpose

Define where the COSMIC Function Point counting skill writes its output artifacts (JSON and markdown reports), ensuring outputs are written to a predictable, user-controllable location rather than scattered across subdirectories or the skill's installation directory.

## Requirements

### Requirement: Output directory defaults to CSV parent

The skill SHALL write its output artifacts to a resolved output directory that
defaults to the parent directory of the input epics CSV. The skill MUST NOT
write artifacts inside its own installed skill directory.

#### Scenario: Default resolves to CSV parent

- **WHEN** the user runs the skill on `/some/path/epics.csv` and gives no output directory
- **THEN** the artifacts are written under `/some/path/`
- **AND** no artifact is written inside the skill directory

### Requirement: User can override the output directory

The skill SHALL let the user specify an output directory that overrides the
default. When the user provides one, the artifacts MUST be written there.

#### Scenario: Explicit output directory honored

- **WHEN** the user supplies an output directory `/out/dir`
- **THEN** both output artifacts are written under `/out/dir`
- **AND** the CSV-parent default is not used

### Requirement: Flattened single output directory

The skill SHALL write both output artifacts — the canonical JSON and the
markdown report — directly into the resolved output directory as
`cosmic-count.json` and `cosmic-count.md`. It MUST NOT split them across
separate `data/` and `outputs/artifacts/` subdirectories.

#### Scenario: Both artifacts in one directory

- **WHEN** the skill writes its outputs to resolved directory `OUT`
- **THEN** the JSON is at `OUT/cosmic-count.json`
- **AND** the markdown is at `OUT/cosmic-count.md`
- **AND** no `data/` or `outputs/artifacts/` subdirectory is created

### Requirement: Resolved output paths surfaced to user

The skill SHALL report both written artifact paths to the user as absolute
paths after the run.

#### Scenario: Paths reported

- **WHEN** the run completes and both artifacts are written
- **THEN** the skill shows the absolute paths of `cosmic-count.json` and `cosmic-count.md`
