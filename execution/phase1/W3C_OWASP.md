# Track A — W3C and OWASP

Fetch date: 2026-11-19. This file records live status of the four submissions, pull request 1236, the GPC next step, and new candidates. It does not file anything. Acceptance means a merge, published text, or an editor decision that changes the specification. A comment that agrees is not acceptance.

The local log names GitHub user `thomasLiu963`, user id 125628460. On 2026-11-19, `GET /users/thomasLiu963` returned 404. `GET /users/thominator1011` returned id 125628460, the same id. Every public item below is authored by `thominator1011` with association `NONE`. That is the account that opened the four submissions.

Commits named below were returned by the GitHub API on 2026-11-19 unless a sentence says otherwise.

## 1. The four submissions, and pull request 1236

None of the four is merged, published, or accepted.

### C-001 — AISVS issue 1232, and maintainer pull request 1236

| Fact | Live value |
| --- | --- |
| Issue | https://github.com/OWASP/AISVS/issues/1232 |
| State | Open. `closed_at` null. Labels empty. The `1.02` label is still absent. |
| Author | `thominator1011`, id 125628460, association `NONE` |
| Created | 2026-11-19T04:05:37Z |
| Comment | One. Jim Manico (`jmanico`, association `MEMBER`), comment id 7022442532, 2026-11-19T21:16:06Z: "I think this is wise, I'll add a PR here. This was my original mistake. We need this, IMO." |
| Assignees | At 2026-11-19T21:16:09Z he assigned `jmanico`. At 2026-11-19T21:16:12Z he assigned `thominator1011`. |
| Document | Draft. `1.02-dev` only. `CONTRIBUTING.md` on the default branch, fetched 2026-11-19, says 1.01 is the latest stable release and that `1.0/` and `1.01/` are locked. |

Pull request https://github.com/OWASP/AISVS/pull/1236 exists. It is not ours.

| Fact | Live value |
| --- | --- |
| Author | `jmanico` (Jim Manico), association `MEMBER` |
| Opened | 2026-11-19T21:16:48Z. State open. `merged` false. `draft` false. |
| Head | `9c85d07cbac210473c1a808b073a3d89cfb79e7f` on `OWASP/AISVS`, not a fork. Committer name "Jim Manico", 2026-11-19T21:16:33Z. |
| Base | `main` at `abcb87056c2a39ae04422abef90c278f43cb4ac8` |
| GitHub merge state | `mergeable` true, `mergeable_state` `clean` |
| Reviews | The reviews API and the issue-comments API returned no objects. |
| Files | Two additions, zero deletions. `1.02-dev/en/0x10-C09-Orchestration-and-Agentic-Action.md` adds row 9.5.8. `1.02-dev/en/0x91-Appendix-B_AI_Security_Controls_Inventory.md` adds the matching inventory line. |

The requirement sentence in the diff is the sentence from issue 1232: "Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action." Level 2. The body starts "Closes #1232" and says 9.7.4 is not reused. The retrieved body also mentions OPA operations documentation; that sentence was truncated in the fetch and is his text, not a file change. The diff does not add OPA, logging, or a new chapter.

`main` moved after the 2026-11-18 pin. Tip on 2026-11-19 is `abcb87056c2a39ae04422abef90c278f43cb4ac8`, 2026-11-19T20:56:39Z, "Merge pull request #1227" (C9.3 agent skills). That merge is earlier than pull request 1236, and 1236 is based on it. On `abcb870`, C9.5 still ends at 9.5.7. Row 9.5.8 is absent. The glossary Fail-Closed entry still says: "AISVS requires AI components with safety or authorization responsibilities to fail closed." (`1.02-dev/en/0x90-Appendix-A_Glossary.md`, line 119 at that commit). The missing-requirement defect is still in `HEAD`. It leaves `HEAD` when 1236, or an equivalent commit, merges.

Acceptance for C-001 is that merge. His comment and the open pull request are not acceptance. No pull request was opened by `thominator1011`.

Do not open a second pull request. Do not reply on 1232 unless a later review asks a question. The next external event is his merge, or a review on 1236.

