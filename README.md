# jipbap

짧은 집밥/음식 감상형 인스타툰 제작 프로젝트.

## Canonical V1

Architecture: **SIX_PANEL_BOARD_FIRST**

Normal boot authority:
1. `runtime/state.json` (single machine authority)
2. generated `runtime/RUN_CONTEXT.md`
3. `JIPBAP_V1_SPEC.md`

Product:
- COVER 1 + BODY 6
- one text-free 2×3 BODY master board
- style/format frozen, staging/storytelling fluid
- actual-boundary extraction + 4:5 FIT without artwork stretch
- quality-first `PRESENTATION_MASTER_DRAFT` before editable reconstruction
- approved artwork/copy preserved into `EDITABLE_COMPOSITION_PACKAGE_V1`
- minimal publish-blocking hard QC

## Normal production conversation

One episode is normally produced in **one ChatGPT conversation across multiple turns**, not one giant response:

`BOOT + PLAN → storyboard approval → same chat BOARD → COVER/EXTRACT/FIT → PRESENTATION_MASTER_DRAFT → publish approval → EDITABLE_RECONSTRUCTION/PARITY_QC`

The storyboard approval is permanent.
The BOARD/style approval exists only while style-carrier calibration is active and should disappear after style delivery becomes stable.

A new chat is used only for real runtime contamination, conversation/context-limit risk, or artifact/approval uncertainty.

## Planning input

A food name alone is sufficient to start a new PLAN.
Situation, remembered sensation, actual words, unexpected detail or a small choice are optional enrichment, not a required questionnaire.

Planning keeps user-provided experience/copy distinct from AI-filled connective assumptions.
Storyboard design may include approximate copy-space, protected face/hand/food regions and text reading order, while final coordinates remain presentation-stage data.
The generated 2×3 BOARD stays text-free.

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

## Extraction and ToonDesk handoff

- `pipeline.extract_board` detects actual 2×3 panel boundaries; it does not use nominal equal slicing.
- one `JIPBAP_BOARD_EXTRACTION_V1` metadata record owns source SHA, detected boxes and S01..S06 extracted-output hashes.
- BODY scene `artwork_provenance` references that extraction metadata + box index.
- final 4:5 FIT remains the artwork object's scene `crop`; no second crop manifest is introduced.
- ToonDesk consumes the project profile but is not JIPBAP authority.
- same-ID reconstruction preserves only properties explicitly marked in `manual_overrides`.
- manual line breaks, bubble/tail geometry, typography and artwork source remain inspectable/editable scene data.
- missing font substitution is surfaced rather than silently accepted.

Legacy composition-first / BODY4 / ASSET_GAP / PERSON-FOOD foundation workflows are historical/debugging material only.

See `JIPBAP_V1_SPEC.md` for the frozen/unfrozen boundary and runtime protocol.
See `RUNTIME_IMPLEMENTATION.md` for the Chat host boundary, exact approval
contract, asset persistence and recovery behavior.
