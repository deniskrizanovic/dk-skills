# COSMIC Functional-Size Measurement (CFP)

> **Disclaimer.** CFP derived from proposal-grain Functional User Requirements is an approximate early measurement per COSMIC Part 2, not a code-verified count. Epics tagged Assumed/Unknown rest on assumptions and should be re-measured against built artifacts.

## Roll-up

| Metric | Value |
|---|---|
| Project CFP (countable) | **75** |
| CFP range (Confirmed floor → measured) | **0 – 75** |
| Epics measured | 12 of 12 |
| Countable epics | 12 |
| Epics resting on assumptions | 12 of 12 |

*Range note: the low bound (0) is the sum of **Confirmed** epics only. 12 of 12 epics rest on assumptions and should be re-measured against built artifacts.*

### Per-epic summary

| Epic | Name | CFP | Confidence | Processes | Gaps |
|---|---|---|---|---|---|
| E01 | Log a Lost Pet Report | **7** | Assumed | 1 | 4 |
| E02 | Request Tree Lopping or Removal | **7** | Assumed | 1 | 3 |
| E03 | Check Rates Payment Status | **5** | Assumed | 1 | 2 |
| E04 | Set Up a Rates Payment Plan | **6** | Assumed | 1 | 2 |
| E05 | Report a Pothole or Road Defect | **6** | Assumed | 1 | 3 |
| E06 | Book a Hard Rubbish Collection | **8** | Assumed | 1 | 3 |
| E07 | Lodge a Noise or Nuisance Complaint | **5** | Assumed | 1 | 2 |
| E08 | Apply for a Parking Permit | **10** | Assumed | 1 | 4 |
| E09 | Update Contact Details on Account | **4** | Assumed | 1 | 2 |
| E10 | Verify Caller Identity | **4** | Assumed | 1 | 2 |
| E11 | Look Up Council Asset by Location | **5** | Assumed | 1 | 2 |
| E12 | Cancel a Hard Rubbish Collection Booking | **8** | Assumed | 1 | 3 |
| | **Total** | **75** | | | 32 |

---

## Data groups

