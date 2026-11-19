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

Chromium `main`, `chrome/browser/chrome_global_privacy_control_browsertest.cc`, test `PrefChangeIsReflectedImmediately`, expects the other behavior for the profile setting. With the Universal Opt-Out features and `GlobalPrivacyControlApi` enabled, the test loads a document, then clears `kUniversalOptOutEnabled`, and expects `navigator.globalPrivacyControl` to become false and a following `fetch` to omit `Sec-GPC`, with no navigation. The comment says the toggle is reflected in the renderer without a reload. The Blink getter reads `RendererPreferences` on each access. A DevTools override, when set, takes precedence over that profile setting.

I ran the WebDriver command, not a DevTools shim, against Chrome 157.0.8103.79 with ChromeDriver 157.0.8103.79. With `GlobalPrivacyControlApi` enabled, `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`. The already loaded document changed from `navigator.globalPrivacyControl === false` and no `Sec-GPC` to `true` and `Sec-GPC: 1` before the next navigation. With no feature enabled, the same command returns "Global Privacy Control is disabled." and the attribute is absent. I did not run `./wpt run`.

On `mozilla-firefox/firefox` `main`, `GPC:SetGlobalPrivacyControl` writes `privacy.globalprivacycontrol.enabled`. `Navigator::GlobalPrivacyControl` and `nsHttpChannel::SetGlobalPrivacyControl` read that preference when the value is used. Firefox is not installed here, so this is source only.

Current WebKit applies the test runner's boolean in the navigation-policy callback, through `WKWebsitePoliciesSetGlobalPrivacyControlEnabled`. `navigator.globalPrivacyControl` reads the frame settings. `WKWebpagePreferences.globalPrivacyControlEnabled` is marked available starting in macOS 27. Safari on this machine is 17.6, and WebKit was not run.

At WPT revision `71b58bb191`, Chrome 158 and Firefox 160 pass the existing `gpc/` tests, including the testdriver test. Those tests set the preference and then open a new document. None of them reads the document that was already loaded. Safari 27.2 does not report a passing signal subtest for those files. There is no open `w3c/gpc` issue on this document-caching question. Issue #146 is about workers and is not this question.

Which behavior should an already loaded top-level document follow after the session preference changes, including after § 8.1?

If the document keeps `gpcAtNavigation` until the next top-level load, Chromium's browser test and the Chrome 157 session above are nonconforming, and a Web Platform Test for that observation can be proposed afterward. If the loaded document is supposed to update immediately, § 3.2 needs an edit before any such test. I am not filing the test or a Chromium bug in parallel with this question.

LLM use: an LLM drafted this issue from the Working Draft, the Chromium test, and a local ChromeDriver session. The person who posts it is responsible for the claims.
