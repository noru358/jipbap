# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Presentation architecture: EDITABLE_COMPOSITION_PACKAGE_V1
Editor scene model: EDITOR_SCENE_MODEL_V1_BASELINE
Presentation shell: JIPBAP_PRESENTATION_SHELL_V1
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

## V1 frozen presentation shell

Template:
- templates/JIPBAP_PRESENTATION_SHELL_V1.json

BODY:
- canvas: 1080 × 1350
- artwork frame: x=40, y=175, 1000 × 1000
- frame is fixed across S01–S06
- no artwork stretch/aspect distortion
- no publish page numbers/internal episode markers

COVER:
- title safe region: x=60..1020, y=50..300
- hero frame: x=60, y=330, 960 × 960
- default grammar: menu tag + dominant title + hero artwork
- subtitle/deck omitted by default
- no hero artwork squeezing/stretching to fit copy

Lettering semantics:
- speech: white bubble + dark outline + tail
- inner thought: tail-free warm off-white thought box + muted outline
- SFX: independent editable text/SFX object

The shell freezes presentation geometry only. Story staging/camera/pose/expression remain fluid inside BOARD generation.

## Editor architecture checkpoint

Midpoint decision recorded:
- `composition/*.layout.json` is the shared scene model for current Chat deterministic rendering and the future first-party Canva-like editor.
- Canva itself is not a production dependency and no Canva/PPTX/PDF format becomes authority.
- current Chat mode remains able to complete BOARD → scene/layout JSON → deterministic render → PNG without the future editor.
- future API/editor may manipulate the same scene objects through selection, drag, resize, rotation, text edit, crop, z-order and grouping.
- minimum scene support now includes stable ids, geometry, rotation, z-index, visibility/lock state, optional grouping and artwork crop metadata.
- SVG remains an interchange/debug derivative; PNG remains a publish derivative.
- no new user gate or BOARD hard-fail class is added by this editor architecture.

Deferred intentionally:
- final COVER object/group structure
- final BODY object/group structure
- lock defaults
- frame/crop interaction rules
- typography-role presets
- text-placement freedom/defaults

The existing frozen COVER/BODY shell remains in force until that dedicated redesign pass is approved.

## V1_E002 approval state

- STORYBOARD_USER_GATE: APPROVED
- BOARD_STYLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: PROVISIONALLY_APPROVED_FEEDBACK_PENDING

Accepted BOARD:
- generation id: f11550ac-4963-465e-8262-fed8052e4ef4
- SHA-256: df1c5c0d6a8c8dd6b38868c579dd4772747dc506591ec615cad007ec4dd736d9
- dimensions: 1024 × 1536
- hard-fail QC: PASS

## V1_E002 deterministic retrofit

Applied without BOARD regeneration:
1. fixed BODY frame across all six pages
2. fixed COVER title/hero shell
3. removed artwork aspect distortion
4. removed page markers
5. compressed mobile copy
6. made speech / inner-thought / SFX visually distinct
7. kept S05 artwork unchanged per user decision

Accepted content feedback:
- shorter natural copy: APPLIED
- speech/thought visual distinction: APPLIED
- less glossy/ad-like FOOD on future BOARD runs: ACCEPTED, use existing FOOD spec more strictly
- additional S05 artwork-payoff intervention: DEFERRED

Presentation authority:
- episodes/V1_E002/composition/*.layout.json
- template_id: JIPBAP_PRESENTATION_SHELL_V1

Current runtime package ZIP SHA-256:
- 29ca16ead377b2cf63d7653cfcfd633ef380e4b1979d57c59c5653a4d4278ecc

Current flattened carousel ZIP SHA-256:
- 12b1fe0d0e13cee8bb72b94ec36300776dba9686f2115f3c27fdc8351ba0b418

No stochastic BOARD regeneration is authorized for presentation-only feedback.

## Previous episode provenance

V1_E001:
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE
- do not mutate unless explicitly reopened

V1_CAL_001:
- prior calibration provenance only
- rejected boards remain non-reference material

## Exact next action

1. In the next clean design session, continue from `EDITOR_SCENE_MODEL_V1_BASELINE` and redesign/freeze the editor-facing COVER and BODY scene structure.
2. Decide only the presentation-layer details still deferred: object/group hierarchy, lock defaults, artwork frame/crop interaction, typography roles and default placement freedom.
3. Preserve the current Chat-mode path: BOARD → scene/layout JSON → deterministic renderer → PNG must remain fully functional without any API editor.
4. Do not introduce Canva, PPTX or another external format as production authority.
5. Until the redesign is approved, keep `JIPBAP_PRESENTATION_SHELL_V1` geometry unchanged and do not regenerate the accepted V1_E002 BOARD for presentation-only work.
6. After the presentation-shell redesign checkpoint is resolved, return to V1_E002 `FINAL_PUBLISH_GATE`; layout-only changes mutate scene/layout JSON and deterministic derivatives only.
7. Keep FOOD gloss as a soft next-BOARD direction and keep the proposed S05 artwork-payoff change deferred unless explicitly reopened.