| Data group | Functional processes | Description |
|---|---|---|
| Accepted Item Categories | E06/FP1-BookHardRubbishCollection | Reference list of item categories eligible for hard/bulky waste collection, used to validate submitted items. |
| Agent Result Message | E04/FP1-SetUpPaymentPlan | On-screen confirmation or validation/error message returned to the agent for all possible outcomes. |
| Animal Registry Record | E01/FP1-Log-Lost-Pet-Report | Stored microchip registrations and found-pet records used to surface potential matches for the reported pet. |
| Asset Location Query | E11/FP1-LookUpAssetByLocation | The location identifier submitted by the caller and forwarded to the GIS service: an address or a map pin (coordinates) pinpointing where to look for an asset. |
| Asset Ownership Details | E11/FP1-LookUpAssetByLocation | The asset record returned for the location: asset type (tree, road, drain, streetlight), council-ownership status, asset attributes, and the responsible team. |
| Booking | E12/FP1-CancelBooking | The persisted hard/bulky-waste collection booking: collection window, item details, status, and the resident it belongs to. The lookup key (address or booking reference) identifies this same object of interest. |
| Booking Result Message | E06/FP1-BookHardRubbishCollection | On-screen acceptance/error message to the agent covering all outcomes (e.g. quota exhausted, items rejected, booking confirmed). |
| Boundary Query | E02/FP1-SubmitTreeLoppingRequest | Tree location coordinates/address sent to the asset/GIS boundary service to be checked against council land ownership. |
| Caller Case Link | E05/FP1-ReportDefect | Association attaching the current caller to an already-existing defect case when a duplicate is detected. |
| Cancellation SMS | E12/FP1-CancelBooking | The outbound confirmation message sent to the caller's mobile via the SMS gateway, carrying the cancelled-booking details. |
| Case Reference | E07/FP1-LodgeNuisanceComplaint | The case reference/acknowledgement identifier returned to the complainant (suppressed when the complainant is anonymous). |
| Change Confirmation | E09/FP1-UpdateContactDetails | The acceptance/error message returned to the agent to relay to the resident indicating whether the contact-detail change was saved or failed validation. |
| Collection Booking | E06/FP1-BookHardRubbishCollection | The booking captured by the agent: resident address, item types and counts, and preferred collection window. |
| Collection Date Allocation | E06/FP1-BookHardRubbishCollection | The next available collection date returned by the waste scheduling service for the requested address/window. |
| Confirmation/Error Message | E01/FP1-Log-Lost-Pet-Report, E05/FP1-ReportDefect, E07/FP1-LodgeNuisanceComplaint | Acceptance or error feedback shown to the agent covering all outcomes of the logging attempt. / Acceptance or error notification returned to the agent for the submission attempt. / Acceptance or validation/error notifications raised while lodging the complaint. |
| Council-Land Validation Result | E02/FP1-SubmitTreeLoppingRequest | The ownership/boundary determination returned by the GIS service indicating whether the tree sits on council land. |
| Crew Work Notification | E02/FP1-SubmitTreeLoppingRequest | The dispatched works item pushed to the Parks & Gardens crew, carrying location, reason and priority. |
| Customer Contact Details | E09/FP1-UpdateContactDetails | The resident's council customer account contact attributes (phone, email, postal address) — the object of interest that is entered as new values, read in its existing state, and written back in modified form to the customer master. |
| Customer Master Record | E10/FP1-VerifyCallerIdentity | The stored identity attributes for the customer (name, address, DOB, account reference) held in the customer master, read to compare against the supplied answers. |
| Defect Report | E05/FP1-ReportDefect | Caller-reported defect details captured by the agent: location, defect type (pothole/footpath/road defect) and severity. |
| Error/Confirmation Message | E02/FP1-SubmitTreeLoppingRequest, E03/FP1-CheckRatesPaymentStatus, E08/FP1-ApplyForParkingPermit | The single grouped set of validation error and confirmation messages returned to the agent (e.g. tree not on council land, missing data, request accepted). / Outcome notification to the agent, e.g. account not found or lookup failed. / Status message covering all validation, residency, allowance, and payment failure/acceptance outcomes. |
| Free Collection Quota | E06/FP1-BookHardRubbishCollection | The resident's remaining number of free hard-rubbish collections for the current year. |
| Hardship Policy Limits | E04/FP1-SetUpPaymentPlan | Council hardship policy parameters (e.g. max term, minimum instalment) against which a proposed plan is validated. |
| Issued Permit | E08/FP1-ApplyForParkingPermit | Existing permits already granted to the address, read to count them against the type's allowance. |
| Lookup Status Message | E11/FP1-LookUpAssetByLocation | Error/confirmation feedback covering outcomes such as no asset found at the location or the asset not being council-owned. |
| Lost Pet Case | E01/FP1-Log-Lost-Pet-Report | The reported incident: caller contact details, pet species/breed/description, last-seen location and date; entered by the agent and persisted as a case with a generated reference. |
| Nuisance Complaint | E07/FP1-LodgeNuisanceComplaint | The lodged complaint: nature of the nuisance (noise, illegal dumping, other), offending address, occurrence dates/times, and the complainant's anonymity preference. |
| Parking Permit | E08/FP1-ApplyForParkingPermit | The newly issued digital residential parking permit record for the vehicle/address. |
| Payment | E08/FP1-ApplyForParkingPermit | Payment request/result exchanged with the external payment service for the calculated fee. |
| Payment Arrangement | E04/FP1-SetUpPaymentPlan | The recorded instalment arrangement (schedule, amounts, dates) persisted against the rate account. |
| Payment Plan Confirmation | E04/FP1-SetUpPaymentPlan | Written confirmation of the agreed payment plan sent to the resident by post or email. |
| Payment Plan Proposal | E04/FP1-SetUpPaymentPlan | Agent-captured proposed instalment amount and payment frequency for the resident's arrears. |
| Permit Application | E08/FP1-ApplyForParkingPermit | Applicant-supplied vehicle registration, residential address, and requested permit type submitted by the agent. |
| Permit Confirmation Email | E08/FP1-ApplyForParkingPermit | Notification carrying issued-permit details sent to the resident on success. |
| Permit Policy | E08/FP1-ApplyForParkingPermit | Reference data for the requested permit type carrying the per-address allowance limit and the applicable fee rate. |
| Property Register Record | E08/FP1-ApplyForParkingPermit | Persistent property/occupancy record used to confirm the applicant resides at the stated address. |
| Queue Routing Instruction | E01/FP1-Log-Lost-Pet-Report | The assignment/routing payload directing the created case into the Animal Management work queue. |
| Rate Account | E04/FP1-SetUpPaymentPlan | The resident's rate account carrying the outstanding arrears balance used to compute the schedule. |
| Rate Account Identifier | E03/FP1-CheckRatesPaymentStatus | The lookup key supplied by the agent to locate the rate account — property number or property address. |
| Rate Payment Status | E03/FP1-CheckRatesPaymentStatus | The account's financial state returned by the finance system: current balance, last payment date and amount, any arrears, and next instalment due date. |
| Regulatory Case | E07/FP1-LodgeNuisanceComplaint | The regulatory case record created from the complaint and routed to the Local Laws / Environmental Health team for action. |
| Resident Acknowledgement | E02/FP1-SubmitTreeLoppingRequest | Acknowledgement email to the resident confirming logging of the request plus the expected response time (data beyond a bare confirmation). |
| Resident Allowance | E12/FP1-CancelBooking | The resident's free hard-rubbish-collection allowance for the year (count of free collections used/remaining) that is credited back when a booking is cancelled. |
| Result Message | E12/FP1-CancelBooking | The on-screen outcome shown to the agent: success confirmation, or the error for a not-found booking or an already-passed collection window. |
| Road Defect Works Order | E05/FP1-ReportDefect | Persisted road-defect / works-order record — read as the candidate population for duplicate detection within a radius, and written when a new order is created and assigned to the Roads team. |
| SMS Booking Confirmation | E06/FP1-BookHardRubbishCollection | Confirmation of the finalised booking (date, items) sent to the resident via SMS. |
| SMS Confirmation | E01/FP1-Log-Lost-Pet-Report | Outbound message to the caller carrying the case reference number, handed to the SMS gateway. |
| Tracking Reference | E05/FP1-ReportDefect | Case / works-order reference returned to the caller so they can track the reported defect. |
| Tree Works Request | E02/FP1-SubmitTreeLoppingRequest | The captured request record: tree location (address or map pin), reason for lopping/removal, reported hazard, derived priority, and any emailed photos. |
| Verification Answers | E10/FP1-VerifyCallerIdentity | The caller-supplied knowledge-based answers submitted by the agent for checking: name, property address, date of birth, or account reference. |
| Verification Attempt Log | E10/FP1-VerifyCallerIdentity | The audit record of a verification attempt (outcome, which factors were checked, timestamp) written against the customer record. |
| Verification Result | E10/FP1-VerifyCallerIdentity | The verified/failed outcome returned to the agent indicating whether the caller's identity was confirmed. |

---

## E01 — Log a Lost Pet Report

**Epic CFP: 7 · Confidence: Assumed**

> A resident calls the council contact centre to report a lost or found pet (e.g. "I've lost my cat"). The agent captures caller details, pet species/breed/description, last-seen location and date, and a contact number. The system checks the animal registry for any matching microchip or found-pet records and displays potential matches to the agent. A lost-pet case is created, an SMS confirmation with a case reference is sent to the caller, and the case is routed to the Animal Management queue.

**Functional users:** Contact centre agent · SMS gateway · Animal Management queue system

