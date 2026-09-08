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
4. editable composition construction
5. SVG / PNG export
를 deterministic post-processing으로 처리한다.

Artwork는 stretch하지 않는다. 4:5 adaptation은 crop, safe margin, padding, placement 중 고정 template 규칙으로 처리한다.

The authoritative presentation artifact is **not the flattened PNG**.
After BOARD acceptance, presentation authority is the editable composition package described below.
Flattened PNG is a publish/export derivative only.

Cover / lettering presentation defaults:
- COVER is a separate design surface, not a default reuse of S01. Accepted BODY artwork may be reused only when it reads strongly as a cover composition.
- Prefer one clear focal food/action image plus intentional negative space for the title.
- Title hierarchy, line break, scale and placement must be composed together with the artwork; do not merely place a centered text block above an image.
- Korean display typography should feel compatible with a casual hand-drawn food comic: readable, friendly and slightly organic rather than office/document-like.
- No single font family is a V1 creative lock. Font choice is an implementation/presentation decision and may change if the current runtime lacks the preferred font.
- Cover or BODY lettering defects are deterministic presentation defects. Repair typography/layout without regenerating accepted BOARD artwork.


### 1.4 Editable composition package

BOARD 이후의 기본 산출 단위는 `EDITABLE_COMPOSITION_PACKAGE_V1`이다.

Logical package:

```text
episode/
├─ artwork/
│  ├─ S01.png
│  ├─ S02.png
│  └─ ...
├─ composition/
│  ├─ COVER.layout.json
│  ├─ S01.layout.json
│  ├─ S02.layout.json
│  └─ ...
├─ editable/
│  ├─ COVER.svg
│  ├─ S01.svg
│  ├─ S02.svg
│  └─ ...
└─ export/
   ├─ COVER.png
   ├─ S01.png
   ├─ S02.png
   └─ ...
```

Authority and derivation:
- `artwork/*.png` contains accepted raster artwork extracted from the approved BOARD.
- `composition/*.layout.json` is the deterministic presentation authority for editable placement/content.
- `editable/*.svg` is a generated editable/interchange representation derived from layout JSON + artwork.
- `export/*.png` is a flattened publish derivative only.
- No font binary is embedded or treated as repository authority; layout records reference font family/style intent and runtime substitution is allowed when needed.

Each layout JSON stores independent objects rather than pre-flattened pixels.
Minimum object classes:
- `artwork`
- `bubble`
- `text`
- `sfx`
- optional decorative vector shape

For editable text/SFX objects, preserve at least:
- stable object id
- object type / semantic role
- literal string
- x / y
- width / height or wrapping box
- font family intent
- font size / weight
- alignment
- rotation
- z-index

Bubble geometry is separate from the text string so either may move or resize independently.
SFX such as `톡` is a text/SFX object, not part of the generated artwork raster.

External-editor contract:
- changing dialogue, narration, inner thought, title or SFX mutates layout JSON only;
- dragging/resizing/rotating text, bubbles or SFX mutates geometry only;
- deterministic rerender updates SVG/PNG without BOARD regeneration;
- accepted artwork must remain byte-identical unless the user explicitly requests an artwork-level change.

This package structure is an output-interface rule, not a new user gate and not a new BOARD hard-fail class.


### 1.5 Frozen presentation shell

V1 presentation geometry is fixed so episodes can be edited externally without per-episode frame drift.

Template id:
- `JIPBAP_PRESENTATION_SHELL_V1`

Canvas:
- all pages: 1080 × 1350 (4:5)

BODY artwork frame:
- x = 40
- y = 175
- width = 1000
- height = 1000
- accepted square BOARD cell is fit 1:1 into this frame
- artwork is never stretched or aspect-distorted
- BODY artwork frame does not move to make room for copy

BODY presentation rule:
- the artwork frame is fixed across S01–S06;
- text, bubble, thought-box and SFX objects may move within the page;
- if copy does not fit cleanly, shorten/reline/reposition the copy object rather than shifting or squeezing artwork;
- no visible page numbers or internal episode markers in publish output.

COVER geometry:
- title safe region: x = 60..1020, y = 50..300
- hero artwork frame: x = 60, y = 330, width = 960, height = 960
- accepted square artwork is fit 1:1 without distortion
- default cover grammar is one small menu tag + one dominant title + one hero artwork
- subtitle/deck is optional, not a default requirement
- title and hero must remain visually separate; do not squeeze hero artwork to make extra text fit.

Lettering semantics:
- `speech`: white speech bubble with a visible tail toward the speaker; dark outline.
- `inner_thought`: tail-free warm off-white thought box with a lighter/muted outline.
- `sfx`: independent text/SFX object with no bubble; may be moved/rotated/scaled.
- literal strings and geometry remain editable in layout JSON.
- a semantic role must not be conveyed only by the words themselves; speech, thought and SFX should be visually distinguishable before reading.

