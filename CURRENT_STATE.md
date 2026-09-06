# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

`episodes/001/README.md`

## Approved

- 독립 프로젝트로 운영: instatoon E008/하위 포맷 아님
- 큰 제작 공정만 instatoon에서 재사용
- Episode 001 menu/moment: 계란후라이 + 흰밥
- 5컷 콘티 방향 승인
- 말투 시스템 승인
- 기본 말투 수정: `먹고 싶었음`보다 `먹고 싶었다` 같은 자연스러운 서술형 종결을 선호
- 실제 시각 레퍼런스 지정: `assets/references/STYLE_REF_001.jpg`
- S01 생성물은 **진행용 임시 PASS**. 스타일 확정이 아님

## Known failures / learnings

1. S02 생성 시 모델이 단일 컷 대신 멀티패널 합본을 반복 생성함.
   - 해결 원칙: one-shot-one-file 계약을 생성 전/후 모두 검증. 합본은 자동 FAIL.
   - 임시 크롭 복구는 실험 진행용일 뿐 정식 생산 방식이 아님.

2. 음식 상태 연속성 오류:
   - 잘못된 흐름: 접시 위 계란 노른자 파열 → 다음 컷에서 계란이 밥 위로 이동
   - 자연스러운 흐름: 계란을 밥 위에 올림 → 그 상태에서 노른자를 터뜨림 → 간장 → 한입
   - 해결: `FOOD_STATE_SYSTEM.md`의 상태 전이 계약을 모든 회차에 적용

## Exact next action

Episode 001 콘티를 상태 전이 기준으로 재컴파일한다.

1. S01: 밥/접시 위 intact egg/김/간장 준비 상태
2. S02: egg.location = on_rice 인 상태에서 yolk를 터뜨림
3. S03: 이미 터진 노른자 + 밥 위 계란에 간장을 소량 추가
4. S04: 첫 한입
5. S05: 거의 비운 그릇 + 잔여 행동

그 후 새 시각계약으로 S02~S05를 다시 제작한다. S01 임시 PASS는 유지하되 최종 스타일 확정으로 승격하지 않는다.
