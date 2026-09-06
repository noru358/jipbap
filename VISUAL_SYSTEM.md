# VISUAL_SYSTEM — jipbap v0.3

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
