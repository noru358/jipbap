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

`storyboard → reusable PERSON/BACKGROUND resolve → missing FOOD/FOOD_STATE/POSE/CONTACT asset authoring → approved registry → deterministic scene composition → lettering/cover → QC/export`

Domain routing:
- PERSON identity: reuse approved assets; do not resample with every meal state.
- FOOD/FOOD_STATE: episode-local generation is expected when the menu/state is new.
- HAND/UTENSIL/CONTACT: episode-local interaction asset is allowed when needed.
- BACKGROUND: reuse plates/components where practical.
- full-frame generation: explicit exception only.

Authority:
- CONTENT_SYSTEM.md
- VOICE_SYSTEM.md
- VISUAL_SYSTEM.md
- FOOD_STATE_SYSTEM.md
- MEAL_CONTEXT_SYSTEM.md
- PRODUCTION_PROTOCOL.md
- assets/REFERENCE_MANIFEST.md
- assets/production/registry.json

## Registry state

`assets/production/registry.json` currently contains **0 approved production assets**.

STYLE_REF_001 remains PERSON authoring authority metadata, not a production pose asset.

## Preserved structural decisions

1. PROXY_EATER remains the core audience promise.
2. FOOD_STATE / meal-context / Korean dining-grammar checks remain active.
3. BODY visual rhythm and temporal distinguishability remain active.
4. Cover is a mandatory product slot and lettering remains editable/deterministic.
5. PERSON reference coverage does not automatically claim FOOD/BACKGROUND style authority.
6. Accepted person identity is now stabilized primarily by asset reuse rather than per-shot regeneration/QC.
7. Food variability does not reopen accepted person pixels.

## Remaining blockers

1. STYLE_REF_001 binary is still not materialized in Git.
2. COVER and LETTERING still need USER_LOCKED composition templates.
3. No approved PERSON starter assets exist in the production registry.
4. No menu-specific FOOD_STATE asset pack has been tested under the hybrid compositor path.
5. Shared AutoPipeline compositor/registry validation must be used for the first pilot.

## Exact next action

Finish the deterministic COVER and LETTERING template calibration because it requires no new image generation.

Then run one fixed hybrid visual fixture: **BODY 4 slides**.
- one approved PERSON pose/identity asset set;
- one meal with enough FOOD_STATE assets to support four meaningful BODY beats;
- only necessary hand/utensil/contact assets;
- deterministic assembly into exactly four separate BODY frames;
- COVER is a separate product slot and is not counted in the four BODY slides;
- no full-frame generation unless explicitly marked as an exception.

The BODY-4 count is calibration-only. Normal Jipbap production length remains content/state-driven.

Do not start a fresh publishable 001 until this pilot validates the hybrid boundary.
