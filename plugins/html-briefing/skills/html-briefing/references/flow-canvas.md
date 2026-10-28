# Flow canvas: default presentation mode

Use this for new HTML presentations unless the user explicitly requests another mode. Preserve an existing artifact's approved mode during ordinary edits. A canvas defines narrative relationships and viewing behavior, not a fixed slide size or a card design.

## Narrative and content

Begin with input (what exists at this business stage) and output (what the work should achieve). Focus each to explain context and intent. Return to the overview and reveal the core steps between them. Each step explains its blocker and solution; expand meaningful perspectives, mechanisms, examples or evidence. Gather branches back into their owning chapters for a summary of difficulties, solutions and supported results. Adapt this structure to decision briefs and independent workstreams without inventing causal or sequential relationships.

Each node has one clear theme, a readable argument and an appropriate main visual. New chapter scenes retain large background-color fields, light text and oversized outline chapter numerals, following [visual direction and selection](visual-direction.md). This visual contract leaves font and palette choice open; approved existing designs remain unchanged during ordinary edits. A node may contain more than one screen of content. Never shrink long content into a fixed-height slide or turn every node into a generic card. Keep core conclusions visible; details supplement them.

The bundled starter uses the following layout, which may be adapted to an approved speaking order: place every chapter title page in the leftmost vertical column; chapters progress downward. Expand the content owned by each chapter to its right, with the first content row aligned to that chapter. Reserve additional rows for deeper content before the next chapter. Arrange parallel perspectives side by side to the right, retaining continuous background bands and labels outside the nodes. This is graph placement, not a pinned sidebar: focused pages still fill the stage. Data science, business and AI engineering are a fictional example, not mandatory labels or a fixed number of perspectives. Connections distinguish sequence from ownership and dependency.

## Independent states

Keep the node graph, explicit structural expansion, local explanation disclosure, camera (center/scale), and per-node reading bookmarks separate. Navigation and zoom must not change the graph or erase disclosures/bookmarks. Only explicit in-content expansion/collapse changes visible descendants. A collapsed branch may retain its local state for reopening; inactive content must not remain in keyboard navigation.

Main-only views may center the chapter being read. In the starter layout, expansion shows the owning chapter at the left of the overview and its content to the right; collapse returns content to that chapter. Deliberate horizontal navigation may center any content node. Subsequent zoom retains that node as its anchor; never pull the camera back to the spine merely because the scale changed. Moving to a chapter-only row focuses that chapter column.

## Input contract

| Input | Result |
|---|---|
| Trackpad scroll in overview | Smooth two-axis canvas pan; settle at valid page/group boundaries |
| Arrow keys / WASD | Spatial node navigation; ignore text-entry controls |
| Trackpad pinch | Continuous zoom; settle at 1/4/9 capacity (side lengths 1/2/3) |
| 1 / 4 / 9, plus / minus | Keyboard zoom fallback, with the same centered-node anchor |
| In-content detail trigger | Open/close an explanation inside that node; no graph change |
| In-content branch trigger | Add/fold owned nodes; visually trace them to their parent |
| Double-click a page’s text or background in overview | Focus that page alone; preserve expansion, disclosures and reading bookmarks |
| In-content focus trigger | Show that node alone, filling the stage |
| Key-node navigation | Focus an already available key node; no implicit expansion/collapse |

The capacities describe the view scale, not an exact visible-node count. Partially visible neighboring pages are useful context. Allow enough outer camera space to center the leftmost/rightmost node at every capacity. Do not hide nodes simply because only part of them is visible.

## Focus and long-form reading

Double-clicking an overview page uses the same focus path as its focus button. Ignore clicks on interactive controls and on hidden/inert nodes. In single-node focus, leave double-click behavior alone so text selection and reading position remain intact.

Single-node focus fills the available stage. Adapt the layout without stretching glyphs. Long content scrolls vertically inside the focused page before the canvas moves. At a content edge, consume the remainder of the same gesture; only a fresh outward gesture after release moves one adjacent node. Hold subsequent momentum to avoid skipping nodes. Reverse input can immediately read back inward. A page without overflow can navigate directly.

In overview, wheel input pans the canvas even over a long node. Arrow/WASD navigation remains independent from content reading. Keep reading bookmarks per node (and disclosure mode where its content differs).

Exiting focus smoothly resets the **displayed overview** to the page top. Keep the saved reading bookmark separate: refocusing restores the previous reading position. Resize, fullscreen and programmatic scroll restoration must not overwrite it. Clamp bookmarks when actual content becomes shorter; preserve a meaningful reading anchor when localization changes layout.