This shell freezes presentation geometry, not story staging. Camera, pose, crop content inside the accepted BOARD cell, expression and object placement in the generated art remain fluid.

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
- cover title, speech, narration, inner thought and SFX are editable deterministic composition objects.
- final flattened PNG is not text authority; the literal string and geometry live in the page layout JSON.

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

Soft staging objective — this is guidance, not a gate or slot template:
- the six BODY panels should have a readable visual rhythm rather than accidentally collapsing into the same camera/framing repeatedly;
- vary shot scale, camera relation, amount of person shown and action emphasis when the story benefits from it;
- food detail, hand action, face reaction and wider context may trade prominence across panels;
- expressions may be modestly amplified beyond neutral realism when that improves appetite/emotional readability, while staying inside the approved drawing language;
- do not satisfy variety by mechanically forcing one of each shot type or one prescribed expression per slot.

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

## 5. Voice / copy boundary

Frozen copy grammar:
- use short, conversational Korean that can plausibly sound like a real person, Korean community post or thread reaction rather than polished script prose
- fragments, dropped subjects, brief exclamations and reaction-first wording are allowed when natural
- do not force slang, memes or trendy expressions merely to simulate community speech
- when copy adds food information, prefer one concrete sensory observation from the immediate bite: aroma, heat, texture, seasoning, moisture, aftertaste or the effect of combining foods
- describe why the bite works rather than relying on generic praise such as simply saying it is delicious
- copy should add what the image cannot fully show — mouthfeel, smell, temperature, flavor transition, aftertaste or the impulse to take another bite — rather than narrating an obvious hand motion
- on mobile, prefer one short reaction and at most one concrete sensory observation per beat; if copy starts competing with the artwork, compress the copy rather than enlarging the lettering area or moving the fixed artwork frame
- silent BODY panels are allowed when the image carries the beat
- do not force a `잘 먹었다`, lesson, punchline or emotional conclusion
- inner thought, speech and narration are separate editable layers
- food/appetite remains the subject; character backstory does not expand unless it directly strengthens the meal moment

Exact wording, dialect intensity, line count and whether a panel is silent remain fluid.

## 6. Physical and semantic continuity

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

## 7. QC: hard fail vs soft score

### 7.1 Hard FAIL only
Reject/retry a master board only for publish-blocking defects:
1. not exactly six extractable cells, or severe panel bleed/geometry failure
2. unintended generated text
3. catastrophic PERSON identity or drawing-medium drift across repeated appearances
4. obvious focal anatomy/contact failure that breaks the depicted action
5. food-state/action contradiction that changes the story or makes the eating sequence impossible
6. wrong core menu/entity or major meal-context substitution

### 7.2 Soft quality score
The following are normally score/repair observations, not automatic hard failure:
- mildly repetitive camera or framing
- a board whose overall staging/emotional range feels flatter than ideal while remaining publishable
- a reaction that could be modestly more expressive
- cover title/font/placement that could be better integrated with accepted artwork
- slightly imperfect utensil placement
- background that is a little generic
- minor tableware preference
- small style variance above the publishable floor
- composition that could be more elegant
- non-critical cultural nuance

One isolated defect does not create a new permanent hard gate.
A new hard gate requires repeated publish-blocking evidence across episodes, or a true media-integrity/corruption class failure.

## 8. Runtime / approval flow

Normal production is **one ChatGPT conversation with multiple user turns**.
Do not try to force PLAN → BOARD → FINAL into one assistant response.

Canonical production flow:

`BOOT → PLAN → STORYBOARD_USER_GATE → BOARD → [TEMP_STYLE_GATE] → ASSEMBLY → FINAL_PUBLISH_GATE → DONE`

### 8.1 BOOT + PLAN turn
At the beginning of a production chat:
- do not require image attachment yet;
- restore latest jipbap `main`;
- read `CURRENT_STATE.md` and this spec;
- if a new episode is required, create the six-beat PLAN;
- if an episode is active, restore its saved PLAN/exact next action;
- present storyboard, copy draft, expression/camera intent, overall visual rhythm and continuity for user review;
- stop at `STORYBOARD_USER_GATE`.

The storyboard gate is permanent because it prevents expensive image work from proceeding on an unwanted story/copy/cut plan.

### 8.2 BOARD turn — same conversation
After the user approves the storyboard, continue in the **same chat**.

If a renderer-safe carrier is already USER_LOCKED:
- the user attaches only `JIPBAP_STYLE_CARRIER_V1` once in the approval/BOARD message;
- the attachment is a SESSION_ONLY runtime carrier, not new creative authority;
- generate the text-free 2×3 master board;
- apply V1 hard-fail QC.

Do not ask the user to reattach the carrier again within the same chat.

### 8.3 Temporary style gate
While `JIPBAP_STYLE_CARRIER_V1` is still being calibrated, show the generated master board once for user style/board approval before ASSEMBLY.

This is a temporary calibration checkpoint, not a permanent production gate.

After the carrier is USER_LOCKED and repeated production evidence shows stable style delivery:
- remove/disable the routine BOARD user gate;
- internal QC may pass BOARD directly to ASSEMBLY.

