# Research-reuse audit

Audit directory: `audits/research-reuse/`
Date of inspection: 2026-11-18
Workspace context: `PROJECT_CONTEXT.md`, which states that the workspace was initialized locally on 2026-11-18, that no audits had been started, that no repositories had been cloned, and that no external submissions existed.

## Decision

`research/D1/` and `research/D2/` contain no manuscripts, datasets, experimental results, protocols, limitation statements, licenses, author lists, or confidentiality records. No finding from either track can be translated into OWASP guidance, a W3C concept, a NIST metrology submission, or a university policy. No result in this workspace is an established empirical result, and no sentence in this workspace is an untested hypothesis from those tracks, because neither class of text is present.

Nothing from D1 or D2 should be released, uploaded, cited as published, or placed in an external issue or pull request. No candidate below is ready for `MASTER_TRACKER.md`. This audit does not add a tracker row. No model inference was run, and no paid API call was made.

## Method

The inspection stayed in this workspace except for ordinary reading of public web pages. It did not clone upstream standards repositories, did not copy pages into `references/`, and did not write experiment outputs.

Local checks, all on 2026-11-18:

- A recursive walk of `research/D1/`, `research/D2/`, `research/incident-evidence/`, `audits/research-reuse/`, `experiments/`, `references/`, `contributions/`, and `evidence/`. Each directory existed. Each contained zero files and zero subdirectories. `research/D1/` and `research/D2/` had modification time `2026-11-18T13:42:59` local time and mode `0755`.
- `git status` showed only untracked `PROJECT_CONTEXT.md` and `MASTER_TRACKER.md`. `git log` could not run because `main` has no commits. `git ls-remote --heads origin` returned no heads.
- The GitHub API for `thomasLiu963/ai-governance-initiative` returned: repository created `2026-11-18T21:32:47Z`, `pushedAt` `2026-11-18T21:32:49Z`, `diskUsage` 0, `isPrivate` false, URL `https://github.com/thomasLiu963/ai-governance-initiative`. The contents API returned HTTP 404 with the message "This repository is empty."

Public pages opened for the receiving-document section are listed under that section. A page that was not opened is marked as not read. Search snippets were not used as sources once a primary page had been fetched. One search summary described the AI Testing Guide license as CC BY-NC-SA 4.0; the fetched `LICENSE.md` on `main` says CC BY-SA 4.0, and this audit uses the fetched file.

`research/incident-evidence/` was counted because it sits beside D1 and D2. It is also empty. It is outside the translation task and supplies no incidents.

## Inventory

A reusable research record would be a regular file under `research/D1/` or `research/D2/` with a nonzero size. The walk found none. The counts below are workspace measurements. They are not measurements of a model.

| Artifact class | D1 | D2 | What the empty cell means |
| --- | --- | --- | --- |
| Manuscript, preprint, or internal note | 0 files | 0 files | No title, authors, date, version, venue, or claim text |
| Dataset or data dictionary | 0 files | 0 files | No rows, schema, access condition, or checksum |
| Experimental result table, figure, log, or metric output | 0 files | 0 files | No point estimate, interval, sample size, model identifier, or date of a run |
| Protocol or methods write-up | 0 files | 0 files | No population, assignment, control, baseline, metric, or stopping rule |
| Limitation statement written by the authors | 0 files | 0 files | No author-stated bound on a claim |
| Publication record | 0 files | 0 files | No DOI, venue, preprint server, or "unpublished" label |
| License or copyright notice | 0 files | 0 files | No permission to copy, adapt, or cite |
| Coauthor or approval record | 0 files | 0 files | No person has authorized reuse or external submission |
| Confidentiality, embargo, IRB, or data-use record | 0 files | 0 files | No sharing rule is stated |

`experiments/`, `references/`, `contributions/`, and `evidence/` were also empty. There is no local citation library and no proof of review or submission.

### Exact files needed before any translation

Place material only under the track it belongs to. A file that exists somewhere else on disk was not inspected and is not part of this inventory. For each track that is supposed to contribute, the following records are needed. A missing record blocks reuse of that track.

