# Opportunities

Date of research: 2026-11-19. Each row states what was re-read, how the earlier closure should be classified, and whether a filing is justified. Drafts are local. None has been sent.

## Reevaluation of the earlier privacy and insurance closures

### Sections 7010 and 7200 — compliance dates

Classification: the seam is real, and it is already given an end date by the regulation itself. It is not a permanent conflict, and it is not outside the Agency’s authority.

Section 7010(c) and (d) tie the pre-use notice and the opt-out link to a business that “uses ADMT as set forth in section 7200, subsection (a).” Section 7200(b) gives a business that already uses automated decisionmaking technology until January 1, 2027, to comply with “the requirements of this Article.” A reader can treat the Article 2 duties as due on January 1, 2026, or as delayed with Article 11. On January 1, 2027, both readings require the same conduct. A petition filed in November 2026 can produce a written decision inside 30 days. It cannot produce an amended section that changes anyone’s duty after the seam closes. An adopted regulation can be amended. This one does not need an amendment in order for the two readings to converge.

### Delete Act proposal — the three items closed on November 19

Classification: those three items were already addressed by the statute or by the statement of reasons. They are not reopened.

The change from 45 days to 30 calendar days in section 7612(a) restates Assembly Bill 883. The statement of reasons says the 45-day limit on changing deletion-list selection is deleted because it fights the shorter access cycle. The ZIP-code rule, first five characters and then strip leading zeros, is explained as the platform’s match key. The March 1, 2028, through March 1, 2029, example, with a report due May 30, 2029, is 90 days after March 1. Section 7630(a)’s first report date of November 1, 2028, sits in subsection (a). The 90-day sentence in subsection (c)(2) is in the paragraph that applies after the first audit. That date was not turned into a separate comment.

### Department of Insurance workshop

Classification: not suitable for a petition or for a comment under Government Code section 11346.9. The Department has authority to adopt title 10 regulations later. It has not adopted an artificial-intelligence section, and it has not noticed one.

Bulletin 2022-5 and the utilization-review guidance remain outside the code. Insurance Code section 10123.135(j)(5) says the guidance issued under that paragraph is not subject to the Administrative Procedure Act. A workshop comment due December 12, 2026, would be a policy essay on a record that has no text and no duty to respond. That comment is not drafted.

### Assembly Bill 566 and section 7025

Classification: the earlier closure was that no notice had been published. That part remains true on this date. The closure does not mean the adopted section is frozen, and it does not mean the Board packet can be ignored.

Civil Code section 1798.136, operative January 1, 2027, requires a business that develops or maintains a browser to offer a configurable opt-out preference signal. The Agency “may” adopt regulations. The November packet uses the statutory definition of “browser” in a new section 7025(h) and still has not been noticed. The right instrument, once a notice exists, is a comment. A petition to invent a browser code before that notice would duplicate a package the Board has already been asked to start.

### Global Privacy Control findings from this project

Classification: one finding is a California implementation gap. One finding is not a California violation.

The Working Draft of September 24, 2026, tells a user agent to send `Sec-GPC` with the value `1`, and it tells a server to honor the field when a value is exactly `1`. Issue 114 on `w3c/gpc` records that ordinary HTTP combination turns two `Sec-GPC: 1` lines into one field value `1, 1`, which the exact-match sentence ignores. Anne van Kesteren’s October 23, 2026 comment says the parser has to operate on the combined value. Title 11, section 7025(b)(1), requires a business to process a commonly used HTTP header and, in the Board packet, names Global Privacy Control as the example. It does not say how to read a combined field. Civil Code section 1798.185(a)(18) tells the Agency to adopt technical specifications for the signal. A sentence that treats `1`, `1, 1`, and `1, 0` as the signal, and `0` or an empty value as not the signal, states the business’s existing duty in a way a reviewer can test. It does not incorporate the W3C draft. It does not assert that the draft and the statute conflict.

The navigation-cache finding is different. The same Working Draft says a preference change is not reflected until the next top-level navigation. A local Chrome run recorded an already loaded document changing immediately. That is a difference between a browser and a draft user-agent rule. It is not a finding that the browser violated title 11 or the Civil Code. Section 7026 tells the business to stop selling or sharing as soon as feasibly possible after the business receives the request. It does not tell the browser when to update a loaded document. A comment that treated the Chrome result as a California violation would manufacture a conflict. That comment is not drafted.

## Candidates that survive

### P-1. Open comment — title 11, section 7614(b)(2)(B)

