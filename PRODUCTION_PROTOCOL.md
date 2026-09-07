# PRODUCTION_PROTOCOL — jipbap v1.0
Updated: 2026-09-07

## 0. Production boundary

Default visual architecture: **COMPOSITION_FIRST_HYBRID_FOOD**.

`menu/moment → sensory + meal-context plan → storyboard → asset resolve → ASSET_GAP authoring → approved assets → deterministic BODY composition → cover/lettering → QC/export`

Full-frame stochastic generation is exception-only.

## 0.1 Executable media-integrity preflight

A path, recorded hash, successful `Image.open()` header read, or visual thumbnail is not proof that
an image is a valid production/reference asset.

Before any raster may be used as reference media, registered as APPROVED, promoted to USER_LOCKED,
or supplied to COMPOSITION, the child executable gate must pass:

```bash
python -m pipeline.cli validate
```

For tracked PNG media the gate verifies:
- exact SHA-256 against the bound authority;
- PNG signature at byte 0;
- `Pillow Image.verify()`;
- a second open plus full `Image.load()` pixel decode;
- recorded dimensions;
- declared alpha policy where composition requires transparency.

Any failure invalidates only the affected binary and its dependent approvals. Creative decisions such
as "Style 1 was selected" remain preserved unless the user changes them, but no invalid binary may
condition a renderer or enter the compositor.

## 1. What stays stable vs what may be generated

### Reuse-first
- recurring PERSON identity / pose assets when they fit;
- reusable background/local plates;
- reusable tableware/props when semantically correct;
- approved cover/lettering templates after calibration.

### Episode-local generation is expected
- new menu / FOOD asset;
- meaningful FOOD_STATE transition;
- hand/utensil/contact asset when the existing library cannot express the action;
- story-specific prop/location component;
- necessary new person pose/expression.

Food variability does not authorize regenerating accepted PERSON identity.

## 2. State machine

`PREPRODUCTION
→ USER_CONTENT_GATE
→ ASSET_RESOLUTION
→ [ASSET_GAP_AUTHORING → ASSET_QC]*
→ BODY_COMPOSITION
→ SEQUENCE_QC
→ COVER_AND_LETTERING
→ FINAL_USER_GATE
→ EXPORT_READY`

One frame = one file.
One frame does not equal one user-approval gate.

## 3. Preproduction

Before visual work, resolve:
- menu/moment;
- PROXY_EATER sensory arc;
- meal-context / cultural grammar;
- FOOD_STATE keyframe states and ordered bridge actions;
- BODY slide roles;
- which entities are visible in each slide;
- focal owner / shot scale / visual delta;
- high-risk hand/utensil/contact geometry;
- cover brief;
- lettering/copy plan.

The user approves the content/storyboard package before asset authoring begins.

## 4. Asset resolution

For each planned BODY slide:
1. list required visible entities;
2. resolve each requirement against `assets/production/registry.json`;
3. use existing approved assets if semantically adequate;
4. choose the smallest **stable** asset boundary for missing capability;
5. keep independent assets separate when deterministic placement is safe;
6. use episode-local INTERACTION_COMPOSITE when splitting high-risk contact would make geometry brittle;
7. create ASSET_GAP for only what is missing;
8. do not weaken the food beat merely to avoid a justified gap.

Before authoring, build an asset dependency DAG.
Examples of dependency types:
- a repeated-person interaction asset depends on an approved PERSON identity anchor;
- a later FOOD_STATE may depend on an earlier approved food appearance/state anchor;
- a contact asset may depend on the approved tool/food/person facts it must preserve.

Independent gaps may be authored in parallel. Dependent gaps may not be authored before their required anchors are approved/hash-bound.

Full-frame-exception need is initially `UNASSESSED`.
Do not predeclare `false` merely from storyboard confidence. Assess it only after stable asset boundaries and deterministic composition have been attempted.

## 5. Asset authoring gate

