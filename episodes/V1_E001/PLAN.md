# V1_E001 PLAN

Updated: 2026-09-08
Status: DONE
Format: COVER 1 + BODY 6
Architecture: SIX_PANEL_BOARD_FIRST
Core menu: 제육볶음 + 흰밥
Concept: 만화 속 인물이 독자 대신 갓 볶은 제육볶음을 밥과 함께 먹어 주는 PROXY_EATER episode.

## COVER intent
- Title: `제육 한 점, 밥 한 숟갈`
- Main image: accepted S01 artwork reused deterministically.
- Character: one primary character.
- Cover text is deterministic post-processing.

## BODY storyboard — approved

### S01 — 첫 향이 오는 순간
- Story function: arrival / anticipation
- Camera: 3/4 medium with food foreground.
- Action: character leans toward freshly cooked 제육볶음.
- Copy: inner thought `이 냄새부터 반칙인데.`

### S02 — 흰밥 위에 얹기
- Story function: transformation / anticipation
- Camera: rice-bowl close-up from a distinct side angle.
- Action: chopsticks place one piece of 제육 onto white rice.
- Copy: inner thought `밥 위에 올리면 끝.`
- Continuity: the rice+pork combination becomes the next lifted bite.

### S03 — 한입으로 집어 올리기
- Story function: approach / sensory reveal
- Camera: distinct food-detail close-up.
- Action: the rice+pork combination is lifted as one complete bite.
- Copy: silent.
- Continuity: direct continuation of S02.

### S04 — 한입 완성
- Story function: ingestion
- Camera: 3/4 face/action close-up.
- Action: character brings the rice+pork bite to the mouth / begins the bite.
- Copy: speech `아, 이건…`
- Contact geometry must remain physically plausible.

### S05 — 상추쌈에 편마늘 올리기
- Story function: secondary preparation / anticipation
- Camera: hand/action-dominant medium close-up.
- Food state: lettuce already holds 제육; sliced garlic is being placed on top.
- Action: garlic placement is visible; this is NOT yet an eating shot.
- Copy: inner thought `상추에 편마늘까지 올리면 또 다르지.`

### S06 — 결국 한입 더
- Story function: residue / secondary payoff
- Camera: wider 3/4 table shot.
- Action: character reaches back toward the 제육 for another bite.
- Food state: believable consumption residue in pork and rice.
- Copy: inner thought `한입만 더 먹을게.`

## Visual rhythm
- S01: medium anticipation
- S02: rice placement detail
- S03: lifted-bite detail
- S04: face/action close-up
- S05: ssam assembly hand-action
- S06: wider return-to-food shot
- Camera/framing/action must not collapse into repetitive front-facing close-ups.

## Style correction approved during BOARD calibration
- Food must remain clearly illustrated, not photo-real.
- Reduce gloss, microtexture and advertising-food realism.
- Keep PERSON and FOOD in one coherent drawn medium.

## Copy boundary
- Generated BODY board remains text-free.
- Copy is added only in deterministic post-processing.
- No generic `잘 먹었다` ending.

## Hard continuity contract
1. Core menu remains 제육볶음 + 흰밥.
2. S02 → S03 → S04 forms a valid rice+pork state transition.
3. S05 is lettuce + already-placed pork + sliced garlic being added.
4. S04 hand/chopstick/food/mouth contact remains plausible.
5. S06 shows believable consumption residue.
6. Same primary character identity and illustrated medium across repeated appearances.
7. No meaning-bearing text in generated BODY raster.

## Approval record
- STORYBOARD_USER_GATE: USER_APPROVED
- BOARD_STYLE_USER_GATE: USER_APPROVED after one corrective regeneration addressing staging variety, S05 garlic placement, and food illustration realism.