### C-002 — AI Exchange pull request 287

https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/287

| Fact | Live value |
| --- | --- |
| State | Open. `merged_at` null. `draft` false. |
| Author | `thominator1011` |
| Created | 2026-11-19T04:06:08Z. `updated_at` 2026-11-19T04:06:09Z. |
| Head | `38276bc55ac61dac954e03eb4f286e1dd050e65b` |
| Recorded base | `c68371ed56051a3d7c894e36c20c3bcbc22eb441` |
| Diff | One file, one line. `content/ai_exchange/content/docs/1_general_controls.md`. Replaces "policy engine outage requires an explicit fail-closed vs fail-open choice" with "if the policy engine is unreachable, deny the action." |
| Reviews, review comments, issue comments | All three APIs returned empty. |
| Checks | Commit status `pending` with zero statuses. Check-runs `total_count` 0. |
| Merge flags | `mergeable` true, `mergeable_state` `unstable` |

`main` has moved since the pull request opened. Tip: `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb`, 2026-11-19T22:42:15Z, merge of pull request 289 by `robvanderveer`. At that commit the contradiction is still present. Line 747: "Fail closed if the policy engine is unreachable." Line 760: "policy engine outage requires an explicit fail-closed vs fail-open choice." GitHub still reports 287 as mergeable against the new tip. Document status remains community guidance, a living OWASP document, not a de jure standard.

Pull request 289 is a different change (dead links). Opened 2026-11-19T21:21:33Z by `wolfspace099`, merged 2026-11-19T22:42:16Z by `robvanderveer`. That is one same-day merge of a different diff. It is not a review of 287. 287 had no review from 04:06Z through this fetch, which is after 289 merged.

Acceptance is a merge whose rendered `#LEAST MODEL PRIVILEGE` text denies the action when the policy engine is unreachable and no longer offers the fail-open choice. Permalink to re-check after a merge: https://owaspai.org/go/leastmodelprivilege. That page was not re-fetched on 2026-11-19. The repository file at `bde8cc6f` is the source checked today.

Next action: wait. Do not reply and do not push another commit.

### C-003 — DPV comment on issue 484

https://github.com/w3c-cg/dpv/issues/484#issuecomment-6999347608

| Fact | Live value |
| --- | --- |
| Issue state | Open. Labels `todo` and `help-wanted`. Assignees empty. |
| Issue `updated_at` | 2026-11-19T04:05:38Z, the comment time |
| Comments | One. Comment 6999347608, `thominator1011`, 2026-11-19T04:05:38Z. No later comment. |
| `dev` tip | `aff91c294b105d9a261ea8622350b0fc7ef0e293`, 2026-11-18T15:35:49Z |
| `master` tip | `689d32c0f7c571d32f7f8635ae548fcc1c3ff695`, 2026-11-18T15:37:14Z |

Those two SHAs are the SHAs named in the comment. No vocabulary commit has landed since the comment. The membership files the comment checked are the same commits. The SPARQL script was not re-run on 2026-11-19. The primer HTML was not re-fetched. Document status in the register is community guidance. The report's status banner was not re-fetched today.

Acceptance is published primer text that states the membership relation for each serialisation, with the `pd:BloodType` example. The comment is not acceptance. Next action: wait. Do not send a second comment and do not open a pull request.

### C-005 — GPC issue 165

https://github.com/w3c/gpc/issues/165

| Fact | Live value |
| --- | --- |
| State | Closed 2026-11-19T20:28:55Z by `SebastianZimmeck` |
| Author | `thominator1011`. Created 2026-11-19T04:05:39Z. Labels and assignees empty. |
| Comment | One. Comment 7021335109, `SebastianZimmeck`, 2026-11-19T20:28:52Z. He then closed the issue. |
| Spec commits since the Working Draft | None. `main` is still `09013acfed7820dc967489514a156e2ced827289`, 2026-09-24T16:56:10Z, "Merge pull request #160". Open pull requests: 0. |

He is an editor. `index.html` at that commit lists editors Sebastian Zimmeck (Wesleyan University), Peter Snyder (Brave Software), Justin Brookman (Consumer Reports), and Aram Zucker-Scharff (The Washington Post).

