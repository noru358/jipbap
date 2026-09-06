# Episode 002 — 고등어구이 + 흰밥

Status: S02_WAITING_REFERENCE_BINDING
Render cursor: S02
Next user gate: RASTER_SET

## Locked state

- PREPRODUCTION: PASS
- S01: APPROVED_LOCKED
- S01 regeneration: FORBIDDEN unless user invalidates
- S02~S05: internal render/QC
- next user approval: full raster set

## Meal context

Context ID: E002_KOREAN_HOME_DINNER

Compiled dining grammar:
- Korean metal spoon + chopsticks
- place spoon/chopsticks together at diner right side
- reject Japanese horizontal chopstick-rest staging
- no palms-together pre-meal gesture as default
- natural hand pose follows current food action
- individual rice/soup; Korean home-table main/sides
- Korean ceramic/porcelain vessels
- reject Japanese miso-bowl/garnish/rolled-egg visual contamination

These are E002-specific compiled constraints, not global hardcodes.

## S01

Status: APPROVED_LOCKED

Role:
- continuity facts only
- not edit target
- not composition authority

## S02 render capsule

target_shot_id: S02

ALLOW:
- STYLE_REF_001 style facts
- S01 continuity facts:
  - same woman identity if any person fragment is visible
  - same mackerel appearance
  - same ceramic tableware family
  - same wooden table
- E002 dining-grammar subset relevant to visible utensils
- current food state only

PRE:
- mackerel.skin=intact
- mackerel.flesh=mostly_intact

ACTION:
- chopstick tips physically pry open browned mackerel skin

POST:
- skin=opened
- white flesh=exposed
- one_flake=separated_or_ready

COMPOSITION:
- 4:5
- single panel
- food macro / oblique close-up
- mackerel plate dominates frame
- partial hand/chopsticks only if needed
- no face
- no full table

MUST NOT:
- S01 full-table composition
- palms-together pose
- fish on rice
- future-shot actions
- text/captions/letters
- multi-panel page

CONTEXT FIREWALL:
- target_only=true
- deny_future_shots=true
- deny_voice_copy=true
- deny_rejected_outputs=true
- deny_locked_shot_as_edit_target=true

## S03~S05

Not included in S02 render input.
They become visible to the renderer only after cursor advances.

## Exact next action

Bind the actual STYLE_REF_001 image to the current renderer context.
Then generate S02 only from the isolated capsule above.
