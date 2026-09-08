# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: V1_SPEC_FROZEN

## Active production state

Active episode: V1_CAL_001
Stage: BOARD
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_CAL_001/PLAN.md
Run receipt: episodes/V1_CAL_001/RUN_RECEIPT.md

## Locked references

- Primary PERSON style authority: PERSON_STYLE_REF_1
- Auxiliary target-look anchor: TARGET_LOOK_BOARD_REF_1
- Existing validated reference-byte provenance remains preserved.
- Prior failed PERSON candidates remain non-reference material.
- Rejected V1_CAL_001 board attempts are non-reference material.

## Runtime authority

Normal boot reads only:
1. CURRENT_STATE.md
2. JIPBAP_V1_SPEC.md

Read specific reference manifests only when reference bytes must actually be materialized/dispatched.

Legacy protocol, calibration, BODY4 asset-composition, ASSET_GAP, foundation-DAG and Lane A/B documents are historical/debugging references only.
They do not own runtime next action.

AutoPipeline pin parity is not a jipbap creative/runtime boot gate under V1.

## Retired current work

The prior exact-next-action chain beginning with FOOD_EGG_RICE_INTACT_V2 regeneration and deterministic PERSON+FOOD S01 composition is RETIRED.
Do not resume it.

## Current BOARD checkpoint

V1_CAL_001 PLAN is complete for a six-beat kimchi-pancake episode.

The image runtime has produced eight rejected candidates.
All eight triggered V1 hard FAIL because they introduced generated text and/or substituted wrong menu, group-story, cover, reference-layout or other non-authoritative content instead of the planned text-free kimchi-pancake 2×3 BODY board.

This is recorded as an execution/runtime failure, not a new permanent V1 gate or architecture rule.

## Exact next action

Resume V1_CAL_001 at BOARD only:
1. do not re-plan the episode;
2. use the six beats and continuity contract already stored in episodes/V1_CAL_001/PLAN.md;
3. in a clean image-runtime context, generate exactly one BODY-only, text-free, equal-cell 2 columns × 3 rows master board for the planned kimchi-pancake episode;
4. bind locked reference media only for their allowed visual influence; TARGET_LOOK_BOARD_REF_1 menu/text/layout remain non-authoritative;
5. do not use any rejected V1_CAL_001 candidate as a reference, continuity source or repair source;
6. apply only JIPBAP_V1 hard-fail QC;
7. on PASS, continue without routine approval through ASSEMBLY → FINAL;
8. deterministically export COVER + six 4:5 BODY pages with lettering;
9. present only the completed carousel for the single user publish gate;
10. append generation-call count, human intervention points, first-pass publishability and rework loops to episodes/V1_CAL_001/RUN_RECEIPT.md.
