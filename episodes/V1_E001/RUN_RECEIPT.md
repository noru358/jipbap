# V1_E001 RUN_RECEIPT

Updated: 2026-09-08
Architecture: SIX_PANEL_BOARD_FIRST
Episode: V1_E001
Stage: DONE

## User approvals

- STORYBOARD_USER_GATE: APPROVED
- JIPBAP_STYLE_CARRIER_V1: USER_LOCKED from supplied single-person transparent carrier
- BOARD_STYLE_USER_GATE: APPROVED ("우선 통과")
- FINAL_PUBLISH_GATE: APPROVED ("우선 승인")

## Carrier

- asset_id: JIPBAP_STYLE_CARRIER_V1
- session-source SHA-256: 43e791e8ebb1389fb7c469786f76fe118bcb96182d7c06e080d9088fb4057a80
- dimensions: 583 × 622
- content contract: one person / no food / no text / no grid / no story sequence / transparent-minimal background
- repository registry: assets/reference_registry.json
- repository binary materialization: NOT_COMPLETED_IN_THIS_RUNTIME
- runtime binding used: SESSION_ONLY fallback

## BOARD

Accepted master board:
- renderer generation id: 3c20747b-7e9c-421c-8a00-1c4b5b481139
- dimensions: 1024 × 1536
- SHA-256: 59740618ec87d67acc0c5e1ac53a1705d585258e0228d16122fa99a8a50084f1
- format: text-free 2 columns × 3 rows
- user-requested correction before acceptance:
  1. increase staging/camera/expression variety
  2. S05 = lettuce already holding pork while sliced garlic is being added
  3. reduce FOOD photorealism and keep FOOD/PERSON in one illustrated medium

V1 hard-fail QC on accepted board:
- six extractable cells: PASS
- meaning-bearing generated text: PASS (none)
- catastrophic person identity/medium drift: PASS
- focal anatomy/contact failure: PASS
- food-state/action contradiction: PASS
- wrong core menu/entity: PASS

Soft note:
- the generated board still uses a relatively polished cute-webcomic rendering and some food-detail emphasis, but the user explicitly accepted it. This is not promoted into a new permanent hard gate.

## Deterministic assembly

Final page size: 1080 × 1350 (4:5)
Generated stochastic artwork was not regenerated after BOARD acceptance.

Artifacts:
- 00_COVER.png — e62713afb7a279d141319359197482f3c7ed4178917b784465c0faeb7c35c7d4
- 01_BODY_S01.png — 0d375a2d196dd696134961703aac6ffa87f663a2c687c6816b66ec927be5ae7e
- 02_BODY_S02.png — 03a1460d1357c1bb1960b6086fabb1c7aa6aa0e0d19faa6f8bfe76e74f5fa999
- 03_BODY_S03.png — 5af6ebbc9899c20f6edac5d09e57db364a85408d3902e3776fcb9113a847168f
- 04_BODY_S04.png — e3844e735524039397cb2cfa38fb50f505d8a448d6105a44a63fa046aae300b2
- 05_BODY_S05.png — 73d025e7737aeba701a1d38c0857af95ad440ae786c9acd1a00d1147cf024b02
- 06_BODY_S06.png — 1d87e01be3fef91fefd56d4380e19403180f323fa2933122d526e27b516ca628
- publish gate preview — aa3c2681601ced9c1c15196d0c444f339afe627ab4d09257766bc64dca29a351
- final carousel ZIP — 2f701ceb3e6044962cd8d6d4438d9d89268ad988bba4500854b6c7767f9b4da5

Final deterministic copy:
- S01 inner thought: 이 냄새부터 반칙인데.
- S02 inner thought: 밥 위에 올리면 끝.
- S03: silent
- S04 speech: 아, 이건…
- S05 inner thought: 상추에 편마늘까지 올리면 또 다르지.
- S06 inner thought: 한입만 더 먹을게.

## Runtime protocol note

This production conversation contained earlier raw/multi-expression style material before the single-person carrier was supplied. The accepted production BOARD was nevertheless explicitly approved by the user. Do not treat this as evidence to remove the canonical clean carrier-isolation rule; it is a run-level deviation, not a new V1 rule.

## Final status

V1_E001 is DONE.
The final carousel was explicitly approved at FINAL_PUBLISH_GATE.
No further mutation is authorized unless the user explicitly reopens this episode.
