# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Production state — active fresh 001

Execution authorization: **ACTIVE_S01_PENDING_REFERENCE_BINDING**

Active episode: **001**
Next new episode number: **002**

Preproduction user gate: **PASS**
BODY render stage: **S01_PENDING**
Render cursor: **S01**
Approved locked BODY shots: NONE

The fresh 001 preproduction package is stored under `episodes/001`.
The retired pre-reset 001/002 packages remain invalid and must not be restored.

## Active E001 contract

MENU/MOMENT:
- 집에서 부친 김치전 + 작은 간장 종지
- 바삭한 가장자리 조각을 집어 간장은 끝에만 살짝 찍고 첫입 먹는 순간

SENSORY ROUTE:
- PURE_SENSORY
- 바삭한 가장자리 → 촉촉한 안쪽 → 간장이 묻은 끝 → 첫입 → 다음 조각
- ending: CONTINUING_BITE

BODY:
- S01 ARRIVAL
- S02 PICK
- S03 DIP
- S04 BITE
- S05 RESIDUE / CONTINUING_BITE

COVER:
- separate product asset
- working title: 김치전은 가장자리부터
- reuse approved BODY artwork first

Durable episode authority:
- episodes/001/PREPRODUCTION.md
- episodes/001/MEAL_SCENE_STATE.json
- episodes/001/RENDER_STATE.json
- episodes/001/shot_contracts/S01.json ... S05.json

## Canonical baseline

Fresh production uses:
- CONTENT_SYSTEM.md
- FOOD_STATE_SYSTEM.md
- MEAL_CONTEXT_SYSTEM.md
- VISUAL_SYSTEM.md
- VOICE_SYSTEM.md
- PRODUCTION_PROTOCOL.md
- assets/REFERENCE_MANIFEST.md
- schemas/shot_contract.schema.json

Carousel structure:
`COVER → BODY S01 → S02 → ... → Sfinal`

BODY gate topology:
`pre-raster user gate → S01 user anchor → S02..final internal QC → raster-set user gate → cover/lettering → final carousel user gate`

## Reference / dispatch blocker

STYLE_REF_001 is still declared in `assets/REFERENCE_MANIFEST.md` as:
`BINARY_REQUIRED_NOT_YET_MATERIALIZED`.

No current render-context evidence has yet proven that the actual STYLE_REF_001 image bytes are bound to the renderer.

Therefore:
- do not render S01 yet;
- do not substitute prompt prose, repository path, hash, chat memory, or retired episode images;
- do not create an episode continuity anchor before S01 user PASS.

## Exact next action

1. Bind the actual STYLE_REF_001 image to the current renderer context.
2. Verify binary identity/hash when the environment exposes the bytes.
3. Compile/authorize the S01-only render capsule.
4. Render **S01 only**, text-free, one panel / one file.
5. Present S01 for the explicit user anchor gate.

After S01 PASS:
- lock S01;
- set render cursor=S02;
- render S02..S05 sequentially with internal QC and no per-shot user gate.
