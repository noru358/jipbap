# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: DONE

## Active production state

Active episode: V1_E001
Stage: DONE
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E001/PLAN.md
Run receipt: episodes/V1_E001/RUN_RECEIPT.md

## Runtime authority

Normal boot reads only:
1. CURRENT_STATE.md
2. JIPBAP_V1_SPEC.md

Legacy asset-composition, ASSET_GAP, BODY4 Lane A/B, PERSON/FOOD foundation DAG and old calibration chains remain historical/debugging material only.

## Style authority and renderer state

Creative style authority:
- PERSON_STYLE_REF_1
- TARGET_LOOK_BOARD_REF_1

Renderer-safe production carrier:
- JIPBAP_STYLE_CARRIER_V1
- status: USER_LOCKED
- approved session-source SHA-256: 43e791e8ebb1389fb7c469786f76fe118bcb96182d7c06e080d9088fb4057a80
- dimensions: 583 × 622
- repository registry: assets/reference_registry.json
- repository binary materialization: NOT_COMPLETED_IN_THIS_RUNTIME
- current permitted binding until materialization: same approved image as SESSION_ONLY fallback

The carrier is style-delivery authority only and does not own menu, staging, camera, layout, story or copy.

## V1_E001 approval state

- STORYBOARD_USER_GATE: APPROVED
- BOARD_STYLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE

Accepted BOARD:
- generation id: 3c20747b-7e9c-421c-8a00-1c4b5b481139
- SHA-256: 59740618ec87d67acc0c5e1ac53a1705d585258e0228d16122fa99a8a50084f1
- hard-fail QC: PASS

User-requested BOARD corrections that were applied before approval:
1. stronger camera/composition/expression variety
2. S05 shows pork already on lettuce while sliced garlic is being added
3. FOOD rendering reduced away from photorealism toward the PERSON's illustrated medium

## Deterministic assembly

Complete:
1. six-cell extraction
2. 4:5 page fit
3. cover assembly
4. lettering / inner-thought / speech composition
5. final seven-page export

Final carousel ZIP SHA-256:
- 2f701ceb3e6044962cd8d6d4438d9d89268ad988bba4500854b6c7767f9b4da5

No stochastic BOARD regeneration is authorized for lettering/layout-only feedback.

## Prior calibration provenance

V1_CAL_001 remains prior calibration provenance and is not the active episode.
Its rejected boards remain non-reference material.
Its kimchi-pancake story is not reused for V1_E001.

## Exact next action

1. V1_E001 is complete. Do not mutate it unless the user explicitly reopens it.
2. On the next new-episode request, boot from latest main and create a fresh PLAN under JIPBAP_V1_SPEC.md.
3. Preserve SIX_PANEL_BOARD_FIRST, the locked style authority, and the single-carrier production rule.
4. Do not promote isolated soft-quality observations from V1_E001 into new permanent hard gates.
