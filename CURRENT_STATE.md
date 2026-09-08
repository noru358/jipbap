# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: ACTIVE

## Active production state

Active episode: V1_E002
Stage: ASSEMBLY
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E002/PLAN.md

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

## V1_E002 approval state

Menu:
- 김치볶음밥 + 반숙 계란후라이

Core arc:
- intact yolk → break → partial mix → scoop with crisped edge → actual bite → second-scoop impulse

- STORYBOARD_USER_GATE: APPROVED
- BOARD_STYLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: NOT_REACHED

Accepted BOARD:
- generation id: f11550ac-4963-465e-8262-fed8052e4ef4
- SHA-256: df1c5c0d6a8c8dd6b38868c579dd4772747dc506591ec615cad007ec4dd736d9
- dimensions: 1024 × 1536
- geometry: exact 2 × 3 board
- hard-fail QC: PASS
- user approval: APPROVED

No stochastic BOARD regeneration is authorized from this point for cover/lettering/layout-only defects.

## Deterministic assembly

In progress:
1. six-cell extraction
2. 4:5 page fit
3. cover assembly as a separate design surface
4. lettering / inner-thought / speech composition
5. complete seven-page carousel inspection

## Previous episode provenance

V1_E001:
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE
- do not mutate unless explicitly reopened

V1_CAL_001:
- prior calibration provenance only
- rejected boards remain non-reference material

## Exact next action

1. Complete deterministic ASSEMBLY from the approved V1_E002 master BOARD.
2. Extract exactly six cells and fit each to 4:5 without stretching artwork.
3. Build COVER as an actual title/artwork composition, using accepted BOARD artwork only; do not regenerate BOARD art.
4. Apply the approved copy as editable/deterministic lettering layers with natural Korean line breaks and hierarchy.
5. Inspect the full seven-page carousel for cover hierarchy, font/line-break fit, text collisions, continuity, and obvious publish-blocking defects.
6. Present the completed carousel at FINAL_PUBLISH_GATE.
7. Do not add a new routine gate or hard-fail class.
