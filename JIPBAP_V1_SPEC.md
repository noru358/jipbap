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

### 1.3 Presentation-master-first assembly

master board PASS 후의 presentation 단계는 **quality-first design → editable reconstruction** 순서로 처리한다.

1. six-cell extraction
2. 4:5 page fit
3. distinct COVER hero fit
4. `PRESENTATION_MASTER_DRAFT`: 대사 / 내면독백 / SFX / 표지 타이틀까지 포함한 완성형 7장 visual draft를 먼저 설계
5. `FINAL_PUBLISH_GATE`: 사용자는 이 완성형 visual draft의 디자인을 승인
6. `EDITABLE_RECONSTRUCTION`: 승인된 visual draft를 원본 artwork bytes 위에 editable scene objects로 재구성
7. `PRESENTATION_PARITY_QC`: 승인 visual target과 ToonDesk/scene render의 시각적 동등성 검수
8. deterministic SVG / PNG / editable package export

핵심 dependency rule:
- **ToonDesk/editor primitive가 presentation 디자인을 선행 결정하지 않는다.**
- 먼저 가장 자연스럽고 완성도 높은 말풍선, 글씨, 행갈이, 위치, 크기, 강조, 표지 타이포를 설계한다.
- 그 다음 editor scene model이 그 디자인을 따라간다.
- 현재 editor가 승인된 디자인을 표현하지 못하면 디자인을 단순화하는 것이 아니라 editor capability를 확장하거나 scene 표현을 보강한다.
- shell의 bubble/font/placement 값은 승인된 presentation master가 없을 때의 **fallback/bootstrap default**일 뿐 aesthetic authority가 아니다.

Artwork는 stretch하지 않는다. 4:5 adaptation은 crop / safe inset / placement로 처리하되, BODY의 기본값은 페이지 전체를 artwork surface로 사용하는 full-art composition이다.
생성 보드가 nominal 2×3 equal-cell contract를 따르더라도 deterministic extraction은 512px 같은 이론적 등분 좌표를 가정하지 않는다. 실제 panel boundary를 검출/확정하여 crop metadata로 기록하고, 인접 패널 픽셀이 섞이지 않게 추출한다.

`PRESENTATION_MASTER_DRAFT`는 accepted BOARD/COVER의 **presentation design target**이다.
- artwork의 정체성/스토리 authority를 새로 만드는 이미지가 아니다.
- creative draft에서 artwork 픽셀이 미세하게 재해석되어 보이더라도 final editable reconstruction은 반드시 승인된 BOARD/COVER 원본 raster를 사용한다.
- presentation master가 소유하는 것은 bubble silhouette, tail feel, text placement, line break, typography character, title hierarchy, emphasis/decor rhythm 같은 presentation intent다.
- literal copy는 PLAN/approved copy가 authority이며, 이미지 모델의 오타나 자형 오류를 final text로 채택하지 않는다.

최종 editable authority는 여전히 `composition/*.layout.json`이다.
다만 각 final composition은 승인된 presentation master의 provenance/hash를 기록하고 그 target을 충실히 재현해야 한다.
Flattened PNG is a publish/export derivative only.

`PRESENTATION_PARITY_QC`:
- accepted BOARD/COVER artwork source identity: exact
- literal text: exact
- page count / page order: exact
- bubble silhouette family, tail direction/feel, line breaks, typography character, title hierarchy, relative placement: materially equivalent
- face/food/hand focal obstruction: no material regression
- antialiasing/font rasterization 차이처럼 의미 없는 pixel-level 차이는 허용
- tool-linked render가 승인 target보다 명백히 기계적/박스형/서식형으로 퇴행하면 FAIL
- parity FAIL은 BOARD 재생성 사유가 아니다. scene reconstruction 또는 editor/tool capability를 고친다.

Cover / lettering presentation defaults:

COVER title system — `COVER_TITLE_SYSTEM_V1`:
- default semantic fields are `episode_no`, `topic_phrase`, and `food_name`.
- default composed grammar is `EP.{episode_no} {topic_phrase}와 {food_name}`.
- the grammar is a series identity/default, not an episode-specific hardcode. The field values remain episode data.
- visually, `EP.{episode_no}` renders as a compact episode label while `{topic_phrase}와 {food_name}` renders as the dominant title; together they must read as the same composed title grammar.
- the automatic episode label is plain lettering by default: no surrounding speech bubble, pill, badge outline or decorative container unless an episode-specific design actually benefits from one.
- `topic_phrase` should be a short natural noun phrase that captures the episode situation rather than a full plot-summary sentence.
- `food_name` uses the canonical reader-facing menu name and may receive restrained emphasis such as accent color or underline.
- automatic COVER title layout uses the existing soft title region and focal-aware placement. It does not freeze exact x/y coordinates, left/right side, camera, hero crop, or line break.
- title may reflow across 1–3 lines. Reflow/reposition before shrinking to poor readability or obstructing face/food/hand focal regions.
- a separate menu tag remains an editor capability, but automatic production should not redundantly repeat the same `food_name` when the standardized title already carries it.
- typography-role styling is standardized; exact artwork staging remains fluid.

General COVER / lettering presentation defaults:
- COVER is a separate design surface and the automatic default is a distinct text-free COVER hero artwork, not reuse of a BODY cell.
- After BODY BOARD PASS, one separate COVER hero generation may occur using the same locked style delivery and approved episode intent. This does not add a user gate; it is the normal cover-art source step before deterministic lettering/composition.
- Reusing accepted BODY artwork for COVER is allowed only when the user explicitly prefers that reuse or when a distinct cover source is genuinely unavailable; silent BODY reuse is not the automatic default.
- COVER automatic layout is a full-canvas artwork layer with editable vector lettering/decoration over it; it is not a rigid header-frame + hero-frame split.
- COVER artwork provenance is explicit and sticky. Once automatic assembly selects the approved source raster and crop for the final-preview candidate, the scene records that source/crop as `cover_artwork_provenance`; later presentation repairs must not silently replace it with S01/S06/another BODY cell.
- Replacing COVER artwork is an explicit artwork-level override or a deliberate pre-final deterministic reselection, never an incidental consequence of shell/profile changes.
- Prefer one clear focal food/action image plus intentional negative space for the title. A soft title-safe region may guide automatic placement but does not crop the artwork into a separate lower hero box.
- automatic COVER placement scores title/menu/decor against declared `face_primary`, `food_primary`, and `hand_action` avoid regions. Reflow/reline/reposition lettering before covering a focal subject.
- Title hierarchy, line break, scale and placement must be composed together with the artwork; do not merely place a centered text block above an image.
- Korean display typography should feel compatible with a casual hand-drawn food comic: readable, friendly and visibly hand-drawn rather than office/document-like or mechanically typeset.
- BODY speech containers should default toward soft organic oval/pillow silhouettes with a restrained curved tail, not rigid rounded rectangles. Bubble geometry remains editable and may be horizontally flipped without mirroring the text.
- No single font family is a V1 creative lock. Each typography role may declare a preferred real font plus fallback chain. Runtime substitution is allowed only when the preferred font is unavailable, and the editor must surface the substitution rather than silently changing appearance.
- A presentation master may be a separate quality-first visual design artifact, but it is never an untracked lookalike. Each approved page target must be hash/provenance-bound to the editable reconstruction and checked by PRESENTATION_PARITY_QC.
- The handed-off editable package must reproduce the approved presentation intent without silently falling back to simpler editor defaults.
- Cover or BODY lettering defects are presentation-layer defects. Repair/reconstruct typography/layout or extend editor capability without regenerating accepted BOARD artwork.


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
│  ├─ COVER.png
│  ├─ S01.png
│  └─ ...
├─ presentation_master/
│  ├─ COVER.png
│  ├─ S01.png
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
- `artwork/*.png` contains accepted raster artwork extracted from the approved BOARD plus the approved distinct COVER hero.
- `presentation_master/*.png` contains the approved quality-first visual presentation targets. These are design-reference artifacts, not editable state and not authority for literal text spelling.
- `composition/*.layout.json` is the final editable presentation authority and shared scene model; it must carry presentation-target provenance and pass parity against the approved presentation master.
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
Speech-bubble tail geometry is also explicit scene data, not a fixed renderer triangle. A bubble may preserve:
- tail enabled/style
- tip x/y
- attachment side + normalized attachment position
- base width
- curvature/softness
The editor should expose direct-manipulation handles for tail tip and attachment point plus width/curve controls. Legacy `tail_to` remains readable for backward compatibility but new saves should emit the richer tail geometry.
Automatic speech-tail placement should use a short pointer to the speaker-facing edge rather than drawing a long pointer across a face/food focal region. The automatic default should target roughly <= 180 px from the attachment point when practical; this is a soft layout default, not an editor limit. Manual tail dragging may exceed it.
The future editor may expose related objects as a convenience group without flattening them.
SFX such as `톡` is a text/SFX object, not part of the generated artwork raster.

