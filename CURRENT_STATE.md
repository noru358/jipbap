# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Presentation architecture: EDITABLE_COMPOSITION_PACKAGE_V1
Editor scene model: EDITOR_SCENE_MODEL_V1_BASELINE
Default presentation shell for new episodes: JIPBAP_PRESENTATION_SHELL_V2
Status: DONE

## Active production state

Active episode: V1_E002
Stage: DONE
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

## Presentation shell versioning

Completed episode provenance:
- V1_E001 / V1_E002 remain on `JIPBAP_PRESENTATION_SHELL_V1`.
- Do not mutate their layout solely because the project default changed.

Default for new episodes:
- template: `templates/JIPBAP_PRESENTATION_SHELL_V2.json`
- canvas: 1080 × 1350
- COVER: title/header x=60,y=40,w=960,h=240 + hero x=40,y=310,w=1000,h=1000
- BODY: artwork x=40,y=40,w=1000,h=1000 + lower meta x=60,y=1080,w=960,h=230
- speech / SFX default inside artwork
- inner thought / narration default inside meta
- artwork starts locked in automatic Chat production
- explicit editor unlock / frame transform / page-structure change is allowed and classified as `CUSTOM_OVERRIDE`, not corruption

The presentation shell is a project default profile. The editor engine may expose broader capabilities without changing JIPBAP's automatic production defaults.

## Editor architecture checkpoint

Midpoint decision recorded:
- `composition/*.layout.json` is the shared scene model for current Chat deterministic rendering and the future first-party Canva-like editor.
- Canva itself is not a production dependency and no Canva/PPTX/PDF format becomes authority.
- current Chat mode remains able to complete BOARD → scene/layout JSON → deterministic render → PNG without the future editor.
- future API/editor may manipulate the same scene objects through selection, drag, resize, rotation, text edit, crop, z-order and grouping.
- minimum scene support now includes stable ids, geometry, rotation, z-index, visibility/lock state, optional grouping and artwork crop metadata.
- SVG remains an interchange/debug derivative; PNG remains a publish derivative.
- no new user gate or BOARD hard-fail class is added by this editor architecture.

Resolved and frozen in this design pass:
- shared four-layer scene stack: background → artwork → lettering → overlay
- COVER hierarchy: fixed top-level layers with menu-tag/title lettering groups
- BODY hierarchy: fixed top-level layers with fluid speech/thought/narration/SFX instance groups
- background and artwork-frame lock defaults for automatic production
- editor capability remains broader: explicit unlock may move/resize/rotate artwork frames and is recorded as CUSTOM_OVERRIDE
- crop editing remains available without changing source artwork bytes
- semantic typography-role presets
- V2 BODY semantic placement defaults: speech/SFX inside artwork; inner-thought/narration in lower meta region
- page add/delete/duplicate/type-change remain editor capabilities rather than being deleted for JIPBAP
- flat objects[] retained for Chat renderer compatibility; groups[] carries future editor semantics

Schema:
- schemas/editor_scene_model_v1.schema.json

JIPBAP_PRESENTATION_SHELL_V1 remains unchanged for completed episodes. New automatic episodes instantiate JIPBAP_PRESENTATION_SHELL_V2.

## V1_E002 approval state

- STORYBOARD_USER_GATE: APPROVED
- BOARD_STYLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: APPROVED

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

## Generic editor boundary

- Generic editor implementation repository: `noru358/Toondesk`.
- ToonDesk is a separate generic editor/renderer capability surface, not JIPBAP canonical authority.
- JIPBAP owns its project profile/default shell; ToonDesk consumes it.
- Canonical JIPBAP profile: `templates/JIPBAP_PRESENTATION_SHELL_V2.json`.
- Any `profiles/jipbap_v2.example.json` copy in ToonDesk is a non-authoritative development/example mirror only.
- ToonDesk transport/session wrappers (`TOONDESK_PACKAGE_V1`, `TOONDESK_PROJECT_V1`) are non-authoritative. `composition/*.layout.json` remains the JIPBAP presentation authority.
- ToonDesk may report explicit profile deviations as `CUSTOM_OVERRIDE`; this is not corruption and does not change scene-format authority.
- Automatic Chat production does not invent per-episode custom overrides. Overrides require explicit user/editor action.

## Exact next action

1. V1_E002 is complete. Do not mutate it unless the user explicitly reopens it.
2. Preserve `EDITOR_SCENE_MODEL_V1`, the four-layer COVER/BODY hierarchy, and `EDITABLE_COMPOSITION_PACKAGE_V1`; instantiate `JIPBAP_PRESENTATION_SHELL_V2` as the default profile for subsequent new episodes while preserving V1 shell provenance for completed episodes.
3. On the next new-episode request, boot from latest main and create a fresh PLAN under the current JIPBAP_V1_SPEC.md.
4. Keep copy concise and natural on mobile; prefer one short reaction plus at most one concrete sensory observation per beat.
5. Keep speech / inner-thought / SFX visually distinct through the frozen semantic lettering roles.
6. Apply the existing FOOD spec more strictly so FOOD remains appetizing but less glossy / ad-like; this remains a soft quality direction, not a new hard gate.
7. Keep the proposed S05 artwork-payoff intervention deferred unless explicitly reopened.
8. Do not add a new routine approval gate or hard-fail class from V1_E002 soft observations.
