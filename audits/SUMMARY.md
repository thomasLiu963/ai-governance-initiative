# Implementation summary

Decision date: 2026-11-18. This file records which completed audits move into local drafting. It does not approve an external submission, and none has been sent. Individual audit reports were left unchanged.

The temporary labels T001–T005 are the stable register IDs C-001–C-005 in `MASTER_TRACKER.md`.

## What is in the November set

Prepare these five locally so each can go to internal review by 2026-11-30. Status stays `candidate`. Submission stays `none` until Thomas approves that specific item.

| ID | Label | Draft | External result that would count |
| --- | --- | --- | --- |
| C-001 | T001 | One AISVS issue: block the agent action when the policy decision point returns nothing before the documented timeout. | A merge into `1.02-dev` that adds that Level 2 requirement. |
| C-002 | T002 | One AI Exchange pull request: one failure rule when the policy engine returns no decision. | A merge that removes the contradictory fail-open choice for state-changing actions. |
| C-003 | T003 | One comment on DPV issue #484: which relation answers concept membership, with the `pd:BloodType` example. | Primer text, in a later DPV report, that states the test for each serialisation. |
| C-004 | T004 | One comment on DPV issue #486: parent of `dpv:RightsFulfilment`, plus a purpose-parent query. | A vocabulary commit whose broader parent for that term is a purpose. |
| C-005 | T005 | One Web Platform Test: the current document keeps the GPC preference until the next top-level navigation. | A merged `wpt` file that fails a same-document change. |

If only one external send is approved before 2026-11-30, send C-002. It is the only item whose public review sample includes same-week merges of a few plain sentences. C-001, C-003, C-004, and C-005 should still be drafted by 2026-11-30. Their historical review times put an external decision after that date.

## Separate tracks

These stay out of the November external set.

- **C-006.** USAC resolution on detection scores. The draft, the evidence brief, and the memorandum already exist under `audits/university-policy/`. Internal reading can finish by 2026-11-30. The November 24, 2026 meeting is not a vehicle: the draft has no sponsors, and the audit could not confirm that the meeting will be held.
- **C-007.** FCC consent-revocation comment. Reopened for local drafting. The Further Notice comment date is 2026-11-25. Internal review of this item is 2026-11-23, earlier than the 2026-11-30 horizon that caused the drop. The draft is `contributions/C-007-FCC/`. Submission stays `none`.
- **Incident evidence.** No candidate. `research/incident-evidence/` has no files. No completed audit reads the AI Incident Database or any other incident corpus.
- **D1 and D2.** No candidate. Both directories are empty. Designs RR-1 through RR-5 in the research-reuse audit stay blocked until author records exist.

## Abandoned

Draft none of the following. A parallel contribution should not reopen them.

| Item | Why it is abandoned |
| --- | --- |
| AISVS restoration of the 9.5.6 denial and still-valid-token predicates, as its own issue | On 2026-11-08 Jim Manico wrote that 9.5.6 needs no change. The queued-action example stays with issue #1196. |
| AISVS row forbidding presentation of the end user's own credential | The deletion is real, and 1.01 deliberately narrowed the related MCP rule. A leader can treat the current identity and token rows as enough. |
| Refiling AISVS #1196, or carrying that example into the AI Testing Guide | `mahfzal87` and `KarinLuni` wrote it. A project leader invited those authors to the Testing Guide. |
| AISVS issues #1226, #1220, #1217, #1195, #1187, #1122, #1152, #1214, #1215, and #1216 | Each is assigned, already decided, or closed with a request that the existing contributors restart it. |
| Any new AI Exchange control identifier, tool listing, taxonomy, or enforceability scale | Those are the submissions that stayed open for months or were closed for scope. |
| Exchange issues and pull requests 244, 276, 191/192, 177, 202, 216, 222, 246, and 247 | Each already has an author or is already merged. |
| DPV issues #465, #451, #482, and #501 | On the 25 November agenda, already agreed in the thread, unanswered and legally broad, or already set for the parent discussion. |
| A GPC specification pull request for the combined `Sec-GPC` value, workers, or the TAG punch list | The workspace has no record of a Privacy Working Group participation or a non-member patent commitment. Editors assigned #164 to themselves. The combined-value assignee scheduled the work after version 1. |
| Purpose-conditional GPC, an AI-training meaning for GPC, and a stronger GDPR reading | The group has not asked an outside contributor to settle those debates. |
| AI Content Disclosure attribute, non-HTML specification, or WHATWG HTML change | The 9 October 2026 report is frozen. Issues #46–#49 are recorded as a future version, and no version draft exists. |
| AI Testing Guide copy of the general oracle in pull request #81, new test numbers, and the APP-06 work in #76, #79, #85, #92, and #97 | Each is already open. Nothing in that repository has merged since 2026-06-01. |
| A detector bake-off, a human-subjects study, or a numerical false-positive ceiling in the USAC text | The university audit rejects all three. Turnitin's own guide already says a score is not the sole basis. |
| NIST metrology YAML, or any external use of D1 or D2 text | No metric, manuscript, license, or coauthor approval is in the workspace. |
| An AI Incident Database submission | No incident file and no audit of that database. |

