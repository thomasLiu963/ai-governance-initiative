# Wave 1 final review

Date: 2026-11-18. Thomas approved the whole batch the same evening. All four items were submitted as `thomasLiu963`. None is merged or published. Acceptance is still none. The public URLs are in `execution/SUBMISSION_LOG.md`.

Excluded from this batch, and not prepared for sending here: T004 / C-004, the FCC comment (C-007), the USAC resolution (C-006), AI Incident Database reports, and D1/D2.

## How to approve

Reply with one of:

- `approve all`
- `approve all except T00x` (name each exclusion)

Anything else is not approval. If an upstream file changes before a write, that item stops and the others continue only if they are still valid.

## Automation

Git 2.39.5 and GitHub CLI 2.94.0 are installed. The public account for every submission is `thomasLiu963` (user id 125628460). The CLI is currently logged in as `thomasRespan` (user id 294379577), and SSH authenticates as `thomasRespan`. Nothing will be posted until the CLI is logged in as `thomasLiu963`. No password or token needs to be pasted.

After approval, all four writes can be done from here:

| ID | External write | Where the work happens |
| --- | --- | --- |
| T002 | Fork `OWASP/www-project-ai-security-and-privacy-guide`, branch, one commit, pull request | A checkout outside this workspace. This workspace is not pushed. |
| T001 | One issue on `OWASP/AISVS` | `gh issue create`. No fork and no pull request. |
| T003 | One comment on `w3c-cg/dpv` issue #484 | `gh issue comment`. No new issue and no pull request. |
| T005 | One issue on `w3c/gpc` | `gh issue create`. The held test, a spec pull request, and a Chromium bug stay local. |

Immediately before each write, the same upstream check is repeated. If the target text or issue has changed in a way that makes the contribution wrong, that item is paused.

The public author is `thomasLiu963`. Local git is configured as `appofanGithub` with the noreply id `125628460`, which is `thomasLiu963`'s GitHub id, but the name in that config is wrong. Git config will not be changed. The Exchange commit will be authored, for that command only, as `thomasLiu963` `<125628460+thomasLiu963@users.noreply.github.com>`. The issue, comment, and pull request will be opened by the `thomasLiu963` login once that account is the active GitHub CLI login. `thomasRespan` will not be used.

## T002 — OWASP AI Exchange

- **Register ID:** C-002
- **Institution:** OWASP AI Exchange, community guidance
- **Repository:** https://github.com/OWASP/www-project-ai-security-and-privacy-guide
- **Channel:** one pull request to `main`. No issue.
- **Problem:** `#LEAST MODEL PRIVILEGE` gives two instructions for one event. Line 747 says "Fail closed if the policy engine is unreachable." Line 760 says "policy engine outage requires an explicit fail-closed vs fail-open choice."
- **Why it matters:** An agent that can call tools, read data, message another agent, or send something outward can be allowed to proceed while the system that was supposed to authorize it is down. A second team can deny the same action and cite the other sentence. The failure is not observable as a deny.
- **What we contribute:** One clause, in one file. The fail-closed implementation sentence stays. The limitations clause stops offering a fail-open choice and says to deny the action.
- **Plain English:** The page currently says both "if the decision service is down, refuse" and "if the decision service is down, pick refuse or allow." We delete the pick. We do not add a new control, a product name, or a special exception for reads.

### Verification on 2026-11-18

- `main` is still `c68371ed56051a3d7c894e36c20c3bcbc22eb441` (2026-11-16).
- Both sentences are still on lines 747 and 760.
- A code search for `fail-open` returns that one file. An issue search for the exact phrase `fail-open` returns zero issues and zero pull requests.
- Issue #202 mentions `#LEAST MODEL PRIVILEGE` as a candidate for a different enforceability note. It does not propose this clause. It will not be mentioned.
- `git apply` of the prepared patch succeeded against the file at that commit. The staged public diff is the single line below.
- The patch does not add a read-only fail-open exception.

### Exact public text

Title:

```text
Least model privilege: deny the action when the policy engine is unreachable
```

Body:

```markdown
### Which page

`content/ai_exchange/content/docs/1_general_controls.md`, control **#LEAST MODEL PRIVILEGE** (https://owaspai.org/go/leastmodelprivilege). One file. One clause, in the Limitations paragraph under the agentic authorisation block. Docs only.

### Problem

The same control gives two instructions for one event.

Runtime policy validation says: "Fail closed if the policy engine is unreachable."

The Limitations paragraph says: "policy engine outage requires an explicit fail-closed vs fail-open choice."

Both sentences were added in the same integration, pull request 185, in the commit that brought in the agentic authorisation block (`693d59d6f7`, merged as `c3562e82` on 2026-08-03). The pull-request discussion does not treat them as different rules. A later permalink edit (`e6679119`, 2026-08-24) changed a link on the Limitations line and left the choice in place. No open issue or pull request uses the words "fail-open."

An implementer can allow a tool call, a data read, a message, or an outbound send while the policy engine is unreachable, and can cite the Limitations sentence. Another team can deny the same call and cite the implementation sentence. For an agent that can change state or send data, fail open means the authorisation gate is missing exactly when it cannot be evaluated.

The other sentences in this block already point the same way: deny-by-default, no action until a permit or deny returns, and default deny when policies conflict. This patch does not touch them.

### Change

Replace the choice clause with: "if the policy engine is unreachable, deny the action."

The implementation sentence stays, including the words "Fail closed." Latency, revocation-latency tolerance, and the email example stay. No new control name, no new permalink, and no product or tool name.

### AI assistance

AI was used. Cursor, using Grok 4.7, read `#LEAST MODEL PRIVILEGE` at commit `c68371ed`, the commit that added both sentences, and the contribution rules, and it drafted this pull-request text and the one-clause patch. That draft was checked against those sources. I have read the patch and both sentences. No product I am affiliated with is mentioned.
```

Approving this item means the first-person sentence is true: you have read the patch and both sentences.

### Exact diff

File: `content/ai_exchange/content/docs/1_general_controls.md`

```diff
-**Limitations:** Authorisation and policy enforcement define what is permitted, not what is wise. Agents can harm within scope; [prompt injection](/go/promptinjection) before delegation is established or misuse of legitimately delegated authority remain risks. LLM-generated delegation instructions may produce structurally valid but contextually unauthorised tokens. Novel action sequences make complete pre-specification hard — combine short token lifetime, revocation, and delegation attenuation with explicit revocation-latency tolerance. Per-action evaluation adds latency; policy engine outage requires an explicit fail-closed vs fail-open choice.
+**Limitations:** Authorisation and policy enforcement define what is permitted, not what is wise. Agents can harm within scope; [prompt injection](/go/promptinjection) before delegation is established or misuse of legitimately delegated authority remain risks. LLM-generated delegation instructions may produce structurally valid but contextually unauthorised tokens. Novel action sequences make complete pre-specification hard — combine short token lifetime, revocation, and delegation attenuation with explicit revocation-latency tolerance. Per-action evaluation adds latency; if the policy engine is unreachable, deny the action.
```

### Remaining uncertainty

- The live rendered page at https://owaspai.org/go/leastmodelprivilege was not clicked in this pass. The repository file at `main` was read.
- No runtime was executed. The contribution is a wording contradiction, not a measured product default.
- Who reviews the pull request is unknown. A same-week merge is possible for a diff this small and is not a promise.
- The disclosure names Grok 4.7 because that is the assistant in this session. Approving confirms the human sentence in that disclosure.

## T001 — OWASP AISVS

- **Register ID:** C-001
- **Institution:** OWASP, AI Security Verification Standard
- **Repository:** https://github.com/OWASP/AISVS
- **Channel:** one issue against `1.02-dev`. No pull request unless a maintainer later asks.
- **Problem:** No current requirement says the runtime blocks an agent action when the policy decision point returns no decision. The glossary still says authorization components fail closed.
- **Why it matters:** A runtime can meet the rows that require a policy engine, place it outside the agent, and time out a human approval, and still run the tool when the authorization call itself is silent, errors, or drops. Disrupting the decision point then disables authorization.
- **What we contribute:** A request to append one Level 2 row, `9.5.8`, and the matching Appendix B inventory line. The old identifier `9.7.4` and its logging clause stay retired.
- **Plain English:** The standard's dictionary says "if authorization cannot be completed, stop." The checklist no longer has a test for that stop. The checklist item existed, was accepted, and was deleted in a chapter rewrite later the same day a levels review had kept it. We ask them to put the stop back as a new row. We do not say we invented it, and we do not send code unless they ask.

### Verification on 2026-11-18

- `main` is still `092232f012ec10d654c1ca345fa10d5a5a8be12a` (2026-11-11).
- `9.5.7` is still the last C9.5 row. A repository search for `9.5.8` returns nothing.
- The glossary sentence is still present: "AISVS requires AI components with safety or authorization responsibilities to fail closed."
- The historical row was re-read at `19e6410889` in `1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md`, line 100. That commit is the #928 merge at 2026-06-15 11:16 UTC. There was no `1.02-dev` tree on that commit. The quotation in the issue matches that line.
- Open pull request #1227 adds `9.3.10` through `9.3.14` and Appendix B lines for those skill rows. It does not take `9.5.8`.
- `9.5.8.patch` remains local. It was previously applied to the two files from `092232f`. It is not part of this submission.

### Exact public text

Title:

```text
[1.02] C9.5: block the agent action when its policy decision point returns no decision
```

Body: the whole of `contributions/T001-AISVS/ISSUE.md`.

```markdown
Target: `1.02-dev` only. Released `1.0/` and `1.01/` stay locked.

