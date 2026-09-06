# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Production state — clean reset after structure test

Execution authorization: **IDLE_NO_ACTIVE_EPISODE**

Active episode: NONE
Next episode number: **001**

The experimental fresh 001 package and all prototype raster outputs from the just-completed structure test are retired.
They are not active episode authority, approval evidence, continuity anchors, subject identity anchors, cover assets or repair sources.

Only generalized structure improvements promoted into canonical authority remain valid.

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
- schemas/render_state.schema.json

Carousel product order:
`COVER → BODY S01 → S02 → ... → Sfinal`

COVER is a separate mandatory product slot.
It may be produced by BODY reuse, dedicated generation, or external import, but final completion is blocked until cover_status=PASS.

BODY production:
`pre-raster user gate → S01 user anchor → S02..final internal QC → whole-sequence QC → raster-set user gate → cover/lettering → final carousel user gate`

## New structural requirements from the prototype

1. **EPISODE_SUBJECT_LOCK**
   - any person recurring in 2+ BODY shots gets an episode-local identity lock;
   - later shots use canonical style authority + subject lock + approved identity-anchor media when supported;
   - episode reset deletes this lock.

2. **SHOT_COVERAGE_RHYTHM**
   - storyboard records focal owner, shot scale, camera relation, visual delta from previous and repetition justification;
   - fixed left/right/front quotas are forbidden;
   - whole-set viewer-perceived redundancy QC occurs before the raster-set user gate.

3. **HUMAN_GEOMETRY_QC**
   - high-risk hand/arm/utensil/mouth contact has an explicit geometry risk/contact chain;
   - broken anatomy/contact geometry is a hard fail.

4. **STYLE_DOMAIN_COHERENCE**
   - food may be more detailed than people but must remain in the same illustration abstraction/rendering language;
   - semi-realistic food + flat-toon person drift is a hard fail.

5. **MANDATORY_COVER_GATE**
   - cover omission cannot be treated as a completed carousel;
   - cover may be created/imported elsewhere but must be registered and PASS before final gate.

## Fail-closed reset rule

While Active episode is NONE:
- do not render;
- do not restore the retired prototype 001 menu/story/copy/shot contracts/approvals;
- do not restore prototype S01-S05 outputs as references;
- do not infer an old menu/story from chat history;
- do not create a render cursor;
- do not create an EPISODE_SUBJECT_LOCK until a fresh episode proposal exists.

Project-level style-reference runtime requirements remain governed by assets/REFERENCE_MANIFEST.md.

## Exact next action

In a new session, restore AutoPipeline + jipbap HEADs and create a fresh **001 preproduction proposal only**:

1. MENU/MOMENT;
2. SENSORY ROUTE;
3. meal context + dining grammar;
4. initial MEAL_SCENE_STATE;
5. recurring-subject detection + EPISODE_SUBJECT_LOCK plan;
6. body emotional/state beats;
7. body visual coverage plan + adjacent visual-delta review;
8. per-shot geometry risk/contact chain;
9. BODY storyboard;
10. COVER brief + cover source route;
11. voice/copy plan.

Present the complete package for explicit user approval before creating/activating `episodes/001` or rendering BODY S01.
