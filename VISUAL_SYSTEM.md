# VISUAL_SYSTEM — jipbap v0.2

## 1. Reference authority

시각적 최상위 권위는 실제 승인 이미지 레퍼런스다.

현재 기준:
- intended binary: assets/references/STYLE_REF_001.jpg
- integrity/status authority: assets/REFERENCE_MANIFEST.md

경로 문자열이나 해시만으로 레퍼런스가 전달된 것으로 간주하지 않는다.
독립 실행 환경에서는 실제 바이너리가 선언 경로에 존재하고 manifest SHA-256과 일치해야 reference-conditioned production을 허용한다.

레퍼런스는 선, 얼굴 비율, 눈/입 단순화, 색감, 배경 밀도, 만화적 표현 수준을 판단하는 기준이다.
텍스트 프롬프트는 레퍼런스를 설명/보조할 뿐 대체하지 않는다.

## 2. Reference-role isolation

모든 이미지 reference binding은 역할을 명시한다.

### STYLE_AUTHORITY
허용 영향:
- 선/채색/질감
- 얼굴 단순화 방식
- 전반적 시각 밀도

금지 영향:
- 현재 shot의 카메라
- 현재 shot의 행동
- 현재 shot의 구도

### CONTINUITY_ANCHOR
허용 영향:
- 동일 회차 인물 identity
- 식기/공간/음식 외형 continuity
- 팔레트와 소품 inventory

금지 영향:
- 현재 shot의 카메라/구도를 복사
- 현재 shot의 행동을 S01 행동으로 되돌림
- 현재 shot을 anchor의 재생성으로 바꿈

### EDIT_TARGET
현재 이미지를 직접 수정해야 하는 shot에만 사용한다.
사용자가 수정 대상으로 지정하지 않은 승인 anchor는 EDIT_TARGET로 쓰지 않는다.

## 3. S01 approved anchor rule

S01 PASS 후:
- S01은 APPROVED_LOCKED
- S01 이미지는 CONTINUITY_ANCHOR 역할만 가진다.
- S02+ 생성에서 S01을 edit canvas로 사용하지 않는다.
- S02+의 composition/action authority는 오직 해당 shot contract다.

모델이 anchor 구도를 과도하게 복제하면:
1. S01 이미지 conditioning을 약화/제거하고
2. S01에서 추출한 continuity facts만 전달하며
3. STYLE_AUTHORITY + current shot contract로 재생성한다.

이때 S01 자체를 재생성하지 않는다.

## 4. Output contract

- 기본: 4:5 portrait
- 한 컷 = 한 이미지 파일
- 한 생성 호출의 납품 대상도 한 컷
- 멀티패널, grid, collage, contact sheet는 HARD FAIL
- 래스터에는 최종 내레이션/대사/말풍선/로고/워터마크 없음
- text_free=true이면 벽 포스터, 냉장고 메모, 간판 등 우발적 읽을 수 있는 글자도 생성하지 않는다.

### Post-generation structural QC
1. 단일 패널인가?
2. 패널 경계선으로 여러 장면이 나뉘지 않았는가?
3. 현재 shot의 필수 엔티티/행동만 존재하는가?
4. 다른 shot의 장면을 함께 그리지 않았는가?
5. 현재 shot contract의 카메라와 행동이 실제 픽셀에 보이는가?

실패하면 사용자에게 넘기지 않고 현재 shot만 재시도한다.

## 5. Shot-specific camera authority

카메라와 composition은 reference image가 아니라 current shot contract가 소유한다.

예:
- table medium
- food macro/close-up
- top/oblique food view
- eating medium close-up
- quiet aftermath

food macro shot에서 anchor가 table-medium이더라도 table-medium으로 회귀하면 CAMERA_COMPOSITION_FAIL이다.

## 6. Food-first framing

음식이 핵심인 비트에서는 얼굴을 항상 보여줄 필요가 없다.
손/젓가락/그릇/음식 초근접을 적극 사용한다.

동일 얼굴 3/4 구도 반복을 모델 기본값으로 허용하지 않는다.

## 7. Anti-ad look

금지/억제:
- 과도한 광택
- 비현실적인 증기/빛 효과
- 사진 광고처럼 완벽한 재료 표면
- 음식만 과도하게 고해상도/실사화

허용/선호:
- 실제 집밥의 약간 삐뚤어진 형태
- 평범한 그릇
- 먹으면서 변하는 음식 상태
- 손의 동작과 잔여 흔적
