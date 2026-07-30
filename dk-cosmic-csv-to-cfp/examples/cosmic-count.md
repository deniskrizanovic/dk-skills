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
| E01 | Log a Lost Pet Report | **8** | Assumed | 1 | 4 |
| E02 | Request Tree Lopping or Removal | **7** | Assumed | 1 | 3 |
| E03 | Check Rates Payment Status | **5** | Assumed | 1 | 1 |
| E04 | Set Up a Rates Payment Plan | **6** | Assumed | 1 | 4 |
| E05 | Report a Pothole or Road Defect | **6** | Assumed | 1 | 3 |
| E06 | Book a Hard Rubbish Collection | **8** | Assumed | 1 | 3 |
| E07 | Lodge a Noise or Nuisance Complaint | **4** | Assumed | 1 | 2 |
| E08 | Apply for a Parking Permit | **10** | Assumed | 1 | 5 |
| E09 | Update Contact Details on Account | **4** | Assumed | 1 | 2 |
| E10 | Verify Caller Identity | **4** | Assumed | 1 | 2 |
| E11 | Look Up Council Asset by Location | **5** | Assumed | 1 | 2 |
| E12 | Cancel a Hard Rubbish Collection Booking | **8** | Assumed | 1 | 4 |
| | **Total** | **75** | | | 35 |

---

## Data groups