This asks to restore a failure behavior the project already accepted. It was merged in #683 and removed when #934 rewrote the chapter. I am not proposing it as a requirement I originated.

## Missing requirement

No current requirement says what the runtime does when the policy decision point for an agent action does not return a decision.

`9.5.1` requires agent actions to be authorized against a runtime policy that limits tools and parameter values. `9.5.3` requires application logic or a policy engine, not the model, to enforce access-control decisions. `5.2.5` isolates that decision point from the agent. `9.6.2` blocks an action when a human-approval gate is not satisfied within the defined approval time. A runtime can satisfy each of those and still invoke the tool when the authorization call returns no decision.

Appendix A still says: "AISVS requires AI components with safety or authorization responsibilities to fail closed."

## History

#676 separated a returned denial from no decision at all. On 2026-04-11 Rico Komenda wrote: "The gap is real. ... No existing control explicitly requires fail-closed behavior on PDP timeout or network partition. ... Level 2 is appropriate." #683 merged the control on 2026-04-13.

At `19e6410889` (merge of #928, 2026-06-15 11:16 UTC), `1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md` still contained:

> **9.7.4** Verify that when the policy decision point (PDP) used for governance evaluation is unavailable (e.g., timeout, network partition, service failure), agent execution fails closed by blocking the proposed action, and the unavailability event is logged with sufficient detail for incident investigation. Level 2.

#928's levels table kept "C9.7.4 | L2 | Fail-closed when PDP unavailable." #934 merged later that day with an empty body and no review. It replaced the chapter and deleted `9.7.4` with the rest of C9.7. No comment on that pull request says this predicate was rejected. No later issue restores it.

## Proposed wording

Append one Level 2 row. Leave C9.7 retired. Do not reuse `9.7.4`. Leave the logging clause out.

> **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2.

A decision is an allow, a deny, or a referral to the C9.2 approval gate. An error, an empty result, a dropped connection, and silence are not decisions. On `main` at `092232f` (re-read 2026-11-18), `9.5.7` is the last C9.5 row and `9.5.8` is unused. Open pull request #1227 adds C9.3 skill rows and does not take `9.5.8`.

Appendix B lists active requirements and adds none of its own. The matching line would be: "Runtime blocks an agent action when its policy decision point does not return a decision within the defined timeout | C9.5.8".

I will not open a pull request unless a maintainer asks for one.

## Example

The defined timeout is 200 ms. The tool call would modify a synthetic resource.

Compliant: a stub accepts the decision request and returns nothing. At 200 ms the tool has not run, and the resource is unchanged. The same block holds when the stub closes the connection or returns an error that is not an allow, a deny, or an approval referral.

Noncompliant: the timeout fires, the runtime invokes the tool, and the resource changes. Treating a closed connection or a non-decision error as permission is the same failure.
```

### Exact diff

None will be submitted. The local patch, which stays unsent, adds this requirement row after `9.5.7` and this Appendix B line after the `C9.5.7` inventory row:

```diff
+| **9.5.8** | **Verify that** when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. | 2 |
```

```diff
+| Runtime blocks an agent action when its policy decision point does not return a decision within the defined timeout | C9.5.8 |
```

### AI-assistance disclosure

AISVS allows an AI-drafted issue when the contributor can defend every sentence and the control is testable. It does not require a banner, a model name, or a generated-by line. Maintainers closed #1215 and #1216 on 2026-11-18 because long generated discussion was not readable. The issue therefore has no disclosure paragraph.

For this review: an AI assistant in Cursor shortened the issue and checked it against `1.02-dev` at `092232f`, the glossary sentence, pull request #1227, and the `9.7.4` line at `19e6410889`. You remain responsible for every sentence if it is filed.

### Remaining uncertainty

- #934 still has no written reason for deleting this one predicate. The chapter rewrite was intentional. A decision that this failure should stop being a requirement is not in the record.
- Agent-framework defaults were not surveyed and are not claimed.
- If #1227 or another edit merges before a maintainer asks for a patch, the local patch must be regenerated. The requirement sentence stays the same only if `9.5.8` is still free.
- Slack and any discussion outside GitHub were not read.

## T003 — W3C Data Privacy Vocabulary

- **Register ID:** C-003
- **Institution:** W3C Data Privacy Vocabulary Community Group
- **Repository:** https://github.com/w3c-cg/dpv
- **Existing issue:** https://github.com/w3c-cg/dpv/issues/484
- **Channel:** one comment on that issue. No new issue and no pull request.
- **Problem:** The primer offers `rdfs:subClassOf or skos:broader` as one subtype test and says DPV-OWL uses `owl:subClassOf`. Those relations answer different questions, and the OWL files use `rdfs:subClassOf`.
- **Why it matters:** A rule that walks one `skos:broader` hop classifies Blood Type as Medical Health and misses special-category personal data. A rule that looks for `rdfs:subClassOf` in the RDFS file also misses it. A rule that looks for `skos:broader` in the OWL file misses it there, because that relation has been removed. The category the vocabulary actually records on the concept is `rdf:type`.
- **What we contribute:** The distinctions, the Blood Type results on both serialisations, the two table cells to correct, one SPARQL query, and the Professional Experience exception so the type rule is not overstated.
- **Plain English:** "Is Blood Type special-category data?" depends on which arrow you follow. The direct parent arrow stops at Medical Health. The type the editors recorded says yes, it is special-category. The OWL file uses a subclass chain instead of the parent arrow, and that chain does reach the category. The comment tells the group which arrow answers which question and which two table cells name an arrow the files do not use.

### Verification on 2026-11-18

- Issue #484 is open, labels `todo` and `help-wanted`, no assignee, zero comments, `updated_at` `2026-08-27T13:13:05Z`.
- `master` is still `689d32c0f7c571d32f7f8635ae548fcc1c3ff695`. `dev` is still `aff91c294b105d9a261ea8622350b0fc7ef0e293`.
- `reproduce.py` was run again with `rdflib` 7.6.0. The report matches `results/report.txt`. The runner also prints a `WROTE` line to the console. That line is not part of the report.
- Blood Type on the RDFS+SKOS files: type true, direct broader false, broader path true, `rdfs:subClassOf+` false. On the OWL IRIs: type true, `rdfs:subClassOf+` true, `skos:broader` absent. The same answers hold for 2.3 and `2.4-dev`.
- The published primer and specification HTML, and the two Jinja templates on `dev`, still contain `owl:subClassOf` and the primer cell `rdfs:subClassOf or skos:broader`.
- The comment is not redundant. Nobody else has answered #484, and the documentation cells are unchanged.

### Exact public text

The comment is the whole of `contributions/T003-DPV-Membership/COMMENT.md`:

```markdown
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
```

Reproducibility line already inside that comment: commits `689d32c0` and `aff91c29`, the four Turtle paths, and the SPARQL query. Local runner: `rdflib` 7.6.0, `contributions/T003-DPV-Membership/reproduce.py`.

### Exact diff

None. The group edits the Jinja templates and regenerates HTML. This project does not open that pull request.

### Remaining uncertainty

- The online spreadsheet was not opened. The repository CSV can lag the sheet.
- Subclass results are SPARQL property paths plus the RDFS meaning of `rdfs:subClassOf`. No OWL tableau reasoner was run.
- The comment is dense. It is one comment because splitting it would drop either the Blood Type result, the documentation cells, or the exception that stops the type rule from being absolute.
- Approving means you can defend the comment, including the disclosure's first-person sentence.

## T005 — W3C Global Privacy Control

- **Register ID:** C-005
- **Institution:** W3C Privacy Working Group
- **Repository:** https://github.com/w3c/gpc
- **Channel:** one issue asking the editors which behavior is intended. No Web Platform Test pull request, no specification pull request, and no Chromium bug.
- **Problem:** The 24 September 2026 Working Draft says a preference change during or after a top-level navigation is not reflected until the next navigation. Chromium's browser test expects the already loaded document to update immediately. Nothing in the current `gpc/` tests reads the document that was already loaded.
- **Why it matters:** The cached value is how one do-not-sell-or-share choice stays stable for the whole page and its subresources. If the open page updates immediately, the page can observe a different choice from the one in force when it loaded. The editors have not said which of those is required.
- **What we contribute:** The question, with the four checks kept separate. The conformance test in `contributions/T005-GPC-WPT/patch/` stays local for a possible later submission if an editor keeps § 3.2.
- **Plain English:** The spec says a loaded page keeps the privacy signal it started with. Chrome's own test says the open page should change as soon as the setting changes. We saw that change locally in two different ways, and we read the browser source. We did not run the official test harness. We are asking the editors to pick, before anyone files a test that would force one answer.

### Verification on 2026-11-18

- Editor's draft `index.html` at `09013acfed7820dc967489514a156e2ced827289` (2026-09-24, still `main`) still has the caching `MUST` at lines 212–214. No later commit.
- Open issues are #164, #162, #146, #143, #138, #125, #114, and #93. None asks whether an already loaded top-level document keeps `gpcAtNavigation`.
- `./wpt run` was not started. There is no official testharness result for `navigation-cache.https.html`.
- DevTools experiment, recorded in `local-results.md`: Chrome 157.0.8103.79 with `GlobalPrivacyControlApi`. The held test's attribute assertion failed, expected false and got true. The same-document header assertion in that file did not run. This used a local vendor shim and was not `./wpt run`.
- ChromeDriver experiment, recorded in `local-run/chromedriver-157.json`: `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`. The loaded document moved from attribute false and no `Sec-GPC` to attribute true and `Sec-GPC: 1` before navigation. With no feature flag, the command returns "Global Privacy Control is disabled."
- Source only: `PrefChangeIsReflectedImmediately` was read and not executed. Firefox and WebKit were not launched.
- wpt.fyi results cited in the issue are for the existing `gpc/` files, which set the preference and then open a new document. They are not a run of the held test.

### Exact public text

Title:

```text
Should an already loaded document keep its GPC value until the next top-level navigation?
```

Body, from the title section of `contributions/T005-GPC-WPT/ISSUE.md`. The local preamble above that title is not posted.

```markdown
Working Draft, 24 September 2026, § 3.2 requires the preference to be cached on each top-level navigation. A change during or after that navigation is not reflected until the next navigation. `gpcAtNavigation` must reflect the preference when the top-level document began loading. § 3.3 and § 3.4 bind `Sec-GPC` and `navigator.globalPrivacyControl` to that boolean. § 8.1 records the session preference and returns `{gpc: <boolean>}`. It does not say to rewrite `gpcAtNavigation` for a document that has already started loading.

https://www.w3.org/TR/2026/WD-gpc-20260924/

Four checks are separate. I did not run `./wpt run`, and there is no official testharness result for this observation.

Source only. Chromium `main`, `chrome/browser/chrome_global_privacy_control_browsertest.cc`, test `PrefChangeIsReflectedImmediately`, expects the other behavior for the profile setting. With the Universal Opt-Out features and `GlobalPrivacyControlApi` enabled, the test loads a document, then clears `kUniversalOptOutEnabled`, and expects `navigator.globalPrivacyControl` to become false and a following `fetch` to omit `Sec-GPC`, with no navigation. The comment says the toggle is reflected in the renderer without a reload. The Blink getter reads `RendererPreferences` on each access. A DevTools override, when set, takes precedence over that profile setting. I read this test. I did not compile or run it. On Firefox `main`, `GPC:SetGlobalPrivacyControl` writes `privacy.globalprivacycontrol.enabled`, and `Navigator::GlobalPrivacyControl` and `nsHttpChannel::SetGlobalPrivacyControl` read that preference when the value is used. Firefox is not installed here. Current WebKit applies the test runner's boolean in the navigation-policy callback, through `WKWebsitePoliciesSetGlobalPrivacyControlEnabled`. `navigator.globalPrivacyControl` reads the frame settings. `WKWebpagePreferences.globalPrivacyControlEnabled` is marked available starting in macOS 27. Safari on this machine is 17.6, and WebKit was not run.

DevTools experiment. Chrome 157.0.8103.79, headless, with `GlobalPrivacyControlApi` enabled. A local copy of the held test loaded `testharness.js`, `testharnessreport.js`, and `testdriver.js`, and a local vendor file, which is not part of the held patch, forwarded get and set to Chrome DevTools `Browser.getGlobalPrivacyControl` and `Browser.setGlobalPrivacyControl`. The assertion that the already loaded document keeps `navigator.globalPrivacyControl === false` failed because the value was true. This was not `./wpt run`. The same-document `Sec-GPC` assertion in that file did not run, because the attribute assertion failed first.

ChromeDriver experiment. Same Chrome version, ChromeDriver 157.0.8103.79. This sent the WebDriver extension command. It did not use that vendor file, and it did not load the held test. With `GlobalPrivacyControlApi` enabled, `POST /session/{id}/privacy` `{"gpc": true}` returned `{"gpc": true}`. The already loaded document changed from `navigator.globalPrivacyControl === false` and no `Sec-GPC` to `true` and `Sec-GPC: 1` before the next navigation. With no feature enabled, the same command returns "Global Privacy Control is disabled." and the attribute is absent.

Existing WPT results, not this test. At revision `71b58bb191`, Chrome 158 and Firefox 160 pass the existing `gpc/` tests, including the testdriver test. Those tests set the preference and then open a new document. None of them reads the document that was already loaded. Safari 27.2 does not report a passing signal subtest for those files. There is no open `w3c/gpc` issue on this document-caching question. Issue #146 is about workers and is not this question.

Which behavior should an already loaded top-level document follow after the session preference changes, including after § 8.1?

If the document keeps `gpcAtNavigation` until the next top-level load, Chromium's unread browser test expects the other behavior, and the DevTools and ChromeDriver sessions above observed it. A Web Platform Test for that observation can be proposed afterward. If the loaded document is supposed to update immediately, § 3.2 needs an edit before any such test. I am not filing the test or a Chromium bug in parallel with this question.

LLM use: an LLM drafted this issue from the Working Draft, the Chromium, Firefox, and WebKit source cited above, the local DevTools experiment, and the local ChromeDriver session. `./wpt run` was not used. The person who posts it is responsible for the claims.
```

### Exact diff

None will be submitted. The held patch adds three new files under `gpc/` and is not opened with this issue.

### Remaining uncertainty

- `./wpt run` was not executed. The issue says so.
- Firefox and WebKit were not launched. The Chromium browser test was not compiled.
- The issue does not explain why wpt.fyi Chrome 158 passes the existing testdriver command when local Chrome 157, with no feature flag, rejects it.
- A substantive pull request on `w3c/gpc` would need Working Group participation or a non-member patent commitment. This workspace has neither, which is why the submission is a question.

## What approval does not do

- It does not mark any item accepted, merged, or published.
- It does not authorize a reply to a later maintainer comment.
- It does not authorize T004, the FCC comment, the USAC resolution, an incident-database report, or D1/D2.
- It does not authorize pushing this workspace to any remote.
