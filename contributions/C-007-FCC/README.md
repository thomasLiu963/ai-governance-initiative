# C-007 — Comment on FCC 26-67 Further Notice

Status: draft for internal review by 2026-11-23. Not filed. Submission is `none`. No Electronic Comment Filing System submission, paper filing, email, or other contact with the Commission has been made. Sending this directory to Commission staff would be an ex parte presentation in a permit-but-disclose proceeding.

The paste-ready comment is [COMMENT.md](COMMENT.md). Delete the internal status block above the caption before any later filing, and replace every bracketed field. The technical appendix is [APPENDIX.md](APPENDIX.md). The fixture it describes is `audits/fcc/sim_revocation.py`, which this draft does not modify. `audits/fcc/AUDIT.md` was left unchanged.

## Decision

The Further Notice is still open. Comments are due 2026-11-25. Reply comments are due 2026-12-28. The synthesis drop treated 2026-11-30 as the review date and concluded that internal review could not finish before the comment deadline. Review of this draft is scheduled for 2026-11-23, which is before that deadline. That calendar correction is not a reason to file, and it is not a reason to adopt the audit's text unchanged.

A narrow comment is justified. Revised 47 CFR 64.1200(a)(10) and (a)(11) require a revocation to be honored within ten business days and do not identify a permission record, cancellation of a communication the caller still controls, or a read of that record at origination. Paragraphs (b)(3) and (d)(3) require an immediate record only for narrower classes of calls. Shortening the maximum, or splitting it for exclusive-means callers, would not add those operations. Paragraphs 30 and 31 of FCC 26-67 ask the timeframe question on the premise that automated means make processing faster. The speed of a label is not the speed of the record or of the origination check. That is the technical increment beyond the existing rules.

The same record does not justify several choices the Further Notice also asks about. This draft does not recommend seven business days, a second consumer-facing clock, a ban on one-way informational texting, an extension of paragraph (d)(5), or the paragraph (a)(13) quoted in footnote 84. It does not answer whether the statute requires an account-wide revocation. It does not treat the fixture as evidence of carrier behavior, cost, or consumer intent. It does not ask the Commission to undo exclusive means, category-limited informational revocation as a framework, or the financial-institution reliable-source amendment.

## What was read on 2026-11-18

- FCC 26-67 PDF, adopted 2026-09-30, released 2026-10-01: <https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf>. Paragraphs 3, 24, 26, 28–39, and 43, footnotes 70, 77, and 84, and Appendix A were read from that file. The September 9, 2026 fact sheet uses different paragraph numbers and was not used.
- Federal Register final rule, 91 FR 67214, FR Doc. 2026-21821: effective 2026-11-25. The amendatory text of paragraphs (a)(10), (a)(11), and (a)(12) matches Appendix A.
- Federal Register Further Notice, 91 FR 67239, FR Doc. 2026-21820: comments due 2026-11-25, reply comments due 2026-12-28. Sections B through F match paragraphs 30–39. The Initial Regulatory Flexibility Analysis asks for comments identified as IRFA responses.
- eCFR 47 CFR 64.1200, unofficial edition, displayed on 2026-11-18 the pre-amendment paragraphs (a)(10), (a)(11), (a)(12), (b)(3), (d)(3), and (d)(5), and the immediate and six-business-day opt-out provisions cited in the comment.
- 47 CFR 1.49, 1.415, 1.419, and 1.1206, from eCFR.
- FCC rulemaking-process page, <https://www.fcc.gov/about-fcc/rulemaking-process>, including the statement that comments are generally posted without change and that an ECFS filer includes a full name, a mailing address, and the docket number.

No AI-assistance disclosure rule for comments appears in the Further Notice or in 47 CFR 1.415 or 1.419. The comment does not invent one. This draft was prepared with AI assistance in research and drafting. A person checks every quotation against the cited source before any external use.

## Filing path, if a person later approves it

1. Internal approval has to be recorded before any submission. This file does not record that approval.
2. File in CG Docket No. 02-278 through <https://www.fcc.gov/ecfs>. Electronic filers submit one copy under 47 CFR 1.419(d). The transmittal screen asks for the filer's full name, mailing address, and the docket number. 47 CFR 1.419(e) requires the filer's name and mailing address, or an attorney's name and mailing address if the party is represented. Do not file with bracketed placeholders.
3. Identify the submission as comments on the Further Notice, FR Doc. 2026-21820. The Report and Order in the same FCC number is already adopted.
4. Keep the heading "Response to the Initial Regulatory Flexibility Analysis." Paragraph 43 requires a separate heading for IRFA comments.
5. 47 CFR 1.49(f)(4) counts an electronic filing at no more than 250 words per page for length limits. The Further Notice states no page limit. 47 CFR 1.49(b) and (c) require a table of contents and a summary when a filing exceeds ten pages under that computation. On 2026-11-18 the comment text below the caption was 2,202 words, under ten pages at 250 words per page. Recompute the word count if the text is edited. Paper format under 47 CFR 1.49(a), if anyone uses it, is 12-point type, double-spaced body, and the margins stated in that paragraph. The Further Notice's paper addresses are 9050 Junction Drive, Annapolis Junction, MD 20701, for hand and courier delivery, and 45 L Street NE, Washington, DC 20554, for U.S. Postal Service delivery. Electronic filing is the path the Register asks for first.
6. The proceeding is permit-but-disclose under 47 CFR 1.1206. A written ex parte, or a memorandum of an oral ex parte, is due in the docket within two business days, in a native format when electronic filing is feasible. Do not email Richard D. Smith or any other staff member with this draft. The contact line in the item is Richard.Smith@fcc.gov, (717) 338-2797.
7. 47 CFR 1.415(c) provides a time for reply comments, which the Register sets at 2026-12-28. 47 CFR 1.415(d) provides that no additional comments are filed unless the Commission requests or authorizes them. If internal review is not finished before 2026-11-25, do not file this comment late and do not recast it as a reply. A reply responds to comments already filed.
8. Do not attach `audits/fcc/AUDIT.md`, this README, or unpublished project files. The appendix may be attached only with the limitations in its first paragraphs intact.

## Reproduce

From the workspace root:

```bash
python3 contributions/C-007-FCC/reproduce.py
```

The script imports `audits/fcc/sim_revocation.py`, writes `results/report.txt`, and exits nonzero if any assertion fails. The report's first section states what a pass does not prove.

## Not verified

- The June 30, 2026 joint-letter attachment, and the EEI, Vibes, NCLC, ABA, and REACH filings, except where FCC 26-67 quotes or describes them.
- The CGB orders cited as 40 FCC Rcd 2395 and DA 26-12. Paragraph 24 of FCC 26-67 and the Federal Register effective date were read. The waiver orders were not.
- 47 CFR 1.46. No extension is requested.
- The United States Code text of 47 U.S.C. § 227, beyond the "called party" citation in FCC 26-67 footnote 80. The comment does not interpret that term.
- ECFS filings already submitted on this Further Notice. This draft does not claim that the operational definition is absent from other comments.
- Prevalence of one-way texting, the cost of any honor period, small-entity burden, carrier or vendor behavior, and model labeling. No paid inference was run.
- The filer's name and mailing address. Both are required before an electronic filing and both are unknown here.
