# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

episodes/002/README.md

Episode 001 remains paused at PREPRODUCTION_RECOMPILE.

## Episode 002 current stage

REMAINING_RENDER_INTERNAL_QC

Approved:
- preproduction package
- S01 visual style
- corrected S01 Korean meal-context presentation
- S01 as Episode 002 continuity anchor

## Structural learning now canonical

S01 exposed a cross-cuisine contamination failure:
a Korean home-meal scene can drift into visually similar foreign meal conventions even when the main dish is correct.

This is now handled structurally through:
- MEAL_CONTEXT_SYSTEM.md
- meal-context compile in preproduction
- meal-context binding in each shot contract
- meal-context QC in remaining render
- meal_context required by schemas/shot_contract.schema.json

No global hardcoded rule such as all Korean soup must use X is introduced.
Each episode compiles its own cuisine/meal-setting constraints.

## Reference state for current session

STYLE_REF_001:
- actual binary available
- SHA-256 verified against manifest

Episode 002 S01 approved anchor:
- actual binary available in current session
- SHA-256: cec9a1be2077772369e89098a9553d67b9ba028b6c5c5448f9ac8f44d1814050
- user verdict: PASS
- repository binary still not materialized

## Exact next action

1. Generate S02 single-panel / text-free using style ref + S01 anchor.
2. Internal QC: structural + visual + meal-context + food-state.
3. Continue S03, S04, S05 with the same procedure.
4. When all four PASS, present the full S01~S05 text-free raster set to the user.
5. Await raster-set gate before lettering.
