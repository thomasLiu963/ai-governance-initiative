# FCC audit: consumer control of automated communications

**Status of this file.** Local research memo, written 2026-11-18. It is not an FCC comment, not an ex parte presentation, and not a proposed rule. Nothing in this file was filed, and no one at the Commission was contacted.

**Document under review.** *Rules and Regulations Implementing the Telephone Consumer Protection Act of 1991*, CG Docket No. 02-278, FCC 26-67, Report and Order and Further Notice of Proposed Rulemaking, adopted September 30, 2026, released October 1, 2026. Full text: <https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf>.

The item was published as two Federal Register documents on October 26, 2026:

| Piece | Federal Register | Action | Date that matters |
| --- | --- | --- | --- |
| Report and Order | [91 FR 67214](https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21821.htm), FR Doc. 2026-21821, FR ID 373556 | Final rule. Title in the Register: *Enhancing the Ability of Consumers To Control the Robocalls* | Effective November 25, 2026 |
| Further Notice | [91 FR 67239](https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21820.htm), FR Doc. 2026-21820, FRS 373557 | Proposed rule. Title in the Register: *Modernizing the Ability of Consumers To Control Robocalls* | Comments due November 25, 2026. Reply comments due December 28, 2026 |

The PDF leaves the comment dates as “30 days” and “60 days” after publication. The Federal Register supplies the calendar dates above. Both documents are FCC 26-67. Comments have to say they address the Further Notice, because the same item number is also a final rule.

**Themes.** Human agency, authorization, human oversight, privacy, and transparency. The local fixture also serves AI reliability, because it states a bound on what a simulation can show.

## 1. Docket, deadlines, and the decision already made

The docket is CG Docket No. 02-278, the Commission’s long-running Telephone Consumer Protection Act (TCPA) implementation docket. FCC 26-67 does two things at once.

The Report and Order amends 47 CFR 64.1200(a)(9)(iii)(A), (a)(10), (a)(11), and (a)(12). On and after November 25, 2026, a caller may:

- treat a revocation made in response to an informational call or text as limited to that category of informational communication;
- treat a revocation made in response to an advertisement or a telemarketing communication as covering later advertising and telemarketing from that caller;
- designate, as the exclusive way to revoke consent, one or more of three methods already listed in the rule: an in-call automated voice or keypress opt-out, a reply text using any of seven standardized words, or a website or telephone number the caller designates for opt-outs;
- decline to process a revocation that arrives by any other method, if one of those exclusive methods was designated and disclosed on the call or in the text.

The Further Notice then asks whether to change that framework again. The questions are in section 3. The comment deadline, November 25, 2026, is the same day the Report and Order becomes effective. It is also before this project’s internal-review date of November 30, 2026. A comment could not wait for that review and still meet the comment date. Reply comments are due December 28, 2026. This audit does not request approval to file either one.

## 2. Requirements already on the books

Two texts have to be kept apart. The Electronic Code of Federal Regulations page for [47 CFR 64.1200](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200), read on November 18, 2026, still displayed the pre-amendment section and pointed to an amendment published at 91 FR 67219. eCFR is a continuously updated unofficial edition. The amendment text below is taken from Appendix A of FCC 26-67, which matches the rule text in the Federal Register final rule.

### 2.1 Codified text read on November 18, 2026

Paragraph (a)(10) says a called party may revoke prior express consent, including prior express written consent, for calls or texts covered by paragraphs (a)(1) through (3) and (c)(2), “by using any reasonable method to clearly express a desire not to receive further calls or text messages.” These methods are reasonable per se:

- an automated, interactive voice or keypress opt-out on a call;
- a reply text using “stop,” “quit,” “end,” “revoke,” “opt out,” “cancel,” or “unsubscribe”;
- a website or telephone number the caller has designated for opt-out requests.

A reply that uses other words must be honored “if a reasonable person would understand those words to have conveyed a request to revoke consent.” A one-way texting protocol is permitted only if each text discloses that two-way texting is unavailable because of the protocol and gives a reasonable alternative, such as a telephone number or website. Every reasonable revocation “must be honored within a reasonable time not to exceed ten business days from receipt.” The same paragraph says callers “may not designate an exclusive means to request revocation of consent.” It also says that consent revoked by a per se method “is considered definitively revoked and the caller may not send additional robocalls and robotexts.”

Paragraph (a)(11) makes other methods, such as a voicemail or an email aimed at the caller, a rebuttable presumption of revocation. The caller may rebut that presumption under a totality-of-circumstances test.

Paragraph (a)(12) allows one confirmation text. It must only confirm the revocation, it must not contain marketing or promotion, and it must be the only additional message after the request. A text sent within five minutes is presumed to fall within prior express consent. The sender must justify a longer delay. If the recipient had consented to several categories, the confirmation may ask whether the revocation covers all of them, and the sender “must cease all further texts for which consent is required absent further clarification that the recipient wishes to continue to receive certain text messages.”

FCC 26-67, paragraph 4, states that the Consumer and Governmental Affairs Bureau delayed the effective date of the “revoke all” portion of (a)(10) until January 31, 2027, citing *Rules and Regulations Implementing the Telephone Consumer Protection Act of 1991*, Order, 40 FCC Rcd 2395 (CGB 2025), and Order, DA 26-12 (CGB Jan. 6, 2026). Those two waiver orders were not opened for this audit. The eCFR page read on November 18 still displayed the revoke-all sentence. The display alone does not settle whether that sentence is enforceable today. Paragraph 24 of FCC 26-67 says the November 25 amendment supersedes that delayed effective date.