Shared renderer/editor contract:
- changing dialogue, narration, inner thought, title or SFX mutates layout JSON only;
- dragging/resizing/rotating editable objects mutates scene geometry only;
- routine Chat production changes artwork framing through crop metadata and never stretches the accepted raster;
- the interactive editor may explicitly unlock an artwork frame and move / resize / rotate the frame; this mutates scene geometry only and is recorded as a `CUSTOM_OVERRIDE`, not as a new scene format;
- deterministic rerender updates SVG/PNG without BOARD regeneration;
- accepted artwork bytes remain byte-identical during ordinary presentation editing; explicit image replacement is an artwork-level override and must not be confused with approved BOARD provenance;
- every accepted artwork page may carry one `artwork_provenance` reference. BODY provenance points to the existing BOARD-extraction metadata + box index; COVER provenance points to its approved source. The final FIT/crop transform remains owned by the artwork object's `crop` metadata rather than duplicated into a second manifest;
- editor-originated `manual_overrides` are property-level metadata, not locks. Automatic layout/reconstruction preserves those properties by default while leaving unmodified properties editable and eligible for automatic updates;
- a line-break-only edit is tracked separately from literal-copy editing. If upstream literal copy later changes, do not silently reuse stale line breaks or shrink text; keep the new copy, preserve unrelated manual geometry, and surface a reflow/manual-attention issue;
- preview and PNG export share the same scene renderer. SVG is a deterministic derivative of the same geometry/text model, but external SVG rasterizers may differ in font metrics/antialiasing and this is not claimed as pixel identity;
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
- crop edits and frame transforms mutate scene metadata only unless the user explicitly replaces the artwork source;
- BODY extraction uses the existing `JIPBAP_BOARD_EXTRACTION_V1` record as the single owner of source hash + actual panel boxes. A scene references that record and box index; it does not create a duplicate crop manifest.
- the final artwork object's `crop` metadata is the single owner of 4:5 FIT pan/scale/anchor. Downstream save/reopen/export reuses it.
- final-crop review should be performed on the 4:5 page with optional `avoid_regions` visible so face/hand/food focal subjects can be checked after FIT.

Placement freedom:
- COVER and BODY both use full-art composition by default: the accepted raster occupies the complete 4:5 canvas and lettering is layered over it as independent vector/scene objects.
- COVER may use a soft title-safe hint to encourage negative space; this is not a separate artwork frame.
- BODY has no mandatory lower meta band and no structural top-art/bottom-copy split.
- speech, inner thought, narration and SFX are all freeform lettering overlays. Their semantic roles remain distinct even when their geometry is fluid.
- automatic placement is focal-aware: prefer naturally empty areas and avoid covering primary face, food or hand-action regions when reasonable.
- a page may carry optional `placement_guides` / `avoid_regions` metadata such as `face_primary`, `food_primary`, `hand_action`; these are soft placement hints, not new BOARD gates.
- the interactive editor should be able to visualize these soft guides on demand and include them as snapping targets while never exporting them into the flattened publish image.
- if no safe area exists, shorten/reline copy, reduce container footprint, or use a restrained translucent/light container before obscuring the focal action.
- explicit human/editor repositioning remains allowed and is a normal scene edit; it becomes `CUSTOM_OVERRIDE` only when it changes project-profile structural defaults such as artwork-frame geometry/page structure, not merely because a lettering object moved.
- unnecessary coverage of focal food/face is a presentation quality defect; obvious obstruction that makes the focal action unreadable must be repaired before publish.
- automatic copy overflow on untouched generated layout may be repaired by reline/reposition or copy revision, never by squeezing artwork.
- if the user has manually changed position, line breaks, tail geometry or typography, automation preserves those marked properties by default. A changed literal copy that no longer fits is surfaced as `layout_attention` instead of silently shrinking type or erasing the user's placement.
- reapplying automatic placement is an explicit editor action that names the affected scope before clearing the relevant manual override; it does not globally reset unrelated edits.

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
- microtexture is simplified into grouped shapes / line cues rather than exhaustive grain-by-grain or fiber-by-fiber rendering
- highlights and gloss are restrained and broad; avoid dense specular highlights that make sauce, yolk, rice or meat read like food photography
- no advertisement-style sauce splash, excessive steam, lacquer gloss or photographic depth-of-field
- macro / extreme-close food shots do not authorize a realism jump; they must preserve the same drawing-medium abstraction as wider PERSON+FOOD shots
- food may carry slightly more surface detail than PERSON, but both must still look drawn in the same medium
- abstraction/detail density should remain reasonably consistent across the six BODY panels so one food close-up does not look as if it came from a different renderer or illustrator

