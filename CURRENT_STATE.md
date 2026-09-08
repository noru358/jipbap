# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Status: STYLE_CARRIER_CALIBRATION

## Active production state

Active episode: V1_CAL_001
Stage: BOARD / STYLE_CARRIER_CALIBRATION
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_CAL_001/PLAN.md
Run receipt: episodes/V1_CAL_001/RUN_RECEIPT.md

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

Carrier creation is isolated from production:
- raw references may be attached in a dedicated carrier-calibration chat;
- user approves the derived carrier there;
- do not generate an episode board in the same raw-reference chat;
- production starts in a clean chat using only the approved carrier.

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

Normal steady-state production uses one conversation with multiple turns:

1. BOOT + PLAN
2. STORYBOARD_USER_GATE
3. same chat: user approves storyboard and attaches JIPBAP_STYLE_CARRIER_V1 once
4. BOARD generation + internal hard QC
5. ASSEMBLY + FINAL
6. FINAL_PUBLISH_GATE
7. DONE

While carrier/style calibration is active, insert one temporary BOARD_STYLE_USER_GATE between 4 and 5.

A new chat is not required between these stages.
Use a new chat only for context-limit risk, observed runtime contamination, repeated stale-template behavior, or artifact/approval uncertainty.

## Current BOARD history

V1_CAL_001 has eight rejected production BOARD attempts recorded in RUN_RECEIPT.md.
Those failures remain non-reference material.

They showed semantic leakage / stale-template behavior and do not create new permanent V1 hard gates.

## Exact next action

1. Do not re-plan V1_CAL_001.
2. Create one candidate JIPBAP_STYLE_CARRIER_V1 in a dedicated carrier-calibration chat using the locked raw creative references.
3. The candidate must satisfy the content-neutral one-person carrier contract in JIPBAP_V1_SPEC.md.
4. Present the carrier for explicit user style approval.
5. On approval, store/register it as JIPBAP_STYLE_CARRIER_V1 and update this state to CARRIER_USER_LOCKED.
6. End the raw-reference calibration chat; do not create the episode BOARD there.
7. Start/resume V1_CAL_001 production in a clean chat.
8. Restore GitHub state and existing PLAN; do not re-plan.
9. Attach only JIPBAP_STYLE_CARRIER_V1 once immediately before BOARD generation.
10. Generate exactly one text-free 2×3 master board and apply only V1 hard-fail QC.
11. Because style calibration is still active, present that board at the temporary BOARD_STYLE_USER_GATE.
12. On board approval, continue in the same chat through deterministic ASSEMBLY → FINAL and present the completed carousel at FINAL_PUBLISH_GATE.
