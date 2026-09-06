# PRODUCTION_PROTOCOL — jipbap v0.6

## 0. Operating mode

현재 기본 모드: MANUAL_VALIDATION

User-gate topology:

content/storyboard contract
→ BODY S01 USER anchor gate
→ BODY S02..final OPERATOR INTERNAL render/QC
→ complete BODY text-free raster-set USER gate
→ mandatory COVER acquisition/assembly + BODY lettering
→ final CAROUSEL USER gate

one frame = one file 이지만 one frame = one user gate는 아니다.

## 1. Render state machine

렌더 단계는 명시적 cursor를 가진다.

PREPRODUCTION_USER_GATE
→ S01_PENDING
→ S01_APPROVED_LOCKED
→ RENDER_CURSOR=S02
→ RENDER_CURSOR=S03 ... → RENDER_CURSOR=Sfinal
→ RASTER_SET_USER_GATE
→ POST_RASTER_COMPOSITION
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
2. SENSORY ROUTE 선정 — PURE_SENSORY / TRIGGER_TO_MEAL / IMAGINED_OR_MEMORY 또는 동등한 회차별 변형
3. MEAL CONTEXT + DINING GRAMMAR compile
4. 초기 MEAL_SCENE_STATE / world-space table topology 정의
5. 콘텐츠 비트 작성
6. 반복 인물 탐지 — BODY 2컷 이상 등장하면 EPISODE_SUBJECT_LOCK 작성
7. VOICE 역할/문구 작성
8. 전체 BODY 콘티 작성 — emotional beat + state beat + visual coverage beat
9. FOOD STATE graph + per-shot scene-state delta 작성
10. bridge action 검사
11. coverage rhythm / adjacent visual-delta 검사
12. 각 컷 geometry risk + contact chain 정의
13. COVER brief 작성 — title / hero 후보 / character slot / reuse-first 여부 + cover source route(BODY_REUSE / DEDICATED / EXTERNAL_IMPORT)
14. 사용자에게 사전 패키지 제시
15. 명시 승인 후 BODY 래스터 제작

## 5. Visual preflight

생성 전:
- render cursor == target shot
- target shot is not APPROVED_LOCKED
- current-shot render capsule compiled
- DENYLIST fields absent
- actual style reference binding
- reference role separation
- 반복 인물이 있으면 EPISODE_SUBJECT_LOCK 존재
- S02+ 반복 인물이 있으면 승인 identity-anchor media binding 가능 여부 확인
- shot coverage fields 존재
- geometry risk/contact chain 존재
- meal context + dining grammar binding
- text_free=true
- single_panel=true

하나라도 실패하면 렌더 금지.

## 6. S01 gate

S01 한 장만 생성한다.

PASS 직후:
1. S01 = APPROVED_LOCKED
2. S01 = CONTINUITY_ANCHOR only
3. 반복 인물이 있으면 S01 subject appearance를 EPISODE_SUBJECT_LOCK과 대조하고 PASS 시 identity anchor로 등록
4. render cursor = S02
5. next user gate = RASTER_SET

## 7. Remaining render

S01 PASS 후:
- S02부터 마지막까지 한 장씩 생성
- current-shot capsule만 사용
- 반복 인물이 보이면 canonical STYLE_AUTHORITY + EPISODE_SUBJECT_LOCK + 승인 identity-anchor media를 함께 사용
- 각 컷 내부 QC
- FAIL이면 같은 shot만 재시도
- PASS이면 cursor 자동 전진
- 컷별 사용자 승인 없음
- 다음 컷으로 가기 전 identity/style-domain/anatomy/contact geometry hard QC를 먼저 통과
- 모든 BODY 후보가 나온 뒤 사용자에게 보여주기 전에 whole-sequence coverage/redundancy QC를 통과

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

### Visual identity / style QC
- canonical reference fidelity
- EPISODE_SUBJECT_LOCK fidelity for recurring people
- face/eye/hair/clothing/local-color consistency
- cross-domain rendering coherence
- STYLE_DOMAIN_SPLIT_FAIL 검사

