# NIST track — Phase 1 report

Inspection date: 2026-11-19.  
Workspace: `/Users/thomas/Desktop/ai-governance-initiative`.  
Prior local audit read: `audits/research-reuse/AUDIT.md`, inspection date 2026-11-18.

This report covers two pathways and keeps them separate: the NIST AI Metrology Center submission process, and the NIST information-quality correction process. No pull request was opened. No email was sent. No correction request was submitted. No YAML file was drafted. No experimental result was created. Nothing in this file was peer-reviewed, and this inspection does not claim that any research was reviewed.

**Substantive candidates that survive: 0.** The empty D1 and D2 directories do not close the Metrology Center pathway. They block any claim about a result. The submission scaffold, with blank evidence fields, is `execution/phase1/drafts/nist-metrology-structure.md`. No correction request is drafted, because no qualifying error was found. The controlling list is `execution/phase1/MASTER_RANKING.md`.

## How this inspection was done

Local reads were limited to the research-reuse audit, `PROJECT_CONTEXT.md` headings for the research directories, and directory listings. Public pages and the GitHub API were read. No repository was cloned. No paid API was called.

Pages fetched on 2026-11-19:

- https://airc.nist.gov/metrology/
- https://airc.nist.gov/metrology/how-to-submit/
- https://airc.nist.gov/metrology/how-to-submit/what-reviewers-look-for/
- https://airc.nist.gov/metrology/how-to-submit/what-to-have-ready/
- https://airc.nist.gov/metrology/how-to-submit/what-happens-next/
- https://raw.githubusercontent.com/usnistgov/ai-metrology-submissions/main/CONTENT_STANDARDS.md
- https://raw.githubusercontent.com/usnistgov/ai-metrology-submissions/main/SUBMISSION_FORMAT.md
- https://raw.githubusercontent.com/usnistgov/ai-metrology-submissions/main/CONTRIBUTING.md
- https://raw.githubusercontent.com/usnistgov/ai-metrology-submissions/main/submissions/README.md
- https://api.github.com/repos/usnistgov/ai-metrology-submissions
- https://api.github.com/repos/usnistgov/ai-metrology-submissions/contents/submissions
- https://api.github.com/repos/usnistgov/ai-metrology-submissions/pulls?state=all&per_page=100
- Issue comments and pull-request reviews for every pull request returned by that list
- https://www.nist.gov/director/nist-information-quality-standards (HTML, for links and modification time)
- https://www.nist.gov/document/bernstein-2025-initial-request
- https://www.nist.gov/document/bernstein-2025-initial-response
- https://www.nist.gov/document/bernstein-2025-appeal-request
- https://www.nist.gov/document/bernstein-2025-appeal-response
- A third-party PDF copy of an August 2020 denial letter, opened only as a document that is not on the current NIST log: https://richardgage911.org/wp-content/uploads/August-2020-NIST-Denial-of-AE911Truth-et-als-2020-Request-for-Correction.pdf

The pulls list returned 28 pull requests and no `Link` header, so it was treated as the full set: numbers 1–27 and 29. Number 28 was not in that list. A follow-up request for issue 28 returned HTTP 403 (rate limit). This report does not describe number 28.

Review and comment timestamps were retrieved for all 28 pull requests. Review bodies other than pull request 19 were read from the opening text returned by the API, not from the full rendered thread. Pull request 19 was also opened as a page, including the 2026-09-15 review and the 2026-10-09 comment. Check-run records were not retrieved, so this report does not time the automated validator from observation.

The appeal-response PDF text extraction is degraded in places. Dates, the scope holding, and the denial sentence quoted below are taken from passages that remained readable. Garbled lines are not treated as quotations.

## Local research: D1 and D2 are empty

Listed on 2026-11-19.

| Path | Result |
| --- | --- |
| `research/D1/` | Directory exists. Zero files. Zero subdirectories. Modification time `2026-11-18T13:42:59`. Mode `drwxr-xr-x`. |
| `research/D2/` | Same. Modification time `2026-11-18T13:42:59`. Mode `drwxr-xr-x`. |
| `research/incident-evidence/` | Same timestamp and mode. Zero files. Not used as evidence. |
| `experiments/` | Directory exists. Zero files. |
| `evidence/` | Directory exists. Zero files. |
| `references/` | Directory exists. Zero files. |

A file walk of `research/` returned no regular files. The 2026-11-18 audit’s empty-directory finding is unchanged.

Experiments E-1 (numerical reanalysis), E-2 (protocol completeness), and E-3 (separating results, hypotheses, and limitations) are specified in the audit and were not run. `experiments/` contains no outputs. There is no manuscript, dataset, result table, protocol, limitation statement, license, or coauthor approval under D1 or D2.

The metrology pathway cannot be supported by D1 or D2. Themes that would otherwise be relevant — AI behavior, preference dependence, human judgment, and evaluation reliability — have no local file to define a metric, cite a result, or implement a calculation. No metric is invented here. The Center catalog already displays established measures in this neighborhood, including Kendall’s W as an annotator-agreement measure (fetched catalog text: a normalization of the Friedman statistic for agreement among three or more annotators). That catalog entry is not a local result, and it is not a submission this project can make.

### Ten records required before any YAML could be drafted

These are the ten records named in the 2026-11-18 research-reuse audit. Each is still absent. A missing record blocks reuse. A YAML that asserted a result would be a fabricated record.

