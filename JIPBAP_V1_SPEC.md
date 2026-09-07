# JIPBAP_V1_SPEC

Updated: 2026-09-08
Status: FROZEN_FOR_V1
Canonical visual architecture: SIX_PANEL_BOARD_FIRST

## 0. Product contract

집밥은 독자 대신 만화 속 인물이 한입 먹어주는 `PROXY_EATER` 음식 감상형 인스타툰이다.
음식의 상태, 먹는 동작, 감각 payoff가 중심이며 인물과 배경은 그 경험을 전달하는 만큼만 사용한다.

V1 최적화 목표:
1. publishable episode당 사람 개입 시간 감소
2. publishable episode당 이미지 생성 호출 수 감소
3. first-pass publishable rate 상승
4. rework loop 감소

작화 품질은 무한 최적화 대상이 아니라 publishable quality floor로 관리한다.

## 1. Frozen format

### 1.1 Carousel
- COVER 1장 + BODY 6장 = 총 7장.
- 모든 최종 carousel page는 4:5.
- COVER는 BODY S01이 아니며 food-state sequence에도 포함되지 않는다.

### 1.2 BODY generation container
- BODY는 정확히 6컷.
- 기본 생성 단위는 무문자 6컷 master board 한 장.
- board grid는 2 columns × 3 rows의 동일 셀.
- 6컷은 독립 생성하지 않는다. V1 기본은 한 생성 안에서 공동 샘플링하여 continuity를 얻는 것이다.
- panel boundary는 명확해야 하며 panel 간 bleed/collage 혼합을 허용하지 않는다.
- board는 생성 컨테이너이지 최종 carousel layout authority가 아니다.

### 1.3 Deterministic presentation shell
master board PASS 후에는 확률적 재생성 없이:
1. six-cell extraction
2. 4:5 page fit
3. cover assembly
4. lettering / speech / inner-thought vector composition
5. export
를 deterministic post-processing으로 처리한다.

Artwork는 stretch하지 않는다. 4:5 adaptation은 crop, safe margin, padding, placement 중 고정 template 규칙으로 처리한다.

## 2. Frozen visual result range

### 2.1 PERSON
Primary style authority:
- `PERSON_STYLE_REF_1`

Subordinate target-look anchor:
- `TARGET_LOOK_BOARD_REF_1`

The auxiliary board may influence only:
- face construction and facial proportion
- eye grammar
- hair silhouette
- line / texture / color treatment
- shared screen language when person and food coexist

It does not own:
- text
- panel layout
- cut order
- menu
- camera
- composition
- meal-context entity selection

Frozen PERSON result characteristics:
- semi-real webtoon illustration, not photoreal
- slightly simplified rather than polished anime realism
- recognizable hand-drawn line character
- restrained shading; no cinematic rendering
- natural eye grammar within the approved reference distribution
- no generic oversized doll/anime eyes
- no excessive eyelash, gloss, hair sparkle, skin airbrushing
- face and body remain believable enough for eating actions

### 2.2 FOOD
Frozen FOOD result characteristics:
- immediately appetizing
- clearly illustrated rather than food-photo realism
- enough material detail to read ingredient, doneness, moisture and current food state
- microtexture is simplified
- highlights and gloss are restrained
- no advertisement-style sauce splash, excessive steam, lacquer gloss or photographic depth-of-field
- food may carry slightly more surface detail than PERSON, but both must still look drawn in the same medium

### 2.3 Cross-domain coherence
Hard style principle:
- PERSON and FOOD must look like one illustrator / one medium made them.
- A flat webtoon PERSON beside near-photographic FOOD is not acceptable.
- realism may vary slightly by subject, but line/color/light abstraction must stay coherent.

### 2.4 Background
Frozen policy:
- omit background and decorative assets unless they materially explain the eating moment.
- when needed, use only the minimum contextual shapes/objects required.
- no ornamental cozy-room filling by default.
- background must not become the visual focal point over food/action.

### 2.5 Text
- no meaning-bearing text is baked into generated BODY raster.
- no generated speech bubbles, captions, labels, logos or panel numbers.
- cover title, speech, narration and inner thought are editable deterministic layers.

## 3. What remains deliberately fluid

The following are NOT V1 locks:
- menu
- episode subject identity
- face direction
- camera side
- camera height
- shot scale
- framing
- pose
- expression
- hand shape
- utensil angle
- eating posture
- food placement
- table arrangement
- exact background
- amount of person visible
- per-panel composition
- dialogue
- inner-thought copy
- which storytelling function occupies which of the six slots

