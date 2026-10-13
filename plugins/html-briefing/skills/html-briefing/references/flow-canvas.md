# Flow canvas: default presentation mode

Use this for new HTML presentations unless the user selects another mode. Preserve an existing artifact's approved mode during ordinary edits. A canvas defines narrative relationships and viewing behavior, not a fixed slide size or a card design.

## Narrative and content

Begin with input (what exists at this business stage) and output (what the work should achieve). Focus each to explain context and intent. Return to the overview and reveal the core steps between them. Each step explains its blocker and solution; expand meaningful perspectives, mechanisms, examples or evidence. Gather branches back into their owning chapters for a summary of difficulties, solutions and supported results. Adapt this structure to decision briefs and independent workstreams without inventing causal or sequential relationships.

Each node has one clear theme, a readable argument and an appropriate main visual. Chapter scenes can be expressive title pages. A node may contain more than one screen of content. Never shrink long content into a fixed-height slide or turn every node into a generic card. Keep core conclusions visible; details supplement them.

Use a vertical centered main line. Arrange parallel perspectives side by side with continuous background bands and labels outside the nodes. Data science, business and AI engineering are a fictional example, not mandatory labels or a fixed number of perspectives. Connections distinguish sequence from ownership and dependency.

## Independent states

Keep the node graph, explicit structural expansion, local explanation disclosure, camera (center/scale), and per-node reading bookmarks separate. Navigation and zoom must not change the graph or erase disclosures/bookmarks. Only explicit in-content expansion/collapse changes visible descendants. A collapsed branch may retain its local state for reopening; inactive content must not remain in keyboard navigation.

Main-flow views and structural transitions center the spine by default. Deliberate horizontal navigation may center any side node. Subsequent zoom retains that node as its anchor; never pull the camera back to the spine merely because the scale changed. Moving to a main-only row recenters that row.

## Input contract

| Input | Result |
|---|---|
| Trackpad scroll in overview | Smooth two-axis canvas pan; settle at valid page/group boundaries |
| Arrow keys / WASD | Spatial node navigation; ignore text-entry controls |
| Trackpad pinch | Continuous zoom; settle at 1/4/9 capacity (side lengths 1/2/3) |
| 1 / 4 / 9, plus / minus | Keyboard zoom fallback, with the same centered-node anchor |
| In-content detail trigger | Open/close an explanation inside that node; no graph change |
| In-content branch trigger | Add/fold owned nodes; visually trace them to their parent |
| In-content focus trigger | Show that node alone, filling the stage |
| Key-node navigation | Focus an already available key node; no implicit expansion/collapse |

The capacities describe the view scale, not an exact visible-node count. Partially visible neighboring pages are useful context. Allow enough outer camera space to center the leftmost/rightmost node at every capacity. Do not hide nodes simply because only part of them is visible.

## Focus and long-form reading

Single-node focus fills the available stage. Adapt the layout without stretching glyphs. Long content scrolls vertically inside the focused page before the canvas moves. At a content edge, consume the remainder of the same gesture; only a fresh outward gesture after release moves one adjacent node. Hold subsequent momentum to avoid skipping nodes. Reverse input can immediately read back inward. A page without overflow can navigate directly.

In overview, wheel input pans the canvas even over a long node. Arrow/WASD navigation remains independent from content reading. Keep reading bookmarks per node (and disclosure mode where its content differs).

Exiting focus smoothly resets the **displayed overview** to the page top. Keep the saved reading bookmark separate: refocusing restores the previous reading position. Resize, fullscreen and programmatic scroll restoration must not overwrite it. Clamp bookmarks when actual content becomes shorter; preserve a meaningful reading anchor when localization changes layout.

Wheel events do not expose physical finger-up. The starter uses an idle-gap heuristic, not a hardware guarantee. Calibrate with real trackpad inertia on the target host before claiming native gesture acceptance. Keep OS/browser accessibility magnification available outside canvas controls and provide keyboard alternatives.

## Motion and chrome

Expansion grows descendants from their parent after establishing enough space. Collapse returns descendants to the nearest surviving ancestor before closing layout gaps. Keep the parent, connector and lane context legible during the transition. Camera motion and structural motion are separate; zoom cannot fold branches. Reduced motion provides the same final state immediately.

The presentation stage fills the window. Do not add a persistent branding header, status footer or zoom toolbar. Use a small top-edge reveal area for an auto-hiding navigation overlay; expose it on hover, keyboard focus and an accessible click/tap control. Its left side lists meaningful available key nodes, and its right side holds language and fullscreen/exit. Leaving hides it without trapping focus. No reset button by default.

Preserve the configured language set. For a single language, omit redundant switching unless requested; a retained language entry states that only that language is available. Fullscreen labels follow actual browser state and rejected requests are handled. See [workspace controls](workspace-controls.md) for language and fullscreen behavior.

## Starter and authoring

The bundled [HTML template](../assets/flow-canvas/presentation.template.html) and [model](../assets/flow-canvas/canvas-model.js) preserve the working fictional customer-feedback example. They are an editable starter, not a universal graph engine. No network assets, GSAP runtime or framework are needed for this starter.

Build an editable, self-contained HTML file with the [builder](../scripts/build_flow_canvas.py):

```sh
python3 scripts/build_flow_canvas.py --output /path/to/project/presentation.html
```

Run that command from this skill directory, or invoke the builder by its absolute path. Existing output is protected unless `--force` is supplied. For continued authoring, copy the template/model into the project's existing source structure and pass `--template` and `--model` to the builder. Never customize the installed plugin cache as a project source.

Adapt the template's `cards` and `slideContent` objects, node-specific visuals, labels and language. Adapt the model's `parents` and `layout`, plus corresponding content-trigger mapping and summary/lane rendering, together when changing narrative topology. Retain stable node IDs, explicit ownership and one authoritative model for navigation and scene state. HTML fragments in the template are trusted authored markup; escape untrusted content before insertion. The demo's dimensions, palette, three lane names and animation duration are tuning choices, not mode requirements.

Reuse projection, zoom-anchor, snap and reading-gesture behavior with the packaged model tests. Do not add a new framework or general graph abstraction solely to recreate this example. The original Chinese fictional demo is a regression example, not the user's language or business content for a new briefing.

## Acceptance

Test actual final files, not just model output:

1. Open branches and local explanations; switch 1→4→9→1. The same content remains open.
2. Center each outer node and zoom to focus. Its identity stays centered; partial neighbors remain visible in overview.
3. Expand and collapse a nested branch. Its parent remains understandable; keyboard focus moves to a surviving owner if needed.
4. Read a long node at top, middle and bottom. Same-gesture edge inertia holds; a new outward gesture moves one node. Reverse scroll reads inward.
5. Exit focus: overview scroll is zero. Re-enter: the saved reading position returns. Repeat after detail changes, resize and fullscreen.
6. Hover/focus the hidden navigation; jump to an existing node. Graph state remains unchanged. Check narrow viewports and reduced motion.
7. Check the extracted self-contained HTML offline, then the intended browser and physical input hardware. Model checks, browser checks, native trackpad feel and cross-platform acceptance are distinct evidence.

Do not claim all seven groups pass from a successful build or copied prototype evidence. Record which checks ran against the delivered package.