### FP1 — FP1-Log-Lost-Pet-Report — 7 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Lost Pet Case | Triggering Entry. RULE 13: one Entry counts for entry of all data describing a single object of interest (caller, pet, location/date, contact captured on the report form). Exactly one triggering Entry per process (RULE 10). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99 |
| 2 | **R** | Animal Registry Record | Read from persistent storage to check for matching microchip/found-pet records (retrieve pattern, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Animal Registry Record | Exit returning the matched registry data to the agent (functional user); same object of interest as the Read. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Lost Pet Case | Write to persistent storage creating the case (Create pattern = Entry + Write, RULE 19). Object entered then written is one data group. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | SMS Confirmation | Exit to the SMS gateway. This carries the case reference (data beyond mere acceptance), so it is a distinct Exit counted separately from the agent's confirmation message. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 6 | **X** | Queue Routing Instruction | Exit sending the routing/assignment to the Animal Management queue system (treated as a separate functional user). See gap CG-E01-02 on the alternative treatments. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | Confirmation/Error Message | One Exit accounts for all confirmation/error messages from the process, regardless of count or cause. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E01)

**CG-E01-01 · Measurement Gap** — Is the animal-registry match check + display to the agent part of the case-logging process, or a distinct agent-triggered search process (agent enters criteria, reviews matches, then separately submits to create the case)? The epic describes it as one continuous narrative.

*Impact:* Modelled as one FP (7 CFP). If split into a separate Search FP (E criteria + R + X = 3 CFP) plus a Create-Case FP (E + W + X SMS + X queue + X confirm = 5 CFP), epic total becomes 8. CFP swing: +1.

**CG-E01-02 · Measurement Gap** — How is 'routed to the Animal Management queue' realised? An Exit to a separate queue/system, a Write to a persistent queue store, or merely a queue/assignment attribute set as part of the case Write (not a separate movement)?

*Impact:* Counted as one Exit. If it is just an attribute of the case Write, this movement disappears. CFP swing: -1 to 0.

**CG-E01-03 · Measurement Gap** — Are 'matching microchip records' and 'found-pet records' one object of interest (a single animal registry) or two distinct objects of interest stored separately?

*Impact:* Modelled as one Read + one Exit over 'Animal Registry Record'. If two distinct objects, this becomes 2 Reads + up to 2 Exits. CFP swing: 0 to +2.

**CG-E01-04 · Measurement Gap** — Are the caller/contact details a separate object of interest from the reported pet/case, requiring a second (non-triggering) Entry?

*Impact:* Modelled as attributes of a single 'Lost Pet Case' object under RULE 13, giving one triggering Entry. If the caller is a distinct object of interest entered in the same process, add one Entry. CFP swing: 0 to +1.

---

## E02 — Request Tree Lopping or Removal

**Epic CFP: 7 · Confidence: Assumed**

> Resident requests that a council-owned tree be lopped or removed (overhanging branches, safety hazard). The agent captures the tree location (address or map pin), reason, and photos if emailed in. The system validates that the tree sits on council land by querying the asset/GIS boundary service, creates a works request, assigns a priority based on the reported hazard, and notifies the Parks & Gardens crew. The resident receives an acknowledgement email with expected response time.

**Functional users:** Resident (via agent) / Contact-centre agent capturing the request · Asset/GIS boundary service (peer software) · Parks & Gardens crew (recipient of works notification) · Resident (recipient of acknowledgement email)

### FP1 — FP1-SubmitTreeLoppingRequest — 7 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Tree Works Request | Single triggering Entry for all data describing one object of interest (location, reason, photos) per RULE 13. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99 |
| 2 | **X** | Boundary Query | Request leg of an external-system round-trip to the asset/GIS boundary service (Exit then Entry). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 3 | **E** | Council-Land Validation Result | Response leg of the external-system round-trip; belongs to the same functional process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 4 | **W** | Tree Works Request | Create of a persistent object of interest = Entry (order 1) + Write; priority assigned from entered hazard requires no persistence Read. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Crew Work Notification | One-way outbound notification to another functional user (no response prompted), so a single Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 6 | **X** | Resident Acknowledgement | Carries data beyond bare confirmation (expected response time), so counted as its own Exit rather than folded into the error/confirmation Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 7 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation messages (e.g. tree not on council land, missing data) from this process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E02)

**CG-E02-01 · Measurement Gap** — Are emailed-in photos treated as attributes of the tree request (folded into the single triggering Entry) or as a separate object of interest with its own Entry (and possible Write)? The description says photos are captured 'if emailed in'.

*Impact:* Modelled as attributes of the Tree Works Request (one Entry). If photos are a distinct object of interest entered/stored separately: +1 E (and possibly +1 W). CFP swing +1 to +2.

**CG-E02-02 · Measurement Gap** — Does 'assigns a priority based on the reported hazard' derive priority purely from entered data, or does it read a stored hazard-to-priority matrix / SLA table from persistent storage?

*Impact:* Modelled as an internal calculation with no Read. If a stored priority/SLA lookup is required: +1 R. CFP swing +1.

**CG-E02-03 · Measurement Gap** — Is the acknowledgement email's 'expected response time' a fixed value or read from a stored SLA/response-time table keyed by priority?

*Impact:* Modelled with no Read (value derived from priority in-process). If read from persistent SLA config: +1 R. CFP swing +1. Overlaps with CG-E02-02 if same lookup source.

---

## E03 — Check Rates Payment Status

**Epic CFP: 5 · Confidence: Assumed**

> Resident phones to ask the status of their rates (property tax) payments. After identity verification, the agent looks up the rate account by property number or address. The system retrieves the current balance, last payment date and amount, any arrears, and the next instalment due date from the finance system, and displays them to the agent who reads them back to the caller.

**Functional users:** Contact centre agent · Finance system

