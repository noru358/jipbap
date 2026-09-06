# REFERENCE_MANIFEST

Updated: 2026-09-07

This manifest records project-level authoritative binary references. Episode-local anchors are registered only inside a newly approved active episode and are not carried across the clean reset.

## STYLE_REF_001

- intended repository path: assets/references/STYLE_REF_001.jpg
- role: project visual/style authority supplied explicitly by the user
- original dimensions: 864 × 1536
- SHA-256: 792be650dc2aae9a2ca5ee6d2fadd51054475d9171eaf5b427fb5192893ec972
- repository binary status: BINARY_REQUIRED_NOT_YET_MATERIALIZED

## Episode-local anchor reset

No episode-local anchor is active.

Previous 001/002 anchors are retired and must not be restored or supplied as continuity media for the fresh 001.

## Runtime binding rule

Session/chat availability is runtime state and MUST NOT be persisted here as if it were repository materialization.

Before every reference-conditioned render execution:
1. verify that the actual required image binary is available to the renderer in the current execution context;
2. if available, verify its SHA-256 when the environment exposes the bytes;
3. if unavailable, FAIL-CLOSED and do not substitute memory, prose descriptions, paths, or hashes for the image.

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

Any renderer/environment that depends only on this Git repository MUST block reference-conditioned production until the required binary exists at the declared path and its SHA-256 matches this manifest.
