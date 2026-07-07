## ADDED Requirements

### Requirement: Perception alignment metric

The coach SHALL compute a per-session **Perception Alignment** metric that measures, of the **high-confidence** expected markers, how many the taster registered. A marker SHALL be counted toward the metric ONLY IF the expectation for that attribute is high-confidence — i.e. the winery tech sheet and the grape/region/vintage style archetype **agree** on it. Attributes that are divergent, atypical, low-confidence, or ungrounded SHALL be **excluded** from both the numerator and the denominator and SHALL remain purely qualitative. The metric is a calibration mirror (the taster versus their own past sessions), NOT a grade of the taster and NOT a quality verdict on the session or the wine.

The coach SHALL apply an **honesty guardrail**: reporting a note the expectation did not predict, contradicting an expectation that proves wrong for this bottle, or flagging the bottle as flawed/atypical SHALL NEVER lower the metric. Honest divergence is neutral information, not a miss.

#### Scenario: Only high-confidence markers are counted

- **WHEN** the coach computes the alignment metric for a session
- **THEN** the denominator includes only attributes where the tech sheet and style archetype agree, and divergent, atypical, low-confidence, or ungrounded attributes are excluded from both numerator and denominator

#### Scenario: Honest divergence never lowers the metric

- **WHEN** the taster reports a note the expectation missed, contradicts an expectation that is wrong for this bottle, or flags the bottle as off/atypical
- **THEN** the metric is not reduced as a result, and the divergence is recorded qualitatively rather than scored as a miss

#### Scenario: Atypical bottle excludes its divergent attributes from the score

- **WHEN** the cross-check flagged the bottle as diverging from its style archetype on certain attributes
- **THEN** those attributes are excluded from the alignment metric and remain qualitative notes, so a correct palate on an atypical bottle is not penalised

## MODIFIED Requirements

### Requirement: Calibration feedback at close

At the end of a session the coach SHALL provide a short calibration comparison between the user's captured notes and the expected profile, framed as learning feedback (what lined up, what was missed, what to focus on next). The coach MAY accompany this with the Perception Alignment metric, but MUST NOT assign a grade of the taster, a letter grade, or a pass/fail verdict on the session. When the coach shows the alignment metric, it SHALL present it **alongside** the qualitative Matched/Missed/Focus-next feedback (not as a replacement) and **paired with its trend across recent sessions**, so the number reads as a calibration mirror rather than a standalone verdict.

#### Scenario: Notes compared to expectation

- **WHEN** the walkthrough is complete
- **THEN** the coach summarises where the user's notes matched the expected profile, where they diverged, and offers one or two concrete focus points for next time

#### Scenario: Metric shown as a calibration mirror, not a grade

- **WHEN** the coach shows the Perception Alignment metric at the close of a session
- **THEN** it presents the metric alongside the qualitative Matched/Missed/Focus-next feedback and paired with the trend across recent sessions, and does not assign a letter grade, pass/fail verdict, or any judgement of the taster