### 2.3 Cross-domain coherence
Hard style principle:
- PERSON and FOOD must look like one illustrator / one medium made them.
- A flat webtoon PERSON beside near-photographic FOOD is not acceptable.
- realism may vary slightly by subject, but line/color/light abstraction must stay coherent.

### 2.4 Background
Frozen policy:
- omit background and decorative assets unless they materially explain the eating moment.
- when needed, use only the minimum contextual shapes/objects required to identify place, motion, or action.
- do not add generic lamps, plants, utensils, shelves, extra diners, street furniture or room decor merely to make a frame feel "finished".
- no ornamental cozy-room filling by default.
- background must not become the visual focal point over food/action.
- a situational establishing panel may use more context than a bite/detail panel, but contextual density should fall away once the story function is already readable.

### 2.5 Text
- no meaning-bearing text is baked into generated BODY master-board cells or generated COVER source raster.
- no generated speech bubbles, captions, labels, logos or panel numbers are accepted as source-art authority.
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

Frozen copy principles:
- `speech`, `inner_thought`, `narration`, `sfx` have distinct functions; none is a mandatory per-panel slot.
- speech carries a reaction/request/relationship toward someone; inner thought carries immediate private reaction or small desire; narration adds time/context absent from the image; SFX carries sound or nonverbal rhythm.
- use conversational Korean that can plausibly be spoken or thought by a real person. Community/thread-like rhythm is allowed when natural, but no global meme/`~함`/`~임` persona is imposed.
- sensory wording is kept when it adds concrete temperature, texture, aroma, flavor direction, viscosity/coating, sound or aftertaste that the image cannot fully show.
- do not narrate an obvious visible action merely because a text slot exists.
- do not enforce a character count, one-sentence-per-panel rule, or one-text-object-per-panel rule.
- read copy aloud as a naturalness check.
- do not force `잘 먹었다`, a moral, emotional closure, punchline, conflict or reversal.

Input policy:
- a food name alone is sufficient to start planning.
- when the user provides situation, remembered sensation, actual words, unexpected detail or small choice, use them.
- these are optional enrichment, never a required questionnaire.
- preserve the distinction between user-given experience/copy and AI-filled connective assumptions; do not present AI-filled details as user memory.
- when story direction is genuinely undecided, offer at most two materially different directions and recommend one. If the user already provided a story/structure, follow it rather than generating alternatives.

Exact wording, dialect intensity, line count and whether a panel is silent remain fluid.
## 6. Storyboard, text-space and continuity

Storyboard planning co-designs image and lettering while keeping the generated BOARD text-free.
Per scene, reuse existing plan fields where they already carry the meaning and add only missing information:
- what becomes new in the scene
- person action and current food state
- actual copy element(s), speaker and role (`speech` / `inner_thought` / `narration` / `sfx`)
- camera distance/relation and visual focus
- approximate copy-space hint, without freezing final x/y
- protected face/hand/food regions that lettering should avoid
- reading order when multiple text elements exist

