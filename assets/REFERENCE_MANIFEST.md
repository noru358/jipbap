# REFERENCE_MANIFEST

> Media integrity is executable authority. PERSON_STYLE_REF_1 is currently materialized and
> validated by clean-checkout CI. Machine-readable byte and decoded-pixel identities live in
> `assets/reference_registry.json`; historical recovery evidence lives in `INTEGRITY_STATE.json`.


Updated: 2026-09-08

This manifest records project-level visual reference identities and integrity metadata.
Episode-local anchors belong only to an active episode package and must not survive an episode reset in this project-level manifest.

## PERSON style calibration candidates

The user explicitly supplied two PERSON-style candidates and requested that both be run through the same calibration path before final selection.

### PERSON_STYLE_REF_1

- user label: 레퍼 스타일 1
- role: PERSON_STYLE_AUTHORITY_CANDIDATE
- coverage_scope: PERSON only
- allowed_influence: face construction, eye grammar, linework, flat/local color, hair simplification, expression grammar, person visual density
- excluded_influence: FOOD style pixels, BACKGROUND/LOCATION design, camera/composition, cover/lettering
- dimensions: 1448 × 483
- current repository byte SHA-256: 6b954d0a3e0f86b135c36527082f7253ba0d2d3c79e6e23141651218cd77e278
- decoded RGBA pixel SHA-256: a8e7eca4f2d5396d1a4b62d7a27351ead7817056b6451632b14e0c78db880e0d
- original user-supplied source byte SHA-256: 6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614
- repository path: assets/references/PERSON_STYLE_REF_1.png
- repository blob SHA: 68bbfc1d0edebfa4c1c4ac2601c92914c9f49fa4
- repository binary status: MATERIALIZED_VALIDATED
- prior corrupt repository SHA-256: 0f7494746f5cfd9d42b5133e9ffaae7cf63dff96f5ee97773bf114f867b0ccaf
- selection status: SELECTED_USER_LOCKED
- recovery note: GitHub-uploaded PNG has different container bytes but identical decoded RGBA pixels to the recovered original; current repository bytes are the executable authority.

### TARGET_LOOK_BOARD_REF_1

- user label: PERSON_STYLE_REF_1 보조 핵심 레퍼 / target-look anchor
- role: PERSON_TARGET_LOOK_AUXILIARY
- source style authority: PERSON_STYLE_REF_1 (unchanged primary authority)
- coverage_scope: auxiliary target-look guidance only
- allowed_influence: face construction, eye grammar, hair silhouette, line/texture/color treatment, and the shared person+food screen language
- excluded_influence: text/copy, panel layout, shot/cut structure, menu/food-state semantics, camera/composition, and meal-context entity selection
- dimensions: 770 × 1024
- current repository byte SHA-256: 3eb4565cb80f901417ea730970dfb8a731614cce58a239b599445e54018838e6
- original session-carrier SHA-256: acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b
- original session-carrier decoded RGBA pixel SHA-256: dc8761e133a2c28000852bac38bfd96706bee54182f5bf7884ebfae8959cd516
- repository path: assets/references/TARGET_LOOK_BOARD_REF_1.png
- repository blob SHA: 5180d5b9784bcabce4828c5a31625ad28ede4aa9
- repository binary status: MATERIALIZED_VALIDATED_FULL_DECODE
- lock status: USER_LOCKED_AUXILIARY
- validation note: clean-checkout CI reported only the provisional byte-hash mismatch, confirming PNG signature, full Pillow decode, and 770×1024 dimensions; the registry was rebound to the actual repository SHA-256 above.
- authority rule: this board narrows the desired target look; it does **not** replace or supersede PERSON_STYLE_REF_1 and its visible captions/panel grid/menu are non-authoritative incidental content.

### PERSON_STYLE_REF_2

- user label: 레퍼 스타일 2
- role: PERSON_STYLE_AUTHORITY_CANDIDATE
- coverage_scope: PERSON only
- allowed_influence: face construction, eye grammar, linework, flat/local color, hair simplification, expression grammar, person visual density
- excluded_influence: FOOD style pixels, BACKGROUND/LOCATION design, camera/composition, cover/lettering
- dimensions: 1122 × 1402
- SHA-256: 6f7643f1eef0f1a5641fb0af60518e097d3caf926267c5c4557a3c156a7922d4
- repository binary status: RUNTIME_ONLY_NOT_MATERIALIZED
- selection status: NOT_SELECTED_CALIBRATION_EVIDENCE_ONLY
- domain firewall note: the visible food/table/kitchen content in this reference is incidental and MUST NOT become FOOD, BACKGROUND, meal-layout, camera or composition authority.


