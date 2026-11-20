# Methodology candidates — NIST AI Metrology

Inspection date: 2026-11-20.  
Evidence base: `SOURCE_INVENTORY.md` in this directory, the live Center page, and the live submissions repository.  
Surviving candidates: **0**.  
`NIST_SUBMISSION_DRAFT.md` was not written.

The question asked of the workspace is whether D1 or D2 already supports a reusable evaluation methodology that is distinctive, reproducible, scientifically defensible, relevant to NIST’s stated interests, and suitable for the submission process. The inventory found no manuscript, dataset, figure, result, protocol, or calculating code for AI behavior, human judgment, preference dependence, or evaluation reliability. A methodology cannot be specified from themes alone.

Three shapes were examined because they are the only ones the local record and the public catalog make serious. Each fails. No fourth shape was invented to fill the quota.

## How a real contribution is distinguished

These four events are different. A later sentence in this file uses only the event that the public record shows.

| Event | What it is | What the record shows on 2026-11-20 |
| --- | --- | --- |
| Submitted methodology | A pull request that adds one YAML file under `submissions/` | Many community metric pull requests are open. Opening one is not review and not acceptance. This project has opened none. |
| Reviewer acknowledgment | A human comment or review on that pull request | Retrieved reviews on community metrics recommend revision and leave the pull request open. A comment that says “rejected” has left the pull request open. |
| Accepted repository contribution | A merge. `CONTRIBUTING.md` says “Acceptance = merge.” | Three merges exist. None adds a metric YAML. `submissions/` on `main` contains `README.md` only. |
| NIST publication | A later Center update that lists a merged file | No community metric has been merged, so none has reached this step. The Center page already displays a catalog. Presence on that page is not evidence that a community YAML was merged. The page says inclusion does not constitute NIST endorsement, validation, or determination of suitability. |

Repository facts fetched 2026-11-20 from `https://api.github.com/repos/usnistgov/ai-metrology-submissions` and from `https://api.github.com/repos/usnistgov/ai-metrology-submissions/contents/submissions`:

