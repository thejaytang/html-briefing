# Editorial titles and vertical glass snapping

## 1. When to choose this treatment

Use this optional treatment when already approved for the artifact or when the user requests editorial serif headings, translucent pages that rise over one another, liquid glass, or whole-page transitions. An explicit alternative wins. Preserve an established artifact unless its redesign is requested. A long reference document or dense dashboard may work better with continuous reading. The material and motion must be implemented visibly; naming a glass preset without rendering the effect does not satisfy it.

Recognize requests such as "editorial glass", "large serif titles with page snapping", "编辑式标题", "向上像透明玻璃一样叠上去" and "整页吸附". Record the selected treatment in the project's existing design source. This reference defines the reusable design; it supplies no business content, fonts or tested presentation runtime.

New presentations default to [flow canvas](flow-canvas.md). Do not apply this preset’s vertical sheet controller to that mode.

## 2. Title composition

- Give each scene a short, meaningful title that states its theme or supported conclusion. Use one or two lines where the language and viewport allow, with the line break at a phrase boundary. Do not force a colon, slogan, fixed word count or manual break at every size.
- Pair an expressive serif display face with a plain sans-serif body and controls. Instrument Serif with Varta is one starting combination; use licensed, locally packaged fonts or deliberate system fallbacks. The skill does not include those font assets.
- Keep the main title in dark ink and optionally accent one meaningful phrase in the project's blue. The wording must remain understandable without colour. Reserve the strongest size contrast for the title, main evidence and supporting explanation.
- Give the scene title the available reading width, with its explanatory lead below. Use side-by-side evidence only for peer comparisons or a clear sequence. A wide screen does not help a heading trapped inside a narrow grid column.
- Start around 48 to 82 CSS pixels for a cover title and 36 to 58 for chapter titles, using responsive sizing. These are tuning ranges, not acceptance criteria. Choose line height from the actual glyphs; never copy tight Latin leading to Chinese. Check long titles, accents and fallback fonts for clipping.
- Adapt Chinese typography with a suitable Song-style title face and readable sans-serif body. Reflow after changing language; retain the current case and chapter. A language switch need not translate evidence that the project requires to remain in its source language.

Illustrative title: "Keep the evidence in view." followed by an accented "Explain what changed." Use this composition only where that is the scene's actual argument.

## 3. Reading order before page effects

For explanatory briefings, start with the scene's premise or conclusion, then its grouped supporting points, then the example or evidence and a short takeaway when useful. The title should identify the whole; subheadings identify its parts. Keep a group's heading above its details rather than stranded in a narrow adjacent column. Use one primary reading path from top to bottom, with a stable title position across pages.

Columns imply parallel items. Give actual process steps an ordered list or explicit sequence, preserving DOM and visual order when they wrap. Put pattern/outcome choices before the selected explanation; distinguish secondary cross-reference tables from the main argument. A summary should close the page without competing with its opening title.

When text wraps despite apparent space, inspect its parent column, `max-width`, explicit breaks, balancing and inherited breakpoint rules before reducing type size. Release unnecessary width caps and forced breaks. Retain a comfortable measure for long body text; never solve wrapping with global `white-space: nowrap` or by shrinking the whole presentation. Check the intermediate width where a multi-column process first wraps, not just desktop and mobile extremes.

## 4. Pages, material and direction

Each scene occupies at least the available presentation viewport between stable navigation controls. Fit the narrative by splitting overloaded scenes or letting long content extend; never shrink the whole page to force it into a fixed canvas.

Use a quiet pale background and translucent light sheets with a restrained border and shadow. Text and evidence panels need enough opacity to remain legible when another layer is behind them. Use a restrained, static backdrop blur on the incoming translucent sheet and stable navigation where supported. Animate translation and opacity, with a slight outgoing-sheet scale (around 1 to 0.97 as a starting point) to establish depth. Avoid animating a full-page blur radius or distorting text. Use an opaque readable fallback if backdrop filtering is unavailable.

Forward progression brings the next sheet upward over the current sheet. Reversing the gesture lowers it to reveal the previous sheet. A scroll-linked version follows native scroll position and settles at a complete page boundary. A discrete gesture version may use a short native Web Animation to move between sheets after an edge gesture; keep ordinary reading inside each sheet native. Both versions require a visible intermediate overlap, not just a jump between selected sections. Do not substitute a horizontal carousel. Keep the outgoing evidence readable until the incoming sheet covers it; avoid fading it to nothing early.

## 5. Implement with native scrolling first

Use one native vertical scroller and CSS scroll snapping as the starting point. For this page-by-page treatment, `scroll-snap-type: y mandatory`, full-height snap areas, `scroll-snap-align: start` and `scroll-snap-stop: always` are useful starting settings. Validate the resulting behaviour with actual content and input devices.

