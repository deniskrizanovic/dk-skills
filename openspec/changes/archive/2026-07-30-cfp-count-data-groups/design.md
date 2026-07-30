# Design — Functional-process data groups

## Context

`cosmic-count.json` today records data groups only inline, as the free-text
`dataGroupRef` on each `dataMovements[]` item. The same object of interest is
repeated wherever it moves (e.g. an object entered then written appears as two
movements with the same `dataGroupRef`). There is no consolidated list of the
distinct data groups per functional process, which blocks two uses:
audit (is the same object counted consistently?) and data-model handoff
(what are the candidate entities?).

## Decisions

### 1. Level: functional process, not epic or report

`dataGroups[]` lives on the child `CosmicMeasureOutput`, sibling to
`dataMovements[]`. A functional process is the natural owner — its movements
define which objects it touches. Epic- and report-level views are derivable by
iterating processes and need no stored field.

### 2. Shape: `{ name, description }`, both required

Minimal but useful for the two goals. No movement types, no persistence flag —
those were explicitly out of scope. `name` is the data-group identifier;
`description` is a short authored gloss of what the object carries.

```json
"dataGroups": [
  {
    "name": "Lost Pet Report",
    "description": "Caller details, pet species/breed/description, last-seen location & date, contact number."
  },
  {
    "name": "Microchip Registry Record",
    "description": "Registry record matched on the reported animal's microchip."
  }
]
```

### 3. Authored by the agent, not derived by JS

`name` alone could be derived by deduplicating `dataGroupRef`. But `description`
is new information not present in the movement data, so pure JS derivation is
impossible. Therefore the measure agent authors the whole `dataGroups[]` array.
It already reasons over each object of interest while enumerating movements, so
the marginal output cost is small. The agent keeps `dataGroupRef` values aligned
with `dataGroups[].name` by construction (same names in both), avoiding a
reconciliation step. The synthesize step passes the array through verbatim — no
LLM re-serialization (consistent with the existing rule that the roll-up and
report are assembled in JS, not echoed by an agent).

### 4. Additive / optional

`dataGroups[]` is optional in the schema. Existing outputs and the code-analysis
COSMIC measurer (which shares the child schema) remain valid without it.

### 5. Render: top-level catalog after the per-epic summary

Although the data lives per-FP, the report presents one consolidated catalog
after the per-epic summary table (before the per-epic detail). This gives a
single at-a-glance list for audit and handoff. The renderer iterates all epics'
functional processes and flattens their `dataGroups[]` into one table keyed by
epic + FP.

```
## Per-epic summary
...table...

## Data groups
| Epic | FP | Data group | Description |
|---|---|---|---|
| E01 | FP1-LogLostPetReport | Lost Pet Report | Caller details, ... |
| E01 | FP1-LogLostPetReport | Microchip Registry Record | ... |
...

---
## E01 — ...
```

If no process carries `dataGroups[]`, the section is omitted.

## Alternatives considered

- **Derive names from `dataGroupRef` parentheticals** (name before `(`,
  description inside). Rejected: only ~half the refs have parentheticals, and it
  cannot produce a real description for the rest. Authored descriptions are the
  requested outcome.
- **Top-level or per-epic `dataGroups[]` storage.** Rejected: the FP owns the
  movements; higher-level views are derivable at render time without duplicating
  state.
- **Strict ref model** (movement `dataGroupRef` becomes an id into a
  data-groups table). Rejected as heavier than needed and breaking; names stay
  as the join key.

## Risks

- **Name drift.** If the agent words a `dataGroups[].name` differently from a
  `dataGroupRef`, the two won't join. Mitigated by instructing the agent to use
  identical names; acceptable for a minimal pass since both are agent-authored
  in the same step.