## Held for a later date

These findings are real. They are not November drafts, and they have no register ID.

| Finding | Next condition |
| --- | --- |
| AISVS 9.5.7, defining when "current authority" is current | After C-001 has a maintainer reply. The Level 2 versus Level 3 collision with 9.5.6 is the known objection. |
| Exchange OX-1, showing the untrusted input on the approval screen | December draft, after any November send is limited to C-002. Pull request 235, the pattern to copy, took sixteen days. A 2026-11-30 merge is not a supported forecast. A 2027-02-15 decision is realistic if the text stays short. |
| Exchange OX-3, re-checking the human principal when a staged action is released | Comment on issue 188 only after an explicit approval. The ten-item list has waited on the agentic workstream since 2026-08-03. A February acceptance is not the forecast. |
| DPV #500, `rdfs:Label` only | A comment if Beatriz Esteves and the chair have not already split the nine header items. The FOOPS literals stay. |
| GPC combined-field receiver, as a comment on issue #114 | After a patent commitment exists, or after Thomas approves a comment that stops short of a pull request. The 22 October 2026 assignee comment places the work after version 1. Comparable normative edits in the sample took 42 days to about five months. |
| GPC worker text on issue #146 | An editor choice between removing the service-worker attribute and defining a snapshot. WebKit pull request 69606 and the current tests already diverge. C-005 does not wait on this choice. |
| Testing Guide pass, fail, and inconclusive text for AITG-APP-13 and AITG-APP-14 | A February submission only if maintainers resume review. The newest merged pull request in the sample is #77 on 2026-06-01. |
| Testing Guide stated-preference case for AITG-APP-10 | After the APP-13 / APP-14 draft, on the same review path. |
| AI Content Disclosure research-use bullet, `human-only` wording, and template-versus-report bullet | When the chairs open a new report version. No chair has replied to issues #46–#49. Community Group membership and the Contributor License Agreement would still be required. |

## Verification of the five

None of C-001–C-005 depends on D1, D2, or incident notes. Every audit that looked for those directories found them absent or empty. A contribution that cites them would be fabricating support.

### Dependencies that still bind the draft

| ID | Open dependency | What the drafter does |
| --- | --- | --- |
| C-001 | Next free C9.5 identifier was `9.5.8` at commit `092232f` on 2026-11-11. Later commits were not re-read. | Re-read `1.02-dev` before freezing the issue. If `9.5.8` is taken, use the next free ID. Append one row. Leave logging, CAEP, and the #1196 procedure out of it. |
| C-002 | The contradiction was read at commit `c68371ed` on 2026-11-16. | Re-read the two sentences before opening a pull request. Small clarifications may go up without an issue. |
| C-003 | Membership counts are lexical. `rdflib` was not run. The primer still needs the group to say whether `rdf:type` or `skos:inScheme` is canonical for special-category data. | The comment asks that question. It states the lexical counts as lexical. A SPARQL rerun happens before posting, on local files, with no paid API. |
| C-004 | Beatriz Esteves named two parents on 2026-09-09 and did not choose. The chair's 18 November minutes say he will commit the error list himself. | Recommend `dpv:LegalCompliance`, with the guard query. Re-read `2.4-dev` first. If a parent commit already exists, withdraw C-004 and record his commit. Do not edit Turtle or the spreadsheet. |
| C-005 | The audit did not execute the test. The first GPC landing in `wpt` was reverted the same day. Issue #146 has no decision for service workers. | Write the same-document and next-navigation assertions. Keep service workers out. Include a dedicated worker only as the snapshot Anne van Kesteren asked for, and label that assertion as tied to #146. Run the file locally in a browser that already has the testdriver extension before any submission. |