The proposed status “record opted out of sale” tells the broker to do what “section 7613(b)(2)(B)” requires. Current section 7613, effective January 1, 2026, places the multiple-consumer opt-out at subsection (a)(2)(B). Subsection (b) is the deletion and suppression rule. It has paragraph (1) and no paragraph (2). The statement of reasons says the proposal keeps the multiple-consumer duty at (a)(2)(B) and points the suppression duty at (b)(1)(B). Proposed section 7632(e)(6)(E) already cites section 7613(a)(2)(B) for the same opt-out. The status sentence and the audit sentence, in one package, name different subsections.

A broker who follows the status citation does not find the opt-out rule. The status is what the consumer later sees: deleted, exempted, opted out of sale, or not found. The citation decides which of those is lawful when one identifier matches more than one person.

This is a comment in a noticed proceeding. Draft: `comment-drop-7614.md`. The same comment asks that the hashing example say “date of birth” where the current and proposed examples say “data of birth.” That second point is a spelling correction inside an example the proposal is moving. It is included because the comment is already being written. It is not a separate filing.

Authority: Civil Code section 1798.99.87. The Agency is amending sections it has already adopted under that section.

Challenge. The Delete Act is not preempted by the CCPA; the status rule implements section 1798.99.86. The Agency has jurisdiction. Existing section 7613(a)(2)(B) already states the duty, so the comment does not create a new consumer right. It makes the new status sentence point at the duty the audit section already names. Section 100 is the wrong instrument while an Article 5 proceeding on the same section is open. A duplicate petition is not drafted.

What a favorable result can be called, if it happens: the Agency’s adopted data-broker text cites section 7613(a)(2)(B) in the “record opted out of sale” status. A final statement of reasons that rejects the comment is a different, narrower result. The comment itself is not that result.

### P-2. Held comment — opt-out preference signals and two automated-decision sentences

Do not send until the notice is in the Notice Register. Draft: `comment-oops.md`. Re-read the colored proposed-text PDF that day. The extraction used here does not preserve underline and strikeout. Points that are already clean in color should be deleted before sending. Points that do not depend on color are the receiver sentence, the browser-feature sentence, and the section 7026(g) citation in the current code.

The comment asks for five things.

1. A receiver sentence for `Sec-GPC`. After combination, split on commas, trim whitespace, and treat the request as an opt-out if any item is the single character `1`. This is the technical specification section 1798.185(a)(18) describes. The packet’s new section 7026(f)(3)(C) assumes the business can tell whether the signal arrived before it sets a sale-or-share cookie. Exact equality to `1` fails that test for a combined value.

2. Section 7025(h) should do what the statement of reasons describes, and only that. The proposed sentence forbids a browser feature from preventing the signal from being sent. The statement of reasons says a feature that discloses personal information must also forward the signal. A feature can make its own request without the signal and still leave ordinary navigations untouched. The requested sentence is: a request the feature itself makes carries the same opt-out preference signal the browser would send on a consumer-initiated navigation, and it does not carry a contradictory value. The reference note should add Civil Code section 1798.136, because subsection (h) uses the definition in section 1798.136(e)(1). The sentence should not be extended to a chatbot that is not a browser. Section 1798.136 defines a browser as an application used to locate, access, and navigate websites. Senate Bill 243 and the vetoed Senate Bill 903 are different statutes and different agencies.

3. Section 7026(g) should cite section 7025(c)(6). The current compilation and the proposed text both cite subsection (b)(6). Subsection (b) stops at (2). Subsection (c)(6) is the display duty and uses the same example.

4. If the operative section 7221(b)(2)(A) still reads “ability to performance at work or performance in an educational program,” replace that clause with “performance at work or performance in an educational program.” Those are the defined terms in section 7001(cc) and (dd). The statement of reasons says that replacement is the point of the edit. The current code says “ability to perform at work or in an educational program.” The extracted proposal is not that sentence and is not the defined-term sentence.

5. If the operative section 7222(b)(1) still reads “to make a significant decision improve our services,” use one example. The statement of reasons says “improve our services” was replaced with “make a significant decision” so the forbidden generic description matches Article 11.

Challenge on the receiver sentence. It regulates the business that receives the header, which section 7025 already regulates. It does not regulate the browser manufacturer. It can become stale if a later signal uses a different token. The sentence is therefore tied to the character `1` that the regulation’s own example, Global Privacy Control, uses, and the comment says the Agency can name a successor value in a later amendment. It is not a section 100 change. It is a specification inside a proceeding whose draft notice says the amendments mostly clarify duties the Agency already enforces. The Agency may reject it as too specific. That risk is why it rides with the citation fixes rather than standing as a petition to open a new technical code.