1. A manuscript or note, with title, authors, date, version, and a status label that uses one of these words as written by the authors: published, accepted, submitted, preprint, unpublished, or internal.
2. If published or posted, the stable locator. If unpublished, a sentence that says whether external quotation is permitted.
3. A copyright or license notice, and the name of the rights holder.
4. A coauthor list and a written decision for each living author whose text would be reused, covering local reanalysis and any later external submission.
5. A confidentiality record: public, embargoed until a stated date, confidential, or restricted by an agreement. If human-subjects or institutional data rules apply, the record needs to name them. Absence of a banner is not a clearance to share.
6. For every dataset: filename, row or item count, schema, license, collection method as stated by the authors, and whether the file may leave this machine.
7. For every reported result: the table or log that contains the number, the metric definition, the sample size, the model or system identifier, the run date, the baseline, and the control condition.
8. The protocol at the level needed to recompute the printed numbers from stored observations, without a new model call.
9. The authors' limitation text, kept verbatim.
10. A sentence-level or section-level distinction, written by the authors, between a reported result and a hypothesis. Where the authors do not make that distinction, the later reader marks the sentence "not classifiable" and does not upgrade it.

Until those records exist, D1 and D2 have no established results and no documented hypotheses.

## Established results and untested hypotheses

| Class | Count | Identifiers |
| --- | --- | --- |
| Established result: a number or qualitative outcome tied to a stored table, protocol, and author-stated limitation | 0 | none |
| Untested hypothesis: a proposed mechanism, effect, or safeguard the authors label as untested | 0 | none |
| Not classifiable | 0 | none; there is no prose to classify |

No work can be reused without new model inference, because no work is present. The reanalysis design later in this file is the path that would avoid new inference if a result table arrives. That design was not executed.

## Release, license, coauthors, and confidentiality

This audit recommends no release.

| Constraint | Record found | Consequence |
| --- | --- | --- |
| Publication status | No manuscript | No sentence may be cited as a published finding |
| License | No notice on D1 or D2 | No right to post, adapt, or donate the text is recorded |
| Coauthors | No names and no approvals | A later external use would risk attributing work to people who have not agreed, or omitting people who should be asked |
| Confidentiality | No marking and no data-use agreement | Lack of a label does not make a future file public |
| Workspace remote | Public GitHub repository, empty, no commits | Pushing research files there would publish them. This audit does not push |

`PROJECT_CONTEXT.md` already forbids sending unpublished research files or sensitive information to third-party services without explicit approval, and forbids external issues, pull requests, and submissions without approval of that specific action. Those rules are unmet for any future D1 or D2 file until the records above exist and Thomas approves the specific action.

The NIST submission pages add a separate public-disclosure rule, quoted in the NIST section: submission files and review discussion are public, and non-public material is not to be put into that process. The W3C AI Content Disclosure charter requires a Community Contributor License Agreement for substantive specification contributions. Those gates are additional reasons to keep future unpublished files local. They are not satisfied by this audit.

## How a real finding would have to map

The notes below describe the evidence each public document asks for. They do not identify a gap in any document. A gap would require a quoted passage and a local result that contradicts or completes it. Neither is available. Sibling audit directories own the line-by-line reviews of those documents. This file does not write in those directories.

Themes used below are the workspace themes: human agency, AI reliability, transparency, privacy, authorization, and human oversight.

### OWASP AI Exchange

- Locator read: `https://owaspai.org/contribute/` and the source `https://raw.githubusercontent.com/OWASP/www-project-ai-security-and-privacy-guide/main/content/ai_exchange/content/contribute.md`, opened 2026-11-18. A PDF rendering, `https://owaspai.org/OWASP-AI-Exchange.pdf`, states "Generated from owaspai.org on: 11/16/2026". The about section of that rendering was read. The threats, controls, and references were not reviewed for errors.
- Document status: living OWASP Flagship community guidance. The same rendering says the project was awarded Flagship status in March 2025. It is not an ISO or W3C standard. The rendering says it is edited through the GitHub repository `OWASP/www-project-ai-security-and-privacy-guide`.
- License of the Exchange, from that rendering: "OWASP AI Exchange by The AI security community is marked with CC0 1.0 meaning you can use any part freely without copyright and without attribution." CC0 applies to the Exchange text. It does not license unpublished D1 or D2 material, and it does not allow this project to donate unpublished material into the Exchange.
- Contribution policy read: consider the roadmap; do not advertise commercial tools, companies, or individuals; disclose affiliation when referencing one's own tools or articles; write so a non-specialist can use the principle and find further detail.
- AI-assistance policy read: material AI assistance must be labeled, including that AI was used and what it did and to what extent.
- Roadmap: the contribute page says the roadmap leads prioritization. The roadmap document itself was not opened, so no topic is recorded as in or out of the roadmap.
- Translation rule for this project: a D1 or D2 result could be cited from the Exchange only after it is already published, the citation is copied accurately, affiliation is disclosed, and the added text states the authors' limitation. An unpublished result, a hypothesis, or a synthetic exercise cannot be written as practitioner guidance. No such citation is proposed.

