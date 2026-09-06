# jipbap

짧은 집밥/음식 감상형 만화 제작 프로젝트. AutoPipeline 아래에서 instatoon과 독립된 child authority를 가진다.

## Core production flow

`menu/moment → sensory/meal-context plan → food-state storyboard → asset resolve → missing asset authoring → deterministic BODY composition → mandatory COVER + lettering → QC/export`

현재 최종 시각 방식은 **COMPOSITION_FIRST_HYBRID_FOOD**다.

- PERSON: 승인된 인물/포즈 asset을 재사용한다.
- FOOD/FOOD_STATE: 메뉴와 상태 변화가 핵심이므로 회차별 신규 생성 허용 비중이 높다.
- HAND/UTENSIL/CONTACT: 필요한 경우 episode-local interaction asset을 만든다.
- BACKGROUND/PROP: 가능한 것은 재사용한다.
- FULL FRAME GENERATION: 조립으로 의미를 보존하기 어려운 샷의 명시적 exception lane만 허용한다.
- lettering/UI/cover title: deterministic editable composition이 소유한다.

즉 **음식을 새로 그릴 수는 있지만, 음식이 바뀔 때마다 사람까지 다시 뽑는 구조는 폐기**한다.

## Fixed principles

- PROXY_EATER: 독자 대신 만화 속 인물이 먹고 감각을 전달한다.
- BODY는 food-state transition과 실제 먹는 순서를 따른다.
- 식문화/메뉴/그릇/도구는 MEAL_CONTEXT_SYSTEM으로 검수한다.
- 한 컷 = 한 이미지 파일.
- 의미가 있는 글자는 raster asset에 굽지 않는다.
- cover는 BODY와 별도인 mandatory first slot이다.
- 승인 asset은 hash-bound이며 bytes가 바뀌면 승인이 승계되지 않는다.
- missing visual capability는 full-frame 재생성 허가가 아니라 ASSET_GAP이다.
- 음식은 더 자세할 수 있지만 사람과 다른 매체처럼 준실사화되면 실패다.
- 실패는 최소 범위만 무효화한다.

## Canonical documents

- CONTENT_SYSTEM.md — 음식/순간과 PROXY_EATER 비트
- VOICE_SYSTEM.md — 텍스트 말투
- VISUAL_SYSTEM.md — **hybrid asset-composition policy**, 레퍼런스/카메라/시각 QC
- FOOD_STATE_SYSTEM.md — 음식 상태·행동 선행조건·연속성
- MEAL_CONTEXT_SYSTEM.md — 식문화/메뉴/그릇/재료 정합성
- PRODUCTION_PROTOCOL.md — 제작/승인/예외 게이트
- CURRENT_STATE.md — 현재 상태와 정확한 다음 행동
- assets/REFERENCE_MANIFEST.md — authoring reference 권위/해시
- assets/production/registry.json — approved production assets
- schemas/asset_registry.schema.json — Jipbap production-asset registry contract
- schemas/shot_contract.schema.json — shot semantics
- CALIBRATION_STATE.json — two-phase template/style calibration state
- calibration/COMPOSITION_CANDIDATES.md — placeholder spec candidates and approval boundary

## Current state

현재 active episode는 NONE이며 asset/template calibration 중이다.
COVER/LETTERING은 placeholder `SPEC_LOCKED`와 real-pixel `USER_LOCKED`를 분리한다.
production registry는 placeholder calibration과 분리되며 현재 0 assets 상태를 유지한다.
hybrid pilot은 BODY 4 slides 고정 fixture이며 COVER는 별도다. fresh 001은 이 pilot과 real-pixel template validation이 통과한 뒤 시작한다.

## Repository topology

Parent: noru358/AutoPipeline

Sibling child projects:
- noru358/instatoon
- noru358/talkshow
- noru358/jipbap