The ten-business-day outer bound and several stricter clocks are already distributed through the section:

| Provision, as displayed November 18, 2026 | What it already requires |
| --- | --- |
| 64.1200(a)(10) | Honor a consent revocation within a reasonable time, maximum ten business days from receipt |
| 64.1200(d)(3) | For a residential do-not-call request covered by paragraph (d), record the request and place the number on the do-not-call list “at the time the request is made,” and honor it within ten business days. Paragraph (d) covers specified exempted artificial or prerecorded calls and telemarketing calls to a residential subscriber |
| 64.1200(b)(3) | On specified prerecorded calls, the in-call opt-out “must automatically record the called person's number to the caller's do-not-call list and immediately terminate the call” |
| 64.1200(a)(9)(i)(F) | Package-delivery opt-out: reasonable time, maximum six business days |
| 64.1200(a)(9)(ii)(F), (a)(9)(iii)(H), (a)(9)(iv)(H) | Inmate-notification, financial-institution, and healthcare exemption opt-outs: honor “immediately” |
| 64.1200(d)(5) | A residential do-not-call request applies to the entity making the call, or on whose behalf it is made, and to an affiliate only when “the consumer reasonably would expect them to be included given the identification of the caller and (for telemarketing calls) the product being advertised,” unless the subscriber asks for a different scope |

Paragraph (d)(5) is the affiliate rule the Further Notice quotes. By its terms it governs the do-not-call requests in paragraph (d). It does not, by its terms, govern every consent revocation under (a)(10). The Report and Order, in the discussion of telemarketing revocations, reminds telemarketers of (d)(5). It does not move (d)(5) into (a)(10).

The statute uses the called party as the person whose consent matters. 47 U.S.C. § 227(b)(1)(A) and (B), in the 2023 United States Code edition on GovInfo, prohibit the covered calls “other than a call made for emergency purposes or made with the prior express consent of the called party,” and residential prerecorded calls “without the prior express consent of the called party,” subject to the exemptions stated in the statute. FCC 26-67, note 80, points to that provision and to the 2024 order’s statement that, once the called party revokes, the caller no longer has consent to make further covered robocalls or robotexts to that called party absent instructions to the contrary. *Rules and Regulations Implementing the Telephone Consumer Protection Act of 1991*, Report and Order and Further Notice of Proposed Rulemaking, 39 FCC Rcd 1988, 1998, para. 32 (2024).

### 2.2 Text adopted September 30, 2026, effective November 25, 2026

Appendix A replaces (a)(10), (a)(11), and (a)(12). The operational changes are:

- Exclusive means is permitted. A caller that designates and discloses one of the three methods “is not required to process revocation requests made by any other means.”
- A text sender that designates reply text as the exclusive means may disclose a single standardized word, such as “stop,” and must still honor any of the seven words.
- Informational revocations may be category-limited. Advertising and telemarketing revocations still cover later advertising and telemarketing from that caller.
- The one-way texting exception remains, with the same disclosure-plus-alternative conditions.
- The ten-business-day outer bound remains, for requests “made in the manner described.”
- Callers that do not designate an exclusive means must still process any reasonable means. The rebuttable presumption in (a)(11) remains for them, and the ten-day bound is restated there.
- The new (a)(12) still permits a confirmation text with no marketing, and it keeps the five-minute presumption. It drops the words “one-time,” drops the clause that the confirmation is the only additional message, and drops the sentence that required the sender to stop every consent-based category until the recipient clarified the scope.

The amendment also revises (a)(9)(iii)(A), the financial-institution fraud-alert exemption, so a wireless number may come from the customer or from a “reliable source” as defined there. The Further Notice does not ask about that revision. This audit does not propose changing it. Paragraphs (a)(9)(iii)(H) and (b)(3) are not in the amendatory instruction.

### 2.3 What the 2024 order is