1. Manuscript status. A manuscript or note with title, authors, date, version, and a status label written by the authors using one of these words: published, accepted, submitted, preprint, unpublished, or internal.
2. Locator or quotation permission. If published or posted, the stable locator. If unpublished, a sentence that says whether external quotation is permitted.
3. License. A copyright or license notice, and the name of the rights holder.
4. Coauthor approval. A coauthor list and a written decision for each living author whose text would be reused, covering local reanalysis and any later external submission.
5. Confidentiality. A record that says public, embargoed until a stated date, confidential, or restricted by an agreement. If human-subjects or institutional data rules apply, the record needs to name them. Absence of a banner is not clearance to share.
6. Dataset description. For every dataset: filename, row or item count, schema, license, collection method as stated by the authors, and whether the file may leave this machine.
7. Stored result. For every reported result: the table or log that contains the number, the metric definition, the sample size, the model or system identifier, the run date, the baseline, and the control condition.
8. Recomputable protocol. The protocol at the level needed to recompute the printed numbers from stored observations, without a new model call.
9. Author limitation text, kept verbatim.
10. The authors’ own result-versus-hypothesis split. A sentence-level or section-level distinction, written by the authors, between a reported result and a hypothesis. Where the authors do not make that distinction, a later reader marks the sentence “not classifiable” and does not upgrade it.

NIST adds gates those ten records do not satisfy by themselves: one or two references about the metric itself, ideally peer-reviewed or an official NIST resource; an implementation that is usable now and that calculates the metric; a published contact email; and a prohibition on non-public material. The submission file and the review discussion are public.

## Pathway 1 — NIST AI Metrology Center

### Rules re-fetched on 2026-11-19

The 2026-11-18 audit’s rule summary is confirmed, with the corrections and additions below.

Confirmed:

- The Center is a public catalog. The fetched page says inclusion “does not constitute NIST endorsement, validation, or determination of suitability of any listed methodology, metric, or tool.” A listing is not scientific acceptance.
- Submissions are open. A submission is a pull request that adds one YAML file describing a single metric or measurement method. Review is public. `CONTRIBUTING.md` says to fork, add one file under `submissions/`, named in lowercase with hyphens, and open the pull request against `main`.
- Seven keys are required: `schema_version`, `name`, `applied_definition`, `submitter_organizations`, `contact_email`, `references`, `implementation_resources`. The current schema version is `"1.0"`. Everything else is optional.
- Content standards require 1–2 references about the metric itself, not just the general topic; specific and ideally peer-reviewed, or an official NIST resource; not a governance framework such as the AI RMF. Implementation resources must point to something usable today: released software, a published dataset, or code already merged into an open-source repository, not an unmerged or draft pull request. They must support calculating the metric. Every link must be confirmed.
- `known_failure_modes` is optional. The “what to have ready” page says it is the field reviewers most often find empty and most often ask about.
- Non-public material is forbidden. `CONTENT_STANDARDS.md` says “Do not input anything non-public.” The Center page, the format document, the contributing guide, and the how-to-submit page each say not to submit proprietary or confidential information, because the file and the review are public. The contact email is published.
- An LLM review is not approval. The standards say to verify LLM output, confirm every citation, and treat a passing LLM check as not changing the bar. Only the reviewers and the approver decide.
- The readiness map (all checked → likely Accept; a few fixable gaps → likely Revise; missing references, no merged implementation, or out of scope → likely Reject) is explicitly an estimate. The reviewers’ evaluation and the approver’s decision on the pull request determine acceptance.

Corrections and additions relative to the 2026-11-18 audit:

- The “what to have ready” page now says it was “last read 2026-11-19,” not 2026-11-16. The “what reviewers look for” page says the same date and says it is rendered from `CONTENT_STANDARDS.md`. Both pages say that if the page disagrees with the repository, the repository is correct.
- `schema_version` 1.0 is dated 2026-07-23 in the format history. The key was named `format_version` until 2026-08-12. The format document says the rename landed before any submission had been merged, so the version stayed 1.0. The pull-request history below is consistent with that sentence: no metric YAML has been merged at any time.
- Submissions must be in English. That line is in the content standards. A collaborator comment on pull request 11, on 2026-08-26, noted that the English requirement was not yet written down; it is in the file fetched from `main` on 2026-11-19.
- An automated check is described as running on a schedule, with a result expected within an hour, and as covering mechanical details (one file, name, parse, schema). Reviewers are described as turning to a pull request once that check is green. The local command named in the format document is `check-jsonschema` against `validation/schemas/v1.json`. This inspection did not retrieve check-run records.
- Stated human timing, from the contributing guide and “what happens next”: review typically starts within about two weeks of opening. That is first contact, not a decision. If two weeks pass with no response, the submitter may comment as a reminder. Discussion length is described as variable. A first round of comments is described as the normal outcome.
- Acceptance and publication are different events. `CONTRIBUTING.md` says “Acceptance = merge.” Merged submissions “are considered for publication on the AI Metrology Center in a subsequent update.” The Center page says an accepted submission is considered for publication there. Merge is not listing. Listing is not endorsement.
- No fixed submission deadline was found on the pages fetched.

Repository facts fetched from the GitHub API on 2026-11-19:

- `usnistgov/ai-metrology-submissions`, public, default branch `main`.
- Created `2026-06-18T16:51:10Z`.
- `pushed_at` `2026-09-14T16:33:15Z`. That timestamp matches the merge of pull request 11.
- `updated_at` `2026-11-19T12:05:02Z`. The last push is still 2026-09-14.
- Homepage `https://airc.nist.gov/metrology/`.
- The `submissions/` directory on `main` contains one file, `README.md`. The README says accepted metric submissions live there, one YAML per metric or method. There is no YAML file on `main`.

The process has not been replaced, and the repository is not empty of process documents. It is empty of accepted metric files.

