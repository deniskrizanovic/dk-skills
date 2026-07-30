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
| E01 | Log a Lost Pet Report | **8** | Assumed | 2 | 4 |
| E02 | Request Tree Lopping or Removal | **6** | Assumed | 1 | 2 |
| E03 | Check Rates Payment Status | **4** | Assumed | 1 | 3 |
| E04 | Set Up a Rates Payment Plan | **6** | Assumed | 1 | 3 |
| E05 | Report a Pothole or Road Defect | **6** | Assumed | 1 | 2 |
| E06 | Book a Hard Rubbish Collection | **8** | Assumed | 1 | 3 |
| E07 | Lodge a Noise or Nuisance Complaint | **5** | Assumed | 1 | 3 |
| E08 | Apply for a Parking Permit | **11** | Assumed | 1 | 5 |
| E09 | Update Contact Details on Account | **3** | Assumed | 1 | 2 |
| E10 | Verify Caller Identity | **4** | Assumed | 1 | 2 |
| E11 | Look Up Council Asset by Location | **5** | Assumed | 1 | 1 |
| E12 | Cancel a Hard Rubbish Collection Booking | **9** | Assumed | 2 | 4 |
| | **Total** | **75** | | | 34 |

---

## Data groups

| Epic | FP | Data group | Description |
|---|---|---|---|
| E01 | FP1-SearchAnimalRegistry | Pet Search Criteria | Species/breed/description and/or microchip identifier supplied by the agent to look for existing matches. |
| E01 | FP1-SearchAnimalRegistry | Registered Animal (Microchip) Record | Persistent registry record of a microchip-registered animal used to detect a match. |
| E01 | FP1-SearchAnimalRegistry | Found-Pet Record | Persistent registry record of a previously reported found pet used to detect a match. |
| E01 | FP1-SearchAnimalRegistry | Potential Match Result | Consolidated set of candidate matching animals returned to the agent for review. |
| E01 | FP2-CreateLostPetCase | Lost Pet Case | The case record carrying caller details, pet species/breed/description, last-seen location and date, contact number, queue assignment and generated case reference. |
| E01 | FP2-CreateLostPetCase | SMS Confirmation | Outbound confirmation message carrying the case reference, addressed to the caller via the SMS gateway. |
| E01 | FP2-CreateLostPetCase | Case Confirmation | Confirmation / case reference returned on-screen to the agent acknowledging successful case creation. |
| E02 | FP1-RegisterTreeWorksRequest | Tree Works Request | The lopping/removal request describing the tree of interest: location (address or map pin), reported reason/hazard, and the priority derived from the reported hazard; entered by the agent and persisted as a works request. |
| E02 | FP1-RegisterTreeWorksRequest | Tree Location Query | Location/parcel coordinates sent to the asset/GIS boundary service to test whether the tree sits on council land. |
| E02 | FP1-RegisterTreeWorksRequest | Council Land Determination | Ownership/boundary result returned by the GIS service indicating whether the tree location falls on council-owned land. |
| E02 | FP1-RegisterTreeWorksRequest | Crew Notification | Work-assignment alert dispatched to the Parks & Gardens crew for the created works request. |
| E02 | FP1-RegisterTreeWorksRequest | Resident Acknowledgement | Confirmation email to the resident including the expected response time for the request. |
| E03 | FP1-CheckRatesPaymentStatus | Rate Account Lookup | Identification data the agent uses to locate the rate (property tax) account: property number or address. |
| E03 | FP1-CheckRatesPaymentStatus | Rate Payment Status | Payment position of the rate account: current balance, last payment date and amount, arrears, and next instalment due date. |
| E04 | FP1-SetUpPaymentPlan | Proposed Payment Plan | Agent-entered instalment amount, payment frequency and target rate-account reference for the resident in arrears. |
| E04 | FP1-SetUpPaymentPlan | Hardship Policy Limits | Council hardship-policy thresholds and rules the proposed plan must satisfy (e.g. min instalment, max term). |
| E04 | FP1-SetUpPaymentPlan | Rate Account | The resident's rates account carrying the outstanding arrears balance needed to validate the plan and compute the schedule. |
| E04 | FP1-SetUpPaymentPlan | Payment Arrangement | The accepted instalment arrangement and calculated repayment schedule persisted against the rate account. |
| E04 | FP1-SetUpPaymentPlan | Validation Result | Error/confirmation indication returned to the agent stating whether the proposed plan was accepted or rejected against policy. |
| E04 | FP1-SetUpPaymentPlan | Payment Plan Confirmation | Written confirmation document (plan terms and schedule) handed to the post/email channel for dispatch to the resident. |
| E05 | FP1-ReportRoadDefect | Defect Report | Captured location, defect type, and severity of the road defect reported by the resident. |
| E05 | FP1-ReportRoadDefect | Existing Road Defect | Persistent road-defect case records queried to detect a duplicate at the same location within a radius. |
| E05 | FP1-ReportRoadDefect | Road Defect Works Order | Newly created works order for the road defect, owned by / assigned to the Roads team. |
| E05 | FP1-ReportRoadDefect | Caller Case Link | Association linking the reporting caller to the matched existing defect case in the duplicate branch. |
| E05 | FP1-ReportRoadDefect | Case Tracking Reference | Case reference/identifier returned to the caller so they can track the reported defect. |
| E05 | FP1-ReportRoadDefect | Confirmation/Error Message | Validation, error, and confirmation feedback for the report-submission process. |
| E06 | FP1-BookHardRubbishCollection | Booking | The hard/bulky waste collection booking: resident address, item types and counts, preferred collection window, and (once allocated) the collection date. Same object of interest whether entered by the agent or written to storage. |
| E06 | FP1-BookHardRubbishCollection | Resident Collection Allowance | The resident's free-collection entitlement/usage for the year, used to check remaining free collections before allowing the booking. |
| E06 | FP1-BookHardRubbishCollection | Accepted Item Categories | Reference catalogue of item categories accepted for hard rubbish collection, used to validate the entered items. |
| E06 | FP1-BookHardRubbishCollection | Scheduling Request | The outbound request to the waste scheduling service asking for the next available collection date (carries location/window/volume context). |
| E06 | FP1-BookHardRubbishCollection | Allocated Collection Date | The next available collection date returned by the waste scheduling service. |
| E06 | FP1-BookHardRubbishCollection | Booking Confirmation | The confirmation of the booking sent to the resident by SMS, carrying the allocated date and booking summary. |
| E06 | FP1-BookHardRubbishCollection | Error/Confirmation Message | On-screen confirmation or error indication to the agent (e.g. no free collections remaining, item not in accepted categories, booking success). |
| E07 | FP1-LodgeComplaint | Nuisance Complaint | The reported nuisance: nature/category of complaint, offending address, and dates/times of occurrence. |
| E07 | FP1-LodgeComplaint | Complainant | The reporting resident's contact details and their anonymity preference. |
| E07 | FP1-LodgeComplaint | Regulatory Case | The persisted regulatory case record, including status and the assigned Local Laws / Environmental Health owner/queue. |
| E07 | FP1-LodgeComplaint | Case Reference | The case identifier acknowledgment delivered to the complainant confirming lodgement. |
| E07 | FP1-LodgeComplaint | Error/Confirmation | Validation error or success acknowledgment returned to the agent for the lodgement action. |
| E08 | FP1-ApplyForParkingPermit | Permit Application | Applicant-supplied application payload: vehicle registration, residential address, and requested permit type. |
| E08 | FP1-ApplyForParkingPermit | Property Record | Persistent property-register entry used to confirm the applicant resides at the stated address. |
| E08 | FP1-ApplyForParkingPermit | Issued Permit | Persistent records of permits already granted to the address, read to tally the current count for the allowance check. |
| E08 | FP1-ApplyForParkingPermit | Permit Allowance | Configured per-address (or per permit-type) maximum number of permits allowed, used as the ceiling in the eligibility check. |
| E08 | FP1-ApplyForParkingPermit | Fee Schedule | Persistent rate/pricing rules read to derive the payable permit fee. |
| E08 | FP1-ApplyForParkingPermit | Payment | Payment request sent to and the settlement/authorization result returned from the external payment system. |
| E08 | FP1-ApplyForParkingPermit | Parking Permit | The newly created digital permit record (permit id, vehicle, address, type, validity) that is persisted and issued back to the applicant. |
| E08 | FP1-ApplyForParkingPermit | Confirmation Email | Notification content dispatched to the email system confirming that the permit was issued. |
| E08 | FP1-ApplyForParkingPermit | Application Status | The single error/confirmation outcome message covering all success and failure paths (e.g. residency failed, allowance exceeded, payment declined, permit issued). |
| E09 | FP1-UpdateContactDetails | Contact Details | The resident's phone, email and postal-address attributes on the council customer account, edited by the agent and persisted to the customer master. |
| E09 | FP1-UpdateContactDetails | Update Confirmation | Confirmation (and any validation-error) message returned to the agent stating the outcome of the contact-detail change. |
| E10 | FP1-VerifyCallerIdentity | Verification Answers | The knowledge-based answers the agent supplies for a call (customer name, property address, date of birth and/or account reference) to be checked. |
| E10 | FP1-VerifyCallerIdentity | Customer Master Record | The persistent customer identity attributes (stored name, address, DOB, account reference) held in the customer master and used as the source of truth for comparison. |
| E10 | FP1-VerifyCallerIdentity | Verification Attempt Log | The persistent audit record of a single verification attempt (outcome, which attributes were checked, time) written against the customer record. |
| E10 | FP1-VerifyCallerIdentity | Verification Result | The verified/failed outcome returned to the agent indicating whether the supplied answers matched the customer master. |
| E11 | FP1-LookUpAssetByLocation | Location Query | The address or map-pin coordinates identifying the point at which to look up a council asset. |
| E11 | FP1-LookUpAssetByLocation | Asset Details | The asset record returned for the location: council-ownership indicator, asset type/attributes (tree, road, drain, streetlight) and the responsible team. |
| E11 | FP1-LookUpAssetByLocation | Lookup Status Message | Confirmation/error indication for the lookup (e.g. invalid address, no council asset found, GIS service unavailable). |
| E12 | FP1-LookUpBooking | Booking Search Criteria | The address or booking reference the agent keys in to locate the resident's existing hard/bulky-waste collection booking. |
| E12 | FP1-LookUpBooking | Booking | The stored hard-rubbish collection booking: collection window, item/bulky-waste details, and current status. |
| E12 | FP2-CancelBooking | Cancellation Request | The agent's command, on the caller's behalf, to cancel the identified booking. |
| E12 | FP2-CancelBooking | Booking | The stored booking record whose collection window/status is read to validate cancellability and whose status is then set to cancelled. |
| E12 | FP2-CancelBooking | Resident Allowance | The resident's annual free hard-rubbish collection entitlement/usage counter that is restored when a booking is cancelled. |
| E12 | FP2-CancelBooking | SMS Confirmation | The cancellation-confirmation text message addressed to the caller and handed to the SMS gateway. |
| E12 | FP2-CancelBooking | Agent Notification | The on-screen confirmation or error message shown to the agent (cancelled / window already passed / not found). |

