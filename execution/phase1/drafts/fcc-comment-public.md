Before the Federal Communications Commission
Washington, D.C. 20554

In the Matter of

Rules and Regulations Implementing the
Telephone Consumer Protection Act of 1991

CG Docket No. 02-278

Comments on the Further Notice of Proposed Rulemaking
FCC 26-67

Filed by: [Full legal name]
Mailing address: [U.S. Postal Service mailing address]
Date: [Filing date]

These comments address the Further Notice of Proposed Rulemaking in FCC 26-67, published at 91 FR 67239 (October 26, 2026), FR Doc. 2026-21820, in CG Docket No. 02-278. They do not ask the Commission to reconsider the Report and Order in the same item, 91 FR 67214, FR Doc. 2026-21821, and they do not address the amendment to 47 CFR 64.1200(a)(9)(iii)(A).

The Further Notice asks whether to shorten the time to honor a revocation, whether that time should differ for callers that designate an exclusive means, whether a category-limited informational revocation should depend on an all-categories method, what to make of silence after a clarification, whether one-way texting should remain, and how an affiliate boundary can be specified. These comments keep the ten-business-day maximum. They define the operations that maximum measures. They do not propose seven business days, a ban on one-way informational texting, or the affiliate paragraph quoted in footnote 84 of FCC 26-67.

## I. Timeframe for honoring a revocation request

Paragraphs 30 and 31 ask whether to reduce the maximum time for honoring a revocation. The Joint Letter suggests seven business days unless the caller shows that a longer time is reasonable. The paragraphs also ask whether exclusive-means callers should have a different maximum, whether two maxima would confuse consumers, and what the costs and benefits would be, including for smaller entities.

Revised paragraph (a)(10), in Appendix A of FCC 26-67 and in the Federal Register final rule, requires a request made in the manner described there to be honored within a reasonable time not to exceed ten business days from receipt. Revised paragraph (a)(11) states the same maximum for callers that designate no exclusive means. The revised paragraph (a)(10) does not contain the sentence, still displayed in the unofficial eCFR text of 47 CFR 64.1200 on November 18, 2026, that consent revoked by a listed method "is considered definitively revoked and the caller may not send additional robocalls and robotexts." Paragraph 3 of FCC 26-67 quotes that sentence as part of the 2024 order. From November 25, 2026, the timing language in the revised paragraphs is the duty to honor the request within ten business days.

That duty names an outcome. It does not identify the caller's internal operations. A component can label an utterance. A record can store the called number, the caller, and the scope. A communication the caller still controls can be cancelled. A later origination can read the record at send time, or it can reuse a clearance stored before the revocation. A label and an acknowledgement can both be complete while origination still uses the earlier clearance. Paragraph (b)(3) already requires an automatic do-not-call entry and immediate termination for a specified call. Paragraph (d)(3) already requires a covered residential request to be recorded at the time it is made, and it still allows ten business days to honor that request. Revised paragraphs (a)(10) and (a)(11) contain neither a contemporaneous permission record nor a rule for communications that remain in the caller's control.

A maximum of seven business days, or a shorter maximum only for exclusive-means callers, would leave that split in place. Matching a keyword produces a label. It does not write the permission record, cancel a queued communication, or check the record at origination. Section 64.1200 already uses "immediately" for the financial-institution and healthcare opt-outs, six business days for package-delivery opt-outs, and ten business days in paragraphs (a)(10) and (d)(3). A further split between exclusive-means callers and other callers would be a distinction the call itself does not disclose. This record contains no cost study and supplies no basis for finding that seven business days is reasonable or unreasonable for any class of caller. The existing maximum should remain, and the rule should state which events it measures.

The Commission should amend paragraphs (a)(10) and (a)(11) to provide that a caller honors a revocation request when all three of the following have occurred. At the time of receipt, the caller records a permission state identifying the called number on which the request was received, the caller or sender, and the scope. The record may note the arrival channel. That note limits the scope only when the request states a channel limit. The caller cancels each automated communication that the recorded scope covers and that remains within the caller's control. After the record is written, the caller originates no automated communication within the recorded scope other than a confirmation that paragraph (a)(12) permits, and a later origination decision reads the permission state at send time.

An automated label, and a spoken or written acknowledgement, do not honor the request. Under this definition, the ten-business-day maximum limits work that remains after the record is written and that is outside the caller's control, including a message already handed to a provider. The maximum does not depend on whether the caller designated an exclusive means. A designated exclusive means honors a request only when it performs the three operations. These comments do not ask the Commission to require processing of a request that arrives by some other method.

The attached appendix is a specification fixture, not a study of platforms or of consumers. It runs four separate functions on strings fixed in the script: a label, a permission write, cancellation of a queued message, and a later send decision. In that fixture, "stop" can be labeled as a standardized word while a later message is still sent, because the label does not write the store. A message flagged as still in the caller's control can be cancelled while a message flagged as already handed off stays pending. A clearance flag set before the write can allow a send that a send-time read suppresses. The empty string leaves the store unchanged. The fixture did not call a model, a network service, or a paid API, and it did not observe a carrier, a provider, a dialer, a handset, or a person. A passing check means the local objects matched that case.

## II. Category-limited revocation, silence, and the called number