### Shot visual QC
- shot-specific camera/composition
- declared focal_owner / shot_scale / camera_relation 실현
- action visibly realized
- food-first framing
- anti-ad rendering

### Human geometry QC
- shoulder/arm/wrist/hand continuity
- finger count/overlap/thumb position
- utensil grip
- food→utensil→mouth contact geometry
- garment/hair occlusion hiding impossible anatomy
- high-risk geometry failure = HARD FAIL

### Meal-context / dining-grammar QC
- cuisine/meal-setting consistency
- preparation/vessel/ingredient/garnish plausibility
- utensil type/material/placement plausibility
- hand/gesture/eating-action plausibility
- table topology plausibility
- cross-context contamination

### Sequence coverage QC
BODY 전체 후보가 준비되면 raster-set user gate 전에 검사:
- viewer-perceived shot distance repetition
- repeated camera side/height caused by renderer default
- repeated person size/face orientation/body orientation/gaze
- repeated hand/utensil layout
- adjacent low-delta cuts that should have been merged or reframed
- fixed direction quota 사용 금지
- intentional repetition이면 storyboard의 repetition justification과 일치하는지

실패하면 문제를 만드는 최소 subset만 재렌더한다.

### Food-state / meal-scene continuity QC
- pre/post food continuity
- bridge actions
- quantity/location/state monotonicity
- persistent table/vessel/utensil topology
- only declared state_delta changes persistent entities
- camera projection change is not mistaken for world-space rearrangement
- unexplained entity creation/disappearance/repositioning = FAIL

## 9. Raster-set gate

모든 BODY 컷 내부 PASS 후 반드시 sequence coverage QC까지 PASS한 전체 무자막 세트를 사용자에게 제시한다.
사용자 PASS 후 mandatory COVER acquisition/assembly와 BODY lettering으로 이동한다.

Raster-set PASS는 BODY artwork를 잠그며, cover 정책 추가만으로 기존 승인 BODY artwork를 소급 무효화하지 않는다.

## 10. Cover assembly

VISUAL_SYSTEM의 COVER_TEMPLATE_v1을 따른다.

1. preproduction에서 cover_source_route를 BODY_REUSE / DEDICATED / EXTERNAL_IMPORT 중 하나로 선언한다.
2. BODY_REUSE면 승인 BODY artwork에서 cover hero 후보를 먼저 찾는다.
3. 충분하면 editable title/series mark와 함께 cover를 조립한다.
4. 부족할 때만 dedicated cover hero를 별도 생성한다.
5. EXTERNAL_IMPORT면 외부/다른 세션에서 만든 cover asset을 identity/hash와 함께 등록한다.
6. dedicated cover hero는 BODY shot numbering/cursor에 포함하지 않는다.
7. COVER는 S01 anchor나 FOOD_STATE/MEAL_SCENE_STATE authority가 아니다.
8. cover_status=PASS가 아니면 FINAL_USER_GATE 진입 금지.

## 11. Lettering / final carousel

VOICE_SYSTEM으로 BODY 문구를 후단 합성하고 cover title을 editable layer로 조립한다.

최종 carousel order:
`COVER → S01 → S02 → ... → Sfinal`

최종 QC:
- cover/body 역할 분리
- cover title/hero mobile legibility
- 컷 순서
- 이미지/텍스트 대응
- composition-aware lettering placement
- 모바일 가독성
- 말투
- meal/dining grammar
- food-state continuity
- meal-scene/table-topology continuity
- 감정/감각 여운


## 12. Episode reset boundary

사용자가 회차 초기화를 명시하면:
- active episode package 삭제/retire
- render cursor 삭제
- episode-local approvals/anchors/EPISODE_SUBJECT_LOCK/cover status 폐기
- prototype/rejected outputs를 이후 reference나 continuity source로 재사용 금지
- canonical project authority에서 일반화된 구조 개선만 유지
- 다음 회차 번호는 사용자가 재시작을 명시한 경우 fresh 001로 되돌릴 수 있다

episode reset은 project style authority나 canonical 구조를 지우는 동작이 아니다.