C-001 and C-002 both concern a missing authorization decision. They are different documents and different edits. C-001 adds a verification row. C-002 deletes one contradictory sentence and limits any remaining fail-open case to a named read-only action. Neither draft cites the other as authority.

C-003 and C-004 are separate comments on separate issues. The contribution guide forbids a pull request that edits generated HTML, RDF, or the exported CSVs. The 18 November minutes say the chair will comment proposed resolutions and make the v2.4 commits. A generated pull request would collide with that plan.

C-005 does not change the GPC specification. The Working Draft already says a preference change waits for the next top-level navigation. The current tests set the preference and then open a new document, so a browser that updates the current document still passes.

### Novelty

| ID | What is new | What is already settled |
| --- | --- | --- |
| C-001 | Naming the loss. The row merged in #683 on 2026-04-13 and disappeared in #934 on 2026-06-15. The glossary still says authorization components fail closed. No later issue reopens `9.7.4`. | The predicate itself was accepted once. This is a restoration, which is the pattern in #1204. |
| C-002 | No open issue states the contradiction between "Fail closed if the policy engine is unreachable" and "an explicit fail-closed vs fail-open choice." | Issue 188 item 9 and issue 222 are different fail-closed rules. Leave them alone. |
| C-003 | A membership procedure for an unassigned `help-wanted` issue with zero comments, checked against `pd:BloodType`, the primer table, and the OWL file. | The primer already says RDFS+SKOS uses `skos:broader` and DPV-OWL uses `rdfs:subClassOf`. The defect is the table cell that offers those relations as alternatives, and the OWL column that says `owl:subClassOf` while the file uses `rdfs:subClassOf`. |
| C-004 | The choice of `dpv:LegalCompliance`, plus a query that finds any purpose whose parent is not a purpose. | A chair already confirmed the defect. Originality is low. The candidate stays because 2.3 and `2.4-dev` still have the wrong parent and the issue has no assignee. |
| C-005 | Test order. Nothing in `gpc/` asserts that the already loaded document keeps the old preference. | The normative sentence exists. This test adds coverage. It adds no protocol rule. |

C-004 is the weakest of the five on novelty and the strongest on prior confirmation. It stays. The stop rule is the parent-commit check above.

### Contribution and AI-assistance policies

All five were checked in the audits. `not-checked` does not attach to them. Disclosure still belongs in anything that is later sent, because this summary and the drafts are AI-assisted.

