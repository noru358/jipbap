# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: ACTIVE

## Active production state

Active episode: V1_E002
Stage: STORYBOARD_USER_GATE
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

## V1_E002 storyboard state

Menu:
- 김치볶음밥 + 반숙 계란후라이

Core arc:
- intact yolk → break → partial mix → scoop with crisped edge → actual bite → second-scoop impulse

Refinement goals exercised in PLAN:
1. community / real-person cadence rather than polished script prose
2. concrete bite-level sensory wording
3. varied but non-mechanical camera / expression rhythm
4. cover treated as a separate design surface

Approval:
- STORYBOARD_USER_GATE: PENDING
- BOARD_STYLE_USER_GATE: NOT_APPLICABLE_UNTIL_BOARD
- FINAL_PUBLISH_GATE: NOT_REACHED

No BOARD generation is authorized before storyboard approval.

## Previous episode provenance

V1_E001:
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE
- do not mutate unless explicitly reopened

V1_CAL_001:
- prior calibration provenance only
- rejected boards remain non-reference material

## Exact next action

1. Present `episodes/V1_E002/PLAN.md` for STORYBOARD_USER_GATE.
2. Wait for the user's storyboard review.
3. Do not generate images, master BOARD, crop pages, cover artwork, or lettering before approval.
4. If approved, continue in the same chat to BOARD using only the locked `JIPBAP_STYLE_CARRIER_V1` as the production runtime carrier.
5. Preserve SIX_PANEL_BOARD_FIRST, the locked style authority, and the single-carrier production rule.
6. Add no new routine approval gate or hard-fail class from isolated soft-quality observations.