- Public repository `usnistgov/ai-metrology-submissions`, default branch `main`, created 2026-06-18.
- `pushed_at` 2026-09-14T16:33:15Z. `updated_at` 2026-11-19T12:05:02Z. The last push is still the content-standards merge.
- The pulls list `state=all&per_page=100` returned 28 pull requests and no number 28: numbers 1–27 and 29. States and `merged_at` values match the 2026-11-19 inspection. No new pull request appears after number 29, opened 2026-11-12.
- Merges: [#10](https://github.com/usnistgov/ai-metrology-submissions/pull/10) (Windows validation fix, 2026-08-26), [#12](https://github.com/usnistgov/ai-metrology-submissions/pull/12) (maintainer test, 2026-08-26), [#11](https://github.com/usnistgov/ai-metrology-submissions/pull/11) (content standards, 2026-09-14). Each `merged_at` is non-null. No other pull request in the list has a merge time.

Reviewer practice, carried from the 2026-11-19 reading of review openings and reconfirmed by the unchanged pull-request states today:

- Content standards say most submissions fall short on scientific grounding: one or two references about the metric itself, ideally peer-reviewed or an official NIST resource, and not a governance framework such as the AI RMF.
- Implementation resources must be usable today: released software, a published dataset, or code already merged. An unmerged pull request does not count. The resources must calculate the metric.
- The definition must be concise, state where the metric does and does not apply, and add value beyond the current Center catalog.
- Missing references, no merged implementation, or an out-of-scope metric is the pattern the standards say is most likely to be rejected. The readiness map is an estimate. The reviewers and the approver decide.
- Pull request 19 is the relevant precedent for a newly proposed method. The 2026-09-15 review rated grounding Partial because the metric-specific support was the submitter’s own specification and a newly published implementation, and it asked for independent or peer-reviewed support. On 2026-10-09 a collaborator wrote “Rejected and Please Resubmit” and left the pull request open. That comment is not a merge, not a Center listing, and not a closed pull request.

The Center page fetched 2026-11-20 already displays, among other entries, these human-judgment agreement measures: Cohen's Kappa, Fleiss' Kappa, Gwet's AC1, Intraclass Correlation Coefficient, Kendall's W, Krippendorff's Alpha, Percent Agreement, and Scott's Pi. Kendall's W is described there as a normalization of the Friedman statistic for agreement among three or more annotators ranking items. Several of those entries use the catalog label “Annotator Agreement Evaluation.” The submission schema’s allowed `primary_tevv_application` values, fetched the same day from `SUBMISSION_FORMAT.md`, include `Human-Centered Evaluation` and do not include “Annotator Agreement Evaluation.” That is a vocabulary difference between the displayed catalog and the current YAML schema. It is not a local result.

`Human-Centered Evaluation` is the schema label a future human-judgment method would use if one existed. The catalog’s existing agreement measures are the overlap test that method would have to pass.

## Candidate A — Preference-conditioned decision stability

**Shape.** A method that holds a case record fixed, changes only a stated preference or requested outcome, and reports whether the system’s decision changes. This is the measurement the project themes name as preference dependence, and it is the shape of the unrun AITG-APP-10 sentence in `audits/owasp-testing/AUDIT.md`.

**Why it was serious enough to examine.** The NIST schema has a human-centered application label. A computable stability quantity, with a fixed record, a varied request, a recorded sampling setting, and a rule for missing judgments, would be in the Center’s subject matter if the authors had defined and measured it.

**Evidence.** No D1 or D2 file defines the quantity, the unit, the inputs, the aggregation, the sample size, the baseline, or the control. The OWASP paragraph is a proposed pass/fail case for a different project. It was not run. It is not a stored result and not a public implementation of a metric.

**NIST fit.** A new method with only the submitter’s note would meet the pull-request-19 objection: grounding rated partial, and a request for independent or peer-reviewed support. There is not even that note.

**Disposition.** Drop. No technical specification is written.

## Candidate B — A new human-judgment reliability coefficient

**Shape.** A reusable coefficient for agreement or consistency among human raters, or between human raters and a model judge, offered as an evaluation-reliability method.

**Why it was serious enough to examine.** Evaluation reliability is one of the named themes, and the Center already treats annotator agreement as in scope.

**Evidence.** The workspace has no rating table, no rater count, no item count, and no code that computes an agreement coefficient from local observations. The catalog page already lists Cohen's Kappa, Fleiss' Kappa, Gwet's AC1, the Intraclass Correlation Coefficient, Kendall's W, Krippendorff's Alpha, Percent Agreement, and Scott's Pi, with applied definitions and references on the page.

**NIST fit.** Content standards require the metric to add value beyond what is already in the Center. Resubmitting one of those displayed measures would fail that test. Defining a new coefficient without data, without a reference about that coefficient, and without a merged implementation would fail the grounding test the standards say is where submissions fall short.

**Disposition.** Drop. The catalog entries are NIST’s displayed resources. They are not results of this project, and this project does not resubmit them.

## Candidate C — RR-2, reanalysis of a stored D1 or D2 result

**Shape.** The research-reuse audit’s only NIST-directed design: recompute the authors’ printed number from stored observations with the authors’ formula, then consider a metrology note only if that definition is citable, referenced, and implemented. E-1 is the experiment. It was not run.

**Why it was serious enough to examine.** It is the one design that refuses to invent a metric. It would become a methodology only after the authors’ own definition, table, limitations, and result-versus-hypothesis split are on disk.

**Evidence.** E-1’s required inputs are absent: a frozen results file, its checksum, the authors’ formula, the printed number, the sample size, and any rounding rule the authors stated. `experiments/` is empty. There is no recomputed value, and this sprint does not create one.

**NIST fit.** Even a completed reanalysis would still need one or two references about the metric itself and a public implementation that calculates that definition. Matching a printed number would show arithmetic agreement with a stored table. The audit’s own limitation says that agreement does not show the original study was well controlled.

**Disposition.** Drop until the ten records in `SOURCE_INVENTORY.md` exist. If they arrive, read the stored result and the authors’ limitation text before writing any definition. Stop if those files do not contain a computable quantity.

## What was not proposed

No YAML key was filled. No sample size, interval, model name, or failure mode was written, because the workspace does not contain those facts. No pull request was opened. The empty scaffold at `execution/phase1/drafts/nist-metrology-structure.md` stays empty.
