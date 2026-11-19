# Master Tracker

Record of candidate contributions for the AI Governance Initiative. An empty row is not a finding. Acceptance is recorded only when an external body has actually decided, and only with evidence linked from `evidence/`.

Last updated: 2026-11-18. Audits under `audits/` are complete. Local drafting of C-001–C-005 is the implementation work. No submission has been approved or sent. No acceptance exists.

The analysis behind this register is `audits/SUMMARY.md`. Temporary labels T001–T005 map to C-001–C-005. IDs are not reused.

## How to record an entry

Add one row to the register and one section under Candidate details. Use the same ID in both places.

- **ID.** `C-001`, `C-002`, and so on. Do not reuse an ID.
- **Audit.** The assigned directory, such as `audits/w3c-dpv`.
- **Status.** One of: `candidate`, `in-review`, `ready`, `submitted`, `accepted`, `rejected`, `withdrawn`, `dropped`.
- **Document status.** One of: `published-standard`, `draft`, `community-guidance`, `proposed-change`.
- **Source.** Title, version or date, and a stable URL or other exact locator. Quote locators; do not paraphrase a citation you have not opened.
- **Policy check.** Whether the project's contribution policy and AI-assistance policy were read, with locators. `not-checked` blocks submission.
- **Themes.** One or more of: human agency, AI reliability, transparency, privacy, authorization, human oversight.
- **Review by.** Internal review date. The immediate horizon is 2026-11-30. The longer horizon is 2027-02-15.
- **Submission.** `none` until an external submission is explicitly approved. Then record the date, channel, and locator.
- **Acceptance.** `none` until there is an external decision. Then `accepted` or `rejected`, with the decision date.
- **Evidence.** Path under `evidence/`, or `none`.

Do not mark `submitted` or `accepted` from intent, a draft, or a local commit. Status `candidate` means the audit record is sufficient for internal review to start. It does not mean a draft has been approved for sending.

## Implementation queue

Draft C-001 through C-005 under `contributions/`, one directory per ID. Leave every file in `audits/` unchanged. Submission of each item remains `none`.

| ID | Status | Deliverable | External result criterion |
| --- | --- | --- | --- |
| C-001 | `in-review` | `contributions/T001-AISVS/` (`ISSUE.md`, `REVIEW.md`, `9.5.8.patch`). Not sent. | Merge into AISVS `1.02-dev` of that requirement. |
| C-002 | `in-review` | `contributions/T002-Exchange/` (`pull-request.md`, `0001-unreachable-policy-engine-denies-the-action.patch`). Not sent. | Merge that removes the fail-open choice and denies the action when the policy engine is unreachable. |
| C-003 | `candidate` | `contributions/T003-DPV-Membership/` (`COMMENT.md`, `README.md`, `reproduce.py`). Not sent. | Published primer text stating the membership relation for each serialisation, with the `pd:BloodType` example. |
| C-004 | `candidate` | `contributions/T004-DPV-Rights/` (`COMMENT.md`, `README.md`, `reproduce.py`). Not sent. Recommends the 9 September action: parent `dpv:FulfilmentOfObligation`. | Vocabulary commit that parents `dpv:RightsFulfilment` on a purpose. |
| C-005 | `candidate` | A GPC navigation-cache Web Platform Test, unsubmitted until it has been run locally. | Merged `wpt` file that fails a same-document preference change. |
| C-006 | `candidate` | Existing USAC resolution draft. Read it. Do not mail it. | Council minutes showing adoption of that resolution. |
| C-007 | `dropped` | None. The FCC comment window closes before internal review. | None. A dropped item has no acceptance test. |

Incident-evidence work and D1/D2 designs have no ID. They are recorded under Tracks without a candidate.

## Register

