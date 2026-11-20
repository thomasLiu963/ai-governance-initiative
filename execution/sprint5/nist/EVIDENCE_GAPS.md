# Evidence gaps — NIST AI Metrology

Inspection date: 2026-11-20.  
Decision: the science is not ready. No methodology is specified. `NIST_SUBMISSION_DRAFT.md` is intentionally absent.

The blocker is the absence of D1 and D2 source records, confirmed by a workspace-wide search on this date. Process familiarity does not replace those records. A YAML written now would assert a definition, a reference, and an implementation that the workspace does not contain.

## The blocker

`research/D1/` and `research/D2/` each contain zero files. The rest of the workspace also contains zero manuscripts, datasets, figures, statistical results, protocols, limitation statements, licenses, coauthor approvals, or calculating code for AI behavior, human judgment, preference dependence, or evaluation reliability. Details and the search method are in `SOURCE_INVENTORY.md`.

E-1, E-2, and E-3 were specified on 2026-11-18 and were not run. This sprint does not run them, because their inputs are the missing files. A new model call is not a substitute for a stored result.

## What a later methodology would still have to clear

These are gates. They are not a draft definition.

### Ten source records

Each record is missing for both tracks.

| Record | Gap on 2026-11-20 |
| --- | --- |
| Manuscript status | No file states title, authors, date, version, or a status word the authors wrote. |
| Locator or quotation permission | No public locator and no sentence permitting quotation. |
| License and rights holder | No notice. |
| Coauthor approval | No names and no written decisions. |
| Confidentiality | No label. Absence of a banner is not clearance. The submission and the review are public. |
| Dataset description | No filename, row count, schema, collection method, or permission to remove the file from this machine. |
| Stored result | No table or log, metric definition, sample size, system identifier, run date, baseline, or control. |
| Recomputable protocol | No procedure that recomputes a printed number without a new model call. |
| Author limitation text | No verbatim limitation. |
| Result-versus-hypothesis split | No author sentence to classify. |

### Three NIST gates the ten records do not satisfy

Fetched 2026-11-20 from `CONTENT_STANDARDS.md` and `SUBMISSION_FORMAT.md` on `main`:

1. One or two references about the metric itself, specific and ideally peer-reviewed, or an official NIST resource. A governance framework such as the AI RMF is for mapping, not grounding. The 2026-11-19 reading of review openings recorded that pull request 6 was left open with the AI RMF called too broad, and that pull request 19 asked for support other than the submitter’s own specification. Those review bodies were not re-fetched on 2026-11-20. The pull requests themselves were still open and unmerged on this date.
2. An implementation usable today: released software, a published dataset, or code already merged into an open-source repository. It must calculate the metric. An unmerged pull request does not count. Every link has to be confirmed.
3. A contact email and at least one submitter organization. Both are published with the file.

`known_failure_modes` is optional. The standards and the “what to have ready” material describe it as the field reviewers often find empty. It can be written only from the authors’ limitations or from a failure the stored result actually shows.

### Catalog overlap

Any later definition has to be checked against the Center page before it is named. On 2026-11-20 the page already displays Cohen's Kappa, Fleiss' Kappa, Gwet's AC1, the Intraclass Correlation Coefficient, Kendall's W, Krippendorff's Alpha, Percent Agreement, and Scott's Pi. A second submission of one of those quantities fails the requirement to add value beyond the catalog.

### Public-disclosure rule

`CONTENT_STANDARDS.md` says “Do not input anything non-public.” `CONTRIBUTING.md` and `SUBMISSION_FORMAT.md` say the file and the review discussion are public. An unpublished manuscript, a confidential dataset, or a human-subjects file cannot be pasted into the YAML to fill a gap.

## Exact submission requirements, recorded so they are not mistaken for a draft

These are the rules a future file would have to meet. This sprint does not apply them to a metric, because no metric exists.

- One YAML file, one metric or measurement method, under `submissions/`, lowercase hyphenated name, pull request from a fork to `main`.
- `schema_version` is `"1.0"`. Seven keys are required: `schema_version`, `name`, `applied_definition`, `submitter_organizations`, `contact_email`, `references`, `implementation_resources`. Other recognised keys are optional. An unrecognised key is an error.
- English. The applied definition is concise and computable. Scope boundaries are explicit.
- Optional metadata, when used, must use the allowed values in `SUBMISSION_FORMAT.md`. For a human-judgment method the schema’s application value is `Human-Centered Evaluation`. The catalog label “Annotator Agreement Evaluation” is not in that allowed list.
- Local mechanical check, named in the format document: `check-jsonschema --schemafile validation/schemas/v1.json` against the YAML. A green check is not reviewer approval. An LLM check is not approval.
- Stated timing, from `CONTRIBUTING.md` and the “what happens next” page fetched 2026-11-20: an automated check is expected within about an hour; first human contact is described as about two weeks and is the start of review, not the decision. Acceptance is the merge. Publication on the Center is a later update. No fixed submission deadline was found.
- Observed timing: no metric YAML has been merged. Community metric pull requests opened in August 2026 were still unmerged on 2026-11-20. Pull requests 21 through 27 and 29 had no review state change that produced a merge. First contact is not acceptance. A merge is not a Center listing. A Center listing is not endorsement.

## What supplying the files would still not authorize

A complete bundle would allow a reader to decide whether a computable definition exists. It would not authorize a pull request. External submission stays blocked until Thomas approves that specific action. The contact email would be public. Unpublished text would stay out of the file.
