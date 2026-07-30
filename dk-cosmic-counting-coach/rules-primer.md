---
name: cosmic-rules-primer
description: >
  Distilled, scope-independent COSMIC v5.0 rules primer covering the movement
  patterns that recur across a delivery scope. Derived from the coach's indexed
  manuals; every rule cites manuals-indexed/<slug>/<file>.md#L<start>-L<end>.
derivedFrom:
  manuals:
    - part-1-mm-principles-definitions-rules-v5-0-aug-2021
    - part-2-mm-guidelines-v5-0-sep-2024
    - part-3c-mis-examples-v5-0-sep-2024
  cosmicVersion: v5.0
  indexDate: 2026-06-17
  regeneratedOn: 2026-07-30
---

# COSMIC v5.0 Rules Primer

Compact reusable reference for the recurring movement patterns. Cite these
directly; grep the manuals only for adjudications NOT covered here. 1 data
movement = 1 CFP.

## 1. External-system round-trip (request → response)

When a functional process needs to tell another party what data to send, an
**Exit** (the request) followed by an **Entry** (the response) are necessary —
so a round-trip to another piece of software is **2 movements** (1 Exit + 1
Entry). When no request is needed to prompt the data, a single Entry suffices.
Both movements belong to the same functional process (all responses to the
triggering Entry stay in one process).
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259`

## 2. CRUD on a persistent object of interest

From a user-triggered functional process (RULE 18 = Read from persistent
storage, RULE 19 = Write to persistent storage, RULE 20 = a delete is a single
Write):

- **Create**: Entry (new data) + Write.
- **Read/retrieve**: Entry (trigger) + Read + Exit (data back to the user).
- **Update**: Entry (changes) + Read (existing) + Write (modified).
- **Delete**: Entry (trigger) + Write (the deletion).

`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149`
`manuals-indexed/part-3c-mis-examples-v5-0-sep-2024/02-help-functionality.md#L33-L36`

## 3. Confirmation and error messages

**One Exit** accounts for ALL types of error/confirmation messages issued by any
one functional process, from all possible causes — regardless of message count
or variety. If a message carries data beyond confirming acceptance/error, that
additional data group is a separate Exit counted in the normal way.
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272`

## 4. Distinct functional processes vs. one

Two functional processes are distinct when they respond to **different
triggering events** (each detected by a functional user). A functional process
is the set of all data movements needed to meet its FUR for all possible
responses to its triggering Entry — so work that all flows from one triggering
event is one process, not several.
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L63-L71`
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L26`

## 5. The single triggering Entry rule

Any one functional process has **exactly one triggering Entry** — the Entry from
a functional user that starts the process on detecting a triggering event (RULE
10). RULE 13: a single Entry is counted for entry of all data describing a
single object of interest, unless the FUR explicitly require the same object to
be entered more than once. All subsequent movements (further Entries, Exits,
Reads, Writes) responding to that triggering Entry belong to the same process.
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26`
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99`
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L243-L243`