| ID | Audit | Status | Document status | Source | Policy check | Themes | Review by | Submission | Acceptance | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | `audits/owasp-aisvs` | `in-review` | `draft` | AISVS 1.02-dev, commit `092232f012ec10d654c1ca345fa10d5a5a8be12a` (2026-11-11), C9 and glossary. https://github.com/OWASP/AISVS/tree/092232f012ec10d654c1ca345fa10d5a5a8be12a/1.02-dev/en | checked | authorization, AI reliability | 2026-11-30 | none | none | none |
| C-002 | `audits/owasp-exchange` | `in-review` | `community-guidance` | OWASP AI Exchange, commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441` (2026-11-16), `#LEAST MODEL PRIVILEGE`. https://owaspai.org/go/leastmodelprivilege | checked | authorization, AI reliability | 2026-11-30 | none | none | none |
| C-003 | `audits/w3c-dpv` | `candidate` | `community-guidance` | DPV 2.3 Final Community Group Report, 25 February 2026, primer section 4, issue #484. https://w3c-cg.github.io/dpv/primer | checked | transparency, privacy, AI reliability | 2026-11-30 | none | none | none |
| C-004 | `audits/w3c-dpv` | `candidate` | `community-guidance` | DPV 2.3, `dpv:RightsFulfilment` parent, issue #486, still present in `2.4-dev` on 2026-11-18. https://github.com/w3c-cg/dpv/issues/486 | checked | privacy, authorization | 2026-11-30 | none | none | none |
| C-005 | `audits/w3c-gpc` | `candidate` | `draft` | GPC Working Draft, 24 September 2026, caching rule; WPT `gpc/` as read 2026-11-18. https://www.w3.org/TR/2026/WD-gpc-20260924/ | checked | privacy, human agency | 2026-11-30 | none | none | none |
| C-006 | `audits/university-policy` | `candidate` | `proposed-change` | Interim 2026 UCLA Student Conduct Code and Divisional Regulation A-306, read 2026-11-18. Draft: `audits/university-policy/usac-resolution-draft.md` | checked for USAC; UCSA vote threshold `not-checked` | human oversight, AI reliability, transparency, privacy, authorization | 2026-11-30 | none | none | none |
| C-007 | `audits/fcc` | `dropped` | `proposed-change` | FCC 26-67, released 2026-10-01; Further Notice comments due 2026-11-25. https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf | `not-checked` (47 CFR 1.419 not read in full) | human agency, authorization, human oversight, privacy, transparency, AI reliability | — | none | none | none |

## Candidate details

### C-001 — AISVS fail-closed when the policy decision does not arrive

- **Provisional label:** T001
- **Audit:** `audits/owasp-aisvs`
- **Exact source:** AISVS 1.02-dev at commit `092232f012ec10d654c1ca345fa10d5a5a8be12a`, 2026-11-11. Glossary fail-closed entry in `1.02-dev/en/0x90-Appendix-A_Glossary.md`. Prior row `9.7.4` at commit `19e6410889`. Removal in pull request #934, 2026-06-15. Locked releases v1.0 and v1.01, both GitHub-dated 2026-10-16, shipped without the row. https://github.com/OWASP/AISVS/tree/092232f012ec10d654c1ca345fa10d5a5a8be12a/1.02-dev/en
- **Document status:** `draft` for 1.02-dev, which is the only tree a contribution may edit. 1.0 and 1.01 are published OWASP community standards and are locked.
- **Gap or error:** No current requirement says what happens when the policy decision point for an agent action does not return a decision. The glossary still says AISVS requires AI components with safety or authorization responsibilities to fail closed. Re-read on 2026-11-18: `9.5.1`, `9.5.3`, `5.2.5`, `5.2.1`, `9.6.2`, `7.1.3`, `10.4.15`, and ASVS 5.0 `16.5.3` do not state this failure. The requirement merged from #683 was still `9.7.4` when #928 merged at 11:16 UTC on 2026-06-15, and #934 deleted it at 14:24 UTC the same day with an empty body and no review. Searches through 2026-11-18 found no issue reopening it.
- **Proposed change:** One appended Level 2 row, plus the matching Appendix B line. `9.5.8` was still free on 2026-11-18. Text: "Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2." "Defined" matches `9.6.2`. A decision is an allow, a deny, or a referral to the C9.2 approval gate.
- **Deliverable:** `contributions/T001-AISVS/ISSUE.md` is the paste-ready issue. `REVIEW.md` is the defense, submission steps, and AI-assistance note. `9.5.8.patch` is local only. It was applied to copies of the two `1.02-dev` files from `092232f` and both hunks applied. It has not been sent. Omit the old logging clause, CAEP, a new chapter, and any revival of C9.7.
- **Themes:** authorization, AI reliability.
- **Implementation requirements:** An adopter that already calls a policy engine on each agent action adds a defined timeout and blocks the action when that call returns no decision. An error, an empty result, a dropped connection, and silence are not decisions. This row does not specify a product or a framework. Envoy `ext_authz` defaults to deny when the authorization service is unavailable; that is an existence proof, not a required implementation. Agent-framework defaults were not surveyed.
- **Contribution policy:** Issue before a pull request. Work targets `1.02-dev/` only. Append IDs; do not renumber or reuse retired IDs. https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md and https://github.com/OWASP/AISVS/blob/main/RELEASE.md
- **AI-assistance policy:** Checked in `CONTRIBUTING.md` and `AGENTS.md` on `main`. Drafting with AI is allowed when the contributor defends every sentence and the control is testable. Keep the issue short. Maintainers closed #1215 and #1216 on 2026-11-18 as unreadable generated discussion.
- **Dependencies:** `9.5.8` was confirmed unused on 2026-11-18, and `main` was still `092232f`. Re-read C9.5 if `main` moves before filing. Open PR #1227 edits C9.3 and Appendix B and does not take `9.5.8`; regenerate the patch if it merges before a leader asks for one. No dependency on D1, D2, incident files, C-002, or the 9.5.6 wording. Do not resubmit #1196.
- **Effort:** A few hours. No paid API.
- **Review path:** GitHub issue on OWASP/AISVS. A pull request only if a leader asks. Closest samples: #683 (same control, merged the day agreement was reached) and #1204 (an editing loss restored; issue 2026-10-21, merge 2026-11-04).
- **Internal review:** Drafted 2026-11-18. Status `in-review`. The text is not approved for sending. The realistic product by 2026-11-30 is an approved issue. A merge by that date requires a leader's agreement to the exact row, which is not yet recorded.
- **External submission:** none
- **External result criterion:** A merge commit on `1.02-dev` that adds this Level 2 requirement. An encouraging comment is not acceptance. Inclusion in a numbered 1.02 release is a separate, unpublished event.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** A quoted reason for deleting this predicate inside #934. The chapter rewrite was intentional; a decision that this failure should stop being a requirement is not in the record. Slack. Whether current agent frameworks already time out closed. Any commit on `main` after `092232f`. The OWASP AI Testing Guide.

