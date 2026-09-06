# Episode 002 — 고등어구이 + 흰밥

Status: LETTERING_QC_FIX
Render cursor: null
Next user gate: FINAL

## Locked state

- PREPRODUCTION: PASS
- S01 artwork: APPROVED_LOCKED
- S02 artwork: APPROVED_LOCKED
- S03 artwork: APPROVED_LOCKED
- S04 artwork: APPROVED_LOCKED
- S05 artwork: APPROVED_LOCKED
- raster-set user gate: PASS
- artwork regeneration: FORBIDDEN unless user explicitly invalidates a shot

## Approved copy

- S01: `오늘은 고등어 한 마리`
- S02: `껍질부터 젓가락이 간다`
- S03: `살은 크게 떼어서`
- S04: 무자막
- S05: `가시만 남았다`

Copy verdict: PASS.

## Lettering visual QC

Verdict: FAIL.

Reason:
- typography is too large/heavy relative to illustration
- thick cream stroke produces thumbnail/meme-like visual weight
- all text was hard-positioned to the same top-left coordinate
- placement does not account for faces, food focal objects, action contact points or negative space
- previous QC only validated readability/copy mapping and therefore missed composition-level lettering quality

Scope of invalidation:
- lettering layer only
- approved raster artwork is untouched
- approved copy is untouched

## Exact next action

Recompile lettering layout from shot composition, then re-letter S01/S02/S03/S05 non-destructively.
Keep S04 silent.
After visual-lettering QC PASS, return to FINAL_USER_GATE.
