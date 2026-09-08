# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: STORYBOARD_USER_GATE

## Active production state

Active episode: V1_E001
Stage: PLAN / STORYBOARD_USER_GATE
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E001/PLAN.md

## Runtime authority

Normal boot reads only:
1. CURRENT_STATE.md
2. JIPBAP_V1_SPEC.md

Legacy asset-composition, ASSET_GAP, BODY4 Lane A/B, PERSON/FOOD foundation DAG and old calibration chains remain historical/debugging material only.

## Style authority and renderer state

Creative style authority remains:
- PERSON_STYLE_REF_1
- TARGET_LOOK_BOARD_REF_1

Raw creative references are no longer normal production renderer attachments.

Renderer-safe production carrier:
- JIPBAP_STYLE_CARRIER_V1
- status: NOT_YET_USER_LOCKED

Required carrier shape:
- exactly one person
- no food
- no text
- no panel/grid
- no story sequence
- plain/transparent minimal background
- carries only face/eye/hair/line/color/texture style information

Carrier creation remains isolated from production:
- raw references may be attached in a dedicated carrier-calibration chat;
- user approves the derived carrier there;
- do not generate an episode board in the same raw-reference chat;
- production board generation resumes using only the approved carrier.

## Controlled experiment evidence

USER-REPORTED CONTROL PASS:
- clean chat/runtime
- no reference attachment
- same kimchi-pancake one-person six-beat contract
- exact 2×3 / text-free structural result succeeded

No artifact/hash was bound from this control, so this is architecture evidence, not an accepted production BOARD.

Interpretation:
- SIX_PANEL_BOARD_FIRST remains canonical;
- the unresolved problem is style delivery / renderer reference representation;
- do not restore legacy asset-composition complexity.

## Approval/session protocol

Normal steady-state production:
1. BOOT + PLAN
2. STORYBOARD_USER_GATE
3. BOARD generation + internal hard QC
4. ASSEMBLY + FINAL
5. FINAL_PUBLISH_GATE
6. DONE

While carrier/style calibration is active, a temporary BOARD_STYLE_USER_GATE remains after BOARD generation.

Do not generate V1_E001 BOARD before explicit storyboard approval.

## Prior calibration provenance

V1_CAL_001 remains prior calibration provenance and is not the active episode.
Its rejected boards remain non-reference material.
Its kimchi-pancake story is not reused for V1_E001.

## Exact next action

1. Present and hold at V1_E001 STORYBOARD_USER_GATE.
2. Wait for explicit user storyboard approval or requested revisions.
3. Do not generate any production image or master board before approval.
4. If the storyboard is revised, update episodes/V1_E001/PLAN.md and remain at STORYBOARD_USER_GATE.
5. If approved and JIPBAP_STYLE_CARRIER_V1 is still NOT_YET_USER_LOCKED, complete the separate carrier-calibration approval flow before production BOARD generation.
6. Once the carrier is USER_LOCKED, resume V1_E001 from the saved PLAN without re-planning.
7. Attach only JIPBAP_STYLE_CARRIER_V1 once immediately before BOARD generation.
8. Generate exactly one text-free 2×3 master board and apply only V1 hard-fail QC.
9. While style calibration remains active, present that board at the temporary BOARD_STYLE_USER_GATE.
10. On board approval, continue through deterministic ASSEMBLY → FINAL and present the completed carousel at FINAL_PUBLISH_GATE.
