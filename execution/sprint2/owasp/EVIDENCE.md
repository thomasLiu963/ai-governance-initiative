# Evidence

Checked 2026-11-19. Public GitHub only. No issue, pull request, or comment was opened. No model API was called.

## Pins

| Repository | Commit | What was read |
| --- | --- | --- |
| `OWASP/AISVS` `main` | `abcb87056c2a39ae04422abef90c278f43cb4ac8` (2026-11-19T20:56:39Z, merge of #1227) | C9, Appendix A glossary line on fail-closed and on TLS, Using AISVS scope list, Appendix B AD.19 and the C9.5 block, `CONTRIBUTING.md` |
| AISVS pull request 1236 | Open. Head not merged. Diff is two additions | `9.5.8` row and the Appendix B line. Does not take `9.2.12` or edit the `9.5.7` sentence |
| AISVS issue 1232 | Open. Jim Manico, 2026-11-19T21:16:06Z: "I think this is wise, I'll add a PR here. This was my original mistake." | Not a comment on `9.5.7` or `9.2.2` |
| `OWASP/www-project-ai-security-and-privacy-guide` `main` | `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb` (2026-11-19T22:42:15Z) | Human-oversight bullets, staged commit, least-model-privilege lines 747 and 760, privacy §7 item 8, testing bullet at `5_testing.md` line 95, `CONTRIBUTING.md`, contribute page "Label AI use" |
| Exchange pull request 287 | Open. No review, no comment | The fail-open sentence is still on `main`. This sweep does not edit that line |
| Exchange issue 188 | Open. Last maintainer comment `robvanderveer`, 2026-08-03T12:40:29Z | No assignee. No pull request |
| `OWASP/www-project-ai-testing-guide` `main` | `006e4e9ee060f2ca2176037499b824e47af5360e` (2026-06-01) | APP-14 expected output still requires an explainability score of 8 and variance below 2.0. APP-13 still requires disclaimers on over 95 percent of high-stakes queries, a Disclaimer Score of 2, and an Authoritative Score of 0. Neither file defines the instrument |
| `GenAI-Security-Project/agent-control-standard` | `integration`, pushed 2026-11-19T18:52:28Z | Issues 613 and 614 filed by `MK023` with reproductions and no comments. Pull request 597 is theirs. Not taken |
| `OWASP/CheatSheetSeries` | `AI_Agent_Security_Cheat_Sheet.md` blob `e70913f` | Section 4 already binds approval to parameters and says to fail closed when approval validation fails. It does not require the untrusted cause. Issues 2948, 3000, 3003, 3014, and 3017 are open on that sheet |
| `GenAI-Security-Project/GenAI-LLM-Top10` | Open issues 161–175 | Errata and release-feedback items already have authors, mostly `drk-ram` |

`9.2.12` does not occur in the AISVS tree at `abcb870`. Closed issues #1125 and #1131 proposed that number for a liveness control. The author withdrew it on 2026-09-07. The identifier was never merged.

Least-model-privilege lines at `bde8cc6f`, still both present: "Fail closed if the policy engine is unreachable." and "policy engine outage requires an explicit fail-closed vs fail-open choice."

## Local checks

Fixtures, each exited 0:

| Script | Output |
| --- | --- |
| `S1-approval-span/reproduce.py` | Instruction absent from today's five fields. Present once the span is added. Secret masked. |
| `S2-displayed-parameters/reproduce.py` | Recipient alice displayed, bob executed. `9.2.1` and `9.2.2` pass. `9.2.8` and proposed `9.2.12` fail. |
| `S3-delegation-instant/reproduce.py` | Write is inside the grant at delegation and outside it at execution. |
| `S4-staged-release/reproduce.py` | Current rule releases the object after the role is removed. Proposed rule freezes it. |

Patches applied with `patch -p1` to copies of the pinned files:

| Patch | Clean tree | After the 1236 insertion |
| --- | --- | --- |
| `S1-approval-span/0001-show-untrusted-input-on-approval.patch` | Applied | Not applicable. Different repository |
| `S2-displayed-parameters/0001-9.2.12-displayed-parameters.patch` | Applied | Applied. Hunks are `9.2.11` and the AD.19 line, not the `9.5.8` lines |
| `S3-delegation-instant/0001-9.5.7-execution-time.patch` | Applied | Applied. Zero lines of context, so the following `9.5.8` line does not break it |
| `S4-staged-release/0001-recheck-principal-before-staged-release.patch` | Applied | Not applicable |

The 1236 check inserted that pull request's two added lines into a copy of `abcb870`. It was not a checkout of Jim Manico's branch. The sentences match the pull request diff retrieved the same day.

The S2 and S3 fixtures encode the requirement sentences. They do not execute an agent runtime. The S1 fixture encodes the field list in the current bullet. It does not render the Exchange site.

## Not verified

- https://owaspai.org/go/oversight as rendered HTML. The repository file was read.
- Slack, the Exchange authors channel, and the agentic workstream.
- Any commit after the SHAs above.
- ASVS's own TLS requirement. The AISVS contradiction is internal: the glossary says AISVS requires TLS 1.3, and Using AISVS says transport security is ASVS's.
- Claude Code's 300-second hook cutoff. Issue 614's reproduction was read and not re-run.
- Whether a Level 2 product in the field already compares displayed and executed parameters. The gap is the requirement text.
