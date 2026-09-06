# PRODUCTION_PROTOCOL — jipbap v0.4

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

## 2. Current-shot render capsule

이미지 생성기는 전체 에피소드 문맥을 직접 받지 않는다.
각 렌더 호출 전에 current-shot-only capsule을 컴파일한다.

### ALLOWLIST
렌더러에 전달 가능한 정보:
1. target_shot_id
2. current shot의 preconditions/action/postconditions
3. current shot의 must_show/must_not_show
4. current shot의 camera/composition
5. STYLE_AUTHORITY
6. 최소 continuity facts
   - 동일 인물 identity facts
   - 현재 음식/식기 상태
   - 필요한 공간/소품 continuity
7. current shot에 필요한 meal-context/dining-grammar subset
8. output contract
   - one panel
   - one file
   - text free

### DENYLIST
렌더러 입력에서 제외:
- 전체 에피소드 storyboard
- future shots
- current shot 이후의 state
- VOICE/lettering copy
- 이전 컷의 자막/대사
- 사용자 승인용 전체 패키지
- rejected render attempts
- APPROVED_LOCKED shot을 edit target로 쓰는 이미지 바인딩
- 현재 컷에 불필요한 식탁/배경 디테일

이 원칙을 위반하면 RENDER_CONTEXT_LEAK_FAIL이다.

## 3. Manual/chat execution fail-closed

현재 실행 환경이 렌더 입력을 current-shot capsule로 격리할 수 없고
전체 대화/전체 에피소드 문맥이 이미지 생성에 섞이는 것이 확인되면:

- 같은 환경에서 무한 재시도하지 않는다.
- rejected output을 reference로 재사용하지 않는다.
- 이전 approved shot을 다시 만들지 않는다.
- 상태를 RENDER_CONTEXT_UNSAFE로 기록한다.
- context isolation이 가능한 새 render context에서 같은 cursor shot부터 재개한다.

중요:
context reset은 episode reset이 아니다.
GitHub의 render cursor/locked shots를 복원한 후 S02부터 그대로 이어간다.

## 4. Preproduction

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

## 5. Visual preflight

생성 전:
- render cursor == target shot
- target shot is not APPROVED_LOCKED
- current-shot render capsule compiled
- DENYLIST fields absent
- actual style reference binding
- reference role separation
- meal context + dining grammar binding
- text_free=true
- single_panel=true

하나라도 실패하면 렌더 금지.

## 6. S01 gate

S01 한 장만 생성한다.

PASS 직후:
1. S01 = APPROVED_LOCKED
2. S01 = CONTINUITY_ANCHOR only
3. render cursor = S02
4. next user gate = RASTER_SET

## 7. Remaining render

S01 PASS 후:
- S02부터 마지막까지 한 장씩 생성
- current-shot capsule만 사용
- 각 컷 내부 QC
- FAIL이면 같은 shot만 재시도
- PASS이면 cursor 자동 전진
- 컷별 사용자 승인 없음

렌더러가 반복 실패하면:
- current-shot capsule/reference binding을 재컴파일
- context leak 여부 검사
- 이전 PASS shot으로 돌아가지 않음

## 8. Internal QC layers

### State-machine QC
- target shot == render cursor
- approved locked shots are not regenerated
- retry scope == current shot only

### Render-context QC
- no future-shot content
- no voice/lettering content
- no rejected outputs as references
- no locked-shot edit target
- only minimal continuity facts

### Structural output QC
- one panel / one file
- no text, including incidental readable environment text
- no collage

### Visual QC
- reference fidelity
- shot-specific camera/composition
- action visibly realized
- food-first framing
- anti-ad rendering

### Meal-context / dining-grammar QC
- cuisine/meal-setting consistency
- preparation/vessel/ingredient/garnish plausibility
- utensil type/material/placement plausibility
- hand/gesture/eating-action plausibility
- table topology plausibility
- cross-context contamination

### Food-state QC
- pre/post continuity
- bridge actions
- quantity/location/state monotonicity

## 9. Raster-set gate

모든 컷 내부 PASS 후 전체 무자막 세트를 사용자에게 제시한다.
사용자 PASS 후 레터링.

## 10. Lettering / final

VOICE_SYSTEM으로 후단 합성.
최종 QC:
- 컷 순서
- 이미지/텍스트 대응
- 모바일 가독성
- 말투
- meal/dining grammar
- food-state continuity
- 감정 여운
