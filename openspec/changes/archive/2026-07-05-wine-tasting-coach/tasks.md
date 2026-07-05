## 1. Skill scaffold

- [x] 1.1 Create `wine-tasting-coach/` directory
- [x] 1.2 Create `wine-tasting-coach/SKILL.md` with frontmatter (name, description, metadata category "Wine / Tasting", version) following the repo's skill pattern
- [x] 1.3 State the runtime environment in `SKILL.md`: Claude web, using web search/browse and the Google Drive connector; no local filesystem
- [x] 1.4 Embed the full tasting-grid content (from `wine-tasting-grid.md`) into `SKILL.md`, and note that the repo file is the human-maintained source to re-sync from

## 2. Intake and expectation sheet

- [x] 2.1 Write the intake step: require wine name + vintage up front; prompt for vintage (or explicit non-vintage) if omitted
- [x] 2.2 Document the web-fetch procedure and trust gradient (tech sheet > grape/region/vintage archetype > avoid crowd notes) with mandatory source citation
- [x] 2.3 Document the mandatory cross-check: always reconcile the specific bottle against a style archetype (even when a tech sheet exists) and flag divergence when the bottle is atypical
- [x] 2.4 Document graceful degradation: announce when coaching from style archetype rather than the specific bottle, and the low-confidence path when only crowd notes exist
- [x] 2.5 Document the vintage-climate and bottle-age adjustment step (garnet shift/anthocyanin loss for aged reds; ripeness/alcohol for hot vintages)

## 3. Grid-driven walkthrough

- [x] 3.1 Instruct the coach to walk the embedded grid in published order (Sight → Nose → Palate), one section at a time
- [x] 3.2 Define the "prime the category, you confirm" leading-question template with a worked example per grid section
- [x] 3.3 Add the hard rule: never assert a marker is present; record unexpected user notes faithfully without rewriting to fit expectation

## 4. Capture and calibration

- [x] 4.1 Define the in-conversation filled-grid output (grid sections/attributes with the user's observations captured under each)
- [x] 4.2 Define the closing calibration comparison (matched / missed / focus-next), explicitly with no numeric score or pass/fail

## 5. Google Sheet library persistence

- [x] 5.1 Define the tasting-library sheet column schema: identity (wine, vintage, date, region/producer) + one column per grid attribute + cited-sources columns + calibration-summary column
- [x] 5.2 Document locating the sheet named exactly "Wine Tasting Log" in Drive and creating it under that exact name with a header row on first use
- [x] 5.3 Document appending one row per completed tasting, mapping observations to existing headers so rows stay aligned; add new columns at the end rather than reordering
- [x] 5.4 Document the Drive-unavailable fallback: complete the tasting, tell the user it couldn't save, and return the filled results inline

## 6. Documentation

- [x] 6.1 Add a `wine-tasting-coach` entry to `README.md` (description, Claude-web + Google Drive requirement, no-scripts note)
- [x] 6.2 Add `wine-tasting-coach/` to the structure tree in `README.md`

## 7. Verification

- [x] 7.1 Dry-run the skill on Claude web against a real bottle + vintage; confirm sources are fetched and cited, and the trust gradient/fallback behaves
- [x] 7.2 Confirm the walkthrough follows the embedded grid order, questions prime-but-don't-assert, and the close produces a filled grid + calibration feedback
- [x] 7.3 Confirm the session is appended as a row to the Google Sheet library (sheet created on first run, headers aligned, Drive-unavailable fallback works)