`copy_space_hint`, `placement_guides` and `avoid_regions` are soft planning/presentation metadata. They must not become a universal top text band or a BOARD generation requirement.
Where practical, review a small 4:5 storyboard view before image generation. If visual storyboard generation is impractical in Chat mode, a scene-by-scene placement description is sufficient; no dedicated storyboard application is required.

Continuity uses the minimum state needed to prevent impossible images:
- current food state
- visible action
- immediately required previous state
- next visible consequence

Do not rebuild a full action/asset dependency DAG.
For eating interactions:
- spoon/chopstick/hand/food/mouth geometry must make physical sense at the visible moment.
- flavor / mouthfeel / aftertaste copy must not occur before the depicted bite has actually entered the mouth, unless a prior panel already established ingestion.
- bridge actions may occur between panels, but before/after states must be compatible.
- cultural meal details follow the current episode context; no global table-setting pose is hardcoded.

Shot scale, camera, expression, number of silent panels and amount of background remain story-driven. Do not impose quotas.
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
- standardized COVER title grammar / role hierarchy that needs deterministic reflow or wording compression
- speech typography/container that feels too mechanically typeset or boxy relative to the artwork
- a sensory line whose timing is slightly ahead of the depicted ingestion state and can be repaired by copy/layout/shot selection without changing the whole story
- FOOD that is slightly too glossy, micro-detailed or advertisement-like while remaining otherwise publishable
- panel-to-panel FOOD abstraction/detail density that is less consistent than ideal
- slightly imperfect utensil placement
- background that is a little generic or unnecessarily dense while still readable
- minor tableware preference
- small style variance above the publishable floor
- composition that could be more elegant
- non-critical cultural nuance

One isolated defect does not create a new permanent hard gate.
A new hard gate requires repeated publish-blocking evidence across episodes, or a true media-integrity/corruption class failure.

## 8. Runtime / approval flow

Normal production is **one ChatGPT conversation with multiple user turns**.
Do not try to force PLAN → ART → FINAL into one assistant response.

Canonical production flow:

`BOOT → PLAN → STORYBOARD_USER_GATE + CARRIER_BIND → INITIAL_ART_BUNDLE → ART_BUNDLE_USER_GATE → EXTRACT/FIT → PRESENTATION_MASTER_DRAFT → FINAL_PUBLISH_GATE → EDITABLE_RECONSTRUCTION → PRESENTATION_PARITY_QC → DONE`

`SIX_PANEL_BOARD_FIRST` remains the V1 BODY architecture. `INITIAL_ART_BUNDLE` is the image-authoring phase that produces the BODY master board and the separate COVER hero together before the artwork approval gate.

### 8.1 BOOT + PLAN turn
At the beginning of a production chat:
- do not require image attachment yet;
- restore latest jipbap `main`;
- read `CURRENT_STATE.md` and this spec;
- if a new episode is required, create the six-beat PLAN;
- if an episode is active, restore its saved PLAN/exact next action;
- present storyboard, copy draft, expression/camera intent, overall visual rhythm and continuity for user review;
- stop at `STORYBOARD_USER_GATE`.

The storyboard gate remains permanent because it prevents image work from proceeding on an unwanted story/copy/cut plan.

When the user approves the storyboard:
- treat that same turn as the normal carrier-binding handoff;
- prefer repository-direct validated `JIPBAP_STYLE_CARRIER_V1` and `JIPBAP_FOOD_STYLE_CARRIER_V1` bytes;
- only when repository-direct binding is unavailable, the user supplies the exact already-approved PERSON + FOOD carriers once as `SESSION_ONLY` runtime carriers;
- the carrier attachment does not create a new reference, story, episode or state reset.

### 8.2 INITIAL_ART_BUNDLE — same image-authoring phase
After storyboard approval and carrier binding, create the initial artwork bundle before asking for another approval.

The bundle contains two separate source artifacts:
1. **BODY master board** — exactly one text-free 2×3 board containing S01..S06.
2. **COVER hero** — exactly one independently authored, text-free cover-source artwork.

They are created in the same initial image-authoring phase, but they are **not one combined raster**:
- COVER does not consume a BODY cell;
- COVER is not a crop/reuse of a BODY cell;
- COVER has its own source/provenance;
- BODY still obeys the frozen six-cell board contract.

