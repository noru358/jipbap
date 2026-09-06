# COMPOSITION CALIBRATION CANDIDATES — two-phase template lock

Status: IN_TEST
Updated: 2026-09-07

These candidates define composition grammar only. They are not production assets and they do not become USER_LOCKED from placeholder review alone.

## Two-phase rule

Phase 1 — PLACEHOLDER SPEC CALIBRATION
- render only deterministic calibration fixtures;
- production registry may remain empty;
- compare hierarchy, placement, crop behavior, negative space, box treatment and type class;
- explicit user selection promotes one COVER candidate and one LETTERING candidate to `SPEC_LOCKED`;
- no placeholder pixel/hash becomes production visual authority.

Phase 2 — REAL-PIXEL VALIDATION
- after the BODY pilot has approved PERSON/FOOD/CONTACT assets;
- rerender the selected specs with those approved assets and hash-bound production font bytes;
- validate phone-size readability, food dominance, character/style coherence and actual Korean glyph metrics;
- explicit user approval then promotes the template to `USER_LOCKED`.

A template cannot skip from IN_TEST directly to USER_LOCKED.

## COVER

All candidates use a 4:5 canvas. COVER remains separate from BODY.

### A — editorial_header
- spec_id: `COVER_A_EDITORIAL_HEADER`
- structure: title/header band in the upper ~28–32%; hero composition below
- food: dominant lower hero, not cropped aggressively
- character: secondary side/corner slot
- title: bold sans editorial class, large two-level hierarchy
- series mark: small, stable top-area slot
- intent: immediate series recognition and strongest title readability
- fixture: `calibration/fixtures/cover_A.scene.json`

### B — full_bleed_plate
- spec_id: `COVER_B_FULL_BLEED_PLATE`
- structure: food hero occupies most of the canvas; compact title plate overlays unused corner space
- food: largest uninterrupted visual area
- character: optional small corner slot
- title: compact editorial class; plate is rectangular, not a generic rounded UI pill
- intent: preserve artwork immersion while keeping title legible
- fixture: `calibration/fixtures/cover_B.scene.json`

### C — food_first_poster
- spec_id: `COVER_C_FOOD_FIRST_POSTER`
- structure: clear title zone + very large food crop + small character slot
- food: may intentionally extend beyond left/top/bottom canvas bounds to create poster-like crop
- character: stable secondary slot and never larger than the food focal mass
- title: bold sans poster class
- intent: make the meal unmistakably the channel hero
- fixture: `calibration/fixtures/cover_C.scene.json`

## LETTERING

Phase-1 sample copy is placeholder text only. Korean font bytes and exact glyph metrics are Phase-2 concerns.

### A — direct_editorial
- spec_id: `LETTERING_A_DIRECT_EDITORIAL`
- box: none
- placement: negative-space anchor
- type class: editorial text
- treatment: dark text with restrained contrast aid only when needed
- intent: least UI-like, strongest integration with artwork
- fixture: `calibration/fixtures/lettering_A.plan.json`

### B — paper_tag
- spec_id: `LETTERING_B_PAPER_TAG`
- box: compact rectangular paper tag
- placement: negative-space anchor
- type class: clean rounded/sans editorial
- intent: reliable readability without generic chat-bubble styling
- fixture: `calibration/fixtures/lettering_B.plan.json`

### C — hand_note
- spec_id: `LETTERING_C_HAND_NOTE`
- box: none
- placement: loose note-style anchor
- type class: handwritten
- treatment: minimal guide-line treatment allowed
- intent: warmer diary/memo feel
- fixture: `calibration/fixtures/lettering_C.plan.json`

## Approval gate

User must choose:
- one COVER candidate A/B/C, reject all, or request a hybrid;
- one LETTERING candidate A/B/C, reject all, or request a hybrid.

The selected candidate is recorded in `CALIBRATION_STATE.json` with status `SPEC_LOCKED`.
Only the selected spec is carried into the BODY pilot and later real-pixel validation.

Rejected candidates remain calibration evidence only and must not silently become defaults.