### FP1 — FP1-CheckRatesPaymentStatus — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Rate Account Identifier | Triggering Entry: the agent enters the property number or address to start the lookup. RULE 10/13 — one triggering Entry per functional process, all data describing the single object of interest entered once. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **X** | Rate Account Identifier | Exit half of the external round-trip: the process tells the finance system which account's data to send. Primer Rule 1 — request to another piece of software is an Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 3 | **E** | Rate Payment Status | Entry half of the external round-trip: balance, last payment date/amount, arrears and next instalment due date returned by the finance system. Primer Rule 1 — response from another piece of software is an Entry. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 4 | **X** | Rate Payment Status | Exit returning the retrieved data to the functional user (agent) to read back to the caller — the retrieve/read-out Exit of a query. Primer Rule 2 (retrieve pattern). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation messages from this process (e.g. account not found). Primer Rule 3. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E03)

**CG-E03-01 · Measurement Gap** — Is the finance system a separate piece of software (external round-trip: Exit request + Entry response) or persistent storage inside the measured boundary (single Read)? The epic says data is 'retrieved from the finance system' but does not fix the software boundary.

*Impact:* CFP swing of 1. Round-trip interpretation (taken here) = 5 CFP; persistent-storage/Read interpretation would replace movements 2+3 with a single Read, giving 4 CFP.

**CG-E03-02 · Measurement Gap** — Identity verification is referenced ('After identity verification') but the epic depends_on E10. Confirm verification movements are measured entirely under E10 and not double-counted here.

*Impact:* No CFP impact on E03 under the assumption that verification is a distinct functional process owned by E10 (different triggering event, primer Rule 4). If any verification data movement were in-scope for this process it would add CFP.

### Caveats & modeling choices (E03)

- Identity verification excluded from this measurement — scoped to E10 per depends_on.
- Finance-system retrieval measured as an external round-trip (Exit+Entry, primer Rule 1); if the finance system is inside the boundary it collapses to one Read (see CG-E03-01).
- One error/confirmation Exit included per primer Rule 3 though the epic does not explicitly describe failure handling; a lookup by property number/address can plausibly fail (not found).

---

## E04 — Set Up a Rates Payment Plan

**Epic CFP: 6 · Confidence: Assumed**

> A resident in arrears requests a payment plan for their outstanding rates. The agent captures the proposed instalment amount and frequency. The system validates the plan against council hardship policy limits, calculates the schedule, records the arrangement on the rate account, and issues a written confirmation of the payment plan to the resident by post or email.

**Functional users:** Council agent (customer service officer) · Resident (arrangement recipient)

### FP1 — FP1-SetUpPaymentPlan — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Payment Plan Proposal | Single triggering Entry that starts the process on the agent submitting the proposed plan; all data for one object of interest is one Entry (RULE 10/13). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Hardship Policy Limits | Read from persistent storage to validate the plan against council hardship policy (rule 2, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Rate Account | Read from persistent storage to obtain the arrears balance needed to calculate the instalment schedule (rule 2, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Payment Arrangement | Write of the calculated arrangement/schedule to persistent storage (rule 2, RULE 19). Schedule calculation itself is data manipulation, not counted. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Payment Plan Confirmation | Exit sending plan detail out of the boundary to the resident; carries data beyond a bare acknowledgement so counted as its own Exit. Post vs email is an implementation channel, still one data group (rule 3 carve-out for messages carrying additional data). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 6 | **X** | Agent Result Message | One Exit accounts for all confirmation/error outcomes to the agent (e.g. plan exceeds hardship limits, or plan accepted), regardless of count/variety (rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E04)

**CG-E04-01 · Measurement Gap** — The epic explicitly describes the written confirmation to the resident but is silent on whether an on-screen confirmation/validation-error message is returned to the agent. Movement 6 (Agent Result Message Exit) is assumed present.

*Impact:* CFP swing of -1 if no agent-facing message exists (process would be 5 CFP).

**CG-E04-02 · Measurement Gap** — Whether the rate account (outstanding balance) is read within this process or was already carried over from the arrears/account-selection context (dependency E03). Movement 3 assumes a Read here to support schedule calculation.

*Impact:* CFP swing of -1 if the balance is supplied by the triggering context rather than read (process would be 5 CFP; both gaps together 4 CFP).

### Caveats & modeling choices (E04)

- No source code exists at this proposal grain; movements inferred from the epic narrative treated as FUR.
- Schedule calculation is treated as data manipulation and not counted as a movement per COSMIC (only E/X/R/W count).
- Post vs email delivery of the resident confirmation is treated as one Exit / one data group (delivery channel is an implementation detail).

---

## E05 — Report a Pothole or Road Defect

**Epic CFP: 6 · Confidence: Assumed**

> Resident reports a pothole, damaged footpath, or road defect. The agent captures the location, defect type, and severity. The system checks for an existing duplicate defect at the same location within a radius; if a duplicate exists it links the caller to that case, otherwise it creates a new road-defect works order, assigns it to the Roads team, and sends the caller a tracking reference.

**Functional users:** Contact-centre agent (defect intake) · Roads-team work-management system (assignment target — see CG-E05-01)

### FP1 — FP1-ReportDefect — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Defect Report | Single triggering Entry that starts the process; one Entry counts for all data describing the single defect object of interest (RULE 10/13). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Road Defect Works Order | Read from persistent storage to check for an existing duplicate defect at the same location within a radius (CRUD-read component, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Caller Case Link | Duplicate-found response: Write attaching the caller to the existing case. Belongs to the same process because all possible responses to the triggering Entry are one functional process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L63-L71 |
| 4 | **W** | Road Defect Works Order | No-duplicate response: Write persisting the new works order (Roads-team assignment treated as an attribute of this Write — see CG-E05-01). Create = triggering Entry (order 1) + Write (RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Tracking Reference | Exit returning the case/works-order reference. This carries data beyond confirmation, so it is a separate Exit from the confirmation message. A single case-reference Exit is assumed to serve both branches (new order ref and existing case ref) — see CG-E05-02. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 6 | **X** | Confirmation/Error Message | One Exit accounts for all confirmation/error messages from all causes in the process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E05)

