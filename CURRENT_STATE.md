# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Operating mode: MANUAL_VALIDATION
Architecture under test: COMPOSITION_FIRST_HYBRID_FOOD
Execution authorization: **MEDIA_INTEGRITY_RECOVERY_ONLY**

## Production state

Active episode: NONE
Next production episode: 001 only after calibration.

All rendering is suspended. The previous exact-next-action to rerender
`PERSON_CONTEXT_SEATED` is superseded by media-integrity recovery.

## Parent/child authority

Before work, verify current `jipbap/main` and that `AutoPipeline/main` pins that same child commit.
README is descriptive only.

Canonical current authority:
- CURRENT_STATE.md
- INTEGRITY_STATE.json
- CALIBRATION_STATE.json
- PRODUCTION_PROTOCOL.md
- assets/reference_registry.json
- assets/REFERENCE_MANIFEST.md
- assets/production/registry.json
- calibration/body4/FOUNDATION_QC.json
- calibration/body4/FIXTURE.json
- calibration/body4/ASSET_PLAN.json
- CONTENT_SYSTEM.md
- VOICE_SYSTEM.md
- VISUAL_SYSTEM.md
- FOOD_STATE_SYSTEM.md
- MEAL_CONTEXT_SYSTEM.md

## Media-integrity incident

The repository now has an executable fail-closed validator:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python -m pipeline.cli validate
```

It checks recorded SHA-256, PNG signature at byte 0, Pillow verify, full pixel decode with
`Image.load()`, dimensions, and declared alpha policy.

The following prior binary approvals are suspended until that gate passes:

1. `PERSON_STYLE_REF_1`
   - creative selection decision: **PRESERVED**
   - repository binary authority: **INVALIDATED**
   - expected SHA-256: `6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614`

2. `FOOD_EGG_RICE_INTACT_V1`
   - prior operator approval: **SUSPENDED**
   - registry status: **INVALIDATED_MEDIA_INTEGRITY**
   - expected SHA-256: `20ed37d273a5ece4e14c602394d648e97db332eb4af39199be4436bd24d9ec61`
   - alpha policy: `MIN_0_MAX_255`

3. `PERSON_CONTEXT_SEATED_STYLE1_SELECTED`
   - Style 1 selection decision: **PRESERVED**
   - raster evidence authority: **INVALIDATED / OPTIONAL TO RECOVER**
   - expected SHA-256: `acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b`

No invalidated or quarantined raster may be used as renderer conditioning, continuity evidence,
repair input, registry asset, or compositor input.

## BODY4 calibration

The approved semantic fixture remains valid:
1. S01 — intact fried egg already on rice.
2. S02 — spoon/yolk breaking contact is visibly in progress.
3. S03 — coated rice is on the spoon immediately before mouth contact.
4. S04 — ingestion occurred between panels; residue state remains.

Content/food-state/meal-context/voice authorities are not invalidated by this byte incident.

## Rendering-architecture decision

**DEFERRED.**

Do not promote board-first or asset-first based on results produced from unverified input bytes.
After media integrity is green, run the same BODY4 fixture through:

- Lane A: repaired hybrid asset/composition path.
- Lane B: board-first comparison path.

Compare at minimum:
- S02 contact geometry;
- S03 hand/spoon/mouth geometry;
- food texture retention after board-cell extraction/expansion;
- food-state continuity;
- PERSON/style continuity;
- retries and reusable-asset cost.

A >4-slide boundary test is required before board-first can claim cross-board continuity.

## Exact next action

1. **Do not render anything.**
2. Recover `PERSON_STYLE_REF_1` first.
   - Prefer the exact original bytes matching the recorded SHA-256.
   - If exact bytes are unavailable, re-supply the intended Style 1 source, fully validate the newly materialized bytes, compute a new SHA-256, and explicitly rebind the preserved Style 1 selection to them.
3. For `FOOD_EGG_RICE_INTACT_V1`, either restore exact bytes or retire it and regenerate after the gate is green.
4. `PERSON_CONTEXT_SEATED_STYLE1_SELECTED` may be restored if convenient; otherwise retire this raster evidence while preserving the Style 1 selection decision.
5. Run `python -m pipeline.cli validate`.
6. Only after PASS may BODY4 rendering/A-B comparison resume.