Paragraphs 35 and 36 ask whether a category-limited reading should be available only when the caller provides a method to revoke consent for every message type that requires consent; whether that method must be automated; whether a revocation stops at the telephone number rather than every number on an account; and whether silence after a clarification should revoke every future robocall. Paragraph 39 asks about a confirmation call or text and about using a confirmation to clarify the category.

The standardized words in paragraph (a)(10)(ii) identify a revocation. They do not name a category, an account, or an affiliate. Revised paragraph (a)(10) lets the caller read an informational revocation as covering the category of the prompting communication. That category is the caller's label. Where the stored categories are finer than the choice disclosed to the consumer, "stop" writes the caller's taxonomy. Footnote 77 describes the Joint Letter's suggestion of an all-categories option "including a separate call or message." A later communication is unavailable when the consumer does not answer it. Paragraph 36 asks whether treating that silence as a revocation of every future robocall reflects the customer's intent. No reply is the same observable event for a non-delivery, an unread message, and a decision to stand on the revocation already made. It has no content from which a new scope can be read.

Revised paragraph (a)(12) permits a confirmation text that confirms the request and contains no marketing or promotional information, with a five-minute presumption. The pre-amendment paragraph, as displayed on eCFR on November 18, 2026, also made that confirmation the only additional message and required the sender to stop every consent-based text until the recipient clarified the scope. The revised paragraph does not contain those two requirements. A clarification question would start a wait. Silence during that wait should not be stored as a new revocation or as consent to resume.

The Commission should provide that a caller may record an informational revocation as limited to the category of that communication only when the communication discloses the limit clearly and conspicuously and the same interaction provides an automated method that records, for that called number and that caller, a revocation of every communication for which consent is required. If either condition is absent, the caller records the revocation as covering every such communication from that caller to that called number. An utterance that states a narrower scope is recorded with the scope it states. Failure to respond to a later communication does not revoke consent and does not restore it. A confirmation permitted by paragraph (a)(12) states the scope already recorded. It does not postpone the record and does not continue a revoked scope. These comments do not request a confirmation call. If the Commission permits one, it is a single call, it states the recorded scope, and it contains no advertising or telemarketing.

The permission state names the called number on which the request was received. A record for any other number on an account is a separate record. These comments do not answer whether 47 U.S.C. § 227 requires or forbids that second write. Paragraph 35 asks the question, and this record does not resolve it.

Paragraph 39 also notes proposals to shorten the standardized word list and to delete the rebuttable presumption in paragraph (a)(11). This record does not measure either change, and these comments do not recommend either one. If the Commission adopts either change, every method the caller remains required to accept honors the request by the three operations in section I.

## III. Reply paths and affiliate identity

Paragraphs 32 through 34 ask whether to remove the one-way texting provision, how widely one-way protocols are used, and whether one-way texting should remain for informational messages and for public institutions such as schools while two-way texting is required for advertising and telemarketing. Paragraphs 37 and 38 ask whether to modify, specify, or extend paragraph (d)(5).

The one-way provision already requires disclosure that two-way texting is unavailable and a reasonable alternative. A required reply string would be another intake path. Either path honors a revocation when it performs the three operations in section I. A reply path, a webpage, a telephone number, or an acknowledgement does not itself honor the request. This record contains no count of one-way protocols and no measurement of the cost of removing them. These comments do not recommend eliminating one-way protocols. A one-way protocol may be used for an informational communication, including a communication sent by or on behalf of a school or another public institution, when each message discloses an alternative that performs the three operations.

Paragraph (d)(5) states a reasonable-expectation standard for the residential do-not-call requests it governs. An origination path checks a stored key. It does not observe an expectation. These comments do not recommend modifying paragraph (d)(5), extending it to every robocall, or adopting proposed paragraph (a)(13). If the Commission specifies affiliate coverage for a consent revocation, the specification should name the stored fields the origination path checks: the caller identity disclosed when consent was obtained, the caller identity disclosed in the communication being revoked, and any affiliate, line of business, or division that disclosure names as covered. A name substituted at later origination is not one of those fields. Paragraph (d)(5) continues to govern the requests it already governs.

## IV. Response to the Initial Regulatory Flexibility Analysis

Paragraph 43 of FCC 26-67 requires comments on the Initial Regulatory Flexibility Analysis to carry a separate heading designating them as responses to that analysis. This section is that response.

These comments contain no cost study. They do not find that seven business days is a reasonable or an unreasonable maximum for a small entity, and they do not estimate a burden for concerns with fewer than 25 employees. Paragraph 41's paperwork question therefore has no numerical answer here.

The section I definition adds no second consumer-facing clock, does not prohibit one-way informational texting, and does not extend paragraph (d)(5). A caller that originates covered communications would record the revocation at receipt, cancel covered communications still in its control, and read that record at later origination. Paragraph (d)(3) already requires a contemporaneous record for a narrower class of residential requests. These comments do not claim the recommended record is costless. A shorter maximum limited to exclusive-means callers, which the analysis identifies as an alternative, would not require the record, the cancellation, or the send-time read. These comments recommend keeping the existing maximum because the record contains no cost measurement and because that alternative would not perform the three operations. Section III leaves one-way informational texting in place when the disclosed alternative performs those operations. Section II places an all-categories method in the same interaction as the revocation, so the caller does not send a second communication and does not treat silence as a new choice.

Respectfully submitted,

[Full legal name]
[U.S. Postal Service mailing address]
[Filing date]