### C-002 — AI Exchange single rule when the policy engine is unreachable

- **Provisional label:** T002
- **Audit:** `audits/owasp-exchange`
- **Exact source:** Repository `OWASP/www-project-ai-security-and-privacy-guide`, commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441`, committed 2026-11-16. `#LEAST MODEL PRIVILEGE` in `content/ai_exchange/content/docs/1_general_controls.md`. Permalink https://owaspai.org/go/leastmodelprivilege
- **Document status:** `community-guidance`. Living OWASP flagship documentation. The project page says "Version 1.0". The repository is updated continuously. It is not a de jure standard.
- **Gap or error:** Runtime policy validation says "Fail closed if the policy engine is unreachable." The limitations paragraph says "policy engine outage requires an explicit fail-closed vs fail-open choice." Both sentences were read on that commit, at lines 747 and 760. They were added together in `693d59d6f7` (pull request 185, merged 2026-08-03). No review comment and no later commit treats them as different rules. A search for `fail-open` on 2026-11-18 returned no issue. The pair is an unreconciled contradiction, not a recorded exception for reads.
- **Proposed change:** One clause. Replace "policy engine outage requires an explicit fail-closed vs fail-open choice" with "if the policy engine is unreachable, deny the action." Leave "Fail closed if the policy engine is unreachable" in place. Do not add a read-only fail-open exception, a timeout, or a new control name.
- **Deliverable:** `contributions/T002-Exchange/`. Paste-ready pull request in `pull-request.md`. Patch `0001-unreachable-policy-engine-denies-the-action.patch`, checked by applying it to the file from `c68371ed`. `rationale.md` and `examples.md` stay local. Not sent. This is the one item to send first if a single external submission is approved before 2026-11-30.
- **Themes:** authorization, AI reliability.
- **Implementation requirements:** Adopters that already deny the action when the policy engine is unreachable change nothing. Adopters that proceed during an outage stop doing so for every action this control already sends through the engine: tool calls, data access, inter-agent messages, and outbound communication. The patch does not authorise a fail-open read.
- **Contribution policy:** Checked. Small clarifications may be a pull request without an issue. https://owaspai.org/contribute/ and `CONTRIBUTING.md` in that repository.
- **AI-assistance policy:** Checked on the contribute page. Material AI assistance must be labeled, including what the assistant was used for and to what extent, in the pull-request body.
- **Dependencies:** Re-read the two sentences at the current commit before opening a pull request. No dependency on C-001, D1, D2, or incident files. Do not attach this edit to issue 188 or issue 222.
- **Effort:** About two hours. No paid API.
- **Review path:** Pull request to `OWASP/www-project-ai-security-and-privacy-guide`. Sample: pull request 225, about fourteen hours to approval; pull request 192, about three minutes; pull request 216, no review from 2026-09-03 through 2026-11-18. Same-week merges in the sample are small plain diffs that Rob van der Veer reviewed.
- **Internal review:** Drafted 2026-11-18. Status `in-review`. The text is not approved for sending. An external decision by 2026-11-30 is possible and is not the success criterion.
- **External submission:** none
- **External result criterion:** A merge commit whose rendered `#LEAST MODEL PRIVILEGE` text no longer offers a fail-open choice, and whose limitations paragraph denies the action when the policy engine is unreachable. The permalink https://owaspai.org/go/leastmodelprivilege quoting that clause is the public check.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** The live site was not clicked through. ISO/IEC and EU AI Act claims inside the Exchange were not re-read. Private Slack and workstreams. Who will merge a future pull request.

