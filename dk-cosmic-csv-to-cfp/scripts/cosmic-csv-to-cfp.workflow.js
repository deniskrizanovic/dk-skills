export const meta = {
  name: 'cosmic-csv-to-cfp',
  description: 'Full COSMIC (CFP) measurement of a scope from an epics list: shared rules primer, one agent per epic, coach-grounded, standalone JSON output',
  phases: [
    { title: 'Prime' },      // derive the common COSMIC rules ONCE (token saver)
    { title: 'Measure' },    // epics — auto-throttled fan-out, medium effort
    { title: 'Synthesize' }, // serialize the JS-computed roll-up (near-free)
  ],
}

// ---- inputs ---------------------------------------------------------------
// args = { epics:[...] }  — each epic: {epic_id, epic_name, description, ...}
// Produce it from an epics CSV with scripts/epics_csv_to_args.py.
const epics = args?.epics ?? []
if (!epics.length) throw new Error('Pass {epics:[...]} as args (see epics_csv_to_args.py)')

// ---- structured schema ----------------------------------------------------
// camelCase throughout, matching the two ship schemas. Each functionalProcesses[]
// item is a standalone CosmicMeasureOutput (cosmic_measure_output.schema.json):
// {functionalProcessId, artifact{type,name}, cfp, dataMovements[]}. Movements use
// the child field names (name, order, movementType, dataGroupRef, note, citation).
const EPIC_SCHEMA = {
  type: 'object',
  required: ['epicId', 'epicName', 'epicCfp', 'confidence', 'functionalProcesses', 'gaps'],
  properties: {
    epicId: { type: 'string' },
    epicName: { type: 'string' },
    functionalUsers: { type: 'array', items: { type: 'string' } },
    functionalProcesses: {
      type: 'array',
      items: {
        type: 'object',
        required: ['functionalProcessId', 'artifact', 'dataMovements', 'cfp'],
        properties: {
          functionalProcessId: { type: 'string' },
          artifact: {
            type: 'object',
            required: ['type', 'name'],
            properties: {
              type: { type: 'string' },
              name: { type: 'string' },
            },
          },
          dataMovements: {
            type: 'array',
            items: {
              type: 'object',
              required: ['name', 'order', 'movementType', 'dataGroupRef'],
              properties: {
                name: { type: 'string' },
                order: { type: 'integer' },
                movementType: { type: 'string', enum: ['E', 'X', 'R', 'W'] },
                dataGroupRef: { type: 'string' },
                note: { type: 'string' },
                citation: { type: 'string' },
              },
            },
          },
          dataGroups: {
            type: 'array',
            items: {
              type: 'object',
              required: ['name', 'description'],
              properties: {
                name: { type: 'string' },
                description: { type: 'string' },
              },
            },
          },
          cfp: { type: 'integer' },
        },
      },
    },
    epicCfp: { type: 'integer' },
    confidence: { type: 'string', enum: ['Confirmed', 'Assumed', 'Unknown'] },
    caveats: { type: 'array', items: { type: 'string' } },
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        required: ['gapId', 'category', 'gapOrQuestion', 'impactOrNotes'],
        properties: {
          gapId: { type: 'string' },
          category: { type: 'string' },
          gapOrQuestion: { type: 'string' },
          impactOrNotes: { type: 'string' },
        },
      },
    },
  },
}

// ---- LEVER 1: derive the common rules ONCE (not N×) -----------------------
// The single biggest token saver. One agent asks the cosmic-coach for the
// handful of rules EVERY epic re-derives (SSO round-trip, CRUD movements, the
// single confirmation/error Exit, functional-process boundaries), captures the
// verbatim citations, and returns a compact primer. Injected into all measure
// agents so they only grep the manuals for the UNUSUAL adjudication their epic
// actually needs.
phase('Prime')
const primer = await agent(`
Invoke the \`cosmic-coach\` skill (Q&A mode) and, using its indexed COSMIC v5.0
manuals under manuals-indexed/, produce a COMPACT reusable rules primer covering
the movement patterns that recur across a Salesforce delivery scope. Cover:

1. External-system round-trip (a functional process sends a request to another
   piece of software and receives a response — e.g. federated SSO to an IdP,
   an API call to an external service): how many movements, and which types?
2. CRUD on a persistent object of interest: which movements (Entry/Read/Write/
   Exit) for create, read, update, delete from a user-triggered process?
3. Confirmation and error messages back to the user: how are they counted?
4. What makes two functional processes DISTINCT vs one (triggering event,
   functional user)?
5. The single triggering Entry rule and how all responses to it belong to the
   same functional process.

For EACH, give the rule in one or two sentences PLUS the exact citation
(manuals-indexed/<slug>/<file>.md#L..). Keep the whole primer under ~500 words.
This is a shared reference, so be precise and terse — no worked examples.
`, { label: 'rules-primer', phase: 'Prime', effort: 'medium' })