His comment quotes the specification, including: "if the preference changes during or after a top-level navigation, it will not be reflected until the next navigation" and the sentence that the user agent SHOULD inform the user of inconsistent tabs and offer a reload. He then writes: "Generally speaking, implementers should always make a best effort to understand and adhere to a user's GPC preference."

That comment does not contain the sentence "an already loaded document keeps `gpcAtNavigation`." It quotes the Working Draft rule that a change is not reflected until the next navigation, which is the rule that binds `navigator.globalPrivacyControl` and `Sec-GPC` to `gpcAtNavigation`. The "best effort" sentence does not say the loaded document updates immediately, and it does not edit the MUST. He did not change `index.html`.

The published Working Draft still says the same thing. https://www.w3.org/TR/2026/WD-gpc-20260924/ was fetched 2026-11-19 (response `Date: Fri, 20 Nov 2026 04:14:30 GMT`, `Last-Modified: Tue, 29 Sep 2026 22:02:43 GMT`). Section 3.2: the preference "MUST be cached on each top-level navigation" and "if the preference changes during or after a top-level navigation, it will not be reflected until the next navigation." The same page defines `gpcAtNavigation` and says its value "MUST reflect the preference" when the active document began loading. This is a W3C Working Draft, not a Recommendation. The editor's draft source matches it. Document status: draft.

Issue 146 is still open, label `agenda+`, zero comments, `updated_at` 2026-10-15T18:39:53Z. No editor has chosen on that issue. Issue 164 is still open, zero comments, assigned to `pes10k`, `AramZS`, `SebastianZimmeck`, and `j-br0`. Its timeline has a `cross-referenced` event by `SebastianZimmeck` at 2026-11-19T20:31:29Z. The API event does not name the source issue. This report does not guess.

The WPT patch was not submitted. `gpc/` on `web-platform-tests/wpt` `master` `221a7fea449dcd9a42d5f249d5e4cf359a619d74` (2026-11-20T02:19:21Z) is still `META.yml` `e9bbee032d85`, `global_privacy_control.testdriver.html` `138bba2eb452`, `idlharness.any.js` `7a7305eb6235`, `navigator-globalPrivacyControl.https.html` `6ddc7ffca419`, `sec-gpc.https.html` `6acc350d241c`, and `support/`. There is no `navigation-cache.https.html`.

## 2. GPC next step

Run the official Web Platform Test locally. Do not file a pull request in this step, and do not open a Chromium bug.

The editor quoted the cache rule and closed issue 165 without changing the draft. That is enough to stop waiting for a specification edit before running the held test. It is not a Working Group resolution, and the "best effort" sentence is not a choice of Chromium's immediate update. The held patch at `contributions/T005-GPC-WPT/patch/` stays unsent until `./wpt run` has executed it. The 2026-11-18 packet recorded that the runner was not started. It was not started for this report either. The ChromeDriver session in that packet is not `./wpt run`.

What the runner requires, from files at WPT `221a7fea`:

- License: `LICENSE.md` is the 3-clause BSD license. `CONTRIBUTING.md` line 1: "All contributions are licensed under the terms of the 3-Clause BSD License."
- `README.md`: clone https://github.com/web-platform-tests/wpt, then `./wpt run` runs tests in a browser and `./wpt lint` lints them. The README also says a pull request is a fork, a branch, `./wpt lint`, and then the pull request.
- `docs/running-tests/from-local-system.md`: Python 3.9 or higher; a `hosts` file produced by `./wpt make-hosts-file | sudo tee -a /etc/hosts`; then `./wpt run [browsername] [tests]`, with the example `./wpt run chrome dom/historical.html`.
- `docs/running-tests/chrome.md`: if Chrome is not the detected stable or canary binary, pass `--binary`. A runtime feature flag is `--binary-arg`. A non-default ChromeDriver is `--webdriver-binary`. The local Chrome 157 observation needed `GlobalPrivacyControlApi`. That flag is not in the WPT document. It is in the 2026-11-18 local packet. A run of the held file has to pass whatever flag that Chrome still requires, and the log has to say which flag was used.
- Suggested reviewers, `gpc/META.yml`: AramZS, bvandersloot-mozilla, j-br0, pes10k, SebastianZimmeck.
- AI policy, `docs/writing-tests/ai-policy.md` and the README section that points at it: LLM use to author tests is allowed. The human who opens the pull request must understand every change and be the attribution on the commit. LLM-generated discussion text must be in a `<blockquote>` of at most one paragraph or a `<details>` element, or it must come from a bot account. Disclosure in the commit message is described as encouraged when an LLM is a significant input. The held patch must not be filed with an unlabeled model-written pull-request body.

