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

COVER and LETTERING use two gates:

`IN_TEST → SPEC_LOCKED → USER_LOCKED`

- SPEC_LOCKED: deterministic placeholder review locks layout/type grammar only.
- USER_LOCKED: selected spec is rerendered with approved pilot artwork + hash-bound production font bytes and explicitly approved at pixel level.
- direct IN_TEST → USER_LOCKED is forbidden.

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

## Remaining blockers

1. COVER candidate spec is not yet user-selected.
2. LETTERING candidate spec is not yet user-selected.
3. STYLE_REF_001 binary is still not materialized in Git for future PERSON authoring.
4. No approved PERSON starter assets exist in the production registry.
5. No menu-specific FOOD_STATE asset pack has been tested under the hybrid compositor path.
6. Real-pixel COVER/LETTERING validation cannot occur until the BODY pilot has approved artwork and production font bytes.

## Exact next action

Run deterministic **placeholder composition calibration** with the shared AutoPipeline compositor + lettering renderer.

- render COVER A/B/C from `calibration/fixtures`;
- render LETTERING A/B/C from `calibration/fixtures`;
- production registry remains untouched;
- user selects one COVER spec and one LETTERING spec;
- record each selection as SPEC_LOCKED, not USER_LOCKED.

Then run one fixed hybrid visual fixture: **BODY 4 slides**.
- resolve required visible entities from the storyboard;
- create ASSET_GAP only for missing PERSON/FOOD_STATE/CONTACT/BACKGROUND capabilities;
- generated/imported assets must pass QC and explicit user approval before hash registration;
- deterministic assembly into exactly four separate BODY frames;
- COVER is a separate product slot and is not counted in the four BODY slides;
- no full-frame generation unless explicitly marked as an exception.

After BODY pilot assets are approved:
- rerender the selected COVER/LETTERING specs with real assets and production font bytes;
- user pixel-validates them;
- promote to USER_LOCKED only after that approval.

Do not start a fresh publishable 001 until the hybrid pilot and real-pixel template validation both pass.
