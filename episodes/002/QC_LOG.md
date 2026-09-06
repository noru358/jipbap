# Episode 002 QC log

## S01

User verdict: PASS.
S01 = APPROVED_LOCKED.

## Defect A — anchor role leakage

Symptom:
S02 attempts fell back to S01 full-table composition.

Fix:
- reference role separation
- S01 continuity only
- S01 not edit target
- render cursor lock

## Defect B — cuisine/dining grammar under-specification

Symptom:
- Japanese-style horizontal chopstick placement
- palms-together pose
- Japanese-adjacent meal presentation

Fix:
- compiled dining grammar
- utensil/table/gesture QC
- E002-specific Korean home-meal constraints

## Defect C — whole-episode context leak

Observed after A/B structural fixes:
- generated output became a multi-panel S01~S05 page
- future-shot actions appeared
- lettering appeared
- S01 was included despite being locked

Classification:
- RENDER_CONTEXT_LEAK_FAIL
- MULTI_PANEL_FAIL
- TEXT_FREE_FAIL
- LOCKED_SHOT_REAPPEAR_FAIL

Root cause:
- renderer input inherited full episode/storyboard/voice context instead of current S02 capsule.

Fix:
- current-shot render capsule
- future-shot/voice/rejected-output denylist
- locked-shot edit target denylist
- fail-closed when execution context cannot isolate render input

Disposition:
- all post-S01 failed outputs rejected
- none are assets
- none may be future references
- S01 remains approved/locked
- cursor remains S02
