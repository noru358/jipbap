# Episode 002 — 고등어구이 + 흰밥

Status: S02_RENDER_BLOCKED_INTERNAL_QC

## Menu / moment

막 구운 고등어를 젓가락으로 가르고, 껍질 아래 살을 크게 떼어 흰밥 위에 올려 먹는 순간.

## Meal context

Context ID: E002_KOREAN_HOME_DINNER

- primary_cuisine_context: Korean home meal
- meal_setting: ordinary evening home dinner
- main: grilled mackerel
- staple: white rice
- soup_or_stew: Korean doenjang-based soup/stew family
- sides: ordinary Korean banchan family
- vessel_conventions: ceramic/porcelain home tableware compatible with the rice bowl/table setting; no foreign-context vessel styling without a reason
- preparation_forms: side dishes must use Korean home-meal preparation forms appropriate to the named dish
- cross_context_risks:
  - visually similar Japanese meal conventions being imported by the image model
  - Japanese-style rolled egg replacing Korean gyeran-mari
  - lacquer/wooden miso-soup bowl styling
  - miso-soup ingredient/garnish conventions appearing in a declared Korean doenjang soup

This is episode-specific context, not a project-wide rule about every Korean meal.

## Content beats

5컷.

### S01 — arrival
User verdict: PASS

State:
- mackerel.location=main_plate
- mackerel.skin=intact
- mackerel.flesh=mostly_intact
- rice.fullness=full

Meal-context constraints:
- entire table must read as Korean home dinner
- Korean-style gyeran-mari if rolled egg is present
- doenjang soup/stew uses Korean home-meal vessel/ingredient presentation
- no cross-context Japanese meal styling

### S02 — crack / open
- pre: mackerel.skin=intact, flesh=mostly_intact
- action: split_skin_and_flesh_with_chopsticks
- post: mackerel.skin=opened, flesh=exposed, one_flake=separated_or_ready
- composition: food macro / oblique close-up
- context: preserve E002_KOREAN_HOME_DINNER table identity; no unrelated side-dish drift

### S03 — place on rice
- pre: one_flake=separated, rice.fullness=full_or_near_full
- action: place_fish_on_rice
- post: one_flake.location=on_rice, mackerel.flesh=partially_removed
- composition: top-oblique food close-up
- context: same rice/tableware/meal context as S01

### S04 — bite
- pre: one_flake.location=on_rice
- action: take_bite_with_rice_and_fish
- post: rice.fullness=partial, placed_flake=consumed_or_partial
- composition: eating medium close-up
- context: same character/meal identity; no ad-like reaction

### S05 — residue
- pre: rice.fullness=partial_or_less, mackerel.flesh=partially_consumed
- action: continue_eating_offscreen_between_beats
- post: rice.fullness=nearly_empty_or_empty, mackerel=mostly_bones_and_small_remnants
- composition: quiet aftermath / table close-up
- context: leftovers must still read as the same Korean home dinner

## Voice draft

- S01: 오늘은 고등어 한 마리
- S02: 껍질부터 젓가락이 간다
- S03: 살은 크게 떼어서
- S04: 무자막
- S05: 가시만 남았다

## Bridge-action check

PASS.

main_plate → separated → on_rice → consumed is action-accounted.
Food quantity/integrity may decrease but must not reset.

## Gate history

- PREPRODUCTION_USER_GATE: PASS
- S01 initial render: style PASS, meal-context FAIL
- structural fix: MEAL_CONTEXT_SYSTEM.md added; context QC promoted to canonical pipeline
- S01 corrected render: USER PASS

## Current render status

S01: PASS
S02: INTERNAL QC BLOCKED — repeated renderer failures; rejected outputs are not assets.
S03~S05: NOT STARTED because S02 must pass first.

See episodes/002/QC_LOG.md.

## Exact next action

Retry S02 one frame at a time using:
- STYLE_REF_001 actual session-bound binary
- S01 approved Episode 002 anchor
- E002_KOREAN_HOME_DINNER meal context
- single-panel, text-free, 4:5 output
- per-shot internal structural + visual + meal-context + food-state QC

Do not ask for per-shot user approval unless the approved contract itself becomes ambiguous.