### Catalog versus merged submissions

The Center page fetched on 2026-11-19 displays a large catalog, including “Jailbreak Success Rate” and “Toxicity Score.” Those two names are also the titles of example pull requests 5 and 4, which are still open and have `merged_at` null. Pull request 7, a toxicity-score file opened by another user, was closed without a merge after a collaborator wrote that the metric already exists on the main page.

Presence on the Center page is therefore not evidence that a community pull request was merged. This inspection found no community metric YAML on `main` and no merged metric pull request. No submission in this process has moved from “merged” to “considered for publication,” because none has been merged.

The catalog also displays application labels that are not in the allowed list in `SUBMISSION_FORMAT.md` as fetched from `main`. Examples read on the catalog page: “Safety Evaluation” (Jailbreak Success Rate), “Annotator Agreement Evaluation” (Kendall’s W), and “Fairness Evaluation” (a bias/fairness entry in the same region of the page). The format’s allowed `primary_tevv_application` values are: Adversarial Robustness Evaluation, Red Teaming Evaluation Method, Automated Language Model Red Teaming Toolkit, Facial Recognition Benchmark Evaluation, Human-Centered Evaluation, Interpretability & Explanation Evaluation, Language Model Benchmark Evaluation, Object Recognition Benchmark Evaluation, Privacy & Security Evaluation, and Tabular Data Benchmark Evaluation. “Human-Centered Evaluation” is in the schema. The three catalog labels named above are not. That is a difference between the displayed catalog and the current submission vocabulary. It is not, by itself, a false scientific claim, and it is not used as a correction candidate.

### Precedent actually opened

Stages are kept separate. “PR opened” is the `created_at` time. “First human comment” is the earliest issue comment or review by a person in the retrieved timeline. “Changes requested” is used only when the review text says so; the API `state` on those reviews was `COMMENTED`, not a separate changes-requested state. “Merge” is a non-null `merged_at`. “Publication” would be a later appearance on the Center from a merged file. None of the metric pull requests has a merge, so none has a publication step in this process.

#### Merges that exist, and why they are not an acceptance rate

Three pull requests have a merge time. None adds a metric YAML.