### OWASP AI Testing Guide

- Locators read: `https://owasp.org/projects/ai-testing-guide`; `https://raw.githubusercontent.com/OWASP/www-project-ai-testing-guide/main/README.md`; `https://raw.githubusercontent.com/OWASP/www-project-ai-testing-guide/main/LICENSE.md`; the table of contents at `https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/README.md` as returned by search and confirmed as a GitHub path. Individual test procedures were not adopted and are not reproduced here.
- Document status: the project page says "26 November 2025 — Version 1 Published" and describes v1 as a community-driven standard for trustworthiness testing. The v1 PDF was not opened, so this audit does not confirm a status block inside the PDF. For this workspace, the accurate label is OWASP community guidance whose project page announces a v1 publication on that date.
- License read on `main`: "OWASP AI Testing Guide is published under the CC BY-SA 4.0 license."
- Contribution path read: the README directs collaboration to the project leaders named on that page, Matteo Meucci and Marco Morana. A separate contribution-policy file and a separate AI-assistance policy were not found in the README or `LICENSE.md`. They are not verified for the rest of the repository.
- Scope read from the project index: the guide describes methodology and repeatable test cases across application, model, infrastructure, and data layers. The table of contents lists test identifiers such as `AITG-APP-01` through `AITG-DAT-05`. This audit did not check whether any identifier's procedure matches a local protocol, because no local protocol exists.
- Translation rule: a local protocol could become a methodology note only if it already states the test objective, controls, baseline, oracle, and limitation, and only if that note is a clarification of a specific section a reviewer can open. This audit does not draft that note and does not supply test steps.

### OWASP AISVS

- Locators read: `https://raw.githubusercontent.com/OWASP/AISVS/main/README.md` and `https://raw.githubusercontent.com/OWASP/AISVS/main/CONTRIBUTING.md`. Requirement bodies under `1.01/en/` and `1.02-dev/` were not read. No requirement is quoted as wrong or missing.
- Document status: community verification catalogue. The README identifies AISVS 1.01 as the latest stable release, with PDF and Markdown under `1.01/`, and identifies `1.02-dev/` as the only active development line. `1.0/` and `1.01/` are locked. Version 2.0 is deferred. This is not an ISO or W3C standard. A release date for 1.01 was not on the pages read.
- License read: Creative Commons Attribution-ShareAlike 4.0 International.
- Contribution policy read: open an issue before a pull request when a change would alter meaning, level, numbering, or scope. New work targets `1.02-dev/`. Preserve existing numbering and chapter objectives. Append identifiers; do not reuse retired ones. A proposed requirement must be concrete and independently testable. `RELEASE.md` is named as the release policy and was not opened.
- AI-assistance policy read: AI tools may help draft, and the contributor must own the security judgment. The policy rejects unreviewed generated text, padded prose, generic boilerplate, and review comments that add no security judgment. Controls must remain independently verifiable.
- Structure read from the README, without checking the control text: twelve chapters, from training-data integrity through monitoring and logging, plus three appendices. Verification levels are 1, 2, and 3, with the README's descriptions of when each is used. Requirement identifiers have the form `C<chapter>.<section>.<requirement>`, and versioned references use a lowercase `v`, for example `v1.0-C9.4.3`. The README gives one example sentence for `C9.4.3` as of version 1.0: "Verify that agent identity credentials rotate on a defined schedule." That sentence was not checked against the 1.01 text.
- Translation rule: the only reuse that matches this standard is an evidence statement an auditor could check. A local limitation could later be compared with one requirement after that requirement's current 1.02-dev text is read. No new requirement is drafted here.

