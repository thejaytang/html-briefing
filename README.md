# HTML Briefing

<p align="center">
  <a href="README.md"><img src="assets/lang-en.svg" alt="Read in English" width="132" height="40"></a>
  <a href="README.zh-CN.md"><img src="assets/lang-zh.svg" alt="切换到简体中文" width="132" height="40"></a>
</p>

![HTML Briefing: project evidence, a clear story, an offline presentation](assets/cover.svg)

Turn project materials into an evidence-led HTML briefing with storytelling at its center and a focused visual combination: Impeccable, UI UX Pro Max, ImageGen and GSAP, plus optional host Visualize previews. For technical teams, researchers and practitioners explaining how their work operates and what its results support.

**One entrypoint. Keep your existing skills. Deliver an explanation people can inspect.**

**Version 0.7.2:** Impeccable now owns fonts, type scale and palette. For each new briefing, preview 2–3 actual-page directions and choose before the full presentation is styled. Chapter pages retain large color fields, light text and outline numerals. Chapter titles now form the leftmost vertical column, with each chapter’s content expanding to the right. Zoom anchors, disclosure and reading bookmarks remain independent.

[Install](#1-install) · [Try a request](#3-use-it) · [Download 0.7.2 ZIP](https://github.com/thejaytang/html-briefing/releases/download/v0.7.2/html-briefing-0.7.2.zip) · [Release notes](https://github.com/thejaytang/html-briefing/releases/tag/v0.7.2) · [Capability map](plugins/html-briefing/skills/html-briefing/references/capabilities.md)

The package has a portable root `plugin.json` and retains the supported Codex compatibility manifest. This format choice does not establish cross-host runtime compatibility. The canonical identifier is `html-briefing` (formerly `html-brifing`). The repository, marketplace and lead skill use the corrected name. This is a skill orchestration plugin, not a slide editor or an automatic dependency manager.

## 1. Install

Requires a Codex host with plugin support, file access and an authorized project workspace. A browser is needed to verify the rendered deliverable. The plugin installs 12 skill entries: the lead, three helpers and eight GSAP modules together. Host services and runtime libraries remain separate; the workflow checks them only when needed.

Install the pinned release from GitHub:

```sh
codex plugin marketplace add thejaytang/html-briefing --ref v0.7.2
codex plugin add html-briefing@html-briefing
```

Alternatively, download the [ZIP](https://github.com/thejaytang/html-briefing/releases/download/v0.7.2/html-briefing-0.7.2.zip) and [SHA-256 checksum](https://github.com/thejaytang/html-briefing/releases/download/v0.7.2/html-briefing-0.7.2.zip.sha256), verify the digest, then enter the extracted `html-briefing-0.7.2` directory:

```sh
codex plugin marketplace add .
codex plugin add html-briefing@html-briefing
```

Keep the extracted directory in place for a local marketplace. Start a **new chat** and invoke `$html-briefing` with materials and audience. For environment checks only, say “Use $html-briefing to check my environment only.” There is no mandatory setup inventory.

For a migration from the old name, install and verify the new plugin before removing the old registration. Back up local customizations and retire the old personal compatibility pointer if it would shadow the new skill. See [maintenance](docs/maintenance.md). The old v0.5.0 release remains available under its original plugin identity; it does not contain the canvas mode.

## 2. What is actually included

**12 skill entrypoints ship in this plugin.** Their required references, scripts and license notices are included. Existing personal skills are preserved: your explicitly chosen version wins, otherwise the lead uses the bundled copy.

| Included workflow | Entries | Source and role |
|---|---:|---|
| HTML Briefing | 1 | Jay Tang: storytelling, evidence, scene continuity, integration and delivery checks |
| Impeccable | 1 | [pbakaus](https://github.com/pbakaus/impeccable): main design system and visual review |
| UI UX Pro Max | 1 | [nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): searchable palette, font, chart and interaction references |
| Playwright | 1 | [OpenAI](https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md): browser QA instructions and CLI wrapper |
| GSAP Skills | 8 | [GreenSock](https://github.com/greensock/gsap-skills): core, timeline, scrolltrigger, performance, plugins, utils, react and frameworks; select by need |

[All 12 entrypoints](plugins/html-briefing/skills/html-briefing/references/bundled-skills.md) · [Licenses, sources and package adaptations](plugins/html-briefing/THIRD_PARTY_NOTICES.md)

**Storytelling belongs to the lead.** It identifies the audience takeaway, connects claims to evidence, chooses a narrative shape for the purpose and plans why each scene follows the previous one. Decision briefs, mechanism explanations, progress reports and parallel projects need different structures. The original [business experience](plugins/html-briefing/skills/html-briefing/references/experience.md) remains intact.

ImageGen uses the Codex system `$imagegen` skill; this package does not redistribute a duplicate. If it is unavailable, report that capability gap.

Impeccable owns visual direction, typography and palette; UI UX Pro Max provides optional focused references within that direction; ImageGen supplies useful imagery; GSAP supplies meaningful motion. **Visualize completes this combination through an existing host installation**, for conversation-only exploration and previews. Its original manifest is proprietary, so its source is not in this public package. If a requested chat preview needs it and it is unavailable, suggest the host's official plugin catalog; do not block standalone HTML delivery.

The plugin does not require every helper on every task. Static charts need no GSAP, and vanilla HTML needs no React workflow. Ordinary writing, coding, charts and tables use the agent's competence and project tools. Humanizer, Ponytail and academic publishing suites remain excluded. Tools and runtime libraries are checked when needed, without silent installation.

## 3. Use it

For new work, the first design step is [visual selection](plugins/html-briefing/skills/html-briefing/references/visual-direction.md): 2–3 rendered HTML directions using the same actual chapter/content pages. Choose or request revisions before full styling. A choice already made for this creation or an explicit waiver is respected; ordinary edits keep the existing design. These are agent instructions, not an enforced UI wizard.

Illustrative requests, not claims about measured business outcomes:

| Situation and input | Request | Expected output and success |
|---|---|---|
| A technical project with source notes and test records | “Use $html-briefing to make a 10-minute offline HTML briefing for colleagues unfamiliar with this project.” | Context, design, mechanism and observed results; final files opened and checked offline |
| An existing briefing with confusing interactions | “Use $html-briefing to fix the nested explanations in this HTML. Keep the narrative and visual direction.” | Scoped repair; selecting, switching and collapsing affected objects leaves no stale details |
| A concept needs a visual explanation | “Use $html-briefing to explain this mechanism with an ImageGen illustration and editable labels.” | Inspected conceptual image, precise page labels and packaged assets; missing generation tools are disclosed |
| A decision is still being discussed | “Use $html-briefing to review these materials and propose an outline only.” | An evidence-bound outline; no implementation, installation or publication |

Open [the flow-canvas example](examples/flow-canvas.html) to explore zoom, three perspectives and long-form reading. Build or adapt it using the [canvas guide](plugins/html-briefing/skills/html-briefing/references/flow-canvas.md).

Open [the fictional offline example](examples/offline-routing.html) directly in a browser. It demonstrates object-bound explanations; it does not connect to a real scheduler.

## 4. How the combination works

![Workflow: evidence and audience enter the lead skill; relevant installed helpers produce a shared design; actual final files are verified](assets/workflow.svg)

The lead skill establishes the audience, argument and evidence. It chooses the relevant available helpers, keeps their outputs consistent, and verifies the final briefing. The illustration describes the intended workflow; it is not an automatic execution engine.

| Capability | Bundled helper / host capability | What it contributes |
|---|---|---|
| Narrative | The lead’s storytelling guidance | Audience takeaway, supported argument and scene continuity |
| Visual system | Impeccable | Consistent hierarchy, layout, typography and states |
| Design references | UI UX Pro Max | Targeted palette, typography, chart and interaction choices |
| Data and tables | Native HTML/SVG and existing project chart tools | Defined metrics, faithful charts and reconciled tables |
| Raster visual expression | ImageGen | Scenes, objects, illustrations, image edits and cutouts |
| Precise relationships | Native HTML/SVG and the bundled diagram guidance | Editable labels, architecture, field mapping and interactions |
| Meaningful motion | Relevant GSAP modules | Object continuity and coordinated state changes |
| Conversation preview | Host Visualize when available | Explore a mechanism or interaction before final implementation |
| Verification | Host browser tools or Playwright | Actual rendering, interactions and delivery checks |

Missing optional helpers use documented baselines. An unavailable required browser or image-generation tool remains an explicit gap. A skill file alone does not provide a model, runtime, credentials or service access. No silent paid ImageGen API fallback.

## 5. Experience built into the workflow

- Give unfamiliar audiences the business context before implementation detail.
- Keep the core solution visible; attach secondary explanations to their objects.
- Make controls change evidence, operations or output, not just decoration.
- Preserve identity across scenes; correctly clear nested disclosure and selection.
- Show how a test was done beside what it observed and what that supports.
- Check the moved/extracted final package; a development server or a Mac screenshot does not prove offline Windows acceptance.

[Distilled experience](plugins/html-briefing/skills/html-briefing/references/experience.md) separates these transferable lessons from optional title styles, navigation and motion preferences. No private business data or project screenshots are included.

New presentations default to [flow canvas](plugins/html-briefing/skills/html-briefing/references/flow-canvas.md): input/output, main steps, blockers, branches and summary. Themed nodes may contain long content. Pan, 1/4/9 zoom, structural disclosure and reading bookmarks stay independent; zoom follows the centered node. Overview shows the page top, while returning to focus restores reading. The bundled starter is dependency-free and editable. Explicit alternatives and approved existing designs are preserved; [editorial glass](plugins/html-briefing/skills/html-briefing/references/editorial-glass.md) remains optional.

The [workspace controls](plugins/html-briefing/skills/html-briefing/references/workspace-controls.md) guidance supports draggable pane boundaries, supporting-pane collapse/restore and narrow previews. Before new localized design, the lead asks for up to three languages and a default. A compact segmented language switch and fullscreen/exit share the top-right toolbar; Chinese retains English professional terms. These are implementation requirements interpreted by the agent, not a bundled UI library.

Canvas navigation is an auto-hiding top overlay for key-node focus, with language and fullscreen at the right. Expansion and folding happen inside content. There is no persistent branding header, status footer or zoom toolbar. Native trackpad feel and platform behavior still require per-artifact validation.

For create/revise work **in ChatGPT**, [matching Sites delivery](plugins/html-briefing/skills/html-briefing/references/chatgpt-sites.md) uses the available host Sites workflow alongside HTML, from the same canonical source. Existing Site URLs and audiences are preserved; a new Site starts private. Explicit local-only or do-not-publish instructions take precedence. Unavailable Sites support is reported as a gap; no ChatGPT plugin-installation or runtime-compatibility claim is implied.

## 6. Fit, compatibility and limits

Use this for project briefings, research explanations, technical demos and presenter-controlled HTML reports. Choose a production-web workflow for applications, a native presentation workflow for editable PPTX, or ordinary writing for a text-only update.

| Surface | Scope |
|---|---|
| Codex on macOS | Release target; actual installation and package evidence is recorded in the validation report |
| Windows / Linux | Portable text/resources, but native installation and rendered acceptance are not verified |
| Other skill hosts | No compatibility claim; host tooling and plugin format require adaptation/testing |
| GSAP and bundled helpers | Skill files included; runtime/service requirements remain separate, and not all combinations are exercised |
| ImageGen | Uses the Codex system skill and available image tool; no duplicate bundled copy |
| Offline output | A production requirement for new standalone local briefings, verified per artifact; plugin installation itself may need network access |

The workflow is interpreted by the agent. It does not guarantee deterministic routing or universally correct output. Instructions are primarily English; the detailed delivery checklist is retained in Chinese. Both README languages describe the same capabilities; this does not establish bilingual runtime testing.

## 7. Development, evidence and sources

```sh
python3 scripts/check_package.py
python3 -m unittest discover -s tests
node tests/canvas-model.test.cjs
```

The package checker and Python tests use Python 3.10+ standard library; canvas model checks additionally require Node.js. The generated HTML has no runtime package dependencies. The optional lockfile contains PyYAML for the official skill metadata validator. Structural checks do not prove browser behavior. Read [AGENTS.md](AGENTS.md), [current state](PROJECT_STATE.md) and [release validation](project-support/release-verification-0.7.2.json) before contributing. Reproduction reports should identify the scene, state, viewport and input without private material.

[Sources and optional upstreams](plugins/html-briefing/skills/html-briefing/references/sources.md) distinguish inspiration, recommended helpers and host documentation. Redistributed skills retain upstream licenses and credits; omitted suites are not installation recommendations.

[MIT](LICENSE), copyright 2026 Jay Tang, covers this repository's original guidance, artwork and checker. Bundled skills retain their MIT or Apache-2.0 licenses as listed in [third-party notices](plugins/html-briefing/THIRD_PARTY_NOTICES.md); libraries and services keep their own terms. [Issues and suggestions](https://github.com/thejaytang/html-briefing/issues) are welcome.
