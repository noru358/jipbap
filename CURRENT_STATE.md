# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Operating mode: MANUAL_VALIDATION
Architecture under test: COMPOSITION_FIRST_HYBRID_FOOD
Execution authorization: **BODY4_A_B_CALIBRATION**

## Production state

Active episode: NONE
Next production episode: 001 only after calibration.

Media-integrity recovery for PERSON_STYLE_REF_1 is resolved. Rendering is authorized only for the approved BODY4 architecture-calibration comparison.

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

## Confirmed clean-checkout evidence

GitHub Actions run `34137819408` checked out commit
`d81a8be607417b37cb7a27ea729b1cfbb7261100` from remote `main`.

The four synthetic validator regression tests passed. Repository validation then failed on the
actual checked-out bytes:

- `FOOD_EGG_RICE_INTACT_V1`: actual SHA-256
  `9a52ef63cb408f17e12b94482a8d9f37049bb8f3daee70702ce745a9acfd5e68`;
- `PERSON_STYLE_REF_1`: actual SHA-256
  `0f7494746f5cfd9d42b5133e9ffaae7cf63dff96f5ee97773bf114f867b0ccaf`;
- `PERSON_CONTEXT_SEATED_STYLE1_SELECTED`: actual SHA-256
  `35b63461b6e15f258ae61455e89f288b12acc9d51e86dc6894b6788037c2fdae`.

All three have non-PNG bytes `59aae78a782daee9` at byte 0 and fail both Pillow verify and
full pixel decode. This is confirmed repository corruption, not a chat-preview ambiguity.

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
   - creative selection decision: **USER_LOCKED**
   - repository binary authority: **VALIDATED**
   - current repository SHA-256: `6b954d0a3e0f86b135c36527082f7253ba0d2d3c79e6e23141651218cd77e278`
   - decoded RGBA pixel SHA-256: `a8e7eca4f2d5396d1a4b62d7a27351ead7817056b6451632b14e0c78db880e0d`
   - recovered original source SHA-256: `6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614`

2. `FOOD_EGG_RICE_INTACT_V1`
   - prior operator approval: **VOID FOR CURRENT BYTES**
   - registry status: **RETIRED**
   - expected SHA-256: `20ed37d273a5ece4e14c602394d648e97db332eb4af39199be4436bd24d9ec61`
   - alpha policy: `MIN_0_MAX_255`

3. `PERSON_CONTEXT_SEATED_STYLE1_SELECTED`
   - Style 1 selection decision: **PRESERVED**
   - raster evidence authority: **RETIRED_CORRUPT_OPTIONAL_EVIDENCE**
   - expected SHA-256: `acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b`

No invalidated or quarantined raster may be used as renderer conditioning, continuity evidence,
repair input, registry asset, or compositor input.

## Session-supplied exact source recovered

The user supplied the original Style 1 source in the current ChatGPT session.

Local full-byte validation of the supplied file:
- dimensions: `1448 × 483`
- format/mode: `PNG / RGBA`
- PNG signature at byte 0: **PASS**
- Pillow `Image.verify()`: **PASS**
- full `Image.load()`: **PASS**
- SHA-256: `6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614`
- result: **EXACT MATCH to the pre-existing PERSON_STYLE_REF_1 authority identity**

Therefore no creative re-selection and no SHA rebinding are required. Only repository byte
materialization remains.

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

1. BODY4 A/B comparison contract is locked at `calibration/body4/RENDER_AB_PLAN.json`.
2. **Lane A first dispatch:** generate `PERSON_CONTEXT_SEATED` from the validated Style 1 media with a real transparent background; no food, tableware, text, checkerboard, or chroma-key background.
3. Hard-QC actual transparency before subjective style/anatomy QC. Do not repair or reuse a failed transparency output.
4. Continue Lane A foundation DAG only after that asset passes.
5. Independently dispatch the single 2×2 text-free Lane B master board from the same BODY4 semantics and Style 1 authority.
6. Do not choose the default architecture until both lanes have comparable valid actual pixels.
