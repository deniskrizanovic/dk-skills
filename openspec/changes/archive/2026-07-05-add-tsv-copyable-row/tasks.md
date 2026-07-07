## 1. Reframe Step 5 persistence in SKILL.md

- [x] 1.1 Reword the Step 5 intro so persistence attempts a connector append only if the connector supports it, and note that the current connector reads but cannot append
- [x] 1.2 State that the connector's working role today is reading prior rows for the Perception Alignment trend (cross-reference Step 4), keeping read and write clearly separated

## 2. Define the tab-delimited copyable-row output

- [x] 2.1 Add a subsection describing the TSV data row: exact column order matching the Step 5 schema, one line per session, and instruction to paste into "Wine Tasting Log"
- [x] 2.2 Document the sanitization rule: replace tab and newline characters inside any cell with a space before emitting
- [x] 2.3 Document the field-count invariant: the data row has the same field count as the header, including blank cells (empty Perception Alignment, unanswered attributes)
- [x] 2.4 Document the on-request header row and the first-use case (no sheet yet → provide header + instruct user to create the sheet with the exact name)

## 3. Reconcile fallbacks and trend

- [x] 3.1 Ensure the existing Drive-unavailable fallback (connector entirely absent) remains a distinct branch and does not conflict with the new TSV path
- [x] 3.2 Confirm the Perception Alignment trend text (Step 4) still reads prior rows and reflects that the current row is pasted after the session

## 4. Sync grid/schema source of truth

- [x] 4.1 Verify the column order used for the TSV header/data matches the embedded grid attributes and Step 5 schema exactly (identity → per-attribute → sources → capture date → calibration → Perception Alignment)

## 5. Verify against spec scenarios

- [x] 5.1 Walk each scenario in the updated wine-tasting-coach spec delta and confirm SKILL.md wording satisfies it (connector-cannot-append, single-line alignment, header offered, trend read, schema stability)
