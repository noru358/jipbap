# FOOD_STATE_SYSTEM — state-transition continuity v0.4

## 0. Why this exists

음식툰에서는 인물 continuity만으로 충분하지 않다.
음식은 컷마다 위치, 조리 상태, 파손/혼합 상태, 양이 변한다.

따라서 모든 컷을 단순한 "장면"이 아니라 **state transition**으로 정의한다.

핵심 불변식:

> previous.postconditions must be compatible with next.preconditions

## 1. Entity state model

회차마다 필요한 음식/도구 엔티티만 선언한다. 아래 필드는 예시이며 메뉴에 맞게 확장한다.

### food entity
- location: plate | bowl | on_rice | utensil | mouth | mixed | other
- integrity: intact | cut | pierced | broken | mixed
- doneness: raw | cooked | runny | set | other
- quantity: full | partial | nearly_empty | empty
- coating/sauce: none | partial | mixed

### vessel entity
- contents
- fullness
- topping

### utensil entity
- location
- holding
- active_action

## 1.5 Meal-scene state / persistent topology

음식 상태만 이어져도 식탁 전체가 컷마다 재배치되면 같은 한 끼로 보이지 않는다.
따라서 식탁이 반복 등장하는 회차는 `MEAL_SCENE_STATE`를 가진다.

`MEAL_SCENE_STATE`는 화면 좌표가 아니라 **세계 안의 상대 관계**를 저장한다.

예:
- diner 앞의 rice_bowl / soup_bowl 관계
- main_plate가 개인 영역인지 중앙 shared 영역인지
- side_dish가 어느 vessel/entity와 인접하는지
- spoon/chopsticks가 어느 식사자 영역에 속하는지
- 식탁/쟁반/상판의 지속 재질과 핵심 소품

카메라가 바뀌면 화면상의 좌우/상하 projection은 달라질 수 있다.
그러나 실제 world-space topology는 명시적 행동 없이 바뀌면 안 된다.

각 shot은 필요할 때:
- `scene_state_ref` — 이전에 확정된 meal-scene state
- `state_delta` — 이번 컷에서 실제로 바뀌는 위치/소유/잔량/접촉 상태
를 가진다.

변경 명령이 없는 persistent entity는 그대로 유지한다.
그릇을 옮기거나 접시를 당기는 등 위치 변화가 실제 행동이라면 그 변화가 action/state_delta에 기록되어야 한다.
설명 없는 재배치, 소품 생성/소실, 이전 상태 복구는 `UNEXPLAINED_SCENE_DRIFT`다.

이 구조는 특정 메뉴의 좌표를 프로젝트 전역에 하드코딩하지 않는다.
회차별 meal context가 초기 topology를 결정하고, 이후 컷은 그 상태와 delta로 이어간다.

## 2. Still-frame temporal model

정지 만화의 한 컷은 작은 동영상이 아니다.
따라서 canonical temporal truth는 `preconditions → action → postconditions` 한 줄이 아니라 다음 둘로 분리한다.

1. **KEYFRAME** — 지금 이 이미지가 정확히 무엇을 보여주는가.
2. **BRIDGE** — 이전 keyframe에서 현재 keyframe까지 어떤 물리 행동이 순서대로 일어났는가.

각 shot은 최소:
- `depicted_state` — 현재 프레임에 실제로 보여야 하는 상태
- `depicted_action_phase` — STATIC / BEFORE_ACTION / ACTION_IN_PROGRESS / AFTER_ACTION + 회차별 설명
- `transition_from_previous` — 첫 컷은 null, 이후 컷은 ordered bridge steps
- `must_show`
- `must_not_show`
를 가진다.

기존 `preconditions / action / postconditions`는 요약/호환 필드로 남을 수 있지만,
그 필드만으로 “지금 숟가락이 음식에 닿기 전인지, 닿는 중인지, 이미 떠진 뒤인지”를 추정하지 않는다.

이 구조의 목적은 특정 음식 동작을 하드코딩하는 것이 아니라,
**정지 이미지에 보이는 순간과 컷 사이에서 생략된 행동을 분리**하는 것이다.

## 3. Keyframe rule

`depicted_state`는 viewer가 현재 이미지 한 장에서 확인할 수 있어야 한다.

예:
- food.location=serving_vessel
- utensil.location=near_mouth
- food_portion.location=utensil
- bite_consumed=false

