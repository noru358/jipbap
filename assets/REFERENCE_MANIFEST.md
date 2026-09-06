# REFERENCE_MANIFEST

Updated: 2026-09-07

This manifest records project-level authoritative binary references. Episode-local anchors are registered inside the active episode.

## STYLE_REF_001

- intended repository path: assets/references/STYLE_REF_001.jpg
- role: project visual/style authority supplied explicitly by the user for fresh E001
- original dimensions: 1448 × 1086
- SHA-256: fd763500b9c34e24d85805eb2c74b5b37a5361b82b3749644254c93922da6422
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED
- current approved runtime source: user-supplied image in the E001 session

This entry supersedes the retired pre-reset STYLE_REF_001 binary metadata.

## Active episode-local anchors

Episode 001:
- E001_S01_APPROVED
- role: CONTINUITY_ANCHOR + DINER_01 episode-local identity anchor
- SHA-256: aa277caf908100d277a878072189d6b0829258c464823a28b83465aec5b54c4c
- dimensions: 1122 × 1402
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED
- edit-target status for S02+: false

Detailed episode asset state: episodes/001/ASSET_MANIFEST.md

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted here as if it were repository materialization.

Before every reference-conditioned render execution:
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. if available, verify its SHA-256 when the environment exposes the bytes;
3. if unavailable, FAIL-CLOSED and do not substitute memory, prose descriptions, paths, or hashes for the image.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

Any renderer/environment that depends only on this Git repository MUST block reference-conditioned production until each required binary exists at the declared path and its SHA-256 matches this manifest.
