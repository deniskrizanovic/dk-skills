## ADDED Requirements

### Requirement: Decant check and guidance for aged wines

When the coach has assessed the wine as **old/mature** during its bottle-age adjustment, the coach SHALL, before beginning the sensory walkthrough, ask the user **how long the wine has been decanted for**, accepting "not decanted" / "poured straight from the bottle" as valid answers. The coach SHALL then provide grounded, **retrospective** guidance on how long the wine ideally should have been decanted, reasoning from the wine's age and tannic structure rather than a fixed rule: fragile older wines are typically decanted gently off their sediment with short or minimal aeration to preserve delicate tertiary aromatics, while sturdier mature wines tolerate more air. The coach SHALL compare the user's actual decant time to its recommendation and explain the likely sensory effect of the difference. The coach SHALL NOT run this check for young wines.

The guidance SHALL be framed as learning feedback, NOT a grade or quality verdict. The decant context MAY inform how the coach interprets divergence during calibration (e.g. a faded nose attributable to over-decanting rather than a missed marker) but SHALL NOT change the Perception Alignment metric.

#### Scenario: Old wine triggers the decant question before tasting

- **WHEN** the coach has assessed the wine as old/mature and is about to start the sensory walkthrough
- **THEN** the coach first asks how long the wine has been decanted (accepting "not decanted") before presenting the first grid section

#### Scenario: Retrospective guidance reasoned from age and structure

- **WHEN** the user reports how long an old wine was decanted
- **THEN** the coach states the decant approach it would have recommended for a wine of that age and structure (e.g. decant off the sediment with short aeration for a fragile old red), compares it to what the user did, and explains the likely sensory effect — as per-bottle reasoning, not a universal minute count

#### Scenario: Over-decanting explained as context, not a scored miss

- **WHEN** the user over- or under-decanted an old wine and the nose or palate reads faded or closed
- **THEN** the coach may note the decant as the likely cause when interpreting divergence at calibration, but does not lower the Perception Alignment metric on account of it

#### Scenario: Young wine skips the check

- **WHEN** the coach has assessed the wine as young rather than old/mature
- **THEN** the coach does not ask the decant question and proceeds directly to the sensory walkthrough

#### Scenario: Age cannot be confidently assessed

- **WHEN** the wine is ungrounded or the coach cannot confidently judge whether it is old/mature
- **THEN** the coach asks the user or notes that it cannot advise on decanting rather than guessing, and does not force the check
