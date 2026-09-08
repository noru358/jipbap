# CURRENT_STATE

Updated: 2026-09-09
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Presentation architecture: EDITABLE_COMPOSITION_PACKAGE_V1
Editor scene model: EDITOR_SCENE_MODEL_V1_BASELINE
Default presentation shell for new episodes: JIPBAP_PRESENTATION_SHELL_V2
Status: DONE

## Active production state

Active episode: V1_E003
Stage: FULL_ART_V2_REBUILD_REQUIRED
BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E003/PLAN.md
Run receipt: pending

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
- V2 revision: `2026-09-09_FULL_ART_OVERLAY`
- canvas: 1080 × 1350
- COVER: full-canvas artwork + vector menu tag/title/decor; title region is a soft placement hint, not a separate frame
- BODY: full-canvas artwork; no fixed lower meta band
- speech / inner-thought / narration / SFX are independent freeform vector/scene overlays
- automatic placement is focal-aware and may use optional face/food/hand avoid metadata
- artwork starts locked in automatic Chat production
- lettering movement is ordinary presentation editing; explicit artwork-frame/page-structure deviation is `CUSTOM_OVERRIDE`
- preferred real fonts + fallback chains are recorded; missing preferred fonts must be surfaced instead of silently substituted

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

## V1_E003 approval state

- STORYBOARD_USER_GATE: IMPLICITLY_ACCEPTED_BY_PRODUCTION_CONTINUATION
- BOARD hard-fail QC: PASS
- FINAL_PUBLISH_GATE: APPROVED
- user final decision recorded: 2026-09-08

Important implementation note:
- the approved visual preview was shown successfully, but the repository has not yet received the canonical V2 editable composition package / RUN_RECEIPT for V1_E003.
- therefore do not declare the episode repository state DONE until deterministic canonicalization and receipt persistence are completed.
- this is artifact completion, not a new user gate and not a new permanent hard-fail class.

## V1_E003 ToonDesk round-trip QC

User test:
- imported the supplied `.toondesk` into ToonDesk
- made no edits
- exported `V1_E003_package.zip`
- returned the export for QC

Round-trip integrity:
- all 7 layout JSON files are byte-semantic equivalent to the source project pages: PASS
- page count COVER + S01..S06: PASS
- 1080 × 1350 PNG export for all 7 pages: PASS
- manifest `custom_override=false`: PASS
- all 7 SVG derivatives parse successfully and retain embedded artwork: PASS

Authoring/package defects discovered:
- S03 artwork contains an obvious strip of the next panel at the bottom: HARD VISUAL FAIL
- S04 artwork contains an obvious strip of the next panel at the bottom: HARD VISUAL FAIL
- root cause: the supplied package naively sliced the 1024×1536 generated board at nominal 512px row boundaries even though the actual generated panel borders were not located at equal 512px row boundaries
- S06 speech bubble obscures a substantial part of the protagonist face/eye area: presentation defect requiring deterministic layout repair
- the previously approved 7-page preview was separately generated instead of being the deterministic derivative of the accepted master BOARD; therefore approval identity and canonical package identity diverged

Interpretation:
- ToonDesk did NOT introduce these defects. The no-edit round trip preserved the supplied scene exactly.
- this is a package-authoring / deterministic-assembly failure, not evidence for a new permanent V1 hard gate or new editor rule.
- V1_E003 must not be declared DONE until the canonical package is rebuilt under the corrected full-art V2 shell and the changed final carousel is shown at the final publish gate.
- the prior final preview approval is not canonical package approval because preview/package identity diverged; FINAL_PUBLISH_GATE is therefore REOPENED_FOR_CANONICAL_IDENTITY for E003 only.

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

1. Rebuild V1_E003 under the corrected `2026-09-09_FULL_ART_OVERLAY` revision of `JIPBAP_PRESENTATION_SHELL_V2`; do not create V3 solely for this correction because no V2 episode was ever completed.
2. Re-extract the accepted master BOARD using detected/confirmed actual panel borders, never nominal 512px slicing. Remove all adjacent-panel contamination from S01..S06.
3. Use full-canvas 1080×1350 artwork on COVER and BODY. COVER title/menu/decor and all BODY speech/thought/narration/SFX must remain independent editable lettering/overlay objects.
4. Remove the mandatory lower meta band. Place lettering focal-aware using soft safe insets and optional face/food/hand avoid regions; repair any focal obstruction such as the prior S06 face-covering bubble.
5. Resolve preferred real fonts from the V2 profile. If the preferred family is unavailable, surface the fallback and ensure final preview/export use the same resolved family.
6. Render the FINAL_PUBLISH_GATE preview from the exact same composition package that will be handed to the user; never separately generate a lookalike preview.
7. Verify no-edit ToonDesk round-trip preserves the rebuilt scene. ToonDesk remains a generic engine; JIPBAP `composition/*.layout.json` remains authority.
8. After the corrected carousel is approved, persist composition/layouts, manifest and RUN_RECEIPT and mark V1_E003 DONE.
9. Separately improve ToonDesk usability by adding a desktop-app launch path while keeping the browser/static fallback; this must not change JIPBAP authority or add a production gate.