---

## E01 — Log a Lost Pet Report

**Epic CFP: 8 · Confidence: Assumed**

**Functional users:** Contact-centre agent · SMS gateway

### FP1 — FP1-SearchAnimalRegistry — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Pet Search Criteria | Single triggering Entry: functional user (agent) informs the process of the triggering event (a match check is requested). Rule 10/Rule 13. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L17-L99 |
| 2 | **R** | Registered Animal (Microchip) Record | Retrieve a data group of persistent registry data to find microchip matches. Rule 18 (Read). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Found-Pet Record | Distinct object of interest from microchip records; a separate Read retrieves found-pet matches. Rule 18 (Read). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Potential Match Result | Data issued to a functional user (agent) is analyzed as a normal Exit; a 'no matches' outcome is covered by the Read and needs no extra movement. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |

### FP2 — FP2-CreateLostPetCase — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Lost Pet Case | Single triggering Entry from the agent (distinct triggering event: create the case) carrying caller, pet, location, date and contact attributes. Rule 10/Rule 13. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L17-L99 |
| 2 | **W** | Lost Pet Case | Move the case data group to persistent storage. Rule 19 (Write). Queue routing (owner = Animal Management queue) is an attribute of the same case object and is not a separate Write. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | SMS Confirmation | Data issued to a software/hardware functional user (SMS gateway) is a normal Exit; no response is described so no Entry round-trip. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 4 | **X** | Case Confirmation | One Exit accounts for all confirmation messages returned to the triggering functional user (agent) acknowledging case creation. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E01)

