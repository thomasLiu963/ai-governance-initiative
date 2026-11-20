# CalPrivacy — opt-out preference signals

DRAFT — NOT FILED. Date of reading: 2026-11-20.

Do not email this document. The formal comment period is not open. A message to the preliminary-comment address, or to regulations@cppa.ca.gov before a notice is in the California Regulatory Notice Register, is not a comment under Government Code section 11346.9.

On the day a notice is published, read the colored proposed text. Delete any paragraph below that the underline and strikeout have already resolved. Set the deadline, the hearing, and the email subject from that notice. Then a separate approval is required before sending.

## Status

| Item | Record |
| --- | --- |
| Regulations page | https://cppa.ca.gov/regulations/ still places Opt-out Preference Signals under preliminary rulemaking. The preliminary period closed April 6, 2026. https://www.cppa.ca.gov/regulations/oops.html says the same. |
| Formal proposal now open | Data Broker Updates and DROP Audit Regulations only. That is a different action. This document is not a comment on it. |
| Packet | Proposed text, October 8, 2026: https://cppa.ca.gov/meetings/materials/20261105_06_09_text.pdf. Draft notice and initial statement of reasons, October 12, 2026. Staff memorandum, November 6, 2026. |
| Draft notice | “Notice published [date].” Written comments close on “[date], at 5:00 p.m. Pacific Time.” Hearing date blank. Those blanks were still blank in the PDF read on 2026-11-20. |
| Registers | No. 45-Z, November 6, 2026, and No. 46-Z, November 13, 2026, do not contain this notice. No. 47-Z was not posted on the November index at the time of this check. |
| Minutes | Not retrieved. A secondary account says the Board voted to commence formal rulemaking. That account is not a notice. |
| Extraction | The text below was read from PDF text extraction. Underline and strikeout are not preserved. |

Authority line on the draft notice: Civil Code section 1798.185. Reference line on the draft notice: sections 1798.100, 1798.105, 1798.106, 1798.110, 1798.115, 1798.120, 1798.121, 1798.125, 1798.130, 1798.135, 1798.140, and 1798.185. Section 1798.136 is not in that list. The note under proposed section 7025 cites sections 1798.120, 1798.135, 1798.140, and 1798.185.

## Already in the adopted rule or in the October packet

These are not open gaps. The comment does not ask the Agency to add them again.

| Topic | Where it already is |
| --- | --- |
| A business must process a commonly used opt-out preference signal, including an HTTP header | Title 11, section 7025(b), effective January 1, 2026. The October 8 text keeps that duty. |
| Global Privacy Control as a named example of that header | Proposed section 7025(b)(1). The statement of reasons, pages 3–4, explains the addition. |
| The signal applies to the browser or device and to a pseudonymous profile the business already associates with it | Section 7025(c)(1), as set out in the October 8 text and quoted in the statement of reasons. Proposed examples (c)(7)(G) and (H), and the statement of reasons at pages 4–5, are the new illustrations, including the counterexample for a business that does not link devices. |
| Cookie syncing for cross-context behavioral advertising stops when the signal is present | Proposed section 7025(c)(7)(F), first sentences. Statement of reasons, page 4. |
| Setting a sale-or-share cookie before determining whether the signal arrived is not compliance “as soon as feasibly possible” | Proposed section 7026(f)(3)(C). Statement of reasons, pages 5–6, including the consent-management and tag-management sequence. The database’s proposed cookie-blocking sentence restates this example. It is not an additional amendment. |
| Metrics, including how many opt-out requests arrived through a signal | Proposed section 7102, as described in the statement of reasons, pages 7–8. |
| The hiring exception uses the defined terms “performance at work” and “performance in an educational program” | Statement of reasons, page 8: proposed section 7221(b)(2)(A) replaces “ability to perform at work or in an educational program” with those defined terms from section 7001(cc) and (dd). |
| The forbidden generic purpose in section 7222(b)(1) becomes “make a significant decision” | Statement of reasons, page 8. It replaces “improve our services.” |

The extracted proposed text shows “ability to performance at work or performance in an educational program” and “to make a significant decision improve our services.” Those joins match a strikeout followed immediately by the new words. They are not treated as the operative sentences. On the colored PDF, confirm that the operative clause matches the statement of reasons. If it does, do not comment on sections 7221 or 7222.

## Gaps the packet does not close

### 1. How a business reads a combined `Sec-GPC` field

This is the original recommendation supported by the project’s Global Privacy Control work. It is not in section 7025 as effective January 1, 2026. It is not in proposed section 7025(b)(1). It is not in the statement of reasons.

Proposed section 7025(b)(1) requires the business to process an HTTP header “like Global Privacy Control (GPC).” Proposed section 7026(f)(3)(C) treats the business as able to determine whether Violet’s GPC signal arrived with the first request, before a cookie is set. Neither sentence states how the field value is read after repeated header lines have been combined.

The W3C Working Draft of September 24, 2026, section 3.3, tells a user agent to send the field value `1`, and the receiver text has required an exact value of `1`. The same draft has also said that multiple `Sec-GPC` headers are honored if any one of them is `1`. Ordinary HTTP combination can deliver those two lines as one field value, `1, 1`. A comparison that accepts only a value equal to the single character `1` drops `1, 1`, and the timing test in proposed section 7026(f)(3)(C) never sees the signal. W3C issue 114 is the open parser issue. Anne van Kesteren’s October 23, 2026 comment states that the parser has to operate on the combined value. This project’s navigation-cache work is a different finding and is not used here. That finding is a difference between one browser and a draft rule for user agents. Title 11 regulates the business that receives the header. It does not regulate when a browser updates a document that has already loaded.

