# CalPrivacy — substantive gaps

DRAFT — NOT FILED. Prepared 2026-11-20. Do not email the opt-out text in this file.

A person checks every quotation against the colored PDF and the Notice Register on the day of sending. This draft was prepared with AI assistance.

## Status on November 20, 2026

Two proceedings are different.

| Proceeding | Status | Comment window |
| --- | --- | --- |
| Opt-out preference signals, title 11, sections 7025, 7026, 7060, 7102, 7122, 7124, 7157, 7221, and 7222 | Board packet for November 5–6, 2026. Proposed text dated October 8, 2026. Draft notice and initial statement of reasons dated October 12, 2026. Staff memorandum dated November 6, 2026. The draft notice still reads “Notice published [date].” The written-comment date and the hearing date are blank. https://cppa.ca.gov/regulations/ still describes opt-out preference signals as preliminary rulemaking. The preliminary period closed April 6, 2026. | None. An email to regulations@cppa.ca.gov, or to a preliminary-comment address, is not a comment under Government Code section 11346.9 until a notice of proposed action is in the California Regulatory Notice Register. |
| Data broker updates and DROP audits, title 11, sections 7601–7604, 7610, 7612–7616, 7620, 7621, and 7630–7633 | Notice of proposed rulemaking, published November 13, 2026. The Agency’s regulations page lists this as the open formal proposal. | Written comments close at 5:00 p.m. Pacific Time on January 6, 2027. Email regulations@cppa.ca.gov. Subject: `Public Comment on Data Broker Updates and DROP Audit Regulations`. Hearing the same day at 10:00 a.m. Pacific Time. https://cppa.ca.gov/regulations/drop_audits |

The November index of the Notice Register, read on November 20, 2026, lists No. 45-Z (November 6) and No. 46-Z (November 13). It does not list a later register, and it does not list an opt-out notice. No. 47-Z, if it is published later on November 20, has to be read before anyone treats this status as current. A secondary account reports that the Board voted on November 6 to commence formal opt-out rulemaking. Official minutes were not retrieved. A vote to commence rulemaking is not a notice.

The accomplishment, for either proceeding, is adopted regulatory text. A timely opt-out comment, once a notice exists, must be answered in the final statement of reasons. That answer is formal consideration. It is an acceptance if the filed regulation contains the requirement. A data-broker comment filed by January 6, 2027, has the same structure. A receipt, a hearing appearance, and the final statement of reasons are different events. Adoption follows a Board action and Office of Administrative Law review. A notice published in December 2026 can put an opt-out comment in the file by February 15, 2027. A filed opt-out regulation by that date is not established.

## Already in the adopted rule or in the October packet

These are not open gaps. The held comment does not ask the Agency to add them again.

| Topic | Where it already is |
| --- | --- |
| A business processes a commonly used opt-out preference signal, including an HTTP header | Title 11, section 7025(b), effective January 1, 2026. The October 8 text keeps that duty. |
| Global Privacy Control named as an example of that header | Proposed section 7025(b)(1). Initial statement of reasons, pages 3–4. |
| The signal covers the browser or device and a pseudonymous profile the business already associates with it | Section 7025(c)(1). Proposed examples (c)(7)(G) and (H). The statement of reasons, pages 4–5, uses the Attorney General’s February 11, 2026 Disney complaint for the principle that a business which can associate devices for advertising can associate them to honor an opt-out. |
| Cookie syncing for cross-context behavioral advertising stops when a signal is present | Proposed section 7025(c)(7)(F), first sentences. The last sentence of that example is the gap in item 3 below. |
| Setting a sale-or-share cookie before determining whether the signal arrived is not compliance “as soon as feasibly possible” | Proposed section 7026(f)(3)(C). Statement of reasons, pages 5–6. |
| Metrics, including how many opt-out requests arrived through a signal, including for a business that must conduct a cybersecurity audit or a risk assessment | Proposed section 7102. Statement of reasons, pages 7–8. |
| A human reviewer with authority to overturn a significant decision, as the general exception to an automated-decisionmaking opt-out | Adopted section 7221(b)(1). The October text keeps the authority to overturn and the authority to change the decision. The hiring exception in (b)(2) is item 5 below. |
| The hiring exception’s defined terms, and the access example’s purpose clause | Statement of reasons, page 8. Proposed section 7221(b)(2)(A) replaces “ability to perform at work or in an educational program” with “performance at work” and “performance in an educational program,” the defined terms in section 7001. Proposed section 7222(b)(1) replaces “improve our services” with “make a significant decision.” The extracted text joins the old words to the new words. That join is the strikeout sitting next to the underline. On the colored PDF, confirm the operative clause. If it matches the statement of reasons, do not comment on the wording of those two replacements. |
| Deletion of inferences by a data broker | Proposed section 7613. Personal information associated with a matched identifier includes inferences. The deletion duty includes inferences drawn from personal information collected from a third party or outside a first-party interaction. |
| A data broker’s automated connection to DROP | Proposed section 7612. The broker may use automated means the platform supports, and a failed connection has its own notice. That is an operations rule. It is not a consumer-autonomy gap. |

