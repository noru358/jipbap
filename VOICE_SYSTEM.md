# VOICE_SYSTEM — jipbap v0.1

## 1. Voice definition

기본 텍스트는 **친한 사람이 자기 피드에 혼잣말처럼 적는 짧은 개인 기록체**다.

문어체보다 말에 가깝지만 유행어·밈·채팅체를 기본값으로 삼지 않는다. 감정을 설명하기보다 행동·취향·디테일을 적는다.

## 2. Default profile

- intimacy: MID
- internetness: LOW
- emotional_density: LOW
- direct_praise: RESTRICTED
- meme_slang: RESTRICTED
- poetic_prose: RESTRICTED
- preferred_endings: natural short declarative / residual action

`-음/-임`은 금지가 아니라 인터넷성이 높을 때 선택적으로 사용한다. 기본값은 자연스러운 종결을 선호한다.

예:
- 선호: `괜히 이게 먹고 싶었다`
- 기본값 아님: `괜히 이게 먹고 싶었음`

문장 조각은 자연스러우면 허용한다.
- `오늘은 그냥 이거`
- `노른자는 반숙`
- `간장은 조금만`
- `밥 다시 푸는 중`

## 3. Text roles

- OPENER — 시작 선언
- PREFERENCE — 개인 취향/먹는 규칙
- MOTION — 지금 벌어지는 작은 동작
- SILENT — 무자막 반응
- RESIDUAL — 감상 대신 결과 행동으로 마무리

## 4. Default constraints

- 컷당 텍스트 0~1개
- 전체 컷의 일부는 무자막 허용
- 맛있다/행복하다/위로된다 같은 추상 감상어 최소화
- 마지막은 평가문보다 잔여 행동 선호
- 광고 카피, 과잉 문학체, 과잉 커뮤체는 기본 FAIL

## 5. Episode 001 approved copy direction

- S01: `오늘은 그냥 이거`
- S02: `노른자는 반숙`
- S03: `간장은 조금만`
- S04: 무자막
- S05: `밥 다시 푸는 중`

문구는 회차 종속 예시이며, 위 구조를 하드코딩하지 않는다.
