# JIPBAP runtime implementation

Status: implemented in `pipeline.runtime.EpisodeRuntime`.

## What the controller owns

`runtime/state.json` is the only mutable runtime authority. It has a monotonic
version, append-only event records, exact review artifacts, asset registry and
approval receipts. A file lock and atomic replace prevent two local controller
calls from committing the same version. `CURRENT_STATE.md` and
`runtime/RUN_CONTEXT.md` are generated after every commit.

Natural-language input is only a conservative typed-event candidate. In
particular, `승인` becomes `APPROVE_CURRENT`; it is accepted only with the
currently displayed artifact id, its aggregate SHA-256, the exact state version
and an idempotency event id. A stale approval fails. A retry of the same approval
event is a no-op and never approves the next gate. `계속` records the next action
but cannot cross a user gate. `DONE까지` is treated the same way.

The normal state path is:

`STORYBOARD_USER_GATE → WAITING_FOR_CARRIER/ARTWORK_READY → ARTWORK_CAPTURE → ART_BUNDLE_USER_GATE → LETTERING_READY → PRESENTATION_MASTER_USER_GATE → DONE`

There are still three user gates: storyboard, actual 4:5 art bundle, and
lettered presentation. A carrier attachment resumes the existing episode; it
does not create a new episode, reference, style or approval.

## Asset and approval contract

- Reference assets and episode assets have separate store paths.
- A candidate must be a physical PNG whose signature is at byte 0, fully decodes,
  and matches a supplied SHA-256 when one is supplied. It is copied atomically
  before it becomes reviewable.
- The BODY board is actual-border extracted and the six cells plus COVER are
  deterministically fitted into physical 1080×1350 review PNGs before the art
  approval is opened.
- Art approval locks the exact BODY/COVER byte records. The controller rejects
  subsequent generation, image editing, inpainting, outpainting and replacement.
- The lettered preview must carry one `TOONDESK_PACKAGE_V1` containing exactly
  COVER + S01..S06 editable layouts. Each layout has an artwork object mapped to
  the retained locked file and a role-appropriate locked provenance record
  (exact SHA-256, exact-reuse method, and `stochastic_regeneration_allowed=false`),
  plus seven actual preview PNGs. A flattened image without that editable package
  cannot be accepted as the presentation result.
- DONE requires locked source bytes, artwork approval, presentation approval and
  verified retained files. Hash mismatch or a missing original fails closed.

The approved source bytes are immutable. Crop, scale, position, bubbles, text,
fonts, z-order and manual overrides remain scene properties. ToonDesk consumes
the same editable scene model; it does not reconstruct art from a flattened
preview.

## Environment connection ledger (2026-09-09)

| Capability | Support status | Actual verification in this change |
| --- | --- | --- |
| A. Read repository image bytes | Supported | Verified against tracked PNGs by `pipeline.cli validate`; full byte/decode tests pass. |
| B. Pass local image paths to the host image generator | Input format advertised by the current image tool (`referenced_image_paths`) | Not called: this request forbids new artwork generation. No automatic-delivery claim. |
| C. Recover generated original bytes from the host | Not established | Not verified. The runtime therefore sets `generated_original_byte_recovery=false` and requires one downloaded original upload before persistent approval. |
| D. Persist/reopen originals in a new work directory | Supported by the runtime store | Verified with immutable copy, state reload and relocated-store test. |
| E. Code extraction/composition/render | Supported | Verified with Pillow actual-border extraction and 4:5 PNG fixture rendering. ToonDesk handles editable scene rendering/export. |
| F. Restrict host image tool by stage | Controlled runtime: supported; Chat host tool: not controllable from repository code | Post-lock refusal is tested. Host limitation is recorded as `CHAT_RUNTIME_LIMIT`; no claim of Work/Chat isolation. |

These are distinct claims. A Git path, Base64 string, preview display and a tool
reference input are not treated as equivalent capabilities.

## Chat attachment rule

With the current Chat capability setting, `automatic_reference_forwarding=false`.
After storyboard approval, attach `JIPBAP_STYLE_CARRIER_V1` only when it has not
been delivered to the **current generation call**. Storing its bytes is not proof
of delivery; the controller records a delivery context separately. After artwork
generation, upload the actual BODY 2×3 original and distinct COVER original only
if the host cannot return their source bytes. The runtime resumes the pending
episode without resetting it. There is no fixed promise about attachment count.

After art approval no carrier can stand in for missing original production art.
For E007 specifically the required recovery inputs are the exact approved BODY
board, exact approved COVER, and approved presentation original; absent files are
not regenerated or silently substituted.

## Controlled-worker boundary

The controller can enforce its own action surface and source registry. It does
not grant a post-lock worker a generator credential or an asset-state mutator.
It cannot disable the separate ChatGPT host image tool, a general shell, or a
network-capable process outside that controlled deployment. Production deployment
must run the renderer/controller under a dedicated service identity with no image
generation credentials; that isolation is not supplied merely by calling it
"Work".

## Production renderer and local review route

`pipeline.presentation` is the actual no-generation post-processing path. It
consumes only the approved board/COVER bytes plus a
`JIPBAP_LETTERING_PLAN_V1`, writes one editable `TOONDESK_PACKAGE_V1`, and
renders COVER + S01..S06 PNG previews from those same scene objects. Bubbles,
curved tails, explicit line breaks, padding, alignment, z-order and a resolved
font file/byte receipt are written into each layout; art bytes are not redrawn.

For a local, persistent review path run:

```bash
python -m pipeline.web --root . --port 8765
```

The route reads/writes the same runtime state, accepts PNG/plan upload, opens
only the current approval, and serves retained preview/download files. It is a
real local controller endpoint, but it is **not deployed** and is not callable
from the Chat host. Remote deployment and Chat attachment bridging remain
separate work items.

## Commands for maintainers

```bash
python -m pipeline.cli validate
python -m pipeline.cli runtime --next-action
python -m unittest discover -s tests -p 'test_*.py' -v
```
