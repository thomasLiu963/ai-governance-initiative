# Examples

These stay in the pull request and in this packet. They are not added to the page. The page change is the one clause in `0001-unreachable-policy-engine-denies-the-action.patch`.

The action in each case is one that the policy engine is already the evaluation point for: a tool call, data access, an inter-agent message, or outbound communication. That scope is the existing policy-based access control bullet. This patch does not widen it.

## 1. Payment while the engine is down

The agent calls a payment tool: 18,000 to a new account. The policy engine cannot be reached. No permit and no deny comes back.

Today, two readings are both available in the published control.

- The runtime bullet says fail closed. The payment is denied.
- The Limitations sentence says an outage requires an explicit fail-closed versus fail-open choice. A team writes "fail open during engine maintenance so payouts are not blocked" and sends the payment. They are quoting the page.

After the patch, the Limitations sentence says to deny the action. The maintenance note no longer has a sentence to cite. The payment waits until the engine returns a permit.

An adopter who already denies on an unreachable engine changes nothing.

## 2. Outbound mail, and a mailbox read, in the same outage

The agent has a draft to a customer list. The engine is unreachable.

The email example directly under the Limitations paragraph is unchanged. It says to limit a summarizer to the messages the user can already read, and to keep that access read-only so the model cannot be talked into sending mail. That is a privilege reduction for a working engine. It is not a rule about what happens when the engine cannot be asked.

Under the patched clause the send is denied. A read of the mailbox is denied as well, for the same reason: the engine did not return a decision, and this control does not split an outage into "writes deny, reads proceed." The read-only limit in the email example remains in force when the engine is healthy.

## 3. The engine answers

Unchanged.

- A permit allows that action.
- A deny blocks it.
- Conflicting policies still default to deny.
- Per-action evaluation still adds latency. That cost stays in the same sentence.
- Short token lifetime, revocation, delegation attenuation, and revocation-latency tolerance stay in the previous sentence.

## 4. A reachable engine that never answers

Out of scope for this patch. The published trigger, and the patched clause, say "unreachable." A process that accepts the connection and returns nothing is a different gap. It is the sort of case a verification requirement can name as a timeout. This pull request does not rename "unreachable," and it does not add a timeout.