### C-003 — DPV concept-membership test for issue #484

- **Provisional label:** T003
- **Audit:** `audits/w3c-dpv`
- **Exact source:** DPV 2.3, Final Community Group Report, 25 February 2026, https://w3c-cg.github.io/dpv/2.3/dpv/ . Primer section 4, https://w3c-cg.github.io/dpv/primer . Issue #484, opened 27 August 2026, labels `todo` and `help-wanted`, no assignee. Rechecked 18 November 2026: zero comments, `updated_at` `2026-08-27T13:13:05Z`. https://github.com/w3c-cg/dpv/issues/484 . Files at `master` `689d32c0f7c571d32f7f8635ae548fcc1c3ff695` and `dev` `aff91c294b105d9a261ea8622350b0fc7ef0e293`.
- **Document status:** `community-guidance`. The report states that it is not a W3C Standard and is not on the W3C Standards Track.
- **Gap or error:** The primer section 4.2 table lists `rdfs:subClassOf or skos:broader` and `owl:subClassOf`. Parsed `2.3/dpv/dpv.ttl`: 973 classes with a preferred label, 948 with `skos:broader`, 195 with `rdfs:subClassOf`. The OWL files use `rdfs:subClassOf` and contain no `skos:broader` and no `owl:subClassOf`. `pd:BloodType` has direct `skos:broader pd:MedicalHealth`. `skos:broader+` reaches `dpv:SpecialCategoryPersonalData`. In `2.3/pd/pd.ttl` the type, `pd:specialcategory-classes`, and that path are the same 32 concepts. `rdfs:subClassOf+` does not reach the category in the RDFS file. It does in the OWL file, under the `owl` IRIs.
- **Proposed change:** The comment in `contributions/T003-DPV-Membership/COMMENT.md`. Category membership is `rdf:type` in both serialisations. The direct parent is `skos:broader` in RDFS+SKOS and `rdfs:subClassOf` in DPV-OWL. The special-category scheme matches the type in this release because a generator hook copies the broader path. `pd:ProfessionalExperience` is typed the undeclared IRI `pd:PersonalData`, so the comment does not say every type IRI is the category. No pull request.
- **Deliverable:** `contributions/T003-DPV-Membership/`. `COMMENT.md` is the paste-ready comment. `README.md` is the evidence, wording, meeting note, AI-assistance rule, and submission steps. `reproduce.py` was run on 18 November 2026 against the pinned files. `results/report.txt` is that run. Not sent.
- **Themes:** transparency, privacy, AI reliability.
- **Implementation requirements:** The group edits the primer source and regenerates HTML. Adopters query the relation the primer names for the serialisation they loaded. This project does not regenerate the specification.
- **Contribution policy:** Checked. Discuss before a pull request. Do not edit generated HTML, RDF, or exported CSVs. https://github.com/w3c-cg/dpv/blob/master/contributing.md and https://github.com/w3c-cg/dpv/wiki/Contribution-Guide (wiki date 12 February 2026).
- **AI-assistance policy:** The DPV guide does not mention AI tools. https://www.w3.org/2026/10/draft-ai-policy.html is a draft and is not a W3C policy. The check is complete: disclose assistance if a tool drafts the substance, and keep the comment short. The Advisory Board LLM document named by that draft was not retrieved.
- **Dependencies:** The SPARQL run is in `contributions/T003-DPV-Membership/results/report.txt`. Re-run `reproduce.py` before posting. No dependency on C-004 other than using two separate comments. The 25 November 2026 public agenda does not name #484. The 18 November minutes put parent changes, v2.4 commits, and other items from that day on that meeting. Do not ask for agenda time.
- **Effort:** About two days. No paid API.
- **Review path:** Comment on #484. Decisions are taken in DPVCG meetings. Documentation fixes in the sample merged the same week or after about eight weeks, usually after a comment by `coolharsh55`. A first pull request without an issue (#86) was closed and redirected.
- **Internal review:** 2026-11-30 for the draft. Posting waits for explicit approval. The chair's proposed December commit window is a hope recorded in the 18 November minutes, not a resolution.
- **External submission:** none
- **External result criterion:** The published primer states, with a worked `pd:BloodType` example, which relation answers category membership in the RDFS+SKOS serialisation and which relation answers it in the OWL serialisation. A merged documentation commit or the v2.4 primer, and a closed issue that points at that text, is the record. The help-wanted label is not acceptance. Our comment is not acceptance.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** Online spreadsheets. The repository CSV export was read. An OWL reasoner was not run; subclass results are SPARQL property paths. Whether `primer/index.html` is generated. The 25 November join link. The Advisory Board LLM document. HTML other than the primer and the SKOS guide.

