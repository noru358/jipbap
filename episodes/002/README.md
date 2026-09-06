# Episode 002 — 고등어구이 + 흰밥

Status: PREPRODUCTION_USER_GATE

## Menu / moment

막 구운 고등어를 젓가락으로 가르고, 껍질 아래 살을 크게 떼어 흰밥 위에 올려 먹는 순간.

이 회차의 중심은 "고등어가 맛있다"는 평가가 아니라:
- 바삭한 껍질을 가르는 동작
- 살이 결대로 떨어지는 변화
- 밥 위에 한 점 올리는 작은 습관
- 먹고 난 뒤 가시와 빈 접시가 남는 결과
를 짧게 체험시키는 것이다.

## Content beats

5컷.

### S01 — arrival
Emotional beat:
- 평범한 저녁 식탁에 고등어 한 마리가 놓인 순간.
- 과장 없이 "오늘 저녁은 이거"라는 도착감.

State beat:
- mackerel.location=main_plate
- mackerel.skin=intact
- mackerel.flesh=mostly_intact
- rice.fullness=full
- chopsticks=available

Must show:
- 흰밥
- 구운 고등어
- 젓가락
- 소박한 집밥 식탁

Must not show:
- 이미 크게 뜯긴 살
- 이미 밥 위에 올라간 고등어
- 광고식 윤광/과장된 증기

### S02 — crack / open
Emotional beat:
- 제일 먼저 손이 가는 부분을 가까이 본다.

State beat:
- pre: mackerel.skin=intact, flesh=mostly_intact
- action: split_skin_and_flesh_with_chopsticks
- post: mackerel.skin=opened, flesh=exposed, one_flake=separated_or_ready

Must show:
- 젓가락이 껍질을 가르고 있는 실제 접점
- 껍질 아래 살결

Must not show:
- 살점이 이유 없이 밥 위에 순간 이동
- 생선이 원형으로 복구된 상태

### S03 — place on rice
Emotional beat:
- 크게 떼어낸 살 한 점을 밥 위에 올린다.

State beat:
- pre: one_flake=separated, rice.fullness=full_or_near_full
- action: place_fish_on_rice
- post: one_flake.location=on_rice, mackerel.flesh=partially_removed

Must show:
- 고등어 살 한 점이 밥 위에 놓이는 관계
- 원 접시에는 그만큼 살이 빠진 흔적

Must not show:
- 새 고등어 한 마리가 추가됨
- S02보다 생선 살이 더 온전해짐

### S04 — bite
Emotional beat:
- 설명 없이 실제 한입.

State beat:
- pre: one_flake.location=on_rice
- action: take_bite_with_rice_and_fish
- post: rice.fullness=partial, placed_flake=consumed_or_partial

Must show:
- 밥+고등어가 한입으로 이어지는 동작

Must not show:
- 먹기 전 상태로 되돌아감
- 과장된 리액션/광고 포즈

### S05 — residue
Emotional beat:
- 평가 대신 먹고 난 흔적.

State beat:
- pre: rice.fullness=partial_or_less, mackerel.flesh=partially_consumed
- action: continue_eating_offscreen_between_beats
- post: rice.fullness=nearly_empty_or_empty, mackerel=mostly_bones_and_small_remnants

Must show:
- 드러난 가시/남은 껍질
- 거의 비운 밥그릇
- 실제 먹은 흔적

Must not show:
- 다시 온전해진 생선
- 다시 가득 찬 밥그릇

## Voice draft

- S01: `오늘은 고등어 한 마리`
- S02: `껍질부터 젓가락이 간다`
- S03: `살은 크게 떼어서`
- S04: 무자막
- S05: `가시만 남았다`

Voice intent:
- LOW internetness
- 짧은 개인 기록체
- 맛있다/행복하다 같은 직접 평가 배제
- 마지막은 결과 상태로 종료

## Food-state graph

- S01 post:
  - mackerel.location=main_plate
  - skin=intact
  - flesh=mostly_intact
  - rice.fullness=full
- S02 action: split_skin_and_flesh_with_chopsticks
- S02 post:
  - skin=opened
  - flesh=exposed
  - one_flake=separated_or_ready
- S03 action: place_fish_on_rice
- S03 post:
  - one_flake.location=on_rice
  - mackerel.flesh=partially_removed
- S04 action: take_bite_with_rice_and_fish
- S04 post:
  - rice.fullness=partial
  - placed_flake=consumed_or_partial
- S05 post:
  - rice.fullness=nearly_empty_or_empty
  - mackerel=mostly_bones_and_small_remnants

## Bridge-action check

PASS.

핵심 위치 변화 `main_plate → chopsticks/separated → on_rice → consumed`가 각 행동으로 설명된다.
생선의 파손/섭취 상태와 밥 양은 뒤로 갈수록 되돌아가지 않는다.

## Visual rhythm

- S01: table medium
- S02: food macro / oblique close-up
- S03: top-oblique food close-up
- S04: eating medium close-up
- S05: quiet aftermath / table close-up

동일한 얼굴 3/4 구도 반복을 피하고 음식의 상태 변화가 화면 중심이 되게 한다.

## Gate

현재 단계는 `PREPRODUCTION_USER_GATE`.

사용자 승인 전:
- S01 렌더 금지
- 대사 래스터 삽입 금지
- 스타일 레퍼런스 없이 임의 작화 금지

승인 후:
1. actual style-reference binding preflight
2. S01 단일 이미지 / 무문자 생성
3. USER anchor gate
4. PASS 시 S02~S05 내부 QC 완주