| Data group | Functional processes | Description |
|---|---|---|
| Asset Details | E11/FP1-LookupAssetByLocation | Ownership status (council-owned or not), asset attributes (type such as tree/road/drain/streetlight and identifier), and the responsible team, as resolved by the GIS/asset service. |
| Booking | E12/FP1-CancelBooking | The persistent hard/bulky-waste collection booking record: collection window, item details, resident/address, and cancellation status. |
| Booking Confirmation | E06/FP1-BookHardRubbishCollection | The SMS message sent to the resident carrying the confirmed collection date and booking reference. |
| Booking Request | E06/FP1-BookHardRubbishCollection | Resident/agent-supplied collection address, item types with counts, and the preferred collection window that initiate the booking. |
| Booking Result Message | E06/FP1-BookHardRubbishCollection | On-screen confirmation/error feedback to the agent covering all outcomes (e.g. no free collections remaining, unaccepted items, success). |
| Booking Search Criteria | E12/FP1-CancelBooking | The lookup key the agent supplies to locate the booking: either the service address or the booking reference number. |
| Caller-Case Link | E05/FP1-ReportRoadDefect | Association record joining the reporting caller to an existing duplicate works order/case so the caller is tracked against it. |
| Caller-Supplied Identity Answers | E10/FP1-VerifyCallerIdentity | The knowledge-based verification answers the agent enters on behalf of the caller — e.g. name, property address, date of birth, or account reference. |
| Cancellation SMS | E12/FP1-CancelBooking | The outbound short-message payload confirming to the caller that their collection booking has been cancelled. |
| Case Reference | E07/FP1-LodgeComplaint | The case reference identifier issued to the complainant so they can track the lodged complaint (suppressed when the complainant is anonymous). |
| Case Tracking Reference | E05/FP1-ReportRoadDefect | The case/works-order reference number returned so the caller can track progress (new reference when created, existing reference when linked). |
| Collection Allowance | E06/FP1-BookHardRubbishCollection, E12/FP1-CancelBooking | The resident's free hard-rubbish collection quota and how many have already been used in the current year. / The resident's persistent annual free hard-rubbish collection quota/usage counter for the year. |
| Collection Date Allocation | E06/FP1-BookHardRubbishCollection | The date-allocation exchange with the waste scheduling service: outbound availability query and the returned next-available collection date. |
| Complaint Case | E07/FP1-LodgeComplaint | The nuisance/regulatory case record: nature of complaint (noise, illegal dumping, other), offending address, dates/times of occurrence, anonymity preference, and assigned Local Laws / Environmental Health team. |
| Confirmation Message | E07/FP1-LodgeComplaint, E08/FP1-ApplyForParkingPermit, E09/FP1-UpdateContactDetails | The single confirmation/error message returned to the agent acknowledging the complaint was accepted and the case created (or reporting a failure). / Acceptance confirmation plus all error/rejection notices (failed residency, allowance exceeded, payment declined) surfaced to the agent/resident. / System response to the agent/resident confirming the contact-detail change was saved, and covering all validation-error/failure notifications for this process. |
| Confirmation/Error Message | E02/FP1-SubmitTreeLoppingRequest, E04/FP1-SetUpPaymentPlan, E05/FP1-ReportRoadDefect, E12/FP1-CancelBooking | The single message stream back to the submitting agent covering all success/validation-failure/error outcomes of the submission. / Acceptance confirmation or validation/error notification returned to the agent for all outcomes of the process. / Consolidated acceptance/validation/error feedback issued to the agent for all possible outcomes of the report submission. / The single on-screen message stream to the agent conveying success confirmation or any error (collection window already passed, booking not found). |
| Confirmation/error message | E01/FP1-LogLostPetReport | On-screen acknowledgment or error surfaced to the agent for the logging action. |
| Contact Details | E09/FP1-UpdateContactDetails | The resident's contact information held on the council customer account — phone, email and postal address — as the object of interest being edited and persisted to the customer master. |
| Crew Notification | E02/FP1-SubmitTreeLoppingRequest | Work assignment dispatched to the Parks & Gardens crew, carrying the request details and priority so they can action the job. |
| Customer Master Record | E10/FP1-VerifyCallerIdentity | Stored customer identity attributes retrieved to validate the supplied answers. |
| Defect Report | E05/FP1-ReportRoadDefect | Inbound report attributes captured by the agent: geographic location, defect type (pothole / damaged footpath / road defect), and severity. |
| Error/Confirmation Message | E03/FP1-CheckRatesPaymentStatus, E11/FP1-LookupAssetByLocation | The process outcome indication to the agent covering all error/confirmation causes, e.g. account not found or finance-system unavailable. / Status feedback returned to the requester covering all error and no-asset-found/confirmation outcomes of the lookup. |
| Fee Schedule | E08/FP1-ApplyForParkingPermit | Persistent tariff of permit fee rates by permit type used to calculate the amount payable. |
| Found-pet record | E01/FP1-LogLostPetReport | Records of pets reported found, matched against the lost-pet report. |
| GIS Boundary Validation | E02/FP1-SubmitTreeLoppingRequest | Round-trip to the asset/GIS boundary service: the location key sent out and the council-land ownership determination returned. |
| Hard Rubbish Booking | E06/FP1-BookHardRubbishCollection | The persisted booking record capturing address, validated items, allocated date, and status. |
| Hardship Policy Limits | E04/FP1-SetUpPaymentPlan | Council hardship policy parameters (e.g. min/max instalment, allowed frequencies, maximum plan duration) the proposed plan is validated against. |
| Item Category Rules | E06/FP1-BookHardRubbishCollection | Reference list of item categories the council accepts for hard-rubbish collection, used to validate the requested items. |
| Location Query | E11/FP1-LookupAssetByLocation | The address or map pin supplied by the requester identifying the location whose council-asset status is to be determined. |
| Lost-pet case | E01/FP1-LogLostPetReport | The reported case: caller name/contact number, pet species/breed/description, last-seen location and date, plus the generated case reference and status. |
| Microchip record | E01/FP1-LogLostPetReport | Registered-pet microchip records held in the animal registry, matched against the reported pet. |
| Parking Permit | E08/FP1-ApplyForParkingPermit | The residential parking permit object of interest: existing permits already issued to the address (read for the allowance check) and the newly issued digital permit that is persisted and delivered. |
| Payment | E08/FP1-ApplyForParkingPermit | The payment request/authorisation data exchanged with the external payment gateway. |
| Payment Plan Arrangement | E04/FP1-SetUpPaymentPlan | The accepted payment arrangement (calculated schedule of instalments and dates) recorded against the rate account. |
| Payment Plan Confirmation | E04/FP1-SetUpPaymentPlan | The written confirmation document detailing the agreed instalment schedule, dispatched to the resident by post or email. |
| Payment Plan Request | E04/FP1-SetUpPaymentPlan | Proposed instalment amount, payment frequency, and the target rate-account reference captured by the agent from the resident. |
| Permit Allowance | E08/FP1-ApplyForParkingPermit | The maximum number of permits allowed for a given address or zone, compared against permits already issued. |
| Permit Application | E08/FP1-ApplyForParkingPermit | The application data captured by the agent: vehicle registration, residential address, and permit type. |
| Property Register | E08/FP1-ApplyForParkingPermit | Persistent register of properties/addresses used to confirm the applicant resides at the stated address. |
| Rate Account | E04/FP1-SetUpPaymentPlan | The resident's rates account holding the outstanding-arrears balance needed to compute the instalment schedule. |
| Rate Account Lookup Query | E03/FP1-CheckRatesPaymentStatus | The account identifier the agent supplies to locate the rate account — either the property number or the property address. |
| Rate Account Payment Status | E03/FP1-CheckRatesPaymentStatus | The payment position returned for the account: current balance, last payment date and amount, any arrears, and the next instalment due date. |
| Resident Acknowledgement | E02/FP1-SubmitTreeLoppingRequest | Acknowledgement email to the resident conveying request receipt plus the expected response time (data beyond a bare confirmation). |
| Road-Defect Works Order | E05/FP1-ReportRoadDefect | Persistent works-order record for a road defect, including location, defect type/severity, and the owning team; read for duplicate detection and written on creation. |
| SMS confirmation | E01/FP1-LogLostPetReport | Outbound SMS to the caller carrying the case reference as confirmation of the logged report. |
| Tree Works Request | E02/FP1-SubmitTreeLoppingRequest | The lodged request: tree location (address or map pin), reason/hazard description, and derived priority; the object of interest created and stored by the process. |
| Verification Attempt Log | E10/FP1-VerifyCallerIdentity | Audit record of a single verification attempt (outcome, timestamp) recorded against the customer record. |
| Verification Result | E10/FP1-VerifyCallerIdentity | The verified / failed outcome returned to the agent so the call can proceed. |

---

## E01 — Log a Lost Pet Report

**Epic CFP: 8 · Confidence: Assumed**

**Functional users:** Contact centre agent (human, via UI) · Caller/resident (recipient of SMS, across boundary) · SMS gateway (peer software)