### C-004 — DPV purpose parent for issue #486

- **Provisional label:** T004
- **Audit:** `audits/w3c-dpv`
- **Exact source:** Issue #486, https://github.com/w3c-cg/dpv/issues/486 . Rechecked 18 November 2026: open, two comments, both 9 September 2026. `dpv:RightsFulfilment` in DPV 2.3 `2.3/dpv/modules/purposes.ttl` at `689d32c0f7c571d32f7f8635ae548fcc1c3ff695` and in `dev` `2.4-dev/dpv/modules/purposes.ttl` at `aff91c294b105d9a261ea8622350b0fc7ef0e293`. Minutes https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/meetings/meeting-2026-09-09.html#a01 .
- **Document status:** `community-guidance`. Same Final Community Group Report as C-003. The error is also in the `2.4-dev` tree.
- **Gap or error:** A purpose's taxonomy parent is a legal basis. On the issue, `besteves4` named `dpv:FulfilmentOfObligation` or `dpv:LegalCompliance`. The 9 September 2026 minutes, with Beatriz present, action the parent `dpv:FulfilmentOfObligation` and a description update. Neither action is in 2.3 or `2.4-dev`. SPARQL finds this as the only purpose whose broader target is not a purpose, other than branch roots parented on `dpv:Purpose`. The OWL file makes the class `rdfs:subClassOf+` Legal Basis while typing it as a purpose. The purposes HTML lists it as an object of `hasLegalBasis`.
- **Proposed change:** The comment in `contributions/T004-DPV-Rights/COMMENT.md`. Apply the minuted parent `dpv:FulfilmentOfObligation`. Leave `ParentType` as `dpv:Purpose`. Do not use `dpv:LegalCompliance`: its definition and scope note are legal-obligation processing, which is the reading the minutes rejected. Include the SPARQL guard. Ask the chair to change the Purpose spreadsheet. No pull request.
- **Deliverable:** `contributions/T004-DPV-Rights/`. `COMMENT.md` is the paste-ready comment. `README.md` records the parent comparison, downstream checks, the 25 November note, AI-assistance requirements, and submission steps. `reproduce.py` was run on 18 November 2026. Not sent.
- **Themes:** privacy, authorization.
- **Implementation requirements:** The group changes one parent in the spreadsheet and regenerates. Adopters that walked from `dpv:LegalObligation` into purposes stop seeing `dpv:RightsFulfilment` there.
- **Contribution policy:** Same as C-003.
- **AI-assistance policy:** Same as C-003.
- **Dependencies:** Re-read issue #486 and the 9 September minutes before posting. If the chair has already committed a parent, do not send a second comment. The 25 November meeting is a viable slot for the group to apply the existing action during the parent pass named in the 18 November minutes. It is not a channel for this project: the join link is login-restricted, and no agenda mail had been posted when the November list index was fetched. Do not email the list. The SPARQL run is in `contributions/T004-DPV-Rights/results/report.txt`.
- **Effort:** About half a day. No paid API.
- **Review path:** Comment on #486. The 18 November minutes say the chair will propose resolutions and commit the error list. Pull request #254 shows he sometimes copies a change into his own commit and closes the pull request.
- **Internal review:** 2026-11-30.
- **External submission:** none
- **External result criterion:** A `dev` or published vocabulary commit in which `dpv:RightsFulfilment` has `skos:broader dpv:FulfilmentOfObligation` and no longer has `skos:broader dpv:LegalObligation`. If the commit uses another purpose, including `dpv:LegalCompliance`, that is the group's choice. Credit is limited to the written rationale. A comment with no vocabulary change is not acceptance.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** The online Purpose spreadsheet. `code/vocab_csv/Purpose.csv` on `dev` still has `ParentTerm` `dpv:LegalObligation`. The generator was not executed. No OWL reasoner. HTML other than the purposes module. The 25 November join link. The Advisory Board LLM document.

### C-005 — GPC navigation-cache Web Platform Test