COVER is defined by role, not by a hardcoded relation to specific BODY slots:
- it should function as the episode's cover/hero image and represent the episode's food/emotion/situation;
- camera, framing, pose, expression, food placement and title-safe negative space remain story-driven;
- do not encode rules such as “different from S04/S06” or any other slot-specific prohibition;
- similarity to a BODY composition is a soft quality consideration unless it causes an actual publish-blocking failure or source/provenance confusion.

Run the existing V1 hard-fail logic on the BODY board. Apply the same publish-blocking standard to COVER for unintended generated text, wrong core menu/entity, catastrophic PERSON/style drift, or focal anatomy/contact failure.
Do not create a new permanent gate from ordinary cover-composition preference.

If only one bundle component fails or is rejected, regenerate/repair only that component unless the defect proves the shared style delivery itself is invalid.

### 8.3 ART_BUNDLE_USER_GATE
Show the BODY master board and the distinct COVER hero together for user review.

This is the normal artwork approval gate.
The user may approve, reject, or request changes to BODY, COVER, or both.

On approval:
- lock the exact accepted BODY board source bytes/provenance;
- lock the exact accepted COVER source bytes/provenance;
- do not stochastically redraw either source for downstream crop, layout, lettering, typography or editor work;
- presentation-only feedback never authorizes BODY/COVER regeneration.

Normal V1 user gates are therefore:
1. storyboard approval;
2. initial artwork bundle approval;
3. final publish approval.

This artwork gate replaces the old split “BOARD approval now / COVER later” operating pattern. It is not a slot template and does not freeze creative staging.

### 8.4 EXTRACT/FIT + PRESENTATION MASTER + EDITABLE RECONSTRUCTION
After `ART_BUNDLE_USER_GATE` approval:
- detect/confirm the six actual BODY panel boundaries and extract six cells as accepted raster artwork; never assume equal pixel split coordinates merely from board dimensions;
- fit the accepted COVER and BODY artwork into full-canvas 4:5 pages without stretching;
- preserve the exact accepted artwork sources for the presentation stage.

Then create `PRESENTATION_MASTER_DRAFT`:
- compose the complete 7-page carousel with final copy, natural bubble shapes/tails, line breaks, typography character, cover title treatment, SFX and local spacing;
- optimize for the comic's visual quality first, **without constraining the draft to the current ToonDesk primitive/default set**;
- preserve the semantic distinction between speech / thought / narration / SFX, but do not force them into one box style or one fixed font template;
- do not let meaning-bearing generated text become literal authority: the approved copy strings remain authoritative and are corrected during editable reconstruction;
- inspect the complete carousel as a visual design object.

At `FINAL_PUBLISH_GATE`:
- show the quality-first `PRESENTATION_MASTER_DRAFT`;
- user approval locks the presentation intent for all seven pages;
- store page-level target provenance/hash.

After approval, do `EDITABLE_RECONSTRUCTION`:
- use the exact accepted BODY-board extractions and exact accepted COVER raster, not stochastic reinterpretations;
- reconstruct bubble / text / SFX / title / decoration as editable scene objects;
- inherit geometry/style from the approved presentation master rather than re-applying generic shell defaults;
- shell presets may fill unspecified details only.

Then run `PRESENTATION_PARITY_QC`:
- compare the editor-rendered 7 pages against the approved presentation targets;
- if materially equivalent, persist composition/SVG/PNG/package and finish without another routine user gate;
- if the editor render visibly degrades the approved design, repair the scene or extend ToonDesk capability and rerun parity;
- only return to the user when a material visual mismatch cannot be resolved without changing approved intent/artwork.

The final editable layout package remains presentation authority after reconstruction.
The approved presentation master is its bound visual target, not an unrelated preview.
A lettering/layout-only defect never authorizes stochastic artwork regeneration.

### 8.5 When to start a new chat / approved-art continuity
A new chat is **not** required between PLAN and `INITIAL_ART_BUNDLE` or between `ART_BUNDLE_USER_GATE` and FINAL.

Start a new chat only when:
- the conversation approaches a product/context limit;
- actual image-runtime contamination is observed;
- repeated outputs stay locked to a stale semantic template despite corrected instructions;
- artifact/approval identity becomes uncertain.

