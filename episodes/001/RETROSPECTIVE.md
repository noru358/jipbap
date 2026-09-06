# E001 RETROSPECTIVE — STRUCTURE TEST

Date: 2026-09-07
Status: FINAL_CANDIDATE_REVISION_REQUIRED
Purpose: preserve the completed run as evidence, not as a publication-quality canonical episode.

## User final feedback

1. Core concept must be PROXY_EATER: the comic eats on behalf of the reader.
2. Copy must make texture, aroma, taste, temperature and feeling concrete enough to trigger appetite.
3. Shot design must optimize salivation/appetite, not merely document chronological eating steps.
4. S01 person style drifted materially from the supplied person-style reference.
5. Home background continuity should be simplified rather than recreated fully in every shot.
6. Cover needs a deliberately designed template.
7. Lettering font/size/placement needs a deliberately designed template.
8. S01/S05 were temporally interchangeable; ending needed a stronger secondary sensory payoff.
9. Structural updates must be committed before dependent renders.

## Internal QC findings

### Reference / style
- STYLE_REF_001 was a multi-character PERSON style sheet, not an all-domain visual reference.
- S01 drifted toward generic polished anime: eyes enlarged beyond much of the reference distribution, more lashes/beautification, richer texture/lighting.
- Food/background style was inferred from model priors because no FOOD/BACKGROUND reference existed.
- E001 S01 remains episode anchor only; it is not promoted to project style authority.

### Meal-scene contract
- S01 introduced multiple banchan despite preproduction saying unnecessary side dishes should not be forced.
- That initial contract violation was missed by internal QC and then propagated as continuity.
- The table setting is attractive but more elaborate than the declared minimal one-person meal.

### Appetite arc
- S02 and S03 contain the strongest appetite value.
- S04 conveys ingestion but the facial "cute" emphasis competes with sensory contact.
- S05 visually resembles the opening and does not prove meaningful post-bite change.
- Sequence appetite peaks around S03 then softens instead of delivering a stronger or second payoff.

### Geometry / action
- No catastrophic anatomy failure was observed.
- S03 spoonful is very heavily loaded and reads slightly hero-shot/ad-like rather than ordinary eating.
- S04 lip/spoon contact is readable, but mouth opening/action realization is restrained enough that the bite feels posed rather than fully embodied.

### Background
- Full-room recurrence creates continuity burden without adding equivalent appetite value.
- Future production should use NONE/LOCAL/FULL background_scope and only lock full location facts when needed.

### Copy
- "비 오니까 이게 생각났다." = context, little sensory value.
- "첫 숟갈은 두부까지." = preference/action, little texture/taste value.
- "국물 한 번 더." = continuation, little sensory payoff.
- None satisfies the new salivation gate strongly.

### Cover / lettering
- E001 cover is a functional test, not a project template.
- BODY text used large Noto Sans Bold rounded boxes; this reads like generic UI overlay and competes with the art.
- Font, line break, box treatment and placement are not locked.

## Structural promotions

Promoted to child canonical authority:
- PROXY_EATER promise
- appetite-value and temporal-distinguishability gates
- sensory copy / salivation gate
- PERSON-only style-reference coverage
- PERSON style-fidelity preflight
- background exposure scopes
- cover/lettering template calibration requirement

Promoted to AutoPipeline shared authority:
- authority-before-execution barrier
- media-reference coverage_scope / allowed_influence

## E001 disposition

Do not mark COMPLETE.
Do not repair the episode automatically.
Keep the outputs as evaluation evidence unless the user explicitly asks to rebuild E001.

## Next action

Before the next production episode:
1. calibrate PERSON-style fidelity on a fresh minimal test using the supplied person reference;
2. design and user-lock a cover template;
3. design and user-lock a lettering template;
4. then start the next episode under the hardened proxy-eater/appetite pipeline.
