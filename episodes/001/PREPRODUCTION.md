# E001 PREPRODUCTION — APPROVED

Status: USER_APPROVED
Approved in chat: 2026-09-07
Episode: 001
Operating mode: MANUAL_VALIDATION

## 1. MENU / MOMENT
- menu: 돼지고기 김치찌개 + 흰밥
- moment: 비 오는 늦은 저녁, 막 끓인 김치찌개에서 두부와 김치가 함께 걸린 첫 숟갈을 떠서 먹고 곧바로 다음 숟갈로 돌아가는 순간
- state arc: untouched stew → spoon enters → loaded spoon → first bite → empty spoon returns

## 2. SENSORY ROUTE
TRIGGER_TO_MEAL.
비 오는 전야를 독립 서사로 늘리지 않고 S01 안의 rainy-home cue로 압축한다.

## 3. MEAL CONTEXT + DINING GRAMMAR
- context: 현대 한국 가정식 / 1인 저녁
- main: 돼지고기 김치찌개
- staple: 흰쌀밥
- visible stew ingredients: 익은 배추김치, 두부, 돼지고기, 소량 대파
- vessels: 평범한 한국식 찌개 그릇/뚝배기 + 도자기 밥공기
- utensils: 스테인리스 숟가락 + 젓가락
- water: plain cup
- diner-relative topology: rice front-left; stew slightly front-right/forward; spoon/chopsticks diner-right; water rear-support
- cross-context risks: 일본식 나무 국그릇, 미소시루 appearance, 일본식 젓가락 배치, 중국식 상차림, 불필요한 과대 반찬상

## 4. INITIAL MEAL_SCENE_STATE
- jjigae: nearly full, intact, surface largely undisturbed
- rice_bowl: full
- spoon: resting at diner-right
- chopsticks: resting beside spoon
- water: rear-support
- diner: seated
- background: simple home interior + rainy window cue; no readable text

Persistent world-space entities do not move without an explicit state_delta/action.

## 5. EPISODE_SUBJECT_LOCK PLAN
Recurring subject detected: DINER_01 appears in 2+ BODY shots.
See SUBJECT_LOCK.md.

## 6. BODY EMOTIONAL / STATE BEATS
- S01 ARRIVAL/TRIGGER: rainy-home context + untouched stew + quiet anticipation
- S02 PREP/CONTACT: spoon enters stew and first disturbs surface
- S03 TRANSFORMATION/SCOOP: tofu + kimchi + pork + broth lifted as one spoonful
- S04 BITE: spoon reaches mouth; first bite
- S05 CONTINUING_BITE: empty spoon returns toward stew; end on next action, not evaluation

Ending grammar: CONTINUING_BITE.

## 7. VISUAL COVERAGE PLAN
| Shot | Focal owner | Scale | Camera relation | Visual delta |
|---|---|---|---|---|
| S01 | stew + diner context | medium-close | slightly elevated 3/4 table view | establishment |
| S02 | broth/spoon contact | macro | oblique over stew surface | person-context → food/contact macro |
| S03 | loaded spoon | close | low-ish side/3/4 on spoonful | pot interior → spoonful suspended above vessel |
| S04 | spoon→mouth | tight close | diner-side 3/4 | food-only emphasis → ingestion contact |
| S05 | return-to-stew meal context | medium / high-oblique | table relation visible | tight contact → wider cycle closure |

Adjacent low-delta review: PASS at planning stage.
No fixed left/right/front quota is used.

## 8. GEOMETRY RISK / CONTACT CHAINS
- S01 LOW: shoulder → forearm → resting hand; no hidden impossible anatomy
- S02 MEDIUM: forearm → wrist → hand → spoon grip → spoon bowl → broth
- S03 HIGH: arm → wrist → grip → spoon bowl → tofu/kimchi/pork
- S04 HIGH: shoulder → upper arm → elbow → forearm → wrist → hand → spoon → food → lips
- S05 MEDIUM: hand → empty spoon → return trajectory toward pot

## 9. BODY STORYBOARD
### S01
pre: meal untouched; utensils resting
action: diner sits ready to begin
post: no meal-state change
must_show: untouched stew focal, DINER_01, Korean home meal context
must_not: eaten residue, text, ad gloss

### S02
pre: spoon has been naturally picked up from resting state
action: spoon enters stew
post: spoon in stew; broth surface disturbed
must_show: physical spoon↔broth contact
must_not: loaded spoon already near mouth

### S03
pre: spoon inside stew
action: scoop tofu + kimchi + pork + broth
post: one spoonful removed and held above vessel
must_show: food physically supported by spoon
must_not: floating ingredients

### S04
pre: loaded spoon above pot
action: move spoon to mouth and take first bite
post: food moves spoon→mouth; spoon becomes empty
must_show: physically coherent first-bite contact
must_not: spoon/hand/face penetration, duplicated utensil

### S05
pre: empty spoon after first bite
action: return spoon toward stew
post: next scoop imminent
must_show: post-bite food surface + continuation action
must_not: unexplained rice loss, moved vessels, new side dishes

Bridge-action review: PASS at planning stage.

## 10. COVER BRIEF
- mandatory separate COVER slot
- initial source route: BODY_REUSE
- preferred hero candidate: approved BODY S01 if composition remains sufficient
- draft title: 비 오는 밤, 김치찌개
- 4:5; large editable title; food hero first; DINER_01 secondary; rainy-home context minimal
- if BODY reuse proves inadequate after raster-set approval, re-evaluate route before dedicated generation

## 11. VOICE / COPY PLAN
- S01 OPENER: "비 오니까 이게 생각났다."
- S02 SILENT
- S03 PREFERENCE: "첫 숟갈은 두부까지."
- S04 SILENT
- S05 RESIDUAL: "국물 한 번 더."

Voice/copy remains composition-stage material and must not be sent to BODY image generation.

## Approval binding
This preproduction package was explicitly approved by the user before BODY S01 generation.
