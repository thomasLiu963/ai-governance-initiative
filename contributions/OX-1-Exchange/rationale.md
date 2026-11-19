# Why the approval screen has to show the cause, and what it must not show

## The gap, checked on commit c68371ed

Human oversight, `1_general_controls.md` line 660:

> Design review interfaces for informed decisions: the action requested, stated rationale, relevant prior actions in the session, estimated impact, and reversibility classification. Do not allow agent-generated urgency framing in the review interface without sanitisation.

Blame for lines 658–663 is the pull request 185 merge (`c3562e82`, 2026-08-03, Spyros Gasteratos). Staged commit, the next bullet, was added later by pull request 235 and shows the pending object, not the input that caused the draft.

Automated oversight, line 648, compares stated intent with tool calls. Agreement between the rationale and the call is treated as a good sign. A hidden instruction that asks for both a plausible rationale and that call does not diverge, so the check passes.

`#MONITOR USE`, `2_threats_through_use.md` line 110:

> Log identifiers and hashes rather than chunk text, since a log of the final model input is itself an augmentation data leak surface.

That sentence is why the approval screen cannot be "go and read the retrieval log." The log is required to omit the text. The approval screen is a different surface, shown to a person at decision time, and it has to be built so it does not become a second copy of the log.

A GitHub issue search for "stated rationale" on 2026-11-18 returned nothing. Issue 244 asks to separate "the tool accepted the call" from "the effect happened." It has an author and a maintainer request for a plainer account. This candidate does not comment on it. Issue 188 item 6 is about binding an approval to an action digest. The approval-token bullet now does that. It does not display the untrusted input.

The testing bullet to extend is `5_testing.md` line 95, "Human oversight as a social surface." It already tests urgency, confusion, and fatigue. It does not test a matching rationale with the instruction sitting only in retrieved text.

## The four hazards, and the clause that answers each

**Misleading model rationales.** The stated rationale stays. The new bullet labels it as model output. The cause on screen is the trace span, not a summary the model wrote for the reviewer. The testing sentence uses the case the deceptive-reasoning check misses: the rationale agrees with the action, and the instruction is only in the retrieved text.

**Interface rendering.** "Render that span as plain text" means the approval UI does not interpret the span as HTML, Markdown, CSS, or an image. White-on-white text, a fake approve button, a link, or a block of urgency wording inside the passage stays visible as text. The existing sentence about sanitising urgency framing still applies to the chrome of the screen. It does not cover a passage that is itself the interface. Bounding the span to what bears on the action also stops a retrieved page from pushing the action off the screen.

**Secret leakage.** Tool output often contains a credential next to the instruction. The reviewer needs the instruction. They do not need the secret value. "Mask secret values that the reviewer does not need to read" uses the idea `#SENSITIVE OUTPUT HANDLING` already applies to model output, without adding a new detector design or a product name. The testing sentence includes a secret in the span so a screen that shows the raw value fails the test.

**Privacy.** Two different copies are easy to mix up.

- The retained retrieval log keeps identifiers and hashes. The new bullet repeats that boundary: do not copy the span into that log. An approval record can store that a span was shown, and a hash or a pointer. It should not become a second store of chunk text.
- The person asked to approve has to see the span. If their role does not allow them to see it, offering Approve on a hidden cause recreates the original bug and adds a disclosure if the screen shows it anyway. The bullet says to reassign the review or deny the action. A source link is how a reassigned reviewer opens the span under their own access. A link the current reviewer cannot open is not a substitute for showing them the cause.

The span is the relevant part, not the whole retrieved document and not the model's paraphrase of it.

## What this does not change

- The field list already required: action, stated rationale, prior actions, impact, reversibility.
- Urgency sanitisation.
- Approval tokens, the kill switch, staged commit, and the static capability manifest.
- The `#MONITOR USE` rule to log hashes rather than chunk text.
- Deceptive-reasoning checks. They remain useful for mismatches. They are not the approval screen.

## Route

Issue first, then a pull request only if a maintainer wants the sentences. Pull request 235 (staged commit, one oversight paragraph, sixteen days to merge) is the pattern. Pull request 192 was accepted and was also called slightly too detailed. This bullet is one bullet on purpose. If a maintainer asks for fewer words, the load-bearing clauses are: show the trace span, render it as plain text, label the rationale as model output, mask secrets, and do not approve a cause this reviewer cannot see.

AI assistance has to be in the issue body, not only a commit trailer. The text is in `issue.md`. No affiliated tool is linked.

A new testing section would sit with the open testing pull requests. One sentence on the existing bullet is the version that can travel with the oversight edit.

## Not verified

- Any commit after `c68371ed`.
- Whether a live approval UI already shows trace spans. No product was reviewed.
- The external write-ups the Exchange cites for hidden instructions. They show instructions changing model behaviour. They were not re-fetched, and they are not a recorded case of a human approver being the person who was misled. The gap is the missing field in the control text.
- Slack and the agentic workstream.
