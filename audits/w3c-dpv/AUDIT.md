# W3C DPV audit

Audit date: 18 November 2026. Authoritative sources read: the [DPVCG repository](https://github.com/w3c-cg/dpv) (`master` and `dev`), the [community group page](https://www.w3.org/groups/cg/dpvcg/), the [contribution guide](https://github.com/w3c-cg/dpv/wiki/Contribution-Guide) (wiki date 12 February 2026), the public list archive for November 2026, and the published DPV 2.3 pages. No pull request, issue, message, or external commit was sent. No paid API calls were made.

`research/D1/`, `research/D2/`, and `research/incident-evidence/` are not in this workspace. No local D1, D2, or incident finding is available to support a candidate.

## Recommendation

Prepare two internal drafts before 30 November 2026, and hold them for explicit approval before anything is posted.

1. A short membership-test note for help-wanted issue [#484](https://github.com/w3c-cg/dpv/issues/484). This is the best external path: the issue is unassigned, labeled `help-wanted` and `todo`, and has no comments. The note should correct the primer’s hierarchy table and give one worked test, using `pd:BloodType`.
2. A parent recommendation for [#486](https://github.com/w3c-cg/dpv/issues/486), plus a SPARQL check that a purpose’s `skos:broader` target is itself a purpose. Chair Beatriz Esteves already confirmed the defect on 9 September 2026. It is still present in published 2.3 and in `dev` `2.4-dev`.

Treat [#500](https://github.com/w3c-cg/dpv/issues/500) as a third, smaller draft: one generator correction for `rdfs:Label`, after separating that defect from metadata the generator writes on purpose. Do not lead on [#465](https://github.com/w3c-cg/dpv/issues/465), [#451](https://github.com/w3c-cg/dpv/issues/451), or [#482](https://github.com/w3c-cg/dpv/issues/482). Those threads already have authors, a draft in the repository, or no maintainer response, and the 18 November meeting put AI quality on the 25 November agenda under its existing proposal.

Post only as a GitHub comment on the existing issue. The contribution guide says to discuss before a pull request, and it forbids pull requests that edit generated HTML, RDF, or the exported CSVs.

## What DPV is

[DPV 2.3](https://w3c-cg.github.io/dpv/2.3/dpv/) is a Final Community Group Report, 25 February 2026, published by the Data Privacy Vocabularies and Controls Community Group. The specification states that it is not a W3C Standard and is not on the W3C Standards Track. The versionless IRI `https://w3id.org/dpv` points at the latest release. Serialisations are RDFS+SKOS (default) and OWL2 (separate namespace).

`dev` contains `2.4-dev` and a `proposals/` directory. The open milestone [dpv v2.4](https://github.com/w3c-cg/dpv/milestone/10) still has due date 31 July 2026 and 77 open issues. That due date is stale relative to the 18 November minutes: the chair proposed December finalisation of whatever is ready, a January beta, and a final release at the end of January, and said he would check that plan with Beatriz Esteves. That schedule is a proposal recorded in the minutes, not a minuted resolution.

Chairs, from the [group page](https://www.w3.org/groups/cg/dpvcg/): Beatriz Esteves and Harshvardhan J. Pandit. GitHub account `besteves4` authored the pull request “add website for Beatriz Esteves”. Account `coolharsh55` writes the chair’s technical comments and is the account the minutes’ chair actions match. This audit did not open GitHub profile pages.

## Named issues

| Issue | State on 18 Nov 2026 | Assignee | Last activity | Reading |
| --- | --- | --- | --- | --- |
| [#484](https://github.com/w3c-cg/dpv/issues/484) membership test | Open. Labels `todo`, `help-wanted`. Milestone none. | None | Opened 27 Aug 2026. Zero comments. | Genuine. Unassigned. |
| [#465](https://github.com/w3c-cg/dpv/issues/465) AI quality | Open. Milestone `proposed-work`. | None | Comment 23 Sep 2026 points at published DQV4AI taxonomies. | Already a group proposal. On the 25 Nov agenda. |
| [#451](https://github.com/w3c-cg/dpv/issues/451) AI output use | Open. Labels `WIP`, `AI`, `eu-aiact`. Milestone `proposed-work`. | None | Chair summary 27 May 2026; proposer agreed the same day; chair note 28 Jun 2026 on EU labelling icons. | Terms agreed in the thread. Not in 2.3 or `2.4-dev`. |
| [#482](https://github.com/w3c-cg/dpv/issues/482) active/passive rights | Open. No labels. | None | Opened 5 Aug 2026. Zero comments. | Gap is real. No maintainer reply. Not in the 18 Nov plan. |

## Contribution route and AI-assistance policy

Route, from [contributing.md](https://github.com/w3c-cg/dpv/blob/master/contributing.md) and the [wiki guide](https://github.com/w3c-cg/dpv/wiki/Contribution-Guide):

- Membership is not required to comment or open an issue. Decisions are taken in the group’s meetings. The public list is `public-dpvcg@w3.org`.
- Discuss a proposal before sending code. Attribution can be `Co-authored-by` without a pull request.
- Pull requests target `dev`, not `master`.
- Do not edit generated HTML or RDF. Do not edit CSVs under the vocabulary export; those mirror online spreadsheets. A change to a term belongs in the spreadsheet, or in an issue if the contributor has no spreadsheet access.
- A new term needs a name, description, class or property, relation to an existing term, source, and justification, and it should follow the style guide at `code/style-guide.md` on `dev`.
- Large non-authoritative donations are gated by five questions: openness, why DPVCG, scope, relation to existing work, and who will maintain it.
- Work in the repository is under the [W3C Document License](https://www.w3.org/copyright/software-license-2023/) unless noted. The README names that document license and links to the software-license URL. The generator on `dev` writes `https://www.w3.org/copyright/document-license-2023/`. This audit did not resolve which URL the group intends.

AI assistance: the DPV contribution guide does not mention AI tools. The W3C text at <https://www.w3.org/2026/10/draft-ai-policy.html> is labeled a draft and says it is not yet a W3C policy. If that draft is later adopted, a human must review and own the contribution, disclose substance produced by an AI tool, reply to review in person, and avoid high-volume generated comments. The draft names an Advisory Board document, “Use of Large Language Models in Standards Work”. That document was not retrieved. There is no DPVCG-specific AI rule in the files read here.

Practical consequence for this project: any external comment should be short, written against a named file or issue, and disclosed as AI-assisted if a tool drafted the substance. A generated vocabulary or a long mapping dump is a poor fit for both the DPV guide and the draft W3C text.

## How review actually happens

GitHub “review” events are sparse. First response is usually an issue comment, and several pull requests were closed after the chair copied the change into his own commit. Acceptance odds cannot be read off merged pull requests alone. Sample, bounded to public GitHub records:

| Item | Opened | First public response | Disposition | Role |
| --- | --- | --- | --- | --- |
| [PR #435](https://github.com/w3c-cg/dpv/pull/435) GDNG lawfulness module, `nuthub`, +17497/−4881, 51 files, base `dev` | 11 Feb 2026 | `coolharsh55` comment 12 Feb 2026. No review object. | Merged 15 Feb 2026. | Repeat contributor. Large generated diff. |
| [PR #459](https://github.com/w3c-cg/dpv/pull/459) DPV-ODRL guide, `besteves4` | 11 Mar 2026 | `coolharsh55` comment 11 Mar 2026, about 2 hours later. | Merged 23 Mar 2026. | Chair account. |
| [PR #409](https://github.com/w3c-cg/dpv/pull/409) homepage typos, `bact` | 7 Dec 2025 | Approving review by `coolharsh55` 2 Feb 2026. | Merged 2 Feb 2026, the same minute as the approval. | External/regular contributor. Waited about eight weeks. |
| [PR #376](https://github.com/w3c-cg/dpv/pull/376) example terms, `bact` | 21 Aug 2025 | No review and no comment on the pull request. | Merged 24 Aug 2025. | Same contributor. |
| [PR #254](https://github.com/w3c-cg/dpv/pull/254) East and Southeast Asian legal concepts, `bact` | 20 Mar 2025 | `coolharsh55` 22 Mar 2025: changes added manually in another commit. | Closed 22 Mar 2025, not merged. Author agreed. | Incorporated without merging the pull request. |
| [PR #86](https://github.com/w3c-cg/dpv/pull/86) “Invisible processing”, `JonathanBowker` | 4 Feb 2023 | `coolharsh55` 5 Feb 2023: discuss first; open an issue rather than a pull request. | Closed unmerged 5 Feb 2023. | One-off pull request without a prior issue. |
| [PR #358](https://github.com/w3c-cg/dpv/pull/358) script for terms without examples, `bact` | 14 Aug 2025 | `coolharsh55` comment the same day. | Still open. 18 Nov minutes: look at it after the issue backlog. | Deferred by the chair, not rejected. |
| [PR #483](https://github.com/w3c-cg/dpv/pull/483) ISO 12792 numbers, `FabianLinde` | 20 Aug 2026 | No comment and no review as of this audit. | Still open. 18 Nov minutes: can be merged. | Meeting participant. Small diff (18/5, 1 file). |
| [PR #470](https://github.com/w3c-cg/dpv/pull/470) stale CSVs, `bact` | 8 Apr 2026 | No comment. | Still open. 18 Nov minutes: chair will look in December. | Deferred. |

The 18 November minutes identify two open pull requests “from Art” as the cosmetic diagram change and the CSV cleanup, and a third open pull request as Fabian’s number correction. `bact` is the author of the CSV pull request and of the examples-script pull request. This audit did not open a profile to confirm the personal name.

Recent merged pull requests visible in the latest thirty updates are mostly documentation, typos, and maintainer or repeat-contributor work. That sample does not show a newcomer landing a new taxonomy in a few days.

## Agenda access

The weekly series runs through 16 December 2026, 13:30–14:30 Europe/Dublin ([event series](https://www.w3.org/events/meetings/65197685-0e2b-44a1-b715-280dc3af0582/)). The 11 November occurrence was cancelled; the notice is on the public list: <https://lists.w3.org/Archives/Public/public-dpvcg/2026Nov/0002.html>.

The 18 November agenda was public in the calendar mail before the call: <https://lists.w3.org/Archives/Public/public-dpvcg/2026Nov/0003.html>. Topics included the v2.4 plan, maintenance, past minutes, EHDS/GDNG, the Data Act, and triage of new GitHub errors. Joining instructions in that mail are restricted to logged-in W3C users. This audit could not see the call link.

Minutes for that meeting are in the repository: [`meetings/meeting-2026-11-18.html`](https://github.com/w3c-cg/dpv/blob/master/meetings/meeting-2026-11-18.html). They record the next meeting as 25 November 2026, with v2.4 commits, IRI and parent changes, AI Act documentation proposal `001`, AI quality proposal `002`, Tytti Rintamaki’s DPIA/FRIA concepts, the note-taking tool, and namespace documentation ([#492](https://github.com/w3c-cg/dpv/issues/492)). As of the list archive fetched on 18 November (last message 14:02 UTC), no agenda mail for 25 November had been posted. Call details for that meeting are not publicly visible without a W3C login.

The chair asked for volunteers on the error backlog and said he will comment proposed resolutions on the issues and make the v2.4 commits himself. A parallel pull request that regenerates the same files is likely to collide with that plan.

## Local checks

Files read from `master` tag content for DPV 2.3, and from `dev` for `2.4-dev`, `code/200_serialise_RDF.py`, `code/shacl_shapes/shapes.ttl`, and `proposals/`. Hierarchy counts are lexical: Turtle blocks split on blank lines, not an RDF parse. `rdflib` is not installed here, and it was not installed for this audit. Exact triples quoted below were read from the files.

**RDFS serialisation, `2.3/dpv/dpv.ttl`.** 973 blocks typed `rdfs:Class`. 948 (97.4%) have `skos:broader`. 195 have `rdfs:subClassOf`. For 191 of those, the `subClassOf` targets equal the `broader` targets. The other four are only `rdfs:subClassOf rdfs:Class`: `dpv:Law`, `dpv:Location`, `dpv:LocationFixture`, `dpv:PublicRegisterOfEntities`. Counting classes and properties together (1123 blocks) gives broader on 90.6% and `subClassOf` on 17.4%. Issue #484’s “~95% / ~18%” matches the order of magnitude. It is not an exact figure, and the issue does not state the denominator.

**The two hierarchies are different relations.** `pd:BloodType` in `2.3/pd/pd.ttl` is typed `dpv:PersonalData` and `dpv:SpecialCategoryPersonalData`, and its `skos:broader` is `pd:MedicalHealth`. It is also in `pd:specialcategory-classes`. Among PD class blocks typed `dpv:SpecialCategoryPersonalData`, 32 were counted; 11 also have `skos:broader dpv:SpecialCategoryPersonalData`. Walking only `skos:broader` does not answer “is this special-category data?”. The direct type, or the scheme, does.

**OWL serialisation, `2.3/dpv/dpv-owl.ttl`.** `skos:broader` occurs 0 times. `owl:subClassOf` occurs 0 times. `rdfs:subClassOf` occurs 952 times. `dpv-owl:AIGovernance` is typed `dpv-owl:OrganisationalMeasure` and is `rdfs:subClassOf dpv-owl:GovernanceProcedures`. The generator on `dev` (`code/200_serialise_RDF.py`, about lines 433–450) copies `skos:broader` to `rdfs:subClassOf` and then deletes `skos:broader`. The primer table in section 4 says the OWL column uses `owl:subClassOf`. The published OWL file does not.

**Primer.** Section 4 of the [primer](https://w3c-cg.github.io/dpv/primer) already says that RDFS+SKOS extension uses `rdf:type` for the top concept and `skos:broader` for the hierarchy, and that DPV-OWL uses `rdfs:subClassOf` for the hierarchy. The same table also lists “`rdfs:subClassOf` or `skos:broader`” as the RDFS subtype relation. That “or” is the ambiguity #484 describes. The published SKOS guide HTML (`guides/dpv-skos.html` on `master`) contains neither `skos:broader` nor `rdfs:subClassOf` in its text. Dev SHACL shapes check that a `skos:broader` target has a `skos:prefLabel`. They do not check which relation answers a membership question.

**`dpv:RightsFulfilment`.** In `2.3/dpv/dpv.ttl` and in `dev` `2.4-dev/dpv/modules/purposes.ttl` it is typed `dpv:Purpose` and has `skos:broader dpv:LegalObligation`. `dpv:LegalObligation` is typed `dpv:LegalBasis`. `dpv:FulfilmentOfObligation` and `dpv:LegalCompliance` exist, both typed `dpv:Purpose`, and `LegalCompliance` is broader-of `FulfilmentOfObligation`. Among purpose blocks, this was the one `skos:broader` target that is a legal basis rather than a purpose. Roots that broaden to `dpv:Purpose` were not counted as defects.

**Active and passive rights.** `dpv:ActiveRight` and `dpv:PassiveRight` are defined in `2.3/dpv/modules/rights.ttl` (created 22 October 2022). `dpv:isExercisedAt` has `dcam:domainIncludes dpv:ActiveRight`. `eu-gdpr.ttl` in 2.3 contains `dpv:ActiveRight` 0 times and `dpv:PassiveRight` 0 times. The same two counts are 0 in `dev` `2.4-dev/legal/eu/gdpr/eu-gdpr.ttl`. Data-subject rights such as `eu-gdpr:A15` have `skos:broader dpv:DataSubjectRight`. The scope note for `dpv:ActiveRight` already uses withdrawal of consent as the example of an active right.

**AI terms agreed in #451 are absent.** `ai:UsageRecord`, `ai:OutputUsageStatus`, `ai:OutputUsedUnchanged`, `ai:OutputHumanVerification`, and any local name containing `Quality` or `Acceptance` do not occur in `2.3/ai/ai.ttl` or in `dev` `2.4-dev/ai/ai.ttl`. `ai:TransparencyRisk` does occur.

**AI quality proposal already in the repo.** `dev` `proposals/002-dqv4ai/iso-25059/iso-25059.ttl` has 105 `skos:prefLabel` values, starting at “AI Service Quality”. `proposals/001-ai-act-documentation/README.md` is a research write-up of AI Act documentation requirements. Issue #465’s 23 September 2026 comment cites DQV4AI at <https://doi.org/10.3233/SSW260022> and <https://w3id.org/dqv4ai/eu-aiact> and <https://w3id.org/dqv4ai/iso-25059>. The paper text was not read.

**Generator metadata (#500).** The ontology block in `2.3/dpv/dpv-owl.ttl` contains `rdfs:Label "DPV"@en`, language-tagged `dct:created`, `dct:issued`, and `dct:modified`, `dct:conformsTo` mixing an IRI and two string literals, `bibo:status` as a string, `dct:hasVersion dpv-owl:`, `profile:isProfileOf` including `dpv-owl:`, and `vann:preferredNamespacePrefix "dpv"` with `vann:preferredNamespaceUri "https://w3id.org/dpv#"`. The generator on `dev` writes these. Line 251 passes `RDFS.Label`. Lines 249–250 set `bibo:status` as a literal and comment that a literal is required so FOOPS does not fail, citing <https://github.com/oeg-upm/fair_ontologies/issues/108>. Lines 265–266 write RDFS and SKOS `dct:conformsTo` as literals. Lines 278 and 405 are an explicit TODO that currently inserts `dct:hasVersion` pointing at the same IRI. The OWL update around lines 453–458 sets `profile:isProfileOf` to OWL and to the vocabulary IRI. This audit did not execute the generator.

## Candidates

### 1. Canonical membership test for issue #484

1. **Gap.** Implementers are not told which relation answers “is this concept a member of category X?”. Issue [#484](https://github.com/w3c-cg/dpv/issues/484). The primer table in section 4 lists `rdfs:subClassOf` or `skos:broader` as if they were alternatives, and lists `owl:subClassOf` for DPV-OWL. Source files: `2.3/dpv/dpv.ttl`, `2.3/pd/pd.ttl` (`pd:BloodType`), `2.3/dpv/dpv-owl.ttl`, primer section 4, `dev` `code/200_serialise_RDF.py` lines 433–450, `dev` `code/shacl_shapes/shapes.ttl`.
2. **Evidence it is open.** The issue has no assignee and no comments. The strings `UsageRecord` and the proposed test are not already documented as a procedure. The SKOS guide HTML does not contain the hierarchy predicates. SHACL checks that a broader target has a label. It does not define the membership test. No other open issue in the searched set (“membership”, “OutputUsage”, “icons”) duplicates this.
3. **Consequence.** A rule engine that walks only `skos:broader` will not classify `pd:BloodType` as special-category data. A rule engine that walks only `rdfs:subClassOf` in the RDFS file will miss most concepts, because that predicate is absent on about four fifths of classes and, where it names a DPV concept, it duplicates `skos:broader`. The same walk fails on the OWL file, which has no `skos:broader`. The primer’s `owl:subClassOf` cell does not match the file, which uses `rdfs:subClassOf`.
4. **Proposed change.** A comment on #484, not a pull request, containing: (a) the test, split by serialisation; (b) a replacement sentence for the primer table; (c) the `pd:BloodType` example; (d) one SPARQL query an adopter can run. Test to state: in the RDFS+SKOS serialisation, category membership that the vocabulary asserts directly is `rdf:type` (and, for personal data, `skos:inScheme`); the taxonomy parent is `skos:broader`; `rdfs:subClassOf` is not a separate hierarchy. In the OWL serialisation, the taxonomy parent is `rdfs:subClassOf`, and `rdf:type` still carries the top category. Ask the group which of `rdf:type` or `skos:inScheme` is canonical for special-category data before treating either as normative.
5. **D1/D2/incidents.** None available.
6. **Experiment.** The lexical counts and the `pd:BloodType` triple above are the experiment. A stricter rerun with a SPARQL engine over the two Turtle files would confirm the counts. No model API is required. Do not regenerate the specification.
7. **Effort and cost.** About two days to draft the comment, the table correction, the example, and the query. No API cost. The group would still edit the primer source and regenerate HTML.
8. **Route, AI policy, review history.** Comment on the existing help-wanted issue. Do not open a pull request against generated HTML. Disclose AI assistance if a tool drafts the prose. Comparable documentation fixes by `bact` were merged, sometimes the same week and sometimes after about eight weeks, usually after a chair comment. A first-time taxonomy pull request without discussion was closed and redirected to an issue (PR #86).
9. **Deadlines.** 30 November 2026: an internal draft ready to post, and not posted unless approved. 15 February 2027: if the group accepts the text in the December commit window described on 18 November, it can ship in the v2.4 report the chair hopes to finish at the end of January. If that schedule slips, or if the group wants a longer debate about `rdf:type` versus `skos:inScheme`, the realistic outcome is an agreed comment and a v2.5 documentation change. Acceptance is not implied by the help-wanted label.
10. **Accurate accomplishment, if accepted.** The DPVCG primer states, with a worked `pd:BloodType` example, which relation answers category membership in the RDFS+SKOS serialisation and which relation answers it in the OWL serialisation.
11. **Evidence.** Issue #484; primer section 4 at <https://w3id.org/dpv/primer>; `pd:BloodType` in <https://w3id.org/dpv/2.3/pd/pd.ttl>; OWL hierarchy in <https://w3id.org/dpv/2.3/dpv/dpv-owl.ttl>; generator lines cited above on `dev`. A later acceptance record would be the merged documentation commit or the published v2.4 primer, plus the issue being closed.

Themes: transparency, privacy, AI reliability. A reviewer can check the disclosure of how to query the vocabulary.

### 2. Purpose parent of `dpv:RightsFulfilment`, issue #486

1. **Gap.** `dpv:RightsFulfilment` is a purpose whose `skos:broader` is `dpv:LegalObligation`, a legal basis. Issue [#486](https://github.com/w3c-cg/dpv/issues/486). Files: `2.3/dpv/modules/purposes.ttl` and the same block in `dev` `2.4-dev/dpv/modules/purposes.ttl`.
2. **Evidence it is open.** `besteves4` wrote on 9 September 2026 that the parent should be `dpv:FulfilmentOfObligation` or `dpv:LegalCompliance`. The reporter acknowledged that the same day. Neither 2.3 nor `2.4-dev` has the change. The issue is still open, with no assignee. The lexical scan found no second purpose whose broader target is typed `dpv:LegalBasis`.
3. **Consequence.** A query for purposes under legal obligation returns a purpose. A query for children of legal bases returns a purpose. Rights-fulfilment processing is filed under the wrong top concept, so a record of why processing is lawful and a record of why it is done can be confused.
4. **Proposed change.** A short comment that recommends `dpv:LegalCompliance` as the parent, because its definition is “purposes associated with carrying out data processing to fulfill a legal or statutory obligation”, while `dpv:FulfilmentOfObligation` is the broader parent of that concept and is not limited to legal obligations. The definition of `dpv:RightsFulfilment` says the purposes are those “specified in law”. Offer one SPARQL query: every resource typed `dpv:Purpose` whose `skos:broader` target is not typed `dpv:Purpose` and is not `dpv:Purpose` itself. Ask the chair to apply it in the spreadsheet. Do not edit the Turtle.
5. **D1/D2/incidents.** None available. The vocabulary’s own definitions are sufficient.
6. **Experiment.** The parent scan above is the experiment. Re-run the query with a SPARQL engine before posting, in case the lexical split missed a block.
7. **Effort and cost.** Half a day, including the query. No API cost. Regeneration is the group’s.
8. **Route.** Comment on #486. The 18 November minutes say the chair will propose resolutions and commit the error list. Posting a competing generated pull request is the wrong route. A comment that chooses between the two parents Beatriz already named is the part still undecided.
9. **Deadlines.** 30 November 2026: the comment drafted and, if approved, posted before the chair’s commit pass. 15 February 2027: the corrected parent can be in v2.4 if the group applies it during the December–January window. If the chair commits a different parent first, the contribution stops at the written rationale. Do not claim the fix as ours if the commit is his.
10. **Accurate accomplishment, if the parent change ships.** DPV no longer classifies rights-fulfilment purposes as a legal basis, and a query guards the purpose tree against the same kind of parent.
11. **Evidence.** Issue comments of 9 September 2026; the two Turtle blocks; definitions of `dpv:LegalCompliance`, `dpv:FulfilmentOfObligation`, and `dpv:LegalObligation` in `2.3/dpv/dpv.ttl`.

Themes: privacy, authorization. The legal basis and the purpose are different claims about why processing happens.

### 3. OWL ontology header: fix the undefined label predicate, issue #500

1. **Gap.** Published `2.3/dpv/dpv-owl.ttl` uses `rdfs:Label`, which is not the RDFS predicate `rdfs:label`. Issue [#500](https://github.com/w3c-cg/dpv/issues/500), item 1. Generator: `dev` `code/200_serialise_RDF.py` line 251, `graph.add((vocab_iri, RDFS.Label, Literal(vocab.upper(), lang='en')))`. This audit did not execute that line.
2. **Evidence it is open.** The issue was opened 16 November 2026, has label `todo`, has no comments, and asks `besteves4` whether the header values are intended. The `rdfs:Label` triple is in the published 2.3 OWL file. The same generator also explains several other items in that issue, so a patch that “fixes” all nine would be wrong: `bibo:status` is a literal on purpose (lines 249–250, FOOPS); RDFS and SKOS `dct:conformsTo` values are literals in the generator (lines 265–266); `dct:hasVersion` pointing at the same IRI is an explicit TODO (lines 278 and 405); the OWL hook sets `profile:isProfileOf` to the vocabulary IRI (lines 453–458).
3. **Consequence.** Ontology metadata that uses `rdfs:Label` is invisible to tools that read `rdfs:label`. The other header fields will keep failing external validators until the group decides which of the intentional literals to keep. Changing the FOOPS workaround without replacing it can fail the check the comment names.
4. **Proposed change.** A comment on #500 that splits the nine items into three groups: the `RDFS.Label` call, which should become `RDFS.label`; the TODO already in the generator (`dct:hasVersion`, and the OWL self-profile if the group did not mean the ontology to be a profile of itself); and the FOOPS literal, which should stay until a replacement satisfies the cited check. Offer the one-line label change. Do not regenerate artifacts in a pull request.
5. **D1/D2/incidents.** None.
6. **Experiment.** Diff the published ontology header against the generator. Optional and sufficient: run the generator’s metadata function on a fixture graph and assert the predicate is `rdfs:label` and that `bibo:status` remains a literal. No external API.
7. **Effort and cost.** About one day for the comment and a local fixture, if Python dependencies are installed later. No API cost. Full regeneration touches every OWL file and is the group’s release step.
8. **Route.** Comment first. The author already asked Beatriz to confirm intent, and the 18 November minutes say the chair will comment on this class of issue. Send the split analysis only if those comments have not already answered it. Review history for generator patches is the `bact` script pull requests: small ones were merged or applied by hand; a larger script (#358) has been open since August 2025 and was deferred again on 18 November.
9. **Deadlines.** 30 November 2026: internal note, posted only if #500 is still unanswered and posting is approved. 15 February 2027: the label predicate can be corrected in the v2.4 regeneration if the group takes the one-line change. The `hasVersion` TODO is a design choice and may stay open past February.
10. **Accurate accomplishment, if accepted.** The OWL serialisation’s ontology header uses `rdfs:label`, and the generator no longer emits `rdfs:Label`.
11. **Evidence.** Issue #500; `2.3/dpv/dpv-owl.ttl` ontology block; `code/200_serialise_RDF.py` on `dev` at the lines cited. A later proof of acceptance is the changed line in a `dev` commit and the predicate in the published v2.4 OWL file.

Themes: transparency, AI reliability. Machine-readable metadata should use the predicate consumers actually query.

### Watched, not recommended to lead

**[#465](https://github.com/w3c-cg/dpv/issues/465) AI quality.** The gap in the AI extension is real: `2.4-dev/ai/ai.ttl` has no quality taxonomy. It is not an unowned gap. `proposals/002-dqv4ai` is already on `dev`, DelaramGlp pointed the issue at a published DQV4AI vocabulary on 23 September 2026, and the 18 November minutes put proposal `002` on the 25 November agenda. A second vocabulary would duplicate that work and fail the guide’s “discuss first” rule. After that meeting, the only contribution worth drafting is whatever subset the group says it still needs. November 30 outcome: do not submit. February 15 outcome: possible help on a slice the group requests, not a new framework. D1/D2 cannot support it. No new experiment until the group picks a direction.

**[#451](https://github.com/w3c-cg/dpv/issues/451) AI output use.** The 27 May 2026 summary (`ai:UsageRecord`, `ai:OutputUsageStatus` and four instances, `ai:OutputHumanVerification`, `ai:OutputHumanVerificationStatus`) is still absent from `2.4-dev`. The proposer and the chair own the wording. The 28 June note says EU voluntary AI-content icons should be a separate AI Act issue; a search of issues for that follow-up did not find one. Writing a competing model would ignore an agreement already in the thread. November 30: do not submit. February 15: one example, only after those terms are actually added. A status comment that the terms are not in `2.4-dev` is optional and low value, because the chairs can see that. Themes if it later lands: human agency, human oversight, transparency.

**[#482](https://github.com/w3c-cg/dpv/issues/482) active/passive rights.** The core classes exist and the GDPR extension does not use them, in 2.3 or `2.4-dev`. The issue has had no reply since 5 August 2026 and was not in the 18 November plan. Classifying every GDPR right is a legal judgement the group has not asked for. A pull request that types all of them would be a large non-authoritative change under the guide’s five questions. Not recommended for either deadline unless a chair asks.

**Issue [#501](https://github.com/w3c-cg/dpv/issues/501).** `dpv:PersonnelPerformanceManagement` has two broader parents, `dpv:PersonnelManagement` and `dpv:PersonnelMonitoring`. Opened 16 November 2026, no comments. The minutes say parent changes will be discussed on 25 November. Leave it to that discussion.

## Rank

| Rank | Candidate | Why this order |
| --- | --- | --- |
| 1 | #484 membership test | Help-wanted, unassigned, no owner in the thread, verified against the files, small, and useful to every adopter. Fits the December documentation window if the group agrees. |
| 2 | #486 purpose parent | A chair already confirmed it. Still unfixed. The remaining choice is one parent, plus a query that stops a repeat. Low originality, high chance the group will take the change. |
| 3 | #500 `rdfs:Label` only | One generator line, confirmed in the published file. Must be separated from intentional FOOPS literals or the comment will look careless. Easy for the chair to include while regenerating v2.4. |
| — | #465, #451, #482 | Real topics. Already staffed, already drafted, or unanswered and legally broad. Starting them now competes with the 25 November agenda and with the people who wrote the proposals. |

## Not verified

- The online spreadsheets, which the contribution guide treats as the canonical term source.
- A SPARQL or OWL-reasoner rerun of the lexical counts. Counts can move if a Turtle block is split differently.
- Execution of `200_serialise_RDF.py`, so the link from `RDFS.Label` to the published `rdfs:Label` triple is source-plus-artifact, not a runtime trace.
- The DQV4AI paper at doi:10.3233/SSW260022. Only the issue comment, the DOI, and the proposal files in `dev` were used.
- The Advisory Board LLM document named by the October 2026 W3C draft policy.
- W3C login, so 25 November joining instructions and any member-only agenda are unseen.
- GitHub profile pages, so personal names are tied to logins only where a pull request, the group page, or the minutes say so.
- Whether `dev` is behind unpublished spreadsheet edits.
- The full set of 129 open issues. The sample was the forty most recently updated open issues, the `help-wanted` label, the four named issues, and the pull-request sample above.
- Any claim that a future comment or patch will be accepted.