Authority line on the draft opt-out notice: Civil Code section 1798.185. The reference line lists sections 1798.100, 1798.105, 1798.106, 1798.110, 1798.115, 1798.120, 1798.121, 1798.125, 1798.130, 1798.135, 1798.140, and 1798.185. Section 1798.136 is not in that list. The note under proposed section 7025 cites sections 1798.120, 1798.135, 1798.140, and 1798.185.

## Evidence from the Global Privacy Control work

Two findings are in this workspace. They support different sentences. Neither finding is a holding that a browser violated California law.

**Combined field value.** Global Privacy Control, W3C Working Draft, September 24, 2026, section “The `Sec-GPC` Header Field for HTTP Requests,” tells a user agent to send a field value that is exactly the character `1`, tells a user agent not to send more than one `Sec-GPC` line, and tells a server to ignore the field unless the value is exactly `1`. The same paragraph says that if multiple `Sec-GPC` headers are present and at least one value is exactly `1`, the server treats the request as a single `Sec-GPC: 1`. https://www.w3.org/TR/2026/WD-gpc-20260924/ Ordinary HTTP combination can present those two lines as one field value, `1, 1`. A comparison that accepts only a value equal to the single character `1` then drops the opt-out. W3C issue 114 is the open receiver issue. On October 23, 2026, Anne van Kesteren wrote that the parser has to operate on the combined value. https://github.com/w3c/gpc/issues/114 The audit is `audits/w3c-gpc/AUDIT.md`.

That finding is about the business that receives the header. Title 11 regulates that business. Civil Code section 1798.185(a)(18) authorizes technical specifications for an opt-out preference signal. The sentence in item 1 does not incorporate the W3C draft, and it does not regulate the browser. A user agent is not supposed to send two lines. The sentence covers the case in which processing has combined the lines anyway.

**Already loaded document.** The same Working Draft, section 3.2, caches the preference for a top-level document until the next top-level navigation. The project’s question, filed November 18, 2026, asks whether an already loaded document keeps that cached value. https://github.com/w3c/gpc/issues/165 A local Chrome 157 session, recorded in `contributions/T005-GPC-WPT/`, observed `navigator.globalPrivacyControl` and `Sec-GPC` change in the already loaded document after a WebDriver set command, with no navigation. That session was not `./wpt run`. It is evidence that the header sent on a request and the script-visible property in a document can be specified, and implemented, differently. It is not evidence that Chrome violated title 11. Title 11 does not regulate when a browser updates a document that has already loaded. Item 2 uses the divergence only to tell the business which observation controls the request.

## Gaps the October opt-out packet does not close

Hold this language until a notice is in the Register. On that day, read the colored text. Delete any paragraph the underline and strikeout have already resolved. Set the deadline, the hearing, and the subject line from the notice. A separate approval then names the register number and the deadline.

### 1. How a business reads a combined `Sec-GPC` field

Proposed section 7025(b)(1) requires the business to process an HTTP header “like Global Privacy Control (GPC).” Proposed section 7026(f)(3)(C) treats the business as able to determine whether the signal arrived with the first request, before a cookie is set. Neither sentence states how the field value is read after repeated header lines have been combined.

Consequence. A consumer whose user agent sent `Sec-GPC: 1`, and whose request arrives with the combined value `1, 1`, receives no opt-out from a business that tests for the single character `1`. The sale or sharing the timing example describes can proceed. The consumer did not withdraw the preference. The bytes were combined.

