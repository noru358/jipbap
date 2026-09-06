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

## 3. Manual/chat render-context isolation

current-shot-only는 **대화 전체를 비워야 한다는 뜻이 아니라 실제 renderer dispatch 입력을 target shot capsule로 제한한다는 뜻**이다.

따라서 같은 ChatGPT 세션 안에 전체 승인 storyboard, future-shot 계획 또는 이전 작업 기록이 존재한다는 사실만으로
자동으로 RENDER_CONTEXT_UNSAFE가 되지 않는다.

정상 same-session 실행 조건:
- 호출 직전에 target shot capsule을 새로 컴파일한다.
- renderer에 의도적으로 전달하는 prompt/reference binding은 ALLOWLIST만 사용한다.
- future-shot instruction, future state, voice copy, rejected output은 dispatch payload에 넣지 않는다.
- 결과물에서 future-shot semantic leakage / multi-shot leakage / current-shot state contradiction을 hard QC한다.
- 결과가 PASS하면 같은 세션에서 다음 cursor shot으로 진행할 수 있다.

RENDER_CONTEXT_UNSAFE는 다음과 같이 **실제 오염 증거 또는 격리 불능 증거**가 있을 때만 선언한다:
- renderer 호출 경계에서 future-shot/전체-storyboard 정보가 실제 payload에 포함됨을 확인했다.
- 결과물에 future-shot action/state가 섞였다.
- single-panel 요청인데 multi-shot/page/collage가 반복된다.
- rejected/locked artifact가 의도와 달리 edit target 또는 continuity seed로 재사용된다.
- current-shot capsule을 재컴파일한 뒤에도 같은 hard context-leak contract가 반복 실패한다.
- artifact/approval identity가 불명확해져 어떤 결과를 기준으로 이어가야 하는지 확정할 수 없다.

이 경우:
- 같은 환경에서 무한 재시도하지 않는다.
- rejected output을 reference로 재사용하지 않는다.
- 이전 approved shot을 다시 만들지 않는다.
- 상태를 RENDER_CONTEXT_UNSAFE로 기록한다.
- 필요한 경우에만 clean render context로 handoff하여 같은 cursor shot부터 재개한다.

중요:
context reset은 episode reset이 아니다.
GitHub의 render cursor/locked shots를 복원한 후 해당 cursor부터 그대로 이어간다.

## 3.5 authority-change barrier

사용자가 구조/규칙을 수정했고 그 변경이 다음 렌더에 영향을 준다면,
대화에서 합의만 한 채 다음 렌더로 진행하지 않는다.

필수 순서:
1. canonical child/parent authority 수정
2. commit/HEAD 검증
3. 필요한 profile/submodule 정합성 확인
4. 그 뒤에만 dependent render 실행

pending structural change가 있으면 visual preflight FAIL이다.

## 4. Preproduction

1. MENU/MOMENT 선정
2. PROXY_EATER promise + APPETITE ARC 정의 — 독자가 어떤 순서로 군침/감각 payoff를 받는지
3. SENSORY ROUTE 선정 — PURE_SENSORY / TRIGGER_TO_MEAL / IMAGINED_OR_MEMORY 또는 동등한 회차별 변형
4. MEAL CONTEXT + DINING GRAMMAR compile
5. 초기 MEAL_SCENE_STATE / world-space table topology 정의
6. 콘텐츠 비트 작성
7. 반복 인물 탐지 — BODY 2컷 이상 등장하면 EPISODE_SUBJECT_LOCK 작성
8. style-domain coverage map + PERSON style-fidelity 기준 정의
9. background_scope 계획 — NONE / LOCAL / FULL; 반복 FULL이면 LOCATION_LOCK plan
10. VOICE sensory payload / 문구 계획
11. 전체 BODY 콘티 작성 — emotional + state + visual coverage + appetite/sensory beat
12. FOOD STATE graph + per-shot scene-state delta 작성
13. bridge action 검사
14. appetite-value gate + opening/ending temporal-distinguishability 검사
15. coverage rhythm / adjacent visual-delta 검사
16. 각 컷 geometry risk + contact chain 정의
17. COVER brief 작성 — title / hero 후보 / character slot / reuse-first 여부 + cover source route(BODY_REUSE / DEDICATED / EXTERNAL_IMPORT)
18. 사용자에게 사전 패키지 제시
19. 명시 승인 후 BODY 래스터 제작

## 5. Visual preflight

생성 전:
- pending structural authority change가 없음
- render cursor == target shot
- target shot is not APPROVED_LOCKED
- current-shot render capsule compiled
- DENYLIST fields absent
- actual style reference binding
- reference role separation
- reference coverage_scope가 current shot에서 요구하는 visual domain과 일치
- PERSON이 보이면 PERSON style-fidelity preflight 기준 존재
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

PASS 추천 전:
- PERSON_STYLE_AUTHORITY 대비 얼굴/눈/선/채색/헤어 단순화 fidelity 내부 QC
- generic polished anime drift가 있으면 사용자에게 PASS 추천하지 않음

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

### Appetite / proxy-eater sequence QC
BODY 전체 후보가 준비되면 검사:
- 각 shot의 appetite_function / sensory_payload가 실제 이미지에 실현되는가
- 단순 절차만 보여주는 low-value frame이 있는가
- 독자가 "대신 먹고 있다"고 느낄 ingestion/contact/payoff가 충분한가
- sequence 초반보다 후반의 감각 payoff가 약해지며 흐지부지 끝나지 않는가
- opening과 ending을 바꿔도 거의 같은 장면이면 TEMPORAL_DISTINGUISHABILITY_FAIL 후보
- menu-specific secondary payoff가 가능한데 단순 복귀 동작으로 끝내지는 않았는가
- visual appetite cue가 음식의 실제 상태에 근거하며 광고용 과장이 아닌가

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
- cover visual template이 사용자 승인된 lock인지; 아니면 template calibration gate로 전환
- lettering font/size/placement/template이 사용자 승인된 lock인지; 아니면 ad-hoc finalization 금지
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
