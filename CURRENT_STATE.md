# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Production state — clean reset

Execution authorization: **IDLE_NO_ACTIVE_EPISODE**

Active episode: NONE

Next episode number: **001**

The previous 001/002 episode packages, their menu/story/copy decisions, approvals, QC records and episode-local anchors are retired and removed from active production state.

Only generalized project rules that were promoted into canonical authority remain valid.

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

The active carousel structure is:
`COVER → BODY S01 → S02 → ... → Sfinal`

COVER is a separate product asset, not BODY S01.
BODY production remains:
`pre-raster user gate → S01 user anchor → S02..final internal QC → raster-set user gate → cover/lettering → final carousel user gate`

## Fail-closed reset rule

While Active episode is NONE:
- do not render;
- do not restore old episode approvals or anchors;
- do not infer an old menu/story from chat history;
- do not create a render cursor;
- do not treat historical episode numbers as active production state.

## Exact next action

Create a fresh 001 **preproduction proposal only** from the current canonical structure:
1. MENU/MOMENT;
2. SENSORY ROUTE;
3. meal context + dining grammar;
4. initial MEAL_SCENE_STATE;
5. body sensory/food-state beats;
6. body storyboard + cover brief;
7. voice/copy plan.

Present that package for explicit user approval before creating/activating `episodes/001` or rendering BODY S01.