- **Provisional label:** T005
- **Audit:** `audits/w3c-gpc`
- **Exact source:** Global Privacy Control, W3C Working Draft, 24 September 2026. https://www.w3.org/TR/2026/WD-gpc-20260924/ and https://www.w3.org/TR/gpc/ . Editor's draft `index.html` on `main`, caching at lines 212–214 as read for the audit. Tests: https://github.com/web-platform-tests/wpt/tree/master/gpc , files `navigator-globalPrivacyControl.https.html`, `sec-gpc.https.html`, and `global_privacy_control.testdriver.html`, read 2026-11-18.
- **Document status:** `draft`. Recommendation-track Working Draft. Publication as a Working Draft is not an endorsement. The deliverable is a test, not a specification edit.
- **Gap or error:** The draft says a preference change during or after a top-level navigation is not reflected until the next navigation. The existing tests call `test_driver.set_global_privacy_control` and then open a new document. Nothing asserts that the already loaded document keeps the old `navigator.globalPrivacyControl` and that a same-document subresource keeps the old `Sec-GPC`. No open WPT pull request for this assertion was found.
- **Proposed change:** One new testharness file under `wpt/gpc/`. Read the current attribute and the `Sec-GPC` value on a same-document subresource. Set the opposite boolean. Assert that the current document and a second same-document subresource keep the original values. Open a new top-level document and assert that it carries the new value. A dedicated-worker assertion may record the snapshot requested in issue #146, and it must be labeled as that issue's proposed behavior. Service workers stay out of this file.
- **Deliverable:** `contributions/C-005/` test file and a short note of the local run. The run uses a browser that already implements the testdriver extension. No specification pull request.
- **Themes:** privacy, human agency.
- **Implementation requirements:** The test reuses existing `testdriver.js` commands and needs a same-document subresource. A browser that applies the set command to the current document fails. Landing a failing test is a reason to discuss it before treating the failure as final, which is also the reason to write it.
- **Contribution policy:** Checked. WPT contributions are under the 3-clause BSD license. https://github.com/web-platform-tests/wpt/blob/master/CONTRIBUTING.md . Suggested reviewers in `gpc/META.yml`: AramZS, bvandersloot-mozilla, j-br0, pes10k, and SebastianZimmeck. The GPC specification's patent commitment does not apply to this test-only candidate. Do not open a pull request on `w3c/gpc` as part of C-005.
- **AI-assistance policy:** `CONTRIBUTING.md` in `w3c/gpc` and the fetched WPT `CONTRIBUTING.md` state no AI rule. https://www.w3.org/TR/llms-standards/ (Group Note, 24 March 2026) says a person remains responsible and should label content that is primarily model output. The Note says the Advisory Board endorsed it and W3C has not. https://www.w3.org/2026/10/draft-ai-policy.html is not yet a W3C policy. Label the pull request.
- **Dependencies:** Local execution before any submission. The first GPC test landing was reverted the same day (`f564d65` added, `3c910a5` reverted, `d5d5da0` re-landed, all on 2025-10-30 and 2025-10-31). Service-worker assertions wait on an editor answer to https://github.com/w3c/gpc/issues/146 . C-005 does not wait on the combined-header algorithm in issue #114.
- **Effort:** One to two days, including the subresource handler. No paid API.
- **Review path:** Pull request to `web-platform-tests/wpt`. Closest sample is wpt#54446: opened 2025-08-21, first human comment 2025-09-04, approved and merged 2025-09-22 by `jgraham`, for a Mozilla author.
- **Internal review:** 2026-11-30 for the unsubmitted file. A local run is part of readiness if a capable browser is available. Absence of that run blocks submission and does not block drafting.
- **External submission:** none
- **External result criterion:** A merged file on `web-platform-tests/wpt` `master` that fails a browser changing `Sec-GPC` or `navigator.globalPrivacyControl` in the current document before the next top-level navigation, plus the pull-request review thread. A wpt.fyi result with a non-empty subtest count is the execution check. An empty count does not establish a pass or a fail.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** The test was not executed. No browser was launched. Stable-channel shipping tables. A complete wpt.fyi comparison. The Chromium code review linked from GPC #151.

### C-006 — USAC resolution on generative-AI detection evidence

