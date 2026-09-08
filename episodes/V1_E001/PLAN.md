# V1_E001 PLAN

Updated: 2026-09-08
Status: STORYBOARD_USER_GATE
Format: COVER 1 + BODY 6
Architecture: SIX_PANEL_BOARD_FIRST
Core menu: 제육볶음 + 흰밥
Concept: 만화 속 인물이 독자 대신 갓 볶은 제육볶음을 밥과 함께 먹어 주는 PROXY_EATER episode.

## COVER intent
- Title draft: `제육 한 점, 밥 한 숟갈`
- Main image: 윤기 과하지 않은 붉은 제육 한 점을 젓가락으로 들어 흰밥 위에 막 올리려는 순간.
- Character: 한 명만 등장. 음식보다 작게, 기대감 있는 표정.
- Background: 식탁 맥락을 이해시키는 최소 형태만. 장식용 배경 금지.
- Cover text is deterministic post-processing, not generated raster text.

## BODY storyboard

### S01 — 첫 향이 오는 순간
- Story function: arrival / recognition / anticipation
- Camera: 3/4 medium close, 음식이 전경, 인물은 뒤쪽에 일부만.
- Food state: 갓 볶아 접시에 담긴 제육. 돼지고기·양파가 읽히고 소스는 촉촉하지만 광고식 광택은 없음.
- Visible action: 젓가락을 들기 직전, 인물이 접시 쪽으로 살짝 몸을 기울임.
- Expression: 냄새를 맡고 눈이 조금 커진 기대감.
- Copy draft: 내면독백 `이 냄새부터 반칙인데.`
- Continuity: 다음 컷에서 같은 접시의 한 점을 집을 수 있어야 함.

### S02 — 제일 맛있어 보이는 한 점 고르기
- Story function: approach / sensory reveal
- Camera: top-oblique food close-up. 손과 젓가락만 최소 노출.
- Food state: 접시 위 제육 한 점과 양파 조각이 분리되어 보임.
- Visible action: 젓가락이 얇게 말린 고기 한 점을 정확히 집어 듦.
- Expression: 얼굴 미노출 가능.
- Copy draft: 무문자.
- Continuity: 집은 고기 한 점이 다음 컷에서 밥 위로 이동.

### S03 — 흰밥 위에 얹기
- Story function: transformation / anticipation
- Camera: rice-bowl close-up, 살짝 낮은 측면.
- Food state: 흰밥 위에 제육 한 점이 막 놓이고 소스가 아주 조금 밥알에 묻음.
- Visible action: 젓가락이 고기를 내려놓는 순간.
- Expression: 얼굴 미노출 또는 입가만 프레임 가장자리에.
- Copy draft: 내면독백 `밥 위에 올리면 끝.`
- Continuity: 다음 컷의 한입은 이 조합에서 바로 이어져야 함.

### S04 — 한입 완성
- Story function: ingestion
- Camera: 3/4 face close-up, 젓가락과 한입이 입 앞에 또렷하게 보임.
- Food state: 제육 + 밥이 한입 크기로 함께 잡혀 있음.
- Visible action: 입에 넣기 직전 또는 막 베어 무는 순간. 손·젓가락·음식·입 접촉이 물리적으로 자연스러워야 함.
- Expression: 기대가 최고점에 오른 집중된 표정.
- Copy draft: 대사 `아, 이건…`
- Continuity: S03에서 만든 밥+제육 조합을 그대로 먹은 결과여야 함.

### S05 — 매콤달큰한 첫 반응
- Story function: reaction / aftertaste
- Camera: 정면에 가까운 shoulder-up. 음식은 화면에서 잠시 빠져도 됨.
- Food state: 입안에 한입을 먹은 직후.
- Visible action: 천천히 씹다가 눈이 살짝 가늘어지고 어깨 힘이 풀림.
- Expression: 과장된 감탄보다 실제로 맛있는 걸 먹었을 때의 작은 만족.
- Copy draft: 내면독백 `매콤한데 끝은 달큰하다.`
- Continuity: 다음 컷에서 다시 접시로 손이 가는 이유가 자연스럽게 이어짐.

### S06 — 결국 한 숟갈 더
- Story function: residue / secondary payoff
- Camera: wider 3/4 table shot with diagonal action.
- Food state: 첫입 이후 제육 접시에 작은 빈자리, 밥그릇도 한입 줄어든 상태.
- Visible action: 젓가락은 다시 제육으로 향하고, 다른 손은 밥그릇을 살짝 당김.
- Expression: 말없이 다음 입을 고르는 편안한 몰입.
- Copy draft: 내면독백 `한입만 더 먹을게.`
- Continuity: 섭취 흔적이 S01보다 분명하되 접시/그릇 위치와 메뉴 정체성은 유지.

## Visual rhythm
- S01: 음식 중심 3/4 medium
- S02: top-oblique extreme food detail
- S03: low-side rice detail
- S04: face/action close-up
- S05: reaction close-up
- S06: wider diagonal table shot
- 동일한 카메라 방향/샷 크기를 반복하지 않고, 음식→행동→감각→재접근의 리듬을 만든다.

## Copy boundary
- Generated BODY board remains completely text-free.
- Above copy is lettering draft only and may be revised at assembly.
- No generic `잘 먹었다` ending.
- Copy never explains an already obvious hand motion.

## Hard continuity contract
1. Core menu stays 제육볶음 + 흰밥 throughout all six BODY cells.
2. S02에서 집은 제육이 S03 밥 위에 놓이고, S04에서 그 밥+제육 한입을 먹는 상태 전이가 성립해야 한다.
3. S04의 젓가락/손/음식/입 contact geometry must be plausible.
4. S06 shows believable consumption residue from earlier panels.
5. Same primary character identity and same illustrated medium across repeated appearances.
6. No generated text, speech bubble, logo, number or panel label in BODY raster.

## User gate
Stop here for explicit storyboard review.
Do not generate a master board before storyboard approval.