Challenge on subsection (h). Section 1798.185(a)(18) authorizes specifications for a signal sent by a platform, browser, or device, and it says those specifications should be updated as the means of interaction change. Section 1798.136(c) authorizes regulations to implement the browser duty, and that section is not operative until January 1, 2027. A notice published in late 2026 is unlikely to produce an effective regulation before that date, after the 45-day comment period, adoption, and Office of Administrative Law review. If the Agency publishes subsection (h) with an effective date before January 1, 2027, the definition it borrows is not yet operative. The comment asks for an effective date on or after that day for subsection (h), and for the reference citation either way. Subsection (h) should not be used to smuggle a general rule for artificial-intelligence assistants.

The navigation-cache result is omitted on purpose.

What a favorable result can be called, if the noticed text later includes it: the regulation states that a combined `Sec-GPC` value containing the token `1` is an opt-out preference signal, or the automated-decision exception uses the defined terms “performance at work” and “performance in an educational program.” “Accepted for formal consideration” is not the right description of a comment that has only been placed in the file. Placement in the file is what the notice already requires the Agency to do with every timely comment. The verifiable decision is the final statement of reasons, and adoption is a later Board and Office of Administrative Law act. Neither is claimed for February 15, 2027. A notice published in late November 2026 produces a comment deadline about 45 days later, in January 2027. A final statement of reasons before February 15 is possible and is not established.

### P-3. Held petition — section 7026(g) only

Draft: `petition-7026-hold.md`. Send only if the opt-out notice is still absent from the Notice Register on December 12, 2026. By then the workshop date is a convenient checkpoint, and a petition received in mid-December can still draw a written decision under Government Code section 11340.7(a) before February 15, 2027. If the notice has been published, do not send the petition. The comment in P-2 covers the same citation, and two filings on one clause waste the Agency’s 30-day clock.

The petition asks for one change: “section 7025(b)(6)” becomes “section 7025(c)(6).” The Agency’s own January 2026 explainer cites sections 7025(c)(6) and 7026(g) together for that example. The code cites a paragraph that is not in section 7025(b).

Classification: the citation is defective as published. It is not outside the Agency’s authority. It has not been corrected by the January 1, 2026 compilation. Title 1, section 100, may be available if the Office of Administrative Law agrees the change has no regulatory effect, because the cited paragraph does not exist and the example words already appear in subsection (c)(6). The petition leaves that choice to the Agency and the Office. It does not assert that section 100 will be used.

A written denial, or a written decision to proceed, published in the Notice Register, is the result section 11340.7 can produce by February 15 if the letter is received in December. An amended code section by that date is not claimed.

## Closed after this pass

| Target | Classification |
| --- | --- |
| Sections 7010 and 7200 | The regulation’s own date ends the seam on January 1, 2027. |
| DROP 30-day cycle, ZIP-code rule, and section 7630(b) example | Consistent with Assembly Bill 883 and the statement of reasons. |
| DROP 45-day list-selection lock | The statement of reasons strikes that sentence. |
| Insurance workshop and Bulletin 2022-5 | No adopted section and no noticed text. Authority to regulate later is intact. Utilization-review guidance is outside the Administrative Procedure Act by statute. |
| Attorney General regulations | No open consumer-privacy rulemaking in the registers read. Enforcement is through the Agency’s title 11 rules and through cases. |
| Department of Consumer Affairs, Board of Psychology, Board of Behavioral Sciences | Assembly Bill 489 and Assembly Bill 1979 are statutes. Senate Bill 903 was vetoed on September 30, 2026. No contrary title 16 sentence and no open notice were found. |
| Senate Bill 243 companion chatbots | Self-executing Business and Professions Code duties. Reports start July 1, 2027. No implementing notice was found. |
| Department of Financial Protection and Innovation PRO 07-24 | The second invitation closed February 26, 2026. |
| Franchise-broker notice Z2026-1027-04 | A title 10 registration proposal. Not read as a privacy or automated-decision rule. |
| W3C navigation-cache failure | A browser-versus-draft observation. Not a title 11 violation. |
| A new automated-decision code for insurance, housing, or chatbots | A policy project. No broken adopted sentence was located. |

## What was not verified

- The colored underline and strikeout in the October 8, 2026 opt-out text. The extraction used for sections 7221 and 7222 may have joined words the color PDF already resolves.
- Official minutes and the vote tally of the November 5–6, 2026 Board meeting.
- Notice Register No. 47-Z, which had not been posted.
- Whether the Agency has said, in a regulation or a posted policy, that it accepts a Government Code section 11340.6 petition by email. The comment address on a noticed proposal is not treated as that statement. The held petition uses mail.
- The full text of every audit paragraph beyond the citations checked in sections 7630, 7632(e)(5), and 7632(e)(6).
- Any title 16 section outside the searches described in `SOURCE_LOG.md`.
