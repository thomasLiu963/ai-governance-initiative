# OWASP sprint ranking

Sweep date: 2026-11-19. Nothing in this directory was filed, posted, or pushed.

The open threads that this sweep does not touch:

- AISVS issue 1232 and Jim Manico's pull request 1236. Still open. `9.5.8` is not on `main`.
- AI Exchange pull request 287. Still open, no review. The fail-open sentence is still in `main`.

## What was searched

AISVS `main` `abcb87056c2a39ae04422abef90c278f43cb4ac8`. Exchange `main` `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb`. AI Testing Guide `main` `006e4e9ee060f2ca2176037499b824e47af5360e` (unchanged since 2026-06-01). CheatSheetSeries open issues through 3018. GenAI-Security-Project `agent-control-standard` `integration` and `GenAI-LLM-Top10` open issues. ASVS open-issue search for AI, agent, and LLM. The legacy LLM Top 10 repository, which points new work at `GenAI-Security-Project/GenAI-LLM-Top10`.

## Rank

Meaning is a missing or contradictory safeguard a deployer would have to change. Value is what an admissions reader can check after a merge. Evidence is what was read on this date. Receptiveness is public maintainer behavior, not a probability. Effort is the remaining send, not the research already done. Timing is a plausible merge, not a promise.

| Rank | Candidate | Meaning | Value if merged | Evidence | Receptiveness | Effort | Timing | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | S1. Approval screen shows the untrusted span | A person can approve an action whose cause is a hidden instruction | Human oversight control on a flagship guide | Bullet at line 660 of `1_general_controls.md`, `bde8cc6f`. No open issue states it | Pull request 235, one oversight paragraph, merged in 16 days. Rob reviews short plain diffs | Issue is written. Pull request waits on him | A February decision is the sample. A November merge is not | Selected. Ready to send on approval |
| 2 | S2. AISVS `9.2.12`, executed parameters equal the displayed ones | Level 2 can pass a swap between the screen and the tool call | One testable Level 2 row in the verification standard | `9.2.1`, `9.2.2`, `9.2.8` at `abcb870`. `9.2.12` unused | Same leaders who restored a lost row in 1236. They also close a second long issue | Issue is written. No pull request until asked | After 1236 merges. A February merge is plausible only after they agree the sentence | Selected. Do not file yet |
| 3 | S3. AISVS `9.5.7`, which instant is current | One delegated write has two conforming answers | Removes an ambiguous authorization row | Row text at `abcb870`. Section objective says execution time. `9.5.6` is Level 3 | Jim's 1232 reply did not mention this row. The Level 2 / Level 3 objection is still open | Issue is written | After S2, not beside it. Agreement is not in hand | Selected. Do not file yet |
| 4 | S4. Re-check the principal before a staged release | A revoked person can still release a staged payment or merge | Authorization check at release | Staged-commit bullet and privacy item 8 at `bde8cc6f`. Issue 188 item 7 unanswered since 2026-08-03 | The workstream was asked in August and has not answered | Comment is written. A pull request is the wrong first step | A February merge is not the forecast | Selected as a draft only. Do not send |
| 5 | Glossary says AISVS requires TLS 1.3; Using AISVS puts transport security in ASVS | False requirement claim | Small. It removes a sentence. It does not add a safeguard | Both sentences at `abcb870`. ASVS was not re-read | Possible one-line issue later. Low next to 1236 | An hour | Not this month | Not selected |
| 6 | Testing Guide APP-13 and APP-14 scores | The pass rule is a number with no instrument | Real, if maintainers review | Scores still in `006e4e9`. No merge since 2026-06-01 | The open queue has sat since June | A day of procedure text, then a pull request nobody is merging | A February submission is possible. A merge is not established | Not selected |
| 7 | Agent Control Standard, Claude Code stops at 300 s | Under `proceed`, a late deny does not stop the tool | High if fixed. The bug is already filed | Issue 614, `MK023`, no comments. Code reports the negotiated timeout for any `TimeoutError` | The reporter has several open conformance issues and pull request 597. Daily merges are from project leads | A fix needs Claude Code 2.1 to reproduce the 300 s cutoff | Their queue, not ours | Not selected. Do not take their bug |
| 8 | AI Agent Security Cheat Sheet, show the cause | The sheet requires a preview and a parameter binding. It does not require the untrusted cause | Would duplicate S1 in a noisier project | Sheet at `e70913f`. Issues 3017, 3014, 3003, 3000, and 2948 are open on that file this week | Four updates in four days. A fifth will be lost in them | — | — | Not selected |
| 9 | Restore the `9.5.6` denial and still-valid-token predicates | The row requires re-evaluation and does not require a deny | Real, and a leader already refused it | Jim Manico, 2026-11-08, on issue 1196: no change to `9.5.6` | Negative | — | — | Discard |
| 10 | Forbid presenting the end user's own credential | The parenthetical was deleted in the chapter rewrite | Easy to dismiss as already implied by `9.4.1` and `9.5.2` | #934. 1.01 narrowed the related MCP rule on purpose | Weak | — | — | Discard |
| 11 | GenAI LLM Top 10 2026 errata | Several open errata | Occupied | Issues 161–175 are largely `drk-ram`, with pull requests attached | Not an unowned gap | — | — | Discard |
| 12 | A new Exchange control, taxonomy, or tool listing | — | The submissions that stay open for months | Issues and pull requests 244, 216, 247, 188's full list | Explicitly the slow path | — | — | Discard |

## Why this order

S1 is the oversight gap with a maintainer who merges a short paragraph. S2 is the same kind of human-oversight hole in the standard that has an acceptance path, and it has to wait until 1236 is no longer the active thread. S3 is smaller and more likely to be argued as a level change, so it follows S2. S4 is a real authorization hole on a thread that has been quiet since August, so the draft stays local.

## Admissions sentences, only after the external result

These sentences are false until the merge or the published text exists.

- S1. The OWASP AI Exchange required the human approval screen to show the recorded untrusted input behind a proposed agent action, not only the model's stated rationale.
- S2. AISVS 1.02 added a Level 2 requirement that a privileged or irreversible agent action runs only with the parameters the human was shown.
- S3. AISVS `9.5.7` names the instant at which delegated authority is compared with the delegating agent's authority.
- S4. The OWASP AI Exchange required a fresh check of the human principal's authority before a staged agent action is released.

An open issue, a review comment, and a local patch are not these sentences.