**CG-E01-01 · Measurement Gap** — Is the animal-registry match check a distinct functional process (agent explicitly requests a search, reviews matches, then creates the case), or is it performed automatically inside the case-creation process with a single triggering event?

*Impact:* Modeled as two FPs (separate triggering Entries). If it is one combined FP, the second triggering Entry disappears: swing -1 CFP (epic 8 -> 7).

**CG-E01-02 · Measurement Gap** — Are microchip/registered-animal records and found-pet records two distinct objects of interest, and are matches returned to the agent as one consolidated data group or two?

*Impact:* Modeled as 2 Reads + 1 consolidated Exit. If it is a single registry object one Read is lost (-1); if matches are returned as two separate data groups one Exit is added (+1). Swing -1 to +1 CFP on FP1.

**CG-E01-03 · Measurement Gap** — Is routing to the Animal Management queue an attribute update on the same case record (folded into the case Write) or a data movement to a separate work-management system/object?

*Impact:* Modeled as part of the case Write (no extra movement). If routing is a separate Write or an Exit to another system, swing +1 CFP on FP2.

**CG-E01-04 · Measurement Gap** — Does the case-creation process return an on-screen confirmation / case reference to the agent, or is the SMS to the caller the only acknowledgement?

*Impact:* Included an agent-confirmation Exit as the natural response to the agent's triggering Entry. If no data is returned to the agent, swing -1 CFP on FP2.

---

## E02 — Request Tree Lopping or Removal

**Epic CFP: 6 · Confidence: Assumed**

**Functional users:** Agent (Contact Centre / Council officer capturing the request) · Asset/GIS boundary service (external software) · Parks & Gardens crew · Resident (acknowledgement recipient)

### FP1 — FP1-RegisterTreeWorksRequest — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Tree Works Request | Single triggering Entry that starts the functional process, carrying the tree location and reason describing the works-request object of interest (Rule 13 single Entry; associated validations/formatting absorbed by the Entry). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L95-L99 |
| 2 | **X** | Tree Location Query | External-system round-trip: request out to the asset/GIS boundary service (a software functional user) is one Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 3 | **E** | Council Land Determination | Response back from the GIS functional user is one Entry, analyzed as a normal Entry regardless of whether the value indicates the tree is not on council land (error condition). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 4 | **W** | Tree Works Request | Create/store the works request = one Write. Assigning priority based on the reported hazard is data manipulation to create the attributes written and is accounted for by the Write (no separate movement). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L141-L146 |
| 5 | **X** | Crew Notification | Exit sending work-assignment data to the crew functional user (Rule 17). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L128-L133 |
| 6 | **X** | Resident Acknowledgement | Exit to the resident functional user; the acknowledgement carries additional data (expected response time) beyond a bare confirmation, so it is counted as its own Exit rather than folded into the generic confirmation/error Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E02)

**CG-E02-01 · Measurement Gap** — The description says the agent 'captures... photos if emailed in.' It is unclear whether emailed-in photos are received by this functional process as a distinct entered object of interest (a separate Entry for a Photo/Attachment data group) or are merely referenced/handled outside the measured software. No dedicated attachment-handling FUR is given.

*Impact:* CFP swing +1: if photos constitute a distinct entered data group per Rule 13, add one Entry (7 CFP total). If they are just email attachments outside the measured boundary, no movement (6 CFP).

**CG-E02-02 · Measurement Gap** — The 'not on council land' outcome is not described. If a distinct rejection/redirect message is sent to the resident, under the primer's confirmation/error rule all such messages from one FP collapse into a single Exit, but if the rejection carries additional distinct data (e.g., referral to the correct authority) it could be a separate data-carrying Exit.

*Impact:* CFP swing 0 to +1: collapses into the existing resident Exit under part-2 §3.3.4 unless a genuinely additional data group is returned on rejection.

### Caveats & modeling choices (E02)

