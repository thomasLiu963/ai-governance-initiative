The three relations are different tests. A single `skos:broader` hop does not answer category membership.

Checked on DPV 2.3, commit `689d32c0` (`2.3/dpv/dpv.ttl`, `2.3/pd/pd.ttl`, `2.3/dpv/dpv-owl.ttl`, `2.3/pd/pd-owl.ttl`), and the same BloodType questions on `2.4-dev`, commit `aff91c29`. In `2.3/dpv/dpv.ttl`, 973 classes with a `skos:prefLabel` include 948 with `skos:broader` and 195 with `rdfs:subClassOf`. For 191 of those 195, every `rdfs:subClassOf` target is also a `skos:broader` target. The other four, `Law`, `Location`, `LocationFixture`, and `PublicRegisterOfEntities`, are only `rdfs:subClassOf rdfs:Class`. The issue’s “~95% / ~18%” does not name a denominator. Neither serialisation `owl:imports` SKOS or OWL. `owl:subClassOf` occurs in neither file. OWL 2 writes a subclass axiom as `rdfs:subClassOf` (https://www.w3.org/TR/owl2-mapping-to-rdf/#Mapping_from_the_Structural_Specification_to_RDF_Graphs).

What each predicate means here:

- `rdf:type` says the resource is an instance of a class (https://www.w3.org/TR/rdf-schema/#ch_type). DPV uses it for the top category named in the spreadsheet `ParentType`.
- `skos:broader` is a direct hierarchical link. SKOS does not declare it transitive (https://www.w3.org/TR/skos-reference/, sections 8.1 and 8.6.6). A path of several hops is an application query. It is not a SKOS entailment, and the files do not import the SKOS axioms that would infer `skos:broaderTransitive`.
- `rdfs:subClassOf` means every instance of the subject class is an instance of the object class, and it is transitive (https://www.w3.org/TR/rdf-schema/#ch_subclassof). The RDFS+SKOS generator writes it when `ParentType` is the token `sc`. Taxonomy parents are `skos:broader` only.
- `skos:inScheme` puts a concept in a concept scheme. A hierarchical link does not entail scheme membership (SKOS Reference, section 4.6.4). The OWL serialisation deletes `skos:inScheme`.

`pd:BloodType` in `2.3/pd/pd.ttl`:

- `rdf:type dpv:PersonalData` and `dpv:SpecialCategoryPersonalData`
- `skos:broader pd:MedicalHealth`
- `skos:inScheme pd:extended-classes, pd:specialcategory-classes`
- no `rdfs:subClassOf`

`pd:MedicalHealth` has `skos:broader pd:External, dpv:SpecialCategoryPersonalData`. One hop stops at Medical Health. The path `skos:broader+` reaches `dpv:SpecialCategoryPersonalData`. In `code/vocab_csv/pd-extended.csv` on `dev`, Blood Type’s `ParentType` is only `dpv:PersonalData`, and Medical Health’s `ParentTerm` is `pd:External,dpv:SpecialCategoryPersonalData`. The extra `rdf:type dpv:SpecialCategoryPersonalData` and `skos:inScheme pd:specialcategory-classes` are written by the PD export hook “Derive concepts as instances of Special Category PD” in `code/vocab_management.py`, whose `WHERE` is `skos:broader+ dpv:SpecialCategoryPersonalData`. In published `2.3/pd/pd.ttl` the type, the scheme, and that path are the same 32 concepts. Eleven are direct children. Blood Type is one of the other twenty-one.

The same four questions on the RDFS+SKOS graph, in 2.3 and in `2.4-dev`, are: type true, direct broader false, broader path true, `rdfs:subClassOf+` false. On the OWL graph the IRIs are `pd-owl:BloodType` and `dpv-owl:SpecialCategoryPersonalData` (`https://w3id.org/dpv/pd/owl#` and `https://w3id.org/dpv/owl#`). Type is true, `rdfs:subClassOf+` is true, `skos:broader` and `skos:inScheme` are absent, and the unversioned `dpv:` / `pd:` IRIs do not match.

Suggested test:

1. RDFS+SKOS. Category membership that the vocabulary records on the concept is `rdf:type` of the declared category IRI. The direct taxonomy parent is `skos:broader`. For special-category data, the published scheme `pd:specialcategory-classes` currently matches that type because the hook copies the broader path into both. The copy is not in the OWL file. `rdfs:subClassOf` is not the taxonomy in this serialisation.
2. DPV-OWL. Use the `owl` IRIs. Category membership is `rdf:type`. The taxonomy parent is `rdfs:subClassOf`.

One published exception to treating every type IRI as the category: `pd:ProfessionalExperience` is `rdf:type https://w3id.org/dpv/pd#PersonalData`, and that object has no `skos:prefLabel`. Its broader path does reach `https://w3id.org/dpv#PersonalData`. This is in 2.3 and in `2.4-dev`. The `ParentType` cell in `pd-extended.csv` is `pd:PersonalData`.

Primer section 4.3 already tells adopters to extend a concept with `rdf:type` of the top concept and `skos:broader` for the place in the hierarchy, and to use `rdfs:subClassOf` in DPV-OWL. The section 4.2 table, in the published primer and in `primer/index.html` on `dev`, says the subtype relation is `rdfs:subClassOf or skos:broader` and that DPV-OWL uses `owl:subClassOf`. Suggested replacement for that row, and one added row:

| Concept | DPV | DPV-OWL |
| --- | --- | --- |
| is subtype of (direct parent) | `skos:broader` | `rdfs:subClassOf` |
| is in a top category | `rdf:type` | `rdf:type` |

Note to put under the table: `skos:broader` is the direct parent. It is not transitive, and it is not `rdfs:subClassOf`. In the RDFS+SKOS files, `rdfs:subClassOf` is not the taxonomy. In DPV-OWL the taxonomy is `rdfs:subClassOf` in the `owl` namespace. For `pd:BloodType`, special-category membership is `rdf:type dpv:SpecialCategoryPersonalData`. The direct parent is `pd:MedicalHealth`, whose own parent list includes the category.

```sparql
PREFIX pd: <https://w3id.org/dpv/pd#>
PREFIX dpv: <https://w3id.org/dpv#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT
  (EXISTS { pd:BloodType a dpv:SpecialCategoryPersonalData } AS ?type)
  (EXISTS { pd:BloodType skos:broader dpv:SpecialCategoryPersonalData } AS ?direct)
  (EXISTS { pd:BloodType skos:broader+ dpv:SpecialCategoryPersonalData } AS ?path)
  (EXISTS { pd:BloodType rdfs:subClassOf+ dpv:SpecialCategoryPersonalData } AS ?subclass)
WHERE {}
```

On the 2.3 and `2.4-dev` RDFS+SKOS files this returns true, false, true, false. I have not opened the online spreadsheet. This is a note on the existing issue. The primer wording is for the group to apply. I am not proposing a pull request against the generated HTML or RDF.

Disclosure: an AI tool drafted this comment. I checked the files and the query, and I am responsible for the text.
