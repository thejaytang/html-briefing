# Workspace, language and viewing controls

Use this guidance for linked panes, multilingual briefings or a fullscreen view. Keep the existing visual direction; a single-column explanation does not need artificial panes.

## Chapter navigation for professional briefings

For the default flow canvas, use the auto-hiding key-node overlay defined in [flow-canvas.md](flow-canvas.md). It focuses existing nodes at single-page scale and never opens or folds branches. Keep language and fullscreen on its right. Reveal on hover and keyboard focus without reserving stage height; also provide an inset click/tap target reachable when browser chrome covers the top edge. For an explicitly selected linear report, persistent top chapter navigation is an option. Derive its order from the actual title outline and argument, rather than a fixed generic menu. A learning atlas, searchable reference or tool workspace does not inherit this requirement; preserve the navigation suited to that task.

- Use one canonical chapter/scene model for the title outline, rendered sections, navigation targets, active state and previous/next controls. Each chapter has a stable ID, full heading and short localized navigation label. Do not maintain a separate hand-written menu or infer all chapters from every `h2`/`h3`.
- The labels summarize the report's main themes in their narrative order. One navigation chapter may own several scenes; every scene has an explicit chapter membership. Do not create a tab for each detail, force a fixed number of chapters or invent a pipeline between independent projects.
- Put chapter links in the upper navigation band and keep language plus fullscreen/exit together at its right edge. Keep the toolbar outside transformed scene layers. On narrow screens, wrap or compact chapter navigation with an accessible overflow/menu treatment while preserving the viewing controls.
- Use semantic links or correctly labeled buttons with stable targets and visible focus. Use `aria-current` for the current chapter. Direct navigation, reading/page changes, URL links, browser history, resizing and language switches must agree on the same chapter state; offset anchors so a sticky header does not hide a title.
- Preserve meaningful section content and reading position. An active highlight must follow the actually displayed chapter after a transition finishes, not only the last button clicked.

Acceptance: traverse every chapter in order and jump backward; verify each localized label reaches its assigned chapter; enter by a direct URL and test refresh/back; inspect long labels, narrow/short windows and fullscreen. A navigation instruction alone does not establish that an untested artifact is stable.

## Resizable and collapsible panes

For a left-to-right workspace, let readers drag the boundaries between adjacent panes and collapse supporting panes to give the main visual more room. Keep resize and collapse controls beside their own boundary or heading, separate from content-tree disclosure.

- Define usable minimum and maximum widths. Clamp widths to available space after window resize, zoom or fullscreen changes; do not let a narrow preview produce inaccessible horizontal overflow.
- Use a visible grip and a generous pointer/touch hit area. Pointer capture keeps a drag stable beyond the grip; release on pointer-up or cancellation. Avoid selecting text while dragging.
- Provide a focusable separator with `role="separator"`, `aria-orientation="vertical"`, an accessible name, `aria-controls` and current/min/max values. Arrow keys resize it; Home/End reach its bounds. A non-drag control must remain available.
- Collapsing a pane leaves a clear restore button or compact rail. Keep its last useful width, content, scroll position, selected object, search and language. Hidden content must not remain in the tab order; move focus out before hiding it.
- Keep the primary content available. At narrow widths, replace side-by-side panes with a drawer or a vertical reading order rather than forcing tiny columns. Disable irrelevant vertical separators in that layout. Local preferences may persist, but do not claim they synchronize between devices.
- A reset-layout action should restore useful default widths and reveal supporting panes.

Check drag in both directions and at bounds, keyboard resizing, collapse/restore in each order, narrow preview, long terms, localization, window resize and fullscreen transitions. The selected concept must still identify its explanation.

## Confirm languages before localized work

Before designing a new briefing or adding/changing its language set, explicitly ask which **one to three languages** the user needs and which is the default. For example: "Which languages should this briefing support, up to three, and which should open first?" If the user already supplied those choices in the current task, use them without asking again. Continue independent source inspection while the answer is pending; do not silently choose languages or begin localized design before the required answer.

For an ordinary edit to an existing briefing, preserve its established language set. If more than three languages are requested, ask the user to choose the up-to-three set; do not silently discard one.

## Compact language switch

Place a compact segmented language button group in the **top-right viewing toolbar**, beside fullscreen. Support one, two or three configured languages; omit a redundant switch for a single-language artifact unless the user requests a language entry; that entry must accurately report the single configured language, not offer an untranslated language. Preserve the approved style: a lightly bordered group, small rounded options and a clear filled active option. Use native buttons, self-language labels such as 中文 / EN / 日本語, an accessible group label and `aria-pressed` for the active choice. Do not use national flags as language names.

Switch all audience-facing content, captions, navigation, controls, tooltips, errors and accessible names. Set the document `lang` and direction when applicable. Keep selection, expanded branches, search, reading position and pane configuration; persist only the language preference when useful. Chinese content retains the original English professional terminology alongside its Chinese explanation. Other languages follow the agreed terminology policy.

Test all configured languages, including hidden explanations and long labels. README language links are separate from this in-page control and do not prove runtime localization.

## Fullscreen beside language

Keep **enter fullscreen / exit fullscreen in the same top-right toolbar** on desktop and narrow layouts. Use one button whose icon, accessible name and pressed state follow the actual fullscreen state. Keep an exit control visible in fullscreen, and allow the browser's Escape behavior.

Use the browser Fullscreen API from a user action. Listen for `fullscreenchange` so Escape and other browser exits update the UI; handle a rejected request and restore focus without claiming success. When the host disallows fullscreen, retain a usable page and explain the unavailable action. A larger CSS layout is not native fullscreen. Pane widths must remain usable after entering or leaving it.

Implementation references: [WAI window splitter pattern](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/) for semantics and keyboard behavior; [MDN Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API) for browser state and availability. Verify the target host instead of assuming API support.


## Presenter and audience views

When requested, use the [live presentation contract](live-presentation.md) for separate audience output, a scaled presenter canvas, editable notes and visible-part synchronization. Fullscreen, pointer mirroring and physical extended-display behavior require separate verification; adding a notes pane does not establish those capabilities.
