# Local results

Date: 2026-11-18. Browser binary: Google Chrome 157.0.8103.79. Profile: a temporary `--user-data-dir`, removed after each run. Headless. No paid API.

Raw records: [local-run/harness-result.json](local-run/harness-result.json) and [local-run/probe-summary.json](local-run/probe-summary.json).

## Executed: the patch file

The file `patch/gpc/navigation-cache.https.html` was loaded in Chrome with `GlobalPrivacyControlApi` and the Blink feature of the same name. Scripts were the WPT copies of `testharness.js`, `testharnessreport.js`, and `testdriver.js` from commit `fa74da28dbe155bf65dc0b16cfdef8e6fb396153`. A local `testdriver-vendor.js`, used only for this run and not included in the patch, forwarded get and set to Chrome DevTools `Browser.getGlobalPrivacyControl` and `Browser.setGlobalPrivacyControl`. The page was served over HTTP on `127.0.0.1`. Popup blocking was disabled so `window.open` could run. `./wpt run` was not used.

Harness status: OK. Two tests.

| Result | Test | Message |
| --- | --- | --- |
| Fail | A preference change waits for the next top-level document load | `assert_equals: the loaded document keeps its cached navigator.globalPrivacyControl expected false but got true` at `navigation-cache.https.html:54` |
| Pass | A new top-level document uses the preference from when it began loading | |

Requests observed for that page, ignoring `favicon.ico`:

| Path | `Sec-GPC` |
| --- | --- |
| `/gpc/navigation-cache.https.html` and its scripts | absent |
| first `/__gpc` (get) and first `sec-gpc-value.py` | absent |
| second `/__gpc` (set to true) | absent on that request |
| `/gpc/support/navigation-cache-document.html`, its testharness script, and its `sec-gpc-value.py` | `1` |
| later `/__gpc` (cleanup) | `1` |

The same-document header assertion on line 57 did not run, because the attribute assertion failed first. The new document's navigation and its subresource both carried `Sec-GPC: 1`, which is the passing half of the test.

This is a real failure of Working Draft § 3.2 on this Chrome configuration: the loaded document took the new preference before the next top-level load. It is also the behavior Chromium's `PrefChangeIsReflectedImmediately` test expects.

## Executed: the same scenario without the harness

Before the patch file existed, the same Chrome binary was driven directly with DevTools, against a small local page rather than the WPT file. Five feature sets were used. "Attribute" is `navigator.globalPrivacyControl === true`. "Exposed" is `'globalPrivacyControl' in navigator`.

| Features | Command | Loaded document | After set, same document | After a later navigation | `Sec-GPC` |
| --- | --- | --- | --- | --- | --- |
| none | error: Global Privacy Control is disabled | not exposed, type `undefined` | unchanged, still not exposed | unchanged, still not exposed | absent on every request |
| `GlobalPrivacyControlApi` | get false, set true returns true | exposed, false | exposed, true | exposed, true | absent on `/page1` and `/sub1`; `1` on `/sub2`, `/page2`, and `/sub3` |
| `GlobalPrivacyControlApi`, `UniversalOptOut`, `UniversalOptOutSettings` | same as the API row | same | same | same | same |
| `GlobalPrivacyControl`, `GlobalPrivacyControlApi`, `UniversalOptOut`, `UniversalOptOutSettings` | same as the API row | same | same | same | same |
| `GlobalPrivacyControlApi`, `GlobalPrivacyControlForce` | get false, set false returns false | exposed, true | stays true | stays true | `1` on every request |

The three rows that enable the API and do not enable Force are the caching failure: `/sub2` is a fetch from the already loaded document after the set, and it gained `Sec-GPC: 1` with no navigation. That is the header half the harness stopped before asserting.

The Force row is not evidence of caching. The setter reported false, the loaded document stayed true, and the next navigation stayed true as well. Force kept the signal on. It did not demonstrate a document waiting for the next load.

The default row is not a pass. The attribute is absent and the command is rejected, so the caching assertions have no implementation to judge. The patch file was not loaded again in that configuration.

`support/sec-gpc-value.py` was called locally with a stand-in request object. Missing, `b"1"`, `"1"`, `b"0"`, and `[b"1", b"1"]` became JSON `null`, `"1"`, `"1"`, `"0"`, and `["1", "1"]`. The browser run then exercised the `null` and `"1"` paths through the same `main` function. The list path was not produced by Chrome.

## Awaiting an implementation

| Environment | Why the caching assertions were not decided there |
| --- | --- |
| Chrome 157 with no GPC feature flag | DevTools returns "Global Privacy Control is disabled." `navigator.globalPrivacyControl` is `undefined`. This is the binary's default. |
| `./wpt run` and ChromeDriver `POST /session/{id}/privacy` | Not run. The DevTools method was called directly. A browser whose ChromeDriver does not implement the WPT endpoint would error in `get_global_privacy_control` before the cache assertions. |
| Firefox | Not installed. `executormarionette.py` turns an unsupported `GPC:SetGlobalPrivacyControl` into `NotImplementedError`. Gecko's IDL exposes the attribute only when `privacy.globalprivacycontrol.functionality.enabled` is set. The pref default and the caching behavior were not run. |
| Safari 17.6 on macOS 14.6.1 | Not run. Current WebKit source marks `WKWebpagePreferences.globalPrivacyControlEnabled` available starting in macOS 27. WebKit's test runner stores the testdriver value and applies it in `decidePolicyForNavigationAction`. That path was read and not executed. |
| Workers | The patch does not start a worker. No worker result was collected. Issue #146 is still open and uncommented. |

The handler unit checks and the Chrome runs above are the DevTools-shim executions. They are not a Web Platform Tests dashboard result, and they are not an acceptance of the patch.

## Separate run: ChromeDriver 157

Recorded in [local-run/chromedriver-157.json](local-run/chromedriver-157.json) and explained in [upstream-check.md](upstream-check.md). ChromeDriver 157.0.8103.79 called `POST /session/{id}/privacy` and `GET /session/{id}/privacy` against the same Chrome binary. That is the WebDriver extension command. It does not load `navigation-cache.https.html`, it does not use the local `testdriver-vendor.js` shim, and `./wpt run` was not started.

With `GlobalPrivacyControlApi` enabled, the set command returned `{"gpc": true}` and the already loaded document moved from attribute false and no `Sec-GPC` to attribute true and `Sec-GPC: 1` before the next navigation. With no feature flag, the command returned "Global Privacy Control is disabled." The shim table above and this session describe the same immediate update. They are two procedures.
