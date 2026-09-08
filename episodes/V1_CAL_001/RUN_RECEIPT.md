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

Total image-generation calls: 8
First-pass publishable: NO
Rework loops: 7
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

### Attempt 06
SHA-256: 11f87a3a9d838315013d7982f8698705db8954a8cd1538d221d74f1a302e98b9
Hard FAIL:
- unintended generated text and cover/title content
- wrong core menu/entity: spicy-pork/egg/soup group meal instead of kimchi pancake
- group-scene substitution and wrong BODY geometry/layout

### Attempt 07
SHA-256: 8f5f75b3dc3c4f6068c41c0bb01c803a4ef62790e5e0b9c4690293051a2d6b0c
Hard FAIL:
- unintended generated text
- wrong core menu/entity and grocery/cooking story substitution
- six-character reference-content leakage instead of one proxy eater
- wrong BODY geometry/layout

### Attempt 08
SHA-256: 742d1ecb0c8b07bad30415a284d846335f1c298354dcd9126f7620f687616b19
Hard FAIL:
- unintended generated text
- wrong core menu/entity and multi-dish group-meal substitution
- six-character reference-content leakage
- not the specified text-free six-beat kimchi-pancake BODY master board

## Diagnosis

The image runtime repeatedly treated non-authoritative reference content and stale group-story cues as content authority even after retries with increasingly explicit BODY-only constraints.
This is a runtime execution failure, not evidence that JIPBAP_V1_SPEC requires a new permanent gate or architecture change.

Rejected outputs are not references and must not be used for continuity or repair.

The current chat image-runtime context is now contaminated by multiple rejected generations, so further same-context retries would violate the clean-runtime requirement in CURRENT_STATE.

## Exact continuation

Resume V1_CAL_001 at BOARD only.
Do not re-plan the episode.
Use a clean image-runtime context and generate exactly one text-free 2×3 BODY master board for the six kimchi-pancake beats in PLAN.md.
Apply only JIPBAP_V1 hard-fail QC.
On PASS, continue deterministically through ASSEMBLY → FINAL and present the completed 7-page carousel for the single user publish gate.
