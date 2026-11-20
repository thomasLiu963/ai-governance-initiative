# Proposed Web Platform Test pull request

Not opened. Do not file until this text is approved. The human who opens it has to understand the test and be the author of the description. WPT's AI policy says model-written discussion in the pull-request body must be labelled and kept to a one-paragraph blockquote or a `<details>` element.

Repository: `web-platform-tests/wpt`, directory `gpc/`. License: 3-clause BSD. Suggested reviewers in `gpc/META.yml`: AramZS, bvandersloot-mozilla, j-br0, pes10k, SebastianZimmeck.

## Files to add

- `gpc/navigation-cache.https.html`
- `gpc/support/sec-gpc-value.py`

Do not add `navigation-cache-document.html`. A new top-level document is already covered by `navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html`. Those tests set the preference and then open a document. Neither reads the document that was already loaded.

## Official run, 2026-11-19

Checkout `221a7fea449dcd9a42d5f249d5e4cf359a619d74`. `./wpt lint` on the two files exited 0. `./wpt run -y chrome` used Chrome 157.0.8103.79 and `--enable-features=GlobalPrivacyControlApi`.

Simplified test, attribute checked first:

`assert_equals: the loaded document keeps its cached navigator.globalPrivacyControl expected false but got true`

Diagnostic copy that checked the header first, then deleted so it is not part of this pull request:

`assert_equals: a later same-document subresource keeps the cached Sec-GPC value expected (object) null but got (string) "1"`

The runner finished. Testdriver accepted the set command. Firefox and WebKit were not run. This checkout contains no test-expectation `.ini` files. A pull request will show an unexpected Chrome failure until Chrome changes or failure metadata is added elsewhere. That failure is the conformance result.

## Proposed title

```text
GPC: an already loaded document keeps the preference until the next top-level navigation
```

## Proposed body

```markdown
### What this tests

Working Draft section 3.2 caches the preference on each top-level navigation. A change during or after that navigation is not reflected until the next navigation. `navigator.globalPrivacyControl` and `Sec-GPC` follow `gpcAtNavigation`.

`navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html` set the preference and then open a new document. They do not read the document that was already loaded. This test does. It sets the opposite session value with the testdriver command and asserts that the loaded document's attribute, and a later same-document subresource, keep the value from when that document began loading.

Editor Sebastian Zimmeck closed w3c/gpc#165 on 2026-11-19 by quoting that cache rule, including the sentence that a change is not reflected until the next navigation. This test encodes that sentence. It does not encode the separate "best effort" sentence in that comment, and it does not change the specification.

### Run

`./wpt lint` passed. `./wpt run chrome` on Chrome 157.0.8103.79 with `GlobalPrivacyControlApi` enabled failed the attribute assertion: expected false, got true. A separate local copy that asserted `Sec-GPC` first failed that assertion too: expected null, got `"1"`. Firefox and WebKit were not run.

<blockquote>LLM use: an LLM drafted this description and the test from the Working Draft, the existing gpc/ files, and the local ./wpt run above. The person who opens the pull request has read the test and is responsible for it.</blockquote>
```
