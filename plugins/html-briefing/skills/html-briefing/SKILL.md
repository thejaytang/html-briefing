---
name: html-briefing
description: Plan, create, revise or review evidence-led HTML project briefings and interactive presentations. Default new presentations to a flow canvas with themed nodes, zoom and long-form reading. Lead storytelling and coordinate Impeccable, UI UX Pro Max, ImageGen, GSAP, optional host Visualize and browser verification; preserve presenter control and verify offline delivery. Use for HTML briefing environment checks, HTML work reports, technical demos and project showcases, not production websites, ordinary text updates or native PPTX authoring.
license: MIT
---

# HTML briefing orchestration

Turn project materials into an explanation a new audience can follow: why the work matters, what was difficult, how the design works, and what the evidence supports. The canonical plugin and lead-skill identifier is `html-briefing`.

## 1. Choose the scope and available capabilities

Read applicable project instructions and current source materials. Find the authoritative content and implementation; fix source files rather than layering patches over generated output. Preserve the user's language, brand, approved content and authorization.

- **Discussion / planning:** inspect materials and propose a narrative; do not build, install or publish.
- **Review only:** inspect and report findings; do not modify the presentation.
- **Create:** use `scripts/new_briefing.py --directory <new-project-directory>` before visual implementation. This copies the bundled canvas template/model and builds the initial HTML. New HTML presentations use this path unless the user explicitly requests another form. Do not infer an exception from the topic, duration, helper preference or a generic request for slides.
- **Revise:** preserve the approved existing mode and implement the scoped edit; do not silently migrate an existing presentation. A small edit does not trigger a new visual-selection round.

Check required tools only when the task reaches them; do not start every briefing with a full setup inventory. Read [environment checks](references/setup.md) if a needed capability is missing or the user explicitly asks to check the environment. For “check environment only” or “只检查环境”, report readiness and stop. Reuse established availability for small edits.

Read [capabilities.md](references/capabilities.md) before selecting helpers. Reuse available skills by capability and user preference; read the actual chosen skill. Never assume a named skill, model or tool exists. Keep third-party installations intact. Check each capability's availability and scope, not every skill on the machine. A skill document does not grant its underlying tool or credentials.

## 2. Establish the narrative and evidence

Determine the audience's existing knowledge, desired understanding or decision, source scope, live versus asynchronous use, language and delivery environment. Before new localized design, explicitly confirm the one-to-three language set and default unless the user already specified them; preserve an existing set for ordinary edits. Read [workspace controls](references/workspace-controls.md) for that question and implementation contract. Ask about duration only when it changes content choices. Infer what the materials already establish.

Read relevant implementation, outputs and test records, and inspect provided images. Use one real case to connect explanation and evidence. Preserve the distinction between implemented, tested, planned and another contributor's work. Do not invent screenshots, performance claims or test outcomes.

Use this argument where appropriate: context and importance → concrete problem → core design → mechanism and verification → result, value and next action. It is not a fixed slide count. Decision briefs may lead with the conclusion. Parallel projects may have separate branches; never fabricate a pipeline between independent systems.

Write a short title outline before visual work. Titles alone should reveal the argument. Keep test method, observation and supported conclusion together. Read [narrative.md](references/narrative.md) when planning or restructuring. Storytelling belongs to this lead: choose an audience takeaway, build a claim-to-evidence argument, choose a suitable narrative shape and make scene transitions explain the next question. Do not delegate this responsibility to a generic writing skill or force a fixed chapter template. Reuse existing project records rather than creating paperwork for a small edit.

For new presentations, use the [flow canvas](references/flow-canvas.md) unless the user explicitly requests another form. Establish the input, desired output, core steps and blockers, then reveal relevant branches. Choose chapter and branch placement for the speaking order: a vertical talk can reveal owned content below its title, while parallel workstreams can use horizontal lanes. The bundled starter uses left-column chapters and rightward content; adapt its layout model for a different approved hierarchy. Focus and zoom remain anchored to the current page. Adapt the argument to the actual material; do not fabricate a process or force this example’s page count. Preserve approved existing designs and explicit alternatives. Key-node navigation is an auto-hiding overlay that focuses existing nodes without changing their expansion state.

## 3. Design scenes and select visual media

