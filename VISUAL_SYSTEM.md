# VISUAL_SYSTEM — jipbap v0.7
## 0. Asset-composition rendering policy

2026-09-07부터 최종 BODY의 기본 시각 경로는 **COMPOSITION_FIRST_HYBRID_FOOD**다.

`storyboard → reusable asset resolve → missing FOOD/POSE/PROP asset authoring → approved assets → deterministic scene composition → lettering`

도메인별 기본:
- **PERSON / recurring subject:** 승인된 인물/포즈 asset을 재사용한다. 음식 상태가 바뀐다는 이유로 사람 얼굴/몸 전체를 매 컷 다시 샘플링하지 않는다.
- **BACKGROUND / reusable props:** 가능한 한 승인된 plate/component를 재사용하고 crop/scale/placement로 장면을 만든다.
- **FOOD / FOOD_STATE:** 메뉴와 상태 변화가 핵심 의미이므로 회차별 신규 생성 비중을 높게 허용한다. 가능하면 음식/그릇/접촉에 필요한 asset 범위만 새로 만든다.
- **HAND / UTENSIL / CONTACT:** 기존 asset으로 물리 관계를 표현하기 어려우면 episode-local interaction asset을 만들 수 있다.
- **FULL FRAME GENERATION:** 조립으로 의미/접촉을 제대로 표현할 수 없는 샷의 명시적 exception lane이다.

신규 생성물은 아래 기존 reference/style/meal/anatomy QC를 그대로 통과한다. 차이는 QC를 없애는 것이 아니라 **매 컷 전체를 다시 생성하는 대신 새 asset 경계에서 검수**한다는 점이다.

accepted PERSON pixel을 FOOD variation 때문에 다시 샘플링하는 것은 기본적으로 `PERSON_RESAMPLE_FAIL`이다.


## 1. Reference authority

시각적 최상위 권위는 실제 승인 이미지 레퍼런스다.

현재 기준:
- intended binary: assets/references/STYLE_REF_001.jpg
- integrity/status authority: assets/REFERENCE_MANIFEST.md

reference path/hash만으로 media binding을 간주하지 않는다.

## 1.1 Style-domain coverage map

한 장의 reference가 모든 시각 영역을 자동으로 소유하지 않는다.

각 style reference는 coverage domain을 선언한다:
- PERSON
- FOOD
- BACKGROUND / LOCATION
- TYPE / GRAPHIC_COMPOSITION
- 또는 그 하위 범위

현재 사용자가 제공한 `STYLE_REF_001`은 **PERSON 스타일 레퍼런스**다.
사람의 얼굴 구조, 눈 문법, 선, 채색, 헤어 단순화에는 권위가 있지만
음식 렌더링, 집 배경, 카메라, 표지 디자인을 직접 보여주지 않으므로 그 영역의 픽셀 스타일 권위로 간주하지 않는다.

미포함 영역은:
1. 프로젝트의 추상화/anti-ad 규칙을 보수적으로 적용하거나,
2. 필요한 경우 별도 FOOD / BACKGROUND / COMPOSITION reference를 승인받는다.

`REFERENCE_DOMAIN_OVERREACH_FAIL`:
사람만 있는 시트를 근거로 음식/배경까지 "레퍼런스와 동일"하다고 주장하거나,
모델의 generic anime/cozy prior를 reference style로 오인하면 실패다.

## 1.2 PERSON style-fidelity preflight

S01에서 반복 인물을 만들기 전에, PERSON_STYLE_AUTHORITY와 실제 생성 인물을 다음 기준으로 대조한다:
- 머리 대비 얼굴 비율
- 눈 흰자/동공 비율과 눈 크기 분포
- 눈이 감정에 따라 변하는 방식
- 코/입 단순화
- 속눈썹/눈썹 밀도
- 헤어 내부선 밀도
- 외곽선 굵기와 정돈 정도
- flat fill / blush / shading 강도
- 얼굴의 generic polished anime 드리프트 여부

