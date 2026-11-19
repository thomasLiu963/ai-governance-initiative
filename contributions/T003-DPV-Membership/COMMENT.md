The three relations answer different questions. For the concept itself, the category DPV records is `rdf:type`. The direct parent is `skos:broader` in the RDFS+SKOS files and `rdfs:subClassOf` in DPV-OWL. A single `skos:broader` hop does not answer category membership. `rdfs:subClassOf` is transitive. In the RDFS+SKOS files it is not the taxonomy.

Checked on DPV 2.3, commit `689d32c0` (`2.3/dpv/dpv.ttl`, `2.3/pd/pd.ttl`, `2.3/dpv/dpv-owl.ttl`, `2.3/pd/pd-owl.ttl`), and on `2.4-dev`, commit `aff91c29`. The two `2.4-dev` OWL files are byte-identical to the 2.3 OWL files. The RDFS+SKOS files differ, and the Blood Type answers below are the same on both. In `2.3/dpv/dpv.ttl`, 973 classes with a `skos:prefLabel` include 948 with `skos:broader` and 195 with `rdfs:subClassOf`. For 191 of those 195, every `rdfs:subClassOf` target is also a `skos:broader` target. The other four, `Law`, `Location`, `LocationFixture`, and `PublicRegisterOfEntities`, are only `rdfs:subClassOf rdfs:Class`. The issue’s “~95% / ~18%” does not name a denominator. Neither serialisation uses `owl:imports`. `owl:subClassOf` occurs in neither file. OWL 2 writes a subclass axiom as `rdfs:subClassOf` (https://www.w3.org/TR/owl2-mapping-to-rdf/#Mapping_from_the_Structural_Specification_to_RDF_Graphs).

What each predicate means here:

- `rdf:type` says the resource is an instance of a class (https://www.w3.org/TR/rdf-schema/#ch_type). DPV uses it for the category named in the spreadsheet `ParentType`.
- `skos:broader` is a direct hierarchical link. SKOS does not declare it transitive (https://www.w3.org/TR/skos-reference/, sections 8.1 and 8.6.6). A path of several hops is an application query. It is not a SKOS entailment, and the files do not import the SKOS axioms that would infer `skos:broaderTransitive`.
- `rdfs:subClassOf` means every instance of the subject class is an instance of the object class, and it is transitive (https://www.w3.org/TR/rdf-schema/#ch_subclassof). The classes schema writes it when `ParentType` is the token `sc`. In the taxonomy schema, a `ParentType` that names a concept is written as `rdf:type`, and `ParentTerm` is written as `skos:broader`.
- `skos:inScheme` puts a concept in a concept scheme. A hierarchical link does not entail scheme membership (SKOS Reference, section 4.6.4). The OWL serialisation deletes `skos:inScheme`.

`pd:BloodType` in `2.3/pd/pd.ttl` and in `2.4-dev/pd/pd.ttl`:

- `rdf:type dpv:PersonalData` and `dpv:SpecialCategoryPersonalData`
- `skos:broader pd:MedicalHealth`
- `skos:inScheme pd:extended-classes, pd:specialcategory-classes`
- no `rdfs:subClassOf`

`pd:MedicalHealth` has `skos:broader pd:External, dpv:SpecialCategoryPersonalData`. One hop stops at Medical Health. The path `skos:broader+` reaches `dpv:SpecialCategoryPersonalData`. In `code/vocab_csv/pd-extended.csv` on `dev`, Blood Type’s `ParentType` is `dpv:PersonalData` and its `ParentTerm` is `pd:MedicalHealth`. Medical Health’s `ParentTerm` is `pd:External,dpv:SpecialCategoryPersonalData`. The extra `rdf:type dpv:SpecialCategoryPersonalData` and `skos:inScheme pd:specialcategory-classes` are written by the PD export hook “Derive concepts as instances of Special Category PD” in `code/vocab_management.py`, whose `WHERE` is `skos:broader+ dpv:SpecialCategoryPersonalData`. In published `2.3/pd/pd.ttl` the type, the scheme, and that path are the same 32 concepts. Eleven are direct children. Blood Type is one of the other twenty-one.

On the RDFS+SKOS graph, in 2.3 and in `2.4-dev`: type true, direct broader false, broader path true, `rdfs:subClassOf+` false. On the OWL graph the IRIs are `pd-owl:BloodType` and `dpv-owl:SpecialCategoryPersonalData` (`https://w3id.org/dpv/pd/owl#` and `https://w3id.org/dpv/owl#`). Type is true, `rdfs:subClassOf+` is true, `skos:broader` and `skos:inScheme` are absent, and the unversioned `dpv:` / `pd:` IRIs do not match. The same OWL answers hold for 2.3 and `2.4-dev`.

That `rdf:type` is on the concept. `pd:BloodType` has no `rdfs:subClassOf` path to the category in the RDFS+SKOS files, so RDFS subclass entailment does not make an instance of `pd:BloodType` an instance of `dpv:SpecialCategoryPersonalData`. In DPV-OWL the `rdfs:subClassOf` chain does, on the `owl` IRIs. This is `rdfs:subClassOf` transitivity and the subclass instance rule applied to the asserted triples. It is not a separate OWL reasoner.

Suggested test:

1. RDFS+SKOS. The category recorded on the concept is `rdf:type` of that category IRI. The direct taxonomy parent is `skos:broader`. For special-category data, `pd:specialcategory-classes` currently matches that type because the hook copies the broader path into both. The copy is absent from the OWL file.
2. DPV-OWL. Use the `owl` IRIs. The category recorded on the concept is `rdf:type`. The taxonomy parent, and the relation that classifies instances, is `rdfs:subClassOf`.

One published exception to treating every type IRI as a category: `pd:ProfessionalExperience` is `rdf:type https://w3id.org/dpv/pd#PersonalData`, and that object has no `skos:prefLabel`. Its broader path does reach `https://w3id.org/dpv#PersonalData`. This is the only such type IRI in `pd.ttl`, in 2.3 and in `2.4-dev`. The `ParentType` cell in `pd-extended.csv` is `pd:PersonalData`.

The specification already states the rule in prose. DPV 2.3, Semantics, says taxonomies are instances of a top concept related by `skos:broader`, and that the OWL serialisation uses `rdfs:subClassOf` instead of `skos:broader`. The table in that section then gives the OWL subtype relation as `owl:subClassOf`. That cell is in `code/jinja2_resources/template_dpv.jinja2` on `dev`. The default column of the same row already says `skos:broader`. Primer section 4.3 tells adopters to extend a concept with `rdf:type` of the top concept and `skos:broader` for the hierarchy, and to use `rdfs:subClassOf` in DPV-OWL. The OWL example in section 4.2 uses `rdfs:subClassOf`. The section 4.2 table says the subtype relation is `rdfs:subClassOf or skos:broader` and that DPV-OWL uses `owl:subClassOf`. That table is in `code/jinja2_resources/template_primer.jinja2`. Both HTML pages are generated from those templates. The same two cells are in the published 2.3 HTML and in the `2.4-dev` HTML.

The existing instance row is already `rdf:type`. Suggested change, with no new row:

- Specification table, OWL cell of “subtype relation”: `rdfs:subClassOf`.
- Primer table, “is subtype of”: `skos:broader` in the DPV column and `rdfs:subClassOf` in the DPV-OWL column.

Note under the primer table: `skos:broader` is the direct parent. It is not transitive. For `pd:BloodType`, special-category membership of the concept is `rdf:type dpv:SpecialCategoryPersonalData`. The direct parent is `pd:MedicalHealth`. One hop does not reach the category. The RDFS+SKOS file has no `rdfs:subClassOf` path, so subclass entailment does not classify an instance of `pd:BloodType` as special-category data. In DPV-OWL, use `pd-owl:BloodType` and `dpv-owl:SpecialCategoryPersonalData`. There, `rdfs:subClassOf` does reach the category and does classify instances.

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

On the 2.3 and `2.4-dev` RDFS+SKOS files this returns true, false, true, false. I have not opened the online spreadsheet. This is a note on the existing issue. The wording is for the group to apply in the two templates. I am not proposing a pull request against the generated HTML or RDF.

Disclosure: an AI tool drafted this comment. I checked the files and the query, and I am responsible for the text.
