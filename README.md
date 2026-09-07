# jipbap

짧은 집밥/음식 감상형 인스타툰 제작 프로젝트.

## Canonical V1

Current architecture: **SIX_PANEL_BOARD_FIRST**.

Normal production reads only:
1. `CURRENT_STATE.md`
2. `JIPBAP_V1_SPEC.md`

The V1 product is:
- COVER 1 + BODY 6
- one text-free 2×3 BODY master board
- style locked, staging fluid
- deterministic extraction / 4:5 assembly / cover / lettering
- minimal hard-fail QC
- one final user publish gate

The old composition-first asset system, BODY4 Lane A/B calibration, ASSET_GAP DAG and FOOD/PERSON foundation workflow are retained only as historical/debugging material and do not own runtime execution.

Reference manifests are consulted only when actual reference bytes must be materialized or validated.

## Fixed creative idea

`PROXY_EATER`: the comic eats on the reader's behalf.
Food state, eating action and sensory payoff are the center of the episode.
Background and decorative assets are omitted unless they are needed to explain the moment.

See `JIPBAP_V1_SPEC.md` for the complete frozen/unfrozen boundary.