- Treated the epic as a single functional process because all activity flows from one triggering event (the agent capturing/submitting the resident's request); no second independent triggering event is described.
- Priority assignment is treated as data manipulation absorbed by the Write per part-1 Rule 19b; no reference-data Read is counted because the priority is derived from the already-entered reported hazard, not from a stored lookup (none is described).
- External GIS council-land check is sized as an Exit+Entry round-trip per the primer, derived from the general functional-user rule (part-2 §3.3.4) rather than a Salesforce-specific worked example.
- Crew and resident are treated as distinct functional users, so their notifications are separate Exits with distinct data groups.

---

## E03 — Check Rates Payment Status

**Epic CFP: 4 · Confidence: Assumed**

**Functional users:** Call-centre agent (human, via the app UI) · Finance system (separate software application)

### FP1 — FP1-CheckRatesPaymentStatus — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Rate Account Lookup | Triggering Entry: agent (functional user) submits the lookup, informing the functional process of the triggering event; a single Entry starts the process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **X** | Rate Account Lookup | External-system round-trip: the finance system is a software functional user, so the outbound request is an Exit analyzed by normal COSMIC rules (primer rule 1). Single Exit for all data describing the one object of interest (Rule 14). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 3 | **E** | Rate Payment Status | External-system round-trip: response from the finance-system functional user is an Entry (balance, last payment date/amount, arrears, next instalment) analyzed by normal COSMIC rules (primer rule 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 4 | **X** | Rate Payment Status | Single Exit for all data describing the one object of interest (the account's payment status) shown to the agent, who reads it back to the caller (Rule 14). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L100-L105 |

### Measurement gaps (E03)

**CG-E03-01 · Measurement Gap** — The FUR does not explicitly state any error/confirmation message (e.g. 'no matching rate account found' when the property number/address does not resolve). If such a message is required, primer rule 3 collapses all error/confirmation messages into a single additional Exit.

*Impact:* CFP swing +1 (one error/confirmation Exit) if the process must report an account-not-found or similar condition. Not counted to avoid inventing a movement not stated in the FUR.

**CG-E03-02 · Measurement Gap** — Boundary of the 'finance system': it is modeled here as a separate software functional user, giving an Exit (request) + Entry (response) round-trip (primer rule 1). If the finance data is instead persistent storage accessed directly by the measured software, the pair collapses to a single Read (Rule 18).

*Impact:* CFP swing -1 (from 4 to 3) if finance retrieval is a Read of persistent storage rather than a round-trip to a separate application. The epic names a distinct 'finance system', so the round-trip interpretation was chosen.

**CG-E03-03 · Measurement Gap** — Identity verification ('After identity verification, the agent looks up...') is referenced but is owned by dependency epic E10 and is therefore excluded from this measurement.

*Impact:* No CFP impact on E03. If identity verification were in scope for E03 it would add at least one further functional process; assumed measured under E10 to avoid double counting.

### Caveats & modeling choices (E03)

- Finance-system interaction modeled as an external round-trip (Exit+Entry) because the epic names a distinct 'finance system'; see CG-E03-02 for the Read alternative.
- Error/confirmation Exit not counted because the FUR does not state one; see CG-E03-01.
- Identity verification excluded as it belongs to dependency epic E10 (CG-E03-03).
- The Entry from the finance system and the Exit to the agent carry the same object of interest (payment status), so they are treated as one data group moved by two different movement types.

---

## E04 — Set Up a Rates Payment Plan

**Epic CFP: 6 · Confidence: Assumed**

**Functional users:** Rates agent (human functional user who captures and submits the proposed plan and receives the validation/confirmation) · Resident's rate account / persistent rates store (object of interest read and written) · Post/email delivery system (software functional user that receives the written confirmation for dispatch to the resident)

### FP1 — FP1-SetUpPaymentPlan — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Proposed Payment Plan | Single triggering Entry: the agent submits the proposed instalment amount/frequency, initiating the functional process; all responses belong to this one FP. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Hardship Policy Limits | Retrieval of one persistent data group; logical validation of the plan against these limits is manipulation accounted for within the Read. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L140 |
| 3 | **R** | Rate Account | Retrieval of the persistent rate account (outstanding arrears) required to validate and to calculate the instalment schedule; distinct object of interest from the policy limits. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L140 |
| 4 | **X** | Validation Result | The single Exit accounting for all error/confirmation messages the FP issues to the agent (plan accepted vs. rejected against policy). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |
| 5 | **W** | Payment Arrangement | Persisting the arrangement/schedule is one Write; the mathematical computation of the schedule is manipulation accounted for within the Write (Rule 19b). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L141-L147 |
| 6 | **X** | Payment Plan Confirmation | Data issued to a software/hardware functional user (post/email channel) analyzed as a normal Exit; carries additional data (plan terms/schedule) beyond the agent's confirmation, so it is a separate Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L272-L276 |

### Measurement gaps (E04)

**CG-E04-01 · Measurement Gap** — The epic says the system 'calculates the schedule' but does not state whether schedule calculation requires reading additional persistent reference data (e.g. interest/penalty rate configuration or a rates calendar) beyond the rate account balance. If such config is read, an extra Read (+1 CFP) applies.

*Impact:* CFP swing: +1 (one additional Read) if a rate/fee configuration data group is read to compute instalments. Not counted here to avoid inventing a movement; FP1 modelled at 6 CFP without it.

**CG-E04-02 · Measurement Gap** — Whether the arrears/eligibility state that qualifies the resident (dependency on E03) is verified within this FP via a Read of a separate object of interest, or whether the Rate Account read already covers it. Assumed covered by the Rate Account read.

*Impact:* CFP swing: +1 (one additional Read) if a distinct eligibility/arrears-status object must be read separately from the Rate Account.

**CG-E04-03 · Measurement Gap** — Whether 'by post or email' represents two distinct functional users requiring two Exits, or a single dispatch channel (one Exit). Modelled as one Exit; per Rule 15 the same Exit type/data group counts once regardless of channel.

*Impact:* CFP swing: 0 under Rule 15 (single data group). No swing expected; noted for transparency on channel modelling.

---

## E05 — Report a Pothole or Road Defect

**Epic CFP: 6 · Confidence: Assumed**

**Functional users:** Agent (call handler capturing the report) · Caller (resident who receives the tracking reference)

### FP1 — FP1-ReportRoadDefect — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Defect Report | Single triggering Entry starting the functional process; carries location, defect type and severity as one data group. All response branches (duplicate vs new) belong to this one FP. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Existing Road Defect | Read of persistent road-defect records to detect a duplicate at the same location within a radius; one Read per data group. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L140 |
| 3 | **W** | Road Defect Works Order | No-duplicate branch: creating the works order writes one data group to persistent storage; the Roads-team assignment is an attribute created within this Write, not a separate movement. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L141-L146 |
| 4 | **W** | Caller Case Link | Duplicate branch: associating the caller with the matched existing case persists a data group (one Write). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L141-L146 |
| 5 | **X** | Case Tracking Reference | The tracking reference is data provided in addition to a confirmation, so it is a separate Exit data group beyond the generic confirmation Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L270-L272 |
| 6 | **X** | Confirmation/Error Message | One Exit accounts for all error/confirmation messages issued by the functional process from all causes; errors arising from the Read/Write add no further movement. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L267-L269 |

### Measurement gaps (E05)

**CG-E05-01 · Measurement Gap** — Does 'assigns it to the Roads team' merely set an owner/assignment attribute on the works order (counted within the Create Write, as measured), or does it also send a distinct notification to the Roads team as a separate functional user? If the latter, that outbound notification is an additional Exit.

*Impact:* CFP swing +1 (one additional Exit to the Roads team) if assignment triggers a separate notification data movement to a distinct functional user.

**CG-E05-02 · Measurement Gap** — The epic states the caller is linked to the case but does not specify how the caller is identified. If the process must look up / retrieve caller (contact) data from persistent storage before linking, that is an additional Read not currently counted.

*Impact:* CFP swing +1 (one additional Read of a Caller/Contact data group) if caller identification requires a persistent-storage lookup within this process.

---

## E06 — Book a Hard Rubbish Collection

**Epic CFP: 8 · Confidence: Assumed**

**Functional users:** Agent (books the collection on behalf of the resident) · Waste scheduling service (external software) · SMS gateway / resident via SMS (external service receiving the confirmation)

### FP1 — FP1-BookHardRubbishCollection — 8 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Booking | Single triggering Entry: agent submits address, item types/counts and preferred window, detecting the 'book collection' event. All responses to this Entry belong to this one functional process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Resident Collection Allowance | Retrieving the resident's free-collection entitlement/usage from persistent storage = one Read per data group. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Accepted Item Categories | Retrieving the accepted-categories reference data from persistent storage to validate the items = one Read. (Assumes categories are persisted; see gap CG-E06-02.) | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Scheduling Request | External-system round-trip: the request out to the waste scheduling service (a functional user) is one Exit, analyzed by normal COSMIC rules. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 5 | **E** | Allocated Collection Date | External-system round-trip: the response back in from the waste scheduling service is one Entry, regardless of whether it signals an error. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 6 | **W** | Booking | Creating the booking in persistent storage = one Write. Same object of interest as the entered booking, so it is the one 'Booking' data group, not two. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 7 | **X** | Booking Confirmation | Confirmation sent to the resident/SMS gateway (a functional user) is an Exit carrying booking data in addition to a bare confirmation, so it is a distinct Exit from the agent-facing message. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |
| 8 | **X** | Error/Confirmation Message | One Exit accounts for all error/confirmation messages the process issues to the agent (no free collections, invalid item, or success). Errors arising from the Reads/Write add no further movement. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E06)

