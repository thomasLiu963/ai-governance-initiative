# NIST AI Metrology Center — submission structure

Status: scaffold only. Not a pull request. Not a metric. No result from D1 or D2 is stated here, because those directories have no files. Do not fill the blanks from memory. Do not submit this file.

Sources re-confirmed in `execution/phase1/NIST.md` on 2026-11-19: one YAML file per metric, public pull request to `usnistgov/ai-metrology-submissions`, schema version `"1.0"`. Inclusion on the Center page is not NIST endorsement. No community metric YAML has been merged. A newly proposed method that cites only the submitter's own note was told, on pull request 19, to resubmit with independent or peer-reviewed support.

## Exact files required before any substantive claim

All ten have to exist for the track that would be submitted. A missing file blocks the claim. It does not block keeping this scaffold.

1. Manuscript: title, authors, date, version, and a status the authors wrote: published, accepted, submitted, preprint, unpublished, or internal.
2. Locator, if the manuscript is public. If it is not public, a written sentence that says whether it may be quoted. Non-public text cannot go into the YAML. The Center's rule is "Do not input anything non-public."
3. License and the rights holder.
4. Written approval from each living coauthor whose text or numbers would be reused, covering reanalysis and a public submission.
5. Confidentiality label: public, embargoed until a stated date, confidential, or restricted. Human-subjects or institutional limits have to be named if they apply.
6. Dataset description: filename, row or item count, schema, license, the authors' collection method, and whether the file may leave the machine.
7. Stored result: the table or log, the metric definition, the sample size, the system identifier, the run date, the baseline, and the control condition.
8. Protocol sufficient to recompute the stored numbers without a new model call.
9. The authors' limitation text, kept verbatim.
10. The authors' own split between a reported result and a hypothesis. A sentence they did not split is marked "not classifiable" and is not upgraded.

NIST adds three gates those files do not satisfy by themselves:

- One or two references about the metric itself, ideally peer-reviewed or an official NIST resource, not a governance framework.
- An implementation that calculates the metric and is usable now: released software, a published dataset, or code already merged. An unmerged pull request does not count.
- A contact email that will be published.

## Methodology requirements the YAML must be able to state

These are questions for the supplied files. They are not answers.

- Applied definition: the quantity, the unit, the inputs, and the aggregation, in words a second person can compute.
- What is held fixed: model, prompt, preference condition, rater pool, and task.
- What is varied: the condition the metric claims to detect, such as a change in human judgment or a change in stated preference.
- Baseline and control: what number the metric is compared with, and what would make the comparison fail.
- Sample size and how a missing or refused human judgment is counted.
- Known failure modes: at least the cases where the metric moves for a reason other than the one it names. Reviewers have asked for this field when it is empty.
- What the metric does not measure: agreement with a person, safety, legal compliance, or deployment quality, unless the stored result actually measures that.

## Novelty assessment, applied only after the files exist

Answer these from the files and from the public catalog. Do not answer them now.

- Does the catalog already display this quantity under another name? Jailbreak success rate and toxicity score are on the Center page without a merged community YAML. A duplicate of a displayed measure is not a new submission.
- Is the definition computable from the stored table, or does it require a new judgment?
- Are the references about this metric, or only about AI governance in general? Pull request 6 was left open because the AI RMF was too broad.
- Is the implementation public and merged, and does it compute this definition rather than a nearby one?
- If the method is new, is there support other than the submitter's own note? Pull request 19 treated submitter-only grounding as partial and was told to resubmit. That is the relevant precedent for an original method. It is not a rejection rate.

## Empty YAML shape

Leave every evidence field blank until the files above are supplied and checked. `contact_email` and `submitter_organizations` stay blank on purpose.

```yaml
schema_version: "1.0"
name: ""                    # short name of one metric; not filled
applied_definition: ""      # computable definition; not filled
submitter_organizations: [] # not filled
contact_email: ""           # published if submitted; not filled
references: []              # 1-2 works about this metric; not filled
implementation_resources: [] # public code or data that calculates it; not filled
# optional, often requested:
# known_failure_modes: []
# primary_tevv_application: ""  # only a value the schema allows
```

## When the files arrive

Read the stored result and the authors' limitation text before writing `applied_definition`. If the files do not contain a computable definition, stop. Do not invent the number, the sample size, or the failure mode. A passing local script is not the implementation resource unless that script is public, merged, and computes the authors' definition.
