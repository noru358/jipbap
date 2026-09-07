# jipbap

> This README is descriptive documentation, not runtime state authority.
> For execution, read `CURRENT_STATE.md`; when media integrity is blocked also read
> `INTEGRITY_STATE.json`. Do not infer a next action from stale summary text here.

짧은 집밥/음식 감상형 만화 제작 프로젝트. AutoPipeline 아래에서 instatoon과 독립된 child authority를 가진다.

## Core production flow

`menu/moment → sensory/meal-context plan → food-state storyboard → asset resolve → missing asset authoring → deterministic BODY composition → mandatory COVER + lettering → QC/export`

현재 설계된 시각 방식은 **COMPOSITION_FIRST_HYBRID_FOOD**이며, calibration 비교가 끝나기 전까지 다른 렌더 lane으로의 전면 전환은 확정하지 않는다.

- PERSON: 승인된 인물/포즈 asset을 재사용한다.
- FOOD/FOOD_STATE: 메뉴와 상태 변화가 핵심이므로 회차별 신규 생성 허용 비중이 높다.
- HAND/UTENSIL/CONTACT: 필요한 경우 episode-local interaction asset을 만든다.
- BACKGROUND/PROP: 가능한 것은 재사용한다.
- FULL FRAME GENERATION: 명시적 exception lane.
- lettering/UI/cover title: deterministic editable composition이 소유한다.

## Fixed principles

- PROXY_EATER: 독자 대신 만화 속 인물이 먹고 감각을 전달한다.
- BODY는 food-state transition과 실제 먹는 순서를 따른다.
- 식문화/메뉴/그릇/도구는 MEAL_CONTEXT_SYSTEM으로 검수한다.
- 한 컷 = 한 이미지 파일.
- 의미가 있는 글자는 raster asset에 굽지 않는다.
- cover는 BODY와 별도인 mandatory first slot이다.
- 승인 asset은 hash-bound이며 bytes가 바뀌면 승인이 승계되지 않는다.
- **hash만 기록하는 것으로는 충분하지 않다. tracked raster는 full-decode media integrity gate를 통과해야 한다.**
- 실패는 최소 범위만 무효화한다.

## Canonical execution references

- CURRENT_STATE.md — 현재 단계와 exact next action
- INTEGRITY_STATE.json — 현재 media-byte recovery 상태
- PRODUCTION_PROTOCOL.md — 제작/승인/예외 게이트
- CONTENT_SYSTEM.md — 음식/순간과 PROXY_EATER 비트
- VOICE_SYSTEM.md — 텍스트 말투
- VISUAL_SYSTEM.md — visual/render policy
- FOOD_STATE_SYSTEM.md — 음식 상태·행동 선행조건·연속성
- MEAL_CONTEXT_SYSTEM.md — 식문화/메뉴/그릇/재료 정합성
- assets/reference_registry.json — machine-readable reference byte identity
- assets/production/registry.json — production asset identity
- pipeline/validate.py — executable media-integrity validation

## Repository topology

Parent: noru358/AutoPipeline

Sibling child projects:
- noru358/instatoon
- noru358/talkshow
- noru358/jipbap
