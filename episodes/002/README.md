# Episode 002 — 고등어구이 + 흰밥

Status: POST_S01_INTERNAL_RENDER
Render cursor: S02
Next user gate: RASTER_SET

## Gate state

- PREPRODUCTION_USER_GATE: PASS
- S01: APPROVED_LOCKED
- S01 regeneration: FORBIDDEN unless user explicitly invalidates approval
- S02~S05: operator internal render/QC
- per-shot user gate: NONE

Machine-readable state:
- episodes/002/RENDER_STATE.json

## Menu / moment

막 구운 고등어를 젓가락으로 가르고, 껍질 아래 살을 크게 떼어 흰밥 위에 올려 먹는 순간.

## Meal context

Context ID: E002_KOREAN_HOME_DINNER

### Core meal ecology
- primary_cuisine_context: Korean home meal
- meal_setting: ordinary evening home dinner
- main: grilled mackerel
- staple: white rice
- soup_or_stew: Korean doenjang-based soup/stew family
- sides: ordinary Korean banchan family
- vessels: ceramic/porcelain Korean-home tableware
- no Japanese-style grated-daikon/shiso/miso-bowl plating unless explicitly selected

### Compiled dining grammar for this episode
- utensil set: Korean spoon + chopsticks; metal is the default visual choice for this episode
- placement: spoon/chopsticks together at the diner’s right side rather than a Japanese-style horizontal chopstick-rest presentation
- table topology: individual rice and soup; main/side dishes arranged as Korean home-table shared dishes where visible
- pre-meal gesture: do not use Japanese-style palms-pressed-together/itadakimasu pose as the default
- natural hand state: relaxed hands, reaching for chopsticks/spoon, or performing the current food action
- current action authority always overrides generic pre-meal posing

These are E002 compiled constraints, not global rules for every Korean meal.

### Cross-context risks
- Japanese-style horizontal chopstick placement on a chopstick rest
- wooden/lacquer miso-soup bowl
- miso-soup garnish/ingredient language
- Japanese rolled-egg presentation replacing Korean gyeran-mari
- palms-together pre-meal pose
- grated daikon + shiso + lemon garnish package on grilled fish

## Shot contracts

### S01 — arrival
Status: APPROVED_LOCKED
- full Korean-home-dinner table
- corrected cultural presentation approved by user
- role after PASS: CONTINUITY_ANCHOR only
- must not become S02 edit target or composition template

### S02 — crack/open
Status: RENDER_CURSOR
- pre: mackerel.skin=intact, flesh=mostly_intact
- action: split_skin_and_flesh_with_chopsticks
- post: mackerel.skin=opened, flesh=exposed, one_flake=separated_or_ready
- composition: food macro / oblique close-up
- must show: chopstick tips physically prying the browned skin and white flesh at the contact point
- must not show: S01 full-table pose, palms-together pose, readable text, fish already on rice
- reference roles:
  - STYLE_REF_001 = STYLE_AUTHORITY
  - S01 = CONTINUITY_ANCHOR, is_edit_target=false

### S03 — place on rice
- pre: one_flake=separated
- action: place_fish_on_rice
- post: one_flake.location=on_rice, mackerel.flesh=partially_removed
- composition: top-oblique food close-up

### S04 — bite
- pre: one_flake.location=on_rice
- action: take_bite_with_rice_and_fish
- post: rice.fullness=partial
- composition: eating medium close-up

### S05 — residue
- pre: rice.fullness=partial_or_less
- action: continue_eating_between_beats
- post: rice.fullness=nearly_empty_or_empty, mackerel=mostly_bones_and_small_remnants
- composition: quiet aftermath

## Voice draft

- S01: 오늘은 고등어 한 마리
- S02: 껍질부터 젓가락이 간다
- S03: 살은 크게 떼어서
- S04: 무자막
- S05: 가시만 남았다

## Exact next action

Render S02 only.
If S02 FAILS, retry S02 only.
If S02 PASSES, advance cursor to S03 automatically.
Continue through S05 without a user gate.
Then present S01~S05 text-free set at RASTER_SET gate.
