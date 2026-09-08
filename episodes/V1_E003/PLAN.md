# V1_E003 PLAN

Episode: V1_E003
Menu: 제육볶음 한 상
Architecture: SIX_PANEL_BOARD_FIRST
Presentation shell: JIPBAP_PRESENTATION_SHELL_V2
Carousel: COVER + 6 BODY
Master board: text-free 2 columns × 3 rows
Final ratio: 4:5

## Episode intent

집에서 막 볶아낸 제육볶음을 한입 먹는 순간을 중심으로 간다.
음식의 양념 상태, 불향이 살짝 밴 가장자리, 밥과 섞였을 때의 질감, 매콤달큰한 뒷맛이 주인공이다.
배경은 식사 맥락에 필요한 최소 요소만 둔다.

## COVER direction

Working title: 제육은 밥을 늘린다
Small menu tag: 집밥 3화 · 제육볶음
Hero direction: 제육 한 점을 막 집어 올린 순간을 크게 잡고, 음식이 주인공으로 읽히게 한다.
Title and hero must have intentional negative space under JIPBAP_PRESENTATION_SHELL_V2. Do not stretch BODY artwork.

## Six BODY beats

### S01 — arrival / heat
- Food state: 막 볶아낸 제육볶음. 양념은 윤기가 과하지 않고, 돼지고기·양파·대파가 분명히 보인다.
- Visual: 팬 또는 접시의 제육을 음식 중심의 근접샷. 아주 약한 김과 볶인 가장자리.
- Camera: food close-up, slightly high 3/4 angle.
- Person: 없어도 됨.
- Copy draft: "팬 열자마자 냄새 확."
- Lettering role: narration.
- Continuity: 다음 컷에서 바로 집어 올릴 수 있는 상태.

### S02 — pick / anticipation
- Food state: 제육 한 점과 양파가 젓가락에 함께 들린다.
- Visual: 음식이 전경, 인물은 반신 정도로 뒤에. 기대감은 중립보다 조금 크게.
- Camera: medium-close 3/4, S01과 다른 거리감.
- Action: 젓가락으로 한 점 집어 올림. 손·젓가락·고기 접촉이 명확해야 한다.
- Copy draft: "끝에 살짝 탄 데부터."
- Lettering role: inner_thought.
- Continuity: 고기는 아직 입에 들어가지 않음.

### S03 — rice combination
- Food state: 흰밥 위에 제육과 양파를 올리고 소량의 양념이 밥알에 스민다.
- Visual: 밥그릇과 젓가락/숟가락 중심의 손동작 디테일. 얼굴은 생략 가능.
- Camera: close top/oblique detail shot.
- Action: 제육을 밥 위에 얹어 한입 조합을 만든다.
- Copy draft: "양념 밥에 좀 묻혀서."
- Lettering role: inner_thought.
- Continuity: S04에서 같은 조합이 입으로 이동할 수 있어야 함.

### S04 — bite
- Food state: 제육+밥 한입.
- Visual: 인물 3/4 얼굴 근접. 입 앞의 한입이 분명하고, 음식/도구/입 위치가 물리적으로 맞는다.
- Camera: face close-up, side relation distinct from S02.
- Expression: 기대 → 먹는 순간의 집중. 과장하되 그림체 안에서.
- Copy draft: "음."
- Lettering role: speech.
- Optional SFX: "냠"
- Continuity: 한입이 실제로 들어가는 순간. 손/팔 추가 생성 금지.

### S05 — sensory reaction
- Food state: 먹은 직후.
- Visual: 얼굴 반응을 조금 더 크게. 음식은 보조적으로 프레임 하단에 남겨도 됨.
- Camera: tighter reaction shot or slight low 3/4.
- Expression: 달큰함 뒤에 매콤함이 올라오는 순간. 만족 + 약간의 열감.
- Copy draft: "달큰한데 뒤에 매콤함 딱 옴."
- Lettering role: inner_thought.
- Continuity: 과도한 만화적 화염/광고식 효과는 쓰지 않음.

### S06 — secondary payoff
- Food state: 남은 제육 양념이 밥에 살짝 묻고, 다음 한입이 준비된다.
- Visual: 인물과 음식이 함께 보이는 조금 넓은 마무리샷. 빈 접시 엔딩이 아니라 아직 먹는 중.
- Camera: wider medium shot, 이전 컷과 다른 리듬.
- Action: 밥 한 숟갈을 더 뜨거나 제육을 다시 집으려는 자연스러운 다음 동작.
- Copy draft: "이건 밥을 더 먹게 됨."
- Lettering role: speech or inner_thought.
- Continuity: 억지 결론 없이 '다음 한입' 욕구로 끝.

## Visual rhythm

food macro → person+food medium → hand/rice detail → bite close-up → reaction close-up → wider continuing-meal shot

Variety is intentional but not a fixed slot template. Camera side, face direction, hand pose and exact crop remain fluid at render time.

## BOARD hard-fail reminders

Retry only for publish-blocking defects:
- not exactly 6 extractable cells / panel bleed
- generated text
- catastrophic identity or drawing-medium drift
- obvious focal anatomy/contact failure
- impossible food-state/action contradiction
- wrong core menu/entity

Soft issues such as mildly repetitive framing, minor utensil placement, or slightly generic background do not create new permanent gates.

## FOOD rendering direction

Appetizing illustrated food, not food photography.
Keep sauce gloss restrained, no ad-style lacquer, splash, excessive steam or photographic depth-of-field.
PERSON and FOOD must read as the same illustrator / same medium.

## Copy policy

Keep mobile copy short and natural.
One reaction plus at most one concrete sensory observation per beat.
Do not narrate obvious hand motion when the image already shows it.
