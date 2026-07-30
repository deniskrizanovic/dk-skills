## Why

The skill writes fixed filenames `cosmic-count.json` / `cosmic-count.md` into
the CSV's parent directory. Running the skill on two different CSVs in the same
directory silently overwrites the first run's outputs, and the filenames give no
clue which scope they measured. Deriving the names from the input CSV makes each
run's outputs self-identifying and non-colliding.

## What Changes

- Output artifact filenames are derived from the input CSV's stem instead of the
  fixed `cosmic-count` base: `<stem>-cosmic-count.json` and
  `<stem>-cosmic-count.md`, where `<stem>` is the CSV filename without its
  extension (e.g. `council-call-centre-epics.csv` →
  `council-call-centre-epics-cosmic-count.json` / `.md`).
- The resolved output *directory* behavior is unchanged (CSV parent by default,
  user override honored, single flattened directory).
- **BREAKING**: readers/tools that hard-code the `cosmic-count.json` /
  `cosmic-count.md` filenames must switch to the derived names.

## Capabilities

### New Capabilities

<!-- none -->

### Modified Capabilities

- `cfp-count-output-location`: the "Flattened single output directory" and
  "Resolved output paths surfaced to user" requirements change — the two
  artifacts are now named from the input CSV stem (`<stem>-cosmic-count.json` /
  `<stem>-cosmic-count.md`) rather than the fixed `cosmic-count.*`.

## Impact

- `dk-cosmic-csv-to-cfp/SKILL.md` — Step 1/2/3 filename references and the
  output-format prose.
- `dk-cosmic-csv-to-cfp/scripts/render_markdown.py` — invoked with the derived
  markdown path; no logic change if the path is passed in, but its usage doc and
  any default must reflect the new naming.
- The main thread's `Write` of the JSON must target the derived path.
- Downstream consumers that read `cosmic-count.json` by fixed name.
