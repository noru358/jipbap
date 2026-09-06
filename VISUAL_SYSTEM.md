# VISUAL_SYSTEM — jipbap v0.1

## 1. Reference authority

시각적 최상위 권위는 실제 승인 이미지 레퍼런스다.

현재 기준:
- intended binary: `assets/references/STYLE_REF_001.jpg`
- integrity/status authority: `assets/REFERENCE_MANIFEST.md`

**경로 문자열이나 해시만으로 레퍼런스가 전달된 것으로 간주하지 않는다.**
독립 실행 환경에서는 실제 바이너리가 선언 경로에 존재하고 manifest SHA-256과 일치해야 reference-conditioned production을 허용한다.

현재 원본 레퍼런스는 이 ChatGPT 세션에 실제 이미지로 공급되어 있으나, GitHub 커넥터의 현재 쓰기 경로는 UTF-8 텍스트와 Git object 조작만 노출되어 있어 해당 바이너리는 원격 저장소에 아직 materialize되지 않았다. 저장소 단독 실행은 이 상태에서 FAIL-CLOSED 한다.

레퍼런스는 선, 얼굴 비율, 눈/입 단순화, 색감, 배경 밀도, 만화적 표현 수준을 판단하는 기준이다.
텍스트 프롬프트는 레퍼런스를 설명/보조할 뿐 대체하지 않는다.

## 2. Temporary anchor rule

Episode 001 진행용 임시 앵커의 intended path:
- `episodes/001/anchors/S01_TEMP_ANCHOR.png`

integrity/status는 `assets/REFERENCE_MANIFEST.md`가 소유한다.

사용자 판정: 임시 PASS.
- 동일 회차의 인물/공간/식탁 연속성 보조에 사용 가능
- 프로젝트 전체의 최종 STYLE LOCK으로 승격 금지
- STYLE_REF_001보다 높은 시각 권위를 갖지 않음
- 저장소 단독 실행에서는 실제 바이너리 materialization 전까지 사용 금지

## 3. Output contract

- 기본: 4:5 portrait
- **한 컷 = 한 이미지 파일**
- 한 생성 호출의 납품 대상도 한 컷
- 멀티패널, 만화 페이지, grid, collage, contact sheet는 HARD FAIL
- 래스터에는 최종 내레이션/대사/말풍선/로고/워터마크 없음

### Post-generation structural QC
생성 직후 다음을 검사한다.
1. 단일 패널인가?
2. 패널 경계선으로 여러 장면이 나뉘지 않았는가?
3. 한 컷 계약의 필수 엔티티만 존재하는가?
4. 다른 컷의 장면을 함께 그리지 않았는가?

실패하면 사용자에게 넘기지 않고 내부 재시도한다.
크롭으로 합본을 쪼개는 것은 정식 생산 경로가 아니다.

## 4. Food-first framing

음식이 핵심인 비트에서는 얼굴을 항상 보여줄 필요가 없다.
손/젓가락/그릇/음식 초근접을 적극 사용한다.

카메라는 스토리 기능에 따라 바꾼다.
- table medium
- food macro/close-up
- top/oblique food view
- eating medium close-up
- quiet aftermath

동일 얼굴 3/4 구도 반복을 모델 기본값으로 허용하지 않는다.

## 5. Anti-ad look

음식을 먹고 싶게 보여주는 것과 광고 렌더링은 다르다.

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
