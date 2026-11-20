# Proposed pull request

Not opened. Do not file, push, or comment until this specific pull request is approved. The person who opens it has to understand the test and be the author of record. WPT allows an LLM to help write a test. Model-written discussion in the pull-request body has to be labelled and kept to one blockquote paragraph, or placed in a `<details>` element.

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

WPT's AI policy does not allow model-written discussion in the main text. Rewrite the opening sentence in your own words after reading the test. If you do not, move that sentence into the `<details>` element and write one sentence yourself. Leave the disclosure as the single `<blockquote>`.

```markdown
An already loaded top-level document keeps `navigator.globalPrivacyControl` and `Sec-GPC` from when that document began loading.

<details>
<summary>Drafted notes on the requirement, the run, and issue 165</summary>

Working Draft section 3.2 caches the preference on each top-level navigation. A change during or after that navigation is not reflected until the next navigation. `gpcAtNavigation` reflects the preference when the active document began loading. Section 3.3 sends `Sec-GPC: 1` only when that boolean is true, and sends no header when it is false. Section 3.4 sets `navigator.globalPrivacyControl` to that boolean. Section 8.1 records the session preference and returns `{gpc}`. It does not mention `gpcAtNavigation`.

`navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html` set the preference and then open a new document. They do not read the document that was already loaded. This test does. It records that document, sets the opposite session value with the testdriver command, and asserts that the attribute and a later same-document subresource keep the value from when that document began loading.

The test does not assert the should-level reload prompt, and it does not create a worker. w3c/gpc#146 has no resolution on workers.

Editor Sebastian Zimmeck closed w3c/gpc#165 on 2026-11-19 by quoting the cache rule, including the sentence that a change is not reflected until the next navigation. He did not edit the specification. This test encodes the published Working Draft sentence. It does not encode the separate "best effort" sentence in that comment, and it does not change the specification.

`./wpt lint` on these two files passed against checkout `221a7fea449dcd9a42d5f249d5e4cf359a619d74`. `./wpt run chrome` on Chrome 157.0.8103.79 with `GlobalPrivacyControlApi` enabled failed the attribute assertion: expected false, got true. A separate local copy that asserted `Sec-GPC` first, and that is not part of this diff, failed that assertion too: expected null, got `"1"`. The header assertion in this file was not reached, because the attribute assertion failed first. Firefox and WebKit were not run. On 2026-11-20, `master` had moved to `8971ee02ffe8be3fa02862e0b07e1e37f34ab7a7`. The `gpc/` blobs this test depends on had not changed, and the lint was not re-run.

A failing Chrome result is the conformance observation. This diff adds no expectation metadata. Failure metadata, if a reviewer requires it, lives in a separate repository.

</details>

<blockquote>LLM use: an LLM drafted the test and the notes in the details element from the Working Draft, the existing gpc/ files, and the local ./wpt run above. The person who opens the pull request has read the test and is responsible for it.</blockquote>
```

## Commit message, for the person who commits

```text
Test that a GPC preference change waits for the next top-level load.

Existing gpc tests only observe documents opened after the preference
is set. The Working Draft already requires the loaded document to keep
gpcAtNavigation.

LLM use: an LLM drafted the test from the Working Draft and the current
gpc files. The human author is responsible for the change.
```

## What this pull request is not

- It is not an amendment to the Global Privacy Control specification.
- It is not a Working Group resolution. Closing issue 165 is an editor comment that quotes the current draft.
- It is not a Chromium bug. Do not open one in the same step. Open one later only if a reviewer asks.
- It is not acceptance. Acceptance is a merge to `web-platform-tests/wpt` `master`.