| PR | Opened | First human comment | Merge | What it is |
| --- | --- | --- | --- | --- |
| [#12](https://github.com/usnistgov/ai-metrology-submissions/pull/12) | 2026-08-26T00:01:33Z | None retrieved | 2026-08-26T18:43:44Z | Maintainer test (`marionlb`): “test(hostile): cover the annotation path the cases cannot reach.” No review body. |
| [#10](https://github.com/usnistgov/ai-metrology-submissions/pull/10) | 2026-08-23T11:22:35Z | 2026-08-25T23:53:07Z, `marionlb` | 2026-08-26T17:34:33Z | Validation bugfix for Windows console output, by `ppcvote`. Approved by `marionlb` at 2026-08-26T17:33:47Z. Comment “Merged. Thanks!” at 2026-08-26T17:34:44Z. |
| [#11](https://github.com/usnistgov/ai-metrology-submissions/pull/11) | 2026-08-24T21:12:36Z | 2026-08-25T13:33:23Z, `jphall663` | 2026-09-14T16:33:15Z | “Add content standards,” by collaborator `jphall663`. Approvals by `amironesei-dot` (2026-09-14T08:13:41Z) and `marionlb` (2026-09-14T16:29:39Z). |

Pull request 10 is a same-week tooling merge. Pull request 12 is a same-day maintainer test. Neither is evidence about metric acceptance. This report does not infer an acceptance rate from them. Pull request 11 is the standards text itself, merged 21 days after it opened, counting from 2026-08-24 to 2026-09-14.

#### Metric and method pull requests

No row below has a merge time. No row below is a YAML file on `main`. No row below was matched to a new Center listing produced by this process.

| PR | Opened (UTC) | First human contact (UTC) | Later recorded action | State on 2026-11-19 |
| --- | --- | --- | --- | --- |
| [#6](https://github.com/usnistgov/ai-metrology-submissions/pull/6) Detector Gap | 2026-08-04T09:08:31Z | 2026-08-13T00:51:53Z, `marionlb` (process note during what that comment called a settling period) | 2026-08-19T17:52:34Z, `jphall663` review, `COMMENTED`. Opening text: interesting, would like to approve; references are the main issue; the AI RMF is too broad. Submitter replied 2026-08-23. 2026-09-11T13:23:49Z, `jphall663` asked other collaborators to jump in. | Open. Not merged. |
| [#8](https://github.com/usnistgov/ai-metrology-submissions/pull/8) Agent Token Budget Utilization | 2026-08-07T06:49:24Z | 2026-08-13T00:56:47Z, `marionlb` | 2026-08-19T18:14:06Z, `jphall663` review, `COMMENTED`. Opening text: would like to include; needs more work or time; too much explication. Submitter replied 2026-09-01. Further comments 2026-09-11 and 2026-09-13. | Open. Not merged. |
| [#9](https://github.com/usnistgov/ai-metrology-submissions/pull/9) CRUS-T | 2026-08-20T14:14:00Z | 2026-08-25T16:29:34Z, `jphall663` review: “Recommend Revise (Request Changes).” The retrieved review text rates scientific grounding sufficient for the cited working paper and a public implementation, and asks to shorten `applied_definition`. | Submitter replied the same day, 2026-08-25T16:53:06Z, and again 2026-08-26. 2026-09-11T13:25:38Z, `jphall663` asked other collaborators to jump in. No approval was in the retrieved reviews. | Open. Not merged. |
| [#14](https://github.com/usnistgov/ai-metrology-submissions/pull/14) adverse-action reason traceability | 2026-09-04T15:55:53Z | 2026-09-10T19:40:39Z, `jphall663` review: “Recommend Revise (Request Changes).” Opening text rates scientific grounding Partial; references not directly tied to the specific metric. | Submitter replies 2026-09-10 and 2026-09-11. 2026-09-11T12:51:19Z, request for other collaborators. Submitter follow-up 2026-10-20T14:20:03Z. No later review was in the retrieved set. | Open. Not merged. |
| [#15](https://github.com/usnistgov/ai-metrology-submissions/pull/15) Cross-SDK Wire-Level Divergence Rate | 2026-09-07T21:39:09Z | 2026-09-11T12:33:52Z, `jphall663` review: “Recommend Revise (Request Changes).” | Submitter reply 2026-09-13T04:57:53Z. | Open. Not merged. |
| [#16](https://github.com/usnistgov/ai-metrology-submissions/pull/16) Audit-Trail Tamper-Detection Rate | 2026-09-07T21:39:11Z | 2026-09-11T12:46:58Z, `jphall663` review: “Recommend Revise (Request Changes).” | Submitter reply 2026-09-13T07:24:20Z. | Open. Not merged. |
| [#17](https://github.com/usnistgov/ai-metrology-submissions/pull/17) Budget Enforcement Semantics Divergence Rate | 2026-09-07T21:39:13Z | 2026-09-11T13:23:05Z, `jphall663` review: “Recommend Revise (Request Changes).” | Submitter reply 2026-09-13. Submitter follow-up 2026-11-04T01:51:45Z. No later review was in the retrieved set. | Open. Not merged. |
| [#18](https://github.com/usnistgov/ai-metrology-submissions/pull/18) Incomplete-Cross-Section Leakage Screen | 2026-09-11T19:54:09Z | 2026-09-15T18:53:22Z, `jphall663` review: “Recommend Revise (Request Changes).” | Submitter reply 2026-09-16T06:03:26Z. Closed 2026-11-06T21:18:34Z by `MaxWellApexLab`, the author. `merged_at` null. `state_reason` null. No maintainer close comment was in the retrieved comments. | Closed by the submitter. Not merged. Not a recorded maintainer rejection. |
| [#19](https://github.com/usnistgov/ai-metrology-submissions/pull/19) Paired-Control Selectivity Test | 2026-09-14T21:29:36Z | 2026-09-15T19:27:40Z, `jphall663` review: “Recommend Revise (Request Changes).” Grounding rated Partial. The review says the most metric-specific grounding appeared to come from the submitter’s own specification and a newly published implementation, and asks for independent or peer-reviewed support if available. | Submitter reply 2026-09-15T20:45:55Z, stating the exact method is newly proposed, primarily submitter-grounded, and not independently validated. `hbooth` comment 2026-10-09T18:32:42Z, quoted below. | Open. Not merged. The rejection sentence did not close the pull request. |
| [#20](https://github.com/usnistgov/ai-metrology-submissions/pull/20) Tool-Descriptor Mutation Detection Rate | 2026-09-21T13:21:23Z | 2026-09-22T16:05:59Z, `jphall663` review: “Recommend Revise (Request Changes).” | Submitter reply 2026-09-22T16:20:14Z. `jphall663` asked other collaborators to comment at 2026-09-22T16:27:59Z. | Open. Not merged. |
| [#21](https://github.com/usnistgov/ai-metrology-submissions/pull/21) Global Cognitive Audit Engine | 2026-09-30T08:14:22Z | None | None | Open. No comment and no review retrieved. |
| [#22](https://github.com/usnistgov/ai-metrology-submissions/pull/22) Judge Health | 2026-10-07T14:33:35Z | None | None | Open. No comment and no review retrieved. |
| [#23](https://github.com/usnistgov/ai-metrology-submissions/pull/23) Cross-Carrier Non-Measurement Fidelity | 2026-10-09T15:37:52Z | None | None | Open. No comment and no review retrieved. |
| [#24](https://github.com/usnistgov/ai-metrology-submissions/pull/24) Selective Risk at Target Coverage | 2026-10-12T01:04:25Z | None | None | Open. No comment and no review retrieved. |
| [#25](https://github.com/usnistgov/ai-metrology-submissions/pull/25) evidence-currency | 2026-10-15T22:42:04Z | None | None | Open. No comment and no review retrieved. |
| [#26](https://github.com/usnistgov/ai-metrology-submissions/pull/26) ai-inventory-fidelity | 2026-10-15T22:43:56Z | None | None | Open. No comment and no review retrieved. |
| [#27](https://github.com/usnistgov/ai-metrology-submissions/pull/27) incident-driven-guard-coverage | 2026-10-15T22:45:08Z | None | None | Open. No comment and no review retrieved. |
| [#29](https://github.com/usnistgov/ai-metrology-submissions/pull/29) Brier Score | 2026-11-12T00:09:37Z | None | None | Open. Inside the stated two-week first-contact window on the inspection date. |

The `hbooth` comment on pull request 19, 2026-10-09, begins:

> tldr;  
> Rejected and Please Resubmit after we have provided additional clarifications regarding what we are looking for.

The same comment says the submission is difficult to follow and lengthy, and that a human reviewer has to expend a fair amount of effort, including on the code, to understand how to use the metric. The pull request remained open. `merged_at` was null. “Rejected” in that comment is not a merge, not a Center listing, and not a closed pull request.

Pull request 19 is also direct evidence about a newly proposed method. The reviewer treated submitter-authored grounding as partial, asked for independent or peer-reviewed support, and a later collaborator comment told the submitter to resubmit after the project clarifies what it wants. An unpublished local note would not clear that bar. D1 and D2 do not contain even that note.

#### Example and road-test pull requests

| PR | Opened | Closed | Merge | What the record shows |
| --- | --- | --- | --- | --- |
| [#1](https://github.com/usnistgov/ai-metrology-submissions/pull/1) | 2026-06-18T16:59:27Z | 2026-07-22T21:45:04Z | None | “Example PR for a submission,” `marionlb`. No comment and no review retrieved. |
| [#2](https://github.com/usnistgov/ai-metrology-submissions/pull/2) | 2026-07-22T21:43:46Z | 2026-07-22T22:34:14Z | None | Example, Toxicity Score. No comment and no review retrieved. |
| [#3](https://github.com/usnistgov/ai-metrology-submissions/pull/3) | 2026-07-22T21:44:02Z | 2026-07-22T22:34:14Z | None | Example, Jailbreak Success Rate. No comment and no review retrieved. |
| [#4](https://github.com/usnistgov/ai-metrology-submissions/pull/4) | 2026-07-22T22:37:24Z | Still open | None | “[Example] Metric submission: Toxicity Score,” `marionlb`. No comment and no review retrieved. The pulls search listing displayed the label `example-submission`. |
| [#5](https://github.com/usnistgov/ai-metrology-submissions/pull/5) | 2026-07-22T22:37:39Z | Still open | None | “[Example] Metric submission: Jailbreak Success Rate (JSR),” `marionlb`. Same label display. `CONTRIBUTING.md` says two worked examples are kept open. |
| [#7](https://github.com/usnistgov/ai-metrology-submissions/pull/7) | 2026-08-04T17:30:02Z | 2026-08-20T20:10:24Z | None | “Create toxicity-score submission file,” `shaily99`. 2026-08-13, `marionlb` thanked the author for road-testing the process. 2026-08-19, `jphall663` asked whether to close it as another example because the metric exists on the main page. 2026-08-20, `jphall663`: “Closing based on convo with @marionlb.” |

Pull requests 4 and 5 have been open since 2026-07-22 without a retrieved human comment. They are the worked examples, not accepted community submissions. Their names appearing on the Center page does not convert those open pull requests into merges.

#### One non-metric pull request still untouched

[#13](https://github.com/usnistgov/ai-metrology-submissions/pull/13), opened 2026-08-31T19:01:15Z by `ppcvote`, “fix(validation): a non-ASCII path in the diff crashes the check,” was still open on 2026-11-19 with no comment and no review retrieved. It is not a metric. It is further evidence that an open pull request can sit without first contact well past two weeks. It is not used to estimate metric acceptance.

### What the precedent supports, and what it does not

Supported by the dates above:

- A pull request can be opened by anyone with a fork. That step is not review, not acceptance, and not publication.
- On the metric pull requests that did receive a person, first human contact fell between about one day (pull requests 19 and 20) and nine days (pull request 6, first process comment). That range is inside the stated “about two weeks.”
- Pull requests 21 through 27 had no retrieved human contact on 2026-11-19. Pull request 21 had been open since 2026-09-30. The stated two-week expectation is not what those seven pull requests show. This report does not convert that gap into a new expected waiting time. It records the gap.
- The substantive reviews retrieved recommend revision and leave the pull request open. Several of those revisions were followed by a request that another collaborator join, and then by weeks without a retrieved approval.
- The oldest reviewed community metric pull requests, 6, 8, and 9, were still open on 2026-11-19. From 2026-08-04 to 2026-11-19 is more than three months without a merge.
- There is no observed time-to-acceptance for a metric, because no metric pull request has been merged.
- There is no observed time from merge to Center publication for a community metric, because there is no such merge.
- A fast merge occurred for a validation fix and for a maintainer test. Using either as a metric acceptance time would be a mistake.

Not supported:

- An acceptance rate of any kind.
- A claim that a revise recommendation is about to become a merge.
- A claim that a comment saying “rejected” has closed or unpublished a submission. Pull request 19 was still open.
- A claim that a submitter closing their own pull request (18) is a NIST decision.
- A claim that Jailbreak Success Rate or Toxicity Score reached the catalog through a merged community YAML. The example pull requests are unmerged, and the toxicity road-test was closed because the metric was already on the page.

### Metrology timing, if a real submission existed

These clocks are stated by NIST or measured from the pull requests above. They are not a schedule for this project. This project cannot open a valid submission until the ten records, the references, and a public implementation exist.

| Question | Evidence |
| --- | --- |
| Time to produce | Blocked. The how-to-submit page says to allow about 30 minutes plus time to gather citations, and the readiness page says the browser steps take about ten minutes once the answers are in hand. Those sentences assume the metric, the references, and the implementation already exist. They are not a time to create the science. D1 and D2 have no files. |
| Time to first response | Stated: automated check within about an hour; first human contact in about two weeks. Observed first human contact on reviewed metric pull requests: 2026-08-13 (#6, #8), 2026-08-25 (#9), 2026-09-10 (#14), 2026-09-11 (#15, #16, #17), 2026-09-15 (#18, #19), 2026-09-22 (#20). Observed non-response, as of 2026-11-19, on #21–#27. Check-run times were not retrieved. |
| Time to acceptance | No metric merge exists from which to measure it. The August 2026 metric pull requests that received revision requests were still unmerged on 2026-11-19. |
| Fixed deadline | None found. |
| Independently verifiable? | Yes, after the fact, on the public pull request and on https://airc.nist.gov/metrology/. There is nothing to verify now, because no submission should be filed. |
| Realistic by 2026-11-30? | No. The files required to draft a YAML do not exist. Eleven days is also shorter than the stated two weeks to first contact, and first contact is not acceptance. |
| Realistic by 2027-02-15? | Not as acceptance or listing. No observed metric has reached either stage, and reviewed August submissions were still open more than three months later. February 15, 2027 is not a date this record supports. |

**Disposition: DROP.** Do not draft a YAML. Do not open a pull request.

## Pathway 2 — NIST information-quality correction

### Current procedure

Source: https://www.nist.gov/director/nist-information-quality-standards

The HTML modification metadata on the fetched page is `2026-07-08T07:41-04:00` (`article:modified_time` and `dcterms.modified`). `dcterms.date` is `2009-07-31T16:13-04:00`. The page identifies the guidelines as NIST’s mechanism under Section 515 of Public Law 106-554, the OMB guidelines (67 Fed. Reg. 8451, February 22, 2002), OMB memorandum M-19-15 (April 24, 2019), and the Department of Commerce guidelines (67 Fed. Reg. 62,685, October 8, 2002).

The page says the guidelines cover information disseminated by NIST on or after October 1, 2002, regardless of when the information was first disseminated, except that pre-dissemination review procedures apply only to information first disseminated on or after that date.

What the page counts as a qualifying dissemination, in its own categories:

- Dissemination means agency-initiated or agency-sponsored distribution of information to the public. It excludes distribution limited to government employees or contractors or grantees; intra- or inter-agency sharing; responses to records requests; correspondence with individuals; press releases; archival records; public filings; subpoenas; and adjudicative processes.
- Covered corporate or general information includes training materials, catalogs, brochures, fact sheets, website descriptions, annual reports, directories, handbooks, and similar non-scientific material, as listed on the page.
- Covered scientific, financial, and statistical information is described as including Standard Reference Data, Standard Reference Materials, economic impact studies, exhibits, and web sites.
- The same scientific section says it “does not include scientific information disseminated in the form of fundamental research communications.”
- A later exclusion list includes: “Documents not authored by NIST and not intended to represent NIST’s views, including information authored and distributed by NIST grantees, as long as the documents are not disseminated by NIST.”
- The same exclusion list includes: “Scholarly and technical publications, research data, code developed for research purposes, findings, reports, and other materials published or otherwise distributed by employees or by NIST contractors or grantees.”
- Hyperlinks to information that others disseminate are not covered. Opinions, where the presentation makes clear they are not the official view of NIST, are not covered.
- The page also says fundamental research communications are expected to meet information-quality standards and go through the Editorial Review Board, and that they “are not included in the scope of the OMB Guidelines.”

An affected person is “an individual or entity that uses, benefits from, or is harmed by the disseminated information at issue.” The burden of proof is on the requester to show both the necessity and the type of correction sought.

Where an initial request is sent:

> Director, NIST Management and Organization Office  
> National Institute of Standards and Technology  
> 100 Bureau Drive, Mail Stop 3220  
> Gaithersburg, MD 20899-3220  
> Email: info.quality@nist.gov

The page says a misdirected request may be forwarded, and that the response time does not start until the responsible office receives it.

A request is not considered when it does not involve “information,” when the information has not actually been disseminated, or when correction would serve no useful purpose. Duplicative, repetitious, or frivolous requests may be rejected. Those rejections are still accounted for in the Department’s report to OMB.

A proper initial request must include, at minimum:

1. The requester’s name, current home or business address, and telephone number or email address.
2. A statement that the request is submitted under Section 515 of Public Law 106-554.
3. An accurate citation to or description of the information, including the date and source from which the requester obtained it, the point and form of dissemination, the office or program if known, and any other identifying detail.
4. An explanation of how the requester is affected.
5. A specific statement of how the information fails to comply with the applicable guidelines and standards, and why the requester believes the information is not correct.

Clocks written on the page:

- For a proper request, the Director of the NIST Management and Organization Office will attempt to communicate either a decision or a status and an estimated decision date within 60 calendar days after receipt.
- NIST will not take more than 120 days to respond without the concurrence of the requester.
- A request that is missing an element, that comes from a person unaffected by the dissemination, or that does not state a claim, gets no action on the merits. The submitter is notified, usually within 60 calendar days, and may amend and resubmit. The outer 120-day sentence is repeated for a “does not state a claim” determination.
- If a proper request is found to state a claim, the Division Chief investigates and either grants a correction or issues an initial denial. No hearing is provided. Corrective action, if any, may take forms the page lists, including a letter, a press release, a website posting, or withdrawal or correction of the information. The page does not promise a particular form.
- The initial decision or status is communicated usually within 60 calendar days of receipt, again with the 120-day outer bound. An initial denial tells the requester they may appeal.
- An appeal of an initial denial must be made within 30 calendar days of the date of the initial decision, in writing, to the NIST Associate Director for Laboratory Programs, 100 Bureau Drive, Mail Stop 1000, Gaithersburg, MD 20899-1000. It must include the requester’s contact details, a copy of the original request and correspondence about the denial, and a statement of why the denial was in error.
- People involved in the initial denial are not involved in the appeal. The Associate Director communicates the decision usually within 60 calendar days after receipt of the appeal. That decision is a final decision by the Department of Commerce.
- If no appeal is filed within 30 calendar days, the initial denial becomes final.

A request received during the comment period of a proposed rule is treated as a comment on that action, not under this correction clock.

These clocks are for a response. A response may be a status, a finding that the request is not proper, a denial, or a correction. Receipt of a request is not a correction. A denial is not a correction.

### Public log actually on the NIST page

The guidelines page, under “Requests for Correction,” says: “The following requests for correction have been submitted to NIST. The requests and responses are posted here.”

The only year heading in the fetched HTML is 2025. The only matter listed is “Bernstein request for correction,” with four links:

- Initial request: https://www.nist.gov/document/bernstein-2025-initial-request — file path on the page `/system/files/documents/2026/07/08/IQA%20Bernstein%20initial%20request%20final.pdf`
- Initial response: https://www.nist.gov/document/bernstein-2025-initial-response
- Appeal request: https://www.nist.gov/document/bernstein-2025-appeal-request
- Appeal response: https://www.nist.gov/document/bernstein-2025-appeal-response

The four file URLs in the HTML are under `/system/files/documents/2026/07/08/`. No other request, and no other year, is linked from that section of the page fetched on 2026-11-19. This inspection did not find a second NIST page that functions as the current public log.

No separate acknowledgment letter is among the four posted documents. The first NIST document in the posted set is the initial decision.

#### Bernstein chronology

The subject is Table 5 of NIST IR 8545, *Status Report on the Fourth Round of the NIST Post-Quantum Cryptography Standardization Process* (March 2025). The requester, Daniel J. Bernstein, argues that the figure “114 189” overstates Classic McEliece key-generation cost and reflects second-round software rather than fourth-round software. This report does not remeasure that table and does not decide who is right about the cycles. The procedural outcome is what the posted letters record.

| Event | Date in the posted document | What it is |
| --- | --- | --- |
| Initial request emailed to the information-quality address | Wednesday, May 7, 2025, 11:39 AM, as shown on the request | A proper-form request under Section 515. Not a correction. |
| Initial decision, letter from Amy Egan, Acting Director, Management and Organization Office | August 4, 2025 | Denial. Not a correction. |
| Appeal by Bernstein | Dated 2025-08-09 in the appeal document. The January 2026 letter calls the appeal August 9, 2025, and calls it timely. | Appeal of the denial. Five days after August 4, inside the 30-day appeal window. |
| Appeal decision | Letter dated January 16, 2026. Signature block for S. Shyam Sunder, Associate Director for Laboratory Programs, carries a digital-signature timestamp of 2026-01-22 18:24:08 −05:00. | Final denial. The letter says it constitutes the final decision by NIST and the Department of Commerce. Not a correction. |

Elapsed times, counted as calendar days from the earlier date to the later date:

- May 7, 2025 to August 4, 2025: 89 days to the initial denial. The guideline says NIST will attempt to communicate a decision or a status within 60 days, and will not take more than 120 days without the requester’s concurrence. Eighty-nine days is past the “usually 60” sentence and inside 120. The posted file is a decision, not a status letter. This inspection did not see a separate concurrence extending the clock.
- August 9, 2025 to January 16, 2026: 160 days to the appeal letter date. The guideline says the Associate Director will communicate usually within 60 days after receipt of the appeal. The letter says the decision is outside that usual time because of a 43-day lapse in appropriations from October 1, 2025 through November 13, 2025. The letter does not describe the rest of the interval. This report does not invent an explanation for the remainder.

The initial decision’s scope holding, from the cleaner of the two letters:

NIST treats NIST IRs as fundamental research communications. The letter says that, as stated in the NIST Guidelines, fundamental research communications are expected to adhere to information-quality standards and receive Editorial Review Board review, and that they are not included in the scope of the OMB and NIST Guidelines. It also says NIST IR 8545 was approved by the Editorial Review Board on March 5, 2025.

The same letter then says that even if the report were in scope, correction would not be warranted. It says the challenged figure was accurately cited from the Open Quantum Safe benchmark source, that NIST is confident the figures reflect the fourth-round version, that a later website disclaimer does not retroactively invalidate the citation, and that choosing one benchmark source over another is not negligence. It denies the request.

The appeal letter repeats the scope holding as a preliminary matter: a NIST internal report is a fundamental research communication and, as such, NIST IR 8545 is outside the scope of the OMB and NIST Guidelines. It then says the appeal review found the initial point-by-point responses sound, rejects the allegation that Table 5 was incorrect or fabricated, affirms the initial decision, and denies the appeal. It says NIST declines to modify the report.

Distinguish the stages in this one posted case:

- Acknowledgment: no separate acknowledgment document is posted.
- Substantive response: the August 4, 2025 letter, and the January 16, 2026 appeal letter.
- Correction: none. The report was not modified by this process, on the letters’ own statement.
- Denial: both the initial decision and the appeal.

One posted case is not a rate. It is the entire current log. It shows that a detailed, timely, written request about a numbered table in a NIST IR can end in a final denial, with the agency’s first stated ground being that a NIST IR is outside the guidelines.

#### A denial letter that is not on the current log

The current NIST log does not link the 2020 World Trade Center correspondence. A third-party PDF was opened because search results surfaced it. It is a letter responding to an April 15, 2020 request about NIST NCSTAR 1A and NIST NCSTAR 1-9 and the NIST WTC 7 FAQ page. The letter says the request is denied. The signature block reads Catherine Fletcher, digitally signed 2020-08-28 16:34:00 −04:00. From April 15, 2020 to August 28, 2020 is 135 days, ending in a denial. That PDF is not treated as an entry on the NIST log, and the underlying engineering dispute is not reopened here. It is recorded only so that an older denial is not silently upgraded into a correction, and so that it is not mistaken for a document the current guidelines page still posts.

### No information-quality candidate

This inspection did not find a demonstrable factual error in a dissemination that the guidelines cover.

Considered and rejected:

- NIST IR 8545 Table 5 is already the subject of a final denial. The agency’s letters say a NIST IR is outside the guidelines. This inspection did not independently remeasure the table. A further request on the same point would be the sort of duplicative request the guidelines say may be rejected. No request is drafted.
- NIST AI technical reports and journal articles by NIST authors fall under the exclusion the guidelines state for scholarly and technical publications and for fundamental research communications, unless a specific document can be shown to be a covered dissemination rather than that class. No such showing was made. A disagreement with a research conclusion is not a candidate.
- The Metrology Center page uses “SI” without defining it in the paragraphs that were read. The 2026-11-18 audit already recorded that the abbreviation is undefined there. An undefined abbreviation is not a demonstrated false statement of fact. It is not a correction candidate.
- Differences between catalog display labels and the current YAML vocabulary are a process mismatch, not a shown scientific error.
- No sentence in D1 or D2 contradicts a NIST publication, because D1 and D2 contain no sentences.

**Disposition: DROP.** No correction request is drafted.

### Information-quality timing, for a request this project is not filing

| Question | Evidence |
| --- | --- |
| Time to produce | Not estimable as a filing. No eligible error was identified, so there is nothing to write. |
| Time to first response | In the only case on the current log, the first posted NIST document is the initial decision, not a separate acknowledgment. May 7, 2025 to August 4, 2025: 89 days. The written target is 60 days for a decision or a status, with an outer bound of 120 days absent concurrence. |
| Time to a correction | The posted case ended in a denial, affirmed on appeal. The appeal letter date is 160 days after August 9, 2025. A correction was not the outcome. The 2020 third-party letter, which is not on the current log, is also a denial, 135 days after the request date it cites. |
| Fixed deadline | None for filing. The 30-day appeal window runs only after an initial denial. |
| Independently verifiable? | The guidelines page and the four posted PDFs are public. A future correction would be verifiable only if NIST posted a changed document or a decision saying the information was corrected. A mailed receipt would not be that. |
| Realistic by 2026-11-30? | No. There is no request to send. A request sent on 2026-11-19 would not reach the 60-day mark until 2027-01-18. |
| Realistic by 2027-02-15? | Not as a correction. February 15, 2027 is 88 days after 2026-11-19, which is after the 60-day target and before the 120-day outer bound for an initial response. The only fully posted NIST case shows that an initial response can be a denial, and that the appeal ran far past 60 days. A response by mid-February is not a correction. |

## Candidates

None. The maximum of three was not filled.

| ID | Pathway | Why it does not survive |
| --- | --- | --- |
| — | Metrology | No defined metric, no reference about that metric, no implementation that calculates it, and no D1 or D2 file. |
| — | Information quality | No demonstrable error in a dissemination the current guidelines cover. |

No public draft was written. A metrology YAML without references and an implementation would not be a draft. `execution/phase1/drafts/` was not created.

## DROP register

1. **New metrology metric drawn from D1 or D2** (AI behavior, preference dependence, human judgment, or evaluation reliability). DROP. Both directories are empty, E-1 through E-3 were not run, and a YAML would assert results and an implementation that do not exist. Precedent on pull request 19 also shows a newly proposed, submitter-grounded method being told to resubmit.
2. **Information-quality request on NIST IR 8545 Table 5.** DROP. The posted process already ended in a final denial (letter dated 2026-01-16, signature timestamp 2026-01-22). NIST’s stated ground includes that a NIST IR is outside the guidelines. The table was not remeasured here. No second request is drafted.
3. **Information-quality request about the Metrology Center page** (undefined “SI,” catalog labels that the YAML schema does not offer, or the non-endorsement sentence). DROP. These are wording and process facts, not a demonstrated false statement in a qualifying dissemination.

## What this report does not claim

- It does not claim a metric acceptance rate, a typical time to merge, or a typical time to appear on the Center.
- It does not claim that any open pull request will be merged or closed.
- It does not claim that the Bernstein denial settles the cycle-count dispute. It records the agency’s decision and the scope ground the letters state.
- It does not claim the 2020 third-party PDF is posted on the current NIST log.
- It does not claim that check suites passed or failed on any pull request.
- It does not claim that issue number 28 was inspected.
- It does not claim that files outside `research/D1/` and `research/D2/` were searched for usable research. They were not treated as D1 or D2.
- It does not authorize a pull request, an email to `info.quality@nist.gov`, or any other external submission.

## Parent return

- File: `execution/phase1/NIST.md`
- D1 and D2 contain files: no. Both directories exist, modification time `2026-11-18T13:42:59`, zero files.
- Candidates that survived: 0.
- DROP 1: no D1/D2 files, so no metrology YAML.
- DROP 2: NIST IR 8545 already has a final information-quality denial, and was not remeasured.
- DROP 3: Metrology Center wording is not a demonstrated qualifying error.
- Precedent dates actually seen: metric first-contact dates 2026-08-13, 2026-08-19, 2026-08-25, 2026-09-10, 2026-09-11, 2026-09-15, 2026-09-22; pull request 19 “Rejected and Please Resubmit” comment 2026-10-09 while the pull request stayed open; pull request 18 closed by its author 2026-11-06 without a merge; tooling merges 2026-08-26 (pull requests 10 and 12) and 2026-09-14 (pull request 11); no metric merge. Information-quality dates: request 2025-05-07, initial denial 2025-08-04, appeal 2025-08-09, appeal letter 2026-01-16, signature timestamp 2026-01-22. Off-log third-party denial signature 2020-08-28, citing a request of 2020-04-15.