`depicted_action_phase`의 공통 phase:
- STATIC — 행동 없이 상태를 보여줌
- BEFORE_ACTION — 다음 접촉/변화 직전
- ACTION_IN_PROGRESS — 접촉/변화가 실제 진행 중
- AFTER_ACTION — 행동이 끝난 결과를 보여줌

구체적인 “무슨 행동인가”는 회차 데이터가 소유한다.
전역 시스템은 계란 깨기, 생선 가르기, 국물 붓기 같은 메뉴별 행동명을 고정하지 않는다.

## 4. Bridge rule

두 keyframe 사이 상태가 달라지면 `transition_from_previous.steps`가 그 변화를 순서대로 설명해야 한다.

각 step:
- `step_id`
- `action`
- `state_delta`
- `visibility`

visibility:
- `DEPICTED_IN_CURRENT_FRAME` — 현재 컷이 그 행동의 진행/종단 순간을 실제로 보여줌
- `IMPLIED_BETWEEN_FRAMES` — 컷 사이에서 생략되지만 상태전이 데이터에는 명시됨

핵심 엔티티 상태가 바뀌는데 대응 step이 없으면 `MISSING_BRIDGE`.

## 5. Off-frame omission policy

bridge action은 반드시 독립 컷일 필요가 없다.
다만 `IMPLIED_BETWEEN_FRAMES`는 다음 조건을 모두 만족할 때만 허용한다.

1. 물리적으로 자연스럽고 이전/다음 keyframe에서 인과가 명확하다.
2. 생략 때문에 행동 순서가 둘 이상으로 해석되지 않는다.
3. 그 행동 자체가 회차의 핵심 감각/군침 payoff가 아니다.
4. 고위험 접촉이나 의미 변화가 생략되더라도 다음 상태의 물리적 전제가 명확하다.
5. omission justification을 기록할 수 있다.

반대로 생략 때문에 “바로 먹었는지, 먼저 떴는지”처럼 순서가 모호해지면 FAIL이다.
이 경우:
- bridge step을 명시하고 현재 keyframe을 더 정확히 정의하거나,
- 그 행동이 충분한 감각 가치가 있으면 별도 컷으로 승격한다.

### Generic example

잘못된 흐름:
- S02 keyframe: food_piece remains on serving vessel
- S03 keyframe: food_piece is already on utensil near mouth
- bridge: 없음

→ `MISSING_BRIDGE`

수정:
- S02 keyframe: food_piece on serving vessel
- S03 transition:
  1. move/scoop food_piece to utensil — IMPLIED_BETWEEN_FRAMES
  2. raise utensil — DEPICTED_IN_CURRENT_FRAME
- S03 keyframe: food_piece on utensil near mouth, not yet ingested

이 구조는 음식 종류가 바뀌어도 그대로 재사용한다.

## 6. Food continuity QC

전체 무자막 세트 내부 QC에서 반드시 확인한다.

- 이전 keyframe에서 현재 keyframe으로의 모든 핵심 상태 변화가 transition steps로 설명되는가
- 현재 이미지가 `depicted_state / depicted_action_phase`를 한 가지 의미로 명확히 보여주는가
- 음식 위치가 설명 없이 순간 이동하지 않는가
- 조리/섭취 순서가 자연스러운가
- 먹은 양이 역행하지 않는가
- 깨진/섞인/소스가 묻은 상태가 원상복구되지 않는가
- 그릇/도구가 행동 논리와 맞는가
- 초기 MEAL_SCENE_STATE의 world-space 관계가 명시적 action 없이 바뀌지 않았는가
- 카메라 projection 변화와 실제 식탁 재배치를 혼동하지 않았는가
- 없던 그릇/반찬/도구가 설명 없이 생기거나 사라지지 않았는가
- 필수 bridge action이 빠지지 않았는가

하나라도 핵심적으로 실패하면 해당 컷 또는 콘티를 FAIL 처리한다.

## 7. Generalization rule

이 시스템은 "특정 음식은 항상 특정 위치/순서로 먹어야 한다" 같은 회차 종속 사실을 전역 규칙으로 저장하지 않는다.

저장할 것은:
- 각 컷은 정확한 keyframe state를 가진다
- 컷 사이 상태 변화에는 ordered bridge가 필요하다
- 생략된 micro-action도 인과에 필요하면 데이터에는 명시한다
- keyframe과 bridge의 구체 행동/상태는 회차별 실제 먹는 방식이 결정한다

즉 메뉴/문화/개인 취향이 바뀌어도 같은 상태 전이 엔진을 재사용한다.
