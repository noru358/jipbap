# REFERENCE_MANIFEST

> Integrity notice: user selection decisions are preserved, but the currently materialized
> PERSON_STYLE_REF_1 and selected calibration-evidence binaries are not executable authority
> until they pass `python -m pipeline.cli validate`. Machine-readable byte identity lives in
> `assets/reference_registry.json`; recovery state lives in `INTEGRITY_STATE.json`.


Updated: 2026-09-07

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
- SHA-256: 6fce9fd274965b9a7a8825079c8862d08af82b74fc9c1b30d170d8dd75b01614
- repository path: assets/references/PERSON_STYLE_REF_1.png
- repository blob SHA: 369aeed50e607319a62371eb79658daa636f12c3
- repository binary status: MATERIALIZED_BINARY_INVALIDATED
- confirmed corrupt repository SHA-256: 0f7494746f5cfd9d42b5133e9ffaae7cf63dff96f5ee97773bf114f867b0ccaf
- selection status: SELECTED_USER_LOCKED_DECISION_BINARY_INVALIDATED

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
2. verify its SHA-256 against the candidate identity above when bytes are accessible;
3. bind the actual image media through the parent media-input contract / renderer media-input surface;
4. if unavailable or mismatched, FAIL-CLOSED for that candidate.

Do not substitute chat memory, prose descriptions, paths without bytes, hashes without bytes, or another candidate's pixels.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

If a later session does not contain the candidate image bytes and they have not been materialized in Git, re-supply the actual reference before continuing PERSON-conditioned authoring.

Historical style-drift lessons have already been promoted into VISUAL_SYSTEM and are not duplicated here.
