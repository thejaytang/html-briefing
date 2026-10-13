# ImageGen as part of scene design

For Codex, use the system `$imagegen` skill for raster images, edits, cutouts and visual variants when the subject benefits from generated imagery. This plugin intentionally omits a duplicate personal ImageGen skill. If the host does not expose a system image skill, explain the gap. Do not install or invoke a duplicate personal copy when the system skill is available.

## Choose what to generate

Good subjects include a business setting, a conceptual illustration, an object render, an explanatory cutaway, a visual metaphor and adaptation of supplied images. Do not automatically generate an image for every scene.

Keep exact data, editable field labels, architecture connections and interactive states in HTML/SVG or data-driven graphics. For a hybrid visual, generate the subject/background and overlay precise labels and interaction in the page. Do not substitute a code-drawn placeholder for an explicitly requested raster image. If the requested generation tool is missing, explain the gap before changing the medium.

Real screenshots and test artifacts remain real evidence. Never create a fake product screen, runtime log or performance chart and present it as observed work. Label concept images and mockups where their status affects interpretation.

## Handoff to the image skill

Describe the scene question, intended asset role, subject, composition, crop/aspect needs, palette, negative space for page labels, background/transparency, exact text if unavoidable and things to preserve. For each input identify whether it is a reference, edit target or inserted material. Inspect local edit targets before editing.

Prefer the built-in image tool when available. A skill file does not provide the tool. If unavailable or failed, disclose that an API/CLI route may require credentials and cost; only use it with explicit authorization. Never ask for a secret in chat or silently switch models/routes. Follow the installed skill's current tool contract.

## Integrate and inspect

Inspect the generated result for meaning, composition, inaccurate text, misleading details, style and edit invariants. Make targeted revisions. Preserve source assets and save replacements non-destructively unless replacement was requested.

Copy the selected final asset into the deliverable's own assets directory, reference it relatively and provide an appropriate text alternative. Do not leave a project dependent on the host's generation cache, an absolute local path or a temporary URL. Preserve alpha when transparency is requested.

Inspect it inside the actual scene, including small/short windows, text overlays and offline viewing. Record the tool route and prompt as project production evidence when applicable, outside the audience-facing page. Report final saved assets according to the chosen image skill.
