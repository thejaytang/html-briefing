# 1. Workspace and delivery update

Date: 2026-10-02. Scope: update the original lead skill, preserve all twelve bundled helpers and prior local editorial-glass rules, prepare a distributable 0.6.0 candidate. No GitHub push, tag or release has been performed for this candidate.

## 1.1 Implemented guidance

- Linked left-to-right panes: draggable and keyboard-adjustable boundaries, usable width bounds, collapse/restore, focus recovery and narrow-layout adaptation.
- Language setup: explicitly confirm one to three languages and a default before new localized design; use already-supplied choices and preserve established sets for ordinary edits. Chinese keeps English professional terminology.
- Viewing toolbar: compact segmented language controls and enter/exit fullscreen together at the top right. Fullscreen follows actual browser state and handles Escape or rejection.
- Professional communication and narrative reports: persistent top navigation derives from the title outline, with one chapter model for headings, labels, scenes and current state. Learning atlases and tool workspaces do not inherit report navigation.
- ChatGPT create/revise delivery: match HTML with a Site from the same source when actual Sites capabilities are available; reuse identity and audience, honor local-only instructions and distinguish successful publication from a preview.

Canonical instructions: [workspace-controls.md](../plugins/html-briefing/skills/html-briefing/references/workspace-controls.md) and [chatgpt-sites.md](../plugins/html-briefing/skills/html-briefing/references/chatgpt-sites.md), routed from the lead skill and applicable references.

## 1.2 Validation scope

Necessary local-preparation acceptance contains 22 items: the 16 existing automated tests and six checks below. Repeated runs count once.

| Check | Result | Evidence |
|---|---|---|
| Existing mutation/runtime tests, 16 cases | PASS | `python3 -m unittest discover -s tests`; final candidate source extract, all 16 passed |
| Package structure, resources, manifest versions and upstream hashes | PASS | `scripts/check_package.py`, including an isolated extract |
| Official skill frontmatter validation | PASS | Official `quick_validate.py` reports valid |
| Installed lead synchronization | PASS | Ten changed/linked lead files byte-compared with maintained source; originals backed up; registration and installed plugin version remain 0.5.0 |
| Rendered bilingual docs and images | PASS | GitHub Markdown rendered for local inspection; both language buttons exercised; covers and workflow inspected; 390px narrow view has no page overflow |
| Public scope, claims and licensing | PASS | Exact intended file list reviewed; no credentials or personal machine paths found; MIT originals and third-party notices preserved; guides claim requirements rather than a bundled runtime |
| Candidate ZIP integrity and safe extraction | PASS | Safe relative paths; extracted file bytes match the reviewed source; SHA-256 saved beside the draft ZIP |

The 0.6.0 candidate is a source/documentation release proposal. This does not prove automatic model dispatch, a new plugin-detail UI refresh, three-language runtime execution, ChatGPT plugin installation or native Windows/Linux behavior. Target artifacts still require their own browser acceptance.

The local installation is an explicitly requested lead customization, not a new published version. A new chat may be needed to load changed instructions. Normal marketplace updates can replace that customization; use a published version for a durable distribution update.

## 1.3 Publishing boundary

The previous public v0.5.0 release and archive remain unchanged. Publishing 0.6.0 requires authorization for the existing `thejaytang/html-brifing` repository. The draft includes prior local editorial-glass guidance; it contains no business screenshots or private source materials. A public release must be rebuilt from the exact committed/tagged tree and verified through the downloaded archive and checksum.

Local-preparation tests: PASS, 22/22. GitHub publication and new-host runtime acceptance are outside this authorized preparation scope.