Wheel events do not expose physical finger-up. The starter uses an idle-gap heuristic, not a hardware guarantee. Calibrate with real trackpad inertia on the target host before claiming native gesture acceptance. Keep OS/browser accessibility magnification available outside canvas controls and provide keyboard alternatives.

For a linear live talk, consider a stricter focus policy: wheel/trackpad input reads only within the current node, while explicit next/previous actions change nodes. Within a node, viewport-sized reading parts may snap to stable boundaries; oversized native demos still need continuous scrolling. Avoid resting halfway between two parts or showing the next heading as an accidental fragment. Preserve keyboard and reduced-motion access. These are adaptations to implement and test, not behavior supplied by the starter.

## Progressive reveal for a live route

For a vertical narrative, center a project's children below its title with downward connectors. Reserve horizontal lanes for actual parallel work or a side branch. A closed side branch should not consume a permanent empty lane; open it from the problem or object that motivates it and reflow around a stable anchor. Keep ownership and continuation to the next chapter visible. Update layout-model checks when changing placement; the starter's left-column assertions do not validate a vertical adaptation.

Define title activation separately from page focus. If the requested action is “expand then focus,” run both through the shared state/controller path; a container chapter may instead reveal only its project entries. Do not attach fold toggles to the whole page, where blank clicks, text selection or double-click focus would conflict. Restore an existing demo instance and user choices when re-entering it.

## Motion and chrome

Expansion grows descendants from their parent after establishing enough space. Collapse returns descendants to the nearest surviving ancestor before closing layout gaps. Keep the parent, connector and lane context legible during the transition. Camera motion and structural motion are separate; zoom cannot fold branches. Reduced motion provides the same final state immediately.

The presentation stage fills the window. Do not add a persistent branding header, status footer or zoom toolbar. Use a small reveal area for an auto-hiding navigation overlay, with an inset click/tap target that remains reachable beneath browser chrome in macOS fullscreen; expose it on hover, keyboard focus and an accessible click/tap control. Its left side lists meaningful available key nodes, and its right side holds language and fullscreen/exit. Leaving hides it without trapping focus. No reset button by default.

Preserve the configured language set. For a single language, omit redundant switching unless requested; a retained language entry states that only that language is available. Fullscreen labels follow actual browser state and rejected requests are handled. See [workspace controls](workspace-controls.md) for language and fullscreen behavior.

## Starter and authoring

The bundled [HTML template](../assets/flow-canvas/presentation.template.html) and [model](../assets/flow-canvas/canvas-model.js) preserve the working fictional customer-feedback example. They are an editable starter, not a universal graph engine. No network assets, GSAP runtime or framework are needed for this starter.

New presentations must begin with the [creation entrypoint](../scripts/new_briefing.py), unless the user explicitly requests another form:

```sh
python3 scripts/new_briefing.py --directory /path/to/new-briefing
```

The destination must not exist. It creates `presentation.template.html`, `canvas-model.js` and the rebuildable `presentation.html`. Preserve these authoring sources and user materials; replace the fictional case with the actual narrative. Use the same canvas sources for the 2–3 visual directions, varying typography/color rather than navigation mode.

Rebuild the edited sources with the [builder](../scripts/build_flow_canvas.py):

```sh
python3 scripts/build_flow_canvas.py --template /path/to/new-briefing/presentation.template.html --model /path/to/new-briefing/canvas-model.js --output /path/to/new-briefing/presentation.html --force
```

Run that command from this skill directory, or invoke the builder by its absolute path. Existing output is protected unless `--force` is supplied. The builder checks canvas structure before writing, including on forced rebuilds. Keep the starter’s controller identifiers; adapting content, layout and styling does not require replacing them. For continued authoring, copy the template/model into the project's existing source structure and pass `--template` and `--model` to the builder. Never customize the installed plugin cache as a project source.

Adapt the template's `cards` and `slideContent` objects, node-specific visuals, labels and language. Adapt the model's `parents` and `layout`, plus corresponding content-trigger mapping and summary/lane rendering, together when changing narrative topology. Retain stable node IDs, explicit ownership and one authoritative model for navigation and scene state. HTML fragments in the template are trusted authored markup; escape untrusted content before insertion. The demo's dimensions, palette, three lane names and animation duration are tuning choices, not mode requirements.

