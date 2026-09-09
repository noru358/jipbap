# V1_E007 PLAN

Updated: 2026-09-09
Status: DRAFT_AWAITING_STORYBOARD_USER_GATE
Episode: V1_E007
Food: 수육국밥
Product concept: PROXY_EATER
Format: COVER + BODY S01..S06
BODY authoring: SIX_PANEL_BOARD_FIRST / text-free 2×3 master board
Final page ratio: 4:5

## User-required story facts

- V1_E006 is fully abandoned as current production authority. No E006 storyboard/copy/artwork/crop/presentation/package may be reused for E007.
- Core menu is 수육국밥.
- S01 must show the protagonist already drunk, loosely staggering / 휘적휘적 into a 국밥집.
- The BODY must include a clearly readable payoff where 깍두기 is mixed/combined into the 국밥 and then eaten, not merely shown as a side dish.

## COVER intent

- Distinct text-free hero artwork, not a BODY crop.
- A steaming bowl of 수육국밥 dominates the foreground; thick boiled-pork slices are clearly readable.
- Slightly tipsy protagonist leans toward the bowl with softened/red cheeks, but the food is the hero.
- Leave natural negative space for title lettering without forcing a rigid header box.
- Default cover grammar: `EP.7 취한 밤과 수육국밥`.
- Protected focal regions: protagonist face, pork/bowl hero, spoon hand.

## BODY storyboard

### S01 — 취한 채 국밥집으로
- New beat: late-night arrival / recognition.
- Action + state: cheeks a little flushed, eyelids heavy, shoulders loose; protagonist 휘적휘적 walks through the restaurant door, one hand catching the doorframe/handle for balance. No food visible yet.
- Camera: wide-to-medium exterior/threshold shot, slight oblique angle; enough storefront/interior cue to read “국밥집” without dense background detail.
- Expression: tired, tipsy, magnetically drawn inside.
- Copy:
  - speech: `사장님… 수육국밥 하나요.`
- Copy-space hint: upper-side empty wall/door area.
- Avoid: face, door-grip hand, walking legs.
- Continuity: next scene is seated bowl arrival.

### S02 — 김 올라오는 수육국밥
- New beat: anticipation / sensory reveal.
- Action + state: steaming bowl lands in front of protagonist; generous 수육 slices, scallion and broth are clearly visible.
- Camera: food-forward 3/4 close-up, bowl dominant; protagonist soft-focus/partial in background.
- Expression: eyes beginning to refocus on the bowl.
- Copy:
  - inner_thought: `와… 냄새부터 좀 살겠다.`
- Copy-space hint: side negative space, not over the pork.
- Avoid: pork surface, steam plume, face.
- Continuity: untouched bowl → first taste.

### S03 — 뜨거운 국물 첫입
- New beat: first ingestion / warmth payoff.
- Action + state: spoon has actually reached the mouth; protagonist takes the first clear broth sip. Bowl remains mostly untouched.
- Camera: medium-close 3/4 face + spoon, bowl lower foreground.
- Expression: half-dead tipsy face loosens as warmth hits; subtle eye focus returns.
- Copy:
  - inner_thought: `아… 뜨끈한 게 내려간다.`
- Copy-space hint: opposite side of spoon path.
- Avoid: eyes, spoon-mouth contact, bowl rim.
- Continuity: ingestion is established before sensory reaction text.

### S04 — 수육 한 점, 국밥 한술
- New beat: meat/body satisfaction.
- Action + state: thick, tender-looking 수육 slice is lifted with spoonful of rice/broth or positioned directly over the spoon; meat grain is illustrated but not photoreal.
- Camera: tight hand/food close-up with a partial lower-face reaction, different from S03.
- Expression: small anticipatory grin / focused hunger.
- Copy:
  - inner_thought: `고기 두께 봐.`
- Copy-space hint: upper corner away from hand-food contact.
- Avoid: pork, spoon, fingers.
- Continuity: keep food geometry physically plausible; no taste claim before ingestion.

### S05 — 깍두기 국물 넣고 쓱
- New beat: transformation / secondary payoff setup.
- Action + state: protagonist adds a little 깍두기 국물 into the 국밥, drops in/presses a piece of 깍두기, then visibly stirs once so part of the broth/rice turns lightly reddish. The side-dish bowl remains nearby as source.
- Camera: overhead/steep 3/4 action shot centered on bowl + hand; face optional or cropped.
- Expression: not primary; deliberate “이제 이거” gesture.
- Copy:
  - inner_thought: `여기서 깍두기 좀 말아주고.`
  - sfx: `쓱-`
- Copy-space hint: clean table corner.
- Avoid: stirring hand, spoon, 깍두기 piece, transformed broth region.
- Continuity: the final bite must visibly derive from this changed bowl state.

### S06 — 깍두기까지 같이 한입
- New beat: ingestion + reaction / final appetite payoff.
- Action + state: spoonful from the now lightly reddish 국밥 reaches the mouth and visibly contains rice/broth, 수육, and a piece of 깍두기 (or unmistakable 깍두기 component). Bite is actually taken in-panel.
- Camera: tight expressive 3/4 face with spoon-mouth contact; bowl can sit blurred/low in frame. Do not repeat S03 framing exactly.
- Expression: eyes brighten, cheeks still a little flushed; modestly amplified satisfaction.
- Copy:
  - inner_thought: `아삭하고 새콤한 게 딱 끊어주네.`
- Copy-space hint: side opposite spoon entry.
- Avoid: eyes, mouth/spoon contact, visible 깍두기 on spoon.
- Continuity: this is the payoff of S05 transformation, not a separate untouched side-dish bite.

## Overall visual rhythm

- S01: wider context / unsteady body movement.
- S02: food hero close-up.
- S03: face + broth ingestion.
- S04: hand/meat macro.
- S05: overhead transformation action.
- S06: tight expressive ingestion payoff.
- Background stays sparse except S01 context; do not hardcode a fixed camera recipe beyond what this story needs.
- PERSON/FOOD drawing language stays locked to approved renderer carriers when artwork generation begins.

## Storyboard QC before user gate

- Exactly six BODY beats: PASS.
- S01 user-required drunk/staggering entrance: PRESENT.
- Core menu identity as 수육국밥: PRESENT.
- 깍두기 is not decorative-only; transformation + ingestion payoff spans S05→S06: PRESENT.
- Sensory copy occurs only after visible/established ingestion: PASS.
- Camera/shot rhythm does not collapse into repeated face-at-table composition: PASS.
- No generated-text requirement is placed on the master BOARD: PASS.
- No episode-specific rule is promoted into a permanent V1 hard gate: PASS.

## Gate

Current gate: `STORYBOARD_USER_GATE`
Exact next action: show this storyboard to the user for revision/approval. Do not generate BODY or COVER before approval. On approval, bind the locked PERSON + FOOD renderer carriers and proceed to `INITIAL_ART_BUNDLE`.
