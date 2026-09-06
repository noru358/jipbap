# BODY 4 calibration fixture — hybrid boundary pilot

Status: **AWAITING USER APPROVAL**  
Fixture: `JIPBAP_HYBRID_BODY4_V2`  
Purpose: architecture calibration only; this is not publishable episode 001.

## Temporal model

A still panel is a **keyframe**, not a miniature video.

- each panel declares the exact visible state;
- every state change from the previous panel is an ordered bridge step;
- a bridge may happen between panels only when the omission is explicit, causally unambiguous and not itself worth a panel;
- menu-specific actions remain episode data, not global hard-coded rules.

This prevents ambiguous jumps such as “food was broken, then somehow it is already in the mouth.”

## BODY sequence

- **S01 — anticipation:** intact fried egg already on rice; person secondary.
- **S02 — transformation:** exact spoon/yolk breaking contact is visible.
- **S03 — pre-bite keyframe:** yolk-coated rice has been scooped and the spoon is immediately before the mouth; **no mouth contact yet**.
- **S04 — residue:** the bite happened between frames; the same already-partial bowl pixels from S03 are reused unchanged.

The omitted S03→S04 ingestion step is explicitly recorded. In normal production, if the bite/contact itself has enough sensory value, it becomes its own panel rather than being silently skipped.

COVER remains separate and BODY=4 remains calibration-only.

## Stable asset boundary

The compositor is not required to align tiny independent layers at brittle high-risk contact points.

Use five gaps:

1. `PERSON_CONTEXT_SEATED`
2. `FOOD_EGG_RICE_INTACT`
3. `INTERACTION_BREAK_YOLK`
4. `FOOD_EGG_RICE_RESIDUE`
5. `INTERACTION_BITE_APPROACH`

`INTERACTION_COMPOSITE` is an episode-local compound asset for inseparable high-risk geometry. It is still smaller than a full-frame exception and excludes unrelated text/background where practical.

`FOOD_EGG_RICE_RESIDUE` is intentionally reused in both S03 and S04 with different composition/crop to prove approved-pixel reuse.

## Dependency order

1. Bind actual STYLE_REF_001 media; author/QC foundation PERSON + intact FOOD.
2. Operator may hash-register QC-passed foundation assets for this bounded pilot.
3. Compose S01 and obtain the **user visual anchor pass**.
4. Only then author interaction assets that depend on the accepted person identity.
5. Continue deterministic composition and internal QC.
6. User receives the later final/template gates defined in canonical protocol.

This avoids parallel resampling of the same person while also avoiding one user approval per isolated raw asset.

## Exception status

Full-frame exception need is **UNASSESSED**, not predeclared false.

First attempt:
`stable asset boundary → approved assets → deterministic composition`.

Only a shot that still cannot preserve the required semantics/contact may open a bounded full-frame exception.

## User gate

The current gate approves this calibration content/storyboard and execution structure only.
It does not approve future generated pixels.
