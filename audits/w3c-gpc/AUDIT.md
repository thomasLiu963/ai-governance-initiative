# W3C Global Privacy Control — technical audit

Audit date: 2026-11-18. Status of this file: local decision record. Nothing in it has been submitted upstream, and nothing here is an acceptance.

## Recommendation

Prepare two drafts for internal review by 2026-11-30, and hold both until Thomas explicitly approves an external comment or pull request.

1. **Receiver algorithm for a combined `Sec-GPC` value** ([w3c/gpc#114](https://github.com/w3c/gpc/issues/114)). This is the clearest normative defect. The current sentence honors duplicate `Sec-GPC: 1` lines and ignores the same bytes once an HTTP stack has combined them into `1, 1`. Anne van Kesteren has already said the parser has to operate on the combined value. Peter Snyder has said pull requests are welcome and that the editors otherwise plan the work for after version 1.
2. **A Web Platform Test that the preference is cached until the next top-level navigation**, with a short note on [w3c/gpc#146](https://github.com/w3c/gpc/issues/146) about workers. The caching requirement is already normative, and the existing tests always navigate after changing the preference, so they never observe a same-document update. The test can be written against the current text. The worker rule should stay a question until the editors choose between removing the service-worker attribute and defining a snapshot.

Offer the small TAG wording in candidate 4 only if [w3c/gpc#164](https://github.com/w3c/gpc/issues/164) is still empty when a submission is approved. The four editors assigned that issue on 2026-11-05, and a competing pull request would collide with work they scheduled for wide review.

Do not propose a purpose-conditional signal, an AI-training opt-out, or a stronger GDPR reading. Those are open debates the group has not asked an outside contributor to settle, and they are new policy frameworks rather than repairs to the protocol.

## Document read

| Item | Status | Locator |
| --- | --- | --- |
| Global Privacy Control (GPC) | W3C Working Draft, 24 September 2026. Recommendation track. Privacy Working Group. Publication as a Working Draft is not an endorsement. | https://www.w3.org/TR/gpc/ and the dated copy https://www.w3.org/TR/2026/WD-gpc-20260924/ |
| Editor's draft source | `index.html` on `main`. Repository `pushed_at` 2026-09-24T16:56:10Z, the same day as the Working Draft. | https://github.com/w3c/gpc/blob/main/index.html and https://w3c.github.io/gpc/ |
| Repository classification | `w3c.json`: `group` `wg/privacy`, `repo-type` `rec-track`, contact Tara Whalen (`tjwhalen`). | https://github.com/w3c/gpc/blob/main/w3c.json |
| Legal and Implementation Considerations Guide | Same repository, `explainer.md`. The guide says it is for reference and is not legal advice. It is not a separate Recommendation. | https://w3c.github.io/gpc/explainer |
| Web Platform Tests | `gpc/` on `master`: testdriver, IDL harness, `navigator.globalPrivacyControl`, and `Sec-GPC` coverage, including dedicated, shared, and service workers. | https://github.com/web-platform-tests/wpt/tree/master/gpc |

No open pull requests were listed on `w3c/gpc` at the time of this audit. Eight issues were open: #164, #162, #146, #143, #138, #125, #114, and #93.

## Contribution route and AI-assistance policy

**Specification repository.** [CONTRIBUTING.md](https://github.com/w3c/gpc/blob/main/CONTRIBUTING.md) says substantive contributions are intended for Recommendation-track documents under the [W3C Patent Policy](https://www.w3.org/policies/patent-policy/) and the [W3C Software and Document License](https://www.w3.org/copyright/software-license/). A substantive contributor must participate in the Privacy Working Group or make a non-member patent licensing commitment. Multi-author pull requests must list other contributors with `+@github_username`.

The Privacy Working Group IPR page says the same thing for non-participants: staff contacts provide instructions for recording a royalty-free commitment before the contribution can be accepted. Non-substantive fixes, such as a typo, can be marked non-substantive. https://www.w3.org/groups/wg/privacy/ipr/ and https://www.w3.org/guide/process/non-participant-commitment.html

This workspace has no record that a participant affiliation or a non-member commitment exists. A spec pull request is therefore not the first step. A short comment on an existing issue is the step that can be reviewed before any patent machinery is invoked.

**Tests.** [web-platform-tests/wpt CONTRIBUTING.md](https://github.com/web-platform-tests/wpt/blob/master/CONTRIBUTING.md) licenses contributions under the 3-clause BSD license and points to the WPT code of conduct. `gpc/META.yml` suggests review by AramZS, bvandersloot-mozilla, j-br0, pes10k, and SebastianZimmeck. That file does not state an AI-assistance rule. The rest of the WPT documentation site was not read for a separate AI rule.

**AI assistance.** `CONTRIBUTING.md` in `w3c/gpc` contains no AI rule. Two public W3C documents do:

- [Use of Large Language Models in Standards Work](https://www.w3.org/TR/llms-standards/), W3C Group Note, 24 March 2026. The Note says the Advisory Board endorsed it and that W3C itself has not. A person remains responsible for the output and should label content that is primarily model output.
- [Draft policy on AI tools in W3C standardization](https://www.w3.org/2026/10/draft-ai-policy.html). The page says it is not yet a W3C policy. Its draft rules are: a human reviews and owns the contribution, AI use that generated the substance is disclosed, a human answers review comments, and contributors do not use a model to produce a high volume of unsolicited text.

Observed practice on this repository: pull request #152 requested a GitHub Copilot review on the day it opened. That review is a bot comment, not a group policy.

Any later submission that uses this audit should be short, tied to the existing issue, written so a person can defend every sentence, and labeled as AI-assisted where the draft policy's disclosure sentence applies. No submission should be sent by an automated account.

## Themes

Every candidate below serves **privacy** and **human agency**: the signal is how a person asks sites not to sell or share data, and the gaps are places where that request can be dropped, mismatched, or read differently by two implementations. Candidate 4 also serves **transparency**, because a header and a script property that disagree expose a preference the person did not separately choose. No candidate depends on a claim about model behavior. Local `research/D1/`, `research/D2/`, and `research/incident-evidence/` contained no files on 2026-11-18, so no prior finding is available to attach.

## #151 and #152

Both are closed.

- [#151](https://github.com/w3c/gpc/issues/151), opened 2026-08-05 by Ari Chivukula (`arichiv`, GitHub company `@googlers`, bio "Google Chrome"). The issue says the WebDriver set command in the Working Draft returned null, while `gpc/global_privacy_control.testdriver.html` expects `{gpc: boolean}`.
- [#152](https://github.com/w3c/gpc/pull/152), opened 2026-08-05 by the same author, merged 2026-09-17. Diff size recorded by the API: +3/−2. Copilot commented on 2026-08-05. The author asked Benjamin VanderSloot's account for review on 2026-09-07 and Justin Brookman on 2026-09-11. Peter Snyder (`pes10k`) approved on 2026-09-17 and the pull request merged the same day. Later approvals on 2026-11-14 by `expertayaz651-web` are after the merge and are not treated as the review that accepted it.

The editor's draft now returns a JSON object with a `gpc` property from both the set and get commands (`index.html` lines 559–566 and 590–595). The return-value mismatch is resolved.

One residual remains in the merged text. Step 5 says `Return [=success=] with data `result``. The variable was introduced as `|result|`. Copilot's 2026-08-05 comment said the backtick form reads as the literal string `result`. The approval did not change that line, and the 24 September 2026 Working Draft still shows it. This is an editorial defect in an algorithm step. It is too small to be its own candidate. It can be corrected in passing if an automation edit is otherwise wanted.

## Review history that was actually retrieved

Dates below come from the GitHub API. "First review" is the first review event or substantive comment returned for that pull request. Empty author logins are reported as empty. Acceptance rates are not inferred from this sample: it includes closed-unmerged pull requests, and it is not a complete history of the repository.

### Merged, substantive

| PR | Author and role as verified | Opened | First review | Merged | What the record shows |
| --- | --- | --- | --- | --- | --- |
| [#152](https://github.com/w3c/gpc/pull/152) | Ari Chivukula, implementing Chrome's WPT-facing GPC support, per #151 | 2026-08-05 | Copilot comment same day. First human approval: Peter Snyder, 2026-09-17 | 2026-09-17 | 43 days. Human approval and merge were the same day, after two unanswered review requests. |
| [#160](https://github.com/w3c/gpc/pull/160) | Don Marti (`dmarti`), invited expert on the Privacy WG IPR list; author of the security self-review | 2026-09-20 | Sebastian Zimmeck approved 2026-09-24 | 2026-09-24 | 4 days. Editor-to-editor. |
| [#145](https://github.com/w3c/gpc/pull/145) | Peter Snyder, editor and WG chair, per the TAG review request | 2026-04-30 | Approval recorded 2026-05-06 with a blank author login. Justin Brookman requested changes 2026-05-27 | 2026-06-11 | 42 days. `bvandersloot-mozilla` approved 2026-06-09. |
| [#112](https://github.com/w3c/gpc/pull/112) | Tim Ledbetter (`tcl3`). GitHub profile: Ladybird browser maintainer | 2025-11-05 | `bvandersloot-mozilla` approved the same day | 2026-02-18 | Same-day approval, merge 105 days later. |
| [#105](https://github.com/w3c/gpc/pull/105) | `bvandersloot-mozilla`. Git commit metadata on the WPT tests names Benjamin VanderSloot. The profile itself has no company field | 2025-06-02 | Sebastian Zimmeck approved 2025-09-04 | 2025-09-04 | 94 days, one human approval, on the merge day. This added the automation section. |
| [#108](https://github.com/w3c/gpc/pull/108) | Robin Berjon (`darobin`), long-standing editor commits on this repository | 2025-09-16 | Don Marti commented 2025-09-17 | 2026-02-19 | About five months, with comments from Jeffrey Yasskin through 2026-02-18. |

### Closed without merge

| PR | Author | Opened | First response retrieved | Closed | Disposition in the record |
| --- | --- | --- | --- | --- | --- |
| [#104](https://github.com/w3c/gpc/pull/104) | Jeffrey Yasskin (`jyasskin`) | 2025-05-14 | Martin Thomson commented 2025-05-15. `bvandersloot-mozilla` requested changes 2025-05-16 | 2025-08-08 | Justin Brookman: the 7 August 2025 WG meeting merged the alternative, #107. |
| [#102](https://github.com/w3c/gpc/pull/102) | Jeffrey Yasskin | 2025-04-22 | Don Marti commented 2025-04-24. Robin Berjon objected 2025-04-30 | 2025-08-08 | Same meeting. Closed in favor of #107. |
| [#147](https://github.com/w3c/gpc/pull/147) | `wongchaiyatham-max`, draft, body text "Controller+v+tab" | 2026-05-21 | Justin Brookman, 2026-06-03, preferred the already-open editor pull request #145 | 2026-07-13 | Superseded. A parallel edit of text an editor is already changing was declined. |
| [#98](https://github.com/w3c/gpc/pull/98) | `chrisn` | 2025-02-20 | No review events in the API payload | 2025-09-04 | Author closed it: little WG interest. |
| [#68](https://github.com/w3c/gpc/pull/68) | `loganaden` | 2024-02-06 | Martin Thomson commented 2024-02-06 | 2024-03-22 | Author moved the material to the explainer. Closed as superseded by #71. |

Two patterns are verified. Editorial or editor-authored text can merge in days (#160) or wait months after approval (#112). Semantic redefinitions of what the signal means (#102, #104) drew objections from implementers and were replaced by a narrower edit the working group chose in a meeting. A draft that duplicates an editor's open pull request (#147) was asked to stand down.

### Tests

| PR | Author | Opened | First human review | Merged |
| --- | --- | --- | --- | --- |
| [wpt#54446](https://github.com/web-platform-tests/wpt/pull/54446) testdriver extension | `bvandersloot-mozilla` | 2025-08-21 | `jgraham` commented 2025-09-04, approved 2025-09-22 | 2025-09-22 |
| [wpt#55796](https://github.com/web-platform-tests/wpt/pull/55796) Gecko signal tests | `moz-wptsync-bot`, Gecko bug 1969865 | 2025-10-31 | `wpt-pr-bot` approved the same day. No other reviewer in the payload | 2025-11-02 |

Commit history on `wpt/gpc`: Benjamin VanderSloot added the tests on 2025-10-30 (`f564d65`), `pstanciu` reverted them the same day because `sec-gpc.https.html` failed (`3c910a5`), and the tests were re-landed on 2025-10-31 (`d5d5da0`). The first landing was not clean.

## Interoperability that was verified, and what was not

Verified from primary sources opened for this audit:

- The Working Draft requires one cached boolean, `gpcAtNavigation`, on each top-level browsing context. The user agent sends `Sec-GPC: 1` only when that boolean is true, and `navigator.globalPrivacyControl` must equal that boolean. A change is not reflected until the next top-level navigation (`index.html` lines 212–229, 250–256, 318–319).
- `WorkerNavigator` includes the mixin (`index.html` lines 307–311). The value is still defined as "the top-level browsing context's `gpcAtNavigation`," which does not name a browsing context for a service worker.
- Fetch already treats a request header whose name starts with `sec-` as a [forbidden request-header](https://fetch.spec.whatwg.org/#forbidden-header-name) (WHATWG Fetch, section read from `fetch.bs` lines 1205–1268). Script-set `Sec-GPC` is already rejected by Fetch. The GPC draft does not mention that.
- WebKit pull request [64077](https://github.com/WebKit/WebKit/pull/64077) merged 2026-05-16 and adds GPC. Pull request [69606](https://github.com/WebKit/WebKit/pull/69606) merged 2026-07-23. Its description says the attribute is exposed only when an embedder enables it through `WKWebpagePreferences`, and that the value is copied into shared and service workers at initialization rather than taken from a live global preference.
- Chromium "Intent to Prototype: Global Privacy Control," Maciej Czarnecki, 6 January 2026, on blink-dev. No milestone is given. Mike West's 8 January 2026 reply supports a Blink prototype and leaves user-interface decisions to embedders. Tracking bug: https://issues.chromium.org/issues/40745270. Ari Chivukula's 5 August 2026 issue #151 says a Chrome WPT-facing change was in review at `crrev.com/c/8186637`. That code review was not opened for this audit.
- Mozilla's standards-position issue [867](https://github.com/mozilla/standards-positions/issues/867) is closed with the label `position: positive` (closed 2025-05-15). The WPT files above were synced from Gecko bugs.

Not established:

- Stable-release shipping status for Chrome, Edge, Safari, or Firefox. A compat-data page was not successfully retrieved. A news article that describes an Edge setting was not used.
- A complete wpt.fyi comparison. A search response on 2026-11-18 showed an Edge 159.0.4393.0 experimental run passing the listed `gpc` files (testdriver 1/1, IDL harness 19/19 on window, worker, shared worker, and service worker, navigator 8/8, `sec-gpc` 16/16). The Chrome 160, Firefox 162, and Safari 256 preview runs in that same response recorded zero subtests for those files. Empty counts are neither passes nor failures. A second results-API call did not return the `gpc` rows.
- Brave and Cromite behavior. The January 2026 Chromium intent describes preference keys in those projects. Their source was not read.

## Ranked candidates

### 1. Define the `Sec-GPC` receiver on the combined field value

1. **Gap.** In the header section, a server must ignore `Sec-GPC` unless the field value is exactly the character `1`. If multiple headers are present and at least one value is exactly `1`, the server must treat the request as a single `Sec-GPC: 1`. Source: Working Draft section "The `Sec-GPC` Header Field for HTTP Requests," and `index.html` lines 263–268. Issue: https://github.com/w3c/gpc/issues/114, opened 2025-11-14 by Anne van Kesteren (`annevk`, GitHub company `@apple`), assigned to Peter Snyder, still open, 11 comments.
2. **Evidence it is still open.** There is no pull request linked from the issue. The assignee's 22 October 2026 comment says pull requests are welcome and that the editors otherwise plan this for after version 1, because version 1 work is the TAG review. On 23 October 2026 Anne van Kesteren wrote: "The parser needs to operate on the combined value." `autoCAT6` posted Node 24 and Node 25 observations on 23 October 2026 and an updated note on 25 October 2026. That note records behavior. It does not propose specification text. No later comment assigns the writing to anyone else.
3. **Consequence.** HTTP implementations routinely combine repeated field lines. Two conforming-looking lines, `Sec-GPC: 1` and `Sec-GPC: 1`, become one value `1, 1`. Under the current exact-match sentence that combined value is ignored, so a duplicated opt-out is processed as no opt-out. The multiple-header sentence and the exact-match sentence disagree about the same bytes depending on whether combination has already happened. A site that uses `headers.get("sec-gpc") == "1"` drops the signal. That is the failure mode Mark Nottingham described on the earlier thread cited in #114.
4. **Proposed change.** Replace the multiple-header paragraph with one receiver algorithm. Input is the combined field value. Split on commas. If any item is exactly `1` after leading and trailing whitespace is removed, the request carries the preference; otherwise the server ignores the field. Keep the sender rule unchanged: a user agent still sends a single field whose value is exactly `1`, and still must not send duplicates. Do not switch the wire format to a structured-field boolean (`?1`). Existing senders emit `1`. The whitespace trim is a proposal that #114 has not yet confirmed; the combined-value requirement has been confirmed. Examples that belong in the draft: `1` honors; `1, 1` honors; `1, 0` honors; `0` ignores; empty ignores.
5. **D1, D2, or incident evidence.** None is on file. The candidate does not need any.
6. **Experiment.** A new browser experiment is not required to show the contradiction. A local string check on 2026-11-18 applied the current "some field value is exactly `1`" rule and a comma-split rule:

    | Input the current rule sees | Current rule | Same bytes read as one combined value |
    | --- | --- | --- |
    | `1` | honor | honor |
    | two values, `1` and `1` | honor | honor (`1, 1`) |
    | two values, `1` and `0` | honor | honor (`1, 0`) |
    | one value already equal to `1, 1` | ignore | honor |
    | `1 ` with a trailing space | ignore | honor, only if trim is included |
    | `0` or empty | ignore | ignore |

    `autoCAT6`'s public Node table already shows both "two `Sec-GPC: 1` lines" and "one `Sec-GPC: 1, 1` line" surfacing as `"1, 1"` from `req.headers['sec-gpc']`. Repeating that Node run would not add a fact. A browser run would matter only if the contribution claimed that a particular browser combines or rejects these values. This audit does not claim that.
7. **Effort and API cost.** One to two days for a comment that contains the algorithm and the examples, plus a patch only after the assignee agrees. No paid API. No new browser feature.
8. **Route, AI policy, review history.** Comment on #114 first. A specification pull request is substantive and needs working-group participation or a non-member licensing commitment. Disclose AI assistance under the draft W3C note above. Comparable normative edits in the sample took 42 days (#145) to about five months (#108). The assignee has also said this is otherwise post-version-1, which is a real chance the group will defer it.
9. **Deadlines.** By 2026-11-30 the deliverable is a one-page algorithm, ready for internal review, still local. By 2027-02-15, if submission is approved, a realistic outcome is a comment on #114 and a reply from the assignee or from Anne van Kesteren. A merge before 15 February is possible only if the editors treat the combined-value bug as version-1 text. Their October comment points the other way. Do not plan on a merge.
10. **Accurate accomplishment, if it later lands.** "The GPC Working Draft's receiver rule now evaluates the combined `Sec-GPC` field value, so a duplicated `1` is still an opt-out after ordinary HTTP header combination." That sentence is not true today.
11. **Evidence that would establish it.** A merged commit on `w3c/gpc` that changes the paragraph at `index.html` lines 263–268, a Working Draft or editor's draft that contains the new algorithm, and the closing comment on #114.

### 2. Say which worker sees `gpcAtNavigation`, and that a running worker need not update live

1. **Gap.** `WorkerNavigator` includes `GlobalPrivacyControl`, and the attribute must be the top-level browsing context's `gpcAtNavigation` (`index.html` lines 307–319). A service worker, and a shared worker used by more than one top-level browsing context, has no single top-level browsing context in that sentence. Separately, the set-command records a session preference (`index.html` lines 561–564) while the caching section says a change waits for the next top-level navigation (lines 212–214). Issue [#146](https://github.com/w3c/gpc/issues/146), Anne van Kesteren, 2026-05-12, label `agenda+`, no assignee and no comments: user agents do not synchronize settings changes into workers, and this feature should not be the one that requires it.
2. **Evidence it is still open.** #146 has no comments and no linked pull request. The TAG review ([w3ctag/design-reviews#1265](https://github.com/w3ctag/design-reviews/issues/1265), Brian Kardell, 2026-09-02) asked how shared and service workers obtain `gpcAtNavigation`. Sebastian Zimmeck replied on 2026-09-28 that the editors' working view was to remove the signal from service workers and keep it for workers tied to one document. The 24 September 2026 draft still includes `WorkerNavigator`. Issue #157, opened by Peter Snyder on 2026-09-10 to add service-worker support, was closed the same day as "non-issue (my error)," which confirms the mixin was already on `WorkerNavigator`. The TAG closed the review on 2026-10-16 as "satisfied with concerns" and treated the worker discussion as already underway. #164, the follow-up punch list, does not include the worker item. WebKit pull request 69606, merged 2026-07-23, describes the opposite of removal: the value is carried into service and shared workers at initialization. The WPT file `gpc/support/navigator-globalPrivacyControl.html` expects a service worker's `navigator.globalPrivacyControl` to equal the value set before the new window opened. No open issue records a decision between those three facts.
3. **Consequence.** A site that trusts `navigator.globalPrivacyControl` inside a service worker can see a value the specification does not define. Two implementations can both claim conformance: one omits the attribute, one snapshots it, one would update live. Anne van Kesteren's request is that a live update not be required. WebKit's merged description already implements a snapshot. The WPT suite currently requires the attribute to be present and equal to the post-navigation value, including in a service worker, so a browser that followed the editors' 28 September removal note would fail tests that another implementer is targeting. Ari Chivukula's #151 says Chrome was implementing those tests.
4. **Proposed change.** A comment on #146, copied to the TAG thread, with two questions and one proposed rule for the case the group already agrees on. Dedicated workers, and a shared worker created from one document, expose the owning document's `gpcAtNavigation` as it was when the worker was created. A later preference change does not have to update that worker or the already loaded document. For service workers, ask the editors to confirm or withdraw the 28 September removal, given WebKit 69606 and the current WPT. Do not open a pull request that deletes the service-worker exposure until that confirmation is in the issue. After a choice, the WPT change is mechanical: keep the dedicated-worker assertion, and either drop the service-worker assertion or state which snapshot it reflects.
5. **D1, D2, or incident evidence.** None.
6. **Experiment.** No new experiment is required to show that the sentence fails to name a browsing context for a service worker. That is a reading of `index.html` lines 318–319. A runtime experiment would be needed only to claim what a shipping browser returns inside a service worker. This audit did not run that test. The smallest useful one, later, is the navigation-cache test in candidate 3, plus one service-worker probe in a browser that already implements the attribute. It should wait until the editors answer #146, so the test encodes a chosen rule.
7. **Effort and API cost.** Two to four days for the comment and a draft paragraph. Test updates are another one to two days after the choice. No paid API.
8. **Route, AI policy, review history.** #146 is already `agenda+`, so the review path is a working-group call rather than a cold pull request. The spec edit is substantive and needs the patent route in `CONTRIBUTING.md`. The WPT half uses the BSD test suite and the reviewers in `gpc/META.yml`. #147 is the cautionary sample: an outside pull request that rewrote text an editor was already changing was declined. Here the editors have stated a leaning and have not landed it, so the comment should ask them to confirm that leaning against the WebKit and WPT evidence.
9. **Deadlines.** By 2026-11-30: the comment text and the two options, locally. By 2027-02-15, if approved: the comment can be on the agenda. A merged spec change is plausible only after a meeting. The sample says a meeting-backed edit can still take from six weeks to several months. A February merge is possible and should not be the success criterion.
10. **Accurate accomplishment, if it later lands.** "The GPC draft now states whether a service worker exposes `globalPrivacyControl`, and it states that a preference change does not have to update an already-running worker." Not true today.
11. **Evidence.** A comment on #146 from an editor choosing one option; a merged change to the mixin or to the value rule in `index.html`; and, if tests change, a merged WPT pull request that matches that sentence.

### 3. Add the missing navigation-cache conformance test

1. **Gap.** The draft says a preference change during or after a top-level navigation is not reflected until the next navigation (`index.html` lines 212–214). The WPT tests do the opposite order. `navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html` call `test_driver.set_global_privacy_control`, then `window.open` a new document, and assert the new document, its subresources, and the workers it creates. Nothing asserts that the already loaded document keeps the old `navigator.globalPrivacyControl` and that a same-document subresource keeps the old `Sec-GPC`. `global_privacy_control.testdriver.html` checks only the WebDriver get and set return values.
2. **Evidence it is still open.** The files above were read from `web-platform-tests/wpt` `master` on 2026-11-18. No later test in `gpc/` asserts same-document stability. #146 is the specification-side request that dynamic worker updates not be required; it does not contain a test. No open WPT pull request for this assertion was found in a repository search for "Global Privacy Control."
3. **Consequence.** A browser that applies `set_global_privacy_control` immediately to the current document still passes the suite, because every assertion runs in a document created after the set. The caching requirement, which exists so a page sees one preference for the whole navigation, has no failing test. That also hides disagreement with the WebDriver set command, whose steps say to record the session preference so that the browser will perform do-not-sell-or-share interactions, without saying "on the next navigation."
4. **Proposed change.** One new testharness file under `wpt/gpc/`:
    - Read `navigator.globalPrivacyControl` and the `Sec-GPC` value on a same-document subresource.
    - Call `test_driver.set_global_privacy_control` with the opposite boolean.
    - Assert the current document's attribute is unchanged, and assert a second same-document subresource still carries the original header value.
    - `window.open` a new top-level document and assert that document's attribute and header carry the new value.
    - Create a dedicated worker before the set, and assert that worker's attribute is unchanged. This is the #146 behavior. Keep the service-worker case out of this test until candidate 2 is decided.
5. **D1, D2, or incident evidence.** None.
6. **Experiment.** The test is the experiment. The smallest rigorous version is the file above, run once in a browser that implements the testdriver extension. This audit did not run it. If the browser fails the same-document assertions, that result is evidence for #146 and for a clarification of the set command. It is a reason to discuss the test before landing it as a hard failure, and it is also the point of writing it. A second browser is enough to see whether the failure is idiosyncratic. No paid API.
7. **Effort and API cost.** One to two days, including the subresource handler. No paid API. The test reuses `testdriver.js` commands that already exist.
8. **Route, AI policy, review history.** Destination is `web-platform-tests/wpt`, directory `gpc/`, not `w3c/gpc`. License: 3-clause BSD, from the WPT `CONTRIBUTING.md` retrieved for this audit. Suggested reviewers are listed in `gpc/META.yml`. The closest review sample is wpt#54446: opened 2025-08-21, first human comment 2025-09-04, approved and merged 2025-09-22 by `jgraham`. The Gecko signal tests were reverted once for failures at `sec-gpc.https.html` before they stuck, so a new test should be run locally before it is proposed. AI disclosure follows the draft W3C note if the group treats WPT as standardization work; the WPT `CONTRIBUTING.md` itself, as fetched, has no AI clause. No patent commitment is stated in that file. A specification change is not part of this candidate.
9. **Deadlines.** By 2026-11-30: the test file, run locally if a browser with the testdriver extension is available, still unsubmitted. By 2027-02-15, if approved: a WPT pull request can realistically be in review. The #54446 timeline was about a month to merge for a Mozilla author with a single reviewer. An outside author, and a test that fails an implementation, can take longer. A February merge is a reasonable hope and not a fact.
10. **Accurate accomplishment, if it later lands.** "The GPC Web Platform Tests now fail a browser that changes `Sec-GPC` or `navigator.globalPrivacyControl` in the current document before the next top-level navigation." Not true of the suite today.
11. **Evidence.** The merged file on `web-platform-tests/wpt` `master`, the pull request review thread, and a wpt.fyi result for that file with a non-empty subtest count. An empty count, as seen for several browsers in the 18 November search response, would not establish a pass or a fail.

### 4. Write the two TAG sentences that the draft does not already contain

1. **Gap.** [#164](https://github.com/w3c/gpc/issues/164), opened 2026-11-05 by Sebastian Zimmeck, assigned to Peter Snyder, Aram Zucker-Scharff, Sebastian Zimmeck, and Justin Brookman. It quotes three items from the TAG's 16 October 2026 close comment on design-reviews#1265:
    - The header and the JavaScript property must reflect the same cached value, and a mismatch is a fingerprinting surface. Jeffrey Yasskin's point, recorded in the issue, is that an extension which changes only the attribute makes the user more fingerprintable.
    - Private-browsing behavior is unspecified, including whether the header's presence reveals private-browsing mode or a per-domain setting.
    - The header is unsettable via Fetch.

    The first consistency requirement is already the consequence of lines 250–256 and 318–319, both of which bind to `gpcAtNavigation`. What is absent is an explicit statement that the two surfaces must not diverge, and a sentence in the privacy considerations (`index.html` lines 516–525) that a divergence is itself identifying. The Fetch fact is true in the Fetch standard and absent from this draft. Private browsing was discussed in closed issue #34; the last comment retrieved there, Justin Brookman on 2025-02-04, points at explainer pull request #96, which merged into the guide. The specification still has no private-browsing sentence, which matches the TAG's "could perhaps" wording.
2. **Evidence it is still open.** #164 has zero comments. No open pull request on the repository touches it. The 24 September 2026 draft's privacy section discusses fingerprinting from the existence of the signal. It does not discuss fingerprinting from disagreement between the header and the attribute. The security section (`index.html` lines 528–531) says there are no known security impacts. Fetch's forbidden-header rule was read separately and is not cited.
3. **Consequence.** Wide review is the group's stated path toward Candidate Recommendation (#138, opened 2026-02-16, still open). The TAG closed "satisfied with concerns" and listed these items. Leaving them unaddressed keeps that concern on the record. The practical privacy consequence is narrower than candidates 1 and 2: a user agent or extension that forges one surface and not the other creates a third bucket of users, distinct from both "signal on" and "signal off." Fetch already prevents a page script from setting the header; the missing sentence is documentation for implementers, not a new enforcement mechanism.
4. **Proposed change.** Two short paragraphs, offered as a comment on #164 rather than as a pull request, so the assigned editors can paste or reject them:
    - In privacy considerations: for a given document, the `Sec-GPC` header the user agent would send and `navigator.globalPrivacyControl` must both be the cached `gpcAtNavigation` of that document's top-level browsing context. A user agent exposes a fingerprinting surface if those two observations disagree.
    - In the header section: `Sec-GPC` is a forbidden request-header for Fetch because the name is byte-lowercase `sec-` followed by more characters, citing Fetch's forbidden-request-header definition. Pages cannot set it with `fetch()` or `XMLHttpRequest`.
    - Optional third sentence, non-normative: this specification does not require a distinct private-browsing value, and user agents should avoid a header presence or absence that exists only in private browsing. This sentence is weaker. The TAG used "could perhaps." Include it only if the editors want all three boxes checked in one pass.
5. **D1, D2, or incident evidence.** None. The fingerprinting concern is the TAG's, quoted in #164.
6. **Experiment.** Not required for the wording. The Fetch classification was checked by reading the Fetch source. A page-level `fetch()` trial would only reconfirm a rule Fetch already states, and only in browsers that implement that rule. Skip it unless an implementer disputes the citation.
7. **Effort and API cost.** Half a day to one day. No paid API.
8. **Route, AI policy, review history.** Comment on #164. If the editors ask for a pull request, the privacy and Fetch sentences are substantive enough that the patent commitment applies; a typo-only patch would not. The collision to avoid is #147: four named editors already own this issue, and it is thirteen days old. #160 shows that editor-authored review text can merge in four days once an editor is driving it. An outside pull request has no such sample.
9. **Deadlines.** By 2026-11-30: the two paragraphs, local, ready to paste if #164 is still empty. By 2027-02-15: this is the candidate most aligned with work the editors have already scheduled. A merge is realistic if an editor adopts the text. It is not realistic to promise, because #112 was approved in a day and merged 105 days later.
10. **Accurate accomplishment, if it later lands.** "The GPC draft now says that a mismatch between `Sec-GPC` and `navigator.globalPrivacyControl` is a fingerprinting surface, and it cites Fetch's rule that script cannot set `Sec-GPC`." The Fetch behavior itself would remain Fetch's rule. This draft would only cite it.
11. **Evidence.** A merged edit to the privacy section and the header section, and #164's first checkbox and third checkbox marked done by an editor. The private-browsing checkbox is a separate, optional sentence.

## Considered and not recommended

- **Purpose-conditional `Sec-GPC` ([#143](https://github.com/w3c/gpc/issues/143)).** An extension author reports sending the header per site and per purpose. Sebastian Zimmeck called the idea interesting on 2026-05-23 in connection with a draft EU Digital Omnibus text. The specification deliberately has no extension mechanism (`index.html` lines 285–289) and defines one global preference. This would be a new protocol. The group has not asked for a proposal.
- **Stronger GDPR text ([#93](https://github.com/w3c/gpc/issues/93)).** Open since 2025-01-20, 15 comments. Michael Kleber objected to stating a GDPR interpretation as fact while the Digital Omnibus is unfinished. Robin Berjon argued that the specification should state web semantics and leave the legal mapping to others, and pointed at the since-merged #108. A 2026 research paper and a personal explainer draft are linked from the thread. Rewriting the legal section would repeat a debate the editors have already narrowed.
- **Explainer guidance on other opt-out rights ([#125](https://github.com/w3c/gpc/issues/125)).** Nick Doty asked whether the guide should say that a different right needs a different mechanism. Justin Brookman replied on 2025-12-18 that the specification and the guide already say GPC is not every privacy right. There is no agreed missing sentence.
- **An AI-training or model-opt-out use of GPC.** The introduction and the legal-effects section say the signal is for sale, sharing, and cross-context targeted advertising, and that it is not deletion, same-context use, or every privacy right. #125 is the group's place for "different right, different mechanism." Attaching an AI-training meaning would be a new framework the repository does not support.
- **Re-fixing the WebDriver return value.** #151 and #152 are done.
- **The backtick `` `result` `` step.** Real, and left in place after the Copilot comment. Worth a one-line correction inside some other automation edit. On its own it does not meet the contribution bar.
- **The doubled "the the" in the intermediary sentence** (`index.html` line 273). Editorial only.
- **Internationalization checklist ([#162](https://github.com/w3c/gpc/issues/162)).** Justin Brookman already filled the short checklist on 2026-10-15. The remaining step is the group's request to the internationalization working group, which #138 says is theirs to send.
- **Wide-review meta issue ([#138](https://github.com/w3c/gpc/issues/138)).** Process tracking by the editors and the staff contact. Outside contributions belong on the concrete technical issues, not on the checklist.

## What this audit did not do

- No issue comment, pull request, email, or other external write.
- No browser was launched, and the proposed WPT file was not executed.
- The Chromium code review linked from #151 was not opened.
- Stable-channel shipping tables were not successfully retrieved. wpt.fyi was only partly retrieved, as recorded above.
- `research/D1/`, `research/D2/`, and `research/incident-evidence/` had no local files to reuse.
- Acceptance probabilities are not estimated. The review table is a bounded sample of dates and stated dispositions.

## Internal-review packet

If one candidate is chosen for the November review, choose candidate 1. The defect is a contradiction in a normative sentence, the design constraint is already in the issue, and the deliverable is a short algorithm with examples.

If a second draft is prepared in parallel, choose candidate 3. It has a separate destination, an existing normative sentence to test, and a review path that does not start with the patent commitment. File the candidate 2 question in the same note as the test, and wait for an editor answer before changing service-worker tests.

Candidate 4 is a prepared comment, sent only if #164 still has no editor text at the moment Thomas approves a submission.
