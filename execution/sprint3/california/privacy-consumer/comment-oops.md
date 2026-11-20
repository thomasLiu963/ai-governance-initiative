DRAFT — NOT FILED
HOLD until the notice of proposed action is published in the California Regulatory Notice Register.
On the day of filing, read the colored proposed text. Delete any paragraph below that the underline and strikeout have already resolved. Do not file this draft against the preliminary-comment docket.

Opt-out Preference Signals (OOPS)

Public comment on the noticed proposal to amend title 11, California Code of Regulations, sections 7025, 7026, 7221, and 7222.

The comments below are limited to sentences in the October 8, 2026 proposed text and the October 12, 2026 initial statement of reasons, read against the regulations effective January 1, 2026. They do not ask the Agency to treat a browser’s result on a draft W3C test as a violation of the Civil Code.

1. How a business reads a combined `Sec-GPC` field

Proposed section 7025(b)(1) names an HTTP header field, “like Global Privacy Control (GPC),” as a format a business must process. Proposed section 7026(f)(3)(C) says the business has not complied as soon as feasibly possible when it sets a sale-or-share cookie before determining whether the GPC signal arrived. Neither sentence states how the field value is read after an HTTP stack has combined repeated lines.

A user agent that sends the signal sends the value `1`. Two such lines are often delivered to the business as one field value, `1, 1`. A comparison that accepts only a field value equal to the single character `1` treats that combined value as no signal. The consumer’s opt-out is then dropped before the timing test in section 7026(f)(3)(C) can be applied.

Civil Code section 1798.185(a)(18) authorizes technical specifications for the signal. Please add a sentence to section 7025, in or immediately after subsection (b):

When the signal is the HTTP header field `Sec-GPC`, the business has received the signal if, after field lines with that name are combined into one field value and that value is split on commas, any item equals the single character `1` once leading and trailing whitespace are removed. The values `1`, `1, 1`, and `1, 0` are the signal. The values `0` and an empty value are not. The business shall not treat the field as absent solely because the combined value is not exactly the single character `1`.

This sentence does not incorporate a W3C specification. It states the value of the signal the regulation already names. If a later commonly used signal uses a different token, the Agency can amend the token. The sentence regulates the business that receives the header. It does not regulate the browser that sends it.

Please also make the last sentence of proposed section 7025(c)(7)(F) use “opt-out preference signal,” as the first sentence of that example does. The example currently switches to “whenever it receives a GPC signal.” A signal that meets subsection (b) and is not GPC should trigger the same configuration.

2. Browser features that make their own requests

Proposed section 7025(h) says a browser feature that makes the consumer’s personal information available to a business “must not prevent, interfere with, contradict, or disable” the opt-out preference signal “from being sent.” The initial statement of reasons describes a different duty: a feature that discloses personal information must also forward the consumer’s signal.

A feature can leave ordinary navigations alone and still omit the signal on a request the feature itself makes. Please replace subsection (h) with:

If a browser, as defined in Civil Code section 1798.136(e)(1), has a feature, tool, or function that makes a request to a business on the consumer’s behalf and that request makes the consumer’s personal information available to the business, the request must carry the same opt-out preference signal, if any, that the browser would send on a consumer-initiated navigation to that business. The feature must not send a contradictory value.

Add Civil Code section 1798.136 to the reference note for section 7025. Subsection (h) uses that section’s definition, and section 1798.136(c) authorizes regulations to implement it. Section 1798.136 is operative January 1, 2027. Please make subsection (h) operative on or after that date.

The requested sentence is limited to a browser as section 1798.136 defines it: an interactive software application used to locate, access, and navigate internet websites. It does not cover a companion chatbot or another assistant that is not a browser.

3. Section 7026(g)

The regulations effective January 1, 2026, and the proposed text, say a business may display “Opt-Out Request Honored” “in accordance with section 7025, subsection (b)(6).” Section 7025(b) has paragraphs (1) and (2). It has no paragraph (6). Section 7025(c)(6) is the requirement to display whether the signal was processed, and it uses the same example. Please change the citation in section 7026(g) from subsection (b)(6) to subsection (c)(6).

4. Section 7221(b)(2)(A)

The regulation effective January 1, 2026, limits the hiring and admission exception to “the consumer’s ability to perform at work or in an educational program.” The initial statement of reasons says that clause is replaced with “performance at work or performance in an educational program,” so the exception uses the defined terms in section 7001(cc) and (dd).

The extracted proposed text reads “ability to performance at work or performance in an educational program.” If that is the operative sentence, please delete the leftover words so the clause is:

the consumer’s performance at work or performance in an educational program

5. Section 7222(b)(1)

The regulation effective January 1, 2026, forbids a generic purpose “such as ‘to improve our services.’” The initial statement of reasons says that example is replaced with “make a significant decision,” so the forbidden description matches the threshold for Article 11. The extracted proposed text reads “to make a significant decision improve our services.” If that is the operative sentence, please end the example at “to make a significant decision.”

Authority for these amendments: Civil Code section 1798.185, including subdivisions (a)(15) and (a)(18). For subsection (h), also Civil Code section 1798.136.

DRAFT — NOT FILED
