# T005 — GPC navigation-cache Web Platform Test

Status: local draft, 2026-11-18. Nothing in this directory has been submitted. No pull request, issue comment, or other external write was made.

## Conclusion

The Working Draft still requires a top-level document to keep the GPC value from when it began loading. Chromium updates that document immediately. Both of those statements were checked against current public source on 18 November 2026, and the Chromium side was also observed through ChromeDriver on this machine. The details are in [upstream-check.md](upstream-check.md).

§ 3.2 says a preference change during or after a top-level navigation is not reflected until the next navigation. `navigator.globalPrivacyControl` and `Sec-GPC` follow `gpcAtNavigation`. The editor's draft matches the 24 September 2026 Working Draft, and no open issue asks the group to change that sentence. Issue #146 is about workers.

Chromium's `PrefChangeIsReflectedImmediately` expects a profile-pref toggle to change `navigator.globalPrivacyControl` and `Sec-GPC` in the already loaded document, with no reload. The Blink getter reads the current renderer preferences on each access. ChromeDriver 157.0.8103.79, which is the endpoint `./wpt run chrome` would call, was run here with `GlobalPrivacyControlApi` enabled. `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`, and the loaded document changed from false and no header to true and `Sec-GPC: 1` before the next navigation. Default Chrome 157 rejects the command. That ChromeDriver session is not the earlier DevTools shim, and it is not `./wpt run`. The shim failed the same attribute assertion. The two runs agree and are recorded separately.

Firefox was not run. On current Firefox source, the Marionette set command writes `privacy.globalprivacycontrol.enabled`, and both the attribute and `Sec-GPC` read that preference when they are produced. WebKit was not run. Its test runner copies a stored boolean onto the navigation's website policies. Safari here is 17.6. The API annotation in current WebKit starts at macOS 27.

wpt.fyi at revision `71b58bb191` shows Chrome 158 and Firefox 160 passing the existing `gpc/` tests. Those tests set the preference and then open a new document. They do not show whether the loaded document keeps the old value. Safari 27.2 does not report passing signal subtests.

The external step that matches this evidence is one question to the Privacy Working Group, drafted in [ISSUE.md](ISSUE.md). The Web Platform Test patch stays local. It is the follow-up if an editor keeps § 3.2. It is dropped if an editor changes § 3.2 so the loaded document updates immediately. A Chromium bug is the same question asked in a second tracker, and it waits for that answer too.

## Packet

| File | Contents |
| --- | --- |
| [upstream-check.md](upstream-check.md) | Spec, Chromium test, ChromeDriver session, Firefox and WebKit source, and wpt.fyi counts checked on 18 November 2026. |
| [ISSUE.md](ISSUE.md) | The only submission-ready text. A question for `w3c/gpc`. Not posted. |
| [verification.md](verification.md) | First-pass specification text, current tests, issue #146, and browser notes. |
| [rationale.md](rationale.md) | Why the held test matches the draft, why workers are separate, and why the parser issue is deferred. |
| [submission.md](submission.md) | Why the issue comes first, and the WPT route that stays closed until an editor answers. |
| [local-results.md](local-results.md) | DevTools shim, separate from the ChromeDriver session. |
| [patch/0001-gpc-navigation-cache.patch](patch/0001-gpc-navigation-cache.patch) | Three new files. Held. Not the current submission. |

The same three files are also present as a tree under `patch/gpc/` so they can be read without applying the diff.

## Themes

Privacy and human agency. The cached boolean is how a person's do-not-sell-or-share request stays one value for the whole top-level document. A user agent that applies a later change inside that document lets the page and its subresources observe a different preference from the one in force when the document loaded.

## Not done

`./wpt lint` and `./wpt run` were not used. No testharness result exists for `navigation-cache.https.html` under the official runner. The ChromeDriver session covered the WebDriver command that runner would send, on Chrome 157 with the API flag, and did not execute this file. Firefox and WebKit were not launched. `PrefChangeIsReflectedImmediately` was read and not executed.