- **Audit:** `audits/university-policy`
- **Exact source:** Interim 2026 UCLA Student Conduct Code, https://studentconduct.ucla.edu/2026-individual-student-code . Divisional Regulations A-306 and A-315, https://senate.ucla.edu/BylawsandRegulations/volume-2 . Both read 2026-11-18. Local proposal text: `audits/university-policy/usac-resolution-draft.md`. One-page brief: `audits/university-policy/evidence-brief.md`. Record: `audits/university-policy/audit-memorandum.md`.
- **Document status:** `proposed-change`. The Code and A-306 are current campus rules. The resolution is this project's proposal. It is not sponsored and not on an agenda.
- **Gap or error:** The Code prohibits unauthorized or unattributed AI use and places the burden on the University by a preponderance. A-306 requires a report and a Deferred Report while suspected cheating is pending. Neither text, nor PACAOS 102.01 as read from the UCSD-hosted interim copy, states the evidentiary value of a detection score. UCLA Humanities Technology sample syllabus language says confirmed detector use will be treated as academic dishonesty and does not define confirmation.
- **Proposed change:** The Council's opinion, in the existing draft, covering three local provisions. UP-001: a detection output is not the sole basis for a conduct finding or for a grade penalty imposed for suspected unauthorized generative-AI use. UP-002: before either consequence, the student receives the work, the course rule, the tool name, the date, the output, and a chance to respond; the decision states the other evidence. UP-003: a prohibition is stated before the work begins, and coursework is not uploaded to a detection service the campus has not approved.
- **Deliverable:** The existing draft and brief. Internal review reads those files. Do not email `ivp@usac.ucla.edu`, any officer, or any sponsor. Do not place the text on the November 24, 2026 agenda.
- **Themes:** human oversight, AI reliability, transparency, privacy, authorization.
- **Implementation requirements:** The Academic Senate would amend A-306 or issue a legislative ruling. The Chancellor would amend the Code after the consultation and Office of the President review the Code already requires. Instructors would state the course rule before the work starts. The campus unit that approves instructional software would keep unapproved detector uploads out of the process. USAC passage does none of those things.
- **Contribution policy:** Checked for USAC. Constitution file `USA-Constitution-Updated-May-2026.pdf`. Bylaws file `Bylaws-Master-2026-Revision_updated-102926.pdf`. Resolution Guide on the USAC Miscellaneous Documents page. A resolution needs three Council sponsors and a majority of the entire voting membership. Action items need their text in the packet. The bylaws, not the guide's Friday 3:00 p.m. instruction, set the submission clock. UCSA ordinary-vote threshold was not found. Any UCSA filing is `not-checked` and blocked. Do not refile the 2025-01-02 syllabus resolution.
- **AI-assistance policy:** No USAC AI-assistance rule was found in the documents read. The draft is local and was prepared with AI assistance. A person checks every quotation against the memorandum before any later external use.
- **Dependencies:** Three sponsors, none obtained. A confirmed meeting date. The 2026–27 academic calendar was not retrieved, so November 24, 2026 is unverified. The official UCOP PACAOS PDF was not downloaded. Bruin Learn's detector settings were not inventoried. No UCLA case file was reviewed.
- **Effort:** The draft exists. No paid API. No detector was run.
- **Review path:** Internal review of the existing text by 2026-11-30. Any later external step is a Council agenda after sponsors exist. The February horizon is the earliest planning date for that step. Passage creates two update duties for the primary sponsor, at the second or third meeting and at the sixth or seventh, unless the Council cancels them.
- **Internal review:** 2026-11-30.
- **External submission:** none
- **External result criterion:** Posted USAC minutes recording that this resolution received a majority of the entire voting membership, with at least three Council sponsors listed in the Council packet. Adoption of Code or Senate text is a separate institutional result and is not acceptance of C-006. The resolution finds no named student responsible or not responsible.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** See the memorandum's unverified list. In particular: actual campus use of a score, whether November 24, 2026 is a meeting day, the canonical UCOP PACAOS file, the *Kato* complaint and order PDFs, *Rignol* entries after 2026-07-24, and any sponsor's consent.

### C-007 — FCC comment defining how a revocation is honored

