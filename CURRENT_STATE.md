# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION
Architecture: COMPOSITION_FIRST_HYBRID_FOOD

## Production state — asset/composition calibration

Execution authorization: **ASSET_AND_TEMPLATE_CALIBRATION_ONLY**

Active episode: NONE
Next production episode: 001 after calibration

The prior E001/evaluation execution package remains retired. Git history is archive only; no retired raster/state file is current production authority.

## Canonical rendering decision

Default BODY path:

`storyboard keyframes + explicit bridges → reusable asset resolve → stable ASSET_GAP boundaries → asset QC/approval/hash registration → deterministic scene composition → editable lettering/cover → QC/export`

Domain routing:
- PERSON identity: reuse approved assets; do not resample with every meal state.
- FOOD/FOOD_STATE: episode-local generation is expected when the menu/state is new.
- INTERACTION_COMPOSITE: use episode-locally when splitting high-risk contact would make geometry brittle.
- BACKGROUND: reuse plates/components where practical.
- full-frame generation: explicit exception only, assessed after composition is attempted.

## Canonical authority

- CALIBRATION_STATE.json
- calibration/COMPOSITION_CANDIDATES.md
- calibration/locks/COVER_SPEC_V1.json
- calibration/locks/LETTERING_SPEC_V1.json
- calibration/body4/FIXTURE.json
- calibration/body4/ASSET_PLAN.json
- calibration/person_style/COMPARE_PLAN.json
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

`assets/production/registry.json` contains **1 approved production asset**: `FOOD_EGG_RICE_INTACT_V1`.

Calibration references/evidence are stored outside the production registry and must not be registered as production pose assets.

## PERSON style lock

Status: **USER_LOCKED**
Selected authority: **PERSON_STYLE_REF_1**

Materialized source:
- path: `assets/references/PERSON_STYLE_REF_1.png`
- dimensions: 1448 × 483
- SHA-256: `6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614`

Materialized selection evidence:
- path: `calibration/person_style/PERSON_CONTEXT_SEATED_STYLE1_SELECTED.png`
- dimensions: 770 × 1024
- SHA-256: `acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b`

The user clarified that the S01–S04 evidence sheet was generated from the original Style 1 source and selected Style 1 as final. Style 2 remains non-production calibration evidence only.

The evidence sheet is a collage/reference artifact, not `PERSON_CONTEXT_SEATED` and not a production registry asset.

## Template lock state

- COVER: **SPEC_LOCKED C — FOOD_FIRST_POSTER**
- LETTERING: **SPEC_LOCKED A — DIRECT_EDITORIAL**
- placeholder pixels/fonts have no production authority.
- USER_LOCKED remains pending real-pixel validation after the BODY pilot.

## BODY4 fixture state

Fixture: `JIPBAP_HYBRID_BODY4_V2`
Status: **APPROVED**

Planned BODY sequence:
1. S01 — intact fried egg already on rice; person secondary.
2. S02 — spoon/yolk breaking contact is visibly in progress.
3. S03 — coated rice has been scooped; spoon is immediately before the mouth; **no mouth contact yet**.
4. S04 — ingestion occurred between panels; unchanged partial-bowl residue is shown.

S03 is explicitly **after scoop / before mouth contact**.

Required production asset gaps:
1. PERSON_CONTEXT_SEATED
2. FOOD_EGG_RICE_INTACT
3. INTERACTION_BREAK_YOLK
4. FOOD_EGG_RICE_RESIDUE
5. INTERACTION_BITE_APPROACH

`FOOD_EGG_RICE_RESIDUE` is intentionally reused unchanged in S03 and S04 to prove approved-pixel reuse.

## Dispatch state

- PERSON_CONTEXT_SEATED: **FAIL-CLOSED / NEW SESSION REQUIRED**. Two current-context attempts baked checkerboard pixels into RGB instead of producing alpha; both are quarantined.
- FOOD_EGG_RICE_INTACT: **RESOLVED / APPROVED** as `FOOD_EGG_RICE_INTACT_V1`.
- INTERACTION_BREAK_YOLK: waiting on PERSON_CONTEXT_SEATED + FOOD_EGG_RICE_INTACT.
- FOOD_EGG_RICE_RESIDUE: waiting on intact food + yolk-break interaction.
- INTERACTION_BITE_APPROACH: waiting on PERSON_CONTEXT_SEATED + residue.

Raw assets do not each require a user click. AUTHORIZED_OPERATOR may bounded-register QC-passed foundation assets. USER approval is reserved for the composed S01 visual/identity anchor and named locks.

## Remaining blockers

1. PERSON_CONTEXT_SEATED has no passing production asset; two no-alpha outputs are quarantined.
2. S01 composition waits on a passing PERSON_CONTEXT_SEATED asset.
3. Full-frame exception need is UNASSESSED until stable assets are composed.
4. Real-pixel COVER/LETTERING validation requires approved BODY pilot artwork and production font bytes.

## Exact next action

**HANDOFF TO A CLEAN SESSION BEFORE THE NEXT PERSON RENDER.**

Repository verification rule at handoff:
- read this file from current `jipbap/main`;
- verify `AutoPipeline/main` pins its `jipbap` gitlink to that same current commit before rendering.

Completed:
- Style 1 source and selected S01–S04 evidence are materialized and USER_LOCKED.
- `FOOD_EGG_RICE_INTACT_V1` passed QC and is registered for bounded calibration use.

Quarantined outputs:
- PERSON attempt 1: `9086ae4bfc8bab2e119604395c071ae83f3d8e7fb5bf59721693e5dd00e12b4c` — RGB, baked checkerboard, pose/expression drift.
- PERSON attempt 2: `aa9be0b19ac230d5044e6a23289d827f4412da10250a7a92e27a492ec6b7eade` — RGB, baked checkerboard.
- Neither may be edited, referenced or registered.

Next single action in a clean session:
1. Restore Git heads and read this file.
2. Dispatch **only** `PERSON_CONTEXT_SEATED` with the selected Style 1 source/evidence.
3. Require a real RGBA alpha channel; do not depict a checkerboard pattern.
4. Inspect channels/alpha before subjective visual QC.
5. If PASS, bounded-register the PERSON asset and deterministically compose S01 using `FOOD_EGG_RICE_INTACT_V1`.
6. Present composed S01 for the explicit user visual/identity anchor gate.

Do not start publishable episode 001 yet.
