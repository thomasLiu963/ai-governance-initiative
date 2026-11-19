# T004 — Parent of `dpv:RightsFulfilment`

Status: draft for internal review. Not submitted. No GitHub comment, pull request, mail, or other external contact has been sent.

Issue: [w3c-cg/dpv#486](https://github.com/w3c-cg/dpv/issues/486), opened 2026-09-07 by `Daham-Mustaf`. Label `todo`. No assignee. Rechecked 18 November 2026: still open, two comments, `updated_at` `2026-09-09T10:13:40Z`.

The external artifact is a comment, not a pull request. The text to paste is [COMMENT.md](COMMENT.md).

## Document status

[DPV 2.3](https://w3c-cg.github.io/dpv/2.3/dpv/) is a Final Community Group Report, 25 February 2026. It says it is not a W3C Standard and is not on the W3C Standards Track. The parent fix would ship in a later release only if the group edits the spreadsheet and regenerates. This draft does not claim that release.

## What was rechecked immediately before this text

- Issue #486 API: open, comments still the two from 9 September 2026 (`besteves4` at 08:31 UTC, `Daham-Mustaf` at 10:13 UTC). No new comment.
- `master` `689d32c0f7c571d32f7f8635ae548fcc1c3ff695`. `dev` `aff91c294b105d9a261ea8622350b0fc7ef0e293`. Both 18 November 2026.
- Git grep of every `*.ttl` and `*.csv` in a sparse `dev` checkout: `RightsFulfilment` occurs only in the purposes serialisations (2.2, 2.3, and `2.4-dev`) and in `code/vocab_csv/Purpose.csv` plus the exported purpose CSVs. No `skos:broader dpv:RightsFulfilment` child.
- Public list index for November 2026, fetched again while this text was prepared. Last messages: 18 November calendar update and the Social Equation Hub enquiry. No 25 November agenda mail. `0005.html` returns 404.
- 25 November event page, fetched again: Confirmed, 13:30–14:30 GMT, agenda text still the 18 November agenda, joining instructions login-restricted.

## The defect, as the reporter and the chairs left it

The reporter showed `dpv:RightsFulfilment` typed `dpv:Purpose` and in `dpv:purposes-classes`, with `skos:broader dpv:LegalObligation`, and said the scope note seems to allow activities that are not legal obligations.

`besteves4` (Beatriz Esteves, a chair on the [group page](https://www.w3.org/groups/cg/dpvcg/)) replied that the concept is a purpose and should not have a legal basis as its parent, and that the parent should be `dpv:FulfilmentOfObligation` or `dpv:LegalCompliance`. The reporter acknowledged that the same morning. The issue still contains that open choice.

The 9 September 2026 minutes close the choice. Present: Beatriz, Georg, Harsh, Julian, Julio, MuhammadAslam, Stratis. Chair: Harsh. Two actions:

1. Change the parent of `dpv:RightsFulfilment` to `dpv:FulfilmentOfObligation`.
2. Update the purpose-module description and examples for Rights Fulfilment.

Source: [`meetings/meeting-2026-09-09.html`](https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/meetings/meeting-2026-09-09.html) at `689d32c0`, anchors `a01` and `a02`. A search of meeting files finds `RightsFulfilment` only in that file. Neither action is in 2.3 or `2.4-dev`.

Harsh’s sentence in those minutes: “dpv:RightsFulfilment should have as parent dpv:FulfilmentOfObligation because rights may not be legal obligations.” The minutes attribute to Georg a clarification that the hierarchy covers purposes where a bearer and a condition need fulfilment, with fulfilment of obligation as the parent. The minutes spell the speaker as Georg. The concept’s contributor list includes Georg P. Krog. This draft does not add a surname the minutes do not use.

After the action, Beatriz is recorded as asking about purposes used as legal bases. Harsh’s reply in the same section is that purpose and legal basis stay separate: the purpose describes what is done, and the legal basis names the authority in law. He gives identity verification as the example of a purpose that must not be recorded as a legal basis.

## The two parents

Published definitions, `2.3/dpv/dpv.ttl`. The `2.4-dev` purpose module has the same parent triples. `reproduce.py` prints them.

| Concept | `rdf:type` | `skos:broader` | Definition |
| --- | --- | --- | --- |
| `dpv:RightsFulfilment` | `dpv:Purpose` | `dpv:LegalObligation` | Purposes associated with the fulfillment of rights specified in law |
| `dpv:LegalObligation` | `dpv:LegalBasis` | `dpv:LegalBasis` | Legal Obligation to conduct the specified activities |
| `dpv:FulfilmentOfObligation` | `dpv:Purpose` | `dpv:Purpose` | Purposes associated with carrying out data processing to fulfill an obligation |
| `dpv:LegalCompliance` | `dpv:Purpose` | `dpv:FulfilmentOfObligation` | Purposes associated with carrying out data processing to fulfill a legal or statutory obligation |
| `dpv:FulfilmentOfContractualObligation` | `dpv:Purpose` | `dpv:FulfilmentOfObligation` | Purposes associated with carrying out data processing to fulfill a contractual obligation |
| `dpv:ProtectionOfIPR` | `dpv:Purpose` | `dpv:FulfilmentOfObligation` | Purposes associated with the protection of intellectual property rights |
| `dpv:OrganisationComplianceManagement` | `dpv:Purpose` | `dpv:OrganisationGovernance` | Purposes associated with managing compliance for organisation in relation to internal policies |

`LegalCompliance` scope note: the purpose is only processing additionally required to fulfil obligations in a law, and it will typically be used with Legal Obligation as the legal basis. `RightsFulfilment` scope note: where the activity also includes something that is not a legal obligation, for example identity verification, record that part as a separate purpose. `OrganisationComplianceManagement` scope note: internal policy compliance; use `LegalCompliance` for external legal or regulatory compliance.

`ParentTerm` / `ParentType` in `code/vocab_csv/Purpose.csv` on `dev`: Rights Fulfilment is `dpv:LegalObligation` / `dpv:Purpose`. Fulfilment of Obligation has an empty `ParentTerm` and `ParentType` `dpv:Purpose`, which the taxonomy schema emits as `skos:broader dpv:Purpose`. Legal Compliance, contractual fulfilment, and protection of IPR already use `ParentTerm` `dpv:FulfilmentOfObligation`.

### If the parent becomes `dpv:FulfilmentOfObligation`

This is the minuted action. Rights fulfilment becomes a fourth purpose child of Fulfilment of Obligation, beside contractual fulfilment, legal compliance, and protection of IPR. Protection of IPR is the existing rights-related sibling, created 2024-02-14, the same date as Rights Fulfilment, with source `DGA 3.1(c)`. Their definitions can both be used for some intellectual-property cases. The action does not move Protection of IPR. This draft does not propose that move.

A query for purposes under Legal Compliance will not return Rights Fulfilment. That follows from Harsh’s reason that rights may not be legal obligations, and from Georg’s description of the parent as fulfilment of an obligation in the broader sense. The legal basis, when a law actually requires the fulfilment, stays on `dpv:hasLegalBasis`.

`dpv:OrganisationComplianceManagement` is the wrong branch. Its scope note sends external legal compliance to `LegalCompliance`. Applying that sentence to Rights Fulfilment would contradict the minutes. The description update (action 2) is where the module text should say that rights fulfilment is under Fulfilment of Obligation.

### If the parent becomes `dpv:LegalCompliance`

This is the other parent Beatriz named on the issue, before the meeting. It would make rights fulfilment a narrower legal-compliance purpose: processing additionally required by statute, typically paired with the legal basis Legal Obligation. That pairing is what the meeting refused. It would also leave the OWL class as a subclass of a purpose that is still used together with `dpv:LegalObligation`, which keeps the purpose/legal-basis mix Harsh described in the next paragraph of the minutes.

Legal Compliance has no current children, so there is no grandchild collision. The conflict is semantic and it reverses a minuted action. This draft does not ask the group to reopen it.

### Scope note

The reporter read the scope note as saying rights fulfilment can include activities that are not legal obligations. The sentence is an authoring instruction: split those activities into separate purposes. The KYC example in section 4 of the purposes module already does that, with `skos:broader` to identity verification and to legal compliance, and `dpv:hasLegalBasis` to `dpv:LegalObligation`. The comment says that, and it does not correct the reporter’s tone. The parent decision is the minutes, not a new reading of the note.

## Downstream effects that were checked

SPARQL on `2.3/dpv/dpv.ttl` and `2.4-dev/dpv/dpv.ttl`: the only purpose whose `skos:broader` target is not typed `dpv:Purpose`, and is not `dpv:Purpose` itself, is Rights Fulfilment → Legal Obligation. Concepts whose parent is `dpv:Purpose` are the roots of a branch. The query in the comment excludes that root on purpose. `dpv:Purpose` is not `rdf:type dpv:Purpose`.

No Turtle concept has `skos:broader dpv:RightsFulfilment`. Changing the parent does not require moving children. Sector, legal, and risk modules in the `dev` Turtle checkout do not name the IRI.

OWL, `2.3/dpv/dpv-owl.ttl` (same checksum on `dev`): `dpv-owl:RightsFulfilment` is typed `dpv-owl:Purpose` and is `rdfs:subClassOf dpv-owl:LegalObligation`, hence `rdfs:subClassOf+ dpv-owl:LegalBasis`. There is no `skos:broader`. `dpv-owl:Purpose` has no `rdfs:subClassOf` path that reaches `dpv-owl:LegalBasis`. `owl:disjointWith` occurs zero times, so the file does not say Purpose and Legal Basis are disjoint. Under the RDFS meaning of `rdfs:subClassOf`, every instance of the Rights Fulfilment class is a Legal Obligation and a Legal Basis. The same IRI is also an instance of Purpose. After the spreadsheet change and a regeneration, the subclass path should go through Fulfilment of Obligation to Purpose, and the Legal Basis path should disappear. This draft did not run the generator.

Generated HTML, `2.3/dpv/modules/purposes.html` and the `2.4-dev` page: the Rights Fulfilment term table lists parent Legal Obligation → Legal Basis, and “Object of relation” `dpv:hasLegalBasis`. The Legal Compliance and Fulfilment of Obligation tables list `dpv:hasPurpose`. `dpv:hasLegalBasis` has `dcam:rangeIncludes` and `schema:rangeIncludes` `dpv:LegalBasis`. `dpv:hasPurpose` ranges over `dpv:Purpose`. The HTML is a generated consequence of the parent. It is another reason the parent is wrong, and it is fixed by regeneration, not by editing the HTML.

SHACL `ex:ValidTermsShape-skos-broader` only requires `skos:prefLabel` on the parent. Legal Obligation has a label, so the shape does not catch a purpose parented to a legal basis.

Section 4 of the purposes module, “Legal Obligation/Compliance”, lists the children of Fulfilment of Obligation as Fulfilment of Contractual Obligation, Legal Compliance, and Protection of IPR, and tells the reader to use the legal basis Legal Obligation when the law requires the processing. It does not name Rights Fulfilment. Action 2 is still open. The comment asks to add Rights Fulfilment to that list and to leave the legal basis on `hasLegalBasis`. It does not paste a replacement for the whole section.

## Themes

Privacy and authorization. A purpose says why the processing is done. A legal basis says what makes that processing lawful. The current parent stores the first claim in the relation used for the second. The generated page then offers the purpose as a filler for `hasLegalBasis`.

## Implementation

One spreadsheet cell: Purpose sheet, term `RightsFulfilment`, `ParentTerm` from `dpv:LegalObligation` to `dpv:FulfilmentOfObligation`. `ParentType` stays `dpv:Purpose`. The chair, or someone with sheet access, makes that edit. The group regenerates. Adopters who copied the old parent update when the regenerated vocabulary is published. No new term. No hand edit of Turtle, HTML, or `code/vocab_csv`.

The SPARQL guard can be re-run on the regenerated `dpv.ttl`. It should return no rows. This draft does not ask for a new SHACL shape in the same comment. The query is enough for the parent pass the chair described on 18 November.

## 25 November 2026

The meeting is a viable moment for the group to apply the existing action. It is not a viable place for this project to speak, and it is not a reason to reopen the parent.

The 18 November minutes say the next meeting’s topics include “discussion on IRI and parent changes”, and that the chair will comment proposed resolutions on the GitHub issues and make the v2.4 commits. Beatriz Esteves sent regrets on 18 November. The note-taking item was deferred because she was expected on 25 November. She is the chair who named both parents and who was present when the action was recorded.

The public event page, fetched while this text was written, has not been updated. It still shows the 18 November agenda: v2.4 plan, maintenance, past minutes, EHDS/GDNG, the Data Act, and triage of IRI, parent, and typo issues, plus “Mailing List: No new updates”. That triage line still covers parent errors, but it is the previous week’s text. There is no agenda mail for 25 November. Joining instructions require a W3C login. Do not mail the list or the chairs to be added.

If this comment is approved before 25 November, it gives the chair a resolution to use in the parent pass. The comment says the choice was made on 9 September. If he has already commented a different parent by the time posting is approved, do not send a second comment. Record his choice and stop.

## AI-assistance requirements

Read:

- [contributing.md](https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/contributing.md)
- [Contribution Guide](https://github.com/w3c-cg/dpv/wiki/Contribution-Guide), wiki date shown as 12 February 2026. No AI-tool rule.
- [Draft W3C AI-tool policy](https://www.w3.org/2026/10/draft-ai-policy.html). The page says it is not yet a W3C policy. It asks a human to own the contribution, disclose AI-drafted substance, answer replies in person, and avoid a flood of generated comments. The Advisory Board document it names was not retrieved.

The comment includes a disclosure line. Before posting, a person re-runs `reproduce.py`, checks the quotations, the minute anchors, and the query, and is the account that posts and that answers replies. Do not post from an automated account.

## Submission

Do not send anything until this specific comment is approved.

1. Re-read [#486](https://github.com/w3c-cg/dpv/issues/486) and the 9 September minutes. If a chair has already named the parent, do not post a competing choice.
2. From `contributions/T004-DPV-Rights/`, install `requirements.txt` in a virtual environment and run `python reproduce.py`. The only bad parent row should be Rights Fulfilment / Legal Obligation.
3. Paste [COMMENT.md](COMMENT.md) on issue #486 from the reviewer’s GitHub account. Keep the disclosure and sign it.
4. Do not open a pull request. Do not edit `code/vocab_csv/Purpose.csv`, the Turtle, or the HTML. The guide says those outputs are generated, the CSV is an export of the online sheet, and a parent change is an issue for someone with sheet access.
5. Do not mail `public-dpvcg@w3.org` and do not contact the chairs.
6. Repository contributions are under the license the group states. The README links the [W3C Software and Document License](https://www.w3.org/copyright/software-license-2023/). The poster is responsible for that.

Record a submission in `MASTER_TRACKER.md` and `evidence/` only after it has been sent. If the group’s commit uses this parent, the accomplishment is the published parent. Do not describe the chair’s commit as this project’s patch.

## Sources

- Issue #486 and the two comments, fetched 18 November 2026.
- Minutes of 9 September 2026 and 18 November 2026 on `689d32c0`.
- `2.3/dpv/dpv.ttl`, `2.3/dpv/dpv-owl.ttl`, `2.3/dpv/modules/purposes.html`, checksums in `results/report.txt`.
- `2.4-dev` copies of those artifacts, `code/vocab_csv/Purpose.csv`, and `code/shacl_shapes/shapes.ttl` at `aff91c29`.
- `construct_parent_taxonomy` and the purposes `taxonomy` entry in `code/vocab_management.py`.
- Sparse `dev` checkout grep of `*.ttl` and `*.csv`.
- RDF Schema 1.1, `rdfs:subClassOf`, cited in the comment.
- 25 November event page: https://www.w3.org/events/meetings/65197685-0e2b-44a1-b715-280dc3af0582/20261125T133000/
- November 2026 list index: https://lists.w3.org/Archives/Public/public-dpvcg/2026Nov/
- Group page for the chairs’ names: https://www.w3.org/groups/cg/dpvcg/

## Not verified

- The online Purpose spreadsheet. `code/vocab_csv/Purpose.csv` on `dev` still has `dpv:LegalObligation`. The sheet itself was not opened.
- Execution of `200_serialise_RDF.py` or the HTML generator. The OWL and HTML consequences are read from the published files and from the generator source. They are not a regeneration run.
- An OWL reasoner. The subclass path is a SPARQL property path. The RDFS reading of that path is the specification, not a reasoner log.
- HTML files other than the purposes module. Turtle and CSV were searched across `dev`.
- W3C login, so the 25 November join link was not visible.
- The Advisory Board LLM document named by the draft AI policy.

## Reproduce

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python reproduce.py
```

The script downloads pinned public files into `cache/` on first run. No model API is called. `rdflib==7.6.0`. `fixture/rights.ttl` is the excerpt the script checks: Rights Fulfilment broader Legal Obligation, Legal Obligation typed Legal Basis, Legal Compliance broader Fulfilment of Obligation, Rights Fulfilment typed Purpose.