### FP1 — FP1-LogLostPetReport — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Lost-pet case | Single triggering Entry: agent submits all data describing the lost-pet case (caller, pet, location/date, contact). One Entry per object of interest (RULE 13/17). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L104 |
| 2 | **R** | Microchip record | System checks animal registry for matching microchip records. A Read retrieves a single data group; microchip records are a distinct object of interest (RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L143 |
| 3 | **R** | Found-pet record | System checks for matching found-pet records. Distinct object of interest from microchip records, so a separate Read (single data group per Read, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L143 |
| 4 | **X** | Microchip record | Potential microchip matches displayed to the agent. Exit sends a single data group across the boundary (RULE 21). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L130 |
| 5 | **X** | Found-pet record | Potential found-pet matches displayed to the agent. Distinct object of interest, so a separate Exit consistent with the two Reads. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L130 |
| 6 | **W** | Lost-pet case | Case persisted to storage; queue routing is taken as owner assignment on the same case object, so one Write per object of interest (RULE 19). See gap CG-E01-04. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L143 |
| 7 | **X** | SMS confirmation | Confirmation SMS carries the case reference (data beyond acceptance confirmation), so it is a separate Exit data group. No documented delivery-receipt response, so no return Entry (see gap CG-E01-03). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 8 | **X** | Confirmation/error message | One Exit accounts for all confirmation/error messages the process issues to the agent, from all causes (primer #3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E01)

**CG-E01-01 · Measurement Gap** — The registry check is counted as two objects of interest (microchip records and found-pet records) yielding 2 Reads + 2 Exits. If the system treats 'registry matches' as a single combined result set (one object of interest), it collapses to 1 Read + 1 Exit.

*Impact:* Swing -2 CFP (8 -> 6).

**CG-E01-02 · Measurement Gap** — Counted as ONE functional process (single triggering event: agent logs report; registry check, case creation, SMS and routing are all responses). If the UI has the agent run the registry search as a separate agent-initiated event before creating the case, it splits into two functional processes with different triggering events (primer #4).

*Impact:* Structural: two processes (e.g. search process E+R+R+X+X+X plus create process E+W+X+X) rather than one; total CFP shifts (~10 vs 8) and the mandatory second triggering Entry/confirmation Exit are added.

**CG-E01-03 · Measurement Gap** — SMS confirmation counted as a single Exit. If sending goes to an SMS gateway (peer software) and the FUR require a synchronous delivery/acknowledgment response, it becomes an Exit+Entry round-trip (primer #1).

*Impact:* Swing +1 CFP (return Entry from the SMS gateway).

**CG-E01-04 · Measurement Gap** — Routing to the Animal Management queue is folded into the case Write as an owner-assignment attribute (same object of interest). If the queue is a distinct persistent object of interest that receives its own write, a separate Write is required.

*Impact:* Swing +1 CFP (additional Write for the queue object).

---

## E02 — Request Tree Lopping or Removal

**Epic CFP: 7 · Confidence: Assumed**

**Functional users:** Council agent (human, via UI) · Asset/GIS boundary service (peer software) · Parks & Gardens crew (recipient functional user) · Resident (email recipient functional user)

### FP1 — FP1-SubmitTreeLoppingRequest — 7 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Tree Works Request | Single triggering Entry: agent (functional user) submits the captured location + reason. All response movements belong to this one process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **X** | GIS Boundary Validation | External round-trip Exit: the asset/GIS boundary service is another piece of software (functional user across the boundary), so the request leaving is an Exit, not a Read. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 3 | **E** | GIS Boundary Validation | External round-trip Entry: the validation response from the GIS service crosses the boundary as an Entry (paired with the Exit above). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 4 | **W** | Tree Works Request | Create on the object of interest = Entry (already counted) + Write. Priority assignment is internal data manipulation, not a separate movement. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Crew Notification | Exit to another functional user (the crew) across the boundary; carries request data, distinct from the agent confirmation Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L207-L213 |
| 6 | **X** | Resident Acknowledgement | Separate Exit: the message provides data (expected response time) beyond mere confirmation, and goes to a different functional user (the resident). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 7 | **X** | Confirmation/Error Message | One Exit accounts for all error/confirmation messages (e.g., success, or 'tree not on council land') returned to the submitting agent from all causes. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E02)

**CG-E02-01 · Measurement Gap** — Photos 'if emailed in' — are they a separate object of interest entered as their own data group (an additional Entry), or attributes/attachments of the Tree Works Request captured in the single submission Entry? Counted here as part of the request Entry.

*Impact:* Swing +1 CFP if photos are a distinct Entry data group.

**CG-E02-02 · Measurement Gap** — Is the 'asset/GIS boundary service' a peer software across the boundary (Exit + Entry round-trip, 2 CFP as counted), or an in-boundary persistently-stored GIS layer that would instead be a single Read (1 CFP)?

*Impact:* Swing -1 CFP if it is a local persistent Read rather than an external round-trip.

**CG-E02-03 · Measurement Gap** — Does the process return an explicit confirmation/error message to the submitting agent (assumed here per the one-Exit error rule), or is submission feedback surfaced only implicitly by the Write/OS with no dedicated Exit?

*Impact:* Swing -1 CFP if no agent-facing confirmation/error Exit exists.

---

## E03 — Check Rates Payment Status

**Epic CFP: 5 · Confidence: Assumed**

**Functional users:** Contact-centre agent (human user via UI) · Finance system (separate software)

### FP1 — FP1-CheckRatesPaymentStatus — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Rate Account Lookup Query | Single triggering Entry from the agent (human functional user) detecting the event 'check rates payment status'; carries property number or address. All responses to this trigger belong to one functional process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **X** | Rate Account Lookup Query | External-system round-trip: the finance system is a separate software functional user, so the outbound request crosses the boundary as an Exit (not a Read). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 3 | **E** | Rate Account Payment Status | Response leg of the external round-trip: balance, last payment date/amount, arrears and next instalment due date received back from the finance system across the boundary as an Entry. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 4 | **X** | Rate Account Payment Status | Exit of the retrieved payment-status data group to the agent (human functional user) so it can be read back to the caller. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 5 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation message types from all causes (e.g. account not found, finance system unavailable). Distinct from the payment-status Exit, which carries data beyond confirmation. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E03)

**CG-E03-01 · Measurement Gap** — Is the account status obtained by an external round-trip to a separate finance system (Exit+Entry), or does Salesforce read it from a local/replicated store (Read)? Also unclear whether the property-number and address lookups hit the same interface or two different retrieval mechanisms.

*Impact:* If a local persistent store is read instead of a cross-boundary call, movements 2-3 (X+E, 2 CFP) would be replaced by a single Read (1 CFP), and the agent-input+display Exits remain. Swing: roughly -1 CFP (4 vs 5). Two distinct retrieval interfaces would not add a process (still one triggering event) but could alter data-group/movement identification.

### Caveats & modeling choices (E03)

- Identity verification is out of scope for this epic — the description states it happens before the lookup and the epic depends_on E10, so no verification movements are counted here.
- The finance system is assumed to be a separate software functional user (strongly implied by 'retrieves ... from the finance system'), making the retrieval a cross-boundary Exit+Entry rather than a persistent-storage Read.
- No local Salesforce Create/Update/Delete is described; the process is read-only from the caller's perspective, so no Write movements are counted.
- Lookup by property number OR address is treated as one triggering event with alternative inputs (one functional process), not two processes.

---

## E04 — Set Up a Rates Payment Plan

**Epic CFP: 6 · Confidence: Assumed**

**Functional users:** Council rates agent (human, via UI) · Rate account persistent store · Council hardship policy store · Post/email delivery system (other software/device functional user)

### FP1 — FP1-SetUpPaymentPlan — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Payment Plan Request | Single triggering Entry: agent detects the resident's request and submits the proposed instalment amount/frequency; all responses belong to this one functional process (Rule 13, single Entry). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99 |
| 2 | **R** | Hardship Policy Limits | Validation against council hardship policy limits requires retrieving the policy limits data group from persistent storage (RULE 18). Assumes limits are stored, not hardcoded — see CG-E04-01. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Rate Account | Calculating the instalment schedule requires the outstanding-arrears balance retrieved from the rate account in persistent storage (RULE 18). Calculation itself is manipulation, not a movement. See CG-E04-02. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Payment Plan Arrangement | Recording the arrangement on the rate account writes the payment-plan data group to persistent storage; one Write per data group per process (RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | Confirmation/Error Message | One Exit accounts for all confirmation/error messages to the agent from all causes (e.g. hardship-policy validation pass/fail) in this functional process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 6 | **X** | Payment Plan Confirmation | The written confirmation carries the instalment schedule (data beyond a plain accept/error confirmation) dispatched to the resident via the post/email delivery system, a functional user across the boundary — a separate Exit data group. No return response is expected, so it is a one-way Exit (not a round trip). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E04)

**CG-E04-01 · Measurement Gap** — Are the council hardship policy limits stored persistently (validated via a Read) or hardcoded configuration/constants embedded in logic? The epic says the plan is 'validated against council hardship policy limits' without stating their source.

*Impact:* If limits are hardcoded constants there is no persistent-storage Read: swing -1 CFP (5 instead of 6). Counted as a Read (RULE 18) under the assumption limits are stored data.

**CG-E04-02 · Measurement Gap** — Is the outstanding-arrears balance read from the rate account within this process, or is it already supplied by dependency E03 and carried in on the triggering Entry? The epic implies calculation needs the balance but does not state the retrieval.

*Impact:* If the balance is passed in via the Entry rather than read here: swing -1 CFP (5 instead of 6). Counted as a Read under the assumption E04 retrieves current balance to compute the schedule.

**CG-E04-03 · Measurement Gap** — Is the calculated instalment schedule also presented back to the agent on-screen (for review/acceptance) as a distinct data group, separate from the pass/fail confirmation and the mailed confirmation?

*Impact:* If the schedule is displayed to the agent as additional data beyond the confirmation message, that is a separate Exit: swing +1 CFP (7 instead of 6). Not counted, as the epic only specifies a written confirmation to the resident.

**CG-E04-04 · Measurement Gap** — Does 'records the arrangement on the rate account' involve updating the rate account status (e.g. flagging it 'on payment plan') as a second, distinct object of interest in addition to writing the arrangement record?

*Impact:* If the rate account itself is also updated as a distinct data group, that is a second Write: swing +1 CFP (7 instead of 6). Counted as a single Write to the Payment Plan Arrangement data group.

---

## E05 — Report a Pothole or Road Defect

**Epic CFP: 6 · Confidence: Assumed**

**Functional users:** Agent (human user capturing the resident's report via UI) · Roads team (recipient of the assigned works order)

### FP1 — FP1-ReportRoadDefect — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Defect Report | Single triggering Entry from the agent (functional user) detecting the 'resident reports a defect' event; all responses to it belong to this one process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Road-Defect Works Order | Read of persistent works-order store to find an existing duplicate defect at the same location within a radius (CRUD Read of the object of interest). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Road-Defect Works Order | No-duplicate branch: Write persisting the new works order with the Roads-team assignment as an owner attribute (one Write per object of interest per process). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Caller-Case Link | Duplicate branch: Write persisting the caller-to-existing-case association. Distinct data group from the new works order; both branches are responses to the same triggering Entry so both live in this process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 5 | **X** | Case Tracking Reference | The reference number is data beyond mere confirmation, so it is a separate Exit data group from the generic confirmation/error Exit (covers both new and linked cases). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 6 | **X** | Confirmation/Error Message | One Exit accounts for all error/confirmation message types from all causes (invalid location, submission accepted, etc.) for the process. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E05)

**CG-E05-01 · Measurement Gap** — The epic states the caller is linked to a case and sent a reference, but does not specify whether the caller's identity/contact details are captured as a separate data group entered by the agent, or are already in session context (e.g. from the call). If captured as a distinct data group it would add one Entry.

*Impact:* CFP swing: +1 (extra Entry for Caller Contact data group) if caller identity is separately captured. Modelled as already-in-context here (no extra Entry).

**CG-E05-02 · Measurement Gap** — 'Assigns it to the Roads team' is modelled as setting an owner attribute on the works-order Write. If assignment instead pushes a notification/work item to the Roads team (a separate software/human functional user across the boundary), that is an additional Exit.

*Impact:* CFP swing: +1 (Exit to Roads team functional user) if an assignment notification is issued. No notification is stated, so excluded from the base count.

**CG-E05-03 · Measurement Gap** — 'Links the caller to that case' is treated as a Write to a distinct Caller-Case Link junction data group. If linking is instead an in-place update to the existing Road-Defect Works Order object of interest, it collapses into the same data group as the create branch and would not add a distinct Write.

*Impact:* CFP swing: -1 (from 6 to 5) if the link is the same object of interest as the works order rather than a separate association data group.

---

## E06 — Book a Hard Rubbish Collection

**Epic CFP: 8 · Confidence: Assumed**

**Functional users:** Council agent (human, via UI) · Waste scheduling service (external software) · SMS gateway / resident (message recipient)

### FP1 — FP1-BookHardRubbishCollection — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Booking Request | Single triggering Entry from the agent detecting the booking event; one Entry per functional process (Primer Rule 5). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Collection Allowance | Retrieve the resident's remaining free collections for the year from persistent storage (Primer Rule 2, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Item Category Rules | Retrieve accepted-category reference data to validate requested items; distinct object of interest from allowance, so a separate Read (Primer Rule 2, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Collection Date Allocation | Outbound request to the waste scheduling service (another piece of software, a functional user across the boundary) — Exit half of the round-trip (Primer Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 5 | **E** | Collection Date Allocation | Response received back from the scheduling service — Entry half of the external round-trip (Primer Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 6 | **W** | Hard Rubbish Booking | Persist the confirmed booking to storage (Primer Rule 2, RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | Booking Confirmation | Confirmation message to the resident via the SMS gateway; carries booking date/reference (data beyond mere acceptance) and targets a different functional user than the agent, so a separate Exit (Primer Rule 3). Modeled as fire-and-forget (no delivery-status Entry) — see gap CG-E06-01. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 8 | **X** | Booking Result Message | One Exit accounting for all confirmation/error message types to the agent from all causes (e.g. quota exhausted, unaccepted items, success) — Primer Rule 3. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E06)

**CG-E06-01 · Measurement Gap** — Does the SMS gateway return a delivery/acknowledgement status to the functional process, making the SMS an external round-trip (Exit + Entry), or is it fire-and-forget (Exit only)? Modeled here as fire-and-forget.

*Impact:* CFP swing +1 (adds one Entry for the delivery-status response) if the SMS is a round-trip per Primer Rule 1.

**CG-E06-02 · Measurement Gap** — The epic states confirmation is by SMS but does not state an on-screen agent-facing confirmation/error message. Is there a distinct agent-facing message (order 8) separate from the resident SMS?

*Impact:* CFP swing -1 if error/confirmation to the agent does not exist as a distinct Exit; included here because error paths (no free collections, unaccepted items) must be reported to the triggering agent (Primer Rule 3).

**CG-E06-03 · Measurement Gap** — Are 'remaining free collections' and 'accepted item categories' two distinct persistent objects of interest (two Reads), or is the allowance derived by counting existing bookings? Modeled as two distinct Reads.

*Impact:* CFP swing +/-1 depending on whether allowance and category-rule data are the same or distinct objects of interest, or derived rather than stored.

### Caveats & modeling choices (E06)

- Single functional process assumed: one triggering event (agent submits booking) drives all responses (Primer Rules 4-5).
- External round-trip to the waste scheduling service counted as Exit+Entry (Primer Rule 1).
- SMS confirmation counted as one Exit to the resident and modeled fire-and-forget; a separate Exit covers all agent-facing confirmation/error messages (Primer Rule 3).
- No source code available (proposal grain) — implementationType/isApiCall omitted; measurement rests on defensible assumptions, hence confidence Assumed.

---

## E07 — Lodge a Noise or Nuisance Complaint

**Epic CFP: 4 · Confidence: Assumed**

**Functional users:** Agent (records complaint via UI) · Complainant / Resident (receives case reference)

### FP1 — FP1-LodgeComplaint — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Complaint Case | Single triggering Entry: agent (functional user) detects the resident lodging a complaint and enters the complaint data group (nature, address, dates/times, anonymity flag). All responses to this Entry belong to one process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **W** | Complaint Case | Create pattern (Entry + Write): the regulatory case, including its routing/assignment to the Local Laws / Environmental Health team, is persisted as a single Write of one data group. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Confirmation Message | One Exit accounts for all confirmation/error messages issued by the process to the agent from all possible causes. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 4 | **X** | Case Reference | The case reference is data beyond mere confirmation, delivered to a different functional user (the complainant) across the boundary, so it is a separate Exit. Conditional on non-anonymous complainant, but counted once as part of the possible responses. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E07)

**CG-E07-01 · Measurement Gap** — How is the case 'routed to the Local Laws / Environmental Health team'? If routing is an assignment field stored on the case, it is already covered by the Create Write (0 extra CFP). If it triggers a notification to a separate team/system functional user, that adds +1 Exit; if that other software returns a response (assignment ack) it is an external round-trip adding +1 Exit + 1 Entry.

*Impact:* CFP swing of +0 to +2 (process CFP 4 to 6). Assumed the in-system-assignment interpretation (0 extra).

**CG-E07-02 · Measurement Gap** — Is the offending address (or complainant identity) validated/looked up against a persistent reference (e.g. property/address register) during lodgement? The description does not state any retrieval, so no Read was counted.

*Impact:* If an address/reference lookup exists, add +1 Read (process CFP 4 to 5). Not counted to avoid inventing movements.

---

## E08 — Apply for a Parking Permit

**Epic CFP: 10 · Confidence: Assumed**

**Functional users:** Council agent (human user capturing the application via UI) · Resident (receives the digital permit and confirmation email) · Payment gateway (other software, functional user across the boundary)

### FP1 — FP1-ApplyForParkingPermit — 10 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Permit Application | Single triggering Entry: agent submits vehicle registration, address and permit type; all responses to this triggering event belong to one functional process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Property Register | Read of persistent property register to verify the applicant resides at the stated address (Rule 18). Treated as persistent storage; see CG-E08-01 if it is an external service. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Parking Permit | Read of existing permit records for the address to count them for the allowance check (Rule 18). Same object of interest as the permit being issued. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **R** | Permit Allowance | Read of the allowance data group compared against the issued-permit count (Rule 18). Assumed persistent; see CG-E08-02. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **R** | Fee Schedule | Read of fee rates to calculate the permit fee (Rule 18); the calculation itself is data manipulation and is not a movement. Assumed persistent; see CG-E08-03. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 6 | **X** | Payment | External-system round-trip: payment gateway is another piece of software (functional user across the boundary); the request out is an Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 7 | **E** | Payment | Second half of the payment round-trip: the response from the payment gateway is received as an Entry. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 8 | **W** | Parking Permit | Write of the newly issued digital permit to persistent storage (Rule 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 9 | **X** | Parking Permit | Exit delivering the digital permit data to the resident. This carries permit data beyond a mere confirmation, so it is a separate Exit from the confirmation message. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 10 | **X** | Confirmation Message | One Exit accounts for all confirmation and error/rejection messages (failed residency, allowance exceeded, payment declined, success) from all causes in this process, e.g. the confirmation email. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E08)

**CG-E08-01 · Measurement Gap** — Is the property register / residency check backed by persistent storage inside this application, or is it an external service (possibly provided by dependency E10/E11)?

*Impact:* Modelled as a single Read (movement 2). If it is another piece of software, the Read becomes an Exit+Entry round-trip. Swing: +1 CFP.

**CG-E08-02 · Measurement Gap** — Is the permit allowance a distinct persistent data group that is read, or a hard-coded constant/business rule?

*Impact:* Modelled as a Read (movement 4). If it is a hard-coded constant it is not a data movement. Swing: -1 CFP.

**CG-E08-03 · Measurement Gap** — Are fee rates stored persistently (a Fee Schedule that is read) or hard-coded? 'Calculates any fee' also implies some permit types may be free.

*Impact:* Modelled as a Read (movement 5). If rates are hard-coded there is no movement (calculation is manipulation, never counted). Swing: -1 CFP.

**CG-E08-04 · Measurement Gap** — Is the digital permit delivered to the resident as an Exit distinct from the confirmation email, or is the email itself the sole permit-delivery channel?

*Impact:* Modelled as two separate Exits (movements 9 and 10) because the permit carries data beyond acceptance. If they are one and the same output, one Exit is removed. Swing: -1 CFP.

**CG-E08-05 · Measurement Gap** — Does taking payment require persisting a payment/transaction record to a local store in addition to the gateway round-trip?

*Impact:* No local Payment Write was counted (only the Exit/Entry round-trip). If a payment record is persisted, add one Write. Swing: +1 CFP.

---

## E09 — Update Contact Details on Account

**Epic CFP: 4 · Confidence: Assumed**

**Functional users:** Customer service agent (human, via UI) · Customer master data store (persistent storage)

### FP1 — FP1-UpdateContactDetails — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Contact Details | Single triggering Entry: the agent submits the new phone/email/postal-address values, informing the process of the triggering event (resident's request to update). One Entry per process (Rule 5). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Contact Details | CRUD Update pattern (Entry + Read + Write): the current version of the contact-details object of interest is retrieved from persistent storage before the new values overwrite it. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Contact Details | CRUD Update Write: the validated contact-details data group is moved to persistent storage (customer master). One Write of this object of interest per process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Confirmation Message | One Exit accounts for all confirmation and error/validation messages from all causes in this functional process; the confirmation carries no data beyond acknowledgement, so it is a single Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E09)

**CG-E09-01 · Measurement Gap** — The epic states 'the system validates the new details' but does not say how. If validation only checks the entered attributes intrinsically (format/mandatory), it adds no movement. If it reads an internal reference data group (e.g., a postcode/address reference table) it adds one Read (+1 CFP). If it calls an external address-validation/verification service, that is an external-system round-trip adding one Exit + one Entry (+2 CFP).

*Impact:* CFP swing 0 to +2. Measured base assumes intrinsic validation (no extra movement). Resolve by confirming whether validation touches a reference data store or an external service.

**CG-E09-02 · Scope Assumption** — Identity verification is referenced ('After identity verification the agent edits the record') but the epic has depends_on: E10, implying verification is measured under E10. This measurement excludes any verification data movements. Confirm identity verification is fully out of E09 scope.

*Impact:* If any verification step is in fact in E09 scope, additional movements (likely an Entry + Exit/Read) would be added; excluded here to avoid double-counting with E10.

---

## E10 — Verify Caller Identity

**Epic CFP: 4 · Confidence: Assumed**

**Functional users:** Call-centre agent (human, via UI) · Customer master data store (persistent storage)

### FP1 — FP1-VerifyCallerIdentity — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Caller-Supplied Identity Answers | Single triggering Entry: the agent detects the triggering event (need to verify a caller) and submits the KBA answers, initiating the process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **R** | Customer Master Record | CRUD-read: retrieve the stored customer identity attributes from persistent storage to compare against the supplied answers (Primer Rule 2, RULE 18). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Verification Attempt Log | Write to persistent storage: log the verification attempt against the customer record (Primer Rule 2, RULE 19). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Verification Result | Exit carrying the substantive verified/failed outcome data group to the agent (functional output). Per Primer Rule 3, this same single Exit also subsumes any error/confirmation messaging from all causes. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E10)

**CG-E10-01 · Measurement Gap** — Does the system present the knowledge-based verification questions (or their expected answers) to the agent, or does the agent ask them independently? The description says 'the agent asks' the questions, implying no software output, but a question-retrieval step could constitute either an additional Exit within this process or a separate query functional process.

*Impact:* If the system supplies questions via an agent request: +2 CFP as a separate functional process (Entry + Exit). If it only pushes questions as part of this process: +1 CFP (an extra Exit). Current count assumes the agent sources questions outside the software, so 0 added.

**CG-E10-02 · Measurement Gap** — Is there a distinct error/confirmation-message Exit (e.g. 'customer not found', 'system unavailable', input-validation errors) separate from the substantive verified/failed Verification Result Exit?

*Impact:* Per Primer Rule 3 a functional process typically has one Exit for all error/confirmation messages. The verified/failed result was treated as the data-carrying output Exit that also absorbs error messaging. If a genuinely separate error-message data group is required: +1 CFP.

### Caveats & modeling choices (E10)

- The verified/failed result is treated as a data-carrying functional-output Exit; under Primer Rule 3 it is also assumed to absorb all error/confirmation messaging, so no separate error Exit was counted (see CG-E10-02).
- One functional process assumed, triggered by the agent submitting answers; question presentation is assumed to occur outside the software (see CG-E10-01).
- Delete/Update semantics not applicable — the logging step is a Create (single Write of a new attempt record).

---

## E11 — Look Up Council Asset by Location

**Epic CFP: 5 · Confidence: Assumed**

**Functional users:** Agent or calling process (lookup requester) · GIS/asset service (external software)

### FP1 — FP1-LookupAssetByLocation — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Location Query | Single triggering Entry from the functional user (agent or calling process) detecting the 'look up asset by location' event; all responses belong to this process (Primer Rule 5). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26 |
| 2 | **X** | Location Query | External-system round-trip: request leaving to another piece of software (GIS/asset service, a functional user across the boundary) = Exit, not Read (Primer Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 3 | **E** | Asset Details | External-system round-trip: response received back from the GIS/asset service = Entry (Primer Rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213 |
| 4 | **X** | Asset Details | Exit delivering the resolved asset details and responsible team to the requesting functional user; distinct data group beyond a bare confirmation. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 5 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation (including no-asset-found) messages from all causes for this process (Primer Rule 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E11)

**CG-E11-01 · Measurement Gap** — The FUR states results are returned 'to the agent OR calling process' — two candidate functional users initiating the same triggering event. Under Primer Rule 4 a different initiating functional user constitutes a DISTINCT functional process. Is this one shared process serving whichever user, or two separate processes (one human-UI initiated, one integration/API initiated)?

*Impact:* Measured as ONE shared process (5 CFP). If treated as two distinct processes per initiating functional user, count would be ~2x. CFP swing: +5 (5 -> 10).

**CG-E11-02 · Measurement Gap** — Assumed the GIS/asset service is a separate piece of software (functional user across the boundary), so asset lookup is a round-trip Exit/Entry rather than a Read from persistent storage owned by this application. If the asset data is actually stored in a datastore owned by this application, movements 2/3 would instead be a single Read.

*Impact:* Under the persistent-storage interpretation the outbound Exit + inbound Entry (2 CFP) collapse to one Read (1 CFP). CFP swing: -1 (5 -> 4).

---

## E12 — Cancel a Hard Rubbish Collection Booking

**Epic CFP: 8 · Confidence: Assumed**

**Functional users:** Call-centre agent (human, via UI) · SMS gateway (other software / notification device)

### FP1 — FP1-CancelBooking — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Booking Search Criteria | Single triggering Entry: agent enters address or booking reference in response to the resident's phone call (one triggering event → one process). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99 |
| 2 | **R** | Booking | Update-CRUD Read: retrieve the persistent booking (collection window, item details, status) needed to confirm and cancel. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Booking | Data Exit: booking window/item details shown so the agent can confirm them with the caller — data beyond a bare confirmation, so a distinct Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |
| 4 | **W** | Booking | Update-CRUD Write: system marks the booking cancelled (status change, not physical delete). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **R** | Collection Allowance | Read current annual free-collection allowance/usage before restoring it (object of interest distinct from the booking). See gap CG-E12-02 — this Read is assumed. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 6 | **W** | Collection Allowance | Write: restore the resident's free-collection allowance for the year. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | Cancellation SMS | Exit across the boundary to the SMS gateway (other software / device functional user); outbound notification counted as one Exit. See gap CG-E12-03 on possible round-trip. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L207-L213 |
| 8 | **X** | Confirmation/Error Message | One Exit accounts for all confirmation and error messages (window-passed, booking-not-found, cancellation confirmed) from all causes. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272 |

### Measurement gaps (E12)

**CG-E12-01 · Measurement Gap** — Process boundary: is the booking lookup ('look up existing booking by address or booking reference, confirm window/item details') a distinct enquiry functional process, or a Read step within the single Cancel process? Modeled here as one process (the phone call is a single triggering event handled continuously by one functional user).

*Impact:* CFP swing +3. If split into a Lookup enquiry (E+R+X-details+X-error = 4 CFP) plus Cancel (E+R+W+R+W+X-SMS+X-msg = 7 CFP), epic total becomes ~11 CFP instead of 8.

**CG-E12-02 · Measurement Gap** — Does restoring the annual free-collection allowance require reading the current allowance/usage (Read + Write), or is it a single in-place Write? Requirement does not state the allowance is retrieved/displayed.

*Impact:* CFP swing -1 (8 → 7) if the allowance Read (order 5) is dropped.

**CG-E12-03 · Measurement Gap** — Is the cancellation SMS a fire-and-forget outbound Exit, or a round-trip where a gateway delivery/acceptance acknowledgment is received and used by the process (Exit + Entry)? Requirement only says 'sends the caller an SMS'.

*Impact:* CFP swing +1 (8 → 9) if a consumed gateway-response Entry is added per external-system round-trip rule.

**CG-E12-04 · Measurement Gap** — Caller identity verification ('after the caller's identity is verified') is assumed out of scope, owned by dependency E06. If verification is intended to be part of THIS epic's process, an additional functional process (or extra movements) would be needed.

*Impact:* No CFP counted here for verification. If in-scope, add a separate identity-verification functional process (est. +5 to +7 CFP).

### Caveats & modeling choices (E12)

- Modeled as a single functional process triggered by the resident's phone call; the lookup is treated as the Read within the cancel rather than a separate enquiry (see CG-E12-01).
- Identity verification treated as out of scope (dependency E06).
- Cancellation modeled as an Update (status = cancelled), not a physical Delete.
- Cancellation SMS counted as one outbound Exit to the SMS gateway (no round-trip Entry) absent evidence of a consumed acknowledgment.

---

## COSMIC v5.0 Movement-Pattern Primer (Salesforce delivery scope)

I now have all the material needed. Composing the primer.

## COSMIC v5.0 Movement-Counting Primer — Salesforce Delivery Scope

**1. External-system round-trip** (functional process calls another piece of software and gets a response — federated SSO to IdP, outbound API call). Count **2 movements**: one **Exit** (the request leaving to the other software, a functional user across the boundary) + one **Entry** (the response received back). Never Read/Write — another piece of software is a functional user, so its interactions cross the boundary and are handled by Exit/Entry, not persistent-storage movements.
> Part 2 §3.4 (manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L198-L213): "Do not identify a Read when the FUR … specify any software or hardware functional user as the source of a data group … Interaction with other functional users is by definition across a boundary … which is handled by an Entry data movement." (and symmetrically for Exit at L207-L213)

**2. CRUD on a persistent object** (user-triggered process). Per object of interest: **Create** = Entry (receive data) + Write; **Read** = Entry (receive key/request) + Read + Exit (return data); **Update** = Entry + Read + Write; **Delete** = Entry + one Write (delete is a single Write). One movement of each type per object of interest per process (Rules 13-15).
> Part 1 §4.5 (manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149): "RULE 18: A Read shall: a) retrieve a single data group from persistent storage… RULE 19: A Write shall: a) move data attributes from a single data group to persistent storage… RULE 20: … A requirement to delete a data group … shall be a single Write data movement."

**3. Confirmation and error messages to the user.** Count **one Exit** total per functional process, covering all error/confirmation message types from all causes. Extra: if the message carries data beyond confirming acceptance/error, that additional data group is a separate Exit. No Entry/Exit for errors surfaced by a Read/Write or by the OS.
> Part 2 §3.4 (manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L272): "One Exit is identified to account for all types of error/confirmation messages issued by any one functional process … from all possible causes … If a message … provides data in addition to confirming … this additional data is identified as a separate data group moved by an Exit."

**4. Distinct vs. one functional process.** Two processes are DISTINCT when they respond to different **triggering events**, or when a different **functional user** initiates them. A triggering event cannot be sub-divided and has either happened or not.
> Part 2 §3.2 (manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L63-L71): "Identify the separate events … the 'triggering events' … Identify which functional user(s) … may respond to each triggering event … Identify the functional process started by each triggering Entry."

**5. Single triggering Entry.** Each functional process is initiated by exactly one Entry from a functional user detecting the triggering event; a single Entry is counted per process. All data movements needed for **all possible responses to that triggering Entry** belong to the same functional process.
> Part 1 §4.2 (manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L14-L26): "be initiated by an Entry data movement from a functional user informing the functional process that it has detected a triggering event … 'the set of all data movements that is needed to meet its FUR for all the possible responses to its triggering Entry'." (RULE 13, single Entry: L95-L99)

**Caveat:** Every process is ≥2 movements (one Entry + at least one Exit or Write). "User-triggered" here assumes a human/UI functional user; a clock-tick or inbound integration is itself a triggering Entry.
