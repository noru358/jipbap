# REFERENCE_MANIFEST

Updated: 2026-09-06

This manifest records the authoritative binary references required by the current manual-validation experiment.

## STYLE_REF_001

- intended repository path: assets/references/STYLE_REF_001.jpg
- role: project visual/style authority supplied explicitly by the user
- original dimensions: 864 × 1536
- SHA-256: 792be650dc2aae9a2ca5ee6d2fadd51054475d9171eaf5b427fb5192893ec972
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED

## Episode 001 S01 temporary anchor

- intended repository path: episodes/001/anchors/S01_TEMP_ANCHOR.png
- role: episode-local continuity anchor only
- user verdict: TEMPORARY_PASS
- project style-lock authority: NO
- original dimensions: 1122 × 1402
- SHA-256: c5769b8a789b75d80764798368f029d68479fe93ff36178c1460c73ae96227fd
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED

## Episode 002 S01 approved anchor

- intended repository path: episodes/002/anchors/S01_APPROVED_ANCHOR.png
- role: Episode 002 continuity anchor
- user verdict: PASS
- project style-lock authority: NO
- original dimensions: 1122 × 1402
- SHA-256: cec9a1be2077772369e89098a9553d67b9ba028b6c5c5448f9ac8f44d1814050
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted here as if it were repository materialization.

Before every reference-conditioned render execution:
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. if available, verify its SHA-256 when the environment exposes the bytes;
3. if unavailable, FAIL-CLOSED and do not substitute memory, prose descriptions, paths, or hashes for the image.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

Any renderer/environment that depends only on this Git repository MUST block reference-conditioned production until the required binary exists at the declared path and its SHA-256 matches this manifest.
