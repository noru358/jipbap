# V1_E007 PRESENTATION MASTER APPROVAL

Updated: 2026-09-09
Episode: V1_E007
Food: 수육국밥
Gate: PRESENTATION_MASTER_USER_GATE / FINAL_PUBLISH_GATE
Status: USER_APPROVED

## Approval

The user explicitly approved the complete seven-page lettered preview on 2026-09-09.

Normal user gates:
- STORYBOARD_USER_GATE: APPROVED
- ART_BUNDLE_USER_GATE: APPROVED
- PRESENTATION_MASTER_USER_GATE / FINAL_PUBLISH_GATE: APPROVED

No additional routine user approval is required after editable reconstruction unless presentation parity cannot be restored without changing the approved intent.

## Locked artwork authority

BODY source:
- SHA-256: `54bd5d32f2cc91fa846da371776c55a225af069fb7bcff23f2c7768d1346d230`
- dimensions: 1024 × 1536
- generation id: `e2151ecc-6722-42c9-bb55-617a7edb493f`

COVER source:
- SHA-256: `68add7ddf89d332df1fb490a6a0714f8bb5f879b241cfbf5a0e483e0eaeaff5f`
- dimensions: 1122 × 1402
- generation id: `f93efb17-cff2-4961-8d2a-39b51e8597f0`

Approved BODY extraction metadata:
- mode: EXACT_CROP_FROM_APPROVED_BOARD
- S01: [9, 8, 506, 501], SHA-256 `a8cb67b73b1d0c5b987d35bc8a24903dc505f4fe4beea0ebf8c7636caf2fc57e`
- S02: [518, 8, 1015, 501], SHA-256 `e38db16e0f5300c91bc8845e3fab0eeda7d73fbe82f3b19f380932b781829022`
- S03: [9, 512, 506, 985], SHA-256 `1abf241c512c1e5b8d2b103ad5f539c87aea4e7914ab97af90260be36f2bcc06`
- S04: [518, 512, 1015, 985], SHA-256 `510cf8972be353e7ffdee9e9c4619286f4699ac5c567f42237a7f390d7167edf`
- S05: [9, 996, 506, 1528], SHA-256 `603042e9cfbee69bf7c7bec41e0f8dd0260bf3596e9cecbd60c86708db365bbd`
- S06: [518, 996, 1015, 1528], SHA-256 `38c163d751bd4c0005908cea400e7663bce4a7c8e9413db658e213458bf6b981`

## Approved presentation intent targets

The user-facing preview that was approved had these page-level SHA-256 hashes:
- COVER: `61e1f55dd580ac017262293880c1275ec6fa20f13cbbaccf225d7e0237e62c7b`
- S01: `9f2df8c17890ff670b5860bdaf3cdfa0ce039fd10a54e80563f8a07e9e9ffcfc`
- S02: `c9d2cb151afe1de3d5c8dddd6567b73dd7c1e04a2efecbea37206c3c1f6c2196`
- S03: `0de43eaf78b9ea82dc8dc4504e907b49f949cfcef02aaea0c851735a7f680ba4`
- S04: `957fd00c434a5196923ca9e28a4714cc30dcf9dccd034dfcdda616f5078dc043`
- S05: `6ae63670adde9e3b47bbb005967778b3ba14a43c1779a23b953029bfb9ee55eb`
- S06: `f1f351f02a0053aefc39f7ae93aa6748f9a0eb846b140bf385057995aee9e8b3`

Literal copy approved:
- COVER: `EP.7 취한 밤과 수육국밥`
- S01 speech: `사장님… 수육국밥 하나요.`
- S02 inner thought: `와… 냄새부터 좀 살겠다.`
- S03 inner thought: `아… 뜨끈한 게 내려간다.`
- S04 inner thought: `고기 두께 봐.`
- S05 inner thought: `여기서 깍두기 좀 말아주고.`
- S05 SFX: `쓱-`
- S06 inner thought: `아삭하고 새콤한 게 딱 끊어주네.`

## Provenance incident

The approved presentation preview was accidentally produced through stochastic image editing after `APPROVED_ART_PIXEL_LOCK`. This violated the normal V1 stage boundary.

Interpretation for E007 only:
- the preview remains the user-approved **presentation intent target** for lettering, title hierarchy, bubble/thought treatment, line rhythm, relative placement and overall page balance;
- its re-rendered/outpainted artwork pixels are NOT promoted to artwork authority;
- the exact locked BODY/COVER listed above remain the sole artwork sources;
- editable reconstruction must use those locked sources and reproduce the approved presentation intent without using the preview pixels as artwork;
- this is an episode-specific provenance correction, not a new permanent rule or gate.

## Exact next action

1. Perform `EDITABLE_RECONSTRUCTION` using only the locked COVER + exact BODY crops.
2. Map the approved presentation intent into `EDITOR_SCENE_MODEL_V1` objects.
3. Run `PRESENTATION_PARITY_QC`: exact artwork-source identity + exact literal copy + materially equivalent lettering/container/title intent.
4. If parity passes, persist composition/export artifacts and final `RUN_RECEIPT.md`, then mark V1_E007 `DONE`.
5. Do not request another routine user approval.
