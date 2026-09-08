# CURRENT_STATE

Updated: 2026-09-09
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Presentation architecture: EDITABLE_COMPOSITION_PACKAGE_V1
Editor scene model: EDITOR_SCENE_MODEL_V1_BASELINE
Default presentation shell for new episodes: JIPBAP_PRESENTATION_SHELL_V2
Status: ACTIVE_REPAIR

## Active production state

Active episode: V1_E003
Stage: TOONDESK_0_3_1_READY_USER_ROUNDTRIP_REQUIRED
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
- V2 full-art semantic placement defaults: speech/thought/narration/SFX are freeform lettering overlays with focal-aware soft placement hints
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
- prior visual preview: APPROVED
- FINAL_PUBLISH_GATE: REOPENED_FOR_CANONICAL_IDENTITY
- reason: approved preview and handed-off package were not the same deterministic artifact
- user prior decision recorded: 2026-09-08

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

## V1_E003 full-art rebuild test

Session rebuild created under corrected V2 profile:
- profile revision: `2026-09-09_FULL_ART_OVERLAY`
- handoff filename: `V1_E003_제육볶음_FULL_ART_V2.toondesk`
- session SHA-256: `f5ecad7c32fd5f54ff7d13a211458c9465bef9b6ea35043f3d61fd6c9deac0be`
- BODY artwork extraction: actual border-based, not nominal equal split
- x interiors: [16,501], [522,1010]
- y interiors: [11,488], [509,937], [958,1517]
- crop contamination QC: PASS in session contact preview
- COVER/BODY artwork frames: full-canvas 1080×1350
- fixed lower meta band: REMOVED
- lettering: independent editable overlays
- local focal-overlap heuristic after placement repair: PASS (no text/container >35% overlap with declared primary avoid region)
- preferred fonts: Jua / Gowun Dodum / Gaegu by semantic role
- final publish gate: still reopened; this session file is a round-trip test handoff, not yet canonical repository completion

## V1_E003 full-art round-trip #2

User returned `V1_E003_package_1` after importing the full-art V2 handoff and exporting without edits.

Verified:
- COVER + S01..S06 layout JSON semantic equality against the supplied `.toondesk`: PASS for all 7 pages
- ToonDesk did not mutate scene geometry/content during the no-edit round trip
- font resolver receipt mostly matched preferred fonts
- one old-build substitution remained: S04 SFX preferred `Gaegu` resolved to `Jua`

Newly diagnosed content-authoring defect:
- the full-art test package itself used `../artwork/S06.png` as COVER artwork, so the previously liked COVER visual source/composition was not preserved
- this is not a ToonDesk round-trip mutation; it is COVER source/provenance loss in package authoring
- COVER text placement also became awkward because source selection and focal-aware lettering were not treated as one deterministic composition problem

Structural repairs accepted 2026-09-09:
- sticky `cover_artwork_provenance` added to V1 scene/profile contract
- presentation-only edits must not silently substitute another BODY source after a cover candidate source/crop is selected
- COVER lettering placement is focal-aware against face/food/hand avoid regions
- speech-bubble tail geometry is now explicit editable scene data (tip, attachment, base width, curve)
- soft safe/avoid guides are editor-toggleable and snapping targets
- font picker must mutate `preferred_family`; requested fonts are loaded before export and fallback remains visible in QC/manifest

## ToonDesk 0.3 implementation checkpoint

Implemented in `noru358/Toondesk`:
- speech bubble tail upgraded from fixed triangle/`tail_to` to soft-curved geometry with direct tip + attachment handles
- tail base width, curve and side controls added
- legacy `tail_to` imports are upgraded on load
- font-family selector bug fixed: changing font updates the real preferred family rather than leaving stale `preferred_family`
- preferred fonts are explicitly loaded before project save/PNG/SVG/package export
- guide toggle added (`G` / UI button); cover title-safe, body safe inset, placement guides and avoid regions can be visualized
- snapping now includes placement-guide and avoid-region boundaries
- focal overlap QC warning added for lettering covering high-priority avoid regions
- exact layer clicks select exact objects for easier bubble/text editing
- horizontal + vertical alignment and equal-spacing operations added
- deterministic `빈곳 배치` helper added for selected lettering/containers
- desktop version bumped to 0.3.0
- relevant pushes to main still auto-build Windows dev artifacts
- `vX.Y.Z` tag builds now publish executable files to GitHub Releases
- workflow now performs static JS/JSON validation before packaging
- auto-update remains intentionally deferred until signed/stable releases are established

## ToonDesk 0.3 build result

Latest Windows development build:
- workflow run #20
- static JS/JSON validation: PASS
- Windows packaging: PASS
- artifact: `ToonDesk-windows`
- contents: `ToonDesk 0.3.0.exe`, `ToonDesk Setup 0.3.0.exe`

E003 repaired local handoff candidate:
- filename: `V1_E003_제육볶음_COVER_RESTORED_TD03.toondesk`
- SHA-256: `82c3ab112aa935665b7d11e92d6c9bc046f66183571a0e9e4cbc0fb2278efe7f`
- COVER source restored from the previously liked cover visual raster
- source SHA-256: `12a701747e5fafc9ad36f20f729d91496f553a0d8a1b81c862d102f130b78a89`
- old baked title/tag are hidden by deterministic artwork-band masks; visible title/menu are editable scene objects
- `cover_artwork_provenance` recorded and locked for the final candidate
- speech bubbles upgraded to rich soft-curved `tail` geometry

