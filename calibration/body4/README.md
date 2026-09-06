# BODY 4 calibration fixture — hybrid boundary pilot

Status: **AWAITING USER APPROVAL**  
Purpose: architecture calibration only; this is not publishable episode 001.

## Why this meal

The fixture uses **fried egg on rice** because one compact meal exercises the exact boundaries the new architecture is meant to prove:

1. PERSON identity appears in more than one shot but is not regenerated with every food state.
2. FOOD_STATE has an unambiguous chain: intact yolk → broken yolk coating rice → one bite removed.
3. S02 forces a real hand/spoon/food contact check.
4. S03 forces a high-risk spoon-to-mouth geometry check.
5. S03 and S04 intentionally reuse the **same approved residue-food asset** with different composition/crop.
6. No full-frame stochastic render is needed.

## BODY sequence

- **S01 — anticipation:** person secondary, egg-on-rice foreground; intact yolk.
- **S02 — transformation:** macro; spoon breaks yolk while the egg is still on the rice.
- **S03 — ingestion:** same person identity; yolk-coated spoonful reaches the mouth.
- **S04 — residue:** food-only close crop; partial bowl and yolk streaks prove the bite happened.

COVER remains a separate product slot and BODY=4 remains calibration-only.

## Minimal starter asset set

Exactly six current gaps:

1. PERSON_CONTEXT_SEATED
2. PERSON_BITE_SPOON_CONTACT
3. FOOD_EGG_RICE_INTACT
4. FOOD_EGG_RICE_BROKEN
5. FOOD_EGG_RICE_RESIDUE
6. CONTACT_SPOON_PRESS_YOLK

No background asset is required for this pilot. LOCAL/NONE context uses deterministic canvas/background exposure so the test remains focused on the hybrid asset boundary.

The bite pose keeps hand + spoon + mouth contact as one semantically coherent PERSON/contact asset. Splitting that interaction into tiny face/hand/spoon fragments would make composition less reliable rather than more modular.

## Registry resolution

Current production registry contains 0 approved assets, so all six requirements are ASSET_GAPs.

This is expected. **Do not register anything before generation/import → QC → explicit user approval → SHA-256 registration.**

## User gate

Asset authoring must not start until this fixture is explicitly approved.  
Approval is for the calibration content/storyboard only; it is not approval of any future generated pixels.
