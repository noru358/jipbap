# jipbap

짧은 집밥/음식 감상형 만화 제작 프로젝트.

이 프로젝트는 instatoon의 하위 포맷이나 에피소드가 아니다. AutoPipeline 아래에서 instatoon, talkshow와 나란히 두는 독립 child project다. 기존 프로젝트에서 가져오는 것은 검증된 상위 제작 공정 원리뿐이며, 소재 규칙·스토리 문법·말투·시각 규칙·에피소드 체계는 이 저장소가 독립적으로 소유한다.

## Core production flow

menu/moment → sensory-route + meal-context compile → meal-scene state → recurring-subject lock + coverage/geometry plan → body storyboard + mandatory cover brief → pre-raster user gate → BODY S01 user anchor → BODY S02..final internal render/QC → whole-sequence QC → complete text-free body-raster user gate → mandatory cover acquisition/assembly + lettering → final carousel QC/export

핵심 운영 원칙:
- 한 컷 = 한 이미지 파일. 멀티패널/콜라주/콘택트시트는 생산 결과로 인정하지 않는다.
- 래스터 이미지는 기본적으로 무문자. 내레이션·말풍선·대사는 후단 레터링에서 분리한다.
- S01은 사용자 시각 앵커 게이트다. S01 통과 후 S02~마지막 컷은 운영자가 내부 QC하며 끝까지 진행하고, 중간 사용자 승인을 기본값으로 요구하지 않는다.
- 음식툰의 컷은 단순한 장면 목록이 아니라 상태 전이(state transition)로 설계한다.
- 같은 식탁이 이어지는 회차는 MEAL_SCENE_STATE를 두고, 이후 컷은 persistent world-state + 명시적 delta로 이어간다.
- 식탁은 개별 음식뿐 아니라 meal context / meal ecology 전체로 검수한다.
- Instagram cover는 BODY S01과 분리된 **mandatory product slot**이며, export는 COVER → S01 → ... → Sfinal 순서다. 다른 도구/세션에서 만들어 import할 수는 있어도 생략할 수는 없다.
- 스타일은 승인된 실제 이미지 레퍼런스가 최상위 시각 권위다. 텍스트 프롬프트나 임시 생성물이 이를 덮어쓰지 않는다.
- reference path/hash ≠ actual media binding. 바이너리 존재와 hash 검증을 fail-closed로 요구한다.
- 동일 인물이 BODY 2컷 이상 반복되면 episode-local subject lock을 만들며, style authority와 identity continuity를 분리한다.
- 컷별 상태 전이뿐 아니라 focal/거리/camera relation/visual delta를 계획하고 whole-sequence redundancy QC를 거친다.
- 손·팔·도구·입 접촉은 고위험 geometry로 별도 검수한다.
- 음식은 더 자세할 수 있지만 인물과 다른 매체처럼 보일 정도로 준실사화되면 실패다.

## Canonical documents

- CONTENT_SYSTEM.md — 음식/순간 선정과 비트 문법
- VOICE_SYSTEM.md — 집밥 프로젝트의 텍스트 말투
- VISUAL_SYSTEM.md — 레퍼런스 권위, 컷/카메라/래스터 규칙
- FOOD_STATE_SYSTEM.md — 음식 엔티티 상태·행동 선행조건·연속성 QC
- MEAL_CONTEXT_SYSTEM.md — 식문화/메뉴 조합/그릇/재료 정합성 QC
- PRODUCTION_PROTOCOL.md — 전체 제작/승인 게이트
- CURRENT_STATE.md — 현재 회차와 정확한 다음 행동
- assets/REFERENCE_MANIFEST.md — 실제 참조 바이너리의 역할/해시/materialization 상태
- schemas/shot_contract.schema.json — 컷 계약의 기계 판독용 최소 스키마

## Production reset — fresh 001 ready

구조 테스트용 001은 폐기했다.

- active episode: NONE
- 다음 제작 번호: 001
- 테스트 001의 메뉴·문구·콘티·승인·prototype raster는 현행 제작 권위가 아니다.
- 테스트에서 일반화된 구조 개선만 canonical project authority에 남긴다.
- 다음 세션은 GitHub 상태를 다시 복원한 뒤 fresh 001 사전기획부터 시작한다.
- episode-local subject lock, continuity anchor, cover status는 새 회차 승인 전에는 존재하지 않는다.

## Repository topology

Parent: noru358/AutoPipeline

Sibling child projects:
- noru358/instatoon
- noru358/talkshow
- noru358/jipbap
