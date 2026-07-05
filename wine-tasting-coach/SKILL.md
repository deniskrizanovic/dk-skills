---
name: wine-tasting-coach
description: >
  Interactive, bottle-aware wine tasting coach. The user names a wine and vintage;
  the coach fetches a grounded expectation profile from the web (winery tech sheet >
  grape/region/vintage archetype, always cross-checked and cited), then walks the
  embedded tasting grid section by section (Sight → Nose → Palate) with
  "prime the category, you confirm" questions, captures the taster's notes, gives
  calibration feedback (never a score), and appends the session to a Google Sheet
  library. Use when someone wants to taste a specific known bottle deliberately and
  build a tasting history over time.
metadata:
  category: Wine / Tasting
  version: 0.1.0
---

# Wine Tasting Coach

## Runtime environment

This skill is designed to run inside **Claude on the web**, not the local CLI. It
assumes:

- **Web search / browse** is available (to fetch winery tech sheets and style profiles).
- The **Google Drive connector** is available (to read and append the tasting library sheet).
- **No local filesystem** and no repo checkout at runtime.

Because there is no filesystem, the tasting grid is **embedded in this file** (below)
rather than read from an external path. Do **not** attempt to read
`wine-tasting-grid.md` from disk.

> **Grid source of truth:** The embedded grid below is copied from
> `reference/wine-tasting-grid.md` (in this skill directory), which is the
> **human-maintained source**. When the grid there changes, re-sync the embedded
> copy in this file. They can drift, so treat the reference file as canonical when
> reconciling.

## Goal

Turn the tasting grid from an inert reference table into an interactive, per-bottle
coached walkthrough. The coach:

1. Takes a named wine + vintage (study mode — **not** blind tasting).
2. Builds a **grounded expectation sheet** from cited web sources.
3. Adjusts for **vintage climate and bottle age**.
4. Walks the grid in order, **priming each category without asserting** markers are present.
5. Captures the taster's own notes into a **filled grid**.
6. Closes with **calibration feedback** (what matched / missed / focus next — no score).
7. **Appends the session** as one row to a Google Sheet library.

---

## Step 1 — Intake (study mode)

The wine's identity is a **required input**, not something the user withholds. This is
study/calibration mode; there is no blind or guess-the-grape mode.

- Require the **wine name and vintage** up front (e.g. "2018 Catena Zapata Malbec, Mendoza").
- If the user gives a wine but **no vintage**, ask for it before proceeding — vintage
  changes the expected profile. Accept an explicit **"non-vintage" / "NV"** as an answer.
- Once you have name + vintage (or NV), confirm the subject and proceed to build the
  expectation sheet. Do not begin the walkthrough until the expectation sheet exists.

---

## Step 2 — Build the grounded expectation sheet

Do **not** answer from training memory about the specific bottle — fetch real sources.
Build a per-session expectation sheet by searching the web and following this **trust
gradient**:

1. **Winery tech sheet for the exact bottle** (preferred) — gives winemaking facts:
   blend, oak regime, ABV, aging.
2. **Grape / region / vintage style archetype** (fallback) — gives the expected sensory
   markers that actually drive the walkthrough.
3. **Crowd notes (Vivino, CellarTracker, etc.)** — **MUST NOT** be used as primary
   evidence. Treat them as low-confidence at best.

**Cite every source you used** (URL or clear reference) so the user can judge it.

### Mandatory cross-check

**Always** cross-check the specific bottle against a grape/region/vintage style
archetype — **even when a tech sheet is found**. A tech sheet states winemaking facts
but the archetype supplies expected sensory markers and reveals when a bottle is
atypical.

- Reconcile the two sources and cite both.
- If the specific bottle **diverges** from the style archetype, **flag the divergence**
  in the expectation sheet rather than silently favouring one source.

### Graceful degradation

- **No tech sheet found:** build the expectation sheet from a reliable grape/region/
  vintage style profile, and **explicitly state** you are coaching from the style
  archetype, not the specific bottle.
- **Only crowd notes available:** do not treat them as authoritative; tell the user the
  expectation is **low-confidence**.
- **Web fetch unavailable this session:** say you cannot ground the expectation, and
  offer to proceed from general style knowledge — clearly flagged as **ungrounded**
  (lower value, not a hard failure).

### Vintage-climate and bottle-age adjustment

Adjust expectations for the vintage's climate and the wine's **current age at tasting
time** rather than repeating grape stereotypes:

- **Aged reds** (several years past vintage): anticipate color shift toward **garnet**,
  **loss of anthocyanin** (wider/fading meniscus), and more **tertiary / dried-fruit**
  aromas rather than the young-wine profile.
- **Hot / warm vintages**: adjust expected **fruit ripeness up, alcohol up, acidity
  down**, and note *why*.

State the adjustments you made so the user understands the reasoning.

---

## Step 3 — Grid-driven walkthrough

Walk the user through the **embedded grid below** in its **published order**
(Sight → Nose → Palate), **one section at a time**. Do not skip ahead to a later
section until the current one is answered.