| ID | Contribution rule that binds the draft | AI-assistance rule |
| --- | --- | --- |
| C-001 | Issue before pull request. Target `1.02-dev` only. A minor release may append a requirement and may not renumber or reuse a retired ID. [CONTRIBUTING.md](https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md), [RELEASE.md](https://github.com/OWASP/AISVS/blob/main/RELEASE.md). | AI drafting is allowed when the contributor will defend every sentence and the control is concrete and testable. On 2026-11-17 and 2026-11-18 the maintainers closed #1215 and #1216 because long generated discussion was not readable. The issue quotes the current gap, the old `9.7.4` sentence, the glossary sentence, and Rico Komenda's 2026-04-11 note. |
| C-002 | Small clarifications may be a pull request with no issue. [CONTRIBUTING.md](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/blob/main/CONTRIBUTING.md), [contribute page](https://owaspai.org/contribute/). | Say that AI was used, what it was used for, and to what extent, in the pull-request body. A commit trailer alone is weaker than the written policy. Pull request 187 merged with a trailer and no body disclosure; the policy still asks for both. |
| C-003, C-004 | Comment on the existing issue. Discuss before code. Pull requests target `dev` and do not edit generated artifacts. [contributing.md](https://github.com/w3c-cg/dpv/blob/master/contributing.md), [wiki guide](https://github.com/w3c-cg/dpv/wiki/Contribution-Guide) dated 12 February 2026. | The DPV guide states no AI rule. The October 2026 W3C text is a draft and is not a W3C policy. Disclose assistance if a tool drafts the substance. Keep each comment short enough for a person to defend in a meeting. |
| C-005 | Pull request to `web-platform-tests/wpt`, directory `gpc/`, under the 3-clause BSD license. Suggested reviewers are in `gpc/META.yml`. [WPT CONTRIBUTING.md](https://github.com/web-platform-tests/wpt/blob/master/CONTRIBUTING.md). | That file, as fetched for the audit, states no AI rule. The March 2026 W3C Group Note on large language models says a person remains responsible and should label content that is primarily model output. The Note says W3C itself has not endorsed it. Label the pull request anyway. |

C-005 does not use the GPC specification repository. A substantive edit there requires Working Group participation or a non-member patent licensing commitment. This workspace has neither. That is why the navigation-cache test is the GPC item in this set, and why the combined-header algorithm is held.

### Effort

| ID | Local draft | Adopter, if the change lands | Paid API |
| --- | --- | --- | --- |
| C-001 | A few hours. | A timeout and a default deny on a call the runtime already makes. Framework support was not measured. The issue must not claim it. | None. |
| C-002 | About two hours. | Teams that already fail closed change nothing. Teams that fail open on a state-changing action stop, or they record a named read-only exception. | None. |
| C-003 | About two days, including the example and one query. | The group edits the primer and regenerates HTML. | None. |
| C-004 | About half a day. | The group changes one spreadsheet parent and regenerates. | None. |
| C-005 | One to two days, including the subresource handler, plus a local browser run before submission. | No product change is required by the test. A browser that updates the current document fails the new test. | None. |

The five drafts touch different repositories. They can be written in parallel under `contributions/C-001` through `contributions/C-005`.

### Historical timing, and what November 30 can mean

The audits refuse an acceptance rate. The dates below are the samples they retrieved.

| ID | Sample that fits this draft | 2026-11-30 | 2027-02-15 |
| --- | --- | --- | --- |
| C-001 | #683 merged the same day after agreement. #1204 restored an editing loss: issue 2026-10-21, merge 2026-11-04. #1117 waited from approval on 2026-07-24 to merge on 2026-07-30. #1215 and #1216 were closed in two days when the text was long. | Internally approved issue text. A merge only if a leader has already agreed the exact row. That agreement is not in hand. | A merge into `1.02-dev` is realistic if the issue stays one sentence. No 1.02 release date is published. |
| C-002 | Pull request 225 was approved in about fourteen hours. Pull request 192 merged in about three minutes. Pull request 216 has had no review since 2026-09-03. | The only item for which an external decision is possible. It is possible if the pull request is approved for sending and Rob van der Veer reviews a very small diff. It is not a promise. | A decision is the ordinary outcome for a diff that stays this small, based on that sample. |
| C-003 | Documentation fixes by `bact` merged the same week or after about eight weeks, usually after a chair comment. Pull request #86, a first pull request with no prior issue, was closed in a day and redirected to an issue. | Internal draft. The 25 November agenda is v2.4 commits, AI Act documentation, and AI quality, not #484. | Possible in the v2.4 report if the group takes the text in the December commit window described on 18 November. A longer debate about `rdf:type` and `skos:inScheme` moves the documentation change past that release. |
| C-004 | Same review path. Pull request #254 was incorporated by the chair in his own commit and closed unmerged. | Internal draft, posted only with approval, and only if `2.4-dev` is still wrong. | The parent can be in v2.4 if the group applies it. If the chair chooses the other parent, the result is his decision. |
| C-005 | `wpt` pull request 54446: opened 2025-08-21, first human comment 2025-09-04, merged 2025-09-22, by a Mozilla author. GPC signal tests were reverted once before they stuck. | The test file, unsubmitted. | A pull request can be in review. A merge is a reasonable hope for a test that matches the current draft and has been run locally. A test that fails an implementation can take longer. |

Acceptance for every ID is the external body's merge, published text, or recorded vote. An issue comment, a local file, and a draft pull request are not acceptance.

## Separate-track verification

### C-006 — USAC resolution

The deliverable is already written: `audits/university-policy/usac-resolution-draft.md`, with `evidence-brief.md` and `audit-memorandum.md`. It asks the Academic Senate and the Chancellor to consider three provisions. It enacts none of them.

| Check | Result |
| --- | --- |
| Policies read | USA Constitution (file updated May 2026), Bylaws (file name updated 2026-10-29), and the Resolution Guide. Where the guide and the bylaws differ, the bylaws control. The guide's Friday 3:00 p.m. mail rule is the 2023 text. The bylaws require the Internal Vice President's mailbox by 12:00 p.m. three school days before the meeting. |
| Sponsors | None. Article VI, Section A.5.c requires three Council members. No member has been asked. |
| November 24, 2026 | The meetings page says Tuesdays at 7:00 p.m. The agenda archive fetched on 2026-11-18 stops at November 17. The academic calendar page that was tried returned 404, so Thanksgiving week is unverified. The draft was written so that it is not an item for that agenda. |
| Vote, if it is later placed | A majority of the entire voting membership. The bylaws do not say whether the President is in that denominator. This summary does not convert the text into a required yes-count. |
| UCSA | The January 2, 2025 resolution asks for syllabus language and does not state an evidence rule. Refiling it is abandoned. The ordinary UCSA vote threshold was not found, so any UCSA filing stays `not-checked` and blocked. |
| External result | Posted minutes showing the Council adopted this resolution. Senate amendment of A-306, or a Chancellor's amendment of the Conduct Code, is a later institutional act. It is not the acceptance criterion for C-006. |
| Effort | The text exists. Further local editing waits on internal review. No API cost. |

Themes: human oversight, AI reliability, transparency, privacy, authorization.

### Incident evidence

`audits/research-reuse/AUDIT.md` walked `research/incident-evidence/` on 2026-11-18 and found zero files. The OWASP, W3C, and university audits each record the same absence. There is no contributor policy to apply, because there is no target issue and no local incident note. Citing a case caption, a vendor percentage, or an unsanitized anecdote from a public issue thread is abandoned. A future incident note belongs in `research/incident-evidence/` and needs a primary public source before any candidate ID is opened.

### C-007 — FCC consent revocation

FCC 26-67 is a Report and Order and a Further Notice, released 2026-10-01, published in the Federal Register on 2026-10-26. Comments are due 2026-11-25. Reply comments are due 2026-12-28. The earlier drop used 2026-11-30 as the review date. This item is now drafted for review on 2026-11-23. That change of date does not approve a filing.

The comment in `contributions/C-007-FCC/COMMENT.md` keeps the ten-business-day maximum and asks the Commission to define honoring as a permission record at receipt, cancellation of communications the caller still controls, and a read of that record at origination. It conditions a category-limited informational revocation on a disclosed limit and an all-categories method in the same interaction. It does not recommend seven business days, a ban on one-way informational texting, an extension of 47 CFR 64.1200(d)(5), or the affiliate paragraph in footnote 84. `reproduce.py` reran `audits/fcc/sim_revocation.py` on 2026-11-18: 9 cases, 0 failed assertions. The report states that those assertions are local objects, not carrier behavior, a reasonable-person finding, or a cost.

47 CFR 1.415, 1.419, 1.49, and 1.1206 were read. The policy check is no longer `not-checked`. 47 CFR 1.419(e) still requires a filer name and mailing address, which the draft leaves blank. 47 CFR 1.415(d) still bars a late comment unless the Commission authorizes it. Submission remains `none`. The four-stage example is not an OWASP patch.

### D1 and D2

The research-reuse audit is the record. Zero manuscripts, datasets, results, protocols, limitation statements, licenses, and coauthor approvals. The public GitHub repository `thomasLiu963/ai-governance-initiative` was empty at inspection. Pushing research files there would publish them. No push is authorized.

| Design | Target the audit considered | Blocker |
| --- | --- | --- |
| RR-1 | A local intake manifest | No files to register. |
| RR-2 | A NIST metrology submission or a Testing Guide note, after a reanalysis | No result table, metric, or peer-reviewed source. NIST also forbids non-public material in a public submission. |
| RR-3 | One AISVS requirement compared with an author-stated limitation | No limitation text. The AISVS defects in C-001 stand on the specification, not on D1 or D2. |
| RR-4 | Existing DPV terms and the three existing disclosure values | No manuscript states purpose, data categories, AI involvement, or human review. |
| RR-5 | One clause in a named university policy | No institution was named when that audit was written. The later university audit chose UCLA and is C-006. RR-5 is not a second university candidate. |

Experiments E-1, E-2, and E-3 were specified and not run. They stay unrun. No model call is authorized to fill the gap.

A later D1 or D2 contribution needs, for the track in question, the ten records listed in the research-reuse audit: manuscript status, locator or a quotation permission, license, coauthor approval, confidentiality, dataset description, a stored result, a protocol sufficient to recompute it, the authors' limitation text, and the authors' own split between result and hypothesis. Until those exist, longer-term D1 and D2 work has no candidate ID.

## What the drafter leaves alone

- Files under each `audits/<name>/` directory, including `AUDIT.md`, `audit-memorandum.md`, `evidence-brief.md`, `usac-resolution-draft.md`, and `audits/fcc/sim_revocation.py`.
- Upstream issues, pull requests, email, ECFS, and USAC inboxes.
- Paid inference and billable model APIs.
- `evidence/`. Nothing has been submitted, so nothing there can prove a decision.