**CG-E06-01 · Measurement Gap** — Does booking a collection separately update/decrement the resident's free-collection allowance (a Write to 'Resident Collection Allowance'), or is remaining allowance derived on the fly by counting existing bookings (no separate Write)? The description states the allowance is checked but not whether it is written back.

*Impact:* CFP swing +1 (9 CFP) if a separate Write to the allowance object is required; 8 CFP as measured if usage is derived rather than stored.

**CG-E06-02 · Measurement Gap** — Are the accepted item categories held in persistent storage (Read at order 3), or are they hardcoded/configuration constants that are not a persisted object of interest?

*Impact:* CFP swing -1 (7 CFP) if categories are not persistent data (no Read); 8 CFP as measured assuming they are read from storage.

**CG-E06-03 · Measurement Gap** — Is the waste scheduling service an independent external software functional user (round-trip = Exit + Entry), or an in-scope component whose date lookup would instead be a Read of persistent schedule data (one Read)?

*Impact:* CFP swing -1 (7 CFP) if it collapses to a single Read instead of an Exit+Entry pair; 8 CFP as measured treating it as an external functional user per primer rule 1.

---

## E07 — Lodge a Noise or Nuisance Complaint

**Epic CFP: 5 · Confidence: Assumed**

**Functional users:** Council agent (records the complaint) · Complainant / resident (receives case reference) · Local Laws / Environmental Health team (receives routed case)

### FP1 — FP1-LodgeComplaint — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Nuisance Complaint | Triggering Entry: the agent detects the lodgement event and submits the nuisance details (nature, offending address, dates/times). A single triggering Entry starts the process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L17-L37 |
| 2 | **E** | Complainant | Second Entry for a distinct object of interest (the reporter): contact details and anonymity preference. Additional (non-triggering) Entries are permitted alongside the single triggering Entry. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 3 | **W** | Regulatory Case | Create the regulatory case in persistent storage, including its assigned Local Laws / Environmental Health team/owner (routing modelled as internal assignment persisted with the case). One Write per data group written. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Case Reference | Confirmation to the complainant that also carries additional data (the case reference); additional data in a confirming message is identified as a separate data group moved by an Exit. Occurs unless the complainant is anonymous. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |
| 5 | **X** | Error/Confirmation | One Exit accounts for all error/confirmation messages issued to the agent; error conditions arising from the Read/Write are already accounted for by those movements. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E07)

**CG-E07-01 · Measurement Gap** — Routing to the Local Laws / Environmental Health team is modelled as internal owner/queue assignment persisted with the case (part of the Write). If routing instead fires an outbound notification/hand-off to a separate team system that is a functional user, that hand-off would be an additional Exit.

*Impact:* CFP swing: +1 (5 -> 6) if the team is served by a distinct downstream software/system requiring an Exit rather than internal assignment.

**CG-E07-02 · Measurement Gap** — Complainant contact/anonymity is treated as a distinct object of interest (second Entry). If the FUR grain treats complainant attributes as part of the same complaint data group (single object of interest captured in one submission), only one triggering Entry exists.

