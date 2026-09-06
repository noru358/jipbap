# E001 PREPRODUCTION — APPROVED

Approval date: 2026-09-07
User gate: PASS
Status: ACTIVE

## 1. MENU / MOMENT

Menu: 집에서 부친 김치전 + 작은 간장 종지

Core moment:
바삭하게 익은 가장자리 조각을 젓가락으로 집어 간장은 끝에만 살짝 찍고 첫입 먹는 순간.

This episode is not a recipe explainer or story-comic reversal.
The food state and eating action are the subject.

## 2. SENSORY ROUTE

Route: PURE_SENSORY

Context atmosphere may suggest a late Korean home meal / light night snack.
Weather or human backstory must not expand into an independent narrative.

Sensory route:
바삭한 가장자리 → 촉촉한 안쪽 → 간장이 묻은 끝 → 첫입 → 다음 조각

Ending grammar: CONTINUING_BITE

## 3. MEAL CONTEXT

primary_cuisine_context: Korean home meal
meal_setting: simple late-evening home meal / snack

Entity roles:
- main: kimchi_pancake
- condiment: soy_dipping_sauce
- utensil: metal_chopsticks
- vessel_main: plain ceramic plate
- vessel_condiment: small ceramic dipping dish

Preparation:
- kimchi pancake is cooked and pre-cut into small bite-sized pieces
- browned/crisp edge remains visually distinguishable
- no recipe-process exposition

Vessel conventions:
- ordinary home ceramic ware
- no restaurant plating or advertising polish

Dining grammar:
- metal chopsticks belong to the diner area
- main plate is in front of the diner
- dipping dish sits in a naturally reachable adjacent area
- food is picked up with chopsticks
- dipping action contacts only the intended tip/edge when the shot calls for it
- world-space table topology persists unless an explicit action/state_delta changes it

Cross-context risks:
- tableware, utensil placement, vessel form, garnish or gesture must not drift into a visibly different cuisine grammar
- do not add unrelated soup, side dishes, garnish, or props merely to make the table look fuller

## 4. INITIAL MEAL_SCENE_STATE

Authority: episodes/001/MEAL_SCENE_STATE.json

Persistent topology is diner-relative/world-space, not screen-coordinate based.

## 5. BODY BEATS

### S01 — ARRIVAL
Emotional beat: the crisp edge is immediately the desirable target.
State beat: chopsticks approach edge_piece_A but do not lift it.
Camera: food-dominant close / medium-close.

### S02 — PICK
Emotional beat: choosing the best edge piece.
State beat: edge_piece_A moves plate → chopsticks.
Camera: contact-focused close shot.

### S03 — DIP
Emotional beat: personal preference for only a little sauce.
State beat: the same edge_piece_A touches sauce at its tip only; coating none → partial.
Camera: food/sauce macro.

### S04 — BITE
Emotional beat: first crisp bite.
State beat: the same bite-sized edge_piece_A moves utensil → mouth and is consumed.
Camera: food/mouth/utensil relation is primary; full face is unnecessary.

### S05 — RESIDUE / CONTINUING_BITE
Emotional beat: the hand already goes for another edge.
State beat: edge_piece_A is absent from the plate; chopsticks approach edge_piece_B.
Camera: return to plate; reduced food state must read.

## 6. CONTINUITY INVARIANTS

- S02, S03 and S04 use the same edge_piece_A.
- edge_piece_A must not teleport, revert, duplicate or lose its partial sauce coating before consumption.
- after S04, edge_piece_A is consumed and remains absent.
- S05 may target edge_piece_B only after edge_piece_A has been consumed.
- sauce dish, plate and chopstick ownership/topology persist unless explicitly changed.
- no new side dishes or utensils may appear without an explicit state change.

## 7. VOICE / COPY PLAN

Lettering is downstream only; all BODY rasters are text-free.

- S01 / OPENER: 괜히 김치전이 먹고 싶었다
- S02 / PREFERENCE: 가장자리부터
- S03 / SILENT: no text
- S04 / PREFERENCE: 간장은 끝에만
- S05 / RESIDUAL: 한 조각 더

Copy remains editable until lettering/final composition.

## 8. COVER BRIEF

COVER != S01

Working title:
김치전은 가장자리부터

Cover grammar:
- large mobile-readable title
- kimchi pancake is the visual hero
- episode character is secondary
- reuse approved BODY artwork first
- prefer suitable BODY food/character assets after raster-set approval
- create DEDICATED_COVER_HERO only if approved BODY assets are insufficient
- title and series mark remain editable composition layers
- cover must not invent a fake BODY food-state transition

## 9. USER-GATE RESULT

Pre-raster user gate: PASS

Exact next production stage:
S01_PENDING

S01 rendering remains fail-closed until actual STYLE_REF_001 media is bound to the renderer in the current execution context.
