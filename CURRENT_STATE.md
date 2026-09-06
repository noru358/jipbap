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

Candidate fixture: `JIPBAP_HYBRID_BODY4_V2`
Status: **AWAITING USER APPROVAL**

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

## Remaining blockers

1. BODY4 V2 calibration content/storyboard requires explicit user approval.
2. STYLE_REF_001 binary is still not materialized in Git/current runtime for PERSON authoring.
3. Production registry still has 0 approved assets.
4. Full-frame exception need is UNASSESSED until stable assets are composed.
5. Real-pixel COVER/LETTERING validation requires approved BODY pilot artwork and production font bytes.

## Exact next action

Obtain explicit user approval for `calibration/body4/FIXTURE.json` V2.

PASS:
- mark fixture APPROVED;
- advance CALIBRATION_STATE to BODY_FIXTURE_ASSET_RESOLUTION;
- bind/materialize STYLE_REF_001 actual media before PERSON dispatch;
- create only the five declared ASSET_GAPs in dependency order;
- compose and present S01 as the next user visual anchor gate;
- after S01 PASS, continue dependent asset authoring/composition without per-asset user gates unless a new lock-worthy decision appears.

FAIL:
- revise only the fixture/storyboard scope requested by the user;
- do not generate assets.

Do not start a fresh publishable 001 until the hybrid pilot and real-pixel template validation both pass.
