---
name: wine-deal-evaluator
description: "Evaluate whether a wine offer from a promotional email is a good deal. Use this skill whenever   the user pastes in text from a wine offer, buy email, flash sale, or wine merchant newsletter —   even if they just say \"is this worth buying?\" or \"what do you think of this wine deal?\".   The skill researches pricing across Australian retailers, checks Wine-Searcher for market   price context, looks up critic scores and vintage quality, and returns a verdict scored out   of 10 with clear reasoning."
---
 
# Wine Deal Evaluator
 
## Purpose
 
Given wine offer text (pasted from an email or newsletter), research the wine and return a
structured verdict on whether it's a good deal for an Australian buyer.
 
---
 
## Step 1 — Parse the Offer
 
Extract from the pasted text:
- **Wine name** (producer + label)
- **Vintage** (year)
- **Variety / style** (e.g. Shiraz, Burgundy, Champagne)
- **Region / appellation**
- **Format** (bottle size, case quantity)
- **Offered price** (per bottle AUD)
- **Any claimed savings or RRP** stated in the email
If the format is ambiguous (e.g. "case of 6"), calculate per-bottle price.
 
---
 
## Step 2 — Research (run these searches in parallel where possible)
 
### 2a. Wine-Searcher — Australian market price
Search: `wine-searcher.com "[producer] [wine name] [vintage]" australia`
- Find the **median / average Australian retail price** (AUD)
- Note lowest current Australian listing if visible
- wine-searcher URL pattern: `https://www.wine-searcher.com/find/[wine+name]/[vintage]/australia`
### 2b. Retailer pricing — check these Australian sites
Search each for the specific wine + vintage. Check availability and current price:
 
| Retailer | URL |
|---|---|
| Wine Direct | winedirect.com.au |
| Vintage Cellars | vintagecellars.com.au |
| Cracka Wines | crackawines.com.au |
| The Wine Collective | thewinecollective.com.au |
| Nicks Wine Merchants | nicks.com.au |
| Langtons | langtons.com.au |
| Winestar | winestar.com.au |
| Buzz Wines | buzzwines.com.au |
| Door to D'Or | doortodor.com.au |
 
For each: record price per bottle (AUD) if found, or note "not listed".
 
### 2c. Critic scores
Search for scores from any of these sources (use whichever you can find):
- **James Halliday** (essential for Australian wines)
- **Wine Advocate / Robert Parker**
- **Wine Spectator**
- **Decanter**
- **Jancis Robinson**
Note the score, reviewer, and any tasting notes if available.
 
