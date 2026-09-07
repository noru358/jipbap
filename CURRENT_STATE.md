# CURRENT_STATE

Updated: 2026-09-08
Project: jipbap
Operating mode: MANUAL_VALIDATION
Architecture under test: COMPOSITION_FIRST_HYBRID_FOOD
Execution authorization: **PERSON_APPROVED_MATERIALIZE_THEN_FOOD**

## Production state

Active episode: NONE
Next production episode: 001 only after calibration.

Media-integrity recovery for PERSON_STYLE_REF_1 and TARGET_LOOK_BOARD_REF_1 is resolved. Rendering remains limited to the approved BODY4 architecture-calibration comparison.

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

## Clean-session handoff checkpoint

- Style 1 source: USER_LOCKED + validated in repository.
- Media-integrity CI: PASS after repository-byte rebind with decoded-pixel equivalence.
- A/B comparison contract: LOCKED at `calibration/body4/RENDER_AB_PLAN.json`.
- Lane A PERSON: **NOT APPROVED / NOT REGISTERED**.
- Alpha finding: real transparency succeeded repeatedly in later attempts.
- Active failure: PERSON_STYLE_FIDELITY / FACE_CONSTRUCTION_DRIFT.
- User decision: move to a clean session before further PERSON generation.

## Target-look anchor registration

- Primary source style authority remains **PERSON_STYLE_REF_1 / USER_LOCKED**.
- Auxiliary core target-look anchor: **TARGET_LOOK_BOARD_REF_1 / USER_LOCKED_VALIDATED**.
- Repository SHA-256: `3eb4565cb80f901417ea730970dfb8a731614cce58a239b599445e54018838e6`.
- Allowed domains only: face construction, eye grammar, hair silhouette, line/texture/color, person+food shared screen language.
- Explicitly non-authoritative: embedded text, panel/grid layout, shot/cut structure, depicted menu/food-state semantics, camera/composition, meal-context entity selection.
- The source style authority is not replaced or weakened by the auxiliary board.
- All failed PERSON candidates from the previous session remain quarantined and must not be bound.

## Clean-session regeneration result (attempts 8-9)

- Both fresh outputs used only the validated hierarchical reference pair:
  - primary: `PERSON_STYLE_REF_1`;
  - auxiliary: `TARGET_LOOK_BOARD_REF_1`.
- Neither fresh output used any prior failed PERSON image as reference/edit target/conditioning input.
- Hard media QC: **PASS** for both; real RGBA alpha extrema 0–255.
- Attempt 8 SHA-256: `7c64dcfec9938c375dc6e4cea47424c8fb2e4c550fdd86f865eb49d397338f7e`.
- Attempt 9 SHA-256: `6bc319d2c385186121d14287bb2dc11f8a1f1c59a4655ffe54fd54779a46c0f4`.
- Internal visual QC: **FAIL** for PERSON_STYLE_FIDELITY / FACE_CONSTRUCTION_DRIFT; attempt 9 also shows eye-grammar drift.
- Neither output is approved, registered, or reusable. Attempts 1-9 are quarantined.
- Under AutoPipeline continuity policy, two fresh failures of the same PERSON style-fidelity contract in one render context trigger a clean-session handoff.

## User decision override — PERSON attempt 8

The user's current explicit decision supersedes the prior internal rejection/handoff diagnosis:

- clean-session PERSON attempt 8: **USER APPROVED**;
- clean-session PERSON attempt 9: **USER REJECTED / QUARANTINED**;
- attempt 8 SHA-256: `7c64dcfec9938c375dc6e4cea47424c8fb2e4c550fdd86f865eb49d397338f7e`;
- attempt 8 hard media QC: RGBA, alpha extrema 0–255;
- attempt 8 is the sole selected `PERSON_CONTEXT_SEATED` candidate;
- attempts 1–7 and 9 remain quarantined;
- no new PERSON generation is authorized while the approved attempt-8 bytes are recoverable.

The approved PERSON is not yet an active production asset because its exact PNG bytes have not yet been materialized and validated at the production registry path.

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

## Current blocker

The media-integrity and real-alpha problems are no longer the active blocker.

In this session, multiple fresh `PERSON_CONTEXT_SEATED` outputs successfully produced real RGBA transparency
(alpha extrema 0–255), but the user rejected them because the PERSON drawing language/face construction drifted
from `PERSON_STYLE_REF_1`.

The user specifically judged:
- color/texture became close or acceptable;
- the person still looked different from the desired reference;
- therefore none of these outputs may be registered or reused.

All rejected PERSON outputs from this session are quarantined. They are not references, edit targets,
continuity anchors, or production assets.

## Runtime binary handoff blocker

- User approval for PERSON attempt 8 is durable and recorded.
- The exact approved PNG exists in the current ChatGPT image runtime and passed local hard media QC.
- The currently available GitHub connector can write text/Git objects but has no direct file-reference bridge from this image runtime into a repository binary blob.
- Therefore the approved PNG cannot be truthfully declared materialized in GitHub from this chat runtime.
- FAIL-CLOSED consequence: do not promote the PERSON registry entry to `APPROVED`, do not generate dependent Lane A interaction assets, and do not compose S01 until the exact approved PNG is present at the production path and validates.
- Required manual bridge: place the approved first image at `assets/production/person/PERSON_CONTEXT_SEATED_v1.png` without editing/re-encoding it.

## Exact next action

1. Manual bridge only: place the exact user-approved attempt-8 PNG at `assets/production/person/PERSON_CONTEXT_SEATED_v1.png` without editing or re-encoding it.
2. Run the repository media-integrity gate and require SHA-256 `7c64dcfec9938c375dc6e4cea47424c8fb2e4c550fdd86f865eb49d397338f7e`, dimensions 1212×1298, RGBA alpha extrema 0–255.
3. Promote `PERSON_CONTEXT_SEATED_V1` from `USER_APPROVED_PENDING_MATERIALIZATION` to `APPROVED`.
4. Generate a fresh `FOOD_EGG_RICE_INTACT` foundation asset; the prior corrupt food raster remains retired.
5. After food hard-QC/style/meal-context PASS, register it and deterministically compose S01 from the approved PERSON + FOOD assets.
6. Present composed S01 for the user visual/identity gate.
7. On S01 PASS, promote the PERSON appearance to the calibration identity anchor and continue the remaining Lane A DAG, then Lane B board-first comparison.
8. Architecture choice remains **DEFERRED** until both lanes have comparable valid pixels.
