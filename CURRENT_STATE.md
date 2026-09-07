# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION
Architecture: COMPOSITION_FIRST_HYBRID_FOOD

## Production state — asset/composition calibration

Execution authorization: **ASSET_AND_TEMPLATE_CALIBRATION_ONLY**

Active episode: NONE
Next production episode: 001 after calibration

The prior E001/evaluation execution package has been removed from the working tree. Git history is the archive; no old raster/state file is current production authority.

## Canonical rendering decision

Default BODY path:

`storyboard keyframes + explicit bridges → reusable asset resolve → stable ASSET_GAP boundaries → asset QC/approval/hash registration → deterministic scene composition → editable lettering/cover → QC/export`

Domain routing:
- PERSON identity: reuse approved assets; do not resample with every meal state.
- FOOD/FOOD_STATE: episode-local generation is expected when the menu/state is new.
- INTERACTION_COMPOSITE: use episode-locally when splitting high-risk contact would make geometry brittle.
- BACKGROUND: reuse plates/components where practical.
- full-frame generation: explicit exception only, assessed after composition is attempted.

Authority:
- CALIBRATION_STATE.json
- calibration/COMPOSITION_CANDIDATES.md
- calibration/locks/COVER_SPEC_V1.json
- calibration/locks/LETTERING_SPEC_V1.json
- calibration/body4/FIXTURE.json
- CONTENT_SYSTEM.md
- VOICE_SYSTEM.md
- VISUAL_SYSTEM.md
- FOOD_STATE_SYSTEM.md
- MEAL_CONTEXT_SYSTEM.md
- PRODUCTION_PROTOCOL.md
- assets/REFERENCE_MANIFEST.md
- assets/production/registry.json
- schemas/asset_registry.schema.json
- schemas/shot_contract.schema.json

## Registry state

`assets/production/registry.json` currently contains **0 approved production assets**.

Calibration placeholder fixtures are stored separately under `calibration/fixtures` and must never be inserted into the production registry.

STYLE_REF_001 remains PERSON authoring authority metadata, not a production pose asset.

## Template lock state

COVER and LETTERING use:

`IN_TEST → SPEC_LOCKED → USER_LOCKED`

Current:
- COVER: **SPEC_LOCKED C — FOOD_FIRST_POSTER**
- LETTERING: **SPEC_LOCKED A — DIRECT_EDITORIAL**
- both approved_spec_sha256 values were reverified against the actual lock files;
- placeholder pixels/fonts have no production authority;
- USER_LOCKED remains pending real-pixel validation after the BODY pilot.

## BODY4 fixture state

Fixture: `JIPBAP_HYBRID_BODY4_V2`
Status: **APPROVED**

Temporal model:
- one still panel = one exact keyframe;
- state changes between panels = ordered bridge steps;
- an omitted micro-action must still be explicit in bridge data;
- omission is allowed only when causal order remains unambiguous and the omitted action does not deserve its own panel.

Planned BODY sequence:
1. S01 — intact fried egg already on rice; person secondary.
2. S02 — spoon/yolk breaking contact is visibly in progress.
3. S03 — coated rice has been scooped; spoon is immediately before the mouth; **no mouth contact yet**.
4. S04 — ingestion occurred between panels; unchanged partial-bowl residue is shown.

This resolves the previous ambiguity: S03 is explicitly **after scoop / before mouth contact**.

Stable required asset gaps:
1. PERSON_CONTEXT_SEATED
2. FOOD_EGG_RICE_INTACT
3. INTERACTION_BREAK_YOLK
4. FOOD_EGG_RICE_RESIDUE
5. INTERACTION_BITE_APPROACH

`FOOD_EGG_RICE_RESIDUE` is intentionally reused unchanged in S03 and S04 to prove approved-pixel reuse.

## Asset dependency order

1. Materialize/bind actual STYLE_REF_001 media.
2. Author foundation PERSON + intact FOOD.
3. After QC, AUTHORIZED_OPERATOR may hash-register them for bounded pilot use.
4. Compose S01 and obtain explicit USER visual pass.
5. Only after S01 pass may its person appearance serve as the identity anchor for dependent interaction assets.
6. Author remaining dependent assets in DAG order.
7. Compose BODY4 and run sequence QC.

Raw assets do not each require a separate user click. USER approval is reserved for named gates/locks; operator approval may carry bounded pilot assets between those gates.

## Asset resolution result

`calibration/body4/ASSET_PLAN.json` is current.

Registry matches: 0.
Resolved ASSET_GAP count: 5.

Dispatch state:
- FOOD_EGG_RICE_INTACT: may be compiled independently from current text/meal authorities.
- PERSON_CONTEXT_SEATED: split into **two calibration candidates** under `calibration/person_style/COMPARE_PLAN.json`; both actual reference binaries are supplied and hash-verified in the current chat runtime.
- candidate outputs remain calibration-only until user style selection; do not register both into production.
- all later interaction/residue assets wait on the selected PERSON foundation and their declared dependencies.

## Remaining blockers

1. PERSON style candidate comparison is not yet rendered/selected.
2. Candidate binaries are runtime-only, not Git-materialized; a later session must reverify/re-supply them if selection is unfinished.
3. Production registry still has 0 approved assets because no final PERSON style has been selected and no real pilot asset has passed bounded registration.
4. Full-frame exception need is UNASSESSED until stable assets are composed.
5. Real-pixel COVER/LETTERING validation requires approved BODY pilot artwork and production font bytes.

## Exact next action

Run the equal-path PERSON style comparison from `calibration/person_style/COMPARE_PLAN.json`.

1. Generate `PERSON_CONTEXT_SEATED_STYLE1_CAL` using only PERSON_STYLE_REF_1 as visual style media.
2. Generate `PERSON_CONTEXT_SEATED_STYLE2_CAL` using only PERSON_STYLE_REF_2 as visual style media.
3. Apply the same semantic target contract and QC rubric to both.
4. User selects the better PERSON style.
5. Only the selected candidate may be promoted toward `PERSON_CONTEXT_SEATED`; the other remains calibration evidence.
6. Then continue the BODY4 dependency DAG and compose the S01 visual anchor.

The common FOOD foundation remains independent from the PERSON style comparison.

Do not let STYLE_REF_2's visible kitchen/food/background pixels become FOOD/BACKGROUND/composition authority.