*Impact:* CFP swing: -1 (5 -> 4) if complainant details collapse into the Nuisance Complaint data group.

**CG-E07-03 · Measurement Gap** — The epic does not state whether the offending address or complaint category is validated against a persistent reference (property/address register, category list) during lodgement.

*Impact:* CFP swing: +1 per distinct persistent data group Read (e.g. +1 for an address/property lookup) if such validation Reads exist.

### Caveats & modeling choices (E07)

- Single functional process identified: one triggering event (agent lodges the complaint). No second process is described in the epic.
- Routing to the team is counted as internal case assignment (folded into the Write), not a separate Exit — see CG-E07-01.
- Complainant modelled as a separate object of interest yielding a second Entry — see CG-E07-02; this is the primary driver of the Assumed confidence.
- No persistent-data Read is counted because the epic does not describe any address/category validation lookup — see CG-E07-03.
- All movements are justified from the shared primer citations (Rules 10/13 for Entries, Rules 18-20 for the Write, part-2 error/confirmation guidance for both Exits); no additional manual adjudication was required.

---

## E08 — Apply for a Parking Permit

**Epic CFP: 11 · Confidence: Assumed**

**Functional users:** Parking permit agent (human functional user who captures data and triggers the application) · Property register system · Payment system · Email/notification system

### FP1 — FP1-ApplyForParkingPermit — 11 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Permit Application | Single triggering Entry: the agent submits vehicle registration, address and permit type, detecting the triggering event that starts the functional process; all subsequent movements are responses to this one Entry (primer item 5). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Property Record | Retrieving persistent property-register data to verify residency = one Read per data group (primer item 2). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **R** | Issued Permit | Retrieving persistent issued-permit data to count permits for the address = one Read (primer item 2). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **R** | Permit Allowance | Retrieving the configured allowance ceiling to compare against the issued count = one Read; treated as a distinct persistent data group (primer item 2). See gap CG-E08-02. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **R** | Fee Schedule | Fee calculation is data manipulation (no movement); reading the persistent fee rates to calculate the fee = one Read (primer item 2). See gap CG-E08-03. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 6 | **X** | Payment | External-system round-trip: the request out to the payment system (a functional user) is one Exit (primer item 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 7 | **E** | Payment | External-system round-trip: the payment/authorization response back in is one Entry, analyzed as a normal Entry regardless of success/failure (primer item 1). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 8 | **W** | Parking Permit | Creating the digital permit in persistent storage = one Write (primer item 2). | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 9 | **X** | Parking Permit | Returning the issued digital permit to the functional user is an Exit carrying data beyond a bare confirmation, so it is a separate Exit (primer item 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |
| 10 | **X** | Confirmation Email | Sending the confirmation email to the email system (a functional user) is an Exit; its content is additional data, so a separate Exit (primer items 1 and 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |
| 11 | **X** | Application Status | One Exit accounts for all error/confirmation messages of the process (residency failed, allowance exceeded, payment declined, or success); Read/Write error reporting adds no further movement (primer item 3). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E08)

**CG-E08-01 · Measurement Gap** — Is the property register the measured software's own persistent storage (modeled here as one Read) or a separate piece of software / external functional user? If external, the residency check becomes an Exit+Entry round-trip.

*Impact:* CFP swing +1 (an Entry would be added if the property register is an external system rather than persistent storage). E08 depends_on E10/E11, which may host this register.

**CG-E08-02 · Measurement Gap** — Is the permit allowance a separately stored/read data group, or an attribute retrieved together with the issued-permit or permit-type data (thus not a distinct Read)?

*Impact:* CFP swing -1 if the allowance is not a distinct data-group Read.

**CG-E08-03 · Measurement Gap** — Does fee calculation read persistent fee-rate data (a Read, as counted), or is the fee entered/passed with the application or fixed constant (no Read)?

*Impact:* CFP swing -1 if no persistent fee-schedule Read occurs.

**CG-E08-04 · Measurement Gap** — How is payment handled? Are payment details captured as an additional Entry from the agent, and is a payment/transaction record persisted (a Write)? Modeled here only as a payment-system Exit+Entry round-trip.

*Impact:* CFP swing +1 to +2 if a distinct payment-details Entry and/or a payment-record Write are in scope.

**CG-E08-05 · Measurement Gap** — Is 'Apply for a Parking Permit' a single functional process (assumed), or is payment a separately triggered functional process (agent/resident initiates payment as its own triggering event)?

*Impact:* If split into two functional processes, the total structure and count change (a second FP would add its own triggering Entry and confirmation Exit, roughly +2 CFP).

---

## E09 — Update Contact Details on Account

**Epic CFP: 3 · Confidence: Assumed**