Add this to section 7025, in or immediately after subsection (b):

> When the opt-out preference signal is the HTTP header field `Sec-GPC`, the business has received the signal if a field line with that name has a field value that is exactly the single character `1` once leading and trailing whitespace are removed. If the business’s HTTP processing combines repeated field lines of that name into one comma-separated field value before the business reads the value, the business has received the signal if any comma-separated item, once leading and trailing whitespace are removed, is exactly the single character `1`. The business shall not treat the field as absent solely because that combined value is `1, 1`, and it shall not treat another item in the combined value as cancelling an item that is `1`. A field whose only value is `0`, and an empty value, are not the signal.

A reviewer can test it. A request whose field value is `1`, or `1, 1`, is an opt-out. A request whose only value is `0`, or whose value is empty, is not. The sentence is tied to the character the regulation’s own example uses. If a later commonly used signal uses a different token, the Agency can amend the token.

Legal basis: Civil Code section 1798.185(a)(18), technical specifications for an opt-out preference signal, and section 1798.185(a)(4), rules for submission and compliance with an opt-out.

**Sentence that is accurate only if the adopted text matches this paragraph.** “The California Privacy Protection Agency adopted a rule that a business receiving the `Sec-GPC` header must treat a combined field value containing an item that is `1` as the consumer’s opt-out, and must not drop the opt-out because the combined value is `1, 1`.”

### 2. The header on the request controls that request

Proposed section 7025(b)(1) also gives “JavaScript object” as an example of a format, and it does not name `navigator.globalPrivacyControl`. Proposed section 7026(f)(3)(C) tells the business to determine whether the signal arrived with the first request. A script that reads the document’s property, after the document has loaded, is reading a second observation.

Consequence. A business that honors a script-visible `false`, and ignores `Sec-GPC: 1` on the request that fetched the document, sells or shares personal information the consumer’s request had already opted out. The project’s navigation-cache question is the reason the two observations can disagree. The question does not establish that any browser’s result was unlawful.

Add this to section 7025, immediately after the combined-value sentence:

> The business determines whether a request carries the signal from that request. If the request’s `Sec-GPC` field meets this subsection, the business has received the opt-out for that request. A script-visible value in the document, including `navigator.globalPrivacyControl`, does not cancel the signal on that request. When the business reads `navigator.globalPrivacyControl` and the value is `true`, the business has also received the signal for the processing that read it.

Legal basis: the same subdivisions of section 1798.185. The sentence regulates the business. It does not tell a browser when to update a loaded document.

### 3. The cookie-syncing example narrows its last sentence to one signal

Proposed section 7025(c)(7)(F) begins with any opt-out preference signal: when Business SS receives an opt-out preference signal, it must not allow the third parties to initiate or perform cookie syncing. The last sentence of the same example requires Business SS to prevent that syncing “whenever it receives a GPC signal.” The statement of reasons, page 4, says the duty applies whenever an opt-out preference signal is present.

Consequence. A signal that meets subsection (b) and is not the named header satisfies the first sentence and fails the last. A business can treat the example as permission to keep syncing for every signal other than Global Privacy Control.

Replace the last sentence so that it uses “opt-out preference signal,” as the first sentence of the example and the statement of reasons do.

### 4. A browser feature that makes its own request

Proposed section 7025(h):

> If a browser, as defined by Civil Code section 1798.136(e)(1), has a feature, tool, or function that interacts with a business on the consumer’s behalf and that feature makes the consumer’s personal information available to the business, that feature must not prevent, interfere with, contradict, or disable the consumer’s opt-out preference signal or other setting indicating the consumer’s choice to opt-out of the sale or sharing of their personal information from being sent to the business.

The statement of reasons, page 5, describes a different duty: a browser feature that discloses personal information must also forward the consumer’s signal.

Consequence. A feature can leave ordinary navigations untouched and still omit the signal on a request the feature itself makes. The page address, a selection, or an account identifier can reach a business on that request without the opt-out the consumer configured. The consumer’s choice does not travel with the personal information the feature discloses.