특히 금지:
- reference 분포보다 과도하게 커진 인형형 원형 눈을 기본값으로 고정
- reference보다 속눈썹/광택/헤어 묘사를 과도하게 미려화
- cinematic glow, depth-of-field, 고급 일러스트 텍스처를 PERSON style로 덧씌우기

S01이 예쁘더라도 PERSON style fidelity가 낮으면 내부적으로 PASS 추천하지 않는다.

## 2. Reference-role isolation

모든 이미지 reference는 역할을 가진다.

### STYLE_AUTHORITY
허용:
- 선/채색/질감
- 얼굴 단순화
- 시각 밀도

금지:
- current shot camera
- current shot action
- current shot composition

### CONTINUITY_ANCHOR
허용:
- identity
- 식기/음식 appearance continuity
- 필요한 최소 공간/소품 facts

금지:
- camera/composition 복사
- anchor의 포즈/행동 복사
- anchor를 다음 shot edit canvas로 사용

### EDIT_TARGET
사용자가 실제 수정 대상으로 지정한 이미지에만 사용.

## 3. Approved production-asset immutability

An approved PERSON / FOOD / BACKGROUND / PROP asset is hash-bound.

- do not mutate bytes under the same approved asset ID;
- replacement receives a new version/ID;
- food-state variation must not silently redesign an accepted PERSON asset;
- a scene repair should first change composition or the smallest faulty asset;
- rejected/replaced assets are not continuity anchors.

## 4. Reference influence isolation

Authoring references control only their declared domains.

When a new asset is authored, extract only the facts needed for that asset:
- PERSON: identity / line / fill / hair / clothing;
- FOOD: ingredient/form/state facts;
- BACKGROUND: location/style facts;
- CONTACT: hand/tool/food geometry.

Do not let a reference's camera, pose, incidental table layout or unrelated object state become mandatory merely because it appears in the image.

Final-frame camera/composition belongs to storyboard + deterministic scene composition.

## 4.5 Episode-local subject identity lock

같은 사람/식사자가 BODY 2컷 이상 반복 등장하면 스타일 레퍼런스만으로 충분하지 않다.
사전기획에서 `EPISODE_SUBJECT_LOCK`을 내부적으로 만든다.

이 lock은 고정 주인공을 프로젝트 전역에 하드코딩하는 규칙이 아니다.
회차가 끝나거나 episode reset되면 폐기되는 **episode-local identity authority**다.

최소 필드:
- subject_id
- source style authority
- face shape / eye grammar / nose-mouth simplification
- hair silhouette / hair color
- skin/local-color treatment
- clothing silhouette / palette
- line / fill / shading / texture characteristics
- invariants — 컷이 바뀌어도 유지할 것
- variables — pose / expression / camera / action처럼 비트에 따라 바뀔 수 있는 것

S01 user PASS 시 반복 인물이 있다면:
- S01의 승인된 인물 외형을 subject lock과 대조한다.
- 일치하면 S01을 episode-local identity anchor로 승격할 수 있다.
- 이후 컷은 `STYLE_AUTHORITY + EPISODE_SUBJECT_LOCK + 필요한 실제 identity-anchor media + current-shot contract`를 사용한다.
- renderer가 실제 image media binding을 지원하는데 반복 인물 anchor를 공급하지 않았다면 continuity-sensitive production은 FAIL-CLOSED한다.

금지:
- anchor의 카메라/포즈를 identity로 오인해 복사
- 다음 컷마다 얼굴을 새로 샘플링
- 음식 디테일을 올리면서 인물의 line/fill/shading 언어를 다른 스타일로 바꾸기
- 한 회차 subject lock을 다음 회차 기본 인물로 자동 재사용

반복 인물이 컷 사이에서 얼굴 비율, 눈 모양/크기, 헤어 실루엣, 피부색, 의상,
선/채색 방식이 의미 없이 변하면 `SUBJECT_IDENTITY_DRIFT_FAIL`이다.

## 4.6 Cross-domain rendering coherence

음식은 인물보다 재료 디테일이 더 많을 수 있다.
그러나 한 컷 안에서 **그림 매체 자체가 둘로 갈라져 보이면 안 된다.**

