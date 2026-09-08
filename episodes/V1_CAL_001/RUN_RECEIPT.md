# V1_CAL_001 RUN_RECEIPT

Run date: 2026-09-08
Runtime stage reached: BOARD
Publish gate reached: NO
User intervention during run: NONE

## Reference carrier validation

PERSON_STYLE_REF_1 session carrier:
- dimensions: 1448×483
- byte SHA-256: 6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614
- decoded RGBA SHA-256: a8e7eca4f2d5396d1a4b62d7a27351ead7817056b6451632b14e0c78db880e0d
- result: MATCHES locked source/pixel identity

TARGET_LOOK_BOARD_REF_1 session carrier:
- dimensions: 770×1024
- byte SHA-256: acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b
- decoded RGBA SHA-256: dc8761e133a2c28000852bac38bfd96706bee54182f5bf7884ebfae8959cd516
- result: MATCHES locked session-carrier/pixel identity

## Generation attempts

Total image-generation calls: 5
First-pass publishable: NO
Rework loops: 4
Accepted master board: NONE

### Attempt 01
SHA-256: 444a487f56952c736db296a35e9f2b871734e2cd92d8f4c53cecc38c83c67fee
Hard FAIL:
- unintended generated text
- wrong core menu/entity: egg rice instead of kimchi pancake
- not BODY-only exact 2×3 master board

### Attempt 02
SHA-256: 8e0f7598c5aa065fba235bed1a2534188f0d81b9a8cdb56e9e1d2c6faa11b932
Hard FAIL:
- unintended generated text
- wrong core menu/entity and meal-context substitution
- cover/multi-person story leakage instead of BODY-only proxy-eater board

### Attempt 03
SHA-256: bf777aea78047e858e54e8220a58447fd65925be8c3133c2e2e2dc9a654a6844
Hard FAIL:
- unintended generated text
- wrong core menu/entity
- reference content/layout leakage despite style-only intent

### Attempt 04
SHA-256: a20c9b1d071d33d4764acfe7cd142939971450d3d1ef5e6a1fe09db5e44b6c08
Hard FAIL:
- unintended generated text
- wrong core menu/entity
- wrong panel count/layout

### Attempt 05
SHA-256: 4895530e27a2705d7c52db317a3126fe29327e9957eb0a5d04ea93db00bda28d
Hard FAIL:
- unintended generated text
- wrong core menu/entity
- wrong BODY geometry/layout and group-scene substitution

## Diagnosis

The current image runtime repeatedly treated non-authoritative reference content (egg-rice/menu/text/layout/group-story cues) as content authority even after retries that progressively reduced or removed reference conditioning.
This is a runtime execution failure, not evidence that JIPBAP_V1_SPEC requires a new permanent gate or architecture change.

Rejected outputs are not references and must not be used for continuity or repair.

## Exact continuation

Resume V1_CAL_001 at BOARD only.
Do not re-plan the episode.
In a clean image-runtime context, generate exactly one text-free 2×3 BODY master board for the six kimchi-pancake beats in PLAN.md.
Apply only JIPBAP_V1 hard-fail QC.
On PASS, continue deterministically through ASSEMBLY → FINAL and present the completed 7-page carousel for the single user publish gate.
