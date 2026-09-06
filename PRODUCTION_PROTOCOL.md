# PRODUCTION_PROTOCOL — jipbap v0.3

## 0. Operating mode

현재 기본 모드: MANUAL_VALIDATION

User-gate topology:

content/storyboard contract
→ S01 USER anchor gate
→ S02..final OPERATOR INTERNAL render/QC
→ complete text-free raster-set USER gate
→ lettering
→ final USER gate

one frame = one file 이지만 one frame = one user gate는 아니다.

## 1. Render state machine

렌더 단계는 명시적 cursor를 가진다.

PREPRODUCTION_USER_GATE
→ S01_PENDING
→ S01_APPROVED_LOCKED
→ RENDER_CURSOR=S02
→ RENDER_CURSOR=S03 ... → RENDER_CURSOR=Sfinal
→ RASTER_SET_USER_GATE
→ LETTERING
→ FINAL_USER_GATE

### Hard invariant: approved-shot immutability

사용자가 S01을 PASS하면:
- S01 status = APPROVED_LOCKED
- S01은 더 이상 생성 대상이 아니다.
- 다음 render target은 반드시 S02다.
- 이후 실패/재시도는 현재 cursor shot에만 국한한다.
- S02 실패 때문에 S01을 다시 생성하거나 수정하면 PROTOCOL_FAIL이다.

S01을 다시 만들 수 있는 유일한 조건:
- 사용자가 명시적으로 S01 승인을 철회하거나
- 사용자가 S01 재제작을 직접 지시한 경우.

운영자가 임의로 anchor 재생성을 선택할 수 없다.

## 2. Preproduction

1. MENU/MOMENT 선정
2. MEAL CONTEXT + DINING GRAMMAR compile
3. 콘텐츠 비트 작성
4. VOICE 역할/문구 작성
5. 전체 콘티 작성
6. FOOD STATE graph 작성
7. bridge action 검사
8. 전체 시각 리듬 설계
9. 사용자에게 사전 패키지 제시
10. 명시 승인 후 래스터 제작

## 3. Visual preflight

생성 전 각 컷에 대해:
- render cursor == target shot
- target shot is not already APPROVED_LOCKED
- actual style reference binding
- reference role separation
- episode continuity anchor binding if useful
- meal context + dining grammar binding
- preconditions/action/postconditions
- must_show / must_not_show
- camera/composition
- text_free=true
- single_panel=true

하나라도 빠지면 렌더 금지.

## 4. S01 gate

S01 한 장만 생성한다.
사용자가 다음을 본다.
- 스타일
- 인물
- 음식 표현 밀도
- 공간 분위기
- 인물/음식 비중
- 식탁 전체의 meal-context/dining-grammar 정합성

PASS 직후:
1. S01을 APPROVED_LOCKED로 기록
2. S01 이미지는 continuity anchor로만 승격
3. render cursor를 S02로 전진
4. 다음 사용자 게이트를 RASTER_SET_USER_GATE로 설정

## 5. Remaining render

S01 PASS 후:
- S02부터 마지막까지 한 장씩 생성
- 각 컷 생성 후 내부 구조/시각/meal-context/dining-grammar/상태 QC
- FAIL이면 같은 shot만 재시도
- PASS이면 cursor를 다음 shot으로 자동 전진
- 사용자에게 컷별 승인을 요구하지 않음

중간에 사용자를 다시 부르는 조건:
- 승인된 콘티/맛/스타일의 본질적 선택이 새로 필요한 경우
- 원래 승인 계약 자체가 잘못되어 운영자가 임의 결정할 수 없는 경우

렌더러가 반복 실패하면:
- 현재 shot의 render context/reference binding을 격리/재컴파일한다.
- 이미 PASS한 이전 shot으로 cursor를 되돌리지 않는다.

## 6. Internal QC layers

### State-machine QC
- target shot == render cursor
- approved locked shots are not regenerated
- retry scope == current shot only

### Structural output QC
- one panel / one file
- no text, including incidental readable environment text
- no collage

### Visual QC
- reference fidelity
- identity/space continuity
- shot-specific camera/composition
- food-first framing
- anti-ad rendering

### Meal-context / dining-grammar QC
- declared cuisine/meal setting consistency
- main/staple/soup/side-dish compatibility
- preparation-form plausibility
- vessel/material plausibility
- ingredient/garnish plausibility
- utensil type/material/placement plausibility
- hand/gesture/eating-action plausibility
- shared-vs-individual table topology plausibility
- cross-context contamination

### Food-state QC
- pre/post continuity
- bridge actions
- quantity/location/state monotonicity where applicable

## 7. Raster-set gate

모든 컷이 내부 PASS일 때 전체 무자막 세트를 사용자에게 제시한다.
사용자 PASS 후에만 레터링으로 넘어간다.

## 8. Lettering

VOICE_SYSTEM에 따라 텍스트를 후단에서 합성한다.
원본 래스터에 생성기로 한글을 굽지 않는다.

## 9. Final QC

- 컷 순서
- 이미지/텍스트 대응
- 모바일 가독성
- 말투 일관성
- meal-context/dining-grammar 일관성
- 음식 상태 연속성
- 최종 감정 여운
