# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

episodes/002/README.md

Episode 001 remains paused.

## Episode 002 render state

Stage: POST_S01_INTERNAL_RENDER
Render cursor: S02
Approved locked shots: S01
Retry scope: CURRENT_SHOT_ONLY
Next user gate: RASTER_SET

Machine state:
- episodes/002/RENDER_STATE.json

## User-approved facts

- Episode 002 preproduction: PASS
- corrected S01 visual/cultural result: PASS
- S01 is immutable unless the user explicitly withdraws approval

## Structural corrections applied

### 1. S01 regeneration bug

Root cause:
- continuity anchor and edit target roles were not separated
- render cursor was not machine-explicit

Fix:
- approved-shot immutability
- explicit render cursor
- current-shot-only retry
- reference-role isolation
- S01 continuity anchor cannot be S02 edit target

Canonical:
- PRODUCTION_PROTOCOL.md
- VISUAL_SYSTEM.md
- schemas/render_state.schema.json
- episodes/002/RENDER_STATE.json

### 2. Cross-cuisine dining-grammar drift

Root cause:
- cuisine label existed, but utensil placement / table topology / gesture grammar were not compiled
- renderer filled the missing detail using generic East-Asian/Japanese visual priors

Fix:
- MEAL_CONTEXT_SYSTEM v0.2 compiles dining grammar
- shot QC now includes utensil type/material/placement + hand/gesture rules
- E002 explicitly compiles Korean-home-dinner grammar without making those details global project rules

## Current E002 dining grammar

- Korean spoon + chopsticks, metal default for this episode
- spoon/chopsticks at diner’s right side; no Japanese horizontal chopstick-rest staging
- no palms-together pre-meal pose as default
- hands must perform the current shot action or rest naturally
- individual rice/soup + Korean home-table shared main/sides
- reject Japanese miso-bowl / garnish / rolled-egg / utensil-layout contamination

## Exact next action

Render S02 only under the new state and reference-role isolation.
Do not regenerate S01.
On S02 PASS, auto-advance to S03, then S04, then S05.
Next user-facing approval is the complete text-free raster set.