**CG-E05-01 · Measurement Gap** — Is 'assigns it to the Roads team' merely an attribute set on the works-order Write (order 4), or does it route/notify a separate downstream Roads work-management system (a distinct functional user), which would be an additional Exit?

*Impact:* Swing +1 CFP. Base count treats assignment as an attribute of the existing Write (+0). If a distinct Roads system is a functional user receiving the order, add 1 Exit (7 CFP).

**CG-E05-02 · Measurement Gap** — In the duplicate-found branch, is the existing-case reference returned to the caller via the SAME 'case reference' Exit as the new-order tracking reference (same data group), or a distinct Exit?

*Impact:* Swing +1 CFP. Base assumes one shared 'Tracking Reference' Exit for both branches. If the existing-case reference is a distinct data group/Exit, add 1 Exit (7 CFP).

**CG-E05-03 · Measurement Gap** — Does resolving the location to coordinates for the 'within a radius' duplicate search require a request/response round-trip to an external geocoding/geospatial service (Exit request + Entry response), or is it done in-process against persistent data?

*Impact:* Swing +2 CFP. Base assumes in-process / persistent-storage handling (+0). An external round-trip adds 1 Exit + 1 Entry per primer rule 1 (8 CFP).

### Caveats & modeling choices (E05)

- Single functional process assumed: the agent's submission is one triggering event; both the duplicate-link and new-order paths are alternative responses to it and are counted in one process (primer rule 4).
- Functional user assumed to be the contact-centre agent operating the system; the resident/caller is served via the agent, not modelled as a separate functional user.
- 'Existing road defects' read and the new 'works order' write are treated as the same object of interest (one data group).
- Confidence is Assumed due to CG-E05-01/02/03; base count is 6 CFP with a possible range of 6-9 CFP depending on adjudication.

---

## E06 — Book a Hard Rubbish Collection

**Epic CFP: 8 · Confidence: Assumed**

> Resident books a hard/bulky waste collection. The agent captures the address, item types and counts, and preferred collection window. The system checks the resident's remaining free collections for the year, validates that the items are within accepted categories, allocates the next available collection date from the waste scheduling service, and confirms the booking by SMS.

**Functional users:** Resident/Agent (booking initiator) · Waste Scheduling Service (external date allocator) · SMS Gateway (external notifier)

### FP1 — FP1-BookHardRubbishCollection — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Collection Booking | Triggering Entry: all data describing the single booking object entered once (RULE 13 single triggering Entry). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Free Collection Quota | Read from persistent storage to check the resident's remaining free collections (RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Accepted Item Categories | Read reference data to validate that submitted items fall within accepted categories (RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Collection Date Allocation | Exit half of the external round-trip: request sent to the waste scheduling service (Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 5 | **E** | Collection Date Allocation | Entry half of the external round-trip: allocated date returned by the scheduling service (Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 6 | **W** | Collection Booking | Write the finalised booking (with allocated date) to persistent storage (RULE 19). Same object of interest as the Entry, so one data group. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | SMS Booking Confirmation | Exit carrying booking data (date, items) to the resident via SMS gateway — data beyond mere acceptance, so a separate Exit counted normally (Rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 8 | **X** | Booking Result Message | Single Exit accounting for all confirmation/error outcomes to the agent (quota exhausted, invalid items, success) (Rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E06)

**CG-E06-01 · Measurement Gap** — The epic states remaining free collections are checked but does not say whether the quota is decremented/written back after a successful booking. If the system updates the resident's free-collection count, an additional Write is required.

*Impact:* CFP swing +1 (one Write to Free Collection Quota) if the quota is persisted on booking.

**CG-E06-02 · Measurement Gap** — Assumed both an outbound SMS confirmation (data-bearing, to resident) and a separate on-screen result/error message to the agent exist. If the on-screen result is not a distinct data group (e.g. no agent-facing UI, SMS is the only response), the agent Exit would not apply.

*Impact:* CFP swing -1 if the agent-facing Booking Result Message Exit does not exist as a distinct movement.

**CG-E06-03 · Measurement Gap** — Reads for 'remaining free collections' and 'accepted item categories' are assumed to hit two distinct persistent object types. If accepted categories are static/hard-coded rather than persistent reference data, that Read would not apply.

*Impact:* CFP swing -1 if Accepted Item Categories is not a read persistent data group.

---

## E07 — Lodge a Noise or Nuisance Complaint

**Epic CFP: 5 · Confidence: Assumed**

> Resident lodges a complaint about noise, illegal dumping, or another nuisance. The agent records the nature of the complaint, the offending address, dates/times of occurrence, and whether the complainant wishes to remain anonymous. A regulatory case is created and routed to the Local Laws / Environmental Health team, and the complainant receives a case reference (unless anonymous).

**Functional users:** Council agent / complainant (resident) · Local Laws / Environmental Health team system

### FP1 — FP1-LodgeNuisanceComplaint — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Nuisance Complaint | Single triggering Entry starting the process; all data describing the one complaint (nature, address, dates/times, anonymity) counted once (RULE 13). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **W** | Regulatory Case | Create pattern: new object of interest written to persistent storage (RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Regulatory Case | Exit sending case data to another piece of software / functional user; no prompting request needed so a single Exit suffices. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 4 | **X** | Case Reference | Data-carrying Exit to the complainant/agent; distinct from a plain confirmation because it carries the reference identifier. Counted once even though suppressed for anonymous complainants (process covers all possible responses). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 5 | **X** | Confirmation/Error Message | One Exit accounts for all confirmation and error messages from every cause in this process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E07)

**CG-E07-01 · Measurement Gap** — The epic does not state whether the offending address is validated against a property/address register or whether an existing/duplicate case is looked up before creation. Either would introduce a Read from persistent storage.

*Impact:* CFP swing +1 (a Read for address/duplicate lookup) to +2 if both a register Read and a duplicate-case Read are required. Measured value assumes no such Read.

