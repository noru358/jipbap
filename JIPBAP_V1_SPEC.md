# JIPBAP_V1_SPEC

Updated: 2026-09-09
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
- This 7-page structure is the automatic JIPBAP production default. A generic editor may expose page add/delete/duplicate/type-change capabilities; an explicit deviation is a `CUSTOM_OVERRIDE`, not the normal JIPBAP V1 production path.

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
4. editable scene/composition construction
5. deterministic SVG / PNG export
를 deterministic post-processing으로 처리한다.

Artwork는 stretch하지 않는다. 4:5 adaptation은 crop / safe inset / placement로 처리하되, BODY의 기본값은 페이지 전체를 artwork surface로 사용하는 full-art composition이다.
생성 보드가 nominal 2×3 equal-cell contract를 따르더라도 deterministic extraction은 512px 같은 이론적 등분 좌표를 가정하지 않는다. 실제 panel boundary를 검출/확정하여 crop metadata로 기록하고, 인접 패널 픽셀이 섞이지 않게 추출한다.

The authoritative presentation artifact is **not the flattened PNG**.
After BOARD acceptance, presentation authority is the editable composition package described below.
Flattened PNG is a publish/export derivative only.

Cover / lettering presentation defaults:
- COVER is a separate design surface, not a default reuse of S01. Accepted BODY artwork may be reused only when it reads strongly as a cover composition.
- COVER automatic layout is a full-canvas artwork layer with editable vector lettering/decoration over it; it is not a rigid header-frame + hero-frame split.
- Prefer one clear focal food/action image plus intentional negative space for the title. A soft title-safe region may guide automatic placement but does not crop the artwork into a separate lower hero box.
- Title hierarchy, line break, scale and placement must be composed together with the artwork; do not merely place a centered text block above an image.
- Korean display typography should feel compatible with a casual hand-drawn food comic: readable, friendly and slightly organic rather than office/document-like.
- No single font family is a V1 creative lock. Each typography role may declare a preferred real font plus fallback chain. Runtime substitution is allowed only when the preferred font is unavailable, and the editor must surface the substitution rather than silently changing appearance.
- The final publish preview and the handed-off editable package must resolve the same scene and font choices. A separately generated lookalike preview is never the approval artifact.
- Cover or BODY lettering defects are deterministic presentation defects. Repair typography/layout without regenerating accepted BOARD artwork.


### 1.4 Editable composition package / editor scene model

BOARD 이후의 기본 산출 단위는 `EDITABLE_COMPOSITION_PACKAGE_V1`이다.
Its `composition/*.layout.json` files are also the shared **editor scene model** for both current Chat-mode rendering and a future first-party Canva-like interactive editor.

This does **not** mean using Canva as a production dependency.
No Canva, PPTX, PDF or other external-editor file format is canonical authority.
The product goal is to reproduce the useful direct-manipulation UX internally: select an object, drag, resize, rotate, edit text, adjust crop, change stacking order, and group/ungroup where appropriate.

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
- `composition/*.layout.json` is the deterministic presentation authority and shared scene model.
- current Chat mode consumes the same scene model through a deterministic renderer and still produces final PNG without any interactive editor.
- a future API/editor surface consumes the same scene model for direct manipulation, then rerenders deterministic derivatives.
- `editable/*.svg` remains a generated interchange/debug derivative; it is not the human-editing authority.
- `export/*.png` is a flattened publish derivative only.
- No font binary is embedded or treated as repository authority; layout records preserve semantic family/style intent plus optional preferred real font and fallback chain.
- Runtime font substitution is allowed when needed, but the editor/renderer must expose the resolved family and warn when the preferred family is unavailable. Silent substitution that changes the approved look is not acceptable for final export.

Each layout JSON stores independent objects rather than pre-flattened pixels.
Minimum object classes:
- `artwork`
- `bubble`
- `text`
- `sfx`
- optional decorative vector shape

Common scene-object fields should support, where applicable:
- stable object id
- object type / semantic role
- x / y
- width / height or wrapping box
- rotation
- z-index
- visible
- locked
- optional group id / parent group
- optional crop position / crop scale for artwork

Editable text/SFX objects additionally preserve:
- literal string
- font family/style role intent
- optional preferred real font family
- optional fallback family chain
- resolved runtime family when an export/preview receipt is recorded
- font size / weight
- alignment

Bubble geometry remains separate from the text string at the data level so either may be edited independently.
The future editor may expose related objects as a convenience group without flattening them.
SFX such as `톡` is a text/SFX object, not part of the generated artwork raster.

Shared renderer/editor contract:
- changing dialogue, narration, inner thought, title or SFX mutates layout JSON only;
- dragging/resizing/rotating editable objects mutates scene geometry only;
- routine Chat production changes artwork framing through crop metadata and never stretches the accepted raster;
- the interactive editor may explicitly unlock an artwork frame and move / resize / rotate the frame; this mutates scene geometry only and is recorded as a `CUSTOM_OVERRIDE`, not as a new scene format;
- deterministic rerender updates SVG/PNG without BOARD regeneration;
- accepted artwork bytes remain byte-identical during ordinary presentation editing; explicit image replacement is an artwork-level override and must not be confused with approved BOARD provenance;
- the interactive editor must remain optional: absence of the future API/editor must not block or alter the current Chat-mode production path.

