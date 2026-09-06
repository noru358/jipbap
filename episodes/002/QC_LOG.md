# Episode 002 QC log

## S01

User verdict: PASS.

Lock:
- S01 = APPROVED_LOCKED
- S01 may not be regenerated unless user explicitly invalidates approval.

## Structural defect discovered after S01

### Defect A — approved anchor role leakage

Symptom:
- S02 attempts repeatedly reproduced S01-like full-table composition and pre-meal pose.

Root cause:
- S01 continuity anchor was effectively allowed to influence composition/action like an edit target.
- no machine-readable render cursor prevented accidental return to S01 semantics.

Fix:
- reference role separation: STYLE_AUTHORITY / CONTINUITY_ANCHOR / EDIT_TARGET
- S01 continuity anchor: is_edit_target=false
- explicit episodes/002/RENDER_STATE.json
- retry_scope=CURRENT_SHOT_ONLY
- approved locked shots cannot be regenerated

### Defect B — cuisine label under-specification

Symptom:
- Japanese-style horizontal chopstick placement / chopstick-rest visual grammar
- palms-together pre-meal gesture
- earlier Japanese-adjacent soup/rolled-egg conventions

Root cause:
- Korean-home-meal classification did not compile utensil placement, table topology and body/hand gesture into render constraints.
- renderer filled the unspecified space using generic East-Asian/Japanese visual priors.

Fix:
- MEAL_CONTEXT_SYSTEM v0.2 adds dining grammar
- QC checks utensil type/material/placement and gesture grammar
- episode-specific E002 grammar compiled in episodes/002/README.md

## Rejected S02 attempts

All S02 outputs created before these structural fixes are rejected.
They are not assets and do not advance the cursor.

## Current contract

- render cursor: S02
- S01: locked
- retry: S02 only
- next user gate: complete raster set
