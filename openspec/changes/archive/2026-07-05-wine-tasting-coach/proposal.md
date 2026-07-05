## Why

The repo already holds a structured `wine-tasting-grid.md` (Sight → Nose → Palate), but it's an inert reference table — it tells you *what* to evaluate, not *how* to taste for it. When tasting a specific bottle, a novice doesn't know which flavours and structural markers to look for, so the grid goes unused. A coaching skill can turn the grid into an interactive, bottle-aware walkthrough that primes what to expect and guides deliberate practice.

## What Changes

- Add a new `wine-tasting-coach` skill (dir + `SKILL.md`) following the repo's established skill pattern.
- The skill is designed to run inside **Claude on the web**, using its web-search/browse and **Google Drive** connector; there is no local filesystem or repo checkout at runtime.
- The **tasting grid content is embedded directly in `SKILL.md`** (self-contained) rather than read from the repo file, since the repo path is not available on the web.
- The skill operates in **study/calibration mode**: the user supplies the bottle + vintage up front (blind tasting is explicitly out of scope).
- The coach **fetches real web sources** to build a per-session "expectation sheet": prefers the winery tech sheet for the exact bottle, falls back to a grape/region/vintage style archetype, and states clearly when it degrades.
- The coach factors in **vintage and bottle age** (e.g. an 8-year-old red shifts garnet, loses anthocyanin) rather than parroting grape stereotypes.
- The coach walks the embedded grid in order, asking **"prime the category, you confirm"** leading questions that name what's typical but require the user to verify it's actually present — guarding against power-of-suggestion.
- The coach **captures** the user's answers, and closes with a short **calibration comparison** (how the notes lined up with the expected profile — framed as feedback, not grading).
- A **trust gradient** governs sources: tech sheet > style archetype > crowd notes (Vivino/CellarTracker are avoided as primary evidence). The coach **always cross-checks** the specific bottle against a style archetype, even when a tech sheet is found.
- Each completed session is **appended as a row to a Google Sheet named "Wine Tasting Log"** (one row per tasting, columns per grid attribute plus wine/vintage/date/sources/calibration), turning tastings into a filterable, sortable history over time.

## Capabilities

### New Capabilities
- `wine-tasting-coach`: An interactive, bottle-aware tasting coach that fetches an expectation profile for a named wine + vintage, walks the tasting grid section by section with category-priming leading questions, captures the taster's notes, and provides calibration feedback.

### Modified Capabilities
<!-- None. The wine-tasting-grid.md is consumed as reference input, not a spec-governed capability. -->

## Impact

- **Runtime environment**: Claude on the web — assumes web search/browse and the Google Drive connector are available. Not designed for local/CLI use.
- **New files**: `wine-tasting-coach/SKILL.md`, self-contained with the grid embedded (and any supporting reference docs).
- **Writes**: rows to a Google Sheet tasting library in the user's Google Drive (creates the sheet on first use if absent).
- **Consumes**: the grid content is copied from `wine-tasting-grid/wine-tasting-grid.md` into `SKILL.md` at authoring time; the repo file remains the human-maintained source but is not read at runtime.
- **Dependencies**: web search/browse for tech sheets and grape/region profiles; Google Drive/Sheets connector for persistence. No scripts or indexing required.
- **README.md**: add a `wine-tasting-coach` entry and structure listing.
- **No breaking changes** to existing skills.
