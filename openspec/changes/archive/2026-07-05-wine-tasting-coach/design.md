## Context

`dk-skills` is a collection of Claude Code skills, each a directory with a `SKILL.md` and optional supporting files. The repo contains `wine-tasting-grid/wine-tasting-grid.md` — a structured but inert reference table covering Sight → Nose → Palate.

This skill targets a different runtime than the rest of the repo: **Claude on the web**, not the local CLI. That means no repo checkout and no local filesystem at runtime, but web search/browse and a **Google Drive** connector are available. Two consequences follow: the grid content is **embedded in `SKILL.md`** (the repo file can't be read on the web), and persistence goes to **Google Sheets in Drive** rather than local files.

The nearest design precedent is `dk-cosmic-counting-coach`: a "coach" skill whose defining principle is *grounded, no invention* (cite the manuals or refuse). The wine coach borrows that grounding instinct but deliberately inverts one rule — it *uses* the web, because the whole point is bottle-aware coaching. The design challenge is keeping that web use trustworthy given how unreliable wine content is online.

This is a prompt-and-workflow skill (no scripts, no indexing). All behaviour lives in `SKILL.md` as instructions the model follows, using the web and Drive connectors available in the Claude-web environment.

## Goals / Non-Goals

**Goals:**
- Turn the existing grid into an interactive, per-bottle coached walkthrough.
- Ground "what to expect" in real, cited web sources with a clear trust gradient.
- Prime the user toward typical markers without asserting they are present (guard against power-of-suggestion).
- Adjust expectations for vintage climate and current bottle age.
- Produce a filled grid + short calibration feedback at close.

**Non-Goals:**
- Blind tasting / guess-the-grape mode (the user names the bottle up front).
- Scoring or grading the user.
- Local/CLI use — this skill assumes the Claude-web environment (web + Drive). Not designed for offline or repo-local runs.
- Any scripts or indexing.
- Modifying the repo's grid file at runtime — its content is embedded into `SKILL.md` at authoring time.
- Purchase recommendations, cellaring/investment advice, or pairing menus.

## Decisions

**1. Single mode: study/calibration (bottle up front).**
We considered supporting blind, guided-discovery, and study modes selectably. Rejected for v1 — the user chose study mode decisively, and multi-mode branching would bloat the skill and blur the leading-question contract. One coherent flow is easier to get right.

**2. Fetch real sources over a trust gradient rather than recall from training.**
Alternatives: answer from model memory (fast, but fabricates specific-bottle facts — the exact failure the COSMIC coach was built to avoid) or fetch everything indiscriminately (drags in low-quality crowd notes). Chosen: fetch, preferring winery tech sheet → grape/region/vintage archetype → (avoid) crowd notes, and cite what was used. Graceful degradation is explicit: if the specific bottle's sheet isn't found, the coach announces it is coaching from the style archetype.

**3. "Prime the category, you confirm" question framing.**
Alternatives: "tell me what to find" (max calibration, but power-of-suggestion makes the user report phantom flavours) or "open, no priming" (that's blind mode, which we excluded). Chosen: name the typical marker as a hypothesis and require the user to verify presence. This keeps study-mode usefulness while keeping the user's palate honest, and it makes each attribute a testable interaction.

**4. The embedded grid drives walkthrough order.**
The grid is the spine, not just background reference; the coach steps through its sections/attributes in published order. Because the skill runs on Claude web with no repo checkout, the grid content is **embedded directly in `SKILL.md`** rather than read from the repo file. Alternatives considered: read the grid from a file in Google Drive (single source of truth, but adds a setup dependency and a fetch on every run) or a Drive-preferred / embedded-fallback hybrid (most robust, more logic). Chosen: embed — simplest and fully self-contained, at the cost that the embedded copy and the repo's `wine-tasting-grid.md` must be kept in sync manually when the grid evolves.

**5. Vintage + age awareness as a first-class step.**
The expectation sheet is adjusted for the vintage's climate and the wine's age at tasting. Rationale: the grid itself notes anthocyanin loss and garnet shift with age; parroting the young-wine grape stereotype would mislead the taster on an older bottle.

**6. Calibration feedback, not a score.**
Close with "what matched / what you missed / focus next," framed as learning. A numeric score would imply a precision the exercise doesn't have and would discourage honest note-taking.

**7. Persist each tasting as a row in a Google Sheet library.**
Every completed session is appended as one row to a Google Sheet in the user's Drive, building a personal library over time. Alternatives considered: a native Google Doc per tasting (readable/shareable, but each tasting is a separate file — no cross-tasting querying) or a markdown file per tasting in Drive (preserves table structure, same one-file-per-tasting limitation). Chosen: a single Sheet named exactly **"Wine Tasting Log"** with one row per tasting, so the library becomes filterable and sortable — "show me every high-acid Sangiovese I've tried," "how have my Malbec notes drifted." The fixed name removes any ambiguity about where tastings go: the coach searches Drive for "Wine Tasting Log" and creates it under that exact name if absent. Schema: identity columns (wine, vintage, date, region/producer), one column per grid attribute, cited-sources columns, and a calibration-summary column; the coach creates the sheet with a header row on first use and appends by matching existing headers so rows stay aligned.

Trade-off: the grid has ~25 attributes, so the sheet is **wide**, and free-text observations get compressed into single cells. Accepted — width is the price of a queryable, single-file history; a taster who wants prose can still read the calibration summary column. If wide-sheet ergonomics become painful, a future revision could split into a normalized two-sheet model (tastings + attributes), but that is out of scope for v1.

**8. Always cross-check the specific bottle against a style profile.**
Even when a producer tech sheet is found, the coach also consults a grape/region/vintage style archetype and reconciles the two. Rationale: a tech sheet states winemaking facts (blend, oak, ABV) but the archetype supplies the expected sensory markers and flags when a bottle is atypical for its style. Cross-checking catches tech-sheet gaps and grounds the sensory expectations that actually drive the walkthrough. Both sources are cited.

## Risks / Trade-offs

- **Unreliable web sources** → Enforce the trust gradient in `SKILL.md`; prefer producer sheets, treat crowd notes as low-confidence, always cite so the user can judge.
- **Bottle not findable online** → Graceful fallback to grape/region/vintage archetype with an explicit disclosure that it's the style, not the bottle.
- **Power-of-suggestion contaminating notes** → The "confirm, don't assert" framing is a hard rule; the coach records unexpected notes faithfully and never rewrites them to fit the expectation.
- **Web fetch unavailable in a session** → The coach should state it can't ground the expectation and offer to proceed from general style knowledge, clearly flagged as ungrounded (lower value, but not a hard failure).
- **Google Drive connector unavailable at save time** → The coach still completes the tasting and calibration, tells the user it couldn't save, and returns the filled results inline so nothing is lost.
- **Embedded-grid drift** → The grid is duplicated between the repo file and `SKILL.md`; they can diverge over time. Mitigation: treat the repo's `wine-tasting-grid.md` as the human-maintained source and re-sync the embedded copy when it changes; note this in the skill.
- **Wide-sheet ergonomics** → ~25 attribute columns is unwieldy to read horizontally. Mitigation: keep a human-readable calibration-summary column; revisit a normalized schema only if needed.
- **Schema evolution** → If the grid gains/loses attributes later, old rows won't have the new columns. Mitigation: append by header-name matching and add new columns at the end rather than reordering.

## Open Questions

- Should the cited expectation sheet itself also be stored (e.g. as a note/comment or a second tab) rather than just source URLs in a cell? Minor; resolve in implementation.
