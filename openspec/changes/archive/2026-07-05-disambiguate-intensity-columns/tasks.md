## 1. Rename in the source-of-truth grid

- [x] 1.1 In `reference/wine-tasting-grid.md`, rename the Sight → Color `Intensity` attribute to `Color Intensity`
- [x] 1.2 In `reference/wine-tasting-grid.md`, rename the Nose → Impression `Intensity` attribute to `Aroma Intensity`

## 2. Rename in the embedded grid

- [x] 2.1 In `SKILL.md`, rename the Sight → Color `Intensity` attribute to `Color Intensity` in the embedded grid
- [x] 2.2 In `SKILL.md`, rename the Nose → Impression `Intensity` attribute to `Aroma Intensity` in the embedded grid

## 3. Update the Step 5 schema description

- [x] 3.1 In `SKILL.md` Step 5 "Column schema", update the enumerated example attribute names so they reference the renamed `Color Intensity` / `Aroma Intensity` (and state that every grid-attribute header is unique)

## 4. Verify

- [x] 4.1 Confirm no remaining bare `Intensity` grid attribute exists in either grid copy (only `Color Intensity` / `Aroma Intensity`)
- [x] 4.2 Confirm the two grid copies (reference + embedded) are in sync for these rows
- [x] 4.3 Confirm the spec scenarios (unique headers, predates-rename) match the SKILL.md wording
