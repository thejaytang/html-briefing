# Visual explanation and interaction

## Choose the relationship before the medium

| Relationship | Representation | Visible meaning |
|---|---|---|
| Input becomes output | One object through stages | What is retained, removed or generated |
| Versions differ | Aligned originals/results with local annotation | Exact location and nature of the difference |
| Methods see different evidence | Same input with linked views | Grain, position, content, cost or supported scope |
| Parameters change work | Control connected to mechanism and output | Evidence, operation or result changes; no invented curve |
| Hierarchy | Expandable tree with real item identity | Parent/child membership |
| Linked workspace panes | Synchronized selection | Different representations of the same object |
| Architecture | Components, interfaces, directional data and boundaries | Who processes what and across which boundary |
| Execution over time | Sequence or timeline | Ordering, actor and wait/response |
| Test or benefit | Method next to observed result | What conclusion follows and how it is used |

Distinguish sequence, containment, dependency and data flow. Label meaningful edges; proximity and arrows do not prove a relationship. Distinguish implemented, planned and external components. Use editable SVG/HTML for precise diagrams; Mermaid is an option when the target host and offline delivery support it. Do not introduce a diagram service just for a small diagram.

Inspect reference images before adopting composition or assets. Cropped and annotated screenshots must preserve their meaning. Generated concepts must be distinguishable from real screens. Read imagegen.md when an illustrative raster subject helps explain the scene.

## Coherent visual design

For new briefings, complete [visual direction and user selection](visual-direction.md) before styling the whole artifact. Impeccable owns typography and color; preserve the chosen chapter identity.

Derive style from the audience, content and brand. Define shared typography, spacing, semantic colors, icon sizes, focus/selection states and motion timing in the project's existing style source. Use hierarchy, contrast and precise alignment; projected technical labels must remain readable. A representative scene includes actual content and an interaction, not only a palette or decorative cover.

One main theme and visual guide attention. Keep navigation coherent; a chapter sidebar is one option for a long live briefing, not a universal rule. Avoid duplicate progress systems. Small inline SVG icons have their own size constraints.

## Canvas state boundaries

For the default flow canvas, follow [flow-canvas.md](flow-canvas.md). A zoom or pan never changes the expanded node graph or local disclosures. Explicit branch collapse hides owned descendants and restores focus to a surviving ancestor; saved reading/disclosure state may remain for reopening. These are distinct from mutually exclusive choices within a local explanation group.

## Object-bound disclosure

Treat the object, trigger, explanation and selected state as a unit. Native details/summary works for local disclosure; a shared explanation area needs explicit current-object identity.

| Action | Expected state |
|---|---|
| First entry | Core visual readable, secondary details closed, no surprise focus jump |
| Select A | A selected; A's explanation visible |
| Select A again / close | Selection and explanation cleared |
| Switch to B in the same group | A closes; B replaces it |
| Change method, case or language | Keep valid selections; close invalid explanations |
| Close a parent | Close owned descendants and clear their selected states |
| Return to a branch | Follow an explicit position/state restoration policy |

Independent groups may stay open. A timer must not replace the case or close an explanation someone is reading. Scroll to details only when necessary. Use real buttons, accessible names, aria-expanded/aria-controls, hidden state and correct focus behavior. Restore focus to the trigger if collapsing content contains focus. Pointer scrolling does not grab keyboard focus. Skip links appear on focus.

For linked left-to-right panes, use [workspace controls](workspace-controls.md): draggable boundaries, supporting-pane collapse/restore, narrow-layout adaptation, and state-preserving language/fullscreen controls in the top right. Content-tree disclosure and pane visibility are separate states.

## Motion and continuity

Preserve object identity from overview to detail and between scenes. Transform structure or shift focus while keeping the object recognizable. Do not fade readable text early just because another scene enters the viewport. Expansion may increase scene height; test the top, middle and bottom rather than relying on one intersection ratio.

Choose scanning, matching, decomposition, filtering or comparison motion only when it represents that operation. The presenter controls progression. Avoid wheel hijacking and automatic whole-presentation playback unless explicitly requested.

Loops are optional for repeatable explanations, with a readable end-state pause. Stable tables and comparisons normally stay still. Do not reset user choices. Pause relevant animation while details are being read, offscreen, in a hidden tab, with global motion off or reduced motion enabled. Every animation has a comprehensible static state. Prefer transforms and opacity; avoid repeated layout work and offscreen animation.

## Connectors and selected states

Anchor connections to the relevant object edge or field row. Recompute geometry after resize, expansion or font loading, using one coordinate system. Connector layers do not intercept input. Align small arrows within the text layout, not using spaces or unrelated absolute coordinates.

Selection can use a light surface, subtle lift, shadow or border; follow project style. Leave space for focus and shadow so overflow does not clip them. Lift should not shift neighboring content. Browser comment overlays are not page defects.

## Semantic acceptance

Before implementing a control, write the evidence / operation / output represented by each setting. For the same case, viewers should see the meaningful difference. A stronger check may add evidence while leaving the conclusion unchanged; do not assume it finds more errors. A simulated mechanism is not a live backend request or a measured result.
