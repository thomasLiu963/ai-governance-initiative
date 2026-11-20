# Phase 1 list

Updated 2026-11-19. November 30 is an early checkpoint. February 15, 2027 is the deadline that matters. An item is not dropped because a name, a manuscript, or a pull request is missing. It is dropped when the target has no regulation to amend, no qualifying error, or no incorporation path.

Nothing in this update was filed, posted, or mailed.

An affirmative result is still an external act: a merged test, a merged requirement, published vocabulary, a Commission order, or a written agency decision in the Notice Register. A 30-day petition response is a real procedural result. It is not an amended regulation.

## DO NOW

### 1. GPC navigation-cache test — pull request drafted, not opened

The official runner has now executed the test.

| Fact | Result |
| --- | --- |
| Checkout | `web-platform-tests/wpt` `221a7fea449dcd9a42d5f249d5e4cf359a619d74` |
| Lint | `./wpt lint` on the two proposed files exited 0 |
| Browser | Chrome 157.0.8103.79, `--enable-features=GlobalPrivacyControlApi` |
| Attribute | Expected false, got true, on the already loaded document |
| `Sec-GPC` | A one-off copy asserted the header first. Expected null, got `"1"` |
| Firefox, WebKit | Not run |

The existing `gpc/` tests set the preference and then open a new document. This test is not a duplicate of that pattern. The new-document file was removed from the proposed pull request so it would not repeat `navigator-globalPrivacyControl.https.html` and `sec-gpc.https.html`.

Editor Sebastian Zimmeck's close of issue 165 quoted the cache rule. The test encodes that rule. Chrome's official result conflicts with it. That is a reason to propose the test, not a reason to drop it.

**Blocker for opening:** explicit approval. The draft is `execution/phase1/drafts/gpc-wpt/PULL_REQUEST.md`. The human who opens it must understand the test. WPT's AI policy requires a labelled disclosure.

**Next step:** read the two files and the run notes. Approve or change them. Do not open the pull request from this update. A Chrome failure will show in CI. This checkout has no test-expectation `.ini` files. Failure metadata, if required to merge, is a separate repository and was not edited.

**November 30:** the run and the draft exist. A merged test does not. **February 15:** a pull request can be in review. A merge is not established. The sample for another GPC-related WPT pull request was about a month and was not re-fetched today.

### 2. California petition — one defensible candidate

**Candidate:** Civil Rights Council, title 2, section 11008.1(a). Change the citation from section 11008(i) to section 11008(h).

This is a substantive amendment, not a missing comma. Current section 11008(h) defines "Employment Benefit." Section 11008(i) defines "Employment Practice," which is any act, omission, policy, or decision affecting a benefit. The automated-decision definition says the computation concerns an employment benefit and then cites (i). Duties in sections 11009(f), 11013, 11016, and 11017(e) use that definition. A reader who follows the citation covers a wider set of acts than a reader who follows the words.

The Council's final statement of reasons shows the letter was chosen on purpose while it still named the benefit. The Council wrote that it would replace broader language with "regarding an employment benefit, as defined in section 11008(i)." History note 4 of the current section 11008 says new subsections (a) and (l) and the relettering were filed June 27, 2025 and operative October 1, 2025. After that relettering, the benefit definition is (h) and (i) is the practice. The citation was not moved with it.

**Why this is still the petition, despite the missing name.** Government Code section 11340.7(a) gives a written denial or a scheduled hearing within 30 days of receipt. That clock is the reason the pathway stays a priority through February 15. The absent name and address block mailing. They do not show that the Council is the wrong respondent or that the citation is harmless.

**Filing blockers:** petitioner's legal name, mailing address, signature, and which office receives it. Oakland Suite 2050 is the 2024 notice address. Sacramento, 651 Bannon Street, Suite 200, is on a 2026 meeting notice. Email is not established as a petition method. Draft: `execution/phase1/drafts/california-petition.md`. Not mailed.

