# FOOD_STATE_SYSTEM — state-transition continuity v0.1

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

## 2. Shot contract

각 컷은 최소 다음을 가진다.

- `preconditions`
- `action`
- `postconditions`
- `must_show`
- `must_not_show`

컷의 감정적 역할과 별도로 존재한다.

## 3. Preconditions

행동은 전제 상태가 맞을 때만 허용한다.

예: `break_yolk`
- egg exists
- egg.yolk == intact
- egg.location == intended_serving_location
- relevant utensil visible/usable

이번 Episode 001에서 `break_yolk`의 intended_serving_location은 `on_rice`다.
이 값은 해당 회차의 먹는 방식에서 결정되며 프로젝트 전역 하드코딩이 아니다.

## 4. Postconditions

행동 후 상태를 반드시 기록한다.

예:
- egg.yolk: intact → pierced/runny
- rice.topping: egg_on_top
- sauce: none → partial
- bowl.fullness: full → partial

다음 컷은 이 결과와 모순되면 안 된다.

## 5. Bridge action detection

콘티의 두 비트 사이에 필요한 물리 행동이 빠졌는지 검사한다.

### Rule
두 컷 사이에서 핵심 엔티티의 위치/상태가 바뀌는데, 그 변화를 설명하는 action이 없으면 `MISSING_BRIDGE`다.

해결 방법:
1. 빠진 행동을 독립 컷으로 추가하거나
2. 다음 컷의 precondition에 이미 완료된 상태를 명확히 포함하고, 시각적으로 자연스럽게 이해 가능한 생략인지 확인한다.

### Episode 001 example
잘못된 흐름:
- S02: egg.location=plate, yolk=broken
- S03: egg.location=on_rice

문제: `plate → on_rice` 이동 action 없음.

수정 흐름:
- S01 post: egg.location=plate, yolk=intact
- bridge: place_egg_on_rice
- S02 pre: egg.location=on_rice, yolk=intact
- S02 action: break_yolk
- S02 post: egg.location=on_rice, yolk=runny

bridge는 별도 컷이 아닐 수도 있다. 단, 다음 컷의 시작 상태가 자연스럽고 명시적으로 보여야 한다.

## 6. Food continuity QC

전체 무자막 세트 내부 QC에서 반드시 확인한다.

- 이전 컷 post-state와 다음 컷 pre-state가 호환되는가
- 음식 위치가 설명 없이 순간 이동하지 않는가
- 조리/섭취 순서가 자연스러운가
- 먹은 양이 역행하지 않는가
- 깨진/섞인/소스가 묻은 상태가 원상복구되지 않는가
- 그릇/도구가 행동 논리와 맞는가
- 필수 bridge action이 빠지지 않았는가

하나라도 핵심적으로 실패하면 해당 컷 또는 콘티를 FAIL 처리한다.

## 7. Generalization rule

이 시스템은 "계란은 밥 위에서 깨야 한다"를 전역 규칙으로 저장하지 않는다.

저장할 것은:
- 음식 행동에는 precondition이 있다
- 상태 변화에는 postcondition이 있다
- 컷 사이 상태 변화에는 bridge가 필요하다
- 회차별 실제 먹는 방식이 intended state를 결정한다

즉 메뉴/문화/개인 취향이 바뀌어도 같은 상태 전이 엔진을 재사용한다.
