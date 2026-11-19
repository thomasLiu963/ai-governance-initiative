# Upstream check, 18 November 2026

This file records the check that followed the first local packet. Nothing here was submitted. `./wpt run` was not started. The ChromeDriver session below is the WebDriver command that `./wpt run chrome` sends. It is a different run from the DevTools shim in [local-results.md](local-results.md).

## What can be concluded

The 24 September 2026 Working Draft still requires one cached boolean per top-level document. Chromium's current implementation updates the already loaded document, and Chromium's own browser test requires that update for the profile setting. ChromeDriver 157 on this machine, with `GlobalPrivacyControlApi` enabled, does the same for the WebDriver set command: the attribute and `Sec-GPC` change before the next navigation.

That is a real discrepancy with § 3.2. The draft's caching sentences are unconditional `MUST` requirements. No open specification issue asks the group to drop or keep them. Firefox's current source reads the live preference at the moment the attribute or the header is produced, and that source was not executed. WebKit's test runner attaches the value in the navigation-policy callback, and WebKit was not executed.

The useful external step is one question to the Privacy Working Group, in [ISSUE.md](ISSUE.md). A Web Platform Test that fails the immediate update, and a Chromium bug that cites the draft, both pick the answer. They wait until an editor confirms § 3.2 or changes it.

## Specification, re-read

| Source | What it still says |
| --- | --- |
| https://www.w3.org/TR/2026/WD-gpc-20260924/ | § 3.2: the preference must be cached on each top-level navigation and is not reflected until the next navigation. `gpcAtNavigation` must reflect the preference when the active document began loading. A reload prompt is a should. § 3.3 and § 3.4 bind the header and `navigator.globalPrivacyControl` to that boolean. § 8.1 records the session preference and returns `{gpc}`. It does not mention `gpcAtNavigation`. |
| https://w3c.github.io/gpc/ and `w3c/gpc` `main` | Same caching, header, attribute, and set-command text. Latest commit on 18 November 2026 is `09013acfed78`, 24 September 2026, "Merge pull request #160". No later commit. No open pull request. |

Open issues re-queried the same day: #164, #162, #146, #143, #138, #125, #114, #93. None asks whether an already loaded top-level document keeps `gpcAtNavigation`. #146, Anne van Kesteren, 12 May 2026, still has zero comments and the label `agenda+`. Its request is that user agents not be required to push settings changes into workers. `updated_at` is `2026-10-15T18:39:53Z`.

## Chromium, read from main

`chrome/browser/chrome_global_privacy_control_browsertest.cc`, fetched from `refs/heads/main` on 18 November 2026. The test was not compiled or run.

`PrefChangeIsReflectedImmediately` enables `kUniversalOptOut`, `kUniversalOptOutSettings`, and `kGlobalPrivacyControlApi`. It sets `kUniversalOptOutEnabled` to true, navigates, and expects `navigator.globalPrivacyControl === true` and `Sec-GPC: 1` on a fetch. It then sets the pref to false and, without another navigation, expects the attribute to be false and the fetch to report `None`. The comment above the fixture says toggling the setting is reflected in the renderer without a reload.

`third_party/blink/renderer/modules/global_privacy_control/navigator_global_privacy_control.cc` returns `IsGlobalPrivacyControlFeatureAndSettingEnabled` on the frame's current `RendererPreferences`, and the same call on a worker's renderer preferences. There is no load-time snapshot in that function.

`third_party/blink/common/global_privacy_control/global_privacy_control_util.cc` returns true when `kGlobalPrivacyControlForce` is enabled. Otherwise, when the API feature is enabled, it returns `global_privacy_control_devtools_override` if that optional is set, and `is_global_privacy_control_setting_enabled` otherwise. The comment says the DevTools override takes precedence over the embedder's profile setting.

The file header in the browser test says the profile pref is copied into renderer preferences only when both Universal Opt-Out features are enabled. `GlobalPrivacyControlApi` alone exposes the attribute. The WebDriver path below used the DevTools override, so it did not need those two features. The profile-pref test and the DevTools override are different inputs into the same live read.

`chrome/test/chromedriver/window_commands.cc` on the same main branch implements `ExecuteSetGlobalPrivacyControl` by calling DevTools `Browser.setGlobalPrivacyControl`, and the get command by calling `Browser.getGlobalPrivacyControl`. The earlier not-implemented stub is not what main contains now.

## ChromeDriver 157, executed

Binary: ChromeDriver 157.0.8103.79, build `6dc9bc3bdaea5c35ed6d41fceab2f7a3a2227c4f-refs/branch-heads/8103@{#1574}`, downloaded from `https://storage.googleapis.com/chrome-for-testing-public/157.0.8103.79/mac-arm64/chromedriver-mac-arm64.zip`. Browser: `/Applications/Google Chrome.app`, version 157.0.8103.79. Headless. Temporary user-data directories. Raw summary: [local-run/chromedriver-157.json](local-run/chromedriver-157.json).

| Session | Command result | Loaded document after set, before navigation |
| --- | --- | --- |
| No GPC feature | Get and set fail with "Global Privacy Control is disabled." | `globalPrivacyControl` is not exposed. Type `undefined`. |
| `--enable-features=GlobalPrivacyControlApi` and `--enable-blink-features=GlobalPrivacyControlApi` | Get starts at `{"gpc": false}`. Set `{"gpc": true}` returns `{"gpc": true}`. | Attribute changes from `false` to `true`. A same-document fetch changes from no `Sec-GPC` to `Sec-GPC: 1`. A later navigation stays `true` and `Sec-GPC: 1`. |