**CG-E07-02 · Measurement Gap** — Whether routing to the Local Laws / Environmental Health team expects a synchronous acknowledgement/case-accepted response back into this process (round-trip) versus a fire-and-forget handoff.

*Impact:* CFP swing +1 if the team system returns a response Entry into the same process (Exit+Entry round-trip per primer rule 1). Measured value assumes a single Exit handoff.

### Caveats & modeling choices (E07)

- Modeled as a single functional process because all movements respond to one triggering event (the agent lodging the complaint).
- Case reference Exit is counted once even though it is not sent for anonymous complainants, since a functional process comprises all data movements needed for all possible responses.
- No Read is counted because the epic describes only capture-and-create with no stated lookup/validation against persistent data.

---

## E08 — Apply for a Parking Permit

**Epic CFP: 10 · Confidence: Assumed**

> Resident applies for a residential parking permit. The agent captures vehicle registration, residential address, and permit type. The system verifies residency against the property register, checks the number of permits already issued to that address against the allowance, calculates any fee, takes payment, and issues a digital permit plus a confirmation email.

**Functional users:** Parking permit agent (acting for the resident/applicant) · Property register (residency source of truth) · Payment service · Email/notification service

### FP1 — FP1-ApplyForParkingPermit — 10 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Permit Application | Single triggering Entry; RULE 13 counts one Entry for all data (vehicle reg, address, permit type) describing the application object. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Property Register Record | Read from persistent storage to verify residency (primer rule 2, retrieve = Read). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Issued Permit | Read existing permits at the address to count them against the allowance (primer rule 2, Read of persistent object). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **R** | Permit Policy | Read reference data for the permit type providing the allowance limit and fee rate; fee is then calculated (calculation is manipulation, not a movement). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Payment | Exit half of external-system round-trip to the payment service (primer rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 6 | **E** | Payment | Entry half of the external round-trip; payment result returned by the payment service stays in this process (primer rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 7 | **W** | Parking Permit | Create/Write the new digital permit to persistent storage (primer rule 2, create = Write). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 8 | **X** | Parking Permit | Exit delivering the issued digital permit back to the resident/agent. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 9 | **X** | Permit Confirmation Email | Separate Exit: carries permit data beyond mere acceptance, so it is counted independently of the generic confirmation message (primer rule 3, last sentence). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 10 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation outcomes (failed residency, over-allowance, payment failure, success) regardless of count (primer rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E08)

**CG-E08-01 · Measurement Gap** — Is the property register accessed as this system's own persistent storage (1 Read) or is it a separate piece of software (e.g. epic E10/E11) requiring an external-system round-trip (Exit request + Entry response)? The epic lists depends_on E10/E11 without clarifying which is the register.

*Impact:* CFP swing +1: modeled as a single Read (1 CFP). If external round-trip, it becomes Exit+Entry (2 CFP), raising the process to 11 CFP.

**CG-E08-02 · Measurement Gap** — Are the permit-type allowance limit and the fee rate a single reference object (modeled here as one 'Permit Policy' Read), two separate persistent reads, or non-persisted configuration constants (no Read)?

*Impact:* CFP swing -1 to +1: modeled as one Read. Two separate reads = +1 (11 CFP); pure config/constants = -1 (9 CFP).

**CG-E08-03 · Measurement Gap** — Is payment a sub-interaction within this functional process (one triggering event = the application, as modeled: Exit request + Entry result), or a distinct functional process with its own resident-triggered event (e.g. the resident separately entering card details)? The latter would also add a separate triggering Entry for card data.

*Impact:* If payment is a separate FP, the two payment movements move to that process and an additional triggering Entry (+1 CFP) plus its own error/confirmation Exit may apply. Boundary/trigger clarification needed against E10/E11.

**CG-E08-04 · Measurement Gap** — Are 'issue a digital permit' (delivery Exit) and the 'confirmation email' (email Exit) truly two distinct data-bearing Exits, or is the digital permit delivered inside the confirmation email as one Exit?

*Impact:* CFP swing -1: modeled as two Exits. If the permit is delivered solely via the email, one Exit is removed (9 CFP).

### Caveats & modeling choices (E08)

- No source code or manuals were re-read; decomposition applies the supplied primer rules and their citations directly, per instructions.
- Modeled as a single functional process because the epic describes one triggering event (application submission); primer rule 4/5.
- Fee calculation itself is data manipulation and not counted as a data movement.
- Functional users and the external/internal nature of the property register and payment service are inferred from the epic description and its depends_on (E10, E11); see gaps CG-E08-01 and CG-E08-03.

---

## E09 — Update Contact Details on Account

**Epic CFP: 4 · Confidence: Assumed**

> Resident calls to update their contact details (phone, email, postal address) held against their council customer account. After identity verification the agent edits the record; the system validates the new details, saves them to the customer master, and confirms the change to the resident.

