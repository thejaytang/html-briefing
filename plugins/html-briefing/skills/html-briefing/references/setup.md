# Environment checks when needed

Normal use starts with the briefing task, not a full inventory. Check the tool needed for the current step. Read this reference for an actual capability gap or an explicit environment-check request; report only relevant available, missing or unknown capabilities.

- Design: Impeccable guidance and launcher are included. Its platform engine is separate; use its documented direct-context fallback if unavailable. Do not enable hooks or install an engine as a check side effect.
- Design references: UI UX Pro Max includes searchable local data and scripts; Python is needed for its search. Use it only for a concrete reference need.
- Images: use the Codex system `$imagegen` skill and its available tool/service; no duplicate personal ImageGen skill is bundled. No silent paid API fallback or credentials in chat.
- Browser verification: use a permitted host browser tool; the bundled Playwright wrapper is an alternative requiring Node/npx and a browser. Do not install global tools as a check side effect.
- Sites: For ChatGPT create/revise delivery, inspect the actual host Sites skills and tools when syncing is due. Read [ChatGPT Sites delivery](chatgpt-sites.md); unavailable hosting is an explicit gap, not a reason to abandon independent HTML delivery.
- Motion: All eight GSAP guidance modules are included. Only when the scene benefits from coordinated motion, add the JS runtime within the authorized project's isolated dependencies and package it locally for offline use. Simple transitions need no GSAP.

Writing, coding, charts and tables use the agent's normal abilities and project tools. Do not recommend a supplementary skill suite. Only load GSAP modules relevant to the actual project. Visualize is an optional host companion for conversation previews; if that preview is requested and the skill is missing, suggest the host’s official plugin catalog without installing automatically. Standalone HTML delivery does not depend on Visualize.

For an explicit package check, verify [the 13 bundled entries](bundled-skills.md). Missing packaged files call for repair/reinstallation of this plugin, not separate helper downloads. Distinguish file presence, exposure in the current chat and actual exercised functionality. A new chat may be needed after an update.

Preserve existing personal skills. Prefer an explicitly selected existing equivalent; otherwise use the bundled copy, resolved from its actual directory. Do not overwrite or standardize other installs.

Reuse checks until relevant conditions change. Environment-only requests finish with the result; they do not start a presentation or install anything. Do not create a global setup flag.
