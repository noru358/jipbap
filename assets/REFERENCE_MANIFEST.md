# REFERENCE_MANIFEST

Updated: 2026-09-06

This manifest records the authoritative binary references required by the current manual-validation experiment.

## STYLE_REF_001

- intended repository path: `assets/references/STYLE_REF_001.jpg`
- role: project visual/style authority supplied explicitly by the user
- original dimensions: 864 × 1536
- SHA-256: `792be650dc2aae9a2ca5ee6d2fadd51054475d9171eaf5b427fb5192893ec972`
- repository binary status: `BINARY_REQUIRED_NOT_YET_MATERIALIZED`

## Episode 001 S01 temporary anchor

- intended repository path: `episodes/001/anchors/S01_TEMP_ANCHOR.png`
- role: episode-local continuity anchor only
- user verdict: `TEMPORARY_PASS`
- project style-lock authority: `NO`
- original dimensions: 1122 × 1402
- SHA-256: `c5769b8a789b75d80764798368f029d68479fe93ff36178c1460c73ae96227fd`
- repository binary status: `BINARY_REQUIRED_NOT_YET_MATERIALIZED`

## Fail-closed rule

A document path or hash is not evidence that the renderer received the image bytes.

Any renderer/environment that depends only on this Git repository MUST block reference-conditioned production until the required binary exists at the declared path and its SHA-256 matches this manifest.

In the current ChatGPT session the originally supplied reference/temporary anchor may be available as chat media, but that session-local availability must never be recorded as repository materialization.