**Functional users:** Customer Service Agent (acting on the calling resident's behalf)

### FP1 — FP1-UpdateContactDetails — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Customer Contact Details | RULE 2 (Update): triggering Entry carrying the new contact-detail values from the agent. RULE 13 — single Entry for all data describing the one object of interest. Validation of the entered details is data manipulation associated with this Entry, not a separate movement. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 2 | **R** | Customer Contact Details | RULE 2 (Update) / RULE 18 — Read the existing persisted customer contact details before applying the change. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Customer Contact Details | RULE 2 (Update) / RULE 19 — Write the validated, modified contact details to the customer master persistent store. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Change Confirmation | RULE 3 — one Exit accounts for all confirmation and validation-error messages issued by the process; the confirmation carries no data beyond acceptance/error status. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E09)

**CG-E09-01 · Measurement Gap** — The description says the update happens 'after identity verification' and E09 depends_on E10. It is unclear whether the customer lookup/identity-verification and the retrieval/display of the existing record for editing are scoped to E09 or entirely to E10. This measurement assumes they belong to E10 and are NOT counted here.

*Impact:* If a distinct 'Retrieve/verify customer record' functional process (Entry + Read + Exit) is actually in E09's scope, add ~+3 CFP (one additional functional process). Swing: +0 to +3 CFP.

**CG-E09-02 · Measurement Gap** — 'The system validates the new details' — it is unspecified whether validation (e.g. postal-address checking) calls an external address-lookup/validation service, which under RULE 1 would be an Exit (request) + Entry (response) round-trip, or reads persistent reference data (an extra Read). Treated here as in-process data manipulation with no additional movement.

*Impact:* If an external validation round-trip exists, +2 CFP (1 Exit + 1 Entry); if it reads persisted reference data, +1 CFP (1 Read). Swing: +0 to +2 CFP.

### Caveats & modeling choices (E09)

- Functional user taken to be the Customer Service Agent; the resident is the caller but does not interact with the software directly, so the confirmation Exit is delivered to the agent.
- Identity verification and existing-record retrieval assumed to be covered by the E10 dependency and excluded from this count (see CG-E09-01).
- Validation of new details treated as data manipulation associated with the triggering Entry, not a separate movement (see CG-E09-02).
- Confidence is Assumed because the E09/E10 scope boundary and validation mechanism required defensible assumptions.

---

## E10 — Verify Caller Identity

**Epic CFP: 4 · Confidence: Assumed**

> A shared capability used at the start of many calls. The agent asks knowledge-based verification questions (name, property address, date of birth, or an account reference). The system checks the supplied answers against the customer master and returns a verified/failed result to the agent, logging the verification attempt against the customer record.

**Functional users:** Call-centre agent · Customer master (persistent store as object of interest)

### FP1 — FP1-VerifyCallerIdentity — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Verification Answers | Single triggering Entry: agent submits the caller's KBV answers, starting the process (RULE 10/13). One Entry covers all answer attributes describing the single object of interest. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Customer Master Record | Read from persistent storage of the stored identity attributes to check the supplied answers (retrieve leg of the CRUD read pattern, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Verification Attempt Log | Write to persistent storage recording the verification attempt against the customer record (RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Verification Result | Exit carrying the substantive verified/failed outcome to the agent. This is result data beyond a bare confirmation, so it is a normal Exit; any error messaging is subsumed by this single Exit (primer rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E10)

**CG-E10-01 · Measurement Gap** — The epic says the agent asks the KBV questions but does not state whether the system generates/presents those questions to the agent. If the system retrieves the expected question set or prompts the agent, this adds movements (potentially a Read of the question/answer set plus an Exit presenting the prompt, ~+2 CFP), or could constitute a separate 'present verification questions' functional process.

*Impact:* CFP swing: +0 (agent formulates questions manually, system only checks answers) to +2 CFP within this process, or a separate process if the system drives the questioning.

**CG-E10-02 · Measurement Gap** — Unclear whether the verified/failed result and any distinct error/exception feedback are one data group or whether additional data (e.g. remaining-attempt count, lockout status) is returned. Per primer rule 3 a single Exit covers all confirmation/error messages, but extra data groups returned to the agent would each be a separate Exit.

*Impact:* CFP swing: +0 to +1 CFP if a distinct additional data group (beyond the pass/fail result) is returned to the agent.

---

## E11 — Look Up Council Asset by Location

**Epic CFP: 5 · Confidence: Assumed**

> A shared capability that, given an address or map pin, queries the GIS/asset service to determine whether an asset (tree, road, drain, streetlight) is council-owned and returns its asset details and responsible team to the agent or calling process.

**Functional users:** Agent or calling process (lookup requester) · GIS/asset service (external system)

### FP1 — FP1-LookUpAssetByLocation — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Asset Location Query | Single triggering Entry: the caller submits an address or map pin, starting the process on detection of the lookup event (RULE 10/13). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **X** | Asset Location Query | External-system round-trip half 1: the process must tell the GIS/asset service which location to resolve, so an Exit (the request) is required. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 3 | **E** | Asset Ownership Details | External-system round-trip half 2: the Entry carrying the GIS response (ownership, details, responsible team). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 4 | **X** | Asset Ownership Details | Data Exit delivering substantive result data (asset details, ownership, responsible team) back to the requesting agent/process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |
| 5 | **X** | Lookup Status Message | One Exit accounts for all error/confirmation messages (no asset found, asset not council-owned). Distinct from movement 4 because that Exit carries substantive result data. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E11)

**CG-E11-01 · Measurement Gap** — Is the GIS/asset service a separate piece of software (external system) reached via a request/response round-trip, or is it this application's own persistent storage? The description says the process 'queries the GIS/asset service', which was assumed to be external software.

*Impact:* If external (assumed): Exit query + Entry response = 2 movements (5 CFP total). If it is the app's own persistent storage: a single Read replaces those two movements (4 CFP total). Swing: -1 CFP.

**CG-E11-02 · Measurement Gap** — Is the 'responsible team' returned directly by the GIS/asset service, or resolved by a separate lookup (e.g., a local Read of an asset-type-to-team mapping)?

*Impact:* Assumed the GIS response includes the responsible team (no extra movement). If it requires a separate local persistent-storage lookup, add 1 Read: +1 CFP.

---

## E12 — Cancel a Hard Rubbish Collection Booking

**Epic CFP: 8 · Confidence: Assumed**

> A resident phones to cancel a previously booked hard/bulky waste collection. After the caller's identity is verified, the agent looks up the existing booking by address or booking reference, confirms the collection window and item details with the caller, and cancels it. The system marks the booking cancelled, restores the resident's free-collection allowance for the year, and sends the caller an SMS confirming the cancellation. If the collection window has already passed or the booking cannot be found, the agent is shown an error message.

**Functional users:** Call centre agent · SMS gateway (external messaging system)

