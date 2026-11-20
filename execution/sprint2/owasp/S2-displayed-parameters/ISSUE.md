Do not file this while pull request 1236 is open. File it only after that pull request merges, and only with an explicit approval. No pull request unless a maintainer asks.

Target: `1.02-dev` only. Released `1.0/` and `1.01/` stay locked.

**Title:**

[1.02] C9.2: execute only the parameters the approval displayed

**Body:**

## Gap

`9.2.2` (Level 2) requires the approval request to display canonicalized, complete action parameters. `9.2.1` (Level 1) blocks a privileged or irreversible action until explicit human approval is received and verified. `9.2.8` (Level 3) rejects execution when a cryptographically bound parameter changes.

A Level 2 assessment does not include `9.2.8`. Nothing in `9.2.1` or `9.2.2` says the parameters that run are the parameters that were displayed. A runtime can show recipient A and amount 10, receive an approval, and execute recipient B and amount 10. The display was complete, and an approval was received.

This is not `9.2.8`. That row stays the Level 3 binding to a signature, a nonce, the requester, and the execution context. The row below is the equality check, which an assessor can do without a signature. It is also not `10.4.8`, which compares a tool definition with the definition the user approved.

`9.2.12` was discussed in #1125 and #1131 for a different control, a positive-control liveness check. That text was not added, and the author withdrew it. On `main` at `abcb87056c2a39ae04422abef90c278f43cb4ac8`, C9.2 ends at `9.2.11` and `9.2.12` does not appear. This issue does not revive #1125.

## Proposed row

Append one Level 2 row. Do not renumber.

> **9.2.12** Verify that the runtime executes a privileged or irreversible action only when its parameters are the parameters displayed in the approval request that authorized the action. Level 2.

Appendix B, under AD.19, after the `9.2.11` line:

> Privileged or irreversible action executed only with the parameters displayed in the approval request that authorized it | C9.2.12

## Example

The approval screen shows recipient alice and amount 10, complete and untruncated. The tool then runs with recipient bob and amount 10.

Level 2 today: `9.2.1` and `9.2.2` can both pass. The proposed row fails. `9.2.8` would also fail, and a Level 2 assessment does not apply it.

Compliant: the tool runs with recipient alice and amount 10, or it does not run.

## AI assistance

Cursor, using Grok 4.7, read C9.2 and Appendix B at `abcb870` and drafted this issue. I will defend every sentence. I will not open a pull request unless a maintainer asks.
