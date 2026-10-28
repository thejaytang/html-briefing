# Live presentation, speaker notes and rehearsal

Read this when implementing presenter mode or editable notes, or revising a presentation that already has them. Apply only the capabilities in scope. The bundled canvas starter does not supply a complete presenter system; these lessons guide project implementation and verification.

## One visible part, one matching script

A canvas node can contain several reading parts, such as an overview, a live demo and a design diagram. Give each part a stable identity and associate its script with that identity and language. Derive navigation, rendered content and note lookup from the same content model. Do not use mutable titles or array positions as draft keys.

Follow the part actually visible in the focused viewport, including scrolling within a node. Use a stable reading anchor or visibility rule that accounts for tall parts, sticky headings and nested demo scroll containers. A small scroll must not make the notes flicker between parts. Scrolling inside an embedded tool should retain that tool's script unless a defined demo state needs a different cue.

Reconcile the active part after expansion, collapse, backward navigation, direct links and language changes. If the current part disappears, select a surviving visible part; do not leave the removed part's script on screen. Preserve the editor caret and scroll position while the user is typing. Avoid re-rendering the note editor on every presentation scroll event.

Keep spoken text simple. Place operation cues inline, in the speaker's preferred language, at the point of use. Notes must name controls that exist in the current view. A static process diagram needs narration and pointing cues; it must not inherit instructions to click removed tabs or choose old examples.

## Protect editable drafts across revisions

Treat these as separate states:

| State | Authority and update rule |
|---|---|
| Authored script | Maintained source for the default narration |
| Generated script/embedded notes | Rebuilt from authored source; check for stale copies |
| User-edited draft | User data, often local to one browser; preserve during unrelated changes |
| Currently displayed notes | Verify which source or draft actually won at runtime |

For editable notes, namespace storage by presentation, stable part ID and language. Store the authored revision or content hash alongside a draft when useful to detect drift. A saved draft can shadow an improved source script indefinitely. Source-file equality alone does not prove the visible notes are current.

When source and draft differ, retain the draft and make the choice understandable. Offer a per-part action to use the current authored script with a recoverable backup of the draft. Do not globally clear storage, silently overwrite manual edits, or infer that all non-default text is obsolete. An authorized migration should target a known old revision and back it up first; matching a few words is a fragile substitute for revision metadata. Handle storage errors without falsely reporting a save. Do not claim browser-local drafts synchronize across devices or write back into source files.

During page revisions, audit source notes and generated notes for removed controls, retired part IDs, changed examples and broken transitions. Inspect browser drafts only through permitted access and preserve the user's recent edits. Ordinary layout changes should not rewrite the script.

## Presenter canvas and audience output

Keep the audience view at its intended logical viewport. Adding a notes pane on the speaker's computer must not squeeze the audience composition into a new responsive layout. A scaled preview of the audience viewport can preserve the composition while remaining operable. Map pointer coordinates, text selection and floating menus through the same scale/transform, including within embedded tools.

Synchronize the necessary presentation state: focused node/part, graph expansion, reading position, language and relevant live-demo state. Use an explicit source of control to avoid feedback loops. Keep private notes and edit controls out of audience messages and DOM. Validate incoming window messages and their source/session; never accept arbitrary script or HTML from another window. If mirroring a pointer, distinguish the audience indicator from the local cursor and hide stale indicators on leave or disconnect.

Opening or closing presenter mode should preserve live inputs and mounted demo instances. Define initial demo disclosure once, then respect manual changes. Revealing a tool pane should not implicitly expand every nested field. Re-entering a scene should follow its stated restoration policy rather than resetting the demonstration.

Keep setup hints dismissible. Fullscreen controls need an inset, keyboard-accessible fallback when the browser covers the top edge. A page cannot remove host application sidebars or OS chrome; report an actual host limitation briefly when it blocks the task, without leaving a permanent warning across the presentation.

## Rehearse the rendered route

Use the actual final artifact and the host's permitted browser tools. Test the changed paths with realistic actions, rather than calling controller methods and treating the result as end-to-end evidence.

| Scenario | Observe in presenter and audience views |
|---|---|
| Start, main route and closing | Correct opening/closing script; required sections reachable; audience shows no notes |
| Scroll down/up through a long node | Each visible reading part has its matching script; nested tool scrolling does not jump parts |
| Expand, read, collapse, return | No orphan notes or empty follow-up screens; reading position and demo state remain valid |
| Use a live demo | Actual selection menus, text edits and pane toggles work at preview scale; audience mirrors intended state |
| Edit notes, navigate away, return, reload | Draft persists; caret is stable while editing; save failures are visible |
| Update source with an existing draft | Conflict is discoverable; current-script restore preserves a recoverable draft |
| Resize, fullscreen, Escape, language | Audience composition remains usable; controls reachable; notes retain correct identity/language |

Also rehearse with a fresh notes store without deleting the real drafts. Test at the narrow presenter width and intended audience dimensions. Physical trackpad momentum, two-display placement, offline opening and spoken timing each need their own observation. Record unavailable checks as unverified, and do not bypass a browser access restriction through another server or renderer.

Time the route with actual speech, scrolling and demonstration pauses when timing is part of acceptance. Distinguish source/controller checks, browser rehearsal, physical projection and measured duration in the delivery record. These checks assess a particular artifact; the skill instructions themselves do not prove future presentations correct.
