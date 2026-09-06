# jipbap

짧은 **집밥/음식 감상형 만화** 제작 프로젝트.

이 프로젝트는 `instatoon`의 하위 포맷이나 에피소드가 아니다. `AutoPipeline` 아래에서 `instatoon`, `talkshow`와 나란히 두는 독립 child project를 목표로 한다. 기존 프로젝트에서 가져오는 것은 검증된 상위 제작 공정 원리뿐이며, 소재 규칙·스토리 문법·말투·시각 규칙·에피소드 체계는 이 저장소가 독립적으로 소유한다.

## Core production flow

`menu/moment → content plan → storyboard → pre-raster user gate → S01 user anchor → S02..final internal render/QC → complete text-free raster-set user gate → lettering → final QC/export`

핵심 운영 원칙:
- **한 컷 = 한 이미지 파일**. 멀티패널/콜라주/콘택트시트는 생산 결과로 인정하지 않는다.
- 래스터 이미지는 기본적으로 **무문자**. 내레이션·말풍선·대사는 후단 레터링에서 분리한다.
- S01은 사용자 시각 앵커 게이트다. S01 통과 후 S02~마지막 컷은 운영자가 내부 QC하며 끝까지 진행하고, 중간 사용자 승인을 기본값으로 요구하지 않는다.
- 음식툰의 컷은 단순한 장면 목록이 아니라 **상태 전이(state transition)** 로 설계한다.
- 스타일은 승인된 실제 이미지 레퍼런스가 최상위 시각 권위다. 텍스트 프롬프트나 임시 생성물이 이를 덮어쓰지 않는다.

## Canonical documents

- `CONTENT_SYSTEM.md` — 음식/순간 선정과 비트 문법
- `VOICE_SYSTEM.md` — 집밥 프로젝트의 텍스트 말투
- `VISUAL_SYSTEM.md` — 레퍼런스 권위, 컷/카메라/래스터 규칙
- `FOOD_STATE_SYSTEM.md` — 음식 엔티티 상태·행동 선행조건·연속성 QC
- `PRODUCTION_PROTOCOL.md` — 전체 제작/승인 게이트
- `CURRENT_STATE.md` — 현재 회차와 정확한 다음 행동
- `schemas/shot_contract.schema.json` — 컷 계약의 기계 판독용 최소 스키마

## Current experiment

프로젝트 1화는 **계란후라이 + 흰밥**.

- 콘티: 승인
- 말투 구조: 승인
- 원본 시각 레퍼런스: `assets/references/STYLE_REF_001.jpg`
- S01: 진행용 임시 PASS, **최종 스타일 락 아님**
- 발견된 구조 오류: 계란을 접시 위에서 먼저 깨고 다음 컷에서 밥 위로 순간 이동하는 음식 상태 연속성 실패
- 해결: `FOOD_STATE_SYSTEM.md`의 precondition/postcondition + bridge action + food continuity QC를 공통 구조로 적용