### 1.4.1 Frozen editor-facing layer contract

The V1 editor scene model is now frozen as `EDITOR_SCENE_MODEL_V1`.

All COVER and BODY pages share the same four top-level layers, in this order:
1. `background`
2. `artwork`
3. `lettering`
4. `overlay`

The scene graph is metadata over a flat `objects[]` list. Objects remain flat for current Chat renderer compatibility; `groups[]` supplies parent/child semantics for the future direct-manipulation editor.

Top-level defaults:
- `background`: visible and locked.
- `artwork`: visible; frame transform locked; crop content editable.
- `lettering`: visible and editable.
- `overlay`: visible/editable but empty by default; optional non-story decorative vectors only.
- meaning-bearing text belongs in `lettering`.

Stable z-bands:
- background: 0
- artwork: 1..9
- lettering: 10..99
- overlay: 100..199

COVER hierarchy:
- `cover.background`
- `cover.artwork`
- `cover.lettering`
  - `cover.menu_tag`
  - `cover.title`
- `cover.overlay`

The menu-tag and title groups are stable editor groups. Their child object count may vary for styling/line treatment while group identity stays fixed. Subtitle/deck remains optional and hidden by default.

BODY hierarchy for each page `SNN`:
- `sNN.background`
- `sNN.artwork`
- `sNN.lettering`
  - zero or more `sNN.speech.NN`
  - zero or more `sNN.thought.NN`
  - zero or more `sNN.narration.NN`
  - zero or more `sNN.sfx.NN`
- `sNN.overlay`

The top-level BODY hierarchy is fixed; semantic lettering instance count remains fluid. Speech/thought groups contain separate container geometry and text objects: group move moves both, while data stays independently editable/ungroupable.

Lock defaults:
- page background: locked by default.
- artwork frame geometry: locked by default in automatic JIPBAP production.
- artwork crop metadata: editable through crop mode.
- lettering and overlay objects: unlocked by default.
- the editor engine retains frame move / resize / rotation capability; an explicit user unlock enables those transforms and marks the page/profile state as `CUSTOM_OVERRIDE`.
- an explicit user image replacement is allowed by the editor engine but is an artwork-level override, not ordinary BOARD-preserving presentation editing.
- lock or geometry overrides never authorize BOARD regeneration.

Artwork frame/crop interaction:
- the active JIPBAP presentation shell owns the automatic first-pass artwork x/y/width/height;
- routine Chat-mode assembly instantiates that geometry and leaves the frame locked;
- crop mode may pan and uniformly scale the accepted raster inside the frame;
- default crop: centered, scale 1.0, zero offset;
- stretching is disabled by default; crop pan/scale cannot expose empty frame area;
- an explicit interactive-editor unlock may transform the frame without changing the underlying scene format;
- crop edits and frame transforms mutate scene metadata only unless the user explicitly replaces the artwork source.

Placement freedom:
- COVER and BODY both use full-art composition by default: the accepted raster occupies the complete 4:5 canvas and lettering is layered over it as independent vector/scene objects.
- COVER may use a soft title-safe hint to encourage negative space; this is not a separate artwork frame.
- BODY has no mandatory lower meta band and no structural top-art/bottom-copy split.
- speech, inner thought, narration and SFX are all freeform lettering overlays. Their semantic roles remain distinct even when their geometry is fluid.
- automatic placement is focal-aware: prefer naturally empty areas and avoid covering primary face, food or hand-action regions when reasonable.
- a page may carry optional `placement_guides` / `avoid_regions` metadata such as `face_primary`, `food_primary`, `hand_action`; these are soft placement hints, not new BOARD gates.
- if no safe area exists, shorten/reline copy, reduce container footprint, or use a restrained translucent/light container before obscuring the focal action.
- explicit human/editor repositioning remains allowed and is a normal scene edit; it becomes `CUSTOM_OVERRIDE` only when it changes project-profile structural defaults such as artwork-frame geometry/page structure, not merely because a lettering object moved.
- unnecessary coverage of focal food/face is a presentation quality defect; obvious obstruction that makes the focal action unreadable must be repaired before publish.
- automatic copy overflow is repaired by reline/shorten/reposition/font-size adjustment within the role preset, never by squeezing artwork.

Typography role presets are implementation defaults, not font-family locks:
- `cover_menu_tag`: nominal 30 px, 26..34, bold.
- `cover_title`: nominal 92 px, 72..112, bold display.
- `body_speech`: nominal 42 px, 36..46, bold.
- `body_thought`: nominal 38 px, 34..42, regular.
- `body_narration`: nominal 36 px, 32..40, medium; text-only by default.
- `body_sfx`: nominal 64 px, 44..84, bold hand-drawn display.