Civil Code section 1798.136, added by Assembly Bill 566, Chapter 465, Statutes of 2025, is operative January 1, 2027. Subdivision (a) prohibits a business from developing or maintaining a browser that lacks consumer-configurable functionality to send an opt-out preference signal. Subdivision (c) authorizes regulations to implement that section. Subdivision (e)(1) defines a browser as “an interactive software application that is used by consumers to locate, access, and navigate internet websites.” Subdivision (e)(2) defines the signal as one that complies with the title and communicates the choice to opt out of sale and sharing. Subdivision (d) gives the browser developer immunity from a recipient’s violation of the title. The regulation can tell the feature to carry the signal. It should not make the browser developer liable for what the recipient does after receipt.

Replace subsection (h) with:

> If a browser, as defined in Civil Code section 1798.136(e)(1), has a feature, tool, or function that makes a request to a business on the consumer’s behalf, and that request makes the consumer’s personal information available to the business, the request must carry the same opt-out preference signal, if any, that the browser would send on a consumer-initiated navigation to that business. The feature must not send a contradictory value. This subsection is operative on or after January 1, 2027.

Add section 1798.136 to the reference note for section 7025. The sentence covers a browser as section 1798.136(e)(1) defines it. It does not cover a companion application that is not a browser.

### 5. The hiring exception has no person who can change the decision

Section 7221(b)(1) lets a business withhold an automated-decisionmaking opt-out when a human reviewer has authority to overturn the decision, reviews the output and the consumer’s information, knows how to interpret the output, and has authority to change the decision. Section 7221(b)(2) is a separate exception for admission, acceptance, and hiring. As proposed, it applies when the business uses the technology solely to assess performance at work or performance in an educational program, the technology works for that purpose, and it does not unlawfully discriminate. The October amendment changes the defined terms in (b)(2)(A). It does not add a reviewer.

Consequence. A consumer can be denied admission, acceptance, or a job by the technology, cannot opt out under section 7221, and has no appeal under subsection (b)(1) to a person with authority to change that decision. Labor Code section 1522, operative July 1, 2027, prohibits sole reliance and requires human corroboration for a disciplinary or termination decision. It does not cover admission or hiring. Title 2, section 11009(f) prohibits a discriminatory employment system. It does not give the consumer an appeal to a person who can change the decision.

The section is already in the draft notice, so this sentence belongs in the opt-out comment once the notice exists. It does not belong in a petition filed while the Agency is opening a rulemaking on the same section.

Add this to section 7221(b)(2), as a further condition of the exception:

> (C) The business provides the consumer the appeal described in paragraph (1), including a human reviewer who has the authority to change the decision.

Legal basis: Civil Code section 1798.185(a)(15), regulations governing opt-out rights for automated decisionmaking technology. The Agency has already decided that a human with authority to change the decision can justify withholding the opt-out. This sentence applies that decision to the hiring exception. An employer remains subject to the Fair Employment and Housing Act and, when it operates, to Labor Code section 1522 for discipline and termination.

### 6. Section 7026(g) cites a paragraph that is not there

The regulations effective January 1, 2026, and the extracted October 8 text, say a business may display “Opt-Out Request Honored” “in accordance with section 7025, subsection (b)(6).” Section 7025(b) has paragraphs (1) and (2). Section 7025(c)(6) is the display requirement, and it uses the same example. The statement of reasons describes typographical corrections in sections 7122, 7221, and 7222. It does not describe a correction of section 7026(g).

If the colored text still cites subsection (b)(6), the comment asks that the citation be subsection (c)(6). If the colored text already cites subsection (c)(6), delete this paragraph before sending. The same citation is the subject of the held petition in `execution/sprint3/california/privacy-consumer/petition-7026-hold.md`. If a notice is published, this comment is the vehicle and that petition is not mailed.

## Data-broker gap, in the proceeding that is open

The open notice is a real comment window. The comment is one email. It includes the two corrections already drafted in `execution/sprint3/california/privacy-consumer/comment-drop-7614.md` and the paragraph below. Two emails on the same notice are not required.

Proposed section 7614(b)(2)(A) tells a data broker to report “record deleted” when it has deleted personal information associated with a matched identifier, “even if some of the personal information is exempt from deletion.” Proposed section 7613 already requires deletion of non-exempt personal information, including inferences, and it already permits a suppression list limited to compliance with Civil Code section 1798.99.86.

