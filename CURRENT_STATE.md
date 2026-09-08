# CURRENT_STATE

Updated: 2026-09-09
Project: jipbap
Runtime spec: JIPBAP_V1_SPEC.md
Architecture: SIX_PANEL_BOARD_FIRST
Presentation architecture: PRESENTATION_MASTER_FIRST
Editable scene package: EDITABLE_COMPOSITION_PACKAGE_V1
Editor scene model: EDITOR_SCENE_MODEL_V1
Default presentation shell for new episodes: JIPBAP_PRESENTATION_SHELL_V2
Status: IN_PROGRESS

## Active production state

Active episode: V1_E006
Stage: INITIAL_ART_BUNDLE_COVER_PENDING_MIGRATION

## Boot snapshot — active episode under new artwork-bundle flow

- Active episode: `V1_E006`
- Current stage: `INITIAL_ART_BUNDLE_COVER_PENDING_MIGRATION`
- Food: 두부조림
- STORYBOARD_USER_GATE: APPROVED
- PERSON renderer projection: USER_LOCKED; repository binary NOT_MATERIALIZED
- FOOD renderer projection: USER_LOCKED; repository binary NOT_MATERIALIZED
- BODY master BOARD: APPROVED_AND_LOCKED_PRE_BUNDLE_MIGRATION
- approved BOARD generation id: `92d89711-72ad-4286-8868-443c64123885`
- approved BOARD SHA-256: `86229c6426192a102cd104926e662dfdf307e368993064b58641140c4048f6e0`
- approved BOARD dimensions: 1024 × 1536
- approved BOARD repository binary materialization: NOT_CONFIRMED; exact accepted pixels must be recovered/re-supplied for any new-chat downstream extraction, never redrawn from hash/prose
- distinct COVER hero: NOT_STARTED
- ART_BUNDLE_USER_GATE: PENDING
- FINAL_PUBLISH_GATE: NOT_STARTED
- Plan: `episodes/V1_E006/PLAN.md`
- V1_E005 remains preserved at its prior `FINAL_PUBLISH_GATE` unchanged.

Canonical flow upgraded 2026-09-09:
- storyboard approval and renderer-carrier binding occur in the same handoff turn;
- `INITIAL_ART_BUNDLE` creates one text-free BODY 2×3 master board plus one separate text-free COVER hero before artwork approval;
- BODY and COVER are shown together at `ART_BUNDLE_USER_GATE`;
- that approval locks the exact BODY/COVER artwork sources for all downstream extraction, presentation and editor work;
- COVER is governed by role, not by any specific BODY slot; slot-specific camera/composition restrictions do not become permanent rules;
- approved artwork is never regenerated merely because a later/new chat lacks its bytes; recover/re-supply the exact accepted pixels or fail closed.

V1_E006 migration:
- BODY was already approved before this architecture change and remains locked;
- do not regenerate BODY to conform retroactively;
- generate only the missing independent COVER, then present locked BODY + COVER together at `ART_BUNDLE_USER_GATE`;
- earlier stale six-panel COVER attempts are REJECTED_NON_CANONICAL and do not become references, carriers, COVER authority or BODY replacements.

Exact next action for episode production:
1. Complete the missing COVER component of V1_E006 `INITIAL_ART_BUNDLE` without regenerating the approved BODY.
2. If a clean/new chat is required, carry the exact approved BODY pixels forward as a SESSION_ONLY production-art carrier (or recover materialized episode bytes); the stored hash/generation id is not a redraw instruction.
3. Use the approved PERSON/FOOD renderer carriers only as style-delivery inputs; if repository-direct bytes are unavailable, bind the exact approved SESSION_ONLY carriers.
4. Generate one independent text-free COVER hero using episode-level cover intent with free camera/composition/pose/expression; do not encode any BODY-slot-specific rule.
5. Present the locked BODY + new COVER together at `ART_BUNDLE_USER_GATE`.
6. After approval, continue EXTRACT/FIT → quality-first `PRESENTATION_MASTER_DRAFT` → `FINAL_PUBLISH_GATE`.

