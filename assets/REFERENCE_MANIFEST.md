# REFERENCE_MANIFEST

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
- dimensions: 1448 × 1086
- SHA-256: 82ad0c13db1e0d3baab1ff3340c8654b54415cadcb92da76ee924da738970d51
- repository binary status: RUNTIME_ONLY_NOT_MATERIALIZED
- selection status: IN_TEST

### PERSON_STYLE_REF_2

- user label: 레퍼 스타일 2
- role: PERSON_STYLE_AUTHORITY_CANDIDATE
- coverage_scope: PERSON only
- allowed_influence: face construction, eye grammar, linework, flat/local color, hair simplification, expression grammar, person visual density
- excluded_influence: FOOD style pixels, BACKGROUND/LOCATION design, camera/composition, cover/lettering
- dimensions: 1122 × 1402
- SHA-256: 6f7643f1eef0f1a5641fb0af60518e097d3caf926267c5c4557a3c156a7922d4
- repository binary status: RUNTIME_ONLY_NOT_MATERIALIZED
- selection status: IN_TEST
- domain firewall note: the visible food/table/kitchen content in this reference is incidental and MUST NOT become FOOD, BACKGROUND, meal-layout, camera or composition authority.

## Comparison rule

Both references must receive the **same semantic PERSON asset contract** and the same BODY4 S01 composition target.
Do not improve one candidate with extra content, pose, camera or food information unavailable to the other.

Evaluation dimensions:
- fidelity to the supplied PERSON drawing language;
- absence of generic GPT/anime beautification drift;
- anatomy/pose stability;
- ability to remain coherent beside the independently authored food asset;
- identity/style stability when reused as the anchor for later interaction assets.

No candidate becomes final PERSON style authority until the user selects it after side-by-side calibration evidence.

## Active episode-local anchors

NONE.

The retired pre-reset E001/S01 anchors are not current authority and are recoverable from Git history only.
Do not use them as continuity, edit, style or repair sources.

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted as if it were repository materialization.

Before every reference-conditioned render execution:
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. verify its SHA-256 against the candidate identity above when bytes are accessible;
3. bind the actual image media through the parent media-input contract / renderer media-input surface;
4. if unavailable or mismatched, FAIL-CLOSED for that candidate.

Do not substitute chat memory, prose descriptions, paths without bytes, hashes without bytes, or another candidate's pixels.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

If a later session does not contain the candidate image bytes and they have not been materialized in Git, re-supply the actual reference before continuing PERSON-conditioned authoring.

Historical style-drift lessons have already been promoted into VISUAL_SYSTEM and are not duplicated here.