// ---- LEVER 2: medium effort, primed — measure one epic per agent ----------
const measurePrompt = (epic, i) => `
You are measuring ONE epic for COSMIC functional size (CFP), v5.0. Full detailed
measurement — enumerate every data movement, no aggregation. 1 movement = 1 CFP.

SHARED RULES PRIMER (already derived from the coach — cite these directly, do
NOT re-derive them; only grep the manuals for adjudications NOT covered here):
${primer}

EPIC (epicId ${epic.epic_id}, index ${i}):
${JSON.stringify(epic, null, 2)}

Method:
1. Treat the epic as Functional User Requirements. Identify functional users,
   each functional process, and the objects of interest / data groups.
2. Decompose each process into individual data movements — E/X/R/W. Apply the
   primer rules directly (cite the primer's citation). For anything the primer
   does NOT cover, invoke the \`cosmic-coach\` skill (Q&A mode) OR grep its
   manuals-indexed/ directly, and record the exact citation. Never decide a
   COSMIC rule from your own training — the v5.0 manuals are the sole authority.
3. Where the requirement is too vague to identify a process or its movements,
   DO NOT invent a number. Emit a measurement gap:
   gapId = "CG-${epic.epic_id}-01" (increment NN per gap, deterministic — no
   random, no timestamps), category = "Measurement Gap", with the CFP swing.

OUTPUT SHAPE — each functional process is a standalone CosmicMeasureOutput:
- functionalProcessId: short stable id/name for the process (e.g. "FP1-Login").
- artifact: { type: "epic", name: "<epic name or requirement source>" }.
- dataMovements[]: one object per movement, each with
    name (short label), order (1-based integer sequence), movementType
    (E|X|R|W), dataGroupRef (the object of interest / data group), and — when
    you applied a rule — note (rule justification) and citation
    (manuals-indexed/<slug>/<file>.md#L..). Since these are proposal-grain
    (no source code), OMIT implementationType and isApiCall entirely.
- dataGroups[]: one entry per DISTINCT data group / object of interest the
    process touches (deduplicated — an object entered then written is ONE data
    group, not two). Each entry: name (the data-group identifier) and
    description (a short AUTHORED gloss of what the object carries — new
    information, not a copy of a movement label). Use the SAME name string in
    dataGroups[].name and in the dataMovements[].dataGroupRef values that refer
    to it, so the two align by construction.
- cfp: the process CFP = count of dataMovements (1 movement = 1 CFP).

epicId: echo "${epic.epic_id}" verbatim. epicName: echo the epic's name
("${epic.epic_name}") verbatim so the report can label it.
epicCfp = sum of each process's cfp. confidence: Confirmed only if every process
is fully decomposable and cited; Assumed if you leaned on defensible assumptions;
Unknown if mostly gaps. Return the structured object — do not write files.
`

phase('Measure')
const results = await pipeline(
  epics,
  (epic, _orig, i) =>
    agent(measurePrompt(epic, i), {
      label: `cfp:${epic.epic_id}`,
      phase: 'Measure',
      effort: 'medium',              // mechanical once primed
      schema: EPIC_SCHEMA,
    })
)

const measured = results.filter(Boolean)
// pipeline preserves order, so a null result maps back to epics[i] — record the
// epics whose measure agent died so the roll-up can't pass off a partial run as
// full coverage (silent truncation would read as "everything measured").
const failedEpics = epics
  .filter((_epic, i) => !results[i])
  .map(epic => epic.epic_id)

// ---- LEVER 3: roll-up computed in JS; synth agent only serializes ---------
phase('Synthesize')
const confirmedSum = measured
  .filter(e => e.confidence === 'Confirmed')
  .reduce((a, e) => a + (e.epicCfp || 0), 0)
const totalSum = measured.reduce((a, e) => a + (e.epicCfp || 0), 0)
const allGaps = measured.flatMap(e => e.gaps || [])
const restingOnAssumptions = measured
  .filter(e => e.confidence !== 'Confirmed')
  .map(e => e.epicId)

const fileObject = {
  disclaimer:
    'CFP derived from proposal-grain Functional User Requirements is an approximate early measurement per COSMIC Part 2, not a code-verified count. Epics tagged Assumed/Unknown rest on assumptions and should be re-measured against built artifacts.',
  rollUp: {
    projectCfpCountable: totalSum,
    cfpRange: [confirmedSum, totalSum],
    epicsMeasured: measured.length,
    epicsTotal: epics.length,
    countableEpics: measured.filter(e => e.confidence !== 'Unknown').length,
    epicsRestingOnAssumptions: restingOnAssumptions,
    epicsFailed: failedEpics,
  },
  rulesPrimer: primer,
  epics: measured,
  measurementGaps: allGaps,
}

log(`${measured.length}/${epics.length} epics · ${totalSum} CFP (range ${confirmedSum}-${totalSum}) · ${allGaps.length} gaps`)
if (failedEpics.length) log(`⚠ ${failedEpics.length} epic(s) failed to measure and are EXCLUDED: ${failedEpics.join(', ')}`)

// The object is fully assembled in JS above — deterministic and JS-computed.
// It is returned VERBATIM as the workflow result; the caller writes it to
// $OUT_DIR/cosmic-count.json with the Write tool (see SKILL.md Step 2). We do NOT
// spend an agent to re-serialize it: an LLM echoing the whole object back
// costs the tokens twice and risks silently altering a value the roll-up
// depends on. The return value is the single source of truth.
return {
  projectCfp: totalSum,
  cfpRange: [confirmedSum, totalSum],
  epicsMeasured: measured.length,
  epicsFailed: failedEpics,
  gaps: allGaps.length,
  cosmicCount: fileObject,   // write this to $OUT_DIR/cosmic-count.json verbatim
}
