# OX-1 — show the untrusted input behind an approval

Status: **internal-review candidate. Not ready to file, and not part of T002.** Do not attach it to the least-model-privilege pull request. Do not open it until someone approves this text.

The Exchange audit ranks this above the fail-closed wording fix, and also says it should go out later: a short issue, then a docs-only pull request, in the pattern of pull request 235. A same-week merge is not the plan. The fail-closed pull request is the one with the short path.

Document: OWASP AI Exchange, community guidance, commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441` (2026-11-16). Permalink: https://owaspai.org/go/oversight

## What this candidate would send

1. An issue, body in `issue.md`. No pull request until a maintainer wants the wording.
2. If they do, the patch in `0001-show-untrusted-input-on-approval.patch`. One new bullet under human oversight, and one sentence added to the existing testing bullet "Human oversight as a social surface." No new control name, no new testing section.

The bullet is the whole requirement. It is longer than the fail-closed clause because the naive fix — paste the retrieved text onto the approval screen — creates the problems the bullet is there to close:

- The stated rationale is model output. It can agree with the proposed action and still be the cover story for a hidden instruction.
- The span has to be rendered as plain text, or the untrusted passage redraws the approval screen.
- Secret values in tool output must be masked.
- A reviewer who is not allowed to see the span must not be asked to approve a cause they cannot read.
- The span stays off the retained retrieval log, which already stores identifiers and hashes rather than chunk text.

## Not T002

`contributions/T002-Exchange/` changes one clause about an unreachable policy engine. This directory does not.

## Not verified

`main` after `c68371ed`. No issue search after 2026-11-18. No model was run. The two packets in `examples.md` are paper fixtures.
