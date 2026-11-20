# GPC navigation-cache test

Status: suitable for a Web Platform Tests pull request. Not submitted. Do not open the pull request, a `w3c/gpc` pull request, or a Chromium bug from this packet.

## Decision

The two-file test is correct, meaningful, and not a duplicate. It is the right next artifact after issue 165. It is a test of the published Working Draft. It is not an amendment of that draft.

| Question | Answer |
| --- | --- |
| Does it encode a requirement that is actually in the draft? | Yes. Section 3.2 is a MUST. Sections 3.3 and 3.4 bind the header and `navigator.globalPrivacyControl` to `gpcAtNavigation`. Section 8.1 does not refresh an already loaded document. |
| Do the current `gpc/` tests already cover it? | No. They set the preference and then call `window.open`. None reads the document that was already loaded. Re-read on `master` `8971ee02` (2026-11-20). The five `gpc/` blobs named in `RESULTS.md` are unchanged. There is no `navigation-cache.https.html`. Open pull request 64623 edits only `getGPC.py`. |
| Did an official run exercise it? | Yes, on 2026-11-19, as recorded in `RESULTS.md`. Lint passed. Chrome 157 with the API flag failed the attribute assertion. This sprint did not re-run the runner. |
| Is a Chrome failure a reason to drop it? | No. The failure is the discrepancy the test exists to show. Chrome updates the loaded document immediately. The draft says the change waits for the next top-level navigation. |
| Does the editor's close of issue 165 adopt the test? | No. He quoted the existing rule and closed the issue. He did not edit the specification. |
| May this be filed as a specification pull request? | No. `w3c/gpc` `CONTRIBUTING.md` requires Working Group participation or a non-member patent licensing commitment for a substantive specification change. This workspace has neither. |

The should-level reload prompt is not asserted. Workers are omitted because issue 146 has no decision. The new-document half of the older three-file patch was removed so the pull request would not repeat the existing tests.

## Ordinary-language significance

Global Privacy Control is a browser signal a person can turn on to say "do not sell or share my data." The draft says that once a page has loaded, that page keeps the choice that was in effect when it loaded. A later change shows up on the next page, not in the middle of the page that is already open. The draft also says the browser should tell the person about tabs that are now out of date and offer to reload them.

Chrome, in the run above, does the other thing. Turning the signal on while a page is open changes what that page's script reads, and what its later requests send, without a navigation. A site can therefore see one choice on the first request and a different choice later in the same page.

This test asks browsers to follow the draft's rule for the page that is already open. If it is merged, it becomes one file in the shared browser test suite. Chrome will show a failure until Chrome changes or the draft changes. Merging the test does not change the specification, does not make Chrome comply, and does not create a legal duty.

## Claims that would be false

- "I amended the W3C Global Privacy Control specification." This packet adds a test. The specification text is unchanged.
- "The editor adopted the test." He quoted the draft and closed a question.
- "Chrome was fixed." Chrome failed the test.
- "This is a W3C Recommendation." Global Privacy Control is a Working Draft. Publication as a Working Draft is not an endorsement.

## Files

| File | Role |
| --- | --- |
| `gpc/navigation-cache.https.html` | The test that was linted and run |
| `gpc/support/sec-gpc-value.py` | Echoes the `Sec-GPC` field, or JSON `null` when it is absent |
| `0001-gpc-navigation-cache.patch` | The exact two-file diff |
| `PULL_REQUEST.md` | Title, body, commit message, and the limits on what may be filed |
| `RESULTS.md` | The run record and the re-check of the draft and the repository |

## Themes

Privacy and human agency. The cached value is how one do-not-sell-or-share choice stays stable for the whole top-level page.

## Next step

Approve or edit `PULL_REQUEST.md`. The human who opens the pull request re-reads the test, keeps the disclosure blockquote, and files only those two files. A reviewer who wants a Chromium bug can ask for one after that. Do not open the bug first.
