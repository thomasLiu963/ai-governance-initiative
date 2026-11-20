# What was run, and what was re-checked

Checked 2026-11-19 (local evening; 2026-11-20 UTC). Nothing in this directory was submitted.

## Official runner, as recorded on 2026-11-19

The run is the one recorded in `execution/phase1/MASTER_RANKING.md` and `execution/phase1/drafts/gpc-wpt/PULL_REQUEST.md`. This sprint did not start `./wpt run` again. The raw wptrunner log was not kept in the workspace. The two files in this packet are byte-copies of the two files that record says were linted and run.

| Fact | Recorded result |
| --- | --- |
| Checkout | `web-platform-tests/wpt` `221a7fea449dcd9a42d5f249d5e4cf359a619d74` |
| Lint | `./wpt lint` on the two proposed files exited 0 |
| Command | `./wpt run -y chrome` |
| Browser | Chrome 157.0.8103.79, `--enable-features=GlobalPrivacyControlApi` |
| Attribute | `assert_equals: the loaded document keeps its cached navigator.globalPrivacyControl expected false but got true` |
| `Sec-GPC` | A one-off copy, not in this diff, asserted the header first. Expected null, got `"1"` |
| Header line in this file | Not reached. The attribute assertion fails first |
| Firefox, WebKit | Not run |
| Expectation `.ini` files | None in that checkout. Not edited |

`master` was still `221a7fea449dcd9a42d5f249d5e4cf359a619d74` when re-queried on 2026-11-20T02:19:21Z, the same commit the run used. The `gpc/` blobs were still `META.yml` `e9bbee032d85`, `global_privacy_control.testdriver.html` `138bba2eb452`, `navigator-globalPrivacyControl.https.html` `6ddc7ffca419`, `sec-gpc.https.html` `6acc350d241c`, and `idlharness.any.js` `7a7305eb6235`. There is still no `navigation-cache.https.html`.

## Recheck, 2026-11-20

`master` moved later that day to `8971ee02ffe8be3fa02862e0b07e1e37f34ab7a7` ("Implement additional `<selectedcontent>` spec changes", committer date 2026-11-20T15:12:01Z). The same five `gpc/` blobs were still those SHAs. `support/` is still `getGPC.py`, `navigator-globalPrivacyControl.html`, and `navigator-globalPrivacyControl.js`. A code search found no `navigation-cache` file. Pull request 64623 was still open and still changed only `gpc/support/getGPC.py`.

The two existing document tests were re-read at those blobs. Each calls `set_global_privacy_control` and then `window.open`. Neither reads `navigator.globalPrivacyControl` in the already loaded document. `resources/testdriver.js` on that master still returns `{gpc}` from both the get and the set command.

https://www.w3.org/TR/gpc/ still contains the section 3.2 cache rule, the section 3.3 header rule, the section 3.4 attribute rule, and the section 8.1 session command. `w3c/gpc` `main` is still `09013acfed7820dc967489514a156e2ced827289`. Issue 165 is still closed by the 2026-11-19 editor comment. No new specification sentence was added.

`./wpt lint` and `./wpt run` were not repeated against `8971ee02`. The 2026-11-19 run remains the execution record. `gpc/META.yml` still names AramZS, bvandersloot-mozilla, j-br0, pes10k, and SebastianZimmeck. `WEB_FEATURES.yml` still maps `**` to `gpc`.

## Earlier runs, which are not this result

These agree with the official failure. They are different procedures.

- 2026-11-18 DevTools shim, in `contributions/T005-GPC-WPT/local-results.md`. A local vendor file forwarded get and set. The same attribute assertion failed: expected false, got true. The same-document header assertion in that file did not run. Not `./wpt run`.
- 2026-11-18 ChromeDriver 157 session, in `contributions/T005-GPC-WPT/upstream-check.md`. `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`, and the already loaded document changed from false and no `Sec-GPC` to true and `Sec-GPC: 1` before the next navigation. That session did not load this test file.

## Specification re-read

https://www.w3.org/TR/gpc/ and the dated Working Draft https://www.w3.org/TR/2026/WD-gpc-20260924/ still say, in section 3.2, that the preference must be cached on each top-level navigation and that a change during or after that navigation is not reflected until the next navigation. `gpcAtNavigation` must reflect the preference when the active document began loading. Section 3.3 binds `Sec-GPC` to that boolean. Section 3.4 binds `navigator.globalPrivacyControl` to it. Section 8.1 records the session preference and returns `{gpc}`. It does not mention `gpcAtNavigation`.

`w3c/gpc` `main` is still `09013acfed7820dc967489514a156e2ced827289`, 2026-09-24. No specification commit has landed since the Working Draft.

## Editor comment

https://github.com/w3c/gpc/issues/165 was closed 2026-11-19T20:28:55Z by `SebastianZimmeck`. His comment quotes the section 3.2 cache rule, including the sentence that a change is not reflected until the next navigation, and the should-level sentence about informing the user and offering a reload. He then writes: "Generally speaking, implementers should always make a best effort to understand and adhere to a user's GPC preference."

He did not write a new normative sentence. He did not edit `index.html`. Closing the issue is not a Working Group resolution and not acceptance of this test.

## Why the assertions match the draft

The test records `navigator.globalPrivacyControl` on the already loaded document, sets the opposite boolean, and requires the attribute to stay at the recorded value. A later `fetch` of `support/sec-gpc-value.py` must carry the same `Sec-GPC` value the first fetch carried. The handler returns JSON `null` when the field is absent and the decoded field value when it is present. `getGPC.py` already treats `request.headers.get("sec-gpc")` as bytes and compares it with `b"1"`, which is the same header read.

The test does not require the document and the session preference to match before the set. It flips the document's value. If the session was already the opposite, the set is a no-op and a caching implementation still passes. If the implementation updates the loaded document, the assertion fails either way.

Cleanup restores the session value from the start of the test.

## What is still not verified

- A fresh `./wpt run` or `./wpt lint` in this sprint. The 2026-11-19 record is the official-run evidence.
- Firefox and WebKit.
- Why wpt.fyi Chrome 158 passes the existing testdriver command when local Chrome 157, with no feature flag, rejects it. The recorded run passed the flag explicitly.
- Whether CI will require an entry in `web-platform-tests/wpt-metadata` before merge.
- Chromium's `PrefChangeIsReflectedImmediately` was read on 2026-11-18 and not executed.
