Do not file this while pull request 1236 is open, and do not file it in the same week as the C9.2 parameter issue. File it only after an explicit approval, and only if the C9.2 issue has not been declined as one authorization issue too many. No pull request unless a maintainer asks.

Target: `1.02-dev` only.

**Title:**

[1.02] C9.5.7: which instant is "current authority"?

**Body:**

`9.5.7`, Level 2, says: "Verify that authority derived through delegation never exceeds the delegating agent's current authority."

"Current" has two readings.

- Delegation time. The check compares the grant with the authority the delegating agent held when it delegated.
- Execution time. The check compares the grant with the delegating agent's authority when the delegated action is authorized for execution.

The section objective says every action is authorized at execution time. The word in the row is "current", which fits the second reading. `9.5.6` re-evaluates backend policy on every privileged action, at Level 3, and does not say which instant `9.5.7` uses. Two Level 2 assessments can disagree on one delegated call made after the parent grant is reduced.

#1104 and #1117 discuss narrowing across a delegation. They do not pick the instant. No open issue asks which instant "current" means.

Preferred replacement, one sentence, same level, no new identifier:

> **9.5.7** Verify that authority derived through delegation does not exceed the delegating agent's authority at the time the delegated action is authorized for execution. Level 2.

If that pulls a continuing check down to Level 2, the other sentence removes the ambiguity without doing so:

> **9.5.7** Verify that authority derived through delegation does not exceed the authority the delegating agent held when it delegated. Level 2.

I am asking for one of those two sentences, not for both, and not for a new row.

## Example

At delegation the parent agent holds read and write. Before the child runs, write is revoked. The child writes.

Delegation-time reading: pass. Execution-time reading: fail. Both can be argued from the current sentence.

## AI assistance

Cursor, using Grok 4.7, read `9.5.7` at `abcb87056c2a39ae04422abef90c278f43cb4ac8` and drafted the two sentences. I will defend both. I will not open a pull request unless a maintainer asks.
