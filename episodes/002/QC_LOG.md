# Episode 002 QC log

## 2026-09-06 — S01

User verdict: PASS

Meaning:
- visual style: PASS
- Episode 002 continuity anchor: PASS
- project-wide style-lock promotion: NO

Meal-context correction before final S01 PASS:
- Korean meal scene had cross-context contamination risk
- rolled egg form, soup vessel/material, and soup ingredient presentation needed Korean-home-meal consistency

Structural response:
- MEAL_CONTEXT_SYSTEM.md added
- meal-context compile promoted into preproduction
- meal-context binding added to shot contract
- meal-context QC added to remaining-render QC

## 2026-09-06 — S02 internal render attempts

Required contract:
- single panel
- text free
- food macro / oblique close-up
- only mackerel plate + partial hand/chopsticks dominant
- action: chopsticks pry open grilled mackerel skin and expose white flesh
- fish remains on main plate
- no fish on rice yet
- preserve Episode 002 Korean-home-dinner context and approved visual style

Observed repeated failures:
- renderer repeatedly reverted to S01-like full-table composition
- character face/body remained dominant
- requested pry-open action was absent
- generated wall/refrigerator text appeared despite text_free=true
- output sometimes added or drifted side dishes/table arrangement

QC classification:
- STRUCTURAL_OUTPUT_FAIL
- CAMERA_COMPOSITION_FAIL
- ACTION_STATE_FAIL
- TEXT_FREE_FAIL
- CONTINUITY_DRIFT

Disposition:
- all failed S02 attempts are rejected and must not be used as episode assets
- do not advance to S03 until a valid S02 exists

Current blocker:
- renderer is not honoring shot-specific composition/action constraints in this execution context

Next valid action:
- retry S02 through a rendering path/context that can honor the shot contract
- run structural + visual + meal-context + food-state QC before advancing
