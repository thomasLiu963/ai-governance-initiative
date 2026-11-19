The parent should be `dpv:FulfilmentOfObligation`. That is the change already recorded on 9 September, and it is still unapplied.

`dpv:RightsFulfilment` is a `dpv:Purpose` in `dpv:purposes-classes`, and its `skos:broader` is `dpv:LegalObligation`. `dpv:LegalObligation` is a `dpv:LegalBasis` in `dpv:legal-basis-classes`. Its definition is “Legal Obligation to conduct the specified activities”. The same parent is in published 2.3 (`2.3/dpv/modules/purposes.ttl`, commit `689d32c0`) and in `2.4-dev` (`2.4-dev/dpv/modules/purposes.ttl` and `code/vocab_csv/Purpose.csv`, commit `aff91c29`). The spreadsheet columns are `ParentTerm` `dpv:LegalObligation` and `ParentType` `dpv:Purpose`. I have not opened the online sheet.

On this issue, @besteves4 named `dpv:FulfilmentOfObligation` or `dpv:LegalCompliance`. The same day’s minutes, with Beatriz present, record two actions: change the parent to `dpv:FulfilmentOfObligation`, and update the purpose-module description and examples. https://github.com/w3c-cg/dpv/blob/689d32c0f7c571d32f7f8635ae548fcc1c3ff695/meetings/meeting-2026-09-09.html#a01 Harsh’s minuted reason is: “dpv:RightsFulfilment should have as parent dpv:FulfilmentOfObligation because rights may not be legal obligations.” The minutes attribute to Georg the clarification that this branch is fulfilment where a bearer and a condition exist, with fulfilment of obligation as the parent and rights fulfilment as one kind of that fulfilment. No later minutes file mentions `RightsFulfilment`.

`dpv:LegalCompliance` would undo that choice. Its definition is “Purposes associated with carrying out data processing to fulfill a legal or statutory obligation”, and its scope note says it is used for processing additionally required by a law and will typically be used with Legal Obligation as the legal basis. It is itself a child of `dpv:FulfilmentOfObligation`. Putting rights fulfilment under it would make “rights specified in law” a kind of legal-compliance purpose and would keep the legal-basis coupling the meeting separated. Immediately after the action, Harsh said purpose and legal basis are different: the purpose says what is done with the data, and the legal basis says where the requirement comes from in law.

`dpv:FulfilmentOfObligation` is “Purposes associated with carrying out data processing to fulfill an obligation”, typed `dpv:Purpose`, with `skos:broader dpv:Purpose`. Its other children are `dpv:FulfilmentOfContractualObligation`, `dpv:LegalCompliance`, and `dpv:ProtectionOfIPR`. Protection of IPR was created on the same date as Rights Fulfilment and is already under Fulfilment of Obligation. Rights Fulfilment has no `skos:broader` children in any Turtle file on `dev`. The scope note does not fold non-legal activities into the concept. It says that where an activity also includes something that is not a legal obligation, such as identity verification, that part is recorded as a separate purpose. Section 4 of the purposes module already does that for KYC: the purpose is broader than identity verification and legal compliance, and `dpv:hasLegalBasis` points at `dpv:LegalObligation`.

Two current consequences of the legal-basis parent:

- In `2.3/dpv/dpv-owl.ttl`, `dpv-owl:RightsFulfilment` is `rdf:type dpv-owl:Purpose` and `rdfs:subClassOf dpv-owl:LegalObligation`, so `rdfs:subClassOf+ dpv-owl:LegalBasis`. Under RDFS, every instance of that class is a legal basis (https://www.w3.org/TR/rdf-schema/#ch_subclassof). `dpv-owl:Purpose` itself has no `rdfs:subClassOf` path to `dpv-owl:LegalBasis`. The OWL file has no `owl:disjointWith` triple.
- The generated purposes page lists Rights Fulfilment as an object of `dpv:hasLegalBasis` and does not list `dpv:hasPurpose`. Legal Compliance and Fulfilment of Obligation are listed under `dpv:hasPurpose`. The same rows are in the `2.4-dev` page. `dpv:hasLegalBasis` has `dcam:rangeIncludes dpv:LegalBasis`. `dpv:hasPurpose` has `dcam:rangeIncludes dpv:Purpose`.

Please change `ParentTerm` in the Purpose sheet from `dpv:LegalObligation` to `dpv:FulfilmentOfObligation` and leave `ParentType` as `dpv:Purpose`. Regeneration then moves the OWL subclass off `LegalBasis` and the HTML row onto `hasPurpose`. I am not proposing a pull request against the CSV, the Turtle, or the HTML.

The 18 November minutes put parent changes on the 25 November agenda. This parent was chosen on 9 September, so it can be applied with that pass.

The module description still lists only Fulfilment of Contractual Obligation, Legal Compliance, and Protection of IPR under Fulfilment of Obligation. The second action is to add Rights Fulfilment to that list and to keep any legal basis on `hasLegalBasis`. `dpv:OrganisationComplianceManagement` points external legal compliance at `dpv:LegalCompliance`. That scope note should stay on organisational compliance. It is not a reason to parent rights fulfilment there, or under Legal Compliance.

Guard for the next parent of this kind:

```sparql
PREFIX dpv: <https://w3id.org/dpv#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?purpose ?parent WHERE {
  ?purpose a dpv:Purpose ; skos:broader ?parent .
  FILTER (?parent != dpv:Purpose)
  FILTER NOT EXISTS { ?parent a dpv:Purpose }
}
```

On `2.3/dpv/dpv.ttl` and on `2.4-dev/dpv/dpv.ttl` the only row is `dpv:RightsFulfilment` / `dpv:LegalObligation`. `code/shacl_shapes/shapes.ttl` checks that a `skos:broader` target has a `skos:prefLabel`. Legal Obligation has a label, so the shape accepts this parent.

Disclosure: an AI tool drafted this comment. I checked the files, the minutes, and the query, and I am responsible for the text.