Before handoff, save current stage and exact next action in `CURRENT_STATE.md`.

If resumed before artwork-bundle approval and image generation is still needed, bind the approved renderer carriers once in the new chat.

If resumed after artwork-bundle approval:
- prefer materialized episode artwork bytes for the exact approved BODY and COVER;
- if those exact bytes are not materialized but are available as user/session artifacts, re-supply the exact approved artwork as a `SESSION_ONLY` production-art carrier;
- a path, hash, generation id or prose description without the approved pixels is not permission to redraw them;
- **never regenerate an approved BODY or COVER merely because a new chat cannot access its bytes**;
- if exact approved bytes are unavailable, fail closed and request/recover those exact bytes rather than creating a replacement.

If the resumed stage is EXTRACT/FIT, PRESENTATION_MASTER_DRAFT, EDITABLE_RECONSTRUCTION or PRESENTATION_PARITY_QC, renderer style carriers are not required unless the user explicitly reopens stochastic artwork generation.

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
Production image generation uses renderer-safe runtime projections rather than raw creative references.

PERSON projection:
- `JIPBAP_STYLE_CARRIER_V1`

FOOD projection:
- `JIPBAP_FOOD_STYLE_CARRIER_V1`
- status until calibrated: REQUIRED_BEFORE_NEXT_PRODUCTION_BOARD

Neither carrier is a new creative style authority. They are runtime-safe projections of the locked creative authorities.

`JIPBAP_STYLE_CARRIER_V1` required properties:
- exactly one person;
- no food;
- no tableware or meal scene;
- no text, logo, caption, number or speech bubble;
- no comic panel/grid structure;
- no story sequence;
- plain or transparent/minimal background;
- enough face/upper-body information to express the desired face construction, eye grammar, hair silhouette, line, fill, shading and texture.

`JIPBAP_FOOD_STYLE_CARRIER_V1` required properties:
- no person, hand or character;
- no text, logo, panel/grid or story sequence;
- no environment/background staging;
- use a tightly cropped, semantically neutral illustrated food-style study whose purpose is line/fill/highlight/microtexture abstraction rather than a recognizable episode menu;
- avoid a complete branded/plated dish composition when possible, so menu/entity semantics are not copied into production;
- demonstrate restrained broad highlights, grouped texture, drawn edges and the same medium abstraction as PERSON.

Both carriers have style-delivery scope only. Neither owns menu, ingredient identity, tableware, camera, staging, story or copy.

### 9.3 One-time carrier creation isolation
Creating or replacing either renderer carrier is a **separate calibration task** from episode production.

During carrier creation:
- raw `PERSON_STYLE_REF_1` / `TARGET_LOOK_BOARD_REF_1` may be attached so the renderer can derive the intended look;
- user approval is required before a new projection becomes `JIPBAP_STYLE_CARRIER_V1` or `JIPBAP_FOOD_STYLE_CARRIER_V1`;
- the approved carrier should be stored/registered as the runtime carrier.

Do **not** generate a production episode board later in that same raw-reference calibration chat.
Start episode production in a clean chat and attach only the approved renderer-safe carrier.

This separation prevents raw-reference semantic content from sharing the same image-runtime context as production BOARD generation.

### 9.4 Production attachment timing
For normal episode production after both projections are USER_LOCKED:
1. start the chat with no image attachment and reach storyboard approval;
2. in the storyboard-approval turn, bind `JIPBAP_STYLE_CARRIER_V1` and `JIPBAP_FOOD_STYLE_CARRIER_V1` once, preferring repository-direct validated bytes and using identical `SESSION_ONLY` carriers only when direct binding is unavailable;
3. generate `INITIAL_ART_BUNDLE`: one text-free BODY 2×3 master board plus one separate text-free COVER hero in the same initial image-authoring phase;
4. present both at `ART_BUNDLE_USER_GATE`;
5. after approval, continue deterministic extraction/FIT → presentation master → final publish gate without stochastic BODY/COVER regeneration.

The attachment does not reset episode/state/story and does not create a new reference.
It is a `SESSION_ONLY` pixel carrier for the already locked runtime style projection.

COVER role is episode-level and fluid. Do not turn current-episode observations about any specific BODY slot into permanent COVER rules.

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