### W3C AI transparency and privacy concepts

Two public bodies were read. Global Privacy Control was not read. No mapping to GPC is made.

**AI Content Disclosure for HTML**

- Locator read: `https://www.w3.org/community/reports/ai-content-disclosure/CG-FINAL-ai-content-disclosure-20261009/`. Charter read: `https://raw.githubusercontent.com/w3c-cg/ai-content-disclosure/main/charter.md`, last modified 2026-09-21, start date 2026-02-03.
- Document status, from the report: Final Community Group Report, 09 October 2026. "It is not a W3C Standard nor is it on the W3C Standards Track." The report says publication does not add the attributes to the HTML Living Standard.
- Values read in the report: `human-only`, `ai-assisted`, and `ai-autonomous`, chosen by whether generative AI was involved and whether a human reviewed the content before publication. The report says `ai-assisted` asserts that human review occurred and does not identify the reviewer, record sign-off, or establish editorial responsibility. Detection, verification, and quantitative authorship percentages are outside the report's stated scope.
- Contribution mechanics, from the charter: substantive contributions to specifications require a participant who has agreed to the W3C Community Contributor License Agreement. Specifications use the W3C Software and Document License. Technical discussion is public.
- Draft W3C process note read separately: `https://www.w3.org/2026/10/draft-ai-policy.html`. Its own status line says it is a draft for discussion and is not yet a W3C policy. It says a human contributor remains responsible, and that substance generated by an AI tool is labeled.
- Translation rule: D1 or D2 text could be labeled with one of the three existing values only after the authors state whether generative AI was involved and whether a human reviewed the specific text before publication. Those facts are not in the workspace. This audit does not propose a new disclosure value. The report's own scope excludes detection research, so a detection experiment would not become a change to this report even if results existed.

**Data Privacy Vocabulary**

- Locators read: `https://w3c-cg.github.io/dpv/` and `https://github.com/w3c/dpv/wiki/Contribution-Guide`. The guide page is dated 12 February 2026 on the fetched view.
- Document status: the homepage identifies DPV version 2.3, dated 25 February 2026, with specifications at `https://w3id.org/dpv`. It also says the website was last updated 28 January 2026. This audit does not resolve that date order and does not claim W3C Recommendation status. The homepage lists an AI extension among general-purpose extensions. That extension's term list was not opened, so no term is recorded as present or missing.
- License, from the homepage: W3C Software and Document License, 2023 version.
- Contribution policy read: discuss proposals before a pull request; decisions go through the DPVCG; do not edit `master` by default; do not hand-edit generated HTML or RDF; do not treat CSV exports as the source of a change. For a large or non-authoritative contribution, the guide asks whether the work is open rather than proprietary, why it belongs in DPV, how it relates to existing work, and who will maintain it.
- AI-assistance policy: not stated on the contribution guide. The separate draft W3C policy above is not yet a W3C policy. Treat AI-assistance expectations for DPV as not verified.
- Translation rule: a future data-flow description could be bound to existing DPV concepts only after the manuscript states purpose, data categories, operations, parties, and measures in words precise enough to point at a term that has been opened. No data-flow description is present. No new term is proposed. Proprietary or unpublished text would fail the guide's question "Is it open?"

### NIST AI Metrology Center

