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

**Cite every source you used** so the user can judge it.

#### Verify before you cite a URL

- **Only cite a URL you actually fetched successfully this session.** Guessed,
  pattern-constructed, or otherwise unverified URLs are **prohibited** — do not emit a
  plausible-looking winery/tech-sheet URL you did not open. A citation that 404s is
  worse than no link.
- **When a source informed the expectation sheet but you could not fetch or verify a
  URL for it, cite a descriptive reference instead** — producer, bottle, and document
  type (e.g. "Catena Zapata — 2018 Malbec tech sheet"). Never present an unverified URL
  as a citation.
- This bar applies to sources shown **inline** during the session, not just the row you
  persist later.

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

### Calibration feedback

Close with a short **calibration comparison** between the user's captured notes and the
expected profile, framed as **learning feedback**:

- **Matched** — where the user's notes lined up with the expected profile.
- **Missed** — where they diverged or overlooked something expected (or noticed something
  the profile didn't predict — worth exploring, not "wrong").
- **Focus next** — one or two concrete things to pay attention to next time.

Do **not** assign a **grade of the taster** — no letter grade, pass/fail verdict, or
quality judgement of the session. Divergence from the expectation is information, not
failure. You **may** accompany the feedback with the **Perception Alignment** metric
below, but it is a calibration mirror (the taster vs. their own past sessions), never a
grade.

### Perception Alignment metric

Compute a per-session **Perception Alignment** metric — of the **high-confidence**
expected markers, how many the taster registered — so the taster can watch their palate
calibrate over time.

**What counts (the denominator):** only attributes where the expectation is
**high-confidence**, i.e. the winery **tech sheet and the grape/region/vintage style
archetype agree** on the marker. This is the load-bearing guardrail: because the
walkthrough primes each category before the user answers, restricting the count to
markers that are genuinely there keeps the metric from simply rewarding agreement.

**What is excluded:** attributes that are **divergent, atypical, low-confidence, or
ungrounded** are left out of **both** the numerator and the denominator and stay purely
qualitative. In particular, any attribute where the cross-check flagged the bottle as
diverging from its style archetype is **not scored** — a correct palate on an atypical
bottle must never be penalised.

**Honesty guardrail:** reporting a note the expectation did not predict, contradicting an
expectation that proves wrong for this bottle, or flagging the bottle as flawed/atypical
**NEVER lowers the metric**. Honest divergence is neutral information, recorded
qualitatively — not scored as a miss. Never build an incentive to agree; an honest palate
is still the point.

**Empty denominator:** if a session has **no** high-confidence markers (e.g. an ungrounded
bottle), show **no metric** for that session and briefly say why (nothing was grounded
strongly enough to calibrate against). Do **not** emit a misleading `0`.

**Display:** show the metric at the close **alongside** the Matched/Missed/Focus-next
feedback — never as a replacement for it — and **paired with its trend across recent
sessions**, so the number reads as a mirror, not a headline verdict. Compute the trend
from the Perception Alignment values in **prior** rows of the `Wine Tasting Log` sheet,
**read via the connector** (see Step 5), e.g. *"6/8 high-confidence markers — up from
your last three sessions."* The current session's row is **not** in the sheet yet (the
user pastes it after the session), so the trend reflects prior sessions and this session
is the new data point being added. Early on there is no trend yet; show the raw count and
note that the trend accrues as more sessions are logged.

---

## Step 5 — Persist to the Google Sheet library

Persist each completed session as a **single row** in a Google Sheet named **exactly**
`Wine Tasting Log` in the user's Google Drive, so tastings accumulate into a filterable,
sortable history.

**Connector reality — read yes, append no.** The Google Sheet connector can **read** a
sheet but **cannot append** to one. So:

- **Append directly only if the connector supports appending.** If a future connector
  gains append, add the row for the user automatically (the append procedure below).
- **Because the current connector cannot append,** the practical save path is to emit a
  **tab-delimited (TSV) row** for the user to copy and paste into `Wine Tasting Log`
  (see "Tab-delimited copyable row" below). This is the normal path today, not a rare
  degraded mode.
- **The connector's working job today is *reading*** prior rows — that is how the
  **Perception Alignment trend** in Step 4 is computed. Keep reading (for the trend) and
  writing (the pasted row) clearly separate: reads work now; writes are manual paste.

### Column schema (stable across sessions)

In order, left to right:

1. **Identity columns:** `Wine`, `Vintage`, `Tasting Date`, `Region/Producer`.
2. **One column per grid attribute** (see the embedded grid — Clarity, Brightness,
   `Color Intensity`, Color, … `Aroma Intensity` … through Balance), holding the user's
   observation for that attribute. Every grid-attribute header is **unique** — the grid's
   two intensity attributes are `Color Intensity` (Sight → Color) and `Aroma Intensity`
   (Nose → Impression), never a shared `Intensity`, so mapping an observation to a column
   by header name is unambiguous.
