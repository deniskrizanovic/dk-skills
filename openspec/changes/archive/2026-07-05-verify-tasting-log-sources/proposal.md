## Why

Source URLs stored in the `Wine Tasting Log` Google Sheet frequently lead to "page not found." The skill tells the coach to "cite every source" and persists those citations, but nothing requires the coach to actually open a URL before writing it — so it records plausible-but-fabricated links (the classic LLM citation failure) or links that later rot, and the user cannot trace their own tasting history back to its evidence.

## What Changes

- The coach MUST only record a source **URL** in the tasting log if it actually fetched that URL successfully during the session. Guessed, pattern-constructed, or unverified URLs are prohibited.
- When a source informed the expectation sheet but no URL could be opened/verified, the coach records a **descriptive reference** (producer + bottle + document type) instead of a fabricated URL.
- Add a **source capture date** to each recorded source so future link rot is explainable as drift rather than fabrication.
- The same verification bar applies to sources shown inline during the session (Step 2 citations), not just the persisted row.
- Update `SKILL.md` (Step 2 and Step 5) and the sheet column schema accordingly.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `wine-tasting-coach`: The "Grounded expectation sheet from web sources" requirement gains a source-verification rule (only cite URLs actually fetched; otherwise use a descriptive reference). The "Persist each tasting to a Google Sheet library" requirement changes its source-column contract to store only verified URLs or descriptive references, plus a capture date.

## Impact

- `wine-tasting-coach/SKILL.md` — Step 2 (build expectation sheet / cite sources), Step 5 (persist to sheet), and the column schema.
- Behavior only; no new tools or dependencies. Existing rows in a user's `Wine Tasting Log` are unaffected (new column added at the end per the existing schema-evolution rule).