허용:
- 음식의 갈변, 결, 수분감처럼 식욕에 필요한 추가 정보
- 인물보다 조금 높은 음식 표면 디테일

실패:
- 인물은 flat toon인데 음식만 준실사/사진풍
- 음식만 과도한 광택·미세 질감·광원 모델링을 받아 광고 사진처럼 보임
- 컷마다 food realism level이 크게 출렁임
- 인물 채색만 별도 애니/셀채색 문법으로 drift

이를 `STYLE_DOMAIN_SPLIT_FAIL`로 본다.
STYLE_AUTHORITY는 인물뿐 아니라 전체 이미지의 선/채색/추상화 범위를 소유한다.

## 5. Rejected-output quarantine

QC FAIL 이미지:
- episode asset이 아니다.
- 이후 reference가 아니다.
- edit target로 쓰지 않는다.
- composition seed로 쓰지 않는다.

실패 이미지를 기반으로 반복 수정하면 오류가 누적되므로 금지한다.

## 6. Generative asset context firewall

When generation is used, send only the current ASSET_GAP / exception contract plus minimum required references.

Do not intentionally include:
- future BODY states;
- unrelated storyboard beats;
- rejected outputs;
- meaning-bearing copy that should be composed later.

If the output contains multiple unrelated scenes/assets or future-state leakage, reject it.

## 7. Asset / final-output contract

Generated asset:
- one requested asset per output by default;
- no grid/collage/contact sheet as a production asset;
- no baked lettering;
- appropriate transparency/isolation when the asset class needs composition flexibility.

Final BODY frame:
- 4:5 portrait;
- one frame = one image file;
- assembled from approved assets by the shared compositor;
- meaning-bearing text stays editable.

## 8. Shot-specific camera authority

camera/composition은 current shot contract가 소유한다.

food macro인데 full-table/character medium이 나오면 CAMERA_COMPOSITION_FAIL.

## 8.5 Shot coverage rhythm

각 shot contract는 current shot의 카메라뿐 아니라 sequence 안에서의 시각적 역할을 가진다.

최소 coverage fields:
- focal_owner
- shot_scale
- camera_relation
- visual_delta_from_previous
- repetition_justification — 유사 구도가 의도적일 때만

규칙:
- 고정된 좌/우/정면 비율을 맞추는 방식으로 다양성을 만들지 않는다.
- 음식 비트의 의미를 가장 잘 보여주는 camera/body/focal 관계를 우선한다.
- 인접 컷이 renderer의 안전한 기본 구도 때문에 반복되면 FAIL 후보다.
- macro/detail/object-only/hand-focused/mouth-contact/table-residue/character-context 등은 비트가 요구할 때 정상적인 완성 컷이다.
- 카메라 변화 자체가 목적이 되면 안 된다. 의미 변화가 먼저다.

완성 BODY raster set은 개별 컷 QC 이후에도 sequence-level coverage QC를 받는다.
viewer가 보기에 거리, 높이, 카메라측, 인물 크기, 얼굴 방향, 손/도구 배치가 기계적으로 반복되면
`SEQUENCE_VISUAL_REDUNDANCY_FAIL`이다.

## 8.6 Human anatomy / contact geometry

사람이 보이는 컷은 얼굴 동일성만 검수하지 않는다.

고위험 예:
- 젓가락/숟가락/포크 grip
- 손가락이 여러 개 겹치는 장면
- 손이 얼굴/입 근처에 오는 장면
- 음식→도구→입 접촉
- 팔이 화면 밖에서 들어와 손으로 이어지는 장면
- 소매/머리카락이 관절을 가리는 장면

검수 체인:
- shoulder → upper arm → elbow → forearm → wrist → hand
- 손가락 수/겹침/엄지 위치
- 도구 grip과 양 끝 방향
- 음식 접촉점
- mouth/teeth/lip 접촉
- 옷/머리카락이 불가능한 신체 구조를 숨기고 있지 않은지

고위험 컷은 shot contract의 geometry risk와 contact chain을 명시한다.
신체가 잘렸거나 비틀렸거나 도구 접촉이 물리적으로 불가능하면,
작화가 예뻐도 `HUMAN_GEOMETRY_FAIL`이다.