**Functional users:** Customer service agent (human user operating the system on the resident's behalf)

### FP1 — FP1-UpdateContactDetails — 3 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Contact Details | Single triggering Entry: the agent submits the edited phone/email/postal-address for the account. One Entry initiates the functional process and its FUR-response set. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **W** | Contact Details | Persisting the updated contact-detail data group to the customer master is a single Write. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Update Confirmation | All confirmation and validation-error messages the functional process can issue collapse into one Exit; error indications arising from the Write add no further movement. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E09)

**CG-E09-01 · Measurement Gap** — Does this functional process itself Read the existing customer record from the customer master (to load/display it for editing or to confirm existence) before writing, or was that Read already performed by the E10 identity-verification/account-lookup process? The epic says 'the agent edits the record' but the record retrieval appears to belong to the E10 dependency.

*Impact:* If a Read of the existing customer record occurs within this FP, add +1 CFP (Read of Contact Details). Base count assumes the record was already retrieved by E10 and no Read is needed here. Swing: +1 CFP (3 -> 4).

**CG-E09-02 · Measurement Gap** — Does validation of the new postal address (or email/phone) invoke an external reference/lookup service (e.g. an address/postcode validation system)? The epic states 'the system validates the new details' without specifying whether validation is internal manipulation or a call to another piece of software.

*Impact:* If an external validation service is called, that service is a functional user and the round-trip adds one Exit (request) + one Entry (response) = +2 CFP. If validation is purely internal data manipulation, it adds 0 CFP (manipulation is not a data movement). Swing: +2 CFP (3 -> 5).

### Caveats & modeling choices (E09)

- Identity verification is treated as out of scope for E09 because it is provided by the E10 dependency (depends_on: E10); only the edit-validate-save-confirm flow is measured.
- The resident is not a functional user of the software (they interact with the agent by phone); the sole functional user is the customer-service agent operating the system.
- Confidence is Assumed rather than Confirmed because the presence of a Read within this FP (CG-E09-01) and a possible external validation round-trip (CG-E09-02) are not resolvable from the epic text; the 3-CFP base reflects the minimal defensible decomposition (E/W/X).

---

## E10 — Verify Caller Identity

**Epic CFP: 4 · Confidence: Assumed**

**Functional users:** Contact-centre agent (human functional user submitting caller answers and receiving the verification outcome)

### FP1 — FP1-VerifyCallerIdentity — 4 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Verification Answers | Single triggering Entry from the agent (functional user) detecting the 'verify this caller' event; starts the functional process and carries the supplied answers into the software. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Customer Master Record | Retrieving the persistent stored identity attributes to check the supplied answers against is one Read of that data group; any error indication arising from the Read adds no separate movement. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Verification Attempt Log | Logging the verification attempt against the customer record moves data to persistent storage = one Write. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **X** | Verification Result | The verified/failed outcome is the functional response of the process to its triggering Entry, issued to the agent as one Exit; it carries genuine result data (not merely a confirmation), so it is a distinct Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E10)

**CG-E10-01 · Measurement Gap** — The description says the agent asks the verification questions but does not state whether the system generates/presents the specific challenge questions (e.g. picks which attributes to ask) before the agent enters answers. If a separate 'request verification questions' functional process exists, it would add a triggering Entry, a Read of the customer master to determine askable attributes, and an Exit of the question set to the agent.

*Impact:* CFP swing +0 to +3. If the system merely accepts free-form answers (assumed here), only the single 4 CFP process exists. If the system supplies the questions, add one functional process of ~3 CFP (E + R + X), making the epic 7 CFP.

**CG-E10-02 · Measurement Gap** — It is ambiguous whether 'logging the verification attempt against the customer record' is a separate object of interest (Verification Attempt Log, assumed here) or an update to the Customer Master Record itself. If it is the same object already Read, it is still a distinct Write and does not change the count; but if no logging is actually persisted, the Write disappears.

*Impact:* CFP swing -1 (down to 3 CFP) only in the case that no verification attempt is persisted. Object-of-interest identity does not change the count as long as a Write occurs.

---

## E11 — Look Up Council Asset by Location

**Epic CFP: 5 · Confidence: Assumed**

**Functional users:** Agent / calling process (submits location, receives asset result) · GIS/asset service (external system, round-trip functional user)

### FP1 — FP1-LookUpAssetByLocation — 5 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Location Query | Single triggering Entry that starts the functional process on the event detected by the agent/calling functional user. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **X** | Location Query | Request leg of the external-system round-trip: the GIS/asset service is a functional user, so the outbound request is one Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 3 | **E** | Asset Details | Response leg of the round-trip: data received back from the GIS/asset functional user is one Entry, analyzed as normal regardless of whether it signals an error. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 4 | **X** | Asset Details | Exit returning the asset ownership/details and responsible team to the agent/calling functional user; same data group with different values (found vs not-council-owned) counts once. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L106-L109 |
| 5 | **X** | Lookup Status Message | One Exit accounts for all error/confirmation messages issued by the functional process (invalid address, no asset found, service unavailable). ASSUMED — epic does not explicitly state a status message. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E11)

**CG-E11-01 · Measurement Gap** — The epic does not specify error/confirmation handling (invalid address, no council asset found, GIS service unavailable) nor whether lookup results are persisted (cached or audit-logged) to storage owned by this software.

*Impact:* One error/confirmation Exit (order 5) is included as a defensible standard per primer rule 3 — ASSUMED. If no functional user status message is issued, remove 1 CFP (-> 4). If lookups are cached or audit-logged to persistent storage, add 1 Write per group (-> 6). CFP swing: 4-6.

---

## E12 — Cancel a Hard Rubbish Collection Booking

**Epic CFP: 9 · Confidence: Assumed**

**Functional users:** Call-centre agent (human user) · SMS gateway (external system)

### FP1 — FP1-LookUpBooking — 3 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Booking Search Criteria | Single triggering Entry: the agent (functional user) detects the triggering event (caller wants their booking found) and initiates the lookup process. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99 |
| 2 | **R** | Booking | Read retrieves the booking data group (window, items, status) from persistent storage. A 'booking not found' outcome is an error condition of the Read and adds no separate movement. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **X** | Booking | Exit returning the retrieved booking details to the agent (functional user) so the window and items can be confirmed with the caller; analyzed as a normal Exit. | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |

### FP2 — FP2-CancelBooking — 6 CFP

| # | Move | Data group | Note | Citation |
|---|---|---|---|---|
| 1 | **E** | Cancellation Request | Single triggering Entry for a distinct triggering event (agent commands the cancellation), separate from the earlier lookup event. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L17-L37 |
| 2 | **R** | Booking | Read retrieves the booking (including collection window/status) to validate that it exists and the window has not passed. The 'window passed'/'not found' error is reported via the single error Exit / accounted for by the Read. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 3 | **W** | Booking | Write moves the updated (cancelled) booking data group to persistent storage. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 4 | **W** | Resident Allowance | Write moves the restored allowance value for the year to persistent storage; the allowance is a distinct object of interest from the booking. | manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149 |
| 5 | **X** | SMS Confirmation | Exit issuing the confirmation message to the SMS gateway (external software functional user); modeled one-way (no consumed response). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276 |
| 6 | **X** | Agent Notification | One Exit accounts for all confirmation/error messages issued to the agent (cancellation confirmed, collection window already passed, booking not found). | manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279 |