**November 30:** a mailed letter can exist if the name and address are supplied this week. A 30-day decision cannot, because the clock runs from receipt. **February 15:** a written denial or a decision to schedule a hearing can exist if the letter is mailed in December. An amended code section is a later APA or section 100 event. The Council's last full proceeding on this subject ran from a May 2024 notice to an October 2025 effective date. That duration is not claimed for a one-citation change, and a code change by February 15 is not claimed either.

No second contradiction, in another agency's adopted rule, met the same bar in this pass. Searches covered the CPPA ADMT articles, the Department of Insurance's November 13, 2026 announcement, the Department of Technology's SIMM page, the Civil Rights Council contractor package, and DMV driverless-testing section 227.42. Details of the drops are below.

### 3. FCC comment — pending approval, deadline November 25

The 2,207-word comment does advance this Further Notice. Revised 47 CFR 64.1200(a)(10) and (a)(11) require a revocation to be honored within ten business days and do not say what "honored" consists of. The comment defines three operations: a permission record at receipt, cancellation of communications the caller still controls, and a send-time read. It ties those operations to the timeframe questions, the category-limit question, silence, one-way texting, and affiliate identity. It does not invent a cost, a prevalence count, or a seven-day recommendation. Other comments already ask for shorter clocks. This one answers a different question.

What can be shortened without removing that answer:

- The recital of the six-day, immediate, and ten-day clocks already in the section. One sentence is enough.
- The in-comment walkthrough of the nine fixture cases, if the appendix is attached. The comment needs the limitation paragraph, not each case.
- The restatement of the existing one-way disclosure rule. Keep the condition that the alternative must perform the three operations.
- Section IV, except the IRFA heading, the statement that there is no cost study, and the statement that the proposal adds no second consumer-facing clock.

Those cuts would land near 1,600 words. Do not cut the three-operation definition, the same-interaction all-categories condition, the silence rule, or the stored affiliate fields.

What becomes public if it is filed: the filer's full legal name and U.S. mailing address, the date, and the comment text. A telephone number or email is public if it is added. 47 CFR 1.419(e) requires the name and address, or an attorney's name and address. Comments are posted without change. Do not add a phone number unless you want it public.

**Blocker:** approval, name, and address. File on a weekday on or before Wednesday, November 25, through ECFS, CG Docket No. 02-278, as comments on FR Doc. 2026-21820. Do not email staff. An order by February 15 is not a supported forecast. The filing is the November result.

## PREPARE FOR DECEMBER

### NIST metrology scaffold

The empty `research/D1/` and `research/D2/` directories are not a reason to drop the Center. They are a reason not to write a metric yet. The scaffold is `execution/phase1/drafts/nist-metrology-structure.md`. It lists the ten source files, the three NIST gates (references about the metric, a public implementation that calculates it, a published contact email), the methodology questions, and the novelty questions. Every evidence field is blank.

**Blocker:** those files, plus references and a public implementation. When they arrive, read the stored result and the authors' limitations before writing a definition. Pull request 19 is the precedent for a new method grounded only in the submitter's note: the reviewer asked for independent support, and a later comment said to resubmit. No metric YAML has been merged, so February 15 is not an established acceptance date. December is for filling the scaffold if the files show up, not for opening a pull request that asserts results.

### NIST information-quality pathway

No current request. The only matter on the NIST log that was opened, Bernstein on NIST IR 8545, ended in a final denial, and a NIST IR was treated as outside the guidelines. No other qualifying false statement was found. A future request requires a demonstrated error in a dissemination the guidelines cover. Until that error is in hand, there is nothing to draft.

### Already submitted, no new action

- AISVS issue 1232 and maintainer pull request 1236. Leave the pull request untouched. Do not open another.
- AI Exchange pull request 287. Wait.
- DPV issue 484. Wait. Do not send a second comment.

## PREPARE FOR FEBRUARY

### Another OWASP audit

