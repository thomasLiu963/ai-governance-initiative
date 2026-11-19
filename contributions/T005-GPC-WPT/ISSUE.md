# Issue to file on w3c/gpc

Status: not filed. Do not post this until Thomas approves this specific issue.

One submission. Do not also open a pull request on `web-platform-tests/wpt`, a pull request on `w3c/gpc`, or a Chromium bug. Those assume an answer this issue is asking for.

Repository: https://github.com/w3c/gpc/issues/new

The person who files this is responsible for every sentence. An LLM assembled the draft from the Working Draft and the sources in [upstream-check.md](upstream-check.md). Keep a disclosure in the issue. Rewriting the body in the filer's own words is appropriate. Pasting it unchanged is acceptable only with that disclosure left in.

## Title

Should an already loaded document keep its GPC value until the next top-level navigation?

## Body

Working Draft, 24 September 2026, § 3.2 requires the preference to be cached on each top-level navigation. A change during or after that navigation is not reflected until the next navigation. `gpcAtNavigation` must reflect the preference when the top-level document began loading. § 3.3 and § 3.4 bind `Sec-GPC` and `navigator.globalPrivacyControl` to that boolean. § 8.1 records the session preference and returns `{gpc: <boolean>}`. It does not say to rewrite `gpcAtNavigation` for a document that has already started loading.

https://www.w3.org/TR/2026/WD-gpc-20260924/

Four checks are separate. I did not run `./wpt run`, and there is no official testharness result for this observation.

Source only. Chromium `main`, `chrome/browser/chrome_global_privacy_control_browsertest.cc`, test `PrefChangeIsReflectedImmediately`, expects the other behavior for the profile setting. With the Universal Opt-Out features and `GlobalPrivacyControlApi` enabled, the test loads a document, then clears `kUniversalOptOutEnabled`, and expects `navigator.globalPrivacyControl` to become false and a following `fetch` to omit `Sec-GPC`, with no navigation. The comment says the toggle is reflected in the renderer without a reload. The Blink getter reads `RendererPreferences` on each access. A DevTools override, when set, takes precedence over that profile setting. I read this test. I did not compile or run it. On Firefox `main`, `GPC:SetGlobalPrivacyControl` writes `privacy.globalprivacycontrol.enabled`, and `Navigator::GlobalPrivacyControl` and `nsHttpChannel::SetGlobalPrivacyControl` read that preference when the value is used. Firefox is not installed here. Current WebKit applies the test runner's boolean in the navigation-policy callback, through `WKWebsitePoliciesSetGlobalPrivacyControlEnabled`. `navigator.globalPrivacyControl` reads the frame settings. `WKWebpagePreferences.globalPrivacyControlEnabled` is marked available starting in macOS 27. Safari on this machine is 17.6, and WebKit was not run.

DevTools experiment. Chrome 157.0.8103.79, headless, with `GlobalPrivacyControlApi` enabled. A local copy of the held test loaded `testharness.js`, `testharnessreport.js`, and `testdriver.js`, and a local vendor file, which is not part of the held patch, forwarded get and set to Chrome DevTools `Browser.getGlobalPrivacyControl` and `Browser.setGlobalPrivacyControl`. The assertion that the already loaded document keeps `navigator.globalPrivacyControl === false` failed because the value was true. This was not `./wpt run`. The same-document `Sec-GPC` assertion in that file did not run, because the attribute assertion failed first.

ChromeDriver experiment. Same Chrome version, ChromeDriver 157.0.8103.79. This sent the WebDriver extension command. It did not use that vendor file, and it did not load the held test. With `GlobalPrivacyControlApi` enabled, `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`. The already loaded document changed from `navigator.globalPrivacyControl === false` and no `Sec-GPC` to `true` and `Sec-GPC: 1` before the next navigation. With no feature enabled, the same command returns "Global Privacy Control is disabled." and the attribute is absent.

Existing WPT results, not this test. At revision `71b58bb191`, Chrome 158 and Firefox 160 pass the existing `gpc/` tests, including the testdriver test. Those tests set the preference and then open a new document. None of them reads the document that was already loaded. Safari 27.2 does not report a passing signal subtest for those files. There is no open `w3c/gpc` issue on this document-caching question. Issue #146 is about workers and is not this question.

Which behavior should an already loaded top-level document follow after the session preference changes, including after § 8.1?

If the document keeps `gpcAtNavigation` until the next top-level load, Chromium's unread browser test expects the other behavior, and the DevTools and ChromeDriver sessions above observed it. A Web Platform Test for that observation can be proposed afterward. If the loaded document is supposed to update immediately, § 3.2 needs an edit before any such test. I am not filing the test or a Chromium bug in parallel with this question.

LLM use: an LLM drafted this issue from the Working Draft, the Chromium, Firefox, and WebKit source cited above, the local DevTools experiment, and the local ChromeDriver session. `./wpt run` was not used. The person who posts it is responsible for the claims.