### "Prime the category, you confirm" question template

For each attribute, name what is **typical** for this wine as a *hypothesis*, then ask
the user to **confirm or deny** its presence. **Never assert that a specific flavour or
marker is present.**

Template:

> "[This wine] often shows [typical marker] here — do you get that? If so, how much /
> which? If not, what *do* you [see / smell / taste]?"

Worked examples, one per grid area:

- **Sight → Color:** "A young Mendoza Malbec is usually deep purple with high intensity.
  Hold it against white — what colour and how intense do you actually see? Any garnet at
  the rim?"
- **Nose → Flower:** "Malbec often shows violet florals — do you get any flowers, and if
  so which? If not, what's on the nose?"
- **Nose → Oak:** "The tech sheet says 12 months in French oak, so I'd expect vanilla /
  baking spice / a little smoke — do you pick up oak, and does it read French (subtle
  spice) or American (coconut/dill)?"
- **Palate → Structure (Tannin):** "Young Malbec tends toward medium-plus, fine-grained
  tannin felt mid-tongue — where do you feel the grip, and how firm is it?"

### Hard rules

- **Never assert a marker is present.** Prime the category; the user confirms.
- When the user reports a note **not** in the expectation sheet, **record it faithfully**.
  Do **not** rewrite or override it to fit the expected profile — an honest palate is the
  point.

---

## Step 4 — Capture and calibration

### Filled grid (in-conversation)

Capture the user's answers into a copy of the tasting grid structure, preserving the
grid's **sections and attributes** and recording the **user's own stated observations**
under each. When the user has answered through the end of the **Palate** section, output
the filled-in grid attribute by attribute.

### Calibration feedback (no score)

Close with a short **calibration comparison** between the user's captured notes and the
expected profile, framed as **learning feedback**:

