# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

`episodes/001/README.md`

## Approved

- 독립 프로젝트로 운영: instatoon E008/하위 포맷 아님
- AutoPipeline의 별도 child project
- 큰 제작 공정만 instatoon에서 재사용
- Episode 001 menu/moment: 계란후라이 + 흰밥
- 5컷 콘티 방향 승인
- 말투 시스템 승인
- 기본 말투 수정: `먹고 싶었음`보다 `먹고 싶었다` 같은 자연스러운 서술형 종결을 선호
- 실제 시각 레퍼런스 지정
- S01 생성물은 **진행용 임시 PASS**. 스타일 확정이 아님

## Repository / reference state

Remote repository: `noru358/jipbap`

Canonical text systems, Episode 001 state and shot-contract schema are materialized on `main`.
`AutoPipeline` registers `jipbap` as an independent submodule child.

Reference integrity authority:
- `assets/REFERENCE_MANIFEST.md`

Current binary status:
- STYLE_REF_001: BINARY_REQUIRED_NOT_YET_MATERIALIZED
- S01_TEMP_ANCHOR: BINARY_REQUIRED_NOT_YET_MATERIALIZED

This is a **transport/materialization blocker for repository-only execution**, not a reversal of the user's visual approval. The current chat has the actual reference media; a future clean environment must fail closed until repository binaries are restored and hash-verified.

## Known failures / learnings

1. S02 생성 시 모델이 단일 컷 대신 멀티패널 합본을 반복 생성함.
   - 해결 원칙: one-shot-one-file 계약을 생성 전/후 모두 검증. 합본은 자동 FAIL.
   - 임시 크롭 복구는 실험 진행용일 뿐 정식 생산 방식이 아님.

2. 음식 상태 연속성 오류:
   - 잘못된 흐름: 접시 위 계란 노른자 파열 → 다음 컷에서 계란이 밥 위로 이동
   - 자연스러운 흐름: 계란을 밥 위에 올림 → 그 상태에서 노른자를 터뜨림 → 간장 → 한입
   - 해결: `FOOD_STATE_SYSTEM.md`의 상태 전이 계약을 모든 회차에 적용

## Exact next action

Current-chat continuation:
1. Episode 001 콘티를 상태 전이 기준으로 사용한다.
2. S01 임시 PASS를 유지한다.
3. 실제 chat-supplied reference media를 렌더 입력으로 사용한다.
4. S02~S05를 single-panel / text-free / state-transition contract로 다시 제작하고 내부 QC한다.
5. 완전한 무자막 세트를 사용자에게 제시한다.

Repository-only / clean-environment continuation:
1. manifest에 선언된 두 바이너리를 intended path에 materialize한다.
2. SHA-256을 검증한다.
3. 그 후에만 reference-conditioned rendering을 허용한다.