### Measurement gaps (E12)

**CG-E12-01 · Measurement Gap** — Caller identity verification ('after the caller's identity is verified') is a stated precondition but is assumed to be delivered by dependency E06 and is therefore NOT measured here. Is identity verification in-scope for E12?

*Impact:* If in-scope, add a verify-identity functional process; if it round-trips to an external identity system it adds an Exit + Entry per primer item 1. CFP swing +2 to +4.

**CG-E12-02 · Measurement Gap** — Granularity: the lookup and the cancel are modeled as two functional processes (a query then an update) because the agent issues two distinct triggering commands. Some measurers would treat the whole agent interaction as one functional process.

*Impact:* If combined into one FP, the separate triggering Entry and the lookup Read/Exit would partially fold together. CFP swing approx -2 (9 -> 7).

**CG-E12-03 · Measurement Gap** — Restoring the free-collection allowance is modeled as a single Write. If the process must first retrieve the current allowance/usage value to compute the restored value, an additional Read is required.

*Impact:* Add 1 Read to FP2. CFP swing +1 (9 -> 10).

**CG-E12-04 · Measurement Gap** — The SMS to the caller is modeled as a one-way Exit to the SMS gateway. If the gateway returns a delivery/ack status that the functional process consumes, that is a return Entry (round-trip per primer item 1).

*Impact:* Add 1 Entry to FP2. CFP swing +1 (9 -> 10).

### Caveats & modeling choices (E12)

- Identity verification excluded as an E06 dependency (see CG-E12-01); if in-scope the count rises.
- Modeled as two functional processes (lookup query + cancel update); a single-FP interpretation lowers the count (CG-E12-02).
- 'Booking not found' and 'collection window already passed' are treated as error conditions covered by the single agent-notification Exit / the validating Read, per primer rule 3 (part-2 §3.3.4 #L265-L279), so they add no extra movements.
- SMS confirmation treated as one-way Exit and allowance restore as a single Write; both have +1 swings if a return/read is actually required (CG-E12-03, CG-E12-04).

---

## COSMIC v5.0 Movement-Pattern Primer (Salesforce delivery scope)

I have everything needed. Composing the primer.

---

## Answer

COSMIC v5.0 movement-pattern primer for Salesforce scope. Each rule is one to two sentences with an exact citation.

### 1. External-system round-trip (call another piece of software, receive response)
The external system is a functional user; the request out is one **Exit** and the response back in is one **Entry** (2 movements), analyzed as normal Exits/Entries regardless of whether the response signals an error.
> "All other data, issued or received by the software being measured, to/from its hardware or software functional users should be analyzed according to the FUR as Exits or Entries respectively, according to the normal COSMIC rules, regardless of whether or not the data values indicate an error condition." — [part-2 §3.3.4, GUIDANCE on Rules 16-19] (manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L273-L276)

### 2. CRUD on a persistent object of interest
Reading persistent data = one **Read** per data group; creating or updating persistent data = one **Write**; deleting = a single **Write**. (Entry to receive the request and Exit to return results are counted separately per that FP.)
> "A Read shall: a) retrieve a single data group from persistent storage… A Write shall: a) move data attributes from a single data group to persistent storage… RULE 20: Write – Delete. A requirement to delete a data group from persistent storage shall be a single Write data movement." — [part-1 §4.5, Rules 18–20] (manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L134-L149)

### 3. Confirmation and error messages back to the user
All confirmation/error messages a functional process can issue collapse into **one Exit**; only genuinely additional data in a message counts as a further Exit, and error indications arising from a Read/Write add no movement.
> "One Exit is identified to account for all types of error/confirmation messages issued by any one functional process… If a message… provides data in addition to confirming… this additional data is identified as a separate data group moved by an Exit… Reads and Writes are considered to account for any associated reporting of error conditions." — [part-2 §3.3.4, GUIDANCE on Rules 16-19] (manuals-indexed/part-2-mm-guidelines-v5-0-sep-2024/03-the-mapping-phase.md#L265-L279)

### 4. What makes two functional processes DISTINCT vs one
A functional process is defined by its **triggering event** detected by a **functional user**; a different triggering event (which cannot be sub-divided) initiated by a functional user is a different functional process.
> "be initiated by an Entry data movement from a functional user informing the functional process that it has detected a triggering event… NOTE 3: In a set of FUR, each event which causes a functional user to trigger a functional process cannot be sub-divided… has either happened or it has not happened." — [part-1 §4.2, Rule 10] (manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L17-L37)

### 5. Single triggering Entry; all responses belong to one FP
Exactly one **triggering Entry** starts a functional process, and that process comprises the set of all data movements needed to meet its FUR for every possible response to that Entry.
> "RULE 13: Functional Process – Single Entry. For any one functional process, a single Entry data movement shall be identified and counted…" plus "'the set of all data movements that is needed to meet its FUR for all the possible responses to its triggering Entry'." — [part-1 §4.2/4.4, Rule 10 NOTE 1 & Rule 13] (manuals-indexed/part-1-mm-principles-definitions-rules-v5-0-aug-2021/04-mapping-phase.md#L24-L99)

## Caveats
- No dedicated worked example for federated SSO/API round-trips exists in the indexed manuals; item 1 is derived from the general functional-user Exit/Entry rule (part-2 §3.3.4 point c), not a Salesforce-specific case.
- Every movement type occurring multiple times with different values still counts once per type (Rule 15, part-1 #L106-L109).
- Indexed corpus is Parts 1, 2, and 3c only; domain guidelines (SOA, business apps) are not indexed.
