# V1_E004 POSTMORTEM — 2026-09-09

Episode remains: DONE
Published artifact remains unchanged.

## User feedback on deterministic review candidate

1. FOOD remains too photoreal / glossy.
2. Earlier draft was preferred because:
   - speech bubbles were more organic and less mechanically rectangular;
   - lettering felt more compatible with the drawn artwork;
   - COVER hero art was distinct from BODY instead of reusing a BODY panel;
   - S05 showed a semantic timing error: flavor was being described before the bite visibly entered the mouth.
3. ToonDesk feedback:
   - speech bubbles need horizontal flip;
   - default bubble silhouette is too boxy;
   - the earlier draft's softer organic bubble treatment is the target direction.

## Structural interpretation

### FOOD
Prompt-only FOOD de-photorealization has not been sufficient across repeated episodes.
Root cause: the current production carrier directly conveys PERSON style but no renderer-safe FOOD pixels.
Decision:
- introduce a separate renderer-safe `JIPBAP_FOOD_STYLE_CARRIER_V1`;
- it is a style projection, not creative authority and not a per-episode approval gate;
- calibrate it once in an isolated clean calibration task before the next production BOARD.

### COVER
Decision:
- keep `COVER_TITLE_SYSTEM_V1` semantic grammar;
- default COVER hero source becomes a distinct text-free cover illustration;
- do not silently reuse BODY artwork;
- EP label stays plain lettering by default, without a pill/bubble enclosure.

### BODY lettering
Decision:
- default speech bubble becomes a softer organic / oval silhouette;
- thinner restrained outline and narrower curved tail;
- hand-drawn Korean typography is preferred over mechanically typeset round-display defaults;
- geometry remains editable.

### Copy/action continuity
Decision:
- flavor/mouthfeel/aftertaste lines require visible or already-established ingestion;
- pre-bite frames may carry smell, appearance, anticipation, or silence;
- this is planning/QC guidance, not a new permanent hard-fail class.

## ToonDesk implementation

ToonDesk 0.3.2 changes pushed:
- soft-oval speech bubble defaults;
- narrower/curvier default speech tail;
- horizontal speech-bubble flip control that mirrors tail geometry without mirroring text;
- JIPBAP profile mirror updated to hand-drawn typography defaults;
- static JavaScript syntax validation: PASS for core/render/panels/actions/interaction/io/wiring.

No E004 published raster is mutated by these changes.