3. **Cited-sources columns:** `Tech Sheet Source`, `Style Archetype Source` (and any
   other sources used). Each source cell holds **only** a URL you fetched successfully
   this session **or** a descriptive reference (producer + bottle + document type) — it
   **MUST NOT** contain a guessed or unverified URL.
4. **Source-capture-date column:** `Source Captured Date` — the date you fetched the
   session's sources, so later link rot is explainable as drift rather than a bad
   citation.
5. **Calibration summary column:** `Calibration Summary` — the human-readable
   matched/missed/focus-next text.
6. **Perception Alignment column:** `Perception Alignment` — the session's metric (see
   Step 4), so the trend can be computed from history. Record it as the count over the
   high-confidence denominator (e.g. `6/8`). Leave the cell **blank** when the session had
   an empty denominator (no high-confidence markers) — a blank is not a zero.

### Tab-delimited copyable row (current save path)

Because the connector cannot append, hand the user a **tab-delimited row** they paste
into `Wine Tasting Log`. TSV pastes into Google Sheets as one row with each cell landing
in an adjacent column — no import dialog. Emit it inside a fenced code block so it copies
cleanly, and tell the user to paste it as a new row in `Wine Tasting Log`.

**Format rules (all mandatory — a pasted line must land as exactly one aligned row):**

1. **Exact column order.** Join the cells with a **single tab** (`\t`) in the **exact
   order of the Column schema above**: identity columns → one per grid attribute
   (Clarity … Balance) → source columns → `Source Captured Date` → `Calibration Summary`
   → `Perception Alignment`.
2. **One line per session.** The whole session is a **single line** — no line breaks
   within the row.
3. **Sanitize every cell.** Before joining, **replace any tab or newline character inside
   a cell value with a single space.** `Calibration Summary` and the per-attribute
   observations are free text; a stray tab or newline would shatter or wrap the row
   across columns. Sanitizing flattens in-cell formatting slightly — column integrity
   wins.
4. **Field count matches the header.** The data row MUST have the **same number of
   fields as the header**, including **blank** fields for empty cells (an
   empty-denominator `Perception Alignment`, or an attribute the taster did not address).
   Never drop a column to avoid an empty value — emit an empty field so everything stays
   aligned.

**Header row — on request / first use.** Emit **only the data row by default.** Provide
the tab-delimited **header row** (the Column schema joined by tabs, same order) when the
user asks for it **or** when no `Wine Tasting Log` sheet exists yet — in the latter case,
tell the user to create a sheet named **exactly** `Wine Tasting Log`, paste the header as
row 1, then paste the data row beneath it.

### Append procedure (only if the connector supports appending)

If a connector that supports appending is available, write the row directly instead of
handing over TSV:

1. **Locate the sheet:** search Drive for a sheet named exactly `Wine Tasting Log`.
2. **First use — create it:** if none exists, create a sheet named exactly
   `Wine Tasting Log` with the header row from the schema above **before** appending the
   first tasting.
3. **Append:** add **one row per completed tasting**, mapping each observation to the
   **existing column by header name** so rows stay aligned across sessions. Write the
   session's `Perception Alignment` value into its column (or leave it blank for an
   empty-denominator session).
4. **Schema evolution:** if the grid gains or loses attributes later, **add new columns
   at the end** — never reorder or duplicate existing columns (old rows would misalign).
   If you open a `Wine Tasting Log` that **predates** the `Source Captured Date` column,
   append that column at the end too (older rows simply leave it blank); do not reorder
   existing columns to slot it in. Apply the **same rule** to the `Perception Alignment`
   column: if an existing sheet lacks it, append it at the end and leave older rows blank
   — never reorder existing columns to insert it.

The **same schema-evolution rule** applies to the tab-delimited header/data row: grow the
schema by appending new columns at the end so header and row stay in lockstep.

### Drive-unavailable fallback (connector entirely absent)

This is a **distinct** case from the TSV path above. The TSV path assumes the connector
is present (it can read the sheet, just not append). If the Google Drive connector is
**not available at all** at save time: still **complete** the tasting and calibration,
**tell the user** you could not reach the library, and **return the filled results
inline** — the filled grid + calibration + the **tab-delimited row** (per the format
rules above), plus the header row, so nothing is lost and the user can paste once a sheet
is reachable.

---

## Embedded Tasting Grid

> Source of truth: `reference/wine-tasting-grid.md` (this skill directory). Re-sync on change.

### Sight

#### Color

| Attribute | Values / Notes |
| :---- | :---- |
| Clarity | Clear, Slight Haze, Murky, presence of Sediment, gas (bubbles) |
| Brightness | Dull, Bright, Day Bright, Star Bright, Brilliant |
| Color Intensity | Low, Medium-Minus, Medium, Medium-Plus, High. *Over time reds will lose their color (anthocyanin) and whites will become richer in color eventually turning brown.* |
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
| Aroma Intensity | Low, Medium-Minus, Medium, Medium-Plus, High. *High-alcohol wines (warmer climates) evaporate more and smell more intense. Serving temperature also affects aromatic intensity — a whiff, not the whole story.* |
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
