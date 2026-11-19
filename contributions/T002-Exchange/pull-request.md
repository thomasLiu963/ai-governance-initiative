# Pull request

Do not open an issue first. `CONTRIBUTING.md` at commit `c68371ed` says small clarifications and doc fixes may be pull requests without an issue. This is one clause in one file.

**Base:** `main` at `c68371ed56051a3d7c894e36c20c3bcbc22eb441` (2026-11-16). Re-read the limitations sentence on current `main` before opening. If that sentence has already changed, stop.

**Title:**

Least model privilege: deny the action when the policy engine is unreachable

**Body:**

### Which page

`content/ai_exchange/content/docs/1_general_controls.md`, control **#LEAST MODEL PRIVILEGE** (https://owaspai.org/go/leastmodelprivilege). One file. One clause, in the Limitations paragraph under the agentic authorisation block. Docs only.

### Problem

The same control gives two instructions for one event.

Runtime policy validation says: "Fail closed if the policy engine is unreachable."

The Limitations paragraph says: "policy engine outage requires an explicit fail-closed vs fail-open choice."

Both sentences were added in the same integration, pull request 185, in the commit that brought in the agentic authorisation block (`693d59d6f7`, merged as `c3562e82` on 2026-08-03). The pull-request discussion does not treat them as different rules. A later permalink edit (`e6679119`, 2026-08-24) changed a link on the Limitations line and left the choice in place. No open issue or pull request uses the words "fail-open."

An implementer can allow a tool call, a data read, a message, or an outbound send while the policy engine is unreachable, and can cite the Limitations sentence. Another team can deny the same call and cite the implementation sentence. For an agent that can change state or send data, fail open means the authorisation gate is missing exactly when it cannot be evaluated.

The other sentences in this block already point the same way: deny-by-default, no action until a permit or deny returns, and default deny when policies conflict. This patch does not touch them.

### Change

Replace the choice clause with: "if the policy engine is unreachable, deny the action."

The implementation sentence stays, including the words "Fail closed." Latency, revocation-latency tolerance, and the email example stay. No new control name, no new permalink, and no product or tool name.

### AI assistance

AI was used. Cursor, using Grok 4.7, read `#LEAST MODEL PRIVILEGE` at commit `c68371ed`, the commit that added both sentences, and the contribution rules, and it drafted this pull-request text and the one-clause patch. That draft was checked against those sources. I have read the patch and both sentences. No product I am affiliated with is mentioned.
