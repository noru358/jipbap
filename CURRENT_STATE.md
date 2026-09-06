# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Production state — fresh E001 active

Execution authorization: **ACTIVE_BLOCKED_RENDER_CONTEXT_UNSAFE**

Active episode: **001**
Next episode number: 002

Approved preproduction authority:
- episodes/001/PREPRODUCTION.md
- episodes/001/SUBJECT_LOCK.md
- episodes/001/SHOT_CONTRACTS.md

Render state authority:
- episodes/001/render_state.json
- episodes/001/ASSET_MANIFEST.md

## Current render state

- BODY S01: **APPROVED_LOCKED**
- S01 user approval: PASS
- S01 role: CONTINUITY_ANCHOR + DINER_01 episode-local identity anchor
- render cursor: **S02**
- next user gate: **RASTER_SET**
- cover source route: BODY_REUSE
- cover status: NOT_STARTED
- sequence QC: NOT_RUN
- lettering: NOT_STARTED

Hard invariant:
S01 must not be regenerated or edited unless the user explicitly withdraws approval or explicitly orders S01 reproduction.

## Active blocker — RENDER_CONTEXT_UNSAFE

The current conversation contains the full approved E001 storyboard and future-shot descriptions.
The available image-generation path in this chat cannot be proven to receive only an isolated current-shot capsule.

Under PRODUCTION_PROTOCOL section 3, S02+ rendering is therefore fail-closed in this render context.

This is a context reset, not an episode reset.
E001, S01 approval, identity lock and render cursor remain valid.

## Reference binding state

Project style authority for fresh E001:
- STYLE_REF_001
- sha256: fd763500b9c34e24d85805eb2c74b5b37a5361b82b3749644254c93922da6422
- repository binary: NOT_YET_MATERIALIZED

Approved S01:
- E001_S01_APPROVED
- sha256: aa277caf908100d277a878072189d6b0829258c464823a28b83465aec5b54c4c
- repository binary: NOT_YET_MATERIALIZED

Before S02 render, actual bytes for both required media must be bound in the clean render context.
A path/hash/prose description alone is insufficient.

## Exact next action

Start a **new clean session** and:

1. restore AutoPipeline + jipbap HEADs;
2. read this CURRENT_STATE and episodes/001/render_state.json;
3. do **not** re-plan E001 and do **not** regenerate S01;
4. bind the actual STYLE_REF_001 image bytes and approved E001_S01_APPROVED image bytes;
5. compile the S02 current-shot-only capsule from episodes/001/SHOT_CONTRACTS.md;
6. verify render cursor == S02 and S01 remains APPROVED_LOCKED;
7. render S02 only;
8. after internal PASS, advance S03 → S04 → S05 with current-shot-only capsules and per-shot QC;
9. run whole-sequence coverage/state/geometry QC;
10. present the complete text-free BODY raster set at the RASTER_SET user gate.

If either required image binary cannot be bound in the new session, stop and request/recover that exact media instead of substituting memory.