A specification pull request on `w3c/gpc` is still out of bounds. `CONTRIBUTING.md` at `09013ac` says substantive contributions are for Recommendation-track documents under the W3C Patent Policy (https://www.w3.org/Consortium/Patent-Policy/) and the Software and Document License, and that a substantive contributor must participate in the Working Group or make a non-member patent licensing commitment. This workspace has neither. The navigation-cache follow-up is a WPT pull request, after the local official run, not a pull request on `w3c/gpc`.

The single next step is the local `./wpt run` of the held file. Preparing the pull-request text before that log exists skips the gate the filed issue already stated. Filing is a later step, and only if the log matches the Working Draft's cache rule. If the editor's "best effort" sentence is read as permission for an immediate update, the run still comes first: it records what Chrome does under the official harness, and the patch stays unsent if the group later edits section 3.2.

## 3. C-004 — send the comment

Issue 486 and `2.4-dev` still have the wrong parent. The comment is ready to send after an explicit approval. The public text is `execution/phase1/drafts/C-004-dpv-486-comment.md`. It was not posted.

https://github.com/w3c-cg/dpv/issues/486 is open. `updated_at` 2026-09-09T10:13:40Z. Label `todo`. No assignee. Two comments, both 9 September 2026, and no comment since:

- `besteves4`, association `COLLABORATOR`, 2026-09-09T08:31:40Z: `dpv:RightsFulfilment` is a purpose and should not have `dpv:LegalObligation` as its parent. She names `dpv:FulfilmentOfObligation` or `dpv:LegalCompliance` and does not choose.
- `Daham-Mustaf`, 2026-09-09T10:13:40Z: thanks her for confirming.

The 9 September minutes at `689d32c0`, https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/meetings/meeting-2026-09-09.html#a01 , fetched 2026-11-19, record:

> ACTION: Change parent of dpv:RightsFulfilment to dpv:FulfilmentOfObligation

and a second action to update the purpose-module description and examples. Harsh's minuted reason: "dpv:RightsFulfilment should have as parent dpv:FulfilmentOfObligation because rights may not be legal obligations." `audits/SUMMARY.md` says to recommend `dpv:LegalCompliance`. That sentence is stale. The minutes, `MASTER_TRACKER.md`, and `contributions/T004-DPV-Rights/COMMENT.md` name `dpv:FulfilmentOfObligation`. This report follows the minutes.

Re-read on 2026-11-19 at the same tips (`dev` `aff91c29`, `master` `689d32c0`):

- `2.4-dev/dpv/modules/purposes.ttl`: `dpv:RightsFulfilment` is `dpv:Purpose`, in `dpv:purposes-classes`, with `skos:broader dpv:LegalObligation`.
- `2.3/dpv/modules/purposes.ttl` line 1434: `skos:broader dpv:LegalObligation`.
- `code/vocab_csv/Purpose.csv` on `dev`: `RightsFulfilment` has `ParentTerm` `dpv:LegalObligation` and `ParentType` `dpv:Purpose`.
- `2.4-dev/dpv/modules/legal_basis.ttl`: `dpv:LegalObligation` is a `dpv:LegalBasis`, `skos:broader dpv:LegalBasis`, in `dpv:legal-basis-classes`, definition "Legal Obligation to conduct the specified activities".
- The same Purpose CSV row for `LegalCompliance` defines it as "Purposes associated with carrying out data processing to fulfill a legal or statutory obligation" and parents it on `dpv:FulfilmentOfObligation`.

The 18 November minutes at `aff91c29` say Harsh will comment proposed resolutions on the GitHub issues, and: "Next meeting in 1week on NOV 25. Topics are v2.4, commits, discussion on IRI and parent changes, and other items discussed today." No commit between that meeting and this fetch applied the 9 September action.

The online Purpose spreadsheet was not opened. The OWL subclass paragraph and the generated HTML row in the draft were checked on 2026-11-18 against these same commits and were not re-parsed on 2026-11-19. The SPARQL guard was not re-executed on 2026-11-19. The parent triple that the query reported was re-read and is still the only purpose-to-legal-basis parent this fetch inspected. "No later minutes file mentions RightsFulfilment" is true of this tree because `dev` and `master` have not moved since the 18 November search.

`contributing.md` on the default branch, fetched 2026-11-19, is three sentences. It points at a wiki guide, says decisions are made in meetings, and says membership is not required to contribute. It states no AI-assistance rule. `GET /repos/w3c-cg/dpv/wiki/Contribution-Guide` and `GET /repos/w3c/dpv/wiki/Contribution-Guide` both returned 404. The wiki text is UNVERIFIED. The public draft is the comment in `contributions/T004-DPV-Rights/COMMENT.md`, including its disclosure sentence. That sentence stays because this workspace discloses when a tool drafts the substance, even though the three-sentence contributing file states no AI rule. The draft contains no admissions strategy.

Mechanism: one comment on issue 486. No pull request. The chair said on 18 November that he will comment resolutions and make the v2.4 commits. The comment asks him to apply the parent the minutes already named.

What would count: a `dev` or published vocabulary commit in which `dpv:RightsFulfilment` has `skos:broader dpv:FulfilmentOfObligation` and no longer has `skos:broader dpv:LegalObligation`. A commit that uses another purpose, including `dpv:LegalCompliance`, is the group's choice. The comment alone is not acceptance.

| Timing | Record |
| --- | --- |
| Time to produce | The comment exists. Posting it, after an explicit approval, is the remaining work. |
| First external response | No measured response time to this comment, because it has not been sent. The 18 November minutes schedule parent changes for the 25 November 2026 meeting and say Harsh will propose resolutions on the issues. That is a scheduled discussion, not a promise that he will answer this comment. The same-week and eight-week documentation samples in the 18 November audit were not re-fetched today. |
| Acceptance | A vocabulary commit. No v2.4 publication date was retrieved. Pull request 254, in which the chair copied a change into his own commit, was not re-fetched today. |
| Deadline | None. The 25 November 2026 meeting is the next agenda that names parent changes. It does not close the issue. |
| Verifiable | Yes. The `skos:broader` triple in `dev` or in a published release. |
| 2026-11-30 | Sending the comment is realistic. A vocabulary commit by that date is not established. |
| 2027-02-15 | A commit can be part of the v2.4 work the 18 November minutes describe. That is not established as a date. |
| Label | DO NOW |

## 4. Candidates

Three. The bar for a fourth was not met. Section 5 records what was checked and left alone.

### 4.1 C-004 — DO NOW

Covered in section 3. Draft: `execution/phase1/drafts/C-004-dpv-486-comment.md`.

### 4.2 GPC navigation-cache test — PREPARE

This is the follow-up already held at `contributions/T005-GPC-WPT/patch/`. It is not a new specification proposal.

The gap is the one in section 2. Existing `gpc/` tests set the preference and then open a new document. Nothing in that directory asserts that the already loaded document keeps `gpcAtNavigation`. The Working Draft's section 3.2 is the rule a test would encode. Chromium's disagreement was read and, for ChromeDriver 157, executed on 2026-11-18. This report did not re-fetch Chromium source and did not re-run ChromeDriver.

Proposed mechanism, later: a pull request to `web-platform-tests/wpt` adding the held test, under the 3-clause BSD license, with the AI-policy labelling in section 2, and with the official run log in the pull request. Reviewers to request are the five names in `gpc/META.yml`. Do not file it now.

Review stages, from the repository's own contributing text: local `./wpt run` and `./wpt lint`, then a pull request, then review by the suggested reviewers or another WPT reviewer, then merge to `master`, then results on wpt.fyi. The closest sample in the 18 November tracker is wpt pull request 54446: opened 2025-08-21, first human comment 2025-09-04, approved and merged 2025-09-22 by `jgraham`, for a Mozilla author. That pull request was not re-fetched on 2026-11-19. The first GPC landing and same-day revert recorded in the tracker (`f564d65`, `3c910a5`, `d5d5da0`, 2025-10-30 and 2025-10-31) were not re-fetched.

What would count: a merge of the test into `web-platform-tests/wpt`. Sebastian Zimmeck's close of issue 165 is not that merge. A failing Chrome result is a conformance observation. It is not, by itself, a merged test.

| Timing | Record |
| --- | --- |
| Time to produce | The patch exists. The missing product is one official local run. The documents require a checkout, Python 3.9+, and a `hosts` edit. This report did not time that run. |
| First external response | The specification question already has an editor comment, on 2026-11-19, about 16 hours after the issue opened. A future WPT pull request has no response yet because it has not been opened. The 54446 sample above is the historical test-review interval on record, and it was not re-fetched today. |
| Acceptance | A merge to `wpt` `master`. Known interval in the unrechecked sample: about a month for a Mozilla author, after a first human comment at two weeks. A test that fails an implementation can sit longer. That is the sample, not a forecast for this file. |
| Deadline | None. |
| Verifiable | Yes, after a merge: the file on `master`, and a wpt.fyi result for that file. |
| 2026-11-30 | The local run is the realistic product. A merged test by that date is not established. |
| 2027-02-15 | A pull request can be in review if the run has been done and the test still matches section 3.2. A merge by that date is not established. |
| Label | PREPARE |

### 4.3 AISVS 9.5.7, when "current authority" is current — PREPARE

The hold in `audits/SUMMARY.md` was: revisit after C-001 has a maintainer reply. That condition is met. Jim Manico's comment on issue 1232, quoted in section 1, is a maintainer reply. The reply is about the missing policy decision. It does not mention 9.5.7.

The row is unchanged at `abcb870`, line 89: "Verify that authority derived through delegation never exceeds the delegating agent's current authority." Level 2. A search of open issues for "9.5.7" on 2026-11-19 returned issue 1232 and closed issues. No open issue asks which instant "current" means. The known objection in the 18 November audit is the Level 2 versus Level 3 collision with 9.5.6, which still says long-running sessions re-evaluate current backend authorization on every privileged action, at Level 3.

Do not file this while pull request 1236 is the open thread he just created. On 2026-11-17 and 2026-11-18 the maintainers closed issues 1215 and 1216 as unreadable generated discussion. A second authorization issue the same day as 1236 repeats that failure mode. Prepare the two-sentence issue locally after 1236 merges, or sooner only if he asks what else is missing in C9.5. This report does not include that draft, because it is not ready to send.

`CONTRIBUTING.md`, fetched 2026-11-19, "AI-Assisted Contributions": AI tools may draft issues. The contributor must be willing to defend every sentence. The control must be concrete and testable. Large unreviewed generated text is what the section says to avoid. The route is an issue first. A pull request waits until a maintainer asks. Target `1.02-dev` only. Append identifiers. Do not reuse a retired identifier.

What would count: a merge into `1.02-dev` that replaces the 9.5.7 sentence with one instant, either execution time or delegation time. An issue comment that discusses the word "current" is not acceptance.

Historical intervals from the 18 November audit, not re-fetched today: issue 1201 opened 2026-10-21, Jim Manico commented 2026-10-24, pull request 1204 merged 2026-11-04. Pull request 1117 was approved by Otto Sulin on 2026-07-24 and merged 2026-07-30. Today's own point is separate: issue 1232 was opened 2026-11-19T04:05:37Z and Jim Manico commented 2026-11-19T21:16:06Z. That is one reply on one issue. It is not a turnaround for 9.5.7.

| Timing | Record |
| --- | --- |
| Time to produce | A few hours for a two-sentence issue, after 1236 is no longer the active thread. |
| First external response | Not established for this wording. The samples above are the recorded intervals for other one-sentence AISVS edits. |
| Acceptance | A merge of the replacement sentence. The 1204 sample took about two weeks from the issue to the merge, after a maintainer had agreed the text was an editing loss. Agreement on 9.5.7 is not in hand. The Level 2 / Level 3 objection is still the objection. |
| Deadline | None. No 1.02 release date was published in the files fetched today. |
| Verifiable | Yes. The 9.5.7 cell in `1.02-dev`. |
| 2026-11-30 | An internal draft is realistic. A merge is not established, and filing before 1236 settles is the wrong step. |
| 2027-02-15 | A merge is the kind of result the 1117 and 1204 samples show for a single sentence after a leader has agreed the sentence. That agreement is not in hand. |
| Label | PREPARE |

## 5. Checked, and not advanced

Held and abandoned items stay dropped unless the condition quoted here is met. These conditions are not met, or the work is already owned.

| Item | Live check on 2026-11-19 | Label |
| --- | --- | --- |
| Exchange OX-1 approval-screen inputs | Hold is a December draft, and the November send was limited to C-002 before that draft. Four items were sent, and the date is 2026-11-19. The condition is not met. | DEFER |
| Exchange OX-3 on issue 188 | The hold requires an explicit approval to comment. None is recorded. | DEFER |
| DPV issue 500, `rdfs:Label` | Open, zero comments, label `todo`, opened 2026-11-16 by `Daham-Mustaf`. The body already proposes `rdfs:label` and eight further metadata fixes. `besteves4` is mentioned and has not commented. A second comment that repeats item 1 is his proposal, not a new repair. | DROP |
| GPC issue 114 | Latest assignee comment is Peter Snyder, 2026-10-22T03:59:09Z: the editors are treating the issue as "PRs welcome, but otherwise planned for post v1." No patent commitment is in this workspace. A comment-only approval is not recorded. | DEFER |
| GPC issue 146 | Still zero comments. No editor choice on the issue. | DEFER |
| AI Testing Guide APP-13 and APP-14 | `main` is still `006e4e9ee060f2ca2176037499b824e47af5360e`, 2026-06-01T08:45:49Z. The newest merged pull request returned by the closed-pull list is 77, merged 2026-06-01. The hold is "only if review resumes." It has not. | DEFER |
| AI Content Disclosure erratum | `main` is still `351c0a68e4460b0ce242470395adeac5fcf5ceb9`, 2026-10-09T17:16:40Z. Open pull requests: 0. Issues 46 and 49 still have zero comments. Issue 51's `updated_at` is 2026-10-17. No new-version draft is in that repository. The hold is "when the chairs open a new version." They have not. | DEFER |
| AISVS 9.5.6 restoration, end-user credential row, refile of 1196 | No new maintainer text reopens them. Left abandoned. | DROP |
| AISVS 1226, 1122, 1187 | Still open and assigned (`sydseter` on 1226; `jmanico` and `ottosulin` on 1122). 1226 was updated 2026-11-19T23:09:12Z. | DROP |
| AISVS 1217 | Closed 2026-11-19T21:00:42Z, reason `not_planned`. Jim Manico's closing comment says C3.3 is the wrong home and C9 does not need a new row. | DROP |
| AISVS 1233 | Open, `Mayur021`, 2026-11-19T05:36:56Z, zero comments. C9.6 objective versus an exercise requirement. His issue. The kill-switch restart asked of the 1215/1216 authors stays abandoned. | DROP |
| AISVS 1234 | Open, `PPushkarev`, 2026-11-19, zero comments, about 10.4.2. His issue. | DROP |
| AISVS 1235 | Open, `jmanico`, 2026-11-19, C2.1.1 locale normalization. His issue, on the topic of assigned issue 1122. | DROP |
| ACT Rules 2472 | Open, assigned to `WilcoFiers`, `HelenBurge`, and `dan-tripp-siteimprove`. `dan-tripp-siteimprove` commented 2026-11-19T00:23:07Z on the "partial checks" wording. Occupied. | DROP |
| ACT Rules 2473 | Open, `WilcoFiers`, 2026-11-12, zero human comments, labels `Agenda item` and `Discussion`. The body says it was AI-generated and reviewed by him, and it proposes that checks using AI models not be listed as ACT implementations until a policy lands. That is his agenda item. | DROP |
| ACT Rules 2474 | His pull request for an AI contribution page, body says drafted with Claude and reviewed by him. Netlify commented. Not an unowned gap. | DROP |
| ACT Rules 2279 and 2475 | 2279 is assigned to `Jym77`; `TobiasNyhuus` commented an implementation on 2026-11-05. 2475 is assigned to `giacomo-petri`, label `reviewers wanted`, and the failing example is already in the pull request. | DROP |
| WCAG and WCAG 3 | `repo:w3c/silver` search for generative or "AI system", open issues, returned an empty list. `repo:w3c/wcag is:issue is:open AI` returned six issues whose titles are about captions, techniques, headings, and multiple ways. None is an artificial-intelligence requirement. No unowned WCAG defect met the bar. | DROP |
| New Exchange controls, and the abandoned Exchange numbers | Not reopened. Pull request 289 is a maintainer-merged link repair, not a control change. | DROP |

ACT Rules and WCAG were in scope for a new contribution. The open ACT work fetched today is either assigned, already implemented by its author, or a proposal Wilco Fiers put on the group's own agenda. No item there had a clear incorporation path for an outside patch this week.

## 6. Policies opened on 2026-11-19

| Project | Locator | What it says |
| --- | --- | --- |
| AISVS | https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md at the default branch, which was `abcb870` | Issue before a pull request. New work targets `1.02-dev/`. Append identifiers and do not reuse retired ones. "AI-Assisted Contributions" allows AI across the workflow, including drafting issues, if the contributor will defend every sentence and the control is concrete and testable. |
| GPC specification | https://github.com/w3c/gpc/blob/09013acfed7820dc967489514a156e2ced827289/CONTRIBUTING.md | Substantive specification contributions require Working Group participation or a non-member patent licensing commitment under https://www.w3.org/Consortium/Patent-Policy/. |
| WPT | `LICENSE.md`, `CONTRIBUTING.md`, `README.md`, and `docs/writing-tests/ai-policy.md` at `221a7fea` | 3-clause BSD. `./wpt lint` before a pull request. LLM-authored tests are allowed with a responsible human. LLM-written discussion must be labelled and wrapped as the policy states. |
| DPV | `contributing.md` on the default branch | Decisions are made in meetings. Membership is not required to contribute. No AI-assistance rule in that file. The wiki URL in the file was not retrievable (404 on both wiki APIs). |
| AI Exchange | The contribute-page AI rule was not re-fetched. Pull request 287's body, fetched today, already contains an "AI assistance" section. The 18 November audit is the record of the page. This report does not requote a page it did not open. | |

## 7. Not verified on 2026-11-19

- The DPV wiki Contribution Guide. Both wiki API calls returned 404.
- The online DPV Purpose spreadsheet.
- A fresh SPARQL run, a fresh OWL parse, and a fresh read of the generated purposes HTML. Those claims in the C-004 draft sit on commits `689d32c0` and `aff91c29`, which are still the branch tips.
- `./wpt run` and `./wpt lint`. Not started.
- A new Chromium, Firefox, or WebKit fetch. The 2026-11-18 source notes were not repeated.
- https://owaspai.org/go/leastmodelprivilege as rendered HTML. The repository file at `bde8cc6f` was read.
- The full body of pull request 1236 past the OPA sentence. The two-file diff was read in full.
- Which issue caused the 2026-11-19T20:31:29Z cross-reference on GPC issue 164.
- WPT pull request 54446, AISVS pull requests 1117 and 1204, and DPV pull request 254. Intervals cited from them are from the 2026-11-18 audit and tracker.
- Slack, mailing-list mail, and the 25 November DPV join link.
- Any commit after the SHAs in this report. The fetches are a point in time on 2026-11-19.
