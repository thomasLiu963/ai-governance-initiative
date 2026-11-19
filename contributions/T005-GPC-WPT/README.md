# T005 — GPC navigation-cache Web Platform Test

Status: local draft, 2026-11-18. Nothing in this directory has been submitted. No pull request, issue comment, or other external write was made.

## Conclusion

A conformance test for preference caching is technically required by the current Global Privacy Control Working Draft, and it is absent from the Web Platform Tests `gpc/` directory and from the open pull requests checked on 2026-11-18.

The draft says a preference change during or after a top-level navigation is not reflected until the next navigation. `gpcAtNavigation` is fixed when that browsing context's active document begins loading. `navigator.globalPrivacyControl` and `Sec-GPC` are both defined from that boolean. The existing tests call `test_driver.set_global_privacy_control` and only then open a new document, so they never observe the document that was already loaded.

The patch adds that missing observation and a new top-level document as the positive control. It does not create a worker. Worker behavior stays with the unresolved question in [w3c/gpc#146](https://github.com/w3c/gpc/issues/146). The `Sec-GPC` receiver algorithm in [w3c/gpc#114](https://github.com/w3c/gpc/issues/114) is unchanged and is not part of this patch. The 20-case Node header suite linked from that issue is not reused.

On this machine the test file was executed in Chrome 157.0.8103.79 with `GlobalPrivacyControlApi` enabled. The loaded document's attribute changed immediately (`expected false but got true`). The new top-level document passed and carried `Sec-GPC: 1`. That is a failure of the Working Draft's caching rule. Chromium's in-tree browser test `PrefChangeIsReflectedImmediately` expects the immediate update. The patch follows the Working Draft.

Default Chrome 157, Firefox, and Safari 17.6 on this Mac did not provide an implementation in which the caching assertions could be decided. Those runs are listed in [local-results.md](local-results.md).

## Packet

| File | Contents |
| --- | --- |
| [verification.md](verification.md) | Specification text, current tests, issue #146, open pull requests, and browser support that were checked. |
| [rationale.md](rationale.md) | Why this test matches the draft, why workers are separate, and why the parser issue is deferred. |
| [submission.md](submission.md) | Where the patch would go, the license, the AI-assistance rules, and the reviewers. |
| [local-results.md](local-results.md) | Which runs executed the test and which configurations are still waiting. |
| [patch/0001-gpc-navigation-cache.patch](patch/0001-gpc-navigation-cache.patch) | Three new files, ready for `git apply` on `web-platform-tests/wpt`. |

The same three files are also present as a tree under `patch/gpc/` so they can be read without applying the diff.

## Themes

Privacy and human agency. The cached boolean is how a person's do-not-sell-or-share request stays one value for the whole top-level document. A user agent that applies a later change inside that document lets the page and its subresources observe a different preference from the one in force when the document loaded.

## Not done

`MASTER_TRACKER.md` was not edited. `./wpt lint` and `./wpt run` were not used. No official Web Platform Tests result exists for this file.
