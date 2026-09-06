# MEAL_CONTEXT_SYSTEM — culinary/cultural coherence v0.2

## 0. Purpose

한 끼의 문화적 정합성은 메뉴명만으로 결정되지 않는다.

메인 음식, 주식, 국·찌개, 반찬, 조미료, 그릇, 수저, 수저 배치, 손동작, 먹기 전/먹는 중 제스처, 공동/개인 접시 구조까지 함께 하나의 dining grammar를 만든다.

따라서 모든 회차는 렌더 전에 meal-context + dining-grammar contract를 컴파일한다.

이 시스템의 목적은 특정 문화의 규칙을 프로젝트 전역에 하드코딩하는 것이 아니라,
회차가 선언한 문화/지역/가정식/식당 맥락을 렌더 가능한 구체적 제약으로 변환하는 것이다.

## 1. Episode-level meal context

각 회차는 최소 다음을 선언한다.

- primary_cuisine_context
- meal_setting
- entity_roles: main / staple / soup_or_stew / side / condiment / drink
- preparation_forms
- vessel_conventions
- ingredient_constraints
- garnish_constraints
- dining_grammar
- cross_context_risks

## 2. Dining grammar

dining_grammar는 최소 다음을 포함한다.

### utensil system
- utensil types
- material
- pairing
- resting/placement convention
- orientation relative to rice/soup/table edge

### table topology
- rice/soup/main/side의 대략적 역할별 위치
- shared dishes vs individual dishes
- 개인 앞자리와 중앙 영역의 구분

### gesture grammar
- 먹기 전 기본 손 위치
- 음식을 집을 때 자연스러운 손동작
- 해당 문화 맥락과 충돌하는 대표적 제스처
- 특정 제스처를 모든 사람에게 고정하지 않도록 variation 허용

### serving/eating grammar
- 어떤 도구로 어떤 음식을 먹는가
- main/side를 옮기거나 집는 방식
- bowl을 드는지/식탁에 두는지 등 해당 회차에 중요한 행동 규칙

## 3. Classification is not enough

"Korean", "Japanese", "Chinese" 같은 라벨만 renderer에 넘기면 FAIL 가능성이 높다.

반드시 라벨을:
- 음식 형태
- 그릇
- 수저
- 배치
- 손동작
- 금지해야 할 cross-context visual priors
로 compile한다.

즉 cuisine classification은 metadata이고,
실제 생성에는 compiled dining grammar가 authority다.

## 4. Plausibility, not stereotype

contract는 하나의 정답 사진을 강제하지 않는다.

검수 기준:
- 해당 식문화 안에서 실제로 가능한가
- 같은 한 끼의 다른 음식과 함께 자연스러운가
- 그릇/수저/배치/손동작이 서로 같은 문화 문맥으로 읽히는가
- 다른 식문화의 대표적 시각 문법이 무심코 섞이지 않았는가

지역·가정·개인별 변형은 허용한다.
불확실한 사항을 전역 절대 규칙으로 승격하지 않는다.

## 5. Preproduction compile

MENU/MOMENT 확정 후:
1. 문화/지역/식사상황 정의
2. 음식 entity 역할 정의
3. 조리 형태·재료·그릇 범위 정의
4. utensil/table topology/gesture grammar 정의
5. cross-context contamination risk 정의
6. 각 shot에 필요한 제약만 내려보냄

이 단계가 없으면 식탁 또는 식사 행동이 등장하는 렌더 금지.

## 6. Render contract

각 shot은:
- meal_context.context_id
- meal_context.constraints[]
- meal_context.dining_grammar[]
를 가진다.

현재 shot에 보이지 않는 요소까지 억지로 넣지는 않는다.
하지만 화면에 등장하는 음식·그릇·수저·손동작은 모두 compiled grammar와 호환되어야 한다.

## 7. Context QC

각 컷 생성 후:
- 음식 조합이 같은 meal context로 읽히는가
- 조리 형태가 맞는가
- 그릇 재질/형태가 맞는가
- 재료/고명이 타 문화 음식으로 drift하지 않았는가
- 수저 종류/재질/배치가 맞는가
- 손/몸 제스처가 해당 식사 맥락과 맞는가
- 식탁 topology가 자연스러운가
- 이전 컷과 문화적 정체성이 흔들리지 않는가

핵심 오류가 있으면 작화가 좋아도 FAIL.

## 8. Generalization rule

전역에 저장할 것:
- 모든 회차는 dining grammar를 compile한다
- 식탁은 음식+그릇+수저+배치+행동 전체로 검수한다
- cross-context contamination을 명시적으로 검사한다

전역에 저장하지 않을 것:
- 특정 문화는 언제나 특정 손동작만 쓴다
- 특정 음식에는 특정 재료가 절대 들어가지 않는다
- 한 회차의 배치를 다른 회차의 절대 규칙으로 복제한다

회차별 실제 메뉴와 상황이 intended grammar를 결정한다.
