# Bundled skill sources and notices

This plugin redistributes the following skill snapshots. Root MIT covers original HTML Briefing code and guidance; third-party files retain their listed licenses. Upstream names indicate provenance, not endorsement. Runtime services/libraries are separate.

| Skill | Upstream | Snapshot | License |
|---|---|---|---|
| [gsap-core](skills/gsap-core/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-core/LICENSE) |
| [gsap-frameworks](skills/gsap-frameworks/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-frameworks/LICENSE) |
| [gsap-performance](skills/gsap-performance/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-performance/LICENSE) |
| [gsap-plugins](skills/gsap-plugins/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-plugins/LICENSE) |
| [gsap-react](skills/gsap-react/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-react/LICENSE) |
| [gsap-scrolltrigger](skills/gsap-scrolltrigger/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-scrolltrigger/LICENSE) |
| [gsap-timeline](skills/gsap-timeline/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-timeline/LICENSE) |
| [gsap-utils](skills/gsap-utils/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-utils/LICENSE) |
| [impeccable](skills/impeccable/SKILL.md) | [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 4.4.0; engine 0.1.6 | [Apache-2.0](skills/impeccable/LICENSE) |
| [playwright](skills/playwright/SKILL.md) | [https://github.com/openai/skills](https://github.com/openai/skills) | local snapshot 2026-09-29 | [Apache-2.0](skills/playwright/LICENSE.txt) |
| [ui-ux-pro-max](skills/ui-ux-pro-max/SKILL.md) | [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | local snapshot 2026-09-29 | [MIT](skills/ui-ux-pro-max/LICENSE) |

## Package adaptations

Source and packaged hashes and adaptations are in [bundle.json](bundle.json). This release reuses the reviewed 0.3.1 snapshots for the selected visual helpers. UI UX Pro Max and Playwright examples resolve their selected skill directory. ImageGen uses the Codex system skill and is not redistributed here. UI UX Pro Max’s long workflow remains a linked reference. All eight GSAP guidance modules are available, without bundling the JavaScript runtime.

Impeccable includes its [Apache license](skills/impeccable/LICENSE), [upstream notices](skills/impeccable/NOTICE.md) and [modern-screenshot MIT notice](skills/impeccable/scripts/modern-screenshot-LICENSE). Engine binaries remain separate.

Visualize is an optional host companion in the workflow. Its original manifest declares Proprietary; its source/assets are not copied. Generic writing/coding and academic suites are not shipped; prior tagged releases preserve their earlier attribution.
