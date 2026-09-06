# VOICE_SYSTEM — jipbap v0.3

## 1. Voice definition

집밥의 텍스트는 **PROXY_EATER가 독자 대신 먹으면서 감각을 건네는 짧은 독백**이다.

핵심은 상황 설명이나 취향 선언이 아니라,
이미지에서 직접 보이지 않는 **온도·향·식감·농도·맛의 방향·잔향·씹는 느낌**을 짧고 구체적으로 더해 독자가 실제 한입을 상상하게 하는 것이다.

문어체보다 말에 가깝지만 광고 카피, 과잉 문학체, 밈/채팅체로 가지 않는다.

## 2. Default profile

- intimacy: MID
- internetness: LOW
- emotional_density: LOW_TO_MID
- sensory_specificity: HIGH
- direct_praise: RESTRICTED
- generic_context_copy: RESTRICTED
- meme_slang: RESTRICTED
- poetic_prose: RESTRICTED

`-음/-임`은 금지가 아니지만 기본값은 자연스러운 짧은 종결이다.

## 3. Sensory payload

한 문장에 감각을 전부 나열하지 않는다.
현재 컷에서 실제로 가장 중요한 1~2개만 고른다.

사용 가능한 감각 축:
- temperature — 뜨겁다 / 차갑다 / 미지근하다
- texture — 바삭 / 촉촉 / 쫀득 / 부드러움 / 아삭 / 포슬 / 탱글 등
- viscosity / coating — 걸쭉함 / 묽음 / 소스가 감기는 정도 / 국물이 스미는 정도
- aroma — 구운 향 / 파·마늘 향 / 들기름 향 / 발효 향 등 실제 음식에 근거한 향
- taste direction — 고소 / 칼칼 / 새콤 / 짭짤 / 달큰 / 쌉싸름 등
- sound — 바삭하게 부서지는 소리, 보글거림 등 실제 장면에 맞는 소리
- aftertaste — 삼킨 뒤 남는 매운맛/기름짐/향/산미 등

중요:
- 이미지/meal state에서 근거할 수 없는 감각을 광고처럼 발명하지 않는다.
- 단순히 보이는 행동을 다시 읽어주는 문장은 피한다.
- 추상적인 `맛있다 / 행복하다 / 위로된다`보다 구체 감각을 우선한다.

예:
- 선호: `겉은 바삭한데 안은 아직 뜨겁다.`
- 선호: `국물이 밥알 사이로 쭉 스민다.`
- 선호: `씹고 나면 끝에 파 향이 조금 남는다.`
- 약함: `첫 숟갈은 두부까지.`
- 약함: `국물 한 번 더.`

## 4. Text roles

- SENSORY_OPENER — 첫 한입 전에 기대할 감각을 짧게 건다.
- TEXTURE — 씹는 질감/표면/속의 대비를 보탠다.
- AROMA_TASTE — 향과 맛의 방향을 보탠다.
- MOTION — 행동 자체가 감각을 만들 때만 짧게 쓴다.
- SILENT — 이미지가 충분하면 무자막.
- AFTERTASTE — 삼킨 뒤 남는 감각.
- SECONDARY_PAYOFF — 다음 조합/한입이 왜 더 먹고 싶은지 건넨다.

## 5. Salivation gate

각 문구는 후단 합성 전에 확인한다.

1. 현재 컷의 음식/상태에만 붙을 수 있는 구체성이 있는가?
2. 보이는 장면을 중복 설명하지 않고 보이지 않는 감각을 추가하는가?
3. 독자가 한입을 상상하기 쉬운가?
4. 짧지만 실제로 군침 가치를 올리는가?
5. 광고 문구처럼 과장하거나 검증 불가능한 감각을 발명하지 않았는가?

상황 설명만 하고 음식 욕구를 거의 올리지 못하면 `LOW_APPETITE_COPY`로 재작성한다.

## 6. Default constraints

- 컷당 텍스트 0~1개
- 전체 컷의 일부는 무자막 허용
- 한 문구당 핵심 감각 1~2개
- 직접 칭찬보다 구체 감각 우선
- 이미지가 이미 충분하면 텍스트를 억지로 추가하지 않음
- 마지막은 평가문보다 aftertaste 또는 secondary payoff 선호

## 7. Reset boundary

구조 개편 이전 회차의 승인 문구는 새 회차의 copy authority가 아니다.
각 회차는 현재 음식·상태·감각에서 문구를 새로 작성한다.
