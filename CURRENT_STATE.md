# CURRENT_STATE

Updated: 2026-09-06
Project: jipbap
Operating mode: MANUAL_VALIDATION

## Active episode

`episodes/002/README.md`

Episode 001 is paused at `PREPRODUCTION_RECOMPILE` / remaining-render retry. It is not deleted or treated as complete.

## Latest user direction

Start a new Episode 002 now.

This newer instruction supersedes the previous "continue Episode 001 next" action. The repository state is reconciled by pausing Episode 001 and starting Episode 002 from the canonical pipeline entry point.

## Episode 002 current stage

`PREPRODUCTION_USER_GATE`

Proposed menu/moment:
- 고등어구이 + 흰밥
- 막 구운 고등어의 껍질을 가르고 살을 크게 떼어 밥 위에 올려 먹는 순간

Prepared:
- menu/moment
- content beats
- voice draft
- 5-shot storyboard
- food-state graph
- bridge-action check
- visual rhythm
- per-shot must_show / must_not_show

Not yet authorized:
- raster generation
- lettering

## Canonical operating rules still in force

- one frame = one image file
- raster images are text-free
- pre-raster user gate before S01
- S01 is the user visual-anchor gate
- S01 PASS → S02..final internal render/QC without per-shot user gates
- full text-free raster-set user gate before lettering
- every food shot uses precondition/action/postcondition continuity
- approved actual image reference is the highest visual authority
- reference path/hash alone is not media binding; reference-conditioned rendering fails closed without verified image bytes

## Reference integrity authority

- `assets/REFERENCE_MANIFEST.md`

Repository binary status remains:
- STYLE_REF_001: BINARY_REQUIRED_NOT_YET_MATERIALIZED
- Episode 001 S01 temporary anchor: BINARY_REQUIRED_NOT_YET_MATERIALIZED

For Episode 002 rendering, the execution environment must have an actual verified style-reference image binding before S01. Repository-only execution remains blocked until the required reference binary is materialized and hash-verified.

## Exact next action

1. User reviews Episode 002 preproduction package in `episodes/002/README.md`.
2. If approved, run visual preflight and verify actual style-reference binding.
3. Generate S01 only, single-panel / text-free / 4:5.
4. Present S01 for the user anchor gate.
