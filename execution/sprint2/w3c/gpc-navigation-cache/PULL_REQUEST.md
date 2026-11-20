# Proposed pull request

Opened 2026-11-20 as https://github.com/web-platform-tests/wpt/pull/65548 by `thominator1011`. Do not open a second pull request. The description has no disclosure line. A commit-message note is optional under the Web Platform Tests policy and was not added. GitHub refused a reviewer request from this account.

Repository: `web-platform-tests/wpt`, branch `master`. Directory: `gpc/`. This is not a pull request to `w3c/gpc`.

License: 3-clause BSD, as stated in WPT `CONTRIBUTING.md` and `LICENSE.md`. The new files do not add a separate copyright header. The existing `gpc/` tests do not either.

Suggested reviewers, from `gpc/META.yml` as read on 2026-11-20: AramZS, bvandersloot-mozilla, j-br0, pes10k, SebastianZimmeck. `WEB_FEATURES.yml` already maps `**` to `gpc`, so the new file does not need a feature-map edit.

## Files

Add only:

- `gpc/navigation-cache.https.html`
- `gpc/support/sec-gpc-value.py`

The exact diff is `0001-gpc-navigation-cache.patch` in this directory. It is two new files. Apply it from a checkout of `master` with `git apply`.

Do not add `gpc/support/navigation-cache-document.html`. A document opened after the preference is set is already covered by `navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html`. Those tests set the preference and then call `window.open`. They never read the document that was already loaded.

Do not edit `gpc/support/getGPC.py`. Open pull request 64623 changes only that file.

## Title

```text
GPC: an already loaded document keeps the preference until the next top-level navigation
```

## Body

```markdown
An already loaded top-level document keeps `navigator.globalPrivacyControl` and `Sec-GPC` from the preference in effect when that document began loading.

Working Draft section 3.2 caches the preference on each top-level navigation. A change during or after that navigation is not reflected until the next navigation. `gpcAtNavigation` is the preference when the active document began loading. Section 3.3 sends `Sec-GPC: 1` only when that boolean is true, and sends no header when it is false. Section 3.4 sets `navigator.globalPrivacyControl` to that boolean. Section 8.1 records the session preference and returns `{gpc}`. It does not refresh an already loaded document.

`navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html` set the preference and then open a new document. They do not read the document that was already loaded. This test records that document, sets the opposite session value with the testdriver command, and asserts that the attribute and a later same-document subresource keep the value from when that document began loading.

The test does not assert the should-level reload prompt, and it does not create a worker. w3c/gpc#146 has no resolution on workers. Closing w3c/gpc#165 quoted the cache rule and did not change the specification. This test encodes the published Working Draft sentence.

`./wpt lint` on these two files passed against checkout `221a7fea449dcd9a42d5f249d5e4cf359a619d74`, and again on November 20, 2026, against `master` `ab51abc`. `./wpt run chrome` on Chrome 157.0.8103.79 with `GlobalPrivacyControlApi` enabled failed the attribute assertion: expected false, got true. Firefox and WebKit were not run. The failure is the conformance observation. This diff adds no expectation metadata.
```

## Commit message, for the person who commits

```text
Test that a GPC preference change waits for the next top-level load.

Existing gpc tests only observe documents opened after the preference
is set. The Working Draft already requires the loaded document to keep
gpcAtNavigation.
```

## What this pull request is not

- It is not an amendment to the Global Privacy Control specification.
- It is not a Working Group resolution. Closing issue 165 is an editor comment that quotes the current draft.
- It is not a Chromium bug. Do not open one in the same step. Open one later only if a reviewer asks.
- It is not acceptance. Acceptance is a merge to `web-platform-tests/wpt` `master`.
