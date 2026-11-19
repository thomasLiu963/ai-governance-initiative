# Issue

Open this only after internal review of the exact sentences. Do not open it in the same week as the least-model-privilege pull request, and do not combine the two.

**Title:**

The approval screen should show the untrusted input behind the action

**Body:**

### Which page

`#OVERSIGHT`, human oversight, `content/ai_exchange/content/docs/1_general_controls.md` (https://owaspai.org/go/oversight).

The review interface must show "the action requested, stated rationale, relevant prior actions in the session, estimated impact, and reversibility classification." It must sanitise urgency framing. It does not require the untrusted input that led to the proposal.

### What the current text does not cover

A person can approve a payment, an email, or a merge while the only explanation on screen was written by the model that followed a hidden instruction.

Two nearby sentences do not close that.

- Deceptive-reasoning checks compare stated intent with tool calls. A hidden instruction that produces a matching rationale and a matching call passes.
- Staged commit shows the pending object. It does not show why the agent drafted it.
- `#MONITOR USE` says to log retrieval IDs and hashes rather than chunk text. That is the right rule for the retained log. It means the log is not a substitute for the approval screen.

### Proposed text

One bullet, immediately after the review-interface bullet:

> On the approval screen, show the untrusted input the trace records behind the proposal, limited to the span that bears on the action. Render that span as plain text, label it untrusted, and mask secret values that the reviewer does not need to read. If this reviewer is not allowed to see the span, do not offer approval of a hidden cause: reassign the review or deny the action. Label the stated rationale as model output. Do not copy the span into the retained retrieval log.

And one sentence on the existing testing bullet "Human oversight as a social surface" in `5_testing.md`, so the test travels with the control and does not become a new testing section:

> Include a case where the instruction is only in retrieved text and the stated rationale agrees with the action: the screen shows that span as plain text, masks a secret in it, and labels the rationale as model output.

No new control name.

The stated rationale stays on screen. It is labelled as model output, because a matching rationale is not evidence of a clean cause. The span comes from the trace (retrieved passage, tool output, or agent message), not from the model's summary. Plain text stops the span from drawing buttons, hiding itself, or restyling the page. Secrets are masked. Personal data the reviewer is not allowed to have is not dumped onto a screen they can approve from: either they can see the span, or they are not the approver. The body is not written into the long-term retrieval log.

### AI assistance

AI was used. Cursor, using Grok 4.7, read the oversight and testing text at commit `c68371ed` and drafted this issue and the two-file patch. I have read both sentences against the current page.