Long content must have a free reading interval before the next page transition. In a stacked-stage implementation, each page's scroll allocation can be the viewport height plus that page's content overflow. Native scrolling maps first to reading the overflow, then to raising the next sheet. Recalculate after resizing, font/image loading, disclosure and language changes, preserving the selected page and valid reading offset.

Add a sticky stage and scroll-linked transforms only when the requested layering needs them. Drive translation and restrained opacity from native scroll position; batch visual updates through animation frames. CSS alone is enough for ordinary snapped sections. This preset does not require GSAP or a new framework.

Keep the following interaction invariants:

- Prioritize reading over page navigation. A gesture beginning inside a long page belongs to that page: stop at its top/bottom and absorb the remaining wheel, trackpad or touch inertia. Reaching an edge must not turn the page in the same gesture. Only a fresh outward gesture begun at that edge may enter one adjacent page; upward navigation enters the previous page at its bottom.
- Keep native scrolling and snapping where practical. CSS snap-stop alone does not distinguish content reading from page navigation. If the implementation shares one scroll track, constrain each gesture to its reading interval or one adjacent transition. Detect wheel release from an input-quiet interval (around 200–250 ms as a tuning starting point), not a fixed post-animation lock. A touch contact and its released inertia remain one gesture until a fresh contact.
- Reverse input must resume reading immediately within the current interval. Do not block all input with a cooldown. Preserve nested-widget scrolling, horizontal gestures and pinch/zoom; a nested widget reaching its edge must not leak the same gesture into page navigation. Explicit chapter/previous/next controls remain immediately usable and reset stale gesture bounds.
- Clamp keyboard reading steps at the content edge; held-key repeats must not spill into page turns. Recalculate gesture bounds or reset them after reflow, explicit navigation and direct scrollbar input. Keep the footer limited to page controls and progress. Do not add persistent scrolling instructions by default; add an explanation only when the user requests it or a demonstrated discoverability problem requires it.
- Native snapping owns settling. Add a `scrollend` correction only if the actual implementation can rest between pages. A debounced fallback for hosts without that event must not be an input lock or pull a reader away from a long page's reading interval.
- Put chapter, language and full-screen controls outside transformed page layers. Decorative layers cannot intercept input. Limit scaling to the outgoing inactive sheet during the transition; restore unit scale at rest. Do not mix transformed and untransformed coordinate systems for hit testing.
- Expose one current scene to keyboard navigation and assistive technology. Keep moving, overlapping scene controls from receiving accidental clicks. A measured-but-inactive sheet may need visibility and inert state rather than removal from layout.
- If the design maintains both scene and main scroll offsets, synchronize focus-driven scrolling. Distinguish renderer-authored updates from external changes so a delayed scene scroll event cannot rewind newer native input. Prefer a single scroll position when it can deliver the design.
- Direct chapter navigation, previous/next controls and keyboard shortcuts must use the same page geometry. Preserve normal behaviour inside forms, tabs, disclosures and nested scrollable regions.

## 6. Reduced motion and verification

With reduced motion, show a stable selected page and use instant positioning or a simple non-moving transition. Retain all content, navigation and long-page reading. Print should return to ordinary document flow with every scene visible.

Check the finished artifact through the permitted browser route:

1. Capture and inspect at least one intermediate frame: the incoming sheet must visibly overlap the outgoing sheet, with readable glass material and restrained depth. Short forward and reverse swipes settle at a whole page; rapid reversal remains responsive. Test trackpad inertia separately from a mouse wheel or touch input when those devices are available.
2. Read a long scene at the top, middle and bottom. A strong downward gesture from the middle stops at the bottom, and its decaying tail stays there; a fresh outward gesture then advances exactly one page. Repeat upward from the middle and confirm a fresh gesture returns to the previous page’s bottom. Reverse before release and verify immediate response.
3. Check nested scroll areas, horizontal gestures, zoom, repeated arrow keys, direct navigation during inertia and reflow after a language/content change. Use browser interaction evidence for the actual scroll boundary; synthetic event or geometry checks supplement it. Physical trackpad/touch feel requires testing on those devices and must not be inferred from screenshots.
4. Chapter, language and full-screen controls respond at their visible positions before and after resizing and full-screen changes. The same full-screen button enters and exits.
5. Tab focus reaches offscreen controls without jumping back; widgets keep their normal keys. Language, font and content changes preserve the selected scene.
6. Inspect title wrapping, Chinese fallbacks, contrast and overlapping sheets at wide, intermediate, narrow and short viewports. The premise, supporting groups and takeaway must remain identifiable in that order. Exercise reduced motion and inspect the final offline package.

Static checks can verify instructions, geometry calculations and state decisions. They cannot establish native snap feel, frame rate, visual fit or hit alignment. Record blocked browser checks as incomplete. A user's approval of this visual direction supports reusing the design; it does not certify a runtime across browsers or devices. Follow [validation-delivery.md](validation-delivery.md) for the artifact's remaining acceptance checks.
