# jipbap

짧은 집밥/음식 감상형 인스타툰 제작 프로젝트.

## Canonical V1

Architecture: **SIX_PANEL_BOARD_FIRST**

Normal boot authority:
1. `CURRENT_STATE.md`
2. `JIPBAP_V1_SPEC.md`

Product:
- COVER 1 + BODY 6
- one text-free 2×3 BODY master board
- style/format frozen, staging/storytelling fluid
- deterministic extraction / 4:5 assembly / cover / lettering
- minimal publish-blocking hard QC

## Normal production conversation

One episode is normally produced in **one ChatGPT conversation across multiple turns**, not one giant response:

`BOOT + PLAN → storyboard approval → same chat BOARD → ASSEMBLY/FINAL → publish approval`

The storyboard approval is permanent.
The BOARD/style approval exists only while style-carrier calibration is active and should disappear after style delivery becomes stable.

A new chat is used only for real runtime contamination, conversation/context-limit risk, or artifact/approval uncertainty.

## Style references and attachment policy

Creative style authority:
- `PERSON_STYLE_REF_1`
- `TARGET_LOOK_BOARD_REF_1`

Raw creative references are not normal production renderer attachments.

Production uses an approved content-neutral runtime projection:
- `JIPBAP_STYLE_CARRIER_V1`

Carrier requirements:
- exactly one person
- no food
- no text
- no panel/grid
- no narrative sequence
- minimal/transparent background

Carrier creation is a one-time/separate calibration task using the raw references.
Do not create a production board in that same raw-reference chat.

Normal episode flow:
1. start with no image attachment and review PLAN;
2. when approving the storyboard, attach only `JIPBAP_STYLE_CARRIER_V1` once;
3. continue BOARD → FINAL in that same chat.

## Fixed creative idea

`PROXY_EATER`: the comic eats on the reader's behalf.
Food state, eating action and sensory payoff are central.
Background/decorative assets are omitted unless needed to explain the moment.

Legacy composition-first / BODY4 / ASSET_GAP / PERSON-FOOD foundation workflows are historical/debugging material only.

See `JIPBAP_V1_SPEC.md` for the frozen/unfrozen boundary and runtime protocol.