- Locators read: `https://airc.nist.gov/metrology/`; `https://airc.nist.gov/metrology/how-to-submit/what-to-have-ready/`, which says it was built from the submission format and "last read 2026-11-16"; `https://raw.githubusercontent.com/usnistgov/ai-metrology-submissions/main/CONTENT_STANDARDS.md`.
- Wording on the Center page: it describes resources "within the SI Resource Center (AIRC)" for "trustworthy SI", and it also invites "Submissions of AI metrics and measurement methodologies." The paragraphs read do not define the abbreviation SI. This audit does not expand it.
- Document status: a NIST resource center and a public submission process for metrics and measurement methods. The Center page says inclusion "does not constitute NIST endorsement, validation, or determination of suitability of any listed methodology, metric, or tool." Listing would not be acceptance of a scientific claim.
- Submission rules read: one YAML file per metric or method, submitted as a public pull request. Required fields include `schema_version`, `name`, `applied_definition`, `submitter_organizations`, `contact_email`, `references`, and `implementation_resources`. The content standards require one or two references about the metric itself, ideally peer-reviewed or an official NIST resource, and not merely a governance framework. Implementation resources must be usable now: released software, a published dataset, or code already merged, and must support calculating the metric. `known_failure_modes` is optional and is described as the field reviewers often ask about. The standards say missing references, no merged implementation, or an out-of-scope metric is the pattern most likely to be rejected.
- Confidentiality rule read on the content-standards page: "Do not input anything non-public." The Center page says not to submit proprietary or confidential information because the submission and the review are publicly visible.
- AI-assistance rule read there: an LLM review is not a substitute for a manual check; citations must be confirmed; a passing LLM check is not approval.
- Translation rule: D1 or D2 could support a submission only if they already contain a defined metric, peer-reviewed references about that metric, a public implementation that calculates it, stated failure modes, and a license. None of those items exist. A local simulation cannot be offered as the implementation or as the empirical reference. No YAML file is created.

### University AI accountability policies

The workspace names no university, no campus policy, no policy version, and no approval authority. No policy page was selected, because choosing an institution would invent the target.

A later clause would need, at minimum: the institution's name; the policy title, version, and stable locator; the current sentence to be changed; the office that can adopt a change; and the research-data rules that cover D1 and D2. The clause would also need a concrete link to at least one workspace theme. Typical accountability content, once a real policy is open, would name the human who remains responsible, what that person can inspect, how a consequential automated action is stopped, what data are retained, and which permission authorizes the action. No clause text is drafted here.

## Conditional contribution designs

These five designs are narrow on purpose. Each is blocked. None has a confirmed gap in a source, none has local evidence, and none is a tracker candidate. External submission is `none`.

### RR-1 — Local intake manifest

- Target: this workspace, before any external citation. Not a change to a standards body.
- Themes: transparency, AI reliability.
- Blocker: there are no research files to register.
- Reuse without new inference: the manifest records files already on disk. It does not call a model.
- When files exist, one row per file would hold path, SHA-256, byte size, track (`D1` or `D2`), artifact class, publication status, license, confidentiality label, authors, approval status, and whether the file may leave the machine.
- Evaluation: a file with any empty license, confidentiality, or publication field is ineligible for citation. A hypothesis row cannot be copied into a standards draft as a result.
- Expected artifact, later: `audits/research-reuse/` manifest table. Not created, because the inventory is the empty table above.
- Limitation: a manifest does not check scientific validity.

### RR-2 — Reanalysis of a stored result, then a possible metrology or testing note

- Target, only after the reanalysis exists and is itself citable: either a NIST Metrology Center method submission or a scoped note to one AI Testing Guide section. The choice waits on the metric the authors actually defined.
- Themes: AI reliability, transparency.
- Blocker: no result table, metric definition, baseline, or peer-reviewed source.
- Reuse without new inference: yes, if raw observations or sufficient statistics are already stored. A new model call is out of this design.
- Experiment: E-1 below. It was not run.
- What would be proposed externally, and only later: the authors' definition, the recomputed comparison to their printed number, the authors' limitations, and a public implementation that calculates the same definition. NIST's required references and implementation link would still have to exist. The AI Testing Guide path would additionally require a specific section and the project leaders' contribution route.
- Limitation: matching a printed number does not show that the original study was well controlled. A mismatch is a discrepancy in stored arithmetic, not a new measurement of a deployed model.

### RR-3 — Author-stated limitation compared with one AISVS requirement

- Target: one requirement in `1.02-dev`, after that requirement is read. No identifier is selected now.
- Themes: AI reliability, human oversight. Authorization or privacy only if the limitation the authors wrote is about permission or data.
- Blocker: no author-stated limitation, and no requirement body was reviewed for a defect.
- Reuse without new inference: the comparison uses the authors' text and the requirement text. It does not generate attacks or run a model.
- Work when unblocked: quote the requirement, quote the limitation, and state whether an auditor could verify the limitation with one piece of evidence. If the requirement is already testable, stop. If a wording defect is visible in the requirement itself, the AISVS route is an issue before any pull request.
- Expected artifact, later: a two-column worksheet in this directory. No new control sentence is pre-written.
- Limitation: a research limitation is not automatically a missing control.