Civil Code section 1798.185 authorizes technical specifications for an opt-out preference signal. The sentence below is a specification for the header the regulation already names. It does not incorporate a W3C document. It does not regulate the browser. A user agent is not supposed to send more than one `Sec-GPC` line. The sentence covers the case in which processing has combined the lines anyway.

Add this to section 7025, in or immediately after subsection (b):

> When the opt-out preference signal is the HTTP header field `Sec-GPC`, the business has received the signal if a field line with that name has a field value that is exactly the single character `1` once leading and trailing whitespace are removed. If the business’s HTTP processing combines repeated field lines of that name into one comma-separated field value before the business reads the value, the business has received the signal if any comma-separated item, once leading and trailing whitespace are removed, is exactly the single character `1`. The business shall not treat the field as absent solely because that combined value is `1, 1`, and it shall not treat another item in the combined value as cancelling an item that is `1`. A field whose only value is `0`, and an empty value, are not the signal.

A reviewer can test it. A request whose `Sec-GPC` field value is `1`, or `1, 1`, is an opt-out. A request whose only value is `0`, or whose value is empty, is not. If a later commonly used signal uses a different token, the Agency can amend the token. The sentence is tied to the character the regulation’s own example uses.

### 2. The cookie-syncing example narrows itself to GPC

Proposed section 7025(c)(7)(F) begins with an opt-out preference signal: “When Business SS receives an OOPS, it must not allow these third parties to initiate or perform cookie-syncing.” The last sentence of the same example says Business SS must prevent that syncing “whenever it receives a GPC signal.” The statement of reasons, page 4, says the duty applies “whenever an OOPS is present.”

A signal that meets subsection (b) and is not GPC would fail the last sentence and pass the first. Replace the last sentence so that it uses “opt-out preference signal,” as the first sentence of the example does. Do not confine the example to one named signal when subsection (b) is written for any signal that meets the subsection.

### 3. A browser feature that makes its own request

Proposed section 7025(h):

> If a browser, as defined by Civil Code section 1798.136(e)(1), has a feature, tool, or function that interacts with a business on the consumer’s behalf and that feature makes the consumer’s personal information available to the business, that feature must not prevent, interfere with, contradict, or disable the consumer’s opt-out preference signal or other setting indicating the consumer’s choice to opt-out of the sale or sharing of their personal information from being sent to the business.

The statement of reasons, page 5, describes a different duty: a browser feature that discloses personal information must also forward the consumer’s signal. A feature can leave ordinary navigations untouched and still omit the signal on a request the feature itself makes. The operative sentence does not reach that request.

Replace subsection (h) with:

> If a browser, as defined in Civil Code section 1798.136(e)(1), has a feature, tool, or function that makes a request to a business on the consumer’s behalf and that request makes the consumer’s personal information available to the business, the request must carry the same opt-out preference signal, if any, that the browser would send on a consumer-initiated navigation to that business. The feature must not send a contradictory value.

Add Civil Code section 1798.136 to the reference note for section 7025. Subsection (h) uses the definition in section 1798.136(e)(1), and section 1798.136(c) authorizes regulations to implement that section. Section 1798.136 is operative January 1, 2027. Make subsection (h) operative on or after that date.

The sentence is limited to a browser as section 1798.136(e)(1) defines it: “an interactive software application that is used by consumers to locate, access, and navigate internet websites.” That definition was read from the official display on 2026-11-20. The proposed sentence does not cover a companion chatbot or another assistant that is not a browser. Senate Bill 243 and the vetoed Senate Bill 903 are different statutes.

### 4. Section 7026(g) cites a paragraph that is not there

The regulations effective January 1, 2026, and the extracted October 8 text, say a business may display “Opt-Out Request Honored” “in accordance with section 7025, subsection (b)(6).” Section 7025(b) has paragraphs (1) and (2). Section 7025(c)(6) is the display requirement, and it uses the same example. The statement of reasons describes typographical corrections in sections 7122, 7221, and 7222. It does not describe a correction of section 7026(g).

If the colored text still cites subsection (b)(6), change that citation to subsection (c)(6). If the colored text already cites subsection (c)(6), delete this paragraph before sending. The same citation is the subject of the held petition in `execution/sprint3/california/privacy-consumer/petition-7026-hold.md`. If a notice is published, this comment is the vehicle and that petition is not sent.

## What this comment is after a notice exists

A timely comment is placed in the rulemaking file. The Agency must answer it in the final statement of reasons. That answer is formal consideration. It is an acceptance only if the adopted text contains the requirement. Adoption follows a Board action and Office of Administrative Law review. The draft notice’s 45 days, any 15-day revision, and that review are the sequence. A notice published in December 2026 can put a comment in the file by February 15, 2027. A filed regulation by that date is not established.

**Admissions sentence, only if the adopted receiver rule matches item 1.** “The California Privacy Protection Agency adopted a rule that a business receiving the `Sec-GPC` header must treat a combined field value containing `1` as the consumer’s opt-out, and must not drop the opt-out because the combined value is not exactly the single character `1`.”

Do not use that sentence for a comment that has only been filed. Do not say a browser’s result on a draft W3C test violated California law.

## Personal information, when a notice exists

The draft notice says written comments and contact information are posted at https://cppa.ca.gov/regulations/oops.html. Use a name. Use an email only if it may be public. Do not add a telephone number.
