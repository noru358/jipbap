# Episode 001 — 계란후라이 + 흰밥

Status: PREPRODUCTION_RECOMPILE

## Concept

평범한 계란후라이와 흰밥을 먹는 과정 자체를 짧게 보여준다.
맛있다는 평가를 직접 반복하지 않고 음식의 상태 변화와 잔여 행동으로 전달한다.

## Approved visual/storyboard direction

5컷.

### S01 — arrival
- 늦은 저녁의 작은 식탁
- 흰밥, 접시 위 계란후라이, 김, 간장
- 먹기 직전
- 현재 생성물은 임시 시각 앵커로만 사용

### S02 — transformation
- **계란후라이가 이미 밥 위에 올라가 있음**
- 노른자는 intact 상태에서 시작
- 젓가락으로 노른자를 막 터뜨림
- 노른자가 밥 쪽으로 흐르기 시작

### S03 — seasoning
- 밥 위 계란 + 이미 터진 노른자 상태를 유지
- 간장을 아주 조금 추가
- 김을 곁들일 수 있음

### S04 — bite
- 실제 한입
- 음식/숟가락(또는 젓가락)/입의 관계가 읽힘
- 과도한 광고식 음식 클로즈업은 피함

### S05 — residue
- 거의 비운 그릇
- 먹은 양이 앞 컷보다 역행하지 않음
- 잔여 행동으로 끝냄

## Voice

- S01: 오늘은 그냥 이거
- S02: 노른자는 반숙
- S03: 간장은 조금만
- S04: 무자막
- S05: 밥 다시 푸는 중

## State graph

- S01 post: `egg.location=plate`, `egg.yolk=intact`, `rice.fullness=full`
- bridge before S02: `place_egg_on_rice`
- S02 pre: `egg.location=on_rice`, `egg.yolk=intact`
- S02 post: `egg.location=on_rice`, `egg.yolk=runny`
- S03 pre: S02 post + `soy_sauce=available`
- S03 post: `rice.topping=egg_and_soy`
- S04 post: `rice.fullness=partial`
- S05 post: `rice.fullness=nearly_empty_or_empty`

## Known prototype failures

- 멀티패널 합본 생성: 정식 생산 실패
- 접시 위 노른자 파열 후 밥 위로 점프: 상태 연속성 실패

다음 렌더는 위 두 실패를 구조적으로 차단한 계약으로 재시도한다.