The “TCPA Consent Order” cited throughout FCC 26-67 is the February 16, 2024 item, 39 FCC Rcd 1988. The Commission’s October 11, 2024 Federal Register notice, [89 FR 82518](https://www.federalregister.gov/documents/full_text/html/2024/10/11/2024-23605.html), set April 11, 2025 as the effective date of the amendments adopted there, including (a)(10) and (a)(11). The March 5, 2024 publication of those amendments is [89 FR 15756](https://www.govinfo.gov/content/pkg/FR-2024-03-05/html/2024-04587.htm). The 2024 order is where the ten-day bound, the seven-word list, the one-time confirmation, and the “any reasonable method” sentence were adopted. FCC 26-67 is the reconsideration of the scope and exclusive-means parts of that framework, plus a new set of questions.

## 3. Questions the Further Notice actually asks

Paragraph numbers are from FCC 26-67. The Federal Register synopsis tracks them, with different lettering.

**Joint letter (para. 29).** On June 30, 2026, the American Bankers Association, the National Consumer Law Center, and ACA International filed a letter in this docket. The cover letter, read on the [ABA’s page](https://www.aba.com/advocacy/policy-analysis/letter-on-revocation-of-consent-under-tcpa), says the attachment would let a caller treat a revocation as category-specific, require notice of that reading and a means to revoke all consent-based messages, and let the caller designate an exclusive reasonable method. The attachment PDF linked from ACA International returned an error and was not read. Where this memo describes the attachment, it uses only quotations and descriptions in FCC 26-67.

**Timeframe (paras. 30–31).** Should the outer bound be reduced? The joint letter suggests seven business days unless the caller shows that a longer time is reasonable. Should callers that designate an exclusive means have a different bound from callers that do not? Would two bounds confuse consumers? What are the costs and benefits, including for smaller entities?

**Two-way texting (paras. 32–34).** Should the one-way exception be removed? How widely are one-way protocols used, and for informational messages, advertising, or both? Should one-way remain available for informational messages, and for public institutions such as schools, while two-way is required for advertising and telemarketing? The joint letter proposes deleting the one-way exception.

**Revoke-all method (paras. 35–36).** The Order allows category-limited informational revocation and does not require a method that stops every consent-based communication. The Further Notice asks whether that limited reading should be available only if the caller provides “a method to revoke consent for all types of messages for which consent is required.” It asks whether that method must be automated and what form it should take. It asks whether a one-step stop-all option is worth the burden, including for small entities. It asks about the Edison Electric Institute request, described in the item, to confine a revocation to the telephone number rather than every number on an account, and whether that reading fits the statute’s “called party.” It asks whether the telemarketing rule, which already revokes all similar telemarketing, is enough. It asks whether treating silence after a clarification message as a revocation of every future robocall is too broad to reflect the customer’s intent. Note 77 quotes the joint letter as suggesting that the caller tell the recipient of an option, “including a separate call or message,” to revoke all consent-based calls and texts. Note 13 records NCLC’s earlier view, as described by the Commission, that a category-limited reading should be paired with a clear disclosure and an automated all-categories method. REACH’s reply comments, which were not opened, are described as opposing any mandatory revoke-all method.

**Affiliates (paras. 37–38).** Should (d)(5) be modified, specified, or extended beyond exempted and telemarketing calls? The joint letter’s proposed new (a)(13) is quoted in note 84: an affiliate, line of business, or division that obtains separate consent and “holds itself out to the called party throughout all calls and texts” as that affiliate, rather than as the parent, “will be deemed a separate caller or text sender.”

**Other (para. 39).** The joint letter also proposes to shorten the standardized word list, to delete the (a)(11) rebuttable presumption, and to allow a confirmation call or text. EEI, in an ex parte that was not opened, is described as asking the Commission to recognize additional standardized keywords and customer-preference tools. Vibes, in an ex parte that was not opened, asks that a confirmation text be allowed to request clarification of the category. The Commission also declined, in the Order, Vibes’s request to delay the effective date by as much as twelve months.

The Initial Regulatory Flexibility Analysis asks, in addition, how any of these choices would affect small entities, and it offers design alternatives the Commission is already considering: a shorter clock only for callers that designate a method, two-way texting only for telemarketing, and a revoke-all duty only if the burden can be limited.

## 4. Technical problems in automated voice, SMS, and AI-mediated systems

The rules above tell a caller to recognize a revocation and then to honor it within a stated outer bound. An automated voice, text, or conversational system can do the first of those in a module that never performs the second. The problems below are mismatches between those modules and the rules as written. They are not findings that any named caller is out of compliance.

### 4.1 Four operations are separately observable

A reviewer can watch four different events:

1. **Recognition.** A component labels an utterance. The label may be “standardized word,” “ordinary language,” “silence,” or “not a revocation.”
2. **Permission state.** A record is written. The useful key is the called number, the caller identity, the channel, and the scope. An acknowledgement in the conversation is a message, not this record.
3. **Queued-action cancellation.** A communication already created, and still inside the caller’s system, is marked so that it will not be originated. A communication already handed to a provider, aggregator, or carrier is outside that local mark.
4. **Later origination.** A send function runs after the request. It either reads the current permission record and suppresses the communication, or it uses an earlier clearance and sends.

Paragraph (b)(3) already ties two of these together for one class of calls: the in-call mechanism must record the number on the do-not-call list and terminate that call. Paragraph (d)(3) already separates recording, which it places “at the time the request is made,” from honoring, which may take up to ten business days. Paragraphs (a)(10) and (a)(11), including the November 25 text, require the request to be “honored” within the outer bound and do not define honoring as the write, the cancellation, and the later check. A system can satisfy a keyword detector and a polite reply while the dialer or the text platform still has the old permission.

That split is especially sharp in an AI-mediated system. The conversational component can be instructed to say that the request was accepted. OWASP’s agent guidance, discussed in section 6, already treats a confirmation flag inside the model’s context as insufficient for authorization. The FCC rule does not say the same thing about a revocation acknowledgement. The November 25 exclusive-means rule widens the split: a caller may lawfully ignore a revocation that is not in the designated channel. The voice agent can still hear it, label it, and answer it.

### 4.2 “Stop” does not carry its own scope

The seven standardized words identify a revocation. They do not identify a category, an account, or an affiliate. Scope has to be added by a rule.

The November 25 text lets the caller supply that rule for informational communications: the revocation may be read as covering only the category of the message that prompted it. The prompting message is something the caller labeled. If the stored categories are finer than the choice the consumer could see, the same word “stop” writes a narrower record than the consumer had a way to name. The Further Notice asks whether this reading should be conditioned on an all-categories method. The adopted (a)(12) no longer requires the sender to stop every consent-based category while a clarification is outstanding. A caller can therefore keep sending the categories it did not infer, without a recorded choice by the called party.

Silence makes the inference worse. The Further Notice asks about a proposal, attributed to the joint letter and questioned by EEI, under which a failure to answer a clarification becomes a revocation of every future robocall. A non-delivery, an unread message, and a decision to stand on the revocation already made are the same observable event: no reply. A permission record that treats that event as intent is implementing a default, not reading a request.

### 4.3 The called number, the account, and the affiliate are different keys

EEI’s request, as described by the Commission, is that a revocation cover the telephone number and not every number on the account. The statute’s term is “called party,” not “account” and not “telephone number.” This audit does not resolve that legal question. The implementation consequence is narrower. An account-level boolean has two outputs, block everything or block nothing. It cannot store “this number only,” and it cannot store “each number the person answered.” Those are separate writes.

Affiliate scope has the same shape. Paragraph (d)(5) states a legal standard, reasonable expectation from the caller’s identification and, for telemarketing, the product. A sending system does not compute an expectation at dial time unless someone has already stored the result. The joint letter’s proposed (a)(13) would use a different test: separate consent, plus holding the division out as the division throughout the communications. A platform can print a division’s name in the text and originate the message from a parent campaign file. The name in the text and the key in the permission store are the same fact only if the store is required to use the disclosed name.

### 4.4 A reply path is an intake channel

The one-way exception already requires a disclosed alternative. Two-way texting, if the Commission requires it, adds a reply string. Neither condition says that the reply, or the alternative, writes the permission record and that later origination reads it. A classifier attached to the reply can label “stop” and leave the campaign queue alone. A website linked from a one-way school or bank text can display instructions and never update the originating platform. Requiring two-way protocols for advertising, and leaving one-way in place for schools, answers a burden question the Further Notice asks. It does not, by itself, connect either path to the permission state.

### 4.5 The outer bound measures different work in different systems

Ten business days, a possible seven, six business days for package delivery, and “immediately” for several exemptions are already different clocks. They do not say which event stops the clock. In a system that writes the permission record when the reply arrives, the remaining time is propagation to vendors and retrieval of anything already in a carrier queue. In a system that batches keyword review by hand, the same clock is the time to notice the request. Shortening the maximum from ten business days to seven does not choose between those architectures. Giving the shorter maximum only to callers that designate an exclusive automated means rewards the existence of an intake channel. It does not require that channel to cancel controlled queue items or to re-check permission at send time.

A clearance computed when a message is scheduled, and reused when it is sent, is the same stale-authorization pattern OWASP already describes for agents (section 6). The communications version is a campaign job authorized on Monday and released on Thursday, after a revocation on Tuesday, because the job stored “cleared” rather than reading the record again.

### 4.6 What this audit does not claim

No count of one-way texting was found in the materials read. No cost of a seven-day bound was measured. No automatic speech recognizer or language model was run. The problems above are structural. They are the reason the recommendations define events inside the caller’s system, and the reason they do not offer a new number of business days as the remedy.

## 5. Recommendations

Each recommendation answers a question the Further Notice asks. Each one uses machinery the rules already contain in some narrower place: recording at the time of the request in (d)(3), an automatic write and immediate termination in (b)(3), an immediate honor duty in the financial and healthcare exemptions, a category distinction the Order has just adopted, and the called-party term in the statute. The candidate sentences are proposed comment text. They are not current law, and they are not filed.

### Recommendation 1. Define “honor,” and do not add a second consumer-facing clock

**Questions.** Paragraphs 30 and 31, on the outer bound and on whether exclusive-means callers should have a different bound. Paragraph 39, on what remains of a revocation if the standardized list shrinks or the rebuttable presumption is removed.

**Why this is the gap.** The Commission, in the 2024 order, reserved the right to shorten the ten-day bound as processing became faster. FCC 26-67, paragraph 31, ties that possibility to exclusive automated means. The speed of a keyword matcher is not the speed of honoring. Paragraphs (b)(3) and (d)(3) already force an immediate record for some calls. Paragraphs (a)(10) and (a)(11) do not. A seven-day maximum, or a shorter maximum only for exclusive-means callers, leaves recognition, acknowledgement, and origination as one undifferentiated duty. Consumers also cannot see which clock applies to a given call. The Further Notice asks whether varying the bound would confuse them. The section already varies it: immediate, six business days, and ten business days, depending on the exemption. A further split between exclusive-means callers and everyone else adds a distinction that is not printed on the call.

This record contains no cost study. It does not support a finding that seven business days is reasonable, or that it is unreasonable, for a small caller. The candidate text therefore keeps the existing maximum and defines the events inside it. If the Commission later has evidence for a shorter maximum, the same definition tells it what the shorter maximum is measuring.

**Candidate text.**

> Honoring a revocation request means all of the following. (i) At the time of receipt, the caller records a permission state that names the called number on which the request was received, the caller or sender, the channel, and the scope of the revocation. (ii) The caller cancels each automated communication that the recorded scope covers and that remains within the caller’s control. (iii) After that record is written, the caller originates no automated communication within the recorded scope other than a confirmation that paragraph (a)(12) permits. An automated label, and a spoken or written acknowledgement, do not honor the request unless (i), (ii), and (iii) have occurred. The reasonable time in paragraphs (a)(10) and (a)(11), not to exceed ten business days from receipt, limits the work that remains after the permission state is recorded and that is outside the caller’s control. That maximum does not differ according to whether the caller has designated an exclusive means. A designated exclusive means meets this section only when it performs (i), (ii), and (iii). If the Commission removes the rebuttable presumption in paragraph (a)(11), or shortens the list of standardized words, every method the caller is still required to accept honors the request only by performing (i), (ii), and (iii).

**What an implementer would change.** The origination path checks the permission record at send time. Queue items still in the caller’s control are cancellable by that record. Acknowledgements are logged as messages, separately from the record. The time of receipt, the time of the write, and the time of each cancellation are kept so the outer bound can be audited. A vendor handoff is marked, because the local cancel cannot reach it.

### Recommendation 2. Condition a category-limited reading on a recorded all-categories method, and store the called number

**Questions.** Paragraphs 35 and 36, including the revoke-all condition, automation, EEI’s telephone-number request, and non-response. Paragraph 39, on Vibes’s clarification text and on a confirmation call.

**Why this is the gap.** The Order has already chosen category-limited informational revocation. The Further Notice asks whether that choice should be available only together with an all-categories method. NCLC’s condition, as the Commission describes it in note 13, was disclosure plus an automated all-categories method. The joint letter, as quoted in note 77, would allow the all-categories option to be “a separate call or message.” A later message is another communication, and it fails when the first message was the consumer’s last reply. The standardized words still do not encode a category. If the caller may infer the narrowest category from the prompting template, the permission write is the caller’s taxonomy.

The current (a)(12), until November 25, tells the sender to cease consent-based texts until the recipient clarifies. The adopted (a)(12) deletes that sentence. Putting a clarification question back into the confirmation, which is Vibes’s request, recreates a waiting period. The Further Notice asks whether non-response during that wait should count as revocation of everything. Non-response has no content. It should not be stored as a new revocation, and it should not be stored as consent to resume.

On the account question, the candidate text stores the number that was used, because that is the number the system received. It does not say the TCPA forbids a second write for another number on the account. FCC 26-67 asks that legal question and this audit does not answer it. The text does say that an account-wide flag is a different record from a number record, so a caller cannot satisfy a number-specific request by flipping every number, or by flipping none.

**Candidate text.**

> A caller may record a revocation made in response to an informational communication as limited to the category of that communication only when the communication discloses that limit clearly and conspicuously and the same interaction provides an automated method that records, for that called number and that caller, a revocation of every communication for which consent is required. If either condition is missing, the caller records the revocation as covering every communication for which consent is required from that caller to that called number. An utterance that states a narrower scope is recorded with the scope it states. The called party’s failure to respond to a later communication does not revoke consent and does not restore it. A confirmation permitted by paragraph (a)(12) states the scope that was recorded and does not continue a scope that was revoked. A confirmation call, if the Commission permits one, is a single call, states the recorded scope, and contains no advertising or telemarketing. The permission state is recorded for the called number on which the request was received. A record for any other number associated with an account is a separate record.

**What an implementer would change.** Category labels used for sending have to be the labels disclosed with the revocation choice. The all-categories control writes the same store as any other revocation, in the interaction that received the request. Clarification is optional copy inside the one confirmation. It is not a timer that reopens the revoked scope. Account profiles may keep several numbers, and a revocation write names which of them it covers.

### Recommendation 3. Require the reply path, or the disclosed alternative, to perform the same write; key affiliates to the disclosure

**Questions.** Paragraphs 32 through 34, on two-way texting, informational messages, and schools. Paragraphs 37 and 38, on affiliates and on whether (d)(5) should be extended.

**Why this is the gap.** Deleting the one-way exception would force a reply channel. Keeping it for schools and other informational senders, which the Further Notice asks about specifically, leaves those senders on a disclosed alternative. In both designs the missing requirement is the same: the path the consumer is told to use has to be the path that writes the permission state in Recommendation 1. This audit has no measurement of how many schools, or how many other small senders, use one-way protocols. It does not recommend prohibiting those protocols.

For affiliates, (d)(5) already states the reasonable-expectation standard for the calls it covers. Extending that sentence to every robocall would extend a standard a dialer cannot evaluate from the words alone. The joint letter’s (a)(13) is already before the Commission and is not repeated here as if it were a new proposal. The additional requirement is mechanical. The caller identity disclosed when consent was obtained, and disclosed in the communication, is the key that origination checks. Affiliates covered by the revocation are the ones that disclosure lists. A later change of the name on the message does not move the record. Paragraph (d)(5) continues to govern the do-not-call requests it already governs, including the consumer’s reasonable expectation and a specific request to include or exclude an affiliate.

**Candidate text.**

> A reply text, and any alternative method disclosed because two-way texting is unavailable, honors a revocation only by performing the recording, cancellation, and suppression required for honoring a revocation. The existence of a reply path, a webpage, a telephone number, or an acknowledgement does not, by itself, honor the request. A one-way protocol may be used for an informational communication, including a communication sent by or on behalf of a public institution such as a school, when each such communication discloses an alternative that performs that recording, cancellation, and suppression.
>
> Except as paragraph (d)(5) already provides, a revocation is recorded against the caller identity disclosed when consent was obtained and disclosed in the communication to which the revocation responds. The record also covers an affiliate, line of business, or division named as covered in that disclosure. Changing the name used to originate a later communication does not remove a record and does not extend it to an identity the disclosure did not name. Paragraph (d)(5) continues to govern the do-not-call requests to which it applies.

**What an implementer would change.** The intake adapter, whether it is a reply keyword, a keypress, a webpage, or an agent tool, calls the same write function. School and other informational one-way texts name that function’s public method in each message. Consent and revocation records store the disclosed caller name and the disclosed affiliate list. The campaign sender looks up that key and cannot satisfy the lookup by substituting a brand name at send time.

### What these recommendations do not do

They do not assert that the TCPA already requires this machinery. They do not ask the Commission to undo category-limited informational revocation, exclusive means, or the financial-institution reliable-source change. They do not propose a seven-day bound, a ban on one-way school texting, or adoption of the joint letter’s (a)(13) under a different name. They do not treat OWASP guidance as a legal duty of callers.

## 6. OWASP authorization and human-control guidance

The same four-stage fixture can be reused as a test of outbound communications. It should not be rewritten as a new general authorization rule. The following documents were read on November 18, 2026. They are community guidance. None of them is a statute or an FCC rule.

| Document | Status | What it already requires | Locator |
| --- | --- | --- | --- |
| OWASP AI Exchange, general controls, `#OVERSIGHT` | Community guidance, unpinned web page | Oversight gates at the infrastructure layer, not as instructions to the model. A kill switch that halts execution regardless of task state and that the agent does not control. A genuine mid-task opt-out. Staged commit, so the actor that prepares a message is not the actor that releases it. Human-oversight tests for urgency, fatigue, and multi-step pressure | <https://owaspai.org/docs/1_general_controls/> and <https://owaspai.org/go/oversight> |
| OWASP AI Exchange, `#LEAST MODEL PRIVILEGE` | Same | Permission checks in the backend, not in the prompt. Deny-by-default grants that expire when the task is cancelled. Re-authorization when scope changes. The limitations paragraph tells designers to combine short token lifetime and revocation with “explicit revocation-latency tolerance” | <https://owaspai.org/go/leastmodelprivilege> |
| OWASP Top 10 for Agentic Applications, version 2026, December 2025 | Community guidance, CC BY-SA 4.0 | ASI02: a policy enforcement point in front of the tool, short-lived credentials, and revocation on drift. ASI03: time-of-check to time-of-use, where a workflow keeps using an authorization that changed before execution; per-action re-authorization; permissions bound to subject, resource, purpose, and duration | <https://genai.owasp.org/download/52117/> |
| OWASP AI Agent Security Cheat Sheet | Community guidance, Cheat Sheet Series page | “Enforce authorization in the execution component, outside the agent's context.” A `user_confirmed` flag is not enough. The check is bound to the actor and the exact call, and it is consumed immediately before execution. Users can interrupt and roll back | <https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html> |

A search of the AI Exchange PDF retrieved that day for “opt-out,” “revocation request,” “permission state,” and “queued” found training-data opt-outs, provider logging opt-outs, the mid-task opt-out and staged-commit language above, and “effective permission state” logging. It did not find a consumer-communications test that separates an utterance label, an acknowledgement, a called-number permission record, cancellation of a message still in the sender’s control, and a later origination.

Re-proposing a kill switch, a backend permission check, a ban on prompt-only authorization, or a per-action re-check would duplicate those documents. The AI Exchange charter says the project explains and aligns security guidance and does not itself set a standard: <https://owaspai.org/charter/>. Its contribution page requires a contributor who used material AI assistance to say that AI was used and to say for what: <https://owaspai.org/contribute/>.

The piece that is not already specified is the communications oracle: the four events in section 4.1, a scope key of called number, disclosed caller, category, and channel, and a rule that silence writes a record only when a policy says so. That oracle is a possible later example under `#OVERSIGHT` or under the AI Exchange testing material. It is not drafted as an OWASP edit in this audit. No OWASP issue or pull request was opened. The LLM Top 10 document itself was not read; the agentic Top 10, which was read, identifies Excessive Agency as LLM06:2025. The AI Exchange page still cites “OWASP for LLM 03: Excessive Agency.” That numbering difference was not reconciled against the LLM Top 10 source.

## 7. Local fixture

### 7.1 Design

`audits/fcc/sim_revocation.py` is a deterministic Python 3 script. It uses the standard library only. It does not call a model, a network service, or a paid API. The recognizer is an exact match on a fixed list of strings.

The script is a specification fixture. Each case builds the four stages as separate steps and asserts the split that case is there to show. A passing assertion means the local objects behaved as that case specifies. It does not mean a carrier, a vendor, a handset, or a production dialer was observed.

Stages in the script:

- `recognize` returns a label and writes nothing.
- `apply_scope` writes a store only when the case calls it. The store key is number, caller, and category, with `*` for every category.
- `cancel_controlled` cancels a pending message only when the store blocks it and `in_caller_control` is true.
- `decide_send` either rereads the store or trusts `cleared_at_schedule`. A message of kind `confirmation` is sent even when the store blocks the number. Any other blocked message is suppressed.

Synthetic strings, all chosen in advance:

| Input | Label the fixture assigns |
| --- | --- |
| `stop`, `unsubscribe`, and the other five standardized words | `standardized` |
| `stop all` | `revoke_all` |
| `stop the payment reminders but keep fraud alerts` | `keep_fraud` |
| `please don't call me anymore`, `stop bothering me` | `ordinary_language` |
| empty string | `silence` |
| `thanks` | `not_revocation` |

The fixture does not claim these labels match a reasonable-person test, a jury, or any model.

### 7.2 What was run

Command, from the workspace root, on November 18, 2026: `python3 audits/fcc/sim_revocation.py`. Result: 9 cases, 0 failed assertions. Observed end states:

| Case | What the objects did |
| --- | --- |
| `recognition_without_write` | `stop` was labeled `standardized`. The store did not block the number. The pending informational message was sent |
| `write_cancels_local_and_suppresses_later` | A write of scope `all` cancelled the pending message still in caller control. The handed-off message stayed `pending`. A later informational message was suppressed |
| `confirmation_once_then_suppress` | The confirmation was sent. A later informational message was suppressed. A later “anything else” message, represented as another informational send, was suppressed |
| `scope_follows_policy_not_the_word_stop` | With the narrow-default policy, `stop` suppressed payment and the fraud message was sent. With the same narrow-default policy, `stop all` suppressed the fraud message |
| `exclusive_means_label_does_not_write` | `please don't call me anymore` was labeled `ordinary_language`. The exclusive-means branch did not write. The queued message was sent |
| `silence_writes_only_if_a_policy_says_so` | An empty reply left the store open. A different policy that wrote `*` blocked a fraud message. Both policies are a few lines of code |
| `number_scope_is_not_account_scope` | A write for `+15550001` left `+15550002` sendable. Writing both numbers suppressed the second |
| `affiliate_follows_stored_caller_key` | A write for `Card Division` suppressed a Card Division message and left a Retail Bank message sendable. A store that also named Retail Bank suppressed that message |
| `send_time_reread_not_schedule_time_clearance` | After `unsubscribe` was written, a sender that trusted a pre-revocation clearance sent the message. A sender that reread the store suppressed it |

### 7.3 What this run can establish

- The four stages can be implemented as different operations. A label and an acknowledgement can be true while a later send still happens.
- A local queue flag cancels only the items the flag is defined to cover. In this script, a handed-off item stays pending.
- Scope is a property of the write. The word `stop` produced a payment-only block under one policy and was not the input that blocked fraud. The input `stop all` did.
- Silence writes a revocation only in the branch that contains that write.
- A number, a second number, a disclosed caller, and a listed affiliate are different keys, and the send decision follows the key that was written.
- A clearance cached before the write is a different input from a read at send time. This is the communications instance of the time-of-check pattern ASI03 already names.

### 7.4 What this run cannot establish

- That any real voice platform, messaging provider, or campaign tool behaves this way, or how often it does.
- Whether a consumer’s words were a revocation under the TCPA, or whether a method was reasonable.
- How an automatic speech recognizer or a language model labels speech, noise, or paraphrase. No model ran. Adding a model would test that model’s labels, and it would still not write the carrier’s queue.
- What happens after a provider has accepted a message. The `handed` object only shows that the local function does not change an object marked outside caller control.
- Whether seven or ten business days is enough time, or what either bound costs a small entity. The script has no clock and no cost.
- That the candidate sentences in section 5 are lawful, or that they are the least burdensome choice. The Initial Regulatory Flexibility Analysis asks for that evidence. This fixture is not that evidence.
- Consumer intent. The silence case shows two recordable defaults. It does not show which default a person meant.

A useful next run, still without a paid model, would be the same oracle against a caller’s own logs or a sandboxed test tenant: export the utterance, the permission row, the queue row, and the send decision, and join them on the called number and the message id. That run is not done. It needs a system this workspace does not have.

## 8. Filing process, if a comment is later approved

This section is a checklist. It is not an instruction that has been carried out.

1. Internal approval has to be recorded before any submission. The project rule is that external submission is a separate step. As of this writing, `MASTER_TRACKER.md` has no FCC candidate and no approval. This audit does not add one.
2. The comment date is November 25, 2026. That is before the project’s November 30 internal-review date. Reply comments are due December 28, 2026. A reply can respond only to matters raised in the comments. 47 CFR 1.415(d) says no further comments are filed unless the Commission requests or authorizes them.
3. File in CG Docket No. 02-278 through the Electronic Comment Filing System, <https://www.fcc.gov/ecfs>, under 47 CFR 1.415 and 1.419, as the Further Notice directs. The Commission’s rulemaking-process page says an ECFS filer includes a full name, a mailing address, and the docket number, and that comments are generally posted without change, including personal information: <https://www.fcc.gov/about-fcc/rulemaking-process>. A 2018 Commission letter describes 47 CFR 1.419(e) as requiring the filer’s name and mailing address, and an attorney’s name and address when a party is represented. The text of section 1.419 was not opened for this audit. Do not put unpublished project files into the filing.
4. Identify the comments as addressed to the Further Notice in FCC 26-67, FR Doc. 2026-21820, 91 FR 67239. The Report and Order in the same item is already adopted.
5. Comments on the Initial Regulatory Flexibility Analysis need a heading that identifies them as IRFA comments. FCC 26-67, paragraph 43.
6. The Further Notice is a permit-but-disclose proceeding under 47 CFR 1.1206. A written ex parte, or a memorandum of an oral ex parte, is due within two business days, in the docket, in a native format when feasible. This audit is not an ex parte filing. Sending it to Commission staff would be a presentation and would trigger that rule.
7. The contact named in the item is Richard D. Smith, Consumer and Governmental Affairs Bureau, Richard.Smith@fcc.gov, (717) 338-2797. He was not contacted.
8. No AI-assistance disclosure rule for comments appears in the Further Notice or in 47 CFR 1.415, which was read. If a comment is later filed, the filer should not invent such a duty. If the same research is later offered to the OWASP AI Exchange, the Exchange page requires a disclosure of material AI assistance. This memo was prepared with AI assistance in research and drafting, and a person still has to check every quotation against the cited source before any external use.

Paper filing addresses, if ever needed, are printed in the Federal Register item: hand and courier delivery to 9050 Junction Drive, Annapolis Junction, MD 20701, and U.S. Postal Service delivery to 45 L Street NE, Washington, DC 20554. Electronic filing is the path the Commission asks for first.

## 9. Contribution record

| Field | Value |
| --- | --- |
| Audit directory | `audits/fcc/` |
| Recommendations | Three, in section 5. Local labels only. They are not rows in `MASTER_TRACKER.md` |
| Status | Draft for internal reading. Not `ready`, not `submitted` |
| Exact source | FCC 26-67, released October 1, 2026; Federal Register publication October 26, 2026. URLs in the header and in section 10 |
| Document status | The Report and Order is an adopted final rule with a future effective date. The Further Notice is a proposed rule. 47 CFR 64.1200, as displayed on eCFR on November 18, 2026, is the codified text, unofficial on eCFR, with a published amendment not yet effective. OWASP documents in section 6 are community guidance. Section 5 is language this project proposes and has not filed |
| Policy check | FCC filing rules: 47 CFR 1.415 was read; the Further Notice’s filing and ex parte directions were read; 47 CFR 1.419 was not read in full. No AI-assistance rule for FCC comments was found in the documents that were read. OWASP AI Exchange contribution and AI-assistance rules were read at <https://owaspai.org/contribute/>. No submission is proposed |
| Themes | Human agency, authorization, human oversight, privacy, transparency, AI reliability |
| External submission | None. None authorized |
| Acceptance | None |
| Evidence | This file and `audits/fcc/sim_revocation.py`. No file was placed in `evidence/` |

## 10. Sources read

- FCC 26-67 (October 1, 2026): <https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf>
- Federal Register final rule, 91 FR 67214 (October 26, 2026): <https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21821.htm>
- Federal Register proposed rule, 91 FR 67239 (October 26, 2026): <https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21820.htm>
- 47 CFR 64.1200, eCFR, read November 18, 2026: <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200>
- 2024 amendments as published, 89 FR 15756 (March 5, 2024): <https://www.govinfo.gov/content/pkg/FR-2024-03-05/html/2024-04587.htm>
- Effective-date notice, 89 FR 82518 (October 11, 2024): <https://www.federalregister.gov/documents/full_text/html/2024/10/11/2024-23605.html>
- 47 U.S.C. § 227, 2023 United States Code edition: <https://www.govinfo.gov/content/pkg/USCODE-2023-title47/html/USCODE-2023-title47-chap5-subchapII-partI-sec227.htm>
- 47 CFR 1.415: <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-1/subpart-C/subject-group-ECFR239589e20cdf698/section-1.415>
- FCC rulemaking process: <https://www.fcc.gov/about-fcc/rulemaking-process>
- ABA cover page for the June 30, 2026 joint letter: <https://www.aba.com/advocacy/policy-analysis/letter-on-revocation-of-consent-under-tcpa>
- OWASP AI Exchange general controls: <https://owaspai.org/docs/1_general_controls/>
- OWASP AI Exchange contribution page: <https://owaspai.org/contribute/>
- OWASP AI Exchange charter: <https://owaspai.org/charter/>
- OWASP Top 10 for Agentic Applications 2026 (December 2025): <https://genai.owasp.org/download/52117/>
- OWASP AI Agent Security Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html>

## 11. Not verified

- The joint-letter attachment. The ACA International PDF URL returned HTTP 520. Only the ABA cover page and the Commission’s quotations were read.
- The EEI, Vibes, NCLC, ABA, REACH, and other comment and ex parte filings, except where FCC 26-67 quotes or describes them. Descriptions in this memo are the Commission’s descriptions, not an independent reading of those filings.
- The CGB waiver orders cited as 40 FCC Rcd 2395 and DA 26-12. Whether the revoke-all sentence in the eCFR copy of (a)(10) is enforceable on November 18, 2026 was not confirmed beyond the eCFR display and FCC 26-67’s recital.
- 47 CFR 1.419, 1.1206, and 1.46, except for the portions FCC 26-67 and the 2018 public letter paraphrase.
- Any edition of the United States Code after the 2023 edition linked above.
- The current text of the OWASP LLM Top 10, the OWASP ASVS, and the AI Exchange testing chapter as a separate document. The AI Exchange and agentic pages were unpinned; they can change after November 18, 2026.
- Prevalence of one-way texting, cost of a shorter honor period, small-entity burden, carrier behavior, and model labeling. No paid inference was run.
- Any external submission, acceptance, or agency response. There is none to record.