Consequence. A consumer who later reads the status can see “record deleted” when non-exempt inferences remain, because the sentence is satisfied by deletion of any associated personal information. The status then confirms a deletion the regulation’s own deletion duty has not finished. Exempt information is a different case. The statute permits that information to remain. The status can say “record deleted” when only exempt information remains, if every non-exempt item is gone.

The extraction mixes strikeout and new text. On the day of sending, read the colored section 7614(b)(2)(A) and section 7613(b)(1)(B). If the operative sentence already limits “record deleted” to completion of the non-exempt deletion, delete this paragraph.

Add this to section 7614(b)(2)(A):

> The data broker reports “record deleted” when it has deleted every non-exempt item of personal information associated with the matched identifier, including an inference drawn in whole or in part from personal information that is not exempt. The code does not mean that exempt information was deleted. If any non-exempt item associated with the matched identifier remains, other than information kept solely on the suppression list under section 7613(b)(1)(B), the data broker shall not report “record deleted.”

Legal basis: Civil Code section 1798.99.87. The duty being reported is section 1798.99.86, as implemented by section 7613.

The citation correction in the Sprint 3 draft stays in the same email. Proposed section 7614(b)(2)(B) cites section 7613(b)(2)(B) for the multiple-consumer opt-out. The initial statement of reasons for this proposal places that duty at section 7613(a)(2)(B), and proposed section 7632(e)(6)(E) already cites (a)(2)(B). The status a consumer later reads should cite the subsection that contains the duty. The “data of birth” example should say “date of birth.” Those two corrections are already written. This file does not replace them.

Authority, deadline, and address for the combined data-broker comment are in `ACTION_QUEUE.md`.

## What stays out

- A rule that Global Privacy Control opts the consumer out of automated decisionmaking. The signal in Civil Code section 1798.136(e)(2) and in the W3C draft communicates a sale-or-sharing opt-out. Section 7221 is a separate right. Item 5 uses the appeal the Agency already wrote. It does not redefine the header.
- A claim that a Chrome result, a Web Platform Test, or issue 165 is a violation of title 11.
- A petition to amend section 7026(g) after an opt-out notice exists. The comment is the prescribed procedure for text the notice includes.
- A second data-broker email that repeats only the Sprint 3 citation.

## Sources opened for this draft

- Proposed opt-out text, October 8, 2026: https://cppa.ca.gov/meetings/materials/20261105_06_09_text.pdf and the Agency mirror at https://privacy.ca.gov/wp-content/uploads/sites/357/2026/11/20261105_06_09_text.pdf
- Initial statement of reasons, October 12, 2026: https://privacy.ca.gov/wp-content/uploads/sites/357/2026/11/20261105_06_09_isr.pdf
- Staff memorandum, November 6, 2026: https://cppa.ca.gov/meetings/materials/20261105_06_09.pdf
- Draft notice, October 12, 2026, with blank dates: https://cppa.ca.gov/meetings/materials/20261105_06_09_npr.pdf
- https://cppa.ca.gov/regulations/ and https://www.cppa.ca.gov/regulations/oops.html
- Notice Register index for November 2026, https://oal.ca.gov/november-2026-california-regulatory-notice-registers/ , read November 20, 2026. No. 46-Z, November 13, 2026.
- Data-broker notice, proposed text, and regulations page: https://cppa.ca.gov/regulations/drop_audits , https://cppa.ca.gov/regulations/pdf/data_broker_updates_and_drop_audits_nopr.pdf , https://cppa.ca.gov/regulations/pdf/data_broker_updates_and_drop_audits_topr.pdf
- Civil Code sections 1798.136 and 1798.185(a)(4), (a)(15), and (a)(18), from the Agency’s January 1, 2026 statute PDF and the chaptered text of Assembly Bill 566.
- Global Privacy Control, W3C Working Draft, September 24, 2026.
- Labor Code sections 1522 and 1524, Senate Bill 947, Chapter 859, Statutes of 2026.

## Not verified

- Official minutes and the vote count of the November 5–6, 2026 Board meeting.
- Notice Register No. 47-Z and any register published after the November 20 reading of the index.
- Underline and strikeout color. Joined words in sections 7221, 7222, and 7614 are treated as extraction artifacts where the statement of reasons states the intended replacement.
- Whether DROP’s consumer-facing status screen uses the words “record deleted” or a response code that the regulation maps to those words. The proposed text uses the words.