Reuse projection, zoom-anchor, snap and reading-gesture behavior with the packaged model tests. Do not add a new framework or general graph abstraction solely to recreate this example. The original Chinese fictional demo is a regression example, not the user's language or business content for a new briefing.

## Acceptance

Test actual final files, not just model output:

1. Check the chosen hierarchy: for the starter, chapters remain left and owned pages unfold right; for an adapted vertical route, children center below their owner and closed side branches leave no empty lane. Open branches and local explanations; switch 1→4→9→1. The same content remains open.
2. Double-click an overview page, including a rightmost branch, to enter full-stage focus; controls retain their actions and repeated double-clicks in focus preserve reading position. Center each outer node and zoom to focus. Its identity stays centered; partial neighbors remain visible in overview.
3. Expand and collapse a nested branch. Its parent remains understandable; keyboard focus moves to a surviving owner if needed.
4. Read a long node at top, middle and bottom. Same-gesture edge inertia holds; a new outward gesture moves one node. Reverse scroll reads inward.
5. Exit focus: overview scroll is zero. Re-enter: the saved reading position returns. Repeat after detail changes, resize and fullscreen.
6. Hover/focus the hidden navigation; jump to an existing node. Graph state remains unchanged. Check narrow viewports and reduced motion.
7. Check the extracted self-contained HTML offline, then the intended browser and physical input hardware. Model checks, browser checks, native trackpad feel and cross-platform acceptance are distinct evidence.

Do not claim all seven groups pass from a successful build or copied prototype evidence. Record which checks ran against the delivered package.


## Creation and delivery gate

Run the packaged scripts from the skill directory, or invoke their absolute paths; asset lookup is relative to the scripts, not the caller’s working directory. The Python 3.10+ standard library is sufficient. Do not substitute a package self-test for checking the actual presentation.

During authoring:

```sh
python3 scripts/check_presentation.py /path/to/new-briefing/presentation.html --structural-only
```

This rejects plain pages and missing starter DOM/controller/input hooks. It prints the artifact SHA-256 and explicitly leaves browser acceptance UNVERIFIED. It does not execute JavaScript, prove behavior, judge storytelling, or prevent a host from bypassing the scripts. Do not fix a failure by adding inert marker strings or waiving the mode without a user request.

Before delivery, inspect the final file with the available browser, then save a small JSON record alongside existing project evidence. Use the final file’s printed SHA-256. Record actual observations for all five groups below, with `status: "PASS"` only after the relevant behaviors work; use `FAIL` or `UNVERIFIED` otherwise. The record attests observations; the checker verifies completeness and artifact identity, not whether an observer is truthful.

```json
{
  "artifact_sha256": "SHA-256 of the inspected HTML",
  "environment": "Actual browser, viewport and input used",
  "checks": {
    "layout": {"status": "UNVERIFIED", "evidence": ""},
    "navigation_zoom": {"status": "UNVERIFIED", "evidence": ""},
    "focus": {"status": "UNVERIFIED", "evidence": ""},
    "disclosure": {"status": "UNVERIFIED", "evidence": ""},
    "reading": {"status": "UNVERIFIED", "evidence": ""}
  }
}
```

- `layout`: the selected chapter/content placement, visible node ownership, and correct space reclamation for closed branches; record any adaptation from the starter.
- `navigation_zoom`: two-axis navigation, 1/4/9 zoom and current-node anchoring without folding branches.
- `focus`: double-click enters full-stage focus; controls retain actions.
- `disclosure`: local detail and structural expansion/collapse behave separately.
- `reading`: long-page scrolling, overview top and bookmark restoration. If the actual presentation has no long content, record that observed fact and why the reading check is not applicable rather than fabricate a scroll test.

```sh
python3 scripts/check_presentation.py /path/to/new-briefing/presentation.html --browser-report /path/to/browser-checks.json
```

Exit 0 means the structure and complete matching evidence record pass; exit 1 means failed checks; exit 2 means missing browser evidence. Recheck after changes: the old record cannot pass for changed HTML. Report physical trackpad, offline and cross-platform checks separately; keyboard/browser verification does not establish them.

For an explicitly requested alternative, pass `--alternative-request "exact user request"`. Keep the same quote in the report’s `user_request` and replace the five canvas checks with `alternative_behavior`, with observed evidence for the requested mode. This reports an explicit alternative, never a canvas pass. The software cannot authenticate human authorization: the agent must verify it in the conversation. Ordinary edits to an already approved non-canvas artifact keep its existing validation workflow; this new-creation gate does not authorize migrating it.
