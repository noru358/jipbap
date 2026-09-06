# PRODUCTION_PROTOCOL — jipbap v0.1

## 0. Operating mode

현재 기본 모드: `MANUAL_VALIDATION`

사용자 승인 구조:

`content/storyboard contract → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`

**one frame = one file** 이지만 **one frame = one user gate**는 아니다.

## 1. Preproduction

1. MENU/MOMENT 선정
2. 콘텐츠 비트 작성
3. VOICE 역할/문구 작성
4. 전체 콘티 작성
5. FOOD STATE graph 작성
6. bridge action 검사
7. 전체 시각 리듬 설계
8. 사용자에게 사전 패키지 제시
9. 명시 승인 후 래스터 제작

## 2. Visual preflight

생성 전 각 컷에 대해:
- actual style reference binding
- episode anchor binding if available
- preconditions/action/postconditions
- must_show / must_not_show
- camera/composition
- text_free=true
- single_panel=true

이 중 하나라도 빠지면 렌더 금지.

## 3. S01 gate

S01 한 장만 생성한다.
사용자가 다음을 본다.
- 스타일
- 인물
- 음식 표현 밀도
- 공간 분위기
- 인물/음식 비중

PASS는 회차 앵커 승인과 프로젝트 스타일 락 승인을 구분해 기록한다.

## 4. Remaining render

S01 PASS 후:
- S02부터 마지막까지 한 장씩 생성
- 각 컷 생성 후 내부 구조/시각/상태 QC
- FAIL은 내부 재시도
- 사용자에게 컷별 승인을 기본적으로 요구하지 않음

중간에 사용자를 다시 부르는 조건:
- 콘티/맛/스타일의 본질적 선택이 필요한 경우
- 원래 승인 계약 자체가 잘못되어 운영자가 임의로 결정할 수 없는 경우

## 5. Internal QC layers

### Structural output QC
- one panel / one file
- no text
- no collage

### Visual QC
- reference fidelity
- identity/space continuity
- food-first framing
- anti-ad rendering

### Food state QC
- pre/post continuity
- bridge actions
- quantity/location/state monotonicity where applicable

## 6. Raster-set gate

모든 컷이 내부 PASS일 때 전체 무자막 세트를 사용자에게 제시한다.
사용자 PASS 후에만 레터링으로 넘어간다.

## 7. Lettering

VOICE_SYSTEM에 따라 텍스트를 후단에서 합성한다.
원본 래스터에 생성기로 한글을 굽지 않는다.

## 8. Final QC

- 컷 순서
- 이미지/텍스트 대응
- 모바일 가독성
- 말투 일관성
- 음식 상태 연속성
- 최종 감정 여운