Infrastructure upgrade completed for future/new work:
- `INITIAL_ART_BUNDLE` is now the canonical initial image-authoring phase: BODY 2×3 master board + separate COVER hero are created before one combined artwork approval gate.
- `ART_BUNDLE_USER_GATE` replaces the prior split BOARD-now/COVER-later approval pattern for new episodes.
- COVER remains role-based and fluid; no BODY-slot-specific camera/composition rule is permanent.
- Approved BODY/COVER source pixels are immutable downstream unless the user explicitly reopens artwork.
- JIPBAP planning/copy guidance now co-designs image + lettering space without putting text into the BOARD.
- `JIPBAP_BOARD_EXTRACTION_V1` remains the single extraction record and now maps each S01..S06 output to the detected box + output SHA-256.
- BODY scene provenance references that extraction record/box index; final 4:5 FIT stays owned by the artwork object's `crop`.
- ToonDesk 0.3.3 preserves manual edits at property scope during same-ID layout reconstruction; no whole-object lock system was added.
- preferred/resolved font family + weight + substitution are persisted/surfaced; preview + PNG continue to share the same Canvas scene renderer.
- curved-tail, organic-bubble, horizontal-flip, guides/alignment and generic page/frame editing remain existing capabilities and were not reimplemented.
- ToonDesk tests + Web Live Sync: PASS at `b06a357d3364cd22b7681a64d4537546cf9c3073`.
- JIPBAP validation including extraction/scene-contract regressions: PASS at `927ad28245933cdf0808b84897020a19c0549e45`.

Remaining verification limits:
- no real-device mobile touch test was performed in this infrastructure pass;
- no browser visual/pixel parity claim is made beyond the shared scene/render contract and CI tests;
- external SVG rasterizers may differ in font metrics/antialiasing;
- whether the revised planning/copy prompt improves actual comic quality must be evaluated on the next new episode, not by rewriting V1_E005.