- **Audit:** `audits/fcc`
- **Exact source:** *Rules and Regulations Implementing the Telephone Consumer Protection Act of 1991*, CG Docket No. 02-278, FCC 26-67, Report and Order and Further Notice of Proposed Rulemaking, adopted 2026-09-30, released 2026-10-01. https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf . Further Notice: 91 FR 67239, FR Doc. 2026-21820, comments due 2026-11-25, reply comments due 2026-12-28. https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21820.htm
- **Document status:** `proposed-change` for the unfiled comment. The Report and Order is a final rule effective 2026-11-25. The Further Notice is an open proposed rule. 47 CFR 64.1200 as displayed on eCFR on 2026-11-18 was the pre-amendment unofficial text.
- **Gap or error:** Paragraphs (a)(10) and (a)(11), including the November 25 text, require a revocation to be honored within an outer bound and do not define honoring as a permission write, cancellation of messages still in the caller's control, and a later origination check. The Further Notice asks about the outer bound, exclusive means, category limits, one-way texting, and affiliates. The audit's three recommended definitions answer those questions. They are not current law.
- **Proposed change:** None will be filed. The unfiled text remains in `audits/fcc/AUDIT.md` section 5. The local fixture remains `audits/fcc/sim_revocation.py` (9 cases, 0 failed assertions, run 2026-11-18).
- **Deliverable:** None. Status is `dropped`.
- **Themes:** human agency, authorization, human oversight, privacy, transparency, AI reliability.
- **Implementation requirements:** Not adopted. A caller that implemented the unfiled text would record a permission state at receipt, cancel covered messages still in its control, and reread that state at origination.
- **Contribution policy:** 47 CFR 1.415 was read. The Further Notice's filing and ex parte directions were read. 47 CFR 1.419 was not read in full. Policy check is `not-checked`, which blocks submission independently of the calendar.
- **AI-assistance policy:** No AI-assistance disclosure rule for comments was found in the Further Notice or in 47 CFR 1.415. That absence was checked. It is not a reason to file.
- **Dependencies:** The comment date, 2026-11-25, is before the internal-review date, 2026-11-30. Reply comments may respond only to matters already raised. The audit did not request approval to file. The joint-letter attachment, the CGB waiver orders, and 47 CFR 1.419 were not fully read.
- **Effort:** Not spent on a filing. The research memo and fixture already exist. No paid API.
- **Review path:** Closed for this window. Electronic Comment Filing System, CG Docket No. 02-278, would have been the channel. Richard D. Smith was not contacted. This audit is not an ex parte presentation.
- **Internal review:** Not scheduled. The item is dropped.
- **External submission:** none
- **External result criterion:** None. There is no acceptance condition. A future Commission request for further comment would be a new candidate, with a new ID, after 47 CFR 1.419 is read and Thomas approves that filing.
- **Acceptance:** none
- **Evidence:** none
- **Not verified:** The items in section 11 of the FCC audit, including prevalence, cost, carrier behavior, and model labeling.

## Tracks without a candidate

### Incident evidence

No ID. `research/incident-evidence/` contained zero files on 2026-11-18 (`audits/research-reuse/AUDIT.md`). No completed audit reads the AI Incident Database. Do not open an issue, a database submission, or a citation from this track. A later ID requires a primary public source filed in that directory and a named receiving document with a confirmed gap.

### D1 and D2

No ID. `research/D1/` and `research/D2/` contained zero files on 2026-11-18. RR-1 through RR-5 in `audits/research-reuse/AUDIT.md` are blocked designs, not candidates. E-1, E-2, and E-3 were not run. External use waits on a manuscript with status, locator or quotation permission, license, coauthor approval, confidentiality, dataset description, stored result, recomputable protocol, author limitation text, and the authors' own result-versus-hypothesis split. C-006 is the university work that does have sources. It does not reuse D1 or D2.

## Held findings with no ID

Do not draft these for the November set. Conditions for revisiting them are in `audits/SUMMARY.md`.

- AISVS 9.5.7 timing sentence, after a reply on C-001.
- Exchange OX-1 approval-screen inputs. A December draft is at `contributions/OX-1-Exchange/`. No ID. Not part of the November send, and not attached to C-002.
- Exchange OX-3 residual on issue 188, only after explicit approval, with no February acceptance forecast.
- DPV #500 `rdfs:Label` comment, if the issue is still unanswered.
- GPC issue #114 combined-value comment, after a patent commitment or a comment-only approval. Specification pull requests on `w3c/gpc` are out of bounds until then.
- GPC issue #146 worker text, after an editor chooses.
- AI Testing Guide AITG-APP-13 and AITG-APP-14 procedures, then the AITG-APP-10 stated-preference case, only if review resumes.
- AI Content Disclosure erratum, when the chairs open a new version.

## Abandoned work

Do not assign an ID and do not draft. Reasons are in `audits/SUMMARY.md`.

- AISVS 9.5.6 predicate restoration as a separate issue, the end-user-credential row, and any refile of #1196.
- Occupied or closed AISVS issues #1226, #1220, #1217, #1195, #1187, #1122, #1152, #1214, #1215, and #1216.
- New Exchange control families, tool listings, taxonomies, and enforceability scales, and issues or pull requests 244, 276, 191, 192, 177, 202, 216, 222, 246, and 247.
- DPV #465, #451, #482, and #501 as our proposals.
- GPC purpose-conditional signals, an AI-training meaning, a GDPR rewrite, and a competing pull request on #164.
- AI Content Disclosure vocabulary additions, a non-HTML specification, and a new WHATWG HTML filing.
- Testing Guide oracle framework #80/#81, new test numbers, and the occupied APP-06 pull requests.
- A detector accuracy study for the USAC text.
- NIST YAML and any D1 or D2 external text.
- The FCC filing represented by dropped C-007.

## Submission log

External submissions require explicit approval before they are sent. None have been approved or sent.

| Date | Candidate | Channel | Approval | Locator | Result |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

## Evidence index

Files placed in `evidence/` are listed here. None yet.

| Path | What it proves | Related ID |
| --- | --- | --- |
| — | — | — |