Style is frozen; staging is fluid.

## 4. Six-slot storytelling rule

Six slots are a fixed render surface, not six fixed event labels.

A normal episode should collectively contain enough of the following functions to create an appetite arc:
- arrival / recognition
- anticipation
- preparation or approach
- transformation
- sensory reveal
- ingestion
- reaction / aftertaste
- residue / secondary payoff

They may be merged, repeated or reordered.

Do NOT hardcode:
S01=intro, S02=prep, S03=break, S04=bite, etc.

If a menu/moment cannot support six publishable visual beats without procedural filler, choose a stronger moment or use sensory/reaction/detail beats. Do not make BODY count variable in V1.

## 5. Physical and semantic continuity

Board planning must define only what is necessary to avoid impossible states:
- current food state
- visible action
- immediately required precondition
- next visible consequence

Do not build a full asset dependency DAG.

For eating interactions:
- spoon/chopstick/hand/food/mouth geometry must make physical sense at the visible moment.
- bridge actions may occur between panels, but before/after states must be compatible.
- cultural meal details follow the current episode context; no global Korean table-setting pose is hardcoded.

## 6. QC: hard fail vs soft score

### 6.1 Hard FAIL only
Reject/retry a master board only for publish-blocking defects:
1. not exactly six extractable cells, or severe panel bleed/geometry failure
2. unintended generated text
3. catastrophic PERSON identity or drawing-medium drift across repeated appearances
4. obvious focal anatomy/contact failure that breaks the depicted action
5. food-state/action contradiction that changes the story or makes the eating sequence impossible
6. wrong core menu/entity or major meal-context substitution

### 6.2 Soft quality score
The following are normally score/repair observations, not automatic hard failure:
- a mildly repetitive camera
- slightly imperfect utensil placement
- background that is a little generic
- minor tableware preference
- small style variance above the publishable floor
- composition that could be more elegant
- non-critical cultural nuance

One isolated defect does not create a new permanent hard gate.
A new hard gate requires repeated publish-blocking evidence across episodes, or a true media-integrity/corruption class failure.

## 7. Runtime flow

`PLAN → BOARD → ASSEMBLY → FINAL → DONE`

### PLAN
- choose menu/moment
- map exactly six publishable beats
- define minimal food-state/action continuity
- draft cover title and lettering copy

No asset resolution stage.
No production-asset DAG.
No S01 identity-anchor gate.

### BOARD
- generate one text-free six-panel master board using the locked style/reference authority
- do internal hard-fail QC
- retry only when a hard FAIL occurs

### ASSEMBLY
- extract six cells
- fit to fixed 4:5 BODY pages
- construct COVER from accepted artwork; no dedicated stochastic cover render by default
- apply lettering / inner thought / speech as editable layers

### FINAL
- inspect complete COVER + six BODY carousel
- one user publish gate
- repair the minimum affected layer
- if only lettering/layout is wrong, never regenerate the board

### DONE
- export final carousel and record lightweight metrics

## 8. Reference and media integrity

Reference binaries remain valuable, but validation is not a per-run ritual.

Run byte/full-decode validation only when:
- a reference is newly added
- repository bytes change
- materialization source changes
- corruption is suspected

A previously validated unchanged reference does not require repeated media-integrity gating at every boot.

Rejected generated boards are not references.

## 9. Legacy demotion

The following are historical/debugging references and are NOT runtime production authority under V1:
- COMPOSITION_FIRST_HYBRID_FOOD
- reusable PERSON/FOOD BODY composition as the canonical visual path
- BODY4 Lane A/Lane B architecture comparison
- PERSON/FOOD foundation asset dependency DAG
- ASSET_GAP state machine
- S01 composed identity-anchor gate
- mandatory per-asset hash approval as a condition for ordinary BODY rendering
- full-frame exception logic built around asset composition
- calibration next_actions that dispatch FOOD foundation regeneration
- AutoPipeline child-pin parity as a creative/runtime boot gate

Existing approved/calibration files may remain in Git history or the working tree for provenance.
They must not override this spec.

Shared deterministic code may still be reused. Its version belongs in implementation receipts, not in the creative authority chain.

## 10. Runtime authority

Normal boot reads:
1. `CURRENT_STATE.md`
2. `JIPBAP_V1_SPEC.md`

Only when actual reference bytes must be dispatched/materialized:
3. `assets/REFERENCE_MANIFEST.md` or the specific reference registry entry

Do not recursively load legacy protocol/calibration documents during normal production.