Not while 1236 and 287 are the open thread. A focused audit can start after 1236 has merged or a reviewer has asked a question that closes the fail-closed point, and after 287 has a decision. Do not repeat 9.5.8, the fail-open sentence, or the issues already marked abandoned in the tracker. AISVS 9.5.7 stays in this bucket. The Level 2 versus Level 3 collision with 9.5.6 is still unresolved, and filing it beside 1236 is the wrong month.

### DPV issue 486

Deprioritized. The 9 September 2026 minutes already select `dpv:FulfilmentOfObligation`. A comment that repeats that choice is not a new technical contribution. Implementing it would edit generated vocabulary, which the contribution guide reserves to the group, and no maintainer has authorized this account to make that commit. Reopen only if a maintainer asks for the change to be implemented, or if a later vocabulary state contains a defect the minutes did not already decide. The parent was still `dpv:LegalObligation` on 2026-11-19. That fact keeps the item alive. It does not make it this month's work.

### GPC test, if the pull request is not opened in November

If approval slips past November, the drafted test is the February item. Do not reopen the specification question. Do not file a Chromium bug in parallel unless a reviewer asks for one.

### California, if the letter is mailed in December

Watch for the written decision. A denial is the result section 11340.7(a) permits. Do not treat silence after 30 days as approval. Do not start a second petition in order to have two filings.

## DROP

### CPPA automated-decision, audit, and risk-assessment rules

The rules are adopted, approved by OAL on September 22, 2025, and effective January 1, 2026. The one drafting seam is real: section 7010 cites section 7200(a), while section 7200(b) delays "the requirements of this Article" until January 1, 2027 for a business already using ADMT. A petition filed in November 2026 can produce a 30-day letter. It cannot produce an effective amendment before that date. On January 1, 2027 the two readings require the same conduct. The other provisions that were read, including the appeal exception in section 7221(b)(1) and the risk-assessment cross-references to Civil Code section 1798.140, can be applied as written. Adding a stricter human-review duty would be a policy choice the Agency removed in the final statement of reasons.

### Department of Insurance

No adopted regulation on underwriting or claims algorithms was found. The November 13, 2026 announcement says the December 15 workshop is not a notice of proposed action and that no new AI regulation is being adopted that day. Bulletin 2022-5 is guidance. Insurance Code section 10123.135(j) is a statute. Paragraph (5) says Department guidance under that paragraph is not subject to the Administrative Procedure Act. A section 11340.6 petition cannot amend the statute and cannot amend guidance the statute has taken out of the chapter.

### Department of Technology

The Statewide Information Management Manual is departmental policy. It was not shown to be a title of the California Code of Regulations. Section 11340.9(d) also removes internal-management rules from the chapter. A petition to "adopt SIMM" would be a request for a new regulatory program, not a correction of an existing section.

### Civil Rights Council contractor package, as an ADS candidate

The Council's rulemaking page places an automated-decision approval paragraph under the contractor heading and dates it January 7, 2026. The linked final text is the contractor nondiscrimination clause, title 2, subchapter 5, not a second automated-decision rule. The webpage sentence is not itself a regulation. No petition is proposed against it.

### DMV driverless testing

Title 13, section 227.42 is a permit application for testing vehicles without a driver in the seat. The text that was opened does not contain a contradiction about a person's consent, a revocation, or an automated decision about a consumer. No petition is proposed.

### NIST correction ideas that were considered and rejected

NIST IR 8545 Table 5, the undefined "SI" on the Metrology Center page, and the catalog labels that the YAML schema does not use. None is a demonstrated false statement in a dissemination the information-quality guidelines were shown to cover.

## What changed from the first ranking

The first list treated an empty research directory, a missing name, and an unsent draft as reasons to drop or defer the pathway. Those are blockers for a particular filing. The GPC test is now an executed official run. The California citation remains the petition candidate because it changes which definition the automated-decision duties use. NIST stays a February submission path with a blank scaffold. DPV 486 moves behind GPC, the petition, and the FCC deadline.