Normal steady-state user gates are therefore:
1. storyboard approval;
2. final publish approval.

### 8.4 ASSEMBLY + FINAL
After BOARD PASS:
- extract six cells as accepted raster artwork;
- fit six 4:5 BODY pages;
- assemble COVER from accepted artwork;
- create/update per-page layout JSON with independent artwork / bubble / text / SFX objects;
- derive editable SVG and flattened PNG from the layout package;
- inspect the complete seven-page carousel, including cover hierarchy/font/line-break/negative-space fit and BODY lettering placement;
- present the completed carousel at `FINAL_PUBLISH_GATE`.

The final publish preview may be PNG, but the editable layout package remains the presentation authority.
A lettering/layout-only defect mutates layout JSON and rerenders deterministic derivatives; it never authorizes stochastic BOARD regeneration.

### 8.5 When to start a new chat
A new chat is **not** required between PLAN and BOARD or between BOARD and FINAL.

Start a new chat only when:
- the conversation approaches a product/context limit;
- actual image-runtime contamination is observed;
- repeated outputs stay locked to a stale semantic template despite corrected instructions;
- artifact/approval identity becomes uncertain.

Before handoff, save current stage and exact next action in `CURRENT_STATE.md`.

If the resumed stage requires image generation, attach `JIPBAP_STYLE_CARRIER_V1` once in the new chat.
If the resumed stage is deterministic ASSEMBLY/FINAL only, no style carrier is required.

## 9. Creative references vs renderer carrier

### 9.1 Creative authority
The canonical style authorities remain:
- `PERSON_STYLE_REF_1`
- `TARGET_LOOK_BOARD_REF_1`

They define what the desired style looks like.
They do **not** automatically have to be direct image-generation inputs.

Observed calibration evidence showed that content-rich or multi-subject references can leak non-authoritative semantics such as subject count, menu, text, panel structure or story context into generation.

Therefore raw creative references are **not normal production renderer attachments**.

### 9.2 Renderer-safe projection
Production image generation should use a separately approved runtime projection:

`JIPBAP_STYLE_CARRIER_V1`

This carrier is not a third creative style authority.
It is a runtime-safe projection of the locked creative authorities.

Required carrier properties:
- exactly one person;
- no food;
- no tableware or meal scene;
- no text, logo, caption, number or speech bubble;
- no comic panel/grid structure;
- no story sequence;
- plain or transparent/minimal background;
- enough face/upper-body information to express the desired face construction, eye grammar, hair silhouette, line, fill, shading and texture;
- no visual element whose count or narrative role should be copied into an episode.

Its authority scope is style delivery only.

### 9.3 One-time carrier creation isolation
Creating or replacing `JIPBAP_STYLE_CARRIER_V1` is a **separate calibration task** from episode production.

During carrier creation:
- raw `PERSON_STYLE_REF_1` / `TARGET_LOOK_BOARD_REF_1` may be attached so the renderer can derive the intended look;
- user approval is required before the result becomes `JIPBAP_STYLE_CARRIER_V1`;
- the approved carrier should be stored/registered as the runtime carrier.

Do **not** generate a production episode board later in that same raw-reference calibration chat.
Start episode production in a clean chat and attach only the approved renderer-safe carrier.

This separation prevents raw-reference semantic content from sharing the same image-runtime context as production BOARD generation.

### 9.4 Production attachment timing
For normal episode production:
1. start the chat with no image attachment and reach storyboard approval;
2. in the same chat, the user's storyboard-approval message attaches `JIPBAP_STYLE_CARRIER_V1` once;
3. continue BOARD → ASSEMBLY → FINAL in that conversation.

The attachment does not reset episode/state/story and does not create a new reference.
It is a SESSION_ONLY pixel carrier for the already locked runtime style projection.

### 9.5 Reference/media integrity
Reference or carrier byte validation is not a per-run ritual.

Run byte/full-decode validation only when:
- a reference/carrier is newly added;
- repository bytes change;
- materialization source changes;
- corruption is suspected.

A previously validated unchanged carrier does not need repeated integrity gating at every boot.
Rejected generated boards are not references or carrier candidates.

### 9.6 Controlled-experiment finding
A user-run clean control with:
- no attached reference image;
- no prior production-image context;
- the same one-person / kimchi-pancake / text-free / exact 2×3 content contract

successfully produced a structurally correct six-panel board.

Interpretation:
- `SIX_PANEL_BOARD_FIRST` container/content obeyability is supported;
- style delivery remains the unresolved layer;
- do not respond by restoring asset-composition/state-machine complexity.

## 10. Legacy demotion

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

## 11. Runtime authority

Normal boot reads:
1. `CURRENT_STATE.md`
2. `JIPBAP_V1_SPEC.md`

Only when actual reference bytes must be dispatched/materialized:
3. `assets/REFERENCE_MANIFEST.md` or the specific reference registry entry

Do not recursively load legacy protocol/calibration documents during normal production.
