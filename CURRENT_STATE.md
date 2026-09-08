# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: ACTIVE

## Active production state

Active episode: V1_E002
Stage: FINAL_PUBLISH_GATE
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E002/PLAN.md
Run receipt: episodes/V1_E002/RUN_RECEIPT.md

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

- STORYBOARD_USER_GATE: APPROVED
- BOARD_STYLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: PENDING

Accepted BOARD:
- generation id: f11550ac-4963-465e-8262-fed8052e4ef4
- SHA-256: df1c5c0d6a8c8dd6b38868c579dd4772747dc506591ec615cad007ec4dd736d9
- dimensions: 1024 × 1536
- hard-fail QC: PASS

## Deterministic assembly

Complete:
1. six-cell extraction
2. 4:5 page fit
3. separate cover composition
4. lettering / inner-thought / SFX composition
5. complete seven-page carousel inspection
6. cover typography deterministic repair

Final carousel ZIP SHA-256:
- 3214a3b8c7c39a4fe34fbbe9f1d0eece211a60553e14c19ea43a10fa2953637f

No stochastic BOARD regeneration is authorized for lettering/layout-only feedback.

## Previous episode provenance

V1_E001:
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE
- do not mutate unless explicitly reopened

V1_CAL_001:
- prior calibration provenance only
- rejected boards remain non-reference material

## Exact next action

1. Present the completed V1_E002 seven-page carousel at FINAL_PUBLISH_GATE.
2. Wait for explicit user publish approval.
3. If the user requests cover/lettering/layout-only changes, repair deterministically without regenerating the accepted BOARD.
4. If user approves final publish, mark V1_E002 DONE and preserve the final carousel ZIP hash in CURRENT_STATE / receipt.
5. Add no new routine gate or hard-fail class from isolated soft-quality observations.
