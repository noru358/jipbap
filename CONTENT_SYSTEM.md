# CONTENT_SYSTEM — jipbap v0.5

## 0. Runtime role

This file is the active creative planning guide under `CURRENT_STATE.md` and `JIPBAP_V1_SPEC.md`.
It does not override frozen V1 format, approval points, style authorities, or PRESENTATION_MASTER_FIRST.

## 1. Product promise

집밥은 사건을 억지로 완결하는 썰툰이 아니라 **만화 속 인물이 독자 대신 먹어주는 음식 경험**이다.
음식의 감각, 실제 사람이 하는 말, 인물의 행동, 화면의 읽기 흐름을 우선한다.
감동·갈등·반전·교훈·펀치라인은 필요한 회차에서만 쓴다. 매 화 의무 구조가 아니다.

## 2. Input policy — food name is enough

사용자가 음식명만 줘도 PLAN을 만들 수 있어야 한다. 다음 정보는 있으면 활용하지만 필수 입력 양식으로 요구하지 않는다.
- 당시 상황
- 기억나는 온도·식감·향·맛 같은 감각
- 실제로 한 말
- 예상과 달랐던 점이나 작은 선택

PLAN에는 사용자가 직접 준 사실과 AI가 합리적으로 보충한 설정을 구분한다.
- `USER_GIVEN`: 사용자가 직접 제공한 경험/문구/상황
- `AI_FILLED`: 장면 연결을 위해 보충한 가설적 설정

정보가 부족하다는 이유만으로 질문을 늘리지 않는다. 음식에서만 성립하는 순간을 먼저 잡고 합리적인 기본안을 제시한다.
이야기 방향이 아직 없을 때만 서로 다른 방향을 최대 2개 제시하고 하나를 추천한다.
사용자가 이미 이야기·구조·실제 경험을 줬다면 그것을 우선하며 대안 제시를 생략한다.

## 3. Food-specific moment first

기획의 첫 질문은 **왜 하필 이 음식이어야 이 장면이 성립하는가?** 이다.
작은 욕심, 예상과 실제, 생활의 제약, 관계의 습관, 감각의 순간 등은 사용할 수 있는 재료이지 고정 분류가 아니다.

좋은 BODY 비트는 적어도 하나를 한다.
- 음식 상태를 의미 있게 바꾼다.
- 이전에 없던 감각 정보를 준다.
- 먹고 싶은 욕구를 높인다.
- 앞선 기대의 payoff를 준다.
- 인물/관계의 실제 반응을 짧게 보여 음식 순간을 더 구체화한다.

절차상 필요하다는 이유만으로 모든 미세 행동을 독립 컷으로 만들지 않는다.

## 4. Storyboard as image + text co-design

BODY 6칸은 고정 렌더 표면일 뿐 고정 사건 슬롯이 아니다. 장면마다 아래 정보를 **필요한 만큼** 함께 설계한다.

- `new_event`: 이 장면에서 새로 생기는 일
- `action_food_state`: 인물의 행동과 현재 음식 상태
- `copy_elements`: 실제 문구, 화자, 역할(`speech` / `inner_thought` / `narration` / `sfx`)
- `visual_focus`: 화면 거리, 카메라 관계, 시선의 중심
- `copy_space_hint`: 대략적인 글 공간. 좌표 확정이 아니라 배치 의도
- `protect_regions`: 가리면 안 되는 얼굴·손·음식 등 핵심 대상
- `reading_order`: 글 요소가 여러 개일 때의 읽는 순서
- `sensory_payload`: 이 장면에서 실제로 전달할 감각이 있을 때만 기록
- `continuity_note`: 앞뒤 선후관계에서 꼭 지켜야 할 것만 기록

기존 `focal owner`, `shot scale`, `camera relation`, `visual delta`, `observable cues`가 이미 같은 의미를 담는다면 새 필드를 중복해서 만들지 않는다.
콘티 단계의 `copy_space_hint`와 `protect_regions`는 soft hint다. 최종 x/y, 행갈이, 꼬리 좌표는 PRESENTATION_MASTER/최종 composition에서 확정한다.

가능하면 1080×1350과 같은 4:5 화면의 축소 콘티로 글과 그림의 관계를 검토한다.
챗모드에서 시각 콘티가 비효율적이면 장면별 배치 설명만으로 진행해도 된다. 콘티 전용 앱은 선행 조건이 아니다.

중요:
- 실제 2×3 BOARD 생성물에는 글자·말풍선·캡션을 넣지 않는다.
- 글 공간을 모든 컷의 상단 빈 띠로 통일하지 않는다.
- 장면마다 글의 위치는 focal subject와 읽기 흐름에 맞춘다.
- 화면 거리·표정·무언 컷 수를 quota로 고정하지 않는다.
- 조사 대상 작가의 그림체를 섞거나 새 reference authority를 추가하지 않는다.

## 5. Continuity without a new DAG

복잡한 행동 DAG를 새로 만들지 않는다. 앞뒤 컷이 물리적으로 성립하는 데 필요한 최소 상태만 본다.
- 현재 음식 상태
- 현재 보이는 행동
- 직전 필수 선행 상태
- 다음에 보일 수 있는 결과

먹기 전 장면에서는 냄새·외형·온기·기대는 말할 수 있지만, 실제 섭취가 보이거나 이전 컷에서 확립되기 전 맛·식감·aftertaste를 이미 느꼈다고 쓰지 않는다.
손·도구·음식·입의 접촉 관계가 보이면 해부학과 물리 연결을 확인한다.
식문화·그릇·수저·배치는 현재 meal context를 따른다. 한 회차의 정답을 전역 하드코딩하지 않는다.

## 6. Visual rhythm

같은 중경·같은 얼굴 크기·같은 손 위치가 의미 없이 반복되면 `VISUAL_REDUNDANCY_RISK`로 본다.
해결 순서는 컷 합치기 → 더 적합한 카메라/초점 관계 탐색 → 연속성을 위해 유사 구도가 필요한 경우 이유 기록이다.
다양성 자체가 목적이 아니다. 카메라·구도·포즈·표정·손·배경은 장면 역할에 맞게 자유롭게 설계한다.

## 7. Ending

마지막 컷에 `잘 먹었다`, 감동 문구, 교훈, 반전을 자동으로 붙이지 않는다.
다음 한입, 남은 음식 상태, 감각의 잔상, 현실 복귀 등 그 회차에 자연스러운 지점에서 끝내면 된다.

## 8. Board / presentation boundary

콘티는 BOARD가 보여줄 그림과 후단 lettering을 함께 설계하지만 산출물의 책임은 분리한다.
- BOARD: 무문자 2×3, 승인된 PERSON/FOOD 스타일 범위와 장면 상태를 전달
- EXTRACT/FIT: 실제 panel boundary를 사용하고 accepted raster를 stretch하지 않음
- PRESENTATION_MASTER: 최종 문구, 행갈이, 말풍선, 타이포, 읽기 흐름을 quality-first로 설계
- EDITABLE_RECONSTRUCTION: 승인 그림·승인 문구를 그대로 두고 presentation intent를 editable scene으로 재구성

기획 품질 개선은 다음 신규 화에서 평가한다. 현재 진행 중인 승인 에피소드의 이야기/이미지/승인 상태를 이 문서 개정만으로 다시 열지 않는다.
