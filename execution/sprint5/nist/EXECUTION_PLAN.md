# Execution plan — NIST institutional track

Inspection date: 2026-11-20.  
Deadline named by the project: 2027-02-15.  
Decision: stop. Do not draft a metric. Do not open a pull request. Do not email NIST.

The strongest evidence-supported methodology does not exist. Candidates A, B, and C in `METHODOLOGY_CANDIDATES.md` each fail for lack of source records. Writing a technical specification, an evaluation procedure, or a YAML would manufacture the science the inventory did not find. `NIST_SUBMISSION_DRAFT.md` is omitted for that reason.

February 15 is a quality date. It is not a reason to file an unready proposal. The public record also does not support treating that date as an acceptance date: no community metric YAML has been merged, and metric pull requests opened in August 2026 were still open on 2026-11-20.

## Current position

| Item | State |
| --- | --- |
| D1 and D2 source files | Absent in the designated directories and absent elsewhere in this workspace. See `SOURCE_INVENTORY.md`. |
| Sprint 4 NIST research | None. `execution/sprint4/` is the California AI sprint. |
| Phase 1 NIST research | `execution/phase1/NIST.md` dropped the track on 2026-11-19. The blank scaffold remains at `execution/phase1/drafts/nist-metrology-structure.md`. |
| This sprint | Confirms the drop after a wider file search and a same-day re-read of the repository, the format, the content standards, and the Center catalog. |
| External action | None taken. None authorized. |

## Work that is allowed before the files arrive

1. Leave the ten source records listed in `SOURCE_INVENTORY.md` as the intake list. When a file arrives, register it against that list before anyone writes a definition.
2. Re-read `CONTENT_STANDARDS.md`, `SUBMISSION_FORMAT.md`, and `CONTRIBUTING.md` on `main` at the time of that intake. The reviewer page says that if the page and the repository disagree, the repository is correct. On 2026-11-20 the reviewer page’s “last read” line was still 2026-11-19, and the repository’s `pushed_at` was still 2026-09-14.
3. Check the Center catalog for the quantity the authors actually defined. The agreement measures already on the page are listed in `EVIDENCE_GAPS.md`.
4. Keep the four outcomes separate: a pull request, a reviewer comment, a merge, and a later Center listing. Record only the one that has happened.

## Work that starts only after the ten records are in the workspace

Do these in order. Stop at the first failure. Do not fill a gap from memory or from a model call.

1. Read the manuscript status, license, coauthor approvals, and confidentiality label. If the material is unpublished, confidential, embargoed, or not approved for a public submission, stop. The YAML and the review are public.
2. Read the stored result and the authors’ limitation text. If they do not contain a quantity a second person can compute, stop.
3. Run E-2 on the protocol file: mark population, assignment, control, baseline, metric, stopping rule, and limitation as present, ambiguous, or absent, using only sentences in the file.
4. Run E-3 on the frozen manuscript: label results-bearing sentences as reported result, hypothesis, limitation, or not classifiable. A reported result has to point at a table, figure, or log in the same bundle.
5. Run E-1 only when the frozen results file, the authors’ formula, the printed number, and the sample size are all present. The output sentence is the audit’s sentence: the run is a recalculation of stored numbers, not a measurement of a model. If the authors state no rounding tolerance, write “tolerance absent” and do not invent one.
6. Compare the authors’ quantity with the live catalog. If the catalog already displays it, stop.
7. Confirm one or two references about that quantity, and confirm each link. A reference about AI governance in general does not qualify.
8. Confirm an implementation that calculates that quantity and is already released or merged. A script that exists only in this workspace does not qualify until it is public and merged.
9. Only then draft a YAML for internal review, with `contact_email` and `submitter_organizations` supplied by Thomas, because both are published. Put the draft under this directory as `NIST_SUBMISSION_DRAFT.md` and leave every claim traceable to a file path. Known failure modes come from the authors’ text or from the stored result.
10. External opening of the pull request is a separate approval. This plan does not give it.

## February 15, if the files arrive in time to do the steps above

From 2026-11-20 to 2027-02-15 is 87 days. The stated first human contact is about two weeks and is not a decision. The August 2026 metric pull requests that received revision requests were still unmerged more than three months later. No metric merge exists from which to estimate acceptance, and no merge-to-listing interval exists because there has been no metric merge.

The feasible February product, if and only if the source records arrive early enough to finish the ten steps, is an internally reviewed YAML that a person could choose to submit. An accepted repository contribution by 2027-02-15 is not a supported forecast. A Center listing by that date is not a supported forecast. A listing would still not be NIST endorsement.

If the records are still absent in December, the track stays stopped. December is not a month for opening a pull request that asserts results.

## What this plan refuses

- A preference-stability metric, a new agreement coefficient, or any other definition written to match the project themes.
- Use of the FCC revocation harness, the GPC browser run, the DPV queries, or the OWASP probes as validation evidence. Those artifacts measure other tasks.
- Use of the OWASP AITG-APP-10 proposal as a measured result. It was not run.
- A resubmission of Kendall's W or of the other agreement measures already on the Center page.
- An information-quality correction. The 2026-11-19 inspection found no qualifying error, and this sprint did not reopen that pathway.
- Any push of research files to the public GitHub remote. The research-reuse audit recorded that remote as public.

## Approval line

No external submission is approved by this file. A later approval has to name the YAML, the contact email, and the public implementation link, and it has to come from Thomas.
