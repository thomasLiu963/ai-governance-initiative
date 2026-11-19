# What was checked

Checked on 2026-11-18 from public source. Commands and raw files used for this packet stayed on this machine.

## Specification

| Item | Locator | What was read |
| --- | --- | --- |
| Working Draft | [Global Privacy Control, 24 September 2026](https://www.w3.org/TR/2026/WD-gpc-20260924/) | Preference Caching (§ 3.2), the `Sec-GPC` generation rules (§ 3.3), the JavaScript property (§ 3.4), and Set Global Privacy Control. |
| Editor's draft source | [`index.html`](https://github.com/w3c/gpc/blob/09013acfed7820dc967489514a156e2ced827289/index.html) at `09013acfed7820dc967489514a156e2ced827289` | The same paragraphs. Repository `pushed_at` is `2026-09-24T16:56:10Z`. That commit is the merge of pull request #160. |
| Document status | W3C Working Draft on the Recommendation track. Publication is not an endorsement and not a Recommendation. | The dated TR and `w3c.json` group `wg/privacy`, repo-type `rec-track`, were already recorded in the audit. This check re-read the normative paragraphs rather than the repository metadata file. |

Section 3.2 of the dated draft says the preference must be cached on each top-level navigation, and that a change during or after a top-level navigation is not reflected until the next navigation. A top-level browsing context has `gpcAtNavigation`, initially false. Its value must reflect the preference when that browsing context's active document began loading. A user agent should offer to reload tabs whose cached value no longer matches; that sentence is a should, and this test does not require the reload prompt.

Section 3.3 says the user agent must not generate `Sec-GPC` when `gpcAtNavigation` is false, and must generate a field value of exactly `1` when it is true. Section 3.4 says `navigator.globalPrivacyControl` must be that same boolean. The value is false when no `Sec-GPC` header would be sent.

Set Global Privacy Control records the session preference and returns `{gpc: <the boolean that was set>}`. The algorithm does not say to rewrite `gpcAtNavigation` for documents that have already started loading. The caching section is the rule for when a change becomes visible.

The editor's draft paragraphs for those four rules match the dated TR. The comparison was the text of the caching section, the two header-generation sentences, the JavaScript "must be `gpcAtNavigation`" sentence, and the set-command steps.

## Existing Web Platform Tests

Tree: [`web-platform-tests/wpt` `gpc/`](https://github.com/web-platform-tests/wpt/tree/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/gpc) at `fa74da28dbe155bf65dc0b16cfdef8e6fb396153` (2026-11-18T23:02:10Z). The files below were downloaded and read.

| File | Blob prefix | What it asserts |
| --- | --- | --- |
| `gpc/global_privacy_control.testdriver.html` | `138bba2eb4` | Get and set return `{gpc: boolean}`. It does not read `navigator.globalPrivacyControl` or `Sec-GPC`. |
| `gpc/navigator-globalPrivacyControl.https.html` | `6ddc7ffca4` | Sets the preference, then `window.open`s a new document and expects that document, a dedicated worker, a shared worker, and a service worker to match the value just set. |
| `gpc/sec-gpc.https.html` | `6acc350d24` | Same order: set, then open `support/getGPC.py`, which checks the header on the new document and the subresources and workers it creates. |
| `gpc/idlharness.any.js` | `7a7305eb62` | IDL surface on window and worker. |
| `gpc/support/getGPC.py` | `d1c46aac254f` | Emits assertions for the request that is already in flight. It has no same-document-before-and-after-set sequence. |
| `gpc/support/navigator-globalPrivacyControl.html` | `270023ed9cf8` | Assertions for a document created after the set, including workers. |
| `gpc/support/navigator-globalPrivacyControl.js` | `beb9ea372cd4` | Worker assertion for a worker created by that new document. |

The contents API listed seven files and the `support/` directory. Every file was read. None reads the already loaded document after `set_global_privacy_control`. A code search for that function returned `resources/testdriver.js`, the wptrunner and WebDriver client, `docs/writing-tests/testdriver.md`, and the three `gpc/` documents above.

## Issue #146 and workers

[w3c/gpc#146](https://github.com/w3c/gpc/issues/146), "UA automation feedback", opened 2026-05-12 by `annevk`, label `agenda+`, no assignee. The issue body asks that user agents not be required to synchronize settings changes into workers for this feature. The comments API returned zero comments. `updated_at` was `2026-10-15T18:39:53Z`. There is no linked pull request.

The Working Draft still says `WorkerNavigator includes GlobalPrivacyControl` and that the attribute must be the top-level browsing context's `gpcAtNavigation`. That sentence does not name a browsing context for a service worker. This packet does not choose a worker rule.

The current `gpc/` worker assertions remain as they are: they check workers created by a document that was opened after the preference was set. This patch does not edit those files.

## Open pull requests

`w3c/gpc` had no open pull requests at the time of the API query.

On `web-platform-tests/wpt`, the open pull request returned for a `gpc` search was [#64623](https://github.com/web-platform-tests/wpt/pull/64623), "WebKit export of https://bugs.webkit.org/show_bug.cgi?id=315807", author `annevk`, opened 2026-11-03, still open on 2026-11-18. Its only file is `gpc/support/getGPC.py`. The patch sequences the script, iframe, and worker fetches and calls `done()` after the worker results. It does not assert that an already loaded document keeps its cached preference. This contribution does not modify `getGPC.py`, so it does not overlap that diff.

Closed WPT pull requests #54446, #55796, and #56495 are the existing testdriver extension, the Gecko signal tests, and the wdspec tests. They are the suite that was read above, not a navigation-cache test.

## Test infrastructure

`resources/testdriver.js` at the same WPT commit exposes `test_driver.get_global_privacy_control()` and `test_driver.set_global_privacy_control(boolean)`. Both return a promise of `{gpc: boolean}`. The default `test_driver_internal` methods throw "not implemented by testdriver-vendor.js".

`tools/wptrunner/wptrunner/testdriver-extra.js` replaces those methods with actions. `tools/webdriver/webdriver/client.py` sends `POST /session/{id}/privacy` with `{"gpc": <boolean>}` and `GET /session/{id}/privacy`. `executorwebdriver.py` forwards those calls. `executormarionette.py` sends Marionette messages `GPC:SetGlobalPrivacyControl` and `GPC:GetGlobalPrivacyControl`, and raises `NotImplementedError` if the browser replies `UnsupportedOperationException`.

`gpc/META.yml` suggests review by `AramZS`, `bvandersloot-mozilla`, `j-br0`, `pes10k`, and `SebastianZimmeck`. `gpc/WEB_FEATURES.yml` maps every file in the directory to the `gpc` feature, so a new file is covered without editing that map.

## Browser code and this machine

Chrome on this Mac is 157.0.8103.79. The framework binary contains the feature-name strings `GlobalPrivacyControl`, `GlobalPrivacyControlApi`, and `GlobalPrivacyControlForce`, the header name `Sec-GPC`, and the DevTools method names `getGlobalPrivacyControl` and `setGlobalPrivacyControl`. Flag text in that binary describes "Global Privacy Control API" as sending `Sec-GPC: 1` and setting `navigator.globalPrivacyControl`. Runtime results are in [local-results.md](local-results.md).

Chromium `main`, fetched the same day, has `BrowserHandler::SetGlobalPrivacyControl` in `content/browser/devtools/protocol/browser_handler.cc`. If `blink::IsGlobalPrivacyControlFeatureEnabled()` is false it returns "Global Privacy Control is disabled." Otherwise it calls `UpdateGlobalPrivacyControlDevToolsOverride`, which stores the boolean and calls `SyncRendererPrefs` on every `WebContents`. `chrome/browser/chrome_global_privacy_control_browsertest.cc` contains `PrefChangeIsReflectedImmediately`. Its comment says toggling the setting is reflected in the renderer without a reload, and the test expects `navigator.globalPrivacyControl` and a following `fetch` to show the new value with no navigation. That is the opposite of Working Draft § 3.2. The Chrome 157 run with `GlobalPrivacyControlApi` behaved the same way.

WebKit `main`, fetched the same day: `NavigatorGlobalPrivacyControl::globalPrivacyControlEnabled` reads the frame setting, and the worker overload reads the worker's `settingsValues()`. `WKWebpagePreferences.globalPrivacyControlEnabled` is annotated `WK_API_AVAILABLE(macos(27.0), ios(27.0), visionos(27.0))`. The header comment says that, when enabled, the attribute and `Sec-GPC: 1` are active for the main frame, its subframes, and their subresources. `TestController::setGlobalPrivacyControl` stores a bool. `decidePolicyForNavigationAction` copies that bool onto the navigation's `WKWebsitePolicies`. `LayoutTests/resources/testdriver-vendor.js` implements the testdriver methods with `testRunner.setGlobalPrivacyControl` and resolves `{gpc: value}`. This packet did not run WebKit.

`mozilla/gecko-dev` `master` `dom/webidl/Navigator.webidl` includes `GlobalPrivacyControl` behind the pref `privacy.globalprivacycontrol.functionality.enabled`. The IDL comment cites `https://globalprivacycontrol.github.io/gpc-spec/`. Firefox is not installed here, and this packet did not run it or determine the pref default.

Safari on this Mac is 17.6 (19618.3.11.11.5) on macOS 14.6.1. The system WebKit framework bundle is dated 4 August 2024. Its `WebCore.framework` directory did not contain a WebCore executable that could be scanned; the dyld shared cache was not scanned. Given the macOS 27 availability annotation in current WebKit source, Safari 17.6 was not treated as an implementation of this API. No Safari run was started.

## Parser issue, deferred

[w3c/gpc#114](https://github.com/w3c/gpc/issues/114) is open, assigned to `pes10k`, and its title is "Define the header value parser." The receiver paragraph in the 24 September 2026 draft is the same contradiction described in the audit: an exact field value of `1` is required, and multiple `Sec-GPC` headers are honored if any one of them is `1`. Anne van Kesteren's 23 October 2026 comment still says the parser has to operate on the combined value. No new receiver defect, distinct from that issue, turned up while reading § 3.3.

The 23 October 2026 comment by `autoCAT6` links a 20-case Node observation suite in `autoCAT6/gpc-header-observations`. This patch does not copy those cases, that script, or those results. `support/sec-gpc-value.py` reports the single `sec-gpc` field value on one request, or JSON `null` when the field is absent, so the navigation test can see what the user agent sent.

## Not verified

- `./wpt lint` and `./wpt run`.
- Whether ChromeDriver forwards `POST /session/{id}/privacy` to `Browser.setGlobalPrivacyControl`. The local run called the DevTools method directly.
- A Firefox build, including whether Gecko caches `gpcAtNavigation`.
- A WebKit or Safari build new enough to expose the API.
- wpt.fyi results for the existing `gpc/` files.
- Shipping defaults for Edge or for Chrome channels other than the local 157.0.8103.79 binary.
- Any worker runtime behavior.