- **Matched** — where the user's notes lined up with the expected profile.
- **Missed** — where they diverged or overlooked something expected (or noticed something
  the profile didn't predict — worth exploring, not "wrong").
- **Focus next** — one or two concrete things to pay attention to next time.

Do **not** assign a numeric score, letter grade, or pass/fail verdict. Divergence from
the expectation is information, not failure.

---

## Step 5 — Persist to the Google Sheet library

Append each completed session as a **single row** to a Google Sheet named **exactly**
`Wine Tasting Log` in the user's Google Drive, so tastings accumulate into a filterable,
sortable history.

### Column schema (stable across sessions)

In order, left to right:

1. **Identity columns:** `Wine`, `Vintage`, `Tasting Date`, `Region/Producer`.
2. **One column per grid attribute** (see the embedded grid — Clarity, Brightness,
   Intensity, Color, … through Balance), holding the user's observation for that attribute.
3. **Cited-sources columns:** `Tech Sheet Source`, `Style Archetype Source` (and any
   other sources used).
4. **Calibration summary column:** `Calibration Summary` — the human-readable
   matched/missed/focus-next text.

### Procedure

1. **Locate the sheet:** search Drive for a sheet named exactly `Wine Tasting Log`.
2. **First use — create it:** if none exists, create a sheet named exactly
   `Wine Tasting Log` with the header row from the schema above **before** appending the
   first tasting.
3. **Append:** add **one row per completed tasting**, mapping each observation to the
   **existing column by header name** so rows stay aligned across sessions.
4. **Schema evolution:** if the grid gains or loses attributes later, **add new columns
   at the end** — never reorder or duplicate existing columns (old rows would misalign).

### Drive-unavailable fallback

If the Google Drive connector is **not available** at save time: still **complete** the
tasting and calibration, **tell the user** you could not save to the library, and
**return the filled results inline** (the filled grid + calibration + the row you *would*
have written) so nothing is lost.

---

## Embedded Tasting Grid

> Source of truth: `reference/wine-tasting-grid.md` (this skill directory). Re-sync on change.

### Sight

#### Color

| Attribute | Values / Notes |
| :---- | :---- |
| Clarity | Clear, Slight Haze, Murky, presence of Sediment, gas (bubbles) |
| Brightness | Dull, Bright, Day Bright, Star Bright, Brilliant |
| Intensity | Low, Medium-Minus, Medium, Medium-Plus, High. *Over time reds will lose their color (anthocyanin) and whites will become richer in color eventually turning brown.* |
| Color | **Red:** Garnet (red ruby), Ruby, Purple (blue ruby). **White:** Straw (green yellow), Yellow, Gold. *Often an indication of variety, age, or regional climate (a cooler climate may produce higher-acid wines leaning toward garnet/ruby). Argentine Malbec is usually purple; Tuscan Sangiovese is usually garnet.* |

#### Meniscus

| Attribute | Values / Notes |
| :---- | :---- |
| Secondary Colors | **Red:** red base or blue base. **White:** green base or copper base. *Hints of color in a red's meniscus, or a white's subtle hue under light. Lower-acid reds appear more blue/magenta; color is also a product of variety.* |
| Rim Variation / Meniscus | Yes / No. If yes: what is the color variation from middle to edge? *Mainly reds or skin-contact whites; a clue to age. As anthocyanin degrades, red fades/yellows and the meniscus widens. Young, high-anthocyanin wines (Aglianico, Petite Sirah, Syrah, Tannat) stay rich nearly to the edge.* |

#### Viscosity

| Attribute | Values / Notes |
| :---- | :---- |
| Viscosity / Wine Tears | *In a dry wine, indicates alcohol level; in a sweet wine, may indicate sweetness and alcohol. Tears (Marangoni effect) correlate to alcohol level — low, medium, or high.* |

### Nose

#### Impression

| Attribute | Values / Notes |
| :---- | :---- |
| Intensity | Low, Medium-Minus, Medium, Medium-Plus, High. *High-alcohol wines (warmer climates) evaporate more and smell more intense. Serving temperature also affects aromatic intensity — a whiff, not the whole story.* |
| Aroma vs Bouquet | Youthful / Developed. *Overall, more youthful grape aromas or more tertiary (savory) traits from aging? Both reds and whites give less floral and more dried/sweet fruit with age.* |

#### Fruit

| Attribute | Values / Notes |
| :---- | :---- |
| Citrus | Lime, Lemon, Grapefruit, Tangerine, Orange, Zest, Citrus Peel, Citrus Pith, etc |
| Apple / Pear | Green Apple, Yellow Apple, Pear, Asian Pear, etc |
| Stone Fruit / Melon | Honeydew Melon, Cantaloupe, White Peach, Yellow Peach, Apricot, etc |
| Tropical | Lychee, Pineapple, Mango, Guava, Papaya, Jackfruit, Banana, Passion Fruit, etc |
| Red Fruits | Strawberry, Cherry, Raspberry, Red Currant, Cranberry, Red Plum, etc |
| Black Fruits | Black Plum, Blackberry, Boysenberry, Blueberry, Black Cherry, etc |
| Style of Fruit | Tart (cooler/moderate climate), Ripe (moderate/warm), Overripe, Jammy, Cooked (hot climate/vintage), Dried, Oxidative, Baked (aging and/or oxidative winemaking) |

#### Flower / Herb / Other

| Attribute | Values / Notes |
| :---- | :---- |
| Flower | **White:** Apple Blossom, Acacia, Honeysuckle, Orange Blossom, Jasmine, etc. **Red:** Violet, Rose, Iris, Peony, Hawthorne, etc |
| Vegetal (pyrazine) | **White:** Gooseberry, Bell Pepper, Jalapeño, Chocolate Mint. **Red:** Green Pepper, Roasted Red Pepper, Bittersweet Chocolate |
| Herbs | **White:** Mint, Basil, Savory, Chervil, Tarragon, Thyme, Sage. **Red:** Mint, Eucalyptus, Sage, Menthol, Oregano |
| Spice | **Red:** Black Pepper |
| Evidence of Botrytis | **White:** Ginger, Honey, Wax |
| Evidence of Oxidation | **White:** Nuts, Applesauce. **Red:** Coffee, Cocoa, Mocha |
| Evidence of Lees | **White:** Dough, Baked Bread, Beer, Yeast |
| Malolactic (MLF) | Oily, Butter, Cream |

#### Earth

| Attribute | Values / Notes |
| :---- | :---- |
| Organic Earth | **White:** Wet Clay, Brettanomyces (Band-Aid), Mushroom. **Red:** Clay, Potting Soil, Wet Leaves, Brettanomyces (Band-Aid), Mushroom |
| Inorganic Earth | Wet Gravel, Slate, Flint, Schist, Granite, Chalk, Sulfur (burnt match) |

#### Oak

| Attribute | Values / Notes |
| :---- | :---- |
| Oak | Yes / No. French / American. New / Used Barrels. **White — New Oak:** Vanilla, Toast, Coconut, Toffee, Butterscotch. **Red — New Oak:** Vanilla, Brown Baking Spices, Cola, Smoke |

### Palate

#### Structure

| Attribute | Values / Notes |
| :---- | :---- |
| Sweetness Level | Bone Dry, Dry, Off-Dry, Medium Sweet, Sweet |
| Body | Low, Medium-Minus, Medium, Medium-Plus, High |
| Acidity | Low, Medium-Minus, Medium, Medium-Plus, High |
| Alcohol | Low, Medium-Minus, Medium, Medium-Plus, High |
| Tannin / Phenolic Bitterness | Low, Medium-Minus, Medium, Medium-Plus, High. **Tannins:** Wood (fine-to-coarse, center of tongue), Grape (coarse bitter, sides/front). **Phenolic Bitterness:** white wines |
| Complexity | *High complexity = more flavors and a profile that evolves from beginning to middle to end.* |
| Length | *Alcohol, acidity, and tannin/phenolic bitterness extend the length of flavor.* |
| Balance | Yes (in balance) / No (out of balance). *More in balance generally indicates higher quality.* |
