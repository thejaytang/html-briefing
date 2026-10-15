# Installation and maintenance

The canonical plugin, marketplace and lead-skill identifier is `html-briefing`. The former spelling was `html-brifing`. The GitHub repository is `thejaytang/html-briefing`; install the pinned `v0.7.4` release.

## Install from GitHub

```sh
codex plugin marketplace add thejaytang/html-briefing --ref v0.7.4
codex plugin add html-briefing@html-briefing
```

The [release](https://github.com/thejaytang/html-briefing/releases/tag/v0.7.4) includes the ZIP and SHA-256 checksum. The ZIP contains a marketplace root, not only the nested plugin. Choose either Git or ZIP installation. If a marketplace with this name is already configured, inspect its source first; to switch sources, remove only that marketplace registration before adding the new source. This does not authorize deleting working files.

## Local installation and name migration

From the extracted repository root, run `codex plugin marketplace add .`, then `codex plugin add html-briefing@html-briefing`. Keep this local source directory in place. Verify the installed manifest, version, lead skill and canvas assets before retiring the old installation. Start a new chat for fresh discovery; a running chat can retain its old skill catalog.

For an explicitly authorized rename, preserve a backup of the old installed plugin and personal compatibility entry. After new-install verification, remove only `html-brifing@html-brifing` with the host CLI and remove only its old marketplace registration. Retire the old personal compatibility pointer outside skill-discovery roots if it conflicts with the new `html-briefing` entry. Do not alter unrelated skills or plugin permissions. This procedure is not an automatic installation hook.

Do not change old release archives, tags or evidence records. Older links and tags belong to their historical versions. New releases require authorization and remote verification. Do not hand-edit cache files or marketplace registries to simulate installation.

## Creating and checking presentations

From the lead skill directory, run `python3 scripts/new_briefing.py --directory <new-directory>`. Customize the copied template/model and rebuild with `scripts/build_flow_canvas.py`; never edit installed cache files. Before delivery run `scripts/check_presentation.py <final.html> --browser-report <report.json>`. The [canvas guide](../plugins/html-briefing/skills/html-briefing/references/flow-canvas.md#creation-and-delivery-gate) defines evidence, exit codes and explicit user-requested alternatives. Missing evidence is not a pass.

## Source and validation

The maintained entrypoint is `plugins/html-briefing/skills/html-briefing/SKILL.md`. Its flow-canvas reference routes to the editable template, geometry/gesture model and builder. Adapt project copies, not the installed cache. The original fictional case is an example, not required business content.

Run `python3 scripts/check_package.py`, `python3 -m unittest discover -s tests`, `node tests/canvas-model.test.cjs`, and `node tests/canvas-double-click.test.cjs`. Build the example with the skill's `scripts/build_flow_canvas.py`. Inspect the extracted final HTML in the intended browser and offline. Structural checks do not establish browser behavior, physical trackpad acceptance, cross-platform support or fresh-chat dispatch.

The bundle remains one storytelling lead plus eleven helpers (12 entries total). Select helpers by need and preserve explicitly chosen equivalents. Keep all upstream notices and per-file hashes in `bundle.json`; ordinary canvas work does not alter imported helper snapshots. Visualize and Sites remain host-provided capabilities. ImageGen uses the Codex system skill. Runtime tools and any service access are separate from skill installation.
