# MEAL_CONTEXT_SYSTEM — culinary/cultural coherence v0.1

## 0. Purpose

음식툰의 한 끼는 메뉴 하나만 맞으면 되는 것이 아니다.
메인 음식, 밥/면 같은 주식, 국·찌개, 반찬, 조미료, 그릇 재질, 담는 방식까지 한 식탁의 meal ecology로 읽힌다.

따라서 음식 상태 연속성(FOOD_STATE_SYSTEM.md)과 별도로,
모든 회차는 렌더 전에 meal-context contract를 가진다.

이 시스템의 목적은 특정 문화의 음식 규칙을 전역 하드코딩하는 것이 아니라,
회차가 선언한 음식/지역/가정식 맥락에 맞는 조합을 동적으로 구성하고 검수하는 것이다.

## 1. Episode-level meal context

각 회차는 최소 다음을 선언한다.

- primary_cuisine_context: 한식, 일식, 중식, 특정 지역/가정식 등
- meal_setting: 집밥, 식당, 도시락, 야식 등
- entity_roles: main / staple / soup_or_stew / side / condiment / drink
- preparation_forms: 해당 맥락에서 자연스러운 조리·절단·제공 형태
- vessel_conventions: 그릇/접시/냄비의 재질·형태 범위
- ingredient_constraints: 핵심 재료와 허용/비선호 재료
- cross_context_risks: 모델이 다른 음식 문화의 시각 관습을 섞기 쉬운 지점

## 2. Plausibility, not stereotype

meal-context contract는 하나의 정답 사진을 강제하지 않는다.

검수 기준은:
- 해당 식문화 안에서 실제로 가능한가
- 같은 한 끼의 다른 음식과 함께 놓였을 때 자연스러운가
- 그릇/담음새가 음식 역할과 맞는가
- 다른 식문화의 대표적 표현을 무심코 끌어오지 않았는가

지역·가정·개인별 변형이 가능한 부분은 허용한다.
불확실한 사항을 임의의 고정 규칙으로 승격하지 않는다.

## 3. Preproduction compile

MENU/MOMENT가 정해지면 콘티 전에 meal context를 컴파일한다.

1. 주 음식의 문화/지역/상황 맥락을 정의
2. 함께 등장할 모든 음식 엔티티의 역할을 정의
3. 각 엔티티의 조리 형태·재료·그릇 범위를 정의
4. 서로 충돌하는 조합이나 cross-context contamination 위험을 체크
5. 컷별 meal_context.constraints로 필요한 항목만 내려보냄

이 단계가 없으면 식탁 전체가 등장하는 래스터 생성은 금지한다.

## 4. Render contract

각 shot contract는 해당 컷에 적용되는 meal context를 포함한다.

예시 형식:
- meal_context.context_id
- meal_context.constraints[]

constraints는 음식별/그릇별/담음새별로 구체적이어야 한다.

예:
- soup vessel must match the declared home-meal context
- side dish preparation form must match the declared cuisine context
- do not import garnish/ingredients solely from a visually similar foreign dish

중요: 위 문장은 구조 예시이며 특정 메뉴의 전역 규칙이 아니다.

## 5. Context QC

각 컷 생성 후 다음을 확인한다.

- 메인/주식/국·찌개/반찬의 조합이 같은 meal context로 읽히는가
- 조리 형태가 선언된 음식과 맞는가
- 그릇 재질/형태가 음식 역할 및 식문화와 맞는가
- 재료·고명·색감이 시각적으로 유사한 타 문화 음식으로 오인될 만한가
- 이전 컷과 식탁 구성의 문화적 정체성이 흔들리지 않는가

핵심 오류가 있으면 visual quality가 좋아도 FAIL이다.

## 6. Generalization rule

전역에 저장할 것은:
- 모든 회차는 meal context를 선언한다
- 식탁은 개별 음식이 아니라 조합 전체로 검수한다
- 조리 형태·재료·그릇·담음새도 문화적 문맥의 일부다
- cross-context contamination을 명시적으로 검사한다

전역에 저장하지 않을 것은:
- 특정 국에는 특정 재료가 절대 들어가지 않는다
- 특정 문화는 특정 그릇만 쓴다
- 한 회차의 취향/구성을 다른 회차의 절대 규칙으로 복제하는 것

회차별 실제 메뉴와 상황이 intended context를 결정한다.
