# V1_E003 RUN RECEIPT

Episode: V1_E003
Menu: 제육볶음
Status: DONE
Closed: 2026-09-09
Architecture: SIX_PANEL_BOARD_FIRST
Presentation shell: JIPBAP_PRESENTATION_SHELL_V2
Profile revision: 2026-09-09_FULL_ART_OVERLAY
Scene model: EDITOR_SCENE_MODEL_V1

## Final decision

The user explicitly requested: "이번 3화는 여기에서 닫자. 마무리해줘."

This explicit close is recorded as FINAL_PUBLISH_GATE = APPROVED_BY_EXPLICIT_USER_CLOSE.
Do not reopen V1_E003 unless the user explicitly asks to revise episode 3.

## Canonical composition

Authority:
- episodes/V1_E003/composition/COVER.layout.json
- episodes/V1_E003/composition/S01.layout.json
- episodes/V1_E003/composition/S02.layout.json
- episodes/V1_E003/composition/S03.layout.json
- episodes/V1_E003/composition/S04.layout.json
- episodes/V1_E003/composition/S05.layout.json
- episodes/V1_E003/composition/S06.layout.json
- episodes/V1_E003/composition/manifest.json

Canonical handoff candidate:
- V1_E003_제육볶음_COVER_RESTORED_TD031.toondesk
- SHA-256: bdd412e63f80ef0bd5d1fc555efb9840cb6a1ccadda5b04d452036c2de850817

COVER approved visual source:
- SHA-256: 12a701747e5fafc9ad36f20f729d91496f553a0d8a1b81c862d102f130b78a89
- provenance: sticky cover_artwork_provenance
- title/menu: editable lettering objects

## BODY extraction

Master board:
- dimensions: 1024 × 1536
- x interiors: [16,501], [522,1010]
- y interiors: [11,488], [509,937], [958,1517]
- extraction method: detected actual panel borders
- nominal 512px slicing: NOT USED
- adjacent-panel contamination: repaired

## Final presentation repairs

- full-art BODY shell; fixed lower meta band removed
- speech / thought / narration / SFX remain editable overlays
- COVER source restored and protected from silent BODY substitution
- COVER title/menu kept editable
- S04 and S06 speech tails use short soft-curved rich-tail geometry
- focal-safe avoid metadata retained
- preferred fonts recorded by semantic role
- ToonDesk font resolver weight-check bug repaired in editor code

## Layout SHA-256

- COVER.layout.json: 3b0a688e3a2c5cca9b39aefe4f29388b188dbc1a30ee9073ca90457de49e2528
- S01.layout.json: 132594819279875ce7ad674c68d3213013943b97783077c8f23dcdfd21f58e0c
- S02.layout.json: 8f352c74f89e70f00802ad35656ce63bd601c5030c38b5db67f3c667b3ec69a7
- S03.layout.json: 29fc30282b6a7d6098d6768c08256419cd5c00f548b2d097945abd119781ab82
- S04.layout.json: 8bdb9e138ce030955a580444d810702a664786894c955e7cdee67457b94b73a4
- S05.layout.json: c1b73c260c8267e0d76319a680acd606f9249db8147f5ea06619c87380ae9245
- S06.layout.json: 9e8890c42aad7f63a550c34cb46e2daa6d922b5163bd54489d0ff713a35456cc

## Round-trip note

Earlier ToonDesk no-edit round trips proved scene preservation and exposed authoring defects that were subsequently repaired.
The final TD031 candidate was not subjected to one additional user-export round trip because the user explicitly chose to close the episode at this point.
This is a closure decision, not a new production rule or permanent gate.

## Carry-forward

Structural improvements from E003 remain active for future episodes:
- actual panel-boundary extraction
- full-art overlay presentation
- sticky COVER provenance
- focal-aware lettering placement
- rich editable speech tails
- explicit preferred/resolved font behavior
- ToonDesk Web Live as the primary interactive editor transport

V1_E003 is complete.