Each scene has a clear theme and a main explanatory visual. Inspect existing diagrams and demos before rebuilding them. For timed live talks, use [narrative guidance](references/narrative.md#timed-talks-and-tool-demonstrations) to budget speech, operation and transitions; avoid screens containing only collapsed questions or secondary navigation. The default view includes the core design and conclusion; object-bound expansion reveals implementation details and evidence. Do not hide the solution itself behind a generic “learn more” control.

For each meaningful interaction, define: **audience question → action → change in the main visual → explanation gained**. A parameter must change the represented evidence, operation or output, rather than only card count or color. Use a static comparison when a meaningful transition cannot be defined.

Read [visual-interaction.md](references/visual-interaction.md) before designing or changing visual interactions. For left-to-right panes, support boundary resizing and supporting-pane collapse/restore; keep language and fullscreen/exit in the top-right toolbar. Read [workspace controls](references/workspace-controls.md) for responsive, keyboard, state and language behavior. For quantitative material, read [data-visualization.md](references/data-visualization.md). For image generation or editing, read [imagegen.md](references/imagegen.md) and the Codex system `$imagegen` skill when available; do not bundle or install a duplicate personal copy. Consider imagery during scene design, not as decoration added at the end.

Read [flow-canvas.md](references/flow-canvas.md) before implementing the default mode. Keep camera position/zoom, structural expansion, local disclosure and reading bookmarks independent. Zoom uses 1/4/9 capacity and stays anchored to the currently centered node, including side branches. Double-clicking a page in overview enters single-page focus; interactive controls keep their own actions. Focus fills the stage and allows long content to scroll. Exiting focus shows the page top in overview while retaining its reading bookmark for re-entry. Use [editorial glass page transitions](references/editorial-glass.md) only for an explicitly selected or already approved alternative; do not mix its page-turn controller with canvas gestures.

For every new briefing, follow [visual direction and selection](references/visual-direction.md) before full visual implementation: Impeccable owns fonts, type scale and palette; build 2–3 actual-page directions using the same representative content, show them, and wait for the user’s choice before styling the full briefing. Retain large background-color fields, light text and oversized outline chapter numerals. A choice already made for this creation or an explicit waiver satisfies the selection step; ordinary revisions preserve the approved design. UI UX Pro Max supplies optional focused references, not a fixed theme menu. Keep storytelling and evidence under this lead’s control.

Use an available host Visualize skill for conversation-only mechanism exploration when useful; its output does not replace the rendered HTML alternatives or final offline artifact. Establish the selected typography, spacing, semantic colors, focus states and motion timing in the project’s existing style source.

## 4. Implement the explanation

Reuse existing components and reasonable project architecture. For a new briefing, customize the canvas sources created by the required entrypoint; do not start from a blank HTML page or substitute a helper’s slide template. Add a framework only when state or authoring needs warrant it. Keep content, language, selection state and animation control distinguishable. Start canvas work from the bundled [template and build instructions](references/flow-canvas.md#starter-and-authoring); preserve the tested gesture/geometry behavior while replacing the fictional narrative and layout with the actual project.

Default to presenter-controlled, naturally extending scenes for live use. Asynchronous readers must understand the core argument without narration. Content, typography, palette and narrative remain flexible within the canvas. Another presentation mode requires the user’s explicit request. See [experience.md](references/experience.md) for reusable lessons and overridable defaults.

When adding presenter mode, editable notes, or changing pages that already have notes, read [live presentation and notes](references/live-presentation.md). Keep notes tied to the visible reading part, preserve user drafts, and verify the actual presenter/audience sequence. This is an implementation contract for requested features, not a claim that the starter already provides them.

Use GSAP only when coordinated sequences or shared-object transitions need it. Use generated images for suitable raster subjects; precise labels, data, connections and interactive state remain editable. Write clear titles and explanations directly, preserving evidence and meaning. Ordinary writing, coding, charts and tables do not require an additional skill. Follow the host agent’s existing competence and applicable project rules.

A new standalone local briefing should open offline unless the project specifies otherwise. Choose a single HTML or an entry file with relative assets. Keep generated final assets inside that deliverable. Live-system demos have separate runtime requirements.

## 5. Verify and deliver

Read [validation-delivery.md](references/validation-delivery.md). Run `scripts/check_presentation.py <final.html> --browser-report <report.json>` before delivery, using the [artifact-bound evidence contract](references/flow-canvas.md#creation-and-delivery-gate). Missing, failed or stale evidence leaves acceptance incomplete. For an explicitly requested alternative, add `--alternative-request` with the exact user request and validate that mode; never invent authorization. Define necessary acceptance checks before running them. Inspect the actual final files with the host's permitted browser tools; use an available Playwright skill when appropriate. Static checks cannot prove rendering, motion, Windows behavior or offline runtime operation.

For feedback, diagnose the cause: “confusing” may mean missing context; “busy” may mean competing themes; “pointless animation” may mean no explanatory state change. Correct shared causes while preserving approved facts and design decisions.

In ChatGPT create/revise tasks, deliver a synchronized Site alongside HTML when Sites is available, following [ChatGPT Sites delivery](references/chatgpt-sites.md) and explicit local-only or no-publish constraints. Use one canonical source and reuse the Site identity. Do not treat a local preview as a published Site.

Deliver the entry file or complete resource package, minimal operating instructions and actual validation scope. Mark untested environments and blocked checks explicitly. Do not upload, publish or include private project materials without corresponding authorization. The HTML explanation and the real application's installation are separate deliverables.

For maintenance or provenance, read [experience.md](references/experience.md) and [sources.md](references/sources.md). Ordinary presentation work does not require re-researching the skill ecosystem.

## Bundled skill resolution

This release includes [12 entries](references/bundled-skills.md): this storytelling lead, Impeccable, UI UX Pro Max, Playwright and all eight GSAP modules. ImageGen uses the Codex system skill. Visualize is a supported host companion, not redistributed. Load only relevant helpers: a static chart needs neither GSAP nor image generation, and vanilla HTML needs no framework modules. Keep generic writing/coding and academic publishing suites outside the workflow. Prefer an explicitly chosen existing equivalent. Precise diagrams, charts and tables use native HTML/SVG and the data guidance. All helpers remain subordinate to user scope, evidence integrity and project rules.