## 9. Food-first framing

음식 비트는 얼굴을 의무로 하지 않는다.
손/수저/그릇/음식 초근접 허용.

### 9.1 Approved food-focus composition baseline — 2026-09-07

- 현재 비트의 주인공이 음식 상태 변화라면 음식과 접촉 행동이 화면의 시각적 우선권을 가진다.
- 손·젓가락·숟가락·그릇은 장식 소품이 아니라 행동 관계의 일부다. 접촉 위치와 도구 방향이 실제 동작과 맞아야 한다.
- 먹기 전/행동 중/행동 후의 상태 차이가 컷 사이에서 읽혀야 한다. 인물 얼굴을 크게 보여주기 위해 이 변화를 희생하지 않는다.
- 인물과 배경은 필요한 상황·감정·공간 정보를 제공하되 음식 초점을 경쟁적으로 빼앗지 않는다.
- 감각이 음식 자체로 충분히 전달되는 경우 object/food-only 또는 hand/utensil-focused frame을 정상적인 완성 컷으로 인정한다.

세부 상태 전이와 물리적 선행조건은 FOOD_STATE_SYSTEM이, 식문화 정합성은 MEAL_CONTEXT_SYSTEM이 소유한다. 이 절은 그 authority를 복제하지 않고 화면 우선순위만 정한다.

## 9.2 Background exposure policy

집밥은 같은 집을 매 컷 풀배경으로 재현하는 프로젝트가 아니다.
배경은 독자의 음식 경험에 필요한 만큼만 노출한다.

shot마다 `background_scope`를 고른다:
- NONE — 음식/손/입 macro에서 배경을 거의 제거
- LOCAL — 테이블 재질, 그릇 일부, 창의 빛 등 현재 행동을 이해시키는 최소 맥락
- FULL — 장소를 처음 잡거나 공간 자체가 감각 진입에 필요할 때만 전체 공간 노출

같은 장소의 FULL 배경이 2컷 이상 반복될 때만 episode-local `LOCATION_LOCK`을 둔다.
LOCK은 픽셀 좌표를 외우는 것이 아니라 최소 지속 facts만 가진다:
- 주요 창/조명/가구의 상대 관계
- 테이블/벽/바닥의 재질과 기본 색
- 식사자의 위치 기준
- 반복되어야 할 핵심 소품

macro/close shot에서 보이지 않는 방 전체를 억지로 다시 생성하지 않는다.
이 방식으로 continuity 부담을 줄이면서, 실제로 보이는 배경은 같은 집으로 읽히게 한다.

## 10. Anti-ad look

억제:
- 과도 광택
- 비현실적 증기/빛
- 광고용 완벽 표면
- 음식만 실사화

선호:
- 실제 집밥 형태
- 평범한 그릇
- 먹으며 변하는 상태
- 손동작/잔여 흔적


## 10.5 Mandatory cover product slot

집밥 carousel에서 COVER는 옵션이 아니다.
최종 산출 슬롯은 항상:

`COVER → BODY S01 → S02 → ... → Sfinal`

이다.

단, COVER의 **제작 주체**는 유연하다.
- BODY_REUSE — 승인 BODY artwork 재구성
- DEDICATED — 전용 hero 생성
- EXTERNAL_IMPORT — 다른 도구/세션에서 제작 후 등록

어느 경로든 최종 완료 전:
- cover asset identity가 등록되어야 하고
- cover QC가 PASS여야 하며
- final carousel의 first slot에 있어야 한다.

COVER가 없거나 placeholder뿐이면 `COVER_MISSING_FAIL`.
BODY가 모두 승인됐어도 final carousel COMPLETE로 갈 수 없다.

## 11. Instagram carousel cover — COVER_TEMPLATE_v1

집밥의 Instagram cover는 본편 음식 상태 시퀀스와 분리된 **product-composition asset**이다.

