# Jipbap deterministic placeholder fixtures

These files exist only for Phase-1 template SPEC calibration.

They are deliberately separate from `assets/production/registry.json`.
Never copy CAL_* assets or placeholder hashes into the production registry.

Run from the AutoPipeline superproject root after child submodules are current:

```bash
mkdir -p jipbap/calibration/fixtures/output

for v in A B C; do
  python -m pipeline.compositor \
    --project-root jipbap \
    --registry calibration/fixtures/registry.json \
    --scene "jipbap/calibration/fixtures/cover_${v}.scene.json" \
    --output "jipbap/calibration/fixtures/output/cover_${v}_art.png"

  python -m pipeline.lettering \
    --project-root jipbap \
    --plan "jipbap/calibration/fixtures/cover_${v}.title.plan.json" \
    --output "jipbap/calibration/fixtures/output/cover_${v}_preview.png"
done

for v in A B C; do
  python -m pipeline.lettering \
    --project-root jipbap \
    --plan "jipbap/calibration/fixtures/lettering_${v}.plan.json" \
    --output "jipbap/calibration/fixtures/output/lettering_${v}_preview.png"
done
```

Candidate C intentionally uses negative x placement to exercise left-edge crop support.

The placeholder runtime font is not production typography authority. After BODY pilot assets exist,
the selected specs must be rerendered with real artwork and hash-bound production font bytes before USER_LOCKED.