## Renderer-safe production carrier

### JIPBAP_STYLE_CARRIER_V1

- role: RENDERER_SAFE_STYLE_CARRIER
- creative authority relationship: runtime-safe projection only; does not replace PERSON_STYLE_REF_1 or TARGET_LOOK_BOARD_REF_1
- content contract: exactly one person; no food; no text; no panel/grid; no story sequence; transparent/minimal background
- dimensions: 583 × 622
- approved session-source byte SHA-256: 43e791e8ebb1389fb7c469786f76fe118bcb96182d7c06e080d9088fb4057a80
- user lock status: USER_LOCKED
- repository registry: assets/reference_registry.json
- intended repository path: assets/references/JIPBAP_STYLE_CARRIER_V1.png
- repository binary status: NOT_MATERIALIZED_IN_REPOSITORY_THIS_RUN
- current runtime binding: SESSION_ONLY_FALLBACK using the exact user-supplied approved carrier pixels
- production rule: future image-generation sessions should prefer validated repository bytes once materialized; until then, attach the same approved carrier once as SESSION_ONLY fallback.
- authority scope: face construction, eye grammar, hair silhouette, line/color/texture style delivery only; no menu, staging, camera, layout, story or copy authority.

## Selected calibration evidence

### PERSON_CONTEXT_SEATED_STYLE1_SELECTED

- role: PERSON_STYLE_SELECTION_EVIDENCE
- source reference: PERSON_STYLE_REF_1
- repository path: calibration/person_style/PERSON_CONTEXT_SEATED_STYLE1_SELECTED.png
- dimensions: 770 × 1024
- SHA-256: acf18912952e977ba5c1c52f97f0b5b38759a680ee8bf4ff04b65621abfb103b
- repository blob SHA: 98976d7b28ff061b95c216652df59e95073bbe42
- status: RETIRED_CORRUPT_OPTIONAL_EVIDENCE
- selection decision retained in CALIBRATION_STATE.json
- confirmed corrupt repository SHA-256: 35b63461b6e15f258ae61455e89f288b12acc9d51e86dc6894b6788037c2fdae
- note: User clarified that this S01–S04 sheet was generated from PERSON_STYLE_REF_1 and selected Style 1 as the final PERSON drawing-language direction.
- production rule: selection evidence and style reference only; this collage is not a production pose asset and must not enter the production registry.

## Comparison rule

Both references must receive the **same semantic PERSON asset contract** and the same BODY4 S01 composition target.
Do not improve one candidate with extra content, pose, camera or food information unavailable to the other.

Evaluation dimensions:
- fidelity to the supplied PERSON drawing language;
- absence of generic GPT/anime beautification drift;
- anatomy/pose stability;
- ability to remain coherent beside the independently authored food asset;
- identity/style stability when reused as the anchor for later interaction assets.

Selection is complete: the user selected PERSON_STYLE_REF_1 after reviewing calibration evidence. PERSON_STYLE_REF_2 remains non-production calibration evidence only.

## Active episode-local anchors

NONE.

The retired pre-reset E001/S01 anchors are not current authority and are recoverable from Git history only.
Do not use them as continuity, edit, style or repair sources.

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted as if it were repository materialization.

Before every reference-conditioned render execution:
0. run the repository media-integrity gate and require PASS for every bound reference;
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. verify its current repository byte SHA-256 and decoded-pixel identity against the machine registry;
3. bind the actual image media through the parent media-input contract / renderer media-input surface;
4. if unavailable or mismatched, FAIL-CLOSED for that candidate.

Do not substitute chat memory, prose descriptions, paths without bytes, hashes without bytes, or another candidate's pixels.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

If a later session does not contain the candidate image bytes and they have not been materialized in Git, re-supply the actual reference before continuing PERSON-conditioned authoring.

Historical style-drift lessons have already been promoted into VISUAL_SYSTEM and are not duplicated here.
