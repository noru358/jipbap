# VISUAL_SYSTEM — jipbap v0.5

## 1. Reference authority

시각적 최상위 권위는 실제 승인 이미지 레퍼런스다.

현재 기준:
- intended binary: assets/references/STYLE_REF_001.jpg
- integrity/status authority: assets/REFERENCE_MANIFEST.md

reference path/hash만으로 media binding을 간주하지 않는다.

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

## 3. Approved anchor immutability

S01 PASS 후:
- S01 = APPROVED_LOCKED
- S01 = CONTINUITY_ANCHOR only
- S02+에서 is_edit_target=false
- S02+의 camera/action authority는 current shot contract

S01이 current shot output으로 다시 등장하면 HARD FAIL.

## 4. Reference fact extraction

S02+에서 continuity가 필요할 때는 가능하면 승인 anchor의 전체 픽셀을 그대로 강하게 conditioning하지 않고
필요한 사실만 추출한다.

예:
- character hair/clothes
- bowl/plate family
- mackerel appearance
- table material

불필요한 사실:
- S01 camera
- S01 body pose
- S01 full-table layout
- S01 incidental background

anchor over-copy가 감지되면:
STYLE_AUTHORITY + extracted continuity facts + current shot contract만 사용한다.

## 5. Rejected-output quarantine

QC FAIL 이미지:
- episode asset이 아니다.
- 이후 reference가 아니다.
- edit target로 쓰지 않는다.
- composition seed로 쓰지 않는다.

실패 이미지를 기반으로 반복 수정하면 오류가 누적되므로 금지한다.

## 6. Current-shot context firewall

렌더러에는 current shot만 전달한다.

금지:
- full storyboard
- future shots
- voice copy
- multi-shot page description

렌더 결과가 여러 shot을 한 번에 포함하면 MULTI_SHOT_CONTEXT_LEAK_FAIL이다.

## 7. Output contract

- 기본: 4:5 portrait
- one shot = one image file
- one render invocation = one shot
- multi-panel/grid/collage/contact sheet = HARD FAIL
- no lettering
- text_free=true이면 우발적 벽/냉장고/간판 글자도 금지

## 8. Shot-specific camera authority

camera/composition은 current shot contract가 소유한다.

food macro인데 full-table/character medium이 나오면 CAMERA_COMPOSITION_FAIL.

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