### 2d. Vintage quality
Search: `"[region] [vintage] vintage report"` or `"[vintage] [appellation] vintage quality"`
- Summarise the vintage reputation in 1–2 sentences (e.g. "2018 Barossa was a warm, early
  harvest year producing concentrated but sometimes overripe reds — generally rated 88–90/100
  for the region")
- Note if it's a celebrated, average, or poor vintage
### 2e. Drinking window
Search for drinking window guidance using critic notes, vintage reports, and comparable wines:
- Search: `"[producer] [wine name] [vintage] drink" OR "drinking window"` to find critic guidance
- If no specific note is found, look for drinking windows on **comparable wines** from the same
  appellation, producer tier, and vintage: e.g. "Chassagne-Montrachet 1er Cru 2022 drinking window"
- Derive three time markers:
  - **Approachable from:** earliest the wine will be enjoyable (may already be open if older)
  - **Peak window:** when the wine is expected to be at or near its best
  - **Drink by:** outer limit before expected decline
- Note the **current status** relative to today's date: e.g. "currently closed", "entering its
  window", "at peak", "past peak"
- If the wine is very young (e.g. 2023/2024 en primeur just released), note whether early
  opening is recommended or if patience is required
### 2f. Wine profile (what's in the bottle)
Draw on appellation rules, producer notes, and general knowledge to establish:
- **Grape variety / blend**: what grapes are used, and whether this is mandated by appellation
  law or specific to the producer (e.g. "100% Chardonnay — required by AOC rules for white
  Chassagne-Montrachet"; "Typically 85% Grenache, 15% Syrah for this producer")
- **Winemaking style**: key choices that shape the wine — oak regime (new vs neutral, size,
  duration), use of whole bunches, MLF, filtration, élevage length, organic/biodynamic status
  if relevant
- **Vineyard / terroir**: soil type, altitude, aspect, vine age if known, and how that
  translates to the wine's character (e.g. clay-limestone = more body and richness; higher
  altitude = more acid and tension)
- **Typical flavour profile**: what to expect in the glass — primary fruit character, secondary
  development (oak, lees, MLF influence), and tertiary notes if aged. Keep this grounded and
  specific to the appellation and producer style, not generic.
- **Style in context**: where this wine sits relative to neighbours — e.g. "Chassagne tends
  richer and more textural than Puligny; Les Chenevottes is one of the lighter, more citrus-
  driven crus, sitting close to the Montrachet boundary"
Use training knowledge for well-known appellations (Burgundy, Bordeaux, Rhône, Barossa, etc.).
Only search if the producer or appellation is obscure or the style is unusual.
 
---
 
## Step 3 — Score and Verdict
 
### Scoring framework (out of 10)
 
Calculate a score based on these weighted factors:
 
| Factor | Weight | How to score |
|---|---|---|
| **Price vs Wine-Searcher median** | 35% | >20% below = full marks; at median = 5/10; above median = low |
| **Price vs cheapest Aus retailer found** | 25% | Beat or match = 8–10; slightly above = 4–6; much higher = 1–3 |
| **Critic score** | 25% | 95+ = 10; 92–94 = 8; 90–91 = 6; 88–89 = 4; <88 = 2; unknown = 5 |
| **Vintage quality** | 15% | Outstanding = 10; Good = 7; Average = 5; Poor = 2; Unknown = 5 |
 
Multiply each sub-score by its weight, sum to get final score out of 10. Round to one decimal.
 
### Verdict thresholds
- **8.0–10**: ✅ Strong buy — excellent deal
- **6.0–7.9**: 🟡 Good deal — worth it if you like the style
- **4.0–5.9**: ⚠️ Borderline — shop around first
- **<4.0**: ❌ Pass — overpriced or underwhelmingly rated
---
 
## Step 4 — Output Format
 
Present the result in this structure:
 
---
### 🍷 [Producer] [Wine Name] [Vintage]
**Offered price:** $XX | **Format:** [bottle / 6-pack / etc.]
 
#### What's in the Bottle
**Grape:** [Variety or blend — e.g. "100% Chardonnay (AOC mandated)"]
**Vineyard:** [Soil, aspect, vine age, altitude if known — 1 sentence]
**Winemaking:** [Oak regime, élevage, any notable choices — 1 sentence]
**Style:** [Where this sits in its region/appellation context — 1–2 sentences placing it relative to neighbours or the producer's range]
**Expect in the glass:** [Specific flavour profile — primary, secondary, any tertiary notes for older vintages. Concrete and informative, not generic marketing language.]
 
#### Price Check
| Source | Price (per bottle) |
|---|---|
| Offered | $XX |
| Wine-Searcher median (Aus) | $XX |
| [Retailer 1] | $XX or not listed |
| [Retailer 2] | $XX or not listed |
| … | … |
 
#### Critic Score
[Score] / 100 — [Reviewer], [Year reviewed if known]
> [Tasting note excerpt if available — keep to 1–2 sentences, paraphrased]
 
#### Vintage
[Vintage year] [Region]: [1–2 sentence vintage summary]
 
#### Drinking Window
**Approachable from:** [Year] | **Peak:** [Year range] | **Drink by:** [Year]
**Now:** [Current status — e.g. "Closed — needs 2–3 years minimum" / "Just entering its window" / "At peak" / "Drink soon"]
[1–2 sentences of context: based on comparable wines, vintage character, or critic guidance — be specific about what's driving the window, e.g. high acidity vintage = longer, warm vintage = earlier]
 
#### Deal Score: X.X / 10
**Verdict:** [✅ / 🟡 / ⚠️ / ❌] [One-sentence plain-English verdict]
 
**Reasoning:** [2–4 sentences explaining the score — be specific about what's driving it up
or down. E.g. "The price is 18% below Wine-Searcher median which is solid, but this is a
mediocre vintage for the region and the wine is widely available at similar prices."]
 
---
 
## Notes & Edge Cases
 
- **Unfindable wine**: If the wine appears to be a merchant-exclusive, negociant label, or
  private bottling with no independent pricing, say so clearly and score the pricing dimension
  as neutral (5/10) — these are often overpriced but sometimes genuine deals.
- **No critic score found**: Score that dimension 5/10 and note absence. Don't invent scores.
- **Multiple wines in one email**: Evaluate each separately with its own score block.
- **Currency**: All prices in AUD. If Wine-Searcher shows USD, convert at current rate.
- **Do not recommend purchasing from sites outside Australia.**