BODY count: 6
Carousel: COVER + 6 BODY
Master board: 2 columns × 3 rows, text-free
Final page ratio: 4:5
Plan: episodes/V1_E006/PLAN.md
Run receipt: pending FINAL_PUBLISH_GATE approval

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
- V2 revision: `2026-09-09_MANUAL_OVERRIDE_PROVENANCE_V1`
- canvas: 1080 × 1350
- COVER: full-canvas artwork + standardized episode-label/title roles; `COVER_TITLE_SYSTEM_V1` default grammar is `EP.{episode_no} {topic_phrase}와 {food_name}`; title region is a soft placement hint, not a separate frame
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
- FINAL_PUBLISH_GATE: APPROVED_BY_EXPLICIT_USER_CLOSE
- user close decision recorded: 2026-09-09
- canonical composition: episodes/V1_E003/composition/*.layout.json
- run receipt: episodes/V1_E003/RUN_RECEIPT.md

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

## V1_E003 closure

- EPISODE STATUS: DONE
- closed by explicit user request on 2026-09-09
- canonical shell: `JIPBAP_PRESENTATION_SHELL_V2`
- profile revision: `2026-09-09_FULL_ART_OVERLAY`
- canonical handoff candidate SHA-256: `bdd412e63f80ef0bd5d1fc555efb9840cb6a1ccadda5b04d452036c2de850817`
- composition authority persisted under `episodes/V1_E003/composition/`
- RUN_RECEIPT persisted
- no additional TD031 user round-trip is required for E003 closure
- do not mutate V1_E003 unless the user explicitly reopens episode 3

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

## ToonDesk Web Live checkpoint

Primary interactive-editor transport changed 2026-09-09:
- hosted ToonDesk web editor is now the normal development/use path
- canonical URL: `https://noru358.github.io/Toondesk/`
- ToonDesk `main` is automatically mirrored to the `gh-pages` branch through `Web Live Sync`
- GitHub's branch-based Pages deployment is active; no EXE download is required for routine editor revisions
- Chrome/Edge hosted mode uses the File System Access API for native project open/save and Ctrl/Cmd+S in-place save when supported
- Electron/Windows builds remain optional for OS file association/offline use and are now manual/tag-driven instead of rebuilding on every `main` push
- web/desktop transport does not change JIPBAP composition authority

## Generic editor boundary

- Generic editor implementation repository: `noru358/Toondesk`.
- ToonDesk is a separate generic editor/renderer capability surface, not JIPBAP canonical authority.
- JIPBAP owns its project profile/default shell; ToonDesk consumes it.
- Canonical JIPBAP profile: `templates/JIPBAP_PRESENTATION_SHELL_V2.json`.
- Any `profiles/jipbap_v2.example.json` copy in ToonDesk is a non-authoritative development/example mirror only.
- ToonDesk transport/session wrappers (`TOONDESK_PACKAGE_V1`, `TOONDESK_PROJECT_V1`) are non-authoritative. `composition/*.layout.json` remains the JIPBAP presentation authority.
- ToonDesk may report explicit profile deviations as `CUSTOM_OVERRIDE`; this is not corruption and does not change scene-format authority.
- Automatic Chat production does not invent per-episode custom overrides. Overrides require explicit user/editor action.

## V1_E004 production checkpoint

User approvals / runtime facts:
- STORYBOARD_USER_GATE: APPROVED
- approved renderer carrier supplied in-session as the already locked `JIPBAP_STYLE_CARRIER_V1`
- first generated 2×3 BOARD was not accepted because background/context density was too high
- revised 2×3 BOARD with reduced background density: USER APPROVED
- approved revised BOARD generation id: `5203ada2-e4fb-4f49-bd88-865f763e7eaa`
- approved revised BOARD dimensions: 1024 × 1536
- BODY count / panel geometry: six visually extractable cells
- BOARD hard-fail QC: PASS at the user-approved checkpoint

Accepted E004 QC findings:
- background simplification improved the board and should remain the automatic default
- later per-page food renders became too photoreal / glossy relative to the simplified PERSON drawing language
- FOOD should stay appetizing but use grouped illustrated texture, restrained gloss and consistent abstraction across wide and macro shots
- the current COVER artwork/text balance was acceptable to the user; the improvement target is series-level standardization rather than changing the basic hero-art composition
- standardized COVER title system accepted: `COVER_TITLE_SYSTEM_V1`
- E004 semantic cover title: `EP.4 퇴근길과 김치볶음밥`

Canonicality correction:
- the separately re-generated 4:5 COVER/S01..S06 images shown after BOARD approval are NON-CANONICAL exploratory previews.
- they were stochastic re-imaginings rather than deterministic derivatives of the accepted 2×3 BOARD, so they must not become E004 presentation authority or final approval identity.
- this does not create a new gate; it restores the already-defined BOARD → deterministic composition rule.

Structural changes applied:
- `JIPBAP_V1_SPEC.md`: natural-spoken copy interpretation clarified; FOOD de-photorealization and panel-consistency guidance strengthened; unnecessary background density added to soft QC; COVER title grammar standardized without fixed coordinates.
- `templates/JIPBAP_PRESENTATION_SHELL_V2.json`: revision advanced to `2026-09-09_COVER_TITLE_SYSTEM_V1`; episode label + semantic title fields added; duplicate menu tag disabled by automatic default while remaining an editor capability.
- `episodes/V1_E004/PLAN.md`: COVER title updated to `EP.4 퇴근길과 김치볶음밥`.

## V1_E004 canonical candidate checkpoint

- approved BODY source: revised 2×3 BOARD generation `5203ada2-e4fb-4f49-bd88-865f763e7eaa`
- actual detected x border bands: [8,11], [503,505], [518,520], [1014,1016]
- actual detected y border bands: [4,6], [490,492], [503,506], [1005,1007], [1020,1022], [1523,1525]
- extracted x interiors: [12,503], [521,1014]
- extracted y interiors: [7,490], [507,1005], [1023,1523]
- nominal equal slicing: NOT USED
- cover source: accepted S06 cell reused deterministically; provenance locked
- cover title system: `COVER_TITLE_SYSTEM_V1`
- composed cover title: `EP.4 퇴근길과 김치볶음밥`
- candidate package SHA-256: `a93e34374aa4ba8ec2eb2c78ff7f483e19eb16ca89deb29836a16b386f6a08eb`
- ToonDesk candidate SHA-256: `c994ec0ef46c27477636f9833e482d6697936a5684b8dc54fdb3df10bda7bbe4`
- preferred profile webfonts were unavailable in this deterministic render runtime; candidate lettering is pinned to Noto Sans KR intent / local Noto Sans CJK KR fallback and this substitution is surfaced rather than hidden.
- canonical composition/export files are prepared in-session but are not yet persisted to repository until FINAL_PUBLISH_GATE approval.
## V1_E004 closure

- EPISODE STATUS: DONE
- STORYBOARD_USER_GATE: APPROVED
- revised BOARD: APPROVED
- FINAL_PUBLISH_GATE: APPROVED
- final publish artifact: earlier 7-page stochastic draft, explicitly selected by user
- final selection record: `episodes/V1_E004/FINAL_SELECTION.md`
- run receipt: `episodes/V1_E004/RUN_RECEIPT.md`
- later deterministic BOARD-derived candidate: preserved for feedback at `episodes/V1_E004/review_candidates/DETERMINISTIC_GATE_20260909.md`
- known FOOD-realism / cross-domain coherence issues remain accepted soft-quality feedback for future episodes
- the E004 page-level stochastic final selection is an explicit one-episode override and does not change the normal V1 deterministic approval-identity path
## V1_E004 post-publish structural feedback

- published V1_E004 artifact remains CLOSED and unchanged.
- postmortem: `episodes/V1_E004/POSTMORTEM_20260909.md`
- repeated FOOD photorealism is now classified as unresolved renderer style-delivery, not merely prompt wording.
- new renderer-safe projection required before next production BOARD: `JIPBAP_FOOD_STYLE_CARRIER_V1`.
- COVER automatic default: distinct text-free hero artwork; no silent BODY-cell reuse.
- `COVER_TITLE_SYSTEM_V1` remains; EP label defaults to plain lettering without an enclosing bubble/pill.
- BODY speech default: soft organic oval bubble + hand-drawn typography; horizontal bubble flip supported in ToonDesk.
- ingestion/copy timing rule added: flavor/mouthfeel claims cannot precede visible or already-established ingestion.

## ToonDesk 0.3.2 checkpoint

- repository: `noru358/Toondesk`
- package version: 0.3.2
- speech bubble horizontal flip: IMPLEMENTED
- default bubble silhouette: `soft_oval`
- default tail: narrower + more curved
- JIPBAP hand-drawn typography profile mirror: UPDATED
- JavaScript syntax validation: PASS for core/render/panels/actions/interaction/io/wiring
- this editor change does not mutate completed E004 output.
## V1_E005 production state

- STORYBOARD_USER_GATE: APPROVED
- one-time FOOD renderer projection: APPROVED / USER_LOCKED
- JIPBAP_FOOD_STYLE_CARRIER_V1 session SHA-256: `e2cb04ff82671fff655830b1a3be540561d3dde108eb18bed7a8cc6d09a9c73a`
- FOOD carrier dimensions: 1254 × 1254
- FOOD carrier repository binary materialization: NOT_COMPLETED_IN_THIS_RUNTIME
- permitted binding until materialization: identical approved SESSION_ONLY fallback
- BODY master BOARD: APPROVED
- approved BOARD SHA-256: `f1c27c4a635406d616f1649127318767ba22ba5d2d51f87088db4808fd76c126`
- approved BOARD dimensions: 1024 × 1536
- detected cell interiors: x [12,503], [520,1012]; y [9,487], [504,986], [1003,1522]
- BODY eye-design correction in S03/S06: APPROVED with revised BOARD
- distinct COVER hero: APPROVED
- COVER source SHA-256: `eba699359373e2534fe5edcfd027c78af0e77962c2609607b086047960828fc8`
- COVER dimensions: 1122 × 1402
- prior tool-first deterministic final candidate: REJECTED_AS_PRESENTATION_BASELINE_BY_STRUCTURAL_FEEDBACK
- rejection reason: editor/shell defaults were allowed to define the upstream bubble/typography design, causing visible quality regression versus the earlier quality-first lettered drafts
- approved BOARD/COVER artwork remain locked and are NOT reopened
- new presentation architecture: `PRESENTATION_MASTER_FIRST`
- current stage: `FINAL_PUBLISH_GATE` on a quality-first `PRESENTATION_MASTER_DRAFT`
- presentation-master candidate session SHA-256: `38f25a32289af32631279c2ec8afecf3997292e8043b649dddf2e0c6b4a6b226`
- candidate is visual-design target only; approved literal copy and accepted BOARD/COVER artwork remain authority
- final editable package must be reconstructed from the approved visual target and pass `PRESENTATION_PARITY_QC`
- tool limitation must not silently simplify approved presentation design; extend ToonDesk/scene capability when required

## Historical location note

The canonical episode exact-next-action is intentionally kept in the boot snapshot near the top of this file.
Do not infer a newer runtime action from historical checkpoints below.
