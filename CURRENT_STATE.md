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

## Exact next action

Run a **template/style calibration session before another full episode**:

A. PERSON style calibration
- use the supplied PERSON reference as actual media;
- generate a minimal subject/style test;
- compare eye ratio, face simplification, line, fill, shading, hair density against the reference;
- user-lock the accepted person rendering direction.

B. FOOD style / appetite calibration
- test a small number of food close-ups under the PERSON style abstraction envelope;
- remove glossy semi-real/ad drift while preserving enough texture to trigger appetite;
- if text rules alone are insufficient, approve a separate FOOD_STYLE_AUTHORITY.

C. COVER template calibration
- make 2–3 structural cover variants using the same approved hero;
- compare title hierarchy, food/character ratio, series mark, safe area and phone-size readability;
- lock one template.

D. LETTERING template calibration
- test 2–3 font/weight/size/box/no-box treatments on the same BODY frame;
- validate negative-space placement and mobile readability;
- lock one project lettering template.

Only after A/B/C/D are approved should a new production episode start.
Do not mark E001 COMPLETE unless the user explicitly asks to repair/reopen it.
