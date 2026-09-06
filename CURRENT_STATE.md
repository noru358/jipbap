# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

episodes/002/README.md

Episode 001 remains paused at PREPRODUCTION_RECOMPILE.

## Episode 002 current stage

S02_RENDER_BLOCKED_INTERNAL_QC

Approved:
- preproduction package
- S01 visual style
- corrected S01 Korean meal-context presentation
- S01 as Episode 002 continuity anchor

## Canonical structural learning

Cross-cuisine contamination is handled through MEAL_CONTEXT_SYSTEM.md:
- episode-level meal-context compile
- shot-level meal-context binding
- context QC for preparation form, vessel/material, ingredients/garnish and table ecology
- no cuisine-specific one-off rule is promoted globally

## Reference state for current session

STYLE_REF_001:
- actual binary available
- SHA-256 verified against manifest

Episode 002 S01 approved anchor:
- actual binary available in current session
- SHA-256: cec9a1be2077772369e89098a9553d67b9ba028b6c5c5448f9ac8f44d1814050
- user verdict: PASS
- repository binary still not materialized

## S02 renderer blocker

The S02 contract requires a text-free food macro showing chopsticks opening the mackerel skin and exposing flesh.

Repeated internal attempts failed because the renderer kept returning S01-like full-table scenes, omitted the required action, included character-dominant framing, and generated text.

All such attempts are rejected and are not episode assets.

See:
- episodes/002/QC_LOG.md

## Exact next action

1. Retry S02 using a rendering route/context that can honor the approved shot contract.
2. Require single-panel + text-free + food-macro + explicit pry-open action.
3. Run structural + visual + meal-context + food-state QC.
4. Only after S02 PASS, continue S03 → S05 internally.
5. Present the complete S01~S05 text-free raster set at the next user gate.
