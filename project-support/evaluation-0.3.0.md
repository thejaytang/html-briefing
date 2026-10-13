# 0.3.0 acceptance record

Date: 2026-09-29. This release changes the product from an external-companion recommendation to a complete redistributable skill bundle. The acceptance denominator is nine groups, not the number of repeated test runs.

| Group | Final status | Actual evidence |
|---|---|---|
| 1. Package, schema and integrity | PASS | 19 official skill validations, portable/compatibility manifest consistency and plugin/marketplace validation, exact 19-entry inventory and 204 recorded imported resources; links and integrity checker pass |
| 2. Bundled runtime checks | PASS | 19 automated tests: 12 package/checker cases, 4 plotting cases, UI database search, ImageGen credential-free dry-run, browser wrapper argument forwarding; installed Impeccable engine probe/context ran against a fictional project using an existing 0.1.6 engine; installed UI search returned results |
| 3. Independent behavior scenarios | PASS | First-use and explicitly selected personal-copy/title-edit scenarios; no redundant skill downloads, no automatic paid fallback, correct small-edit scope. Three found issues fixed and independently rechecked: stale five-skill wording, Impeccable relative link, Playwright global-install recommendation |
| 4. Sources and original-copy preservation | PASS | All 17 imported original skill snapshots still match recorded source hashes. Upstream MIT/Apache notices preserved; additional Impeccable/modern-screenshot notices included. Visualize manifest is Proprietary and no source is redistributed. Source scan found only a fictional /Users/me example in upstream JavaFX guidance, not a private path |
| 5. Bilingual rendered documentation | PASS | English/Chinese at 1280 and 390 widths, language navigation both ways, four assets loaded; nine browser checks; inventory-table screenshot inspected |
| 6. Clean installation | PASS | Supported CLI accepted the portable manifest plus compatibility overlay and installed 0.3.0 in an isolated home, discovered 19 actual skills and verified every recorded resource; installed helper probes succeeded from a separate cwd |
| 7. Public archive reproducibility | PASS | Downloaded ZIP/checksum match; all 249 archive files match v0.3.0; 19 tests pass from the extracted archive and its clean installation succeeds. Public English/Chinese README navigation verified both ways |
| 8. Production installation | PASS | Supported CLI reports enabled 0.3.0; 19 actual entries; all 222 installed files byte-equal to the downloaded release |
| 9. Codex detail-page display | BLOCKED | The computer-use tool prohibits access to the Codex application. The visible skill count cannot be observed through that tool; reopen the detail page manually after update |

The independent scenarios manually followed actual skill instructions and do not prove automatic host routing. ImageGen dry-run creates no image and makes no service call. The browser wrapper test validates command forwarding with a stub executable, not a downloaded Playwright CLI/browser. Real README rendering uses the host browser runtime. Impeccable was exercised with an already available engine, not a fresh download. Native Windows/Linux, actual image service execution and every GSAP combination remain unverified.

Vendored text retains original whitespace where possible. Package adaptations and individual hashes are in plugins/html-briefing/bundle.json. Root MIT does not relicense Apache-2.0 files. Existing personal copies were not overwritten or updated. No new external helper plugin was installed.

Overall: **FAIL (verification incomplete), 8/9 groups passed**. All executed functional checks passed. The sole missing observation is the refreshed Codex detail-page skill count, blocked by the computer-use tool. The minimum remaining step is to reopen the detail page and observe version 0.3.0 and 19 skills. See [release identity](release-verification-0.3.0.json). Main adds post-publication evidence; the tag and downloadable archive remain immutable.
