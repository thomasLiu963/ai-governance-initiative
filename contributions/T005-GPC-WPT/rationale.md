# Why this test

## The requirement

Working Draft § 3.2 fixes `gpcAtNavigation` when the top-level browsing context's active document begins loading. A later preference change waits for the next navigation. § 3.3 and § 3.4 bind `Sec-GPC` and `navigator.globalPrivacyControl` to that boolean.

The set command updates the session preference and returns it. It does not contain a step that refreshes documents already loaded. A browser can return `{gpc: true}` from the command and still leave the loaded document at its cached value. The existing testdriver file already checks the return value. This test checks the document.

`window.open` is the positive control because a new auxiliary browsing context is a new top-level browsing context. Its document begins loading after the set, so § 3.2 requires it to sample the updated preference. The existing `navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html` already use that order. Keeping the opener alive is what lets one test see both the cached document and the new document. A reload of the same browsing context would also sample again, and would discard the document under test before both states could be asserted.

The subresource is one `fetch` of `support/sec-gpc-value.py`. The draft requires the header on the user agent's HTTP requests when `gpcAtNavigation` is true, and forbids the header when it is false. One same-document request is enough to see whether that boolean changed. The file does not repeat the image, iframe, script, and worker matrix in `getGPC.py`.

The echo reports the field value the server received. The assertion accepts JSON `null` when the attribute is false, and the string `1` when it is true. A value of `0`, an empty string, or a list fails. That matches the sender rules in § 3.3. It is not a receiver algorithm and it does not implement the combined-value rule still open in issue #114.

## Workers stay out

Issue #146 asks the group not to require user agents to push settings changes into workers. It has no editor decision. The draft still includes the mixin on `WorkerNavigator` and still defines the value as the top-level browsing context's `gpcAtNavigation`, which does not identify a service worker.

A worker assertion would pick one of those unresolved readings:

- a dedicated worker created before the change, reading a live `gpcAtNavigation` that itself does not update
- a worker that snapshots the session preference at creation and therefore might see the new value if it is created after the set and before the next navigation
- a service worker, which the current tests require and which editors have discussed removing

The navigation rule can be tested without any of those choices. `navigation-cache.https.html` and `navigation-cache-document.html` do not construct a worker. The patch does not edit the existing worker assertions, which apply to workers created by a document opened after the set.

## Why the test is a normal file

The caching sentences are already `MUST` requirements in the Working Draft. A `.tentative` name would mean the behavior is not specified yet. The file is `gpc/navigation-cache.https.html`, alongside the other secure `gpc/` tests.

ChromeDriver 157 with the API flag updates the loaded document immediately, and Chromium's `PrefChangeIsReflectedImmediately` expects that update for the profile setting. The test file still encodes § 3.2. It is held until an editor says that sentence remains the requirement. If the Working Group changes § 3.2 so a preference change is visible in the loaded document, this patch should be dropped rather than landed. Filing it before that answer would ask WPT to decide the question posed in `ISSUE.md`.

The should-level reload prompt is not asserted. The test also does not assert that the session preference and the loaded document match before the set. It records the document, sets the opposite boolean, and requires the document to keep the recorded value.

## What a conforming user agent does

After `set_global_privacy_control` resolves with the new session boolean:

- the already loaded top-level document keeps the same `navigator.globalPrivacyControl`
- a later subresource request from that document keeps the same `Sec-GPC` presence and value
- a top-level document that begins loading after the set exposes the new boolean and sends `Sec-GPC` from that boolean

The command's return value remains the new session preference. Restoring the previous session preference is cleanup so later tests in the same session are not left on the flipped value.

## Smallest patch

Three new files:

| Path | Role |
| --- | --- |
| `gpc/navigation-cache.https.html` | Records the loaded document, sets the opposite session preference, asserts that the document is unchanged, and opens the next top-level document. |
| `gpc/support/navigation-cache-document.html` | Asserts the new document's attribute and one subresource header. |
| `gpc/support/sec-gpc-value.py` | Returns `{"sec-gpc": <field value or null>}` with `Cache-Control: no-store`. |

`META.yml` and `WEB_FEATURES.yml` do not need edits. `getGPC.py` is left for pull request #64623.