### FP1 — FP1-CancelBooking — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Booking | Triggering Entry: agent enters the lookup key (address or booking reference) identifying the booking to cancel. RULE 10/13 — exactly one triggering Entry, one Entry per object of interest. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Booking | Read from persistent storage to retrieve the booking (window, item details, status) — RULE 18; part of the update/delete CRUD pattern. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Booking | Exit of the retrieved collection window and item details so the agent can confirm them with the caller (retrieve pattern: Entry + Read + Exit). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Booking | Write to persistent storage setting the booking status to cancelled — RULE 19 (a state change/deletion is a single Write). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **R** | Resident Allowance | Read the resident's current free-collection allowance for the year before crediting it back (update pattern Read existing). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 6 | **W** | Resident Allowance | Write the incremented allowance back to storage — RULE 19; distinct object of interest from Booking. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | Cancellation SMS | Single Exit to the external SMS gateway; no request/response round-trip is needed to prompt the send, so one Exit suffices. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259 |
| 8 | **X** | Result Message | One Exit accounts for all confirmation and error messages (booking not found, collection window passed, success) from this process, regardless of count or cause. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272 |

### Measurement gaps (E12)

**CG-E12-01 · Measurement Gap** — How is the free-collection allowance restored? Measured as a stored yearly counter updated in place (Read + Write = 2 movements). If it is a single decrement/credit Write with no prior read it is 1 movement; if the allowance is derived on the fly from non-cancelled bookings it is 0 movements.

*Impact:* CFP swing of -2 to 0 on this process (8 -> 6..8).

**CG-E12-02 · Measurement Gap** — Identity verification ('after the caller's identity is verified') is assumed to be a separate functional process delivered by dependency epic E06 and is therefore NOT counted here. If verification movements (e.g. Entry of identifiers + Read + Exit of verification result) are in scope of E12, they add roughly +3 CFP.

*Impact:* CFP swing of 0 to +3 if verification is folded into this epic.

**CG-E12-03 · Measurement Gap** — The booking lookup/display step is included here as part of the cancel process (Entry key + Read + Exit of details). If the lookup is instead the separate process delivered by dependency epic E10 and the cancel is triggered by a distinct 'confirm cancel' command on an already-displayed booking, the Read/Exit-of-details may belong to E10 and this process would drop the display Exit (-1) or add a second command Entry.

*Impact:* CFP swing of about -1 to +1 depending on process-boundary decision with E10.

### Caveats & modeling choices (E12)

- Modelled as a single functional process triggered by the resident's cancellation request; lookup, confirmation, cancellation, allowance restore, and notifications all flow from that one triggering event (primer rules 4 and 5).
- Identity verification treated as out of scope (delegated to dependency E06) - see CG-E12-02.
- Allowance restoration assumed to be a stored counter update (Read + Write) - see CG-E12-01.
- Success confirmation and both error cases (not found / window passed) to the agent are consolidated into one Exit per primer rule 3; the SMS to the caller is a separate functional-user Exit.

---

## COSMIC v5.0 Movement-Pattern Primer (Salesforce delivery scope)

---
name: cosmic-rules-primer
description: >
  Distilled, scope-independent COSMIC v5.0 rules primer covering the movement
  patterns that recur across a delivery scope. Derived from the coach's indexed
  manuals; every rule cites manuals-indexed/<slug>/<file>.md#L<start>-L<end>.
derivedFrom:
  manuals:
    - part-1-mm-principles-definitions-rules-v5-0-aug-2021
    - part-2-mm-guidelines-v5-0-sep-2024
    - part-3c-mis-examples-v5-0-sep-2024
  cosmicVersion: v5.0
  indexDate: 2026-06-17
  regeneratedOn: 2026-07-30
---

# COSMIC v5.0 Rules Primer

Compact reusable reference for the recurring movement patterns. Cite these
directly; grep the manuals only for adjudications NOT covered here. 1 data
movement = 1 CFP.

## 1. External-system round-trip (request → response)

When a functional process needs to tell another party what data to send, an
**Exit** (the request) followed by an **Entry** (the response) are necessary —
so a round-trip to another piece of software is **2 movements** (1 Exit + 1
Entry). When no request is needed to prompt the data, a single Entry suffices.
Both movements belong to the same functional process (all responses to the
triggering Entry stay in one process).
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L255-L259`

## 2. CRUD on a persistent object of interest

From a user-triggered functional process (RULE 18 = Read from persistent
storage, RULE 19 = Write to persistent storage, RULE 20 = a delete is a single
Write):

- **Create**: Entry (new data) + Write.
- **Read/retrieve**: Entry (trigger) + Read + Exit (data back to the user).
- **Update**: Entry (changes) + Read (existing) + Write (modified).
- **Delete**: Entry (trigger) + Write (the deletion).

`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149`
`manuals-indexed/part-3c-mis-examples-v5-0-sep-2024/02-help-functionality.md#L33-L36`

## 3. Confirmation and error messages

**One Exit** accounts for ALL types of error/confirmation messages issued by any
one functional process, from all possible causes — regardless of message count
or variety. If a message carries data beyond confirming acceptance/error, that
additional data group is a separate Exit counted in the normal way.
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L272`

## 4. Distinct functional processes vs. one

Two functional processes are distinct when they respond to **different
triggering events** (each detected by a functional user). A functional process
is the set of all data movements needed to meet its FUR for all possible
responses to its triggering Entry — so work that all flows from one triggering
event is one process, not several.
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L63-L71`
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L26`

## 5. The single triggering Entry rule

Any one functional process has **exactly one triggering Entry** — the Entry from
a functional user that starts the process on detecting a triggering event (RULE
10). RULE 13: a single Entry is counted for entry of all data describing a
single object of interest, unless the FUR explicitly require the same object to
be entered more than once. All subsequent movements (further Entries, Exits,
Reads, Writes) responding to that triggering Entry belong to the same process.
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26`
`manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99`
`manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L243-L243`