### RR-4 — Bind an author-written data or authorship statement to existing W3C concepts

- Target: existing DPV terms, after the relevant term definitions are opened, and the three existing `ai-disclosure` values. No new term and no new disclosure value.
- Themes: transparency, privacy, human oversight.
- Blocker: no manuscript states purposes, data categories, parties, measures, AI involvement, or human review.
- Reuse without new inference: this is a document binding. It does not detect AI use and does not call a model. That matches the disclosure report's statement that detection is out of scope.
- Evaluation: every binding cites the manuscript sentence and the opened term or value. A sentence that does not say whether a human reviewed the text stays unlabeled. Proprietary text is not submitted to DPVCG.
- Expected artifact, later: a local binding table. An external issue only if an opened DPV definition cannot express a distinction the authors actually made, and only after the contribution guide's openness questions are satisfied.
- Limitation: `ai-assisted` does not prove reviewer competence or editorial responsibility. A DPV binding does not prove legal compliance.

### RR-5 — One accountability clause for a named university policy

- Target: unnamed. No institution is specified in `PROJECT_CONTEXT.md`, `MASTER_TRACKER.md`, or the research directories.
- Themes: whichever of human agency, authorization, and human oversight the opened policy actually governs.
- Blocker: no policy text, no responsible office, and no local research practice to attach the clause to.
- Reuse without new inference: policy drafting from existing research descriptions and the current policy sentence. No model evaluation.
- Gate: read the current clause, record its locator and version, and propose one replacement or addition that a reviewer can diff. Include who may approve an automated action, what record they can inspect, and how they stop it.
- Expected artifact, later: a redline against the fetched policy. Not started.
- Limitation: a clause this project drafts has no force until the institution adopts it. Adoption is not claimed.

## Experiments

E-0 was run. E-1, E-2, and E-3 are specified and were not run. No synthetic series was generated. No output under `experiments/` was written; `PROJECT_CONTEXT.md` reserves that directory for raw outputs, and there are none.

### E-0 — Filesystem inventory (executed)

- Question: do D1 and D2 contain any reusable research file?
- Population: the two track directories after the workspace initialization on 2026-11-18.
- Control: the same walk was applied to both directories and to the neighboring empty directories listed in the method.
- Baseline: `PROJECT_CONTEXT.md` says the directories exist and that audits had not started. It does not claim that research files were loaded.
- Procedure: recursive directory walk, recording entry count, size, and modification time. No hasher output exists because there were no files.
- Criterion: one or more regular files with nonzero size would count as present material. Classification of scientific claims would still require the file contents.
- Observed result: zero entries in each track. Modification time of both directories: `2026-11-18T13:42:59` local.
- This result measures the workspace. It does not measure a model, a dataset, or a safeguard.
- Limitation: the walk does not see files stored outside these directories, unmounted volumes, or a remote that later gains commits. The GitHub contents check covers only the configured `origin` at the time of the call, and that repository was empty.

### E-1 — Numerical reanalysis (not executed)

- Purpose: recompute a printed result from stored observations or sufficient statistics.
- Inputs required: a frozen results file, its SHA-256, the authors' metric formula, the authors' printed number, the authors' sample size, and any tolerance or rounding rule they state.
- Test cases:
  1. Recompute the point estimate from the stored observations with the authors' formula.
  2. If an interval is printed and the formula and inputs are both present, recompute the interval.
  3. Compare the row count with the sample size stated in the prose.
- Controls: the source file is read-only. A second local implementation of the same formula is allowed only with local software. No model API, no new labels, and no substitution of a different metric.
- Baseline: the number printed by the authors, quoted with its table location. The baseline is not "improved."
- Evaluation: if the authors state a rounding rule, agreement is judged only against that rule. If they state no tolerance, the output says "tolerance absent" and does not invent one. A mismatch is recorded as a discrepancy between the prose and the stored arithmetic.
- Limitations: agreement does not validate sampling, assignment, or model behavior. Disagreement does not establish a new empirical measurement. Missing inputs stop the experiment.
- Expected artifact, if it is ever run: a local note with input checksums, formula, recomputed values, and the sentence "This is a recalculation of stored numbers, not a measurement of a model."
- Status: not run. Inputs are absent, so there is no recomputed value.