New generated/imported assets are not production assets until QC + approval + hash registration.

Apply the relevant authorities:
- PERSON style: VISUAL_SYSTEM;
- food state: FOOD_STATE_SYSTEM;
- dining/cultural consistency: MEAL_CONTEXT_SYSTEM;
- voice/copy is not baked into raster assets.

Important PASS criteria:
- correct drawing language;
- PERSON identity continuity;
- believable food form/state;
- correct Korean meal ecology where applicable;
- physically valid hand/tool/contact geometry;
- no unintended text;
- appropriate scope and crop flexibility.

Rejected output is not a reference or registry asset.

### 5.1 Approval scope

`approved_by` may be USER or AUTHORIZED_OPERATOR, but their meaning differs.

- AUTHORIZED_OPERATOR may register a QC-passed asset for bounded episode/pilot use so deterministic composition can proceed.
- USER approval is required when a result becomes a creative/identity lock, project-reusable/canonical authority, or a named user gate.
- A recurring PERSON foundation asset may be operator-approved first; the composed first anchor frame is then shown to the user.
- Only after that composed anchor frame passes may its person appearance be promoted to the episode identity anchor used for dependent interaction assets.
- If the user rejects the anchor frame, dependent authoring does not proceed and affected operator-approved assets are invalidated/replaced at minimum scope.

This preserves `generate/import → QC → approval → hash registration` without forcing one user click per raw asset.

## 6. Deterministic BODY composition

The AutoPipeline compositor owns final BODY assembly.

Scene data specifies approved asset IDs and transforms/layer order.
Meaning-bearing text remains separate.

Composition may vary:
- crop;
- x/y;
- scale;
- layer order;
- occlusion;
- pose asset;
- background exposure.

This is the first repair surface for visual repetition. Open a new pose/view ASSET_GAP only when composition cannot serve the beat.

## 7. Sequence QC

After BODY frames exist, inspect the sequence as a whole.

Required:
- PROXY_EATER appetite/sensory progression is readable;
- food state actually changes when the story claims it changes;
- neighboring frames have meaningful visual delta;
- camera/framing is not mechanically repetitive;
- PERSON identity and drawing medium remain coherent;
- tool/contact actions remain physically believable;
- no Japanese/Western dining grammar is accidentally substituted for a Korean context unless the story calls for it.

No fixed left/right/front quota.

Calibration fixture: BODY 4 slides exactly, with COVER separate. This fixed count exists only to control architecture-test variables.
Normal production has no inherited BODY=4 rule; frame count is determined by the approved sensory/food-state arc.

## 8. Cover + lettering

COVER is a mandatory product slot and is not BODY S01.

Export order:
`COVER → BODY S01 → ... → Sfinal`

Cover may reuse approved BODY/FOOD/PERSON assets or author a missing hero asset.
Title, series mark, narration and speech text remain editable composition layers.

Template calibration has two gates: placeholder review may promote one candidate to SPEC_LOCKED, but final production readiness still requires USER_LOCKED after rerender with approved pilot assets and hash-bound production font bytes. Placeholder fixtures never enter the production asset registry.

## 9. Final user gate

User reviews:
- complete carousel order;
- food/appetite effect;
- character/style coherence;
- lettering legibility;
- cover;
- any remaining semantic or anatomy defect.

PASS → EXPORT_READY.
FAIL → invalidate only the minimum affected scene/asset/template layer.

## 10. Full-frame exception

Use only when normal asset composition would materially degrade a required food/contact scene.

Record:
- scene ID;
- why composition is insufficient;
- bound references;
- retry/cost cap;
- output hash;
- approval scope.

Default scope is EPISODE_LOCAL_ONLY.
An exception output never becomes project-wide PERSON/FOOD style authority automatically.

## 11. Reset / history

A fresh episode starts without episode-local subject/food/contact assets from an older episode unless explicitly promoted.

Git history is the archive. Retired episode packages should not remain in the working tree merely as reminders.
