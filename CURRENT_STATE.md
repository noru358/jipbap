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

`storyboard → reusable PERSON/BACKGROUND resolve → missing FOOD/FOOD_STATE/POSE/CONTACT asset authoring → asset QC + user approval → hash-bound production registry → deterministic scene composition → editable lettering/cover → QC/export`

Domain routing:
- PERSON identity: reuse approved assets; do not resample with every meal state.
- FOOD/FOOD_STATE: episode-local generation is expected when the menu/state is new.
- HAND/UTENSIL/CONTACT: episode-local interaction asset is allowed when needed.
- BACKGROUND: reuse plates/components where practical.
- full-frame generation: explicit exception only.

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
- placeholder pixels/fonts have no production authority;
- USER_LOCKED remains pending real-pixel validation after the BODY pilot.

## BODY4 fixture state

Candidate fixture: `JIPBAP_HYBRID_BODY4_V1`
Status: **AWAITING USER APPROVAL**

Calibration meal:
- fried egg already on top of rice;
- intact yolk → spoon breaks yolk in place → yolk-coated spoonful is eaten → residue remains;
- Korean simple home-meal grammar;
- no full-frame generation.

Planned BODY sequence:
1. S01 ANTICIPATION — person secondary, intact egg-on-rice foreground.
2. S02 TRANSFORMATION — macro spoon/yolk contact.
3. S03 INGESTION — same person identity, spoon-to-mouth bite.
4. S04 FOOD_RESIDUE — food-only close crop.

Minimal required asset gaps:
1. PERSON_CONTEXT_SEATED
2. PERSON_BITE_SPOON_CONTACT
3. FOOD_EGG_RICE_INTACT
4. FOOD_EGG_RICE_BROKEN
5. FOOD_EGG_RICE_RESIDUE
6. CONTACT_SPOON_PRESS_YOLK

`FOOD_EGG_RICE_RESIDUE` is intentionally reused in S03 and S04 with different deterministic composition/crop to prove approved-pixel reuse.

## Preserved structural decisions

1. PROXY_EATER remains the core audience promise.
2. FOOD_STATE / meal-context / Korean dining-grammar checks remain active.
3. BODY visual rhythm and temporal distinguishability remain active.
4. Cover is a mandatory product slot and lettering remains editable/deterministic.
5. PERSON reference coverage does not automatically claim FOOD/BACKGROUND style authority.
6. Accepted person identity is stabilized primarily by asset reuse rather than per-shot regeneration/QC.
7. Food variability does not reopen accepted person pixels.
8. One frame = one image file, but one frame does not equal one user approval gate.
9. BODY=4 is calibration-only, never a normal production hard-code.
10. Registry entry order is generation/import → QC → explicit user approval → SHA-256 registration.

## Remaining blockers

1. BODY4 calibration content/storyboard requires explicit user approval.
2. STYLE_REF_001 binary is still not materialized in Git for PERSON asset authoring.
3. Production registry still has 0 approved assets.
4. Real-pixel COVER/LETTERING validation requires approved BODY pilot artwork and production font bytes.

## Exact next action

Obtain explicit user approval for `calibration/body4/FIXTURE.json`.

PASS:
- mark fixture APPROVED;
- advance CALIBRATION_STATE to BODY_FIXTURE_ASSET_RESOLUTION;
- resolve the six requirements against the production registry;
- since registry is currently empty, create only those six ASSET_GAP authoring jobs;
- do not call a renderer until required actual reference media is bound and parent media authorization passes.

FAIL:
- revise only the fixture/storyboard scope requested by the user;
- do not generate assets.

Do not start a fresh publishable 001 until the hybrid pilot and real-pixel template validation both pass.
