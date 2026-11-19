# T003 — Canonical concept-membership test

Status: draft for internal review. Not submitted. No GitHub comment, pull request, mail, or other external contact has been sent.

Issue: [w3c-cg/dpv#484](https://github.com/w3c-cg/dpv/issues/484), “Document the canonical way to test concept membership”, opened 2026-08-27 by `Gogga`. Labels `todo`, `help-wanted`. No assignee. Rechecked 18 November 2026: still open, zero comments, `updated_at` `2026-08-27T13:13:05Z`.

The external artifact is a comment, not a pull request. The text to paste is [COMMENT.md](COMMENT.md).

## Document status

[DPV 2.3](https://w3c-cg.github.io/dpv/2.3/dpv/) is a Final Community Group Report, 25 February 2026. The report says it is not a W3C Standard and is not on the W3C Standards Track. The versionless IRI `https://w3id.org/dpv` points at the latest release. `dev` contains `2.4-dev`. This contribution proposes wording for the primer. It does not change a W3C Recommendation.

## What was rechecked immediately before this text

- Issue #484 API: open, no comments, no assignee, labels unchanged.
- `master` `689d32c0f7c571d32f7f8635ae548fcc1c3ff695` (18 November 2026, minutes and index fix). `dev` `aff91c294b105d9a261ea8622350b0fc7ef0e293` (same day).
- Public list index for November 2026, fetched again while this text was prepared: last messages are the 18 November calendar update and the Social Equation Hub enquiry. `0005.html` returns 404. There is no 25 November agenda mail.
- Event page for 25 November 2026, fetched again while the draft was prepared: status Confirmed, 13:30–14:30 GMT. The agenda text was still the 18 November agenda. Joining instructions are restricted to logged-in W3C users. This final pass did not fetch that page again.
- Final pass, same day: issue API still open, zero comments, `updated_at` unchanged. `master` and `dev` still the commits above. `reproduce.py` re-run with `rdflib` 7.6.0. `2.4-dev/dpv/dpv-owl.ttl` and `2.4-dev/pd/pd-owl.ttl` match the 2.3 OWL checksums. The list index still ends at `0004.html`, the Social Equation Hub enquiry, and `0005.html` is still 404.

## The gap

Implementers are not told which relation answers “is this concept in category X?”. The issue treats `rdf:type`, a transitive `skos:broader` walk, and `rdfs:subClassOf` as rival answers to one question, and it says `subClassOf` is not an inference relation.

Those predicates are defined differently, and DPV emits them for different spreadsheet columns.

| Relation | Specification | What DPV emits |
| --- | --- | --- |
| `rdf:type` | The subject is an instance of the object class. [RDF Schema 1.1, §3.3](https://www.w3.org/TR/rdf-schema/#ch_type). | Top category from spreadsheet `ParentType`, when that cell names a concept. Also the PD hook below. |
| `skos:broader` | Direct hierarchical link. Not declared transitive. [SKOS Reference §§8.1 and 8.6.6](https://www.w3.org/TR/skos-reference/). A broader link does not entail `skos:inScheme` ([§4.6.4](https://www.w3.org/TR/skos-reference/)). | Spreadsheet `ParentTerm`, via `construct_parent_taxonomy` in `code/vocab_funcs.py`. |
| `skos:broaderTransitive` | Transitive superproperty of `skos:broader` (SKOS S22, S24). Not for assertions. | Not asserted. Neither serialisation has `owl:imports`, so a reasoner does not load the SKOS axioms unless the adopter does. |
| `rdfs:subClassOf` | Every instance of the subject class is an instance of the object class. Transitive. [RDF Schema 1.1, §3.4](https://www.w3.org/TR/rdf-schema/#ch_subclassof). | Written when `ParentType` is the token `sc`. A `ParentType` that names a concept is `rdf:type`, and its `ParentTerm` is `skos:broader`. |
| `owl:subClassOf` | Not the OWL 2 RDF mapping. A subclass axiom is `rdfs:subClassOf`. [OWL 2 Mapping to RDF Graphs](https://www.w3.org/TR/owl2-mapping-to-rdf/#Mapping_from_the_Structural_Specification_to_RDF_Graphs), table row `SubClassOf(CE1 CE2)`. | Zero triples in the 2.3 RDFS and OWL files. `rdflib` 7.6.0 has no such term in the OWL namespace. |
| `skos:inScheme` | Membership of a concept scheme. The range is `skos:ConceptScheme` (SKOS S4). | PD hook, and ordinary module schemes. Deleted when the OWL file is built (`code/200_serialise_RDF.py`). |

`code/vocab_schemas.py` sends the PD extension and the purposes module through the `taxonomy` schema. In `construct_parent_taxonomy`, a `ParentType` that names a concept is written as `rdf:type`, and `ParentTerm` is written as `skos:broader`. `rdfs:subClassOf` is written only when `ParentType` is the token `sc`. Blood Type’s row is the named-concept case, so its taxonomy parent is `skos:broader` only. Core `PersonalData.csv` uses the `classes` schema. `SpecialCategoryPersonalData` there has `ParentType` `sc` and `ParentTerm` `dpv:SensitivePersonalData`, so that core class has both `rdfs:subClassOf` and `skos:broader` to Sensitive Personal Data.

The PD hook in `code/vocab_management.py`, title “Derive concepts as instances of Special Category PD”, inserts `rdf:type dpv:SpecialCategoryPersonalData` and `skos:inScheme pd:specialcategory-classes` wherever `skos:broader+ dpv:SpecialCategoryPersonalData`.

## Counts

Parsed with `rdflib` 7.6.0. See `results/report.txt`.

In `2.3/dpv/dpv.ttl`, classes with `skos:prefLabel`: 973. With `skos:broader`: 948. With `rdfs:subClassOf`: 195. Four `rdfs:subClassOf` edges have no matching `skos:broader` edge: `Law`, `Location`, `LocationFixture`, `PublicRegisterOfEntities`, each pointing at `rdfs:Class`. The other subclass edges repeat a broader target.

Across `dpv.ttl` and `pd.ttl` together, terms with a preferred label: 1,354 (1,204 classes, 150 properties). Class `skos:broader`: 1,179. Class `rdfs:subClassOf`: 195. The OWL pair has class `skos:broader` 0, class `rdfs:subClassOf` 1,183, `skos:broader` triples 0, `owl:subClassOf` triples 0. 1,179 + 4 = 1,183: the OWL rewrite copies `skos:broader` onto `rdfs:subClassOf` and keeps the four `rdfs:Class` edges. The copy is in `convert_owl_semantics` in `code/200_serialise_RDF.py`.

In `2.3/pd/pd.ttl` the special-category type, `skos:inScheme pd:specialcategory-classes`, and `skos:broader+ dpv:SpecialCategoryPersonalData` are the same 32 concepts. Direct `skos:broader dpv:SpecialCategoryPersonalData`: 11. The other 21 include `BloodType`.

`rdf:type dpv:PersonalData`: 229 concepts in `pd.ttl`. `skos:broader+ dpv:PersonalData`: 230. The extra concept is `pd:ProfessionalExperience`, whose only DPV type is `https://w3id.org/dpv/pd#PersonalData`. That IRI has no preferred label in 2.3 or `2.4-dev`. The broader path reaches `https://w3id.org/dpv#PersonalData`. `pd-extended.csv` has `ParentType` `pd:PersonalData` for that row.

## Worked example

`code/vocab_csv/pd-extended.csv` on `dev`:

- `BloodType`: `ParentTerm` `pd:MedicalHealth`, `ParentType` `dpv:PersonalData`
- `MedicalHealth`: `ParentTerm` `pd:External,dpv:SpecialCategoryPersonalData`, `ParentType` `dpv:PersonalData`

Published `pd:BloodType`:

```turtle
pd:BloodType a rdfs:Class, skos:Concept,
        dpv:PersonalData, dpv:SpecialCategoryPersonalData ;
    skos:broader pd:MedicalHealth ;
    skos:inScheme pd:extended-classes, pd:specialcategory-classes .
```

Shortest broader chain: Blood Type → Medical Health → Special Category Personal Data, and Medical Health → External → Personal Data. Special Category Personal Data continues to Sensitive Personal Data → Personal Data and Sensitive Data.

| Question on the RDFS+SKOS files | 2.3 and 2.4-dev |
| --- | --- |
| `rdf:type dpv:SpecialCategoryPersonalData` | true |
| direct `skos:broader` that category | false |
| `skos:broader+` that category | true |
| `rdfs:subClassOf+` that category | false |

On `pd-owl:BloodType` / `dpv-owl:SpecialCategoryPersonalData`: `rdf:type` true, `rdfs:subClassOf+` true, `skos:broader` false, `skos:inScheme` false. The unversioned IRIs are false.

The special-category type on Blood Type is the hook’s copy of the ancestor’s `ParentTerm`. It is not a second hierarchy. A rule that reads one `skos:broader` hop misses it. A rule that reads only `rdfs:subClassOf` in the RDFS file misses it. A rule that reads `skos:broader` in the OWL file misses it, because that predicate has been removed. The test that both published serialisations carry for the concept is `rdf:type` of the category IRI in that file’s namespace. That type sits on the concept. RDFS subclass entailment does not pass it on to an instance of `pd:BloodType`. In DPV-OWL, `rdfs:subClassOf` does. `results/report.txt` records that closure for 2.3 and `2.4-dev`.

`fixture/membership-rdfs.ttl` and `fixture/membership-owl.ttl` are excerpts of those published triples. `reproduce.py` checks that the fixture preserves the four RDFS answers and the OWL subclass path.

## Primer wording

Published primer section 4.2, table row “is subtype of”: RDFS cell `rdfs:subClassOf or skos:broader`, OWL cell `owl:subClassOf`. The same cells are in `primer/index.html` on `dev`. Section 4.3 already says extension uses `rdf:type` of the top concept and `skos:broader` for the hierarchy, and that DPV-OWL uses `rdfs:subClassOf`. The OWL example in section 4.2 uses `rdfs:subClassOf`. `guides/dpv-skos.html` on `master` contains neither `skos:broader` nor `rdfs:subClassOf`.

The DPV 2.3 specification, Semantics, already says taxonomies use `skos:broader` and that the OWL serialisation uses `rdfs:subClassOf`. Its table then names `owl:subClassOf` in the OWL column. The default column of that row already says `skos:broader`. Both tables are generated. The editable sources on `dev` are `code/jinja2_resources/template_dpv.jinja2` and `code/jinja2_resources/template_primer.jinja2`. `code/300_generate_HTML.py` writes the specification to the vocabulary directory and the primer to `primer/index.html` from `GUIDES` in `code/vocab_management.py`.

Change two cells, as in [COMMENT.md](COMMENT.md). Specification OWL cell of “subtype relation”: `rdfs:subClassOf`. Primer “is subtype of”: `skos:broader` and `rdfs:subClassOf`. Do not add a row. The instance row is already `rdf:type`. Put the Blood Type note under the primer table. Leave section 4.3 as it is.

`code/shacl_shapes/shapes.ttl` requires a preferred label on the object of `skos:broader`. It does not say which relation answers membership.

## Themes

Transparency and AI reliability. A policy or rule engine that walks the wrong predicate will classify `pd:BloodType` as ordinary personal data, or will miss it in the OWL file, while the vocabulary has recorded it as special-category data. The disclosure of the query is the requirement.

## Implementation

Adopters query `rdf:type` for the category recorded on the concept, and direct `skos:broader` for the parent, in the RDFS+SKOS file. In the OWL file they use the `owl` namespace, `rdf:type` for the category, and `rdfs:subClassOf` for the parent and for instance classification. The group edits the two Jinja templates and regenerates the HTML. No vocabulary term changes. The `pd:PersonalData` type on Professional Experience is a separate data error. This comment reports it so the membership rule is not overstated. It does not propose a spreadsheet edit for that row.

## 25 November 2026

The meeting is confirmed, 13:30–14:30 GMT, and it is not a viable place to introduce this item.

The 18 November minutes (`meetings/meeting-2026-11-18.html` on `689d32c0`) set the next meeting’s topics as v2.4, commits, IRI and parent changes, and the other items discussed that day: the v2.4 schedule check with Beatriz Esteves, AI Act proposal 001, AI quality proposal 002, Tytti Rintamaki’s DPIA and FRIA concepts, the note-taking tool, and namespace documentation ([#492](https://github.com/w3c-cg/dpv/issues/492)). Membership documentation is not among them. The public event page has not been updated to that list. Its agenda is still the 18 November text, including “Mailing List: No new updates”. Joining instructions are login-restricted. This project must not mail the list or the chairs to ask for time.

The comment stands on its own. If someone later wants a call about `rdf:type` versus the special-category hook, that is after the comment, on a meeting whose agenda has room for it.

## AI-assistance requirements

Read:

- [contributing.md](https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/contributing.md), which points at the wiki.
- [Contribution Guide](https://github.com/w3c-cg/dpv/wiki/Contribution-Guide), wiki date shown as 12 February 2026. It does not mention AI tools.
- [Draft policy on AI tools in W3C standardization](https://www.w3.org/2026/10/draft-ai-policy.html). The page says it is not yet a W3C policy. The draft requires a human to review and own the contribution, to label substance an AI tool produced, to answer review in person, and to avoid high-volume generated comments. The Advisory Board document it names was not retrieved.

There is no DPVCG-specific AI rule in the files read. The comment still carries a disclosure line, because the draft asks for one and because an AI tool drafted the substance. Before posting, a person re-runs `reproduce.py`, checks every quotation against the cited file, replaces nothing in the technical sentences, and keeps the disclosure. That person answers any reply. Do not post from an automated account. Do not send a follow-up comment if the first one has no reply.

## Submission

Do not send anything until this specific comment is approved.

1. Re-read [#484](https://github.com/w3c-cg/dpv/issues/484). If it has new comments, stop and revise.
2. From `contributions/T003-DPV-Membership/`, create a virtual environment, `pip install -r requirements.txt`, and run `python reproduce.py`. Compare the console with `results/report.txt`.
3. Paste [COMMENT.md](COMMENT.md) as a comment on issue #484, from the reviewer’s own GitHub account. Keep the disclosure. Sign the human’s name in that line.
4. Do not open a pull request. Do not edit `primer/index.html`, generated HTML, RDF, or `code/vocab_csv` in a pull request. The contribution guide says to discuss first, forbids pull requests that edit generated HTML or RDF, and says term changes belong in the spreadsheet or in an issue. This item is documentation, discussed on the existing help-wanted issue.
5. Do not mail `public-dpvcg@w3.org` and do not contact the chairs about the 25 November call.
6. A GitHub comment on this repository is a contribution under the license the group applies to repository contributions. The README links the [W3C Software and Document License](https://www.w3.org/copyright/software-license-2023/). The poster is responsible for that.

Record a later submission only in `MASTER_TRACKER.md` and `evidence/` after it has actually been sent.

## Sources

- Issue #484, body fetched 18 November 2026.
- Files at the two commits above, checksums in `results/report.txt`.
- `code/vocab_funcs.py` `construct_parent` and `construct_parent_taxonomy`.
- `code/vocab_schemas.py` and the `pd` / `dpv` entries in `code/vocab_management.py`.
- `code/vocab_csv/pd-extended.csv` and `code/vocab_csv/PersonalData.csv` on `dev`.
- `code/200_serialise_RDF.py` OWL rewrite of `skos:broader`.
- `code/shacl_shapes/shapes.ttl`.
- Primer section 4.2 and 4.3 on `master` `primer/index.html`, and the same table cells on `dev`.
- DPV 2.3 specification, Semantics, `2.3/dpv/index.html` on `master`, and the same subtype row in `2.4-dev/dpv/index.html`.
- `code/jinja2_resources/template_dpv.jinja2` and `template_primer.jinja2` on `dev`, rendered by `code/300_generate_HTML.py`.
- `guides/dpv-skos.html` on `master`: no matches for `skos:broader`, `rdfs:subClassOf`, or `owl:subClassOf`.
- SKOS Reference, RDF Schema 1.1, and the OWL 2 RDF mapping, sections cited above.
- 18 November minutes and the 25 November event page, URLs in the meeting section.
- November 2026 public-list index: https://lists.w3.org/Archives/Public/public-dpvcg/2026Nov/

## Not verified

- The online spreadsheets. The repository CSV export was read. It can lag the sheet.
- An OWL reasoner. The subclass results are SPARQL property paths over asserted triples, plus the RDFS specification of what `rdfs:subClassOf` means. They are not a reasoner trace.
- An OWL tableau reasoner. The instance result in `results/report.txt` applies RDFS rules rdfs11 and rdfs9 to asserted `rdfs:subClassOf` triples. `primer/index.html` is generated, from `template_primer.jinja2`, by `code/300_generate_HTML.py`.
- W3C login, so the 25 November join link was not visible.
- The Advisory Board LLM document named by the draft AI policy.
- HTML other than the primer, the SKOS guide, and the files named above.

## Reproduce

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python reproduce.py
```

The script downloads the pinned Turtle files into `cache/` on first run. No model API is called. `rdflib==7.6.0`.
