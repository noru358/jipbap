# CURRENT_STATE

Updated: 2026-09-07
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Production state — E001 retrospective / revision required

Execution authorization: **STRUCTURE_HARDENED_TEMPLATE_CALIBRATION_NEXT**

Active episode: **001 (evaluation run; not COMPLETE)**
Next production episode: UNRESOLVED until template calibration

## E001 disposition
- BODY S01–S05: prior raster-set gate PASS preserved as historical approval evidence
- final carousel candidate: **REVISION_REQUIRED / NOT APPROVED FOR COMPLETE**
- publication status: NOT_APPROVED
- do not automatically repair or publish E001
- E001 outputs remain evaluation evidence unless the user explicitly reopens/rebuilds the episode

Authority:
- CALIBRATION_STATE.json
- calibration/COMPOSITION_CANDIDATES.md
- CONTENT_SYSTEM.md
- VOICE_SYSTEM.md
- VISUAL_SYSTEM.md
- PRODUCTION_PROTOCOL.md
- assets/REFERENCE_MANIFEST.md
- episodes/001/RETROSPECTIVE.md
- episodes/001/render_state.json

## Structural changes now canonical

1. PROXY_EATER is the core audience promise.
2. BODY planning includes appetite/sensory beat, appetite-value gate and temporal-distinguishability.
3. Copy uses concrete sensory payload and a salivation gate.
4. STYLE_REF_001 is PERSON-only authority; S01 must pass person-style fidelity preflight.
5. Background uses NONE / LOCAL / FULL exposure scopes; full-room continuity is only locked when actually needed.
6. Cover and lettering have no approved visual template yet; E001 test composition is not a template lock.
7. A structural rule change must be committed and verified before any dependent render.
8. AutoPipeline media references now have coverage_scope / allowed_influence.

## Reference state

STYLE_REF_001:
- role: PERSON_STYLE_AUTHORITY
- sha256: fd763500b9c34e24d85805eb2c74b5b37a5361b82b3749644254c93922da6422
- repository binary: NOT_YET_MATERIALIZED
- coverage: PERSON only

Important:
The binary is not stored in the repository yet. The manifest contains identity/hash/role only.
Future renderer execution still requires the actual image bytes to be supplied or otherwise recovered.

## Structural resolutions completed

1. Public BODY S01 and visual anchor are now independently routed:
   - BODY_S01 when the opener is naturally suitable;
   - non-public DEDICATED_A00 when anchor needs would weaken the appetite-first opener.
2. AutoPipeline now distinguishes pre-dispatch authorized bindings from post-dispatch SUPPLIED proof and requires a hash-locked dispatch receipt with explicit media-input handles before result import.
3. Reference influence is domain-scoped and requested influence cannot exceed declared coverage.

## Remaining blockers

1. STYLE_REF_001 binary is still not materialized in Git. The executable packet/receipt path can prove use of a binary once registered, but the repository does not yet contain that image file.
2. The new dispatch-receipt path still needs one live end-to-end validation with the actual ChatGPT image renderer when image generation is available.
3. COVER and LETTERING have no USER_LOCKED template artifacts yet.
4. PERSON style and FOOD anti-photoreal calibration still require image generation.

## Exact next action

Present the deterministic COVER and LETTERING calibration candidates for user selection.

- COVER: choose A / B / C, reject all, or request a hybrid.
- LETTERING: choose A / B / C, reject all, or request a hybrid.
- do not promote any candidate to USER_LOCKED before explicit selection.
- no image generation is required for this gate.

After both composition templates are USER_LOCKED, defer PERSON/FOOD image calibration until image generation is available.

