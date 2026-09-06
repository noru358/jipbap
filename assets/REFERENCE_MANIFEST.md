# REFERENCE_MANIFEST

Updated: 2026-09-07

This manifest records project-level authoritative binary references.
Episode-local anchors belong only to an active episode package and must not survive an episode reset in this project-level manifest.

## STYLE_REF_001

- intended repository path: assets/references/STYLE_REF_001.jpg
- role: PERSON_STYLE_AUTHORITY supplied explicitly by the user
- coverage_scope: PERSON only
- allowed_influence: face construction, eye grammar, linework, flat color, hair simplification, person visual density
- excluded_influence: FOOD style pixels, BACKGROUND/LOCATION design, camera/composition, cover/lettering
- original dimensions: 1448 × 1086
- SHA-256: fd763500b9c34e24d85805eb2c74b5b37a5361b82b3749644254c93922da6422
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED
- current runtime media availability: NOT_VERIFIED

This metadata identifies the intended authority but does not substitute for the image bytes.

## Active episode-local anchors

NONE.

The retired pre-reset E001/S01 anchors are not current authority and are recoverable from Git history only.
Do not use them as continuity, edit, style or repair sources for the BODY4 calibration pilot or a future fresh 001.

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted here as if it were repository materialization.

Before every reference-conditioned render execution:
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. verify its SHA-256 against this manifest when the environment exposes the bytes;
3. bind the actual media through the parent media-input contract;
4. if unavailable or hash-mismatched, FAIL-CLOSED.

Do not substitute:
- chat memory;
- prose descriptions;
- repository paths without bytes;
- hashes without bytes;
- retired episode anchors.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

Any renderer/environment that depends only on this Git repository MUST block PERSON reference-conditioned authoring until STYLE_REF_001 exists at the declared path with matching SHA-256, or the same verified bytes are explicitly supplied through the current runtime media binding.

Historical style-drift lessons have already been promoted into VISUAL_SYSTEM and are not duplicated here.