### E-2 — Protocol completeness review (not executed)

- Purpose: decide whether a stored protocol is sufficient for E-1 or for a later testing note.
- Inputs required: one protocol file.
- Test cases: score only these fields, and only from sentences in the file: population, assignment to conditions, control condition, baseline system, metric, stopping rule, limitation.
- Controls: a field that is not written is scored absent. Context from other papers is not filled in. No model judges the protocol.
- Baseline: the protocol's own methods section, when a methods section exists.
- Evaluation: each field is `present`, `ambiguous`, or `absent`. There is no pass rate that implies a system was tested.
- Limitations: a complete write-up can still describe a weak study. Completeness is not effectiveness.
- Expected artifact: a seven-row checklist citing line locations.
- Status: not run.

### E-3 — Separate results, hypotheses, and limitations (not executed)

- Purpose: keep later standards text from promoting a hypothesis into a result.
- Inputs required: one frozen manuscript.
- Test cases: label each results-bearing sentence as `reported result`, `hypothesis`, `limitation`, or `not classifiable`. A reported result must point at a table, figure, or log in the same bundle.
- Controls: two independent readings of the same frozen text. Disagreement remains disagreement and is not averaged away. A model is not used as a judge, because that would be new inference and would mix this audit with a model measurement.
- Baseline: headings the authors used, such as results, discussion, or future work, when those headings exist.
- Evaluation: every numeral in a results section either cites a stored table or is marked "number without a table."
- Limitations: the labels describe the manuscript's support for its own sentences. They are not replication.
- Expected artifact: a local labeled list. It would not be published while the manuscript is unpublished or confidentiality is unresolved.
- Status: not run.

## Readiness against the contribution bar

`MASTER_TRACKER.md` requires an exact source, a document status, a checked contribution policy, a checked AI-assistance policy, a gap a reviewer can confirm, the themes, the proposed text, implementation requirements, and what was not verified. External submission needs a separate approval.

| Design | Source opened | Gap confirmed in that source | Local evidence | Tracker status |
| --- | --- | --- | --- | --- |
| RR-1 | Workspace rules only | No external gap | Empty directories | Do not add |
| RR-2 | NIST submission rules; AI Testing Guide status pages | No | No metric | Do not add |
| RR-3 | AISVS README and CONTRIBUTING | No requirement defect shown | No limitation text | Do not add |
| RR-4 | Disclosure report and DPV contribution guide | No missing term shown | No data-flow or review statement | Do not add |
| RR-5 | No university policy | No | No institution | Do not add |

## What was not verified

- Scientific content of D1 or D2. There is no content.
- Files that may exist outside `research/D1/` and `research/D2/`. They were not searched for, and they are not inventoried.
- Whether a later commit appears on `origin`.
- The OWASP AI Exchange roadmap, and any technical error in the Exchange.
- The AI Testing Guide v1 PDF, its test procedures, and any AI-assistance rule outside `README.md` and `LICENSE.md`.
- AISVS `RELEASE.md` and the requirement text of 1.01 and 1.02-dev.
- The DPV AI extension and the other DPV modules.
- W3C Global Privacy Control.
- The meaning of the abbreviation SI on the NIST Metrology Center page.
- Any university policy.
- Legal effect of the EU AI Act, the W3C Community Contributor License Agreement, CC0, or CC BY-SA. The licenses are recorded as stated by the pages read, not as legal advice.
- Acceptance of any contribution. No submission was made.

## Assistance and handling

A coding agent inventoried the directories, opened the public pages cited above, and drafted this file. The file is a local audit. It has not been submitted to OWASP, W3C, NIST, GitHub, or a university. If any later external text is taken from this audit, the OWASP AI Exchange rule requires a label that AI was used and a description of what it did; the AISVS rule requires the human submitter to own the judgment; the NIST rule forbids treating an LLM check as approval and forbids putting non-public material into the submission. Those labels are not a submission.