Hard distinction:
- `COVER` != `S01`
- COVER는 FOOD_STATE / MEAL_SCENE_STATE의 첫 상태가 아니다.
- COVER는 S01 user anchor를 대체하지 않는다.
- COVER용 전용 이미지가 생겨도 본편 continuity anchor로 자동 승격하지 않는다.

Carousel export order:
`COVER → S01 → S02 → ... → Sfinal`

### Fixed template grammar

프로젝트 수준에서 고정/반복하는 요소:
- 4:5 master ratio
- 큰 제목의 기본 hierarchy와 safe area
- hero 영역과 제목 영역의 대략적 비율
- 시리즈 표식/브랜드 요소의 위치
- 모바일에서 한눈에 같은 시리즈로 읽히는 밀도와 여백 원칙

회차별 variable slots:
- 제목
- 대표 음식
- 해당 회차 인물/표정/작은 행동
- 최소 배경 맥락
- 음식과 인물의 구체 배치

템플릿은 픽셀 좌표를 모든 회차에 복제하는 고정 포스터가 아니다.
시리즈 정체성은 유지하되 음식 hero와 캐릭터가 제목에 가려지지 않도록 composition을 회차별로 조정한다.

### Reuse-first hero policy

1. 승인된 본편 artwork 중 cover hero로 충분한 음식/인물 자산이 있으면 우선 재사용/재구성한다.
2. 적합한 본편 자산이 없을 때만 `DEDICATED_COVER_HERO`를 만든다.
3. dedicated cover hero는 가능하면 S01 및 body raster direction이 승인된 뒤 생성해 style/identity drift를 줄인다.
4. cover title/series mark는 raster에 굽지 않고 COMPOSITION 단계에서 editable layer로 조립한다.

Cover QC:
- 제목이 phone-size에서 즉시 읽히는가
- 음식이 회차의 주인공으로 보이는가
- 해당 회차 캐릭터가 필요 이상으로 food focal area를 압도하지 않는가
- 본편과 같은 drawing language / identity인가
- 본편 상태 연속성을 잘못 암시하는 fake action/state를 만들지 않는가


## 12. Composition-template validation status

COVER/LETTERING template calibration is explicitly two-phase.

### Phase 1 — SPEC_LOCKED

Production registry assets are not required. Use only `calibration/fixtures` placeholder assets and the shared deterministic compositor/lettering runtime.

The user compares:
- hierarchy and safe-area behavior;
- food-hero / character-slot ratio;
- crop/overflow behavior;
- title/lettering anchor strategy;
- box vs no-box treatment;
- typography class, not final font pixels.

Explicit selection promotes the chosen grammar to `SPEC_LOCKED` only.
Placeholder pixels, runtime default fonts and calibration hashes are never production visual authority.

### Phase 2 — USER_LOCKED

After the BODY pilot has approved real PERSON/FOOD/CONTACT assets:
- rerender only the selected spec;
- bind actual production font bytes by SHA-256;
- inspect real Korean glyph metrics and phone-size readability;
- verify food dominance, character/style coherence and collision with actual artwork.

Only explicit user approval of this real-pixel result promotes the template to `USER_LOCKED`.

Direct `IN_TEST → USER_LOCKED` promotion is forbidden.

## 13. Lettering-template policy

BODY lettering은 generic UI 흰색 rounded box를 기본값으로 사용하지 않는다.

공통 원칙:
- 음식 focal area와 얼굴을 가리지 않는 negative-space 우선 배치
- 이미지마다 임의 위치가 아니라 scene-aware anchor 규칙 사용
- 한눈에 읽히되 이미지보다 먼저 튀지 않는 hierarchy
- 의미 단위 line-break는 editable plan에 명시
- silent shot에는 장식성 텍스트를 추가하지 않음
- parent `pipeline/lettering.py`가 deterministic preview와 receipt를 소유
- calibration placeholder의 runtime default font는 SPEC 비교 전용
- production font는 project file + SHA-256 binding 필수
- exact font family / size / line height / Korean glyph metrics는 Phase-2 pixel validation에서 확정

E001 임시 Noto Sans Bold + 큰 rounded box는 승인된 lettering template이 아니다.
