# DPV ServiceOptimisation scope note

Status: ready to post as one comment on issue 495, after explicit approval. Not posted.

## Source

| Item | Locator |
| --- | --- |
| Issue | https://github.com/w3c-cg/dpv/issues/495. Open, no assignee, zero comments, `updated_at` 2026-10-29. |
| Published vocabulary | DPV 2.3 Final Community Group Report, 25 February 2026. `master` `689d32c0f7c571d32f7f8635ae548fcc1c3ff695`. |
| Development tree | `dev` `aff91c294b105d9a261ea8622350b0fc7ef0e293`, directory `2.4-dev`. |
| Document status | Community-group vocabulary. The report says it is not a W3C Standard and is not on the W3C Standards Track. |

## What is wrong

On 8 February 2026 the term was re-parented under `dpv:ServiceManagement`. The scope note was not updated. It still says ServiceOptimisation is a subclass of ServiceProvision. The same release's note on ServiceProvision says that term is only for providing a service, and not for managing or monitoring it.

A reader who follows the note classifies optimisation as provision. A reader who follows the parent classifies it as management. Those are different purposes.

## Proposed change

One replacement sentence, in `COMMENT.md`. No new term. No pull request. The contribution guide says vocabulary edits belong in the spreadsheet, and that generated HTML, RDF, and exported CSVs are not pull-request targets.

## Contribution and AI rules

`contributing.md` on the default branch says decisions are made in meetings and membership is not required to contribute. It states no AI-assistance rule. The comment discloses the drafting anyway. The wiki Contribution Guide URL in that file returned 404 on 2026-11-19 and was not retried.

## Ordinary-language significance

DPV is a shared list of privacy terms. Software uses it to record why personal data was processed. "Optimising the service" and "providing the service the person asked for" are different reasons. The list now places optimisation with managing the service, but a leftover sentence still says it is part of providing the service. The comment asks the maintainers to replace that one sentence so the note matches the parent they already chose.

If they do, the change is in a Community Group vocabulary. It is not a W3C Recommendation, and it does not by itself change any company's privacy notice.

## Claims that would be false

- "I changed the W3C privacy standard." DPV is a Community Group report.
- "The group agreed." Agreement is a later vocabulary commit, or a meeting resolution.
- "This creates a new privacy right." It corrects a label on an existing term.

## What would count

A `dev` or published commit in which `dpv:ServiceOptimisation` no longer says it is a subclass of ServiceProvision, and its parent is still ServiceManagement. The comment alone is not acceptance.

## Not verified

The online Purpose spreadsheet. The generator was not run. No OWL reasoner was run. The contradiction is the two scope notes and the parent triple, which were read in the Turtle.
