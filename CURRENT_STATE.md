# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

episodes/002/README.md

## Episode 002 state

Stage: POST_S01_INTERNAL_RENDER
Render cursor: S02
Approved locked shots: S01
Retry scope: CURRENT_SHOT_ONLY
Next user gate: RASTER_SET

## Confirmed structural failures and fixes

### A. Approved S01 was effectively regenerated

Cause:
- anchor/edit-target role leakage
- render cursor not enforced at generation boundary

Fix:
- S01 APPROVED_LOCKED
- S01 CONTINUITY_ANCHOR only
- S01 is_edit_target=false
- explicit render cursor
- current-shot-only retry

### B. Korean meal drifted into Japanese visual grammar

Cause:
- cuisine label without compiled dining grammar

Fix:
- MEAL_CONTEXT_SYSTEM v0.2
- utensil material/type/placement
- table topology
- hand/gesture grammar
- cross-context contamination QC

E002 compiled grammar:
- Korean metal spoon + chopsticks
- right-side placement; no Japanese horizontal chopstick-rest staging
- no palms-together pre-meal pose
- current food action controls hand pose

### C. Whole-episode render/context leak

Observed:
- renderer generated multi-panel S01~S05 page
- future-shot actions and lettering appeared in a supposed S02 render

Fix:
- current-shot render capsule
- allowlist only current shot + minimal continuity + style + relevant meal grammar
- deny future shots, voice copy, rejected outputs, locked-shot edit targets
- multi-shot output = RENDER_CONTEXT_LEAK_FAIL

Canonical:
- PRODUCTION_PROTOCOL.md v0.4
- VISUAL_SYSTEM.md v0.3
- schemas/shot_contract.schema.json

## Current execution blocker

The clean continuation context successfully restored GitHub state, so the previous whole-episode-context blocker is no longer presumed active.

However, required image binaries are not materialized in GitHub and are not bound to the renderer in the current execution context.

Current blocker:
REFERENCE_BINDING_REQUIRED_FOR_E002_S02

This does NOT reset the episode.

Persisted state remains:
- S01 PASS/LOCKED
- cursor S02
- next user gate RASTER_SET

## Exact next action

Bind the actual STYLE_REF_001 image in the current render context.
Bind the approved E002 S01 anchor when continuity pixels are needed; otherwise use only extracted continuity facts.
Then render S02 only from its isolated capsule.
After S02 PASS, auto-advance S03 → S04 → S05.
Do not recreate S01.