Runtime font substitution remains allowed; semantic typography role is authority and no font binary is.
Automatic production should also persist `preferred_family` / `fallback_families` when a role has a selected real font. ToonDesk or any renderer must expose a missing-preferred-font warning and use the same resolved family for preview and export.

Scene object requirements:
- page-level `scene_model: EDITOR_SCENE_MODEL_V1`;
- page type `cover` or `body`;
- stable `groups[]` metadata;
- each render object carries `group_id`, `visible`, `locked`, and `rotation` where applicable;
- artwork carries explicit crop metadata.

This layer contract is a presentation/interface rule, not a new user gate and not a new BOARD hard-fail class. Malformed scene data that cannot render deterministically is an artifact-integrity error, never a reason to regenerate accepted BOARD artwork.


### 1.5 Presentation shell / project profile

The scene model is the reusable editor data model; the JIPBAP presentation shell is a **project default profile**, not the editor engine's capability ceiling.

Versioning:
- `JIPBAP_PRESENTATION_SHELL_V1` remains frozen for episodes already completed with it, including V1_E001 / V1_E002.
- new automatic JIPBAP episodes use `JIPBAP_PRESENTATION_SHELL_V2`.
- V2 had no completed episode before the 2026-09-09 full-art correction; the failed V1_E003 test package is non-canonical. Therefore V2 is corrected in place instead of creating unnecessary V3 version churn.
- changing the default shell does not mutate completed episodes.

V2 template:
- `templates/JIPBAP_PRESENTATION_SHELL_V2.json`

Canvas default:
- 1080 × 1350 (4:5)

COVER V2 default:
- artwork frame: full canvas x=0, y=0, width=1080, height=1350
- soft title-safe hint: x=48, y=36, width=984, height≈330; this guides negative-space composition only and does not partition the artwork
- default grammar: one full-canvas artwork + one small menu tag + one dominant title; optional decorative vector accents
- subtitle/deck remains optional
- title/menu/decor are independent editable vector/scene objects above artwork
- automatic assembly does not squeeze/stretch artwork to make copy fit

BODY V2 default:
- artwork frame: full canvas x=0, y=0, width=1080, height=1350
- no mandatory lower meta region and no fixed top-art/bottom-copy split
- speech / inner thought / narration / SFX are independent freeform overlays above artwork
- automatic placement uses soft safe insets plus optional focal/avoid metadata rather than a fixed band
- automatic Chat-mode assembly starts the full-canvas artwork frame locked and never stretches the raster

Default-versus-override rule:
- normal Chat production instantiates the V2 defaults consistently across episodes;
- the generic editor retains page add/delete/duplicate, page-type change, frame move/resize/rotation, crop, text edit, group and z-order capabilities;
- explicit user unlock or structural edit may deviate from the JIPBAP defaults and is recorded as `CUSTOM_OVERRIDE`;
- a custom override is not scene corruption and does not create a new canonical file format;
- profile deviation alone is not a BOARD hard fail, does not create a new user gate, and never authorizes stochastic BOARD regeneration;
- if the user wants to return to automatic JIPBAP defaults, the profile can be reapplied deterministically.

Lettering semantics:
- `speech`: white speech bubble with a visible tail toward the speaker; dark outline.
- `inner_thought`: tail-free warm off-white thought treatment, free text, or restrained translucent/light container depending on local artwork.
- `narration`: compact freeform caption/text; no mandatory meta band.
- `sfx`: independent text/SFX object; may be moved/rotated/scaled.
- literal strings and geometry remain editable in layout JSON.
- container style and placement must preserve the focal food/action/face rather than enforcing a page-wide template.

This shell freezes the **automatic first-pass defaults**, not human editor freedom and not story staging. Camera, pose, crop content inside the accepted BOARD cell, expression and generated composition remain fluid.

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
- on mobile, prefer one short reaction and at most one concrete sensory observation per beat; if copy starts competing with the artwork, compress/reposition the copy or reduce its container footprint rather than sacrificing the focal artwork
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
- detect/confirm the six actual panel boundaries and extract six cells as accepted raster artwork; never assume equal pixel split coordinates merely from board dimensions;
- fit the extracted artwork into full-canvas 4:5 BODY scenes without stretching;
- assemble COVER as full-canvas artwork plus independent editable title/menu/decor objects;
- create/update per-page layout JSON with independent artwork / bubble / text / SFX objects and optional focal/avoid placement metadata;
- resolve preferred/fallback fonts and record any substitution warning;
- derive editable SVG and flattened PNG from that exact layout package;
- inspect the complete seven-page carousel, including panel-edge cleanliness, cover hierarchy/font/line-break/negative-space fit, focal obstruction and BODY lettering placement;
- present **the PNG derivatives rendered from the same composition package that will be handed off** at `FINAL_PUBLISH_GATE`.

The final publish preview may be PNG, but the editable layout package remains the presentation authority.
A separately generated or re-imagined preview is not a valid approval proxy for a different handoff package.
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
