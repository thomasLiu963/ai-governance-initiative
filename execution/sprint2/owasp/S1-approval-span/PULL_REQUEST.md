Open only if a maintainer asks for the wording, or after the issue in `ISSUE.md` has been open and has not been declined. Do not open this pull request on the same day as pull request 287, and do not add these commits to that pull request.

**Title:**

Oversight: show the untrusted input on the approval screen

**Body:**

The human-oversight review interface lists the action, the stated rationale, prior actions, impact, and reversibility. It does not require the untrusted input that led the agent to propose the action. A matching rationale can be the cover story for a hidden instruction.

This adds one bullet under human oversight and one sentence on the existing testing bullet "Human oversight as a social surface." No new control name and no new testing section.

The span is the trace record (retrieved passage, tool output, or agent message), rendered as plain text, labelled untrusted, with secrets masked. If the reviewer is not allowed to see it, the screen does not offer approval of a cause they cannot read. The span is not copied into the retained retrieval log.

### AI assistance

AI was used. Cursor, using Grok 4.7, read `#OVERSIGHT` and the testing bullet at commit `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb` and drafted both sentences. I have read them against that commit. The patch is the whole change.