## V1_E003 ToonDesk 0.3 returned-package QC

User returned `V1_E003_package_Re` from the restored-cover TD03 candidate.

Round-trip integrity:
- COVER + S01..S06 layout JSON semantic equality against `V1_E003_제육볶음_COVER_RESTORED_TD03.toondesk`: PASS for all 7 pages
- `cover_artwork_provenance`: preserved exactly, source `../artwork/COVER_APPROVED.png`
- rich speech-tail objects: preserved in layout JSON
- guide / avoid-region metadata: preserved through semantic page equality
- `custom_override=false`: preserved

Visual QC:
- restored COVER source/composition: substantially restored and focal subject no longer covered by title
- minor baked-title fragment remained in the cover mask edge: deterministic mask repair required
- S04 speech tail is publish-blocking presentation failure: pointer is far too long and crosses the protagonist face
- S06 speech tail is publish-blocking presentation failure: pointer crosses both eyes/face
- BODY crop contamination remains resolved

Font QC:
- all preferred/resolved families match except S04 SFX: preferred `Gaegu`, resolved `Jua`
- root cause found in ToonDesk font resolver: after loading weight 700, availability check used implicit weight 400; this can falsely mark Gaegu 700 unavailable
- resolver corrected to check the requested weight and sample text
- package did not contain a user font-family edit relative to the source candidate, so the manual font-change interaction itself was not exercised in this returned package

Repairs prepared:
- JIPBAP automatic speech-tail default now prefers short focal-safe pointers (roughly <=180px when practical; manual editor length remains unrestricted)
- E003 S04/S06 tail geometry shortened and moved off focal facial regions
- COVER residual baked-title fragment mask enlarged without covering the retained underline
- repaired handoff candidate: `V1_E003_제육볶음_COVER_RESTORED_TD031.toondesk`
- candidate SHA-256: `bdd412e63f80ef0bd5d1fc555efb9840cb6a1ccadda5b04d452036c2de850817`
- ToonDesk 0.3.1 source fix committed; Windows development build pending

## ToonDesk 0.3.1 build result

Latest Windows development build:
- workflow run #23
- head: `26d7a0999e36fdc951d21164d23c3414f97d2b06`
- static JS/JSON validation: PASS
- Windows packaging: PASS
- artifact: `ToonDesk-windows`
- artifact id: 10066881620
- contents: ToonDesk 0.3.1 installer + portable executables

Font resolver repair:
- availability checks now use the requested font weight and sample text
- this specifically addresses the false `Gaegu 700 → Jua` fallback observed in the returned TD03 package

## Previous episode provenance

V1_E001:
- FINAL_PUBLISH_GATE: APPROVED
- EPISODE STATUS: DONE
- do not mutate unless explicitly reopened

V1_CAL_001:
- prior calibration provenance only
- rejected boards remain non-reference material

## Board extraction implementation checkpoint

Reusable implementation added:
- `pipeline/extract_board.py`
- `python -m pipeline.cli extract-board <source> <output_dir> --metadata <json>`
- actual dark panel-border detection for the frozen 2×3 board
- refuses implausible/missing border geometry rather than falling back to nominal 512px slicing
- non-equal-boundary regression test added
- CI run #166: PASS
- repository validator now skips byte expectations only for explicitly non-materialized SESSION_ONLY carriers, consistent with JIPBAP_V1_SPEC §9.5; it still fails active materialized references without hashes

This implementation prevents the V1_E003 adjacent-panel crop bug from becoming a one-off manual fix.

## ToonDesk desktop usability checkpoint

Implemented in `noru358/Toondesk`:
- Electron desktop shell added while retaining static-browser fallback
- native open/save dialogs
- `.toondesk` OS file-association build configuration
- double-click / OS-open project handoff
- Ctrl/Cmd+S in-place save for an opened project
- preferred-font resolution warnings in QC
- JIPBAP full-art V2 example profile mirrored as non-authoritative example only
- Windows desktop build workflow: PASS through run #4 (head `0492910...`); artifact contains `ToonDesk Setup 0.2.0.exe` and portable `ToonDesk 0.2.0.exe`
- subsequent workflow revisions only narrow automatic triggers/artifact upload scope; they do not change scene authority

The desktop wrapper is transport/UX only. It does not change JIPBAP `composition/*.layout.json` authority or create a new production gate.

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

1. Use ToonDesk 0.3.1 Windows build (workflow run #23 PASS) with `V1_E003_제육볶음_COVER_RESTORED_TD031.toondesk`.
2. Open S04/S06 and verify the new short rich tails no longer cross the focal face; optionally drag tail tip/attachment and adjust width/curve to confirm direct manipulation.
3. Change one text object's actual font family once and visually confirm the preview changes. Export a package.
4. Verify the returned package preserves all 7 layouts semantically, COVER provenance, rich-tail geometry and guide metadata; verify the chosen font's preferred/resolved families match when available and Gaegu 700 no longer false-falls back.
5. Use those exact exported COVER + 6 BODY PNG derivatives as FINAL_PUBLISH_GATE preview.
6. After approval, persist canonical V1_E003 composition/layouts, manifest and RUN_RECEIPT and mark V1_E003 DONE.
7. Do not create V3 or a new production gate from these presentation/editor fixes.