This session did not load `navigation-cache.https.html` and did not produce a testharness report. It sent the HTTP extension command from § 8.1.

## `./wpt run`

Not started. The runner lives in a checkout of `web-platform-tests/wpt` and installs its own virtualenv. That checkout was not created. The command the Chrome executor would send is the privacy endpoint exercised above. A testharness log for `gpc/navigation-cache.https.html` still does not exist.

`gpc/` on `master` is unchanged from the first packet: `META.yml` `e9bbee032d85`, testdriver `138bba2eb452`, IDL `7a7305eb6235`, navigator `6ddc7ffca419`, `sec-gpc` `6acc350d241c`, `support/getGPC.py` `d1c46aac254f`. No file asserts the already loaded document. Open pull request #64623 still changes only `gpc/support/getGPC.py`.

## wpt.fyi, queried 18 November 2026

Existing files only. These runs do not contain a navigation-cache test. Counts are passes/total from `https://wpt.fyi/api/search`.

| Run | Browser | Revision | testdriver | navigator | sec-gpc |
| --- | --- | --- | --- | --- | --- |
| 5091530419994624 | Chrome stable 158.0.8127.36 | `71b58bb191` | 1/1 | 8/8 | 16/16 |
| 5165587534446592 | Chrome canary 160.0.8168.0 | `71b58bb191` | 1/1 | 8/8 | 16/16 |
| 5102456061820928 | Firefox stable 160.0.1 | `71b58bb191` | 1/1 | 8/8 | 16/16 |
| 5073377791049728 | Firefox nightly 162.0a1 | `2f83c6fe83` | 1/1 | 8/8 | 16/16 |
| 5189568014581760 | Edge experimental 159.0.4393.0 | `2f83c6fe83` | 1/1 | 8/8 | 16/16 |
| 5121161130934272 | Safari stable 27.2 (22625.2.8.11.9) | `71b58bb191` | 0/1, status O | 0/0, status E | 0/0, status E |
| 6474556597075968 | Safari preview 256 | `93494ff9df` | 0/1, status O | 0/0, status E | 0/0, status E |

Chrome, Firefox, and Edge passes show that those products can run the current suite. The suite sets the preference and then opens a new document, so a pass does not show caching. Safari's `0/0` status E rows have no signal subtests. An empty count is neither a pass nor a fail. A search of `web-platform-tests/wpt` found no Chrome launch flag named `GlobalPrivacyControlApi`. This packet does not explain why Chrome 158 in that stable run accepts the testdriver command when local Chrome 157, with no flag, rejects it.

## Firefox source, not executed

`mozilla-firefox/firefox` `main`, fetched the same day.

- `remote/marionette/driver.sys.mjs`, `gpc_setGlobalPrivacyControl`, sets `privacy.globalprivacycontrol.enabled` and returns `{gpc}`.
- `dom/base/Navigator.cpp`, `Navigator::GlobalPrivacyControl`, returns that pref, or the private-browsing pref when the main pref is false. The function does not store a navigation-time value.
- `netwerk/protocol/http/nsHttpChannel.cpp`, `SetGlobalPrivacyControl`, reads the same prefs when the request channel is assembled and sets the header to `1` when either is true.
- `modules/libpref/init/StaticPrefList.yaml` defaults both `privacy.globalprivacycontrol.enabled` and `privacy.globalprivacycontrol.pbmode.enabled` to false.
- `browser/app/profile/firefox.js` sets `privacy.globalprivacycontrol.pbmode.enabled` to true. That is a desktop override of the private-browsing default. It was not run.

Firefox is not installed on this Mac.

## WebKit source, not executed

- `Tools/WebKitTestRunner/TestController.cpp` copies `m_globalPrivacyControlEnabled` onto the navigation's `WKWebsitePolicies` inside the policy callback, with `WKWebsitePoliciesSetGlobalPrivacyControlEnabled`, and then uses those policies for that navigation.
- `Source/WebCore/page/NavigatorGlobalPrivacyControl.cpp` returns `frame->settings().globalPrivacyControlEnabled()`.
- `Source/WebCore/Scripts/SettingsTemplates/Settings.cpp.erb` sets that setting from the website policies.
- `Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.h` marks `globalPrivacyControlEnabled` available in macOS 27.0, iOS 27.0, and visionOS 27.0.
- The WebKit blog post https://webkit.org/blog/18646/global-privacy-control-gpc-webkit-api/ describes setting the property in `decidePolicyFor` so that the navigation opts in.

Safari on this Mac is 17.6 (19618.3.11.11.5), macOS 14.6.1. It was not launched. The source shows where WebKit attaches the value. It is not a runtime result for an already loaded document.

## Route

File the issue in [ISSUE.md](ISSUE.md) only after explicit approval.

Hold [patch/0001-gpc-navigation-cache.patch](patch/0001-gpc-navigation-cache.patch). If an editor says § 3.2 stands, that patch is the follow-up WPT, with the ChromeDriver result named in the pull request so the failure is the conformance result. If an editor changes § 3.2 so the loaded document updates immediately, drop the patch. Do not open the patch while the issue is unanswered, and do not open a Chromium bug that asks Chromium to fail `PrefChangeIsReflectedImmediately` before that answer.
