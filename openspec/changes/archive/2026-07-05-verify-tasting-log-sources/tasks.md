## 1. Step 2 — verify-before-cite

- [x] 1.1 In `SKILL.md` Step 2, add a hard rule: a source may be cited as a URL ONLY if the coach fetched it successfully this session; guessed/pattern-constructed/unverified URLs are prohibited.
- [x] 1.2 Add the fallback: when a source informed the expectation sheet but no URL could be fetched/verified, cite a descriptive reference (producer + bottle + document type) instead of a URL.

## 2. Step 5 — persistence and schema

- [x] 2.1 In Step 5, state that each source column holds only a verified URL or a descriptive reference, never an unverified URL.
- [x] 2.2 Add a `Source Captured Date` column to the column schema (Step 5 §"Column schema"), placed at the end, and describe it.
- [x] 2.3 Note in the schema-evolution guidance that sheets predating the capture-date column get the column appended at the end (never reorder existing columns).

## 3. Verify

- [x] 3.1 Re-read `SKILL.md` Step 2 and Step 5 to confirm the wording matches every scenario in the delta spec (verified-URL-only, descriptive-reference fallback, capture-date column, stable schema).
- [x] 3.2 Run `openspec validate verify-tasting-log-sources` (or `openspec status`) and confirm the change is consistent.
