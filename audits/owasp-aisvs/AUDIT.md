# OWASP AISVS — Technical Audit

Decision date: 2026-11-18. Specification inspected at commit `092232f012ec10d654c1ca345fa10d5a5a8be12a` (merge of #1225, 2026-11-11). Issues read through 2026-11-18. No external submission has been made.

## Recommendation

Prepare one issue, and do not file it until internal review approves that specific text. The issue should restore a single Level 2 requirement: if the policy decision point for an agent action does not return a decision within the documented timeout, the runtime blocks the action. That control was accepted and merged, then disappeared in a chapter condensation, while the glossary still says AISVS requires authorization components to fail closed.

Hold the 9.5.6 wording repair until that issue shows whether the maintainers will restore lost authorization predicates. Do not resubmit the #1196 test example, and do not take any of the six open issues.

## Document status

| Item | Status | Locator |
| --- | --- | --- |
| AISVS 1.0 and 1.01 | Published OWASP community standard. Both GitHub releases are dated 2026-10-16. `1.0/` and `1.01/` are locked. | [v1.01](https://github.com/OWASP/AISVS/releases/tag/v1.01), [v1.0](https://github.com/OWASP/AISVS/releases/tag/v1.0) |
| AISVS 1.02 | Draft. Only active development tree. Header still says October 2026. | [1.02-dev/en](https://github.com/OWASP/AISVS/tree/092232f012ec10d654c1ca345fa10d5a5a8be12a/1.02-dev/en) |
| This audit's proposed text | Proposed change. Not submitted. | This file |

The [OWASP project page](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs), read 2026-11-18, still says 1.0 is the latest stable release and that 1.01 is in progress. GitHub is the newer source. A different URL in `CONTRIBUTING.md` (`https://owasp.org/www-project-artificial-intelligence-security-verification-standard/`) returned 404.

1.01 release notes say the release has 213 active chapter requirements. At the inspected 1.02 commit this audit counted 216 active rows plus retired `10.2.6`. Appendix B contained every active ID once. That count is a local check, not a claim about a later commit.

## What was read

- `CONTRIBUTING.md`, `AGENTS.md`, `RELEASE.md`, `SECURITY.md`, `MODELS.md` on `main`.
- `1.02-dev/en`, with C5, C8, C9, C10, and C12 read in full, plus Using AISVS, the glossary, and Appendix B.
- The pre-condensation C9 text at commit `19e6410889` and the post-condensation text introduced by #934 at `068b541832`.
- Issues #725 and #1196 in full. All six open issues. A bounded set of related closed issues and pull requests listed below.
- Local workspace: `research/D1/`, `research/D2/`, and `research/incident-evidence/` are not present. Nothing in those tracks can support a candidate.

Public GitHub and the OWASP project page were readable. Slack, maintainer meetings, and any discussion outside GitHub were not. `MODELS.md` describes a maintainer review lineup that names model products and would require paid inference. It was read and not run.

## Contribution route and AI-assistance rule

Non-maintainers open an issue before a pull request. Work targets `1.02-dev/` only. A minor release may append requirements. It may not renumber, reuse retired IDs, or change an existing chapter's control objective. See [RELEASE.md](https://github.com/OWASP/AISVS/blob/main/RELEASE.md) and [CONTRIBUTING.md](https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md).

AI assistance is explicitly allowed, including for drafting issues, provided the contributor will defend every sentence and the control is concrete and testable. On 2026-11-17 and 2026-11-18, Otto Sulin (collaborator) and Jim Manico (member and project leader) closed #1215 and #1216 after saying long generated discussion is not readable and asking for a concise human restart. #1228 and #1229 were closed on 2026-11-17 because the issue was still assigned to someone else. A useful submission here is a short issue that quotes the current row, states one missing predicate, and waits.

Security reports go to jim@owasp.org under `SECURITY.md`. A missing requirement is an issue, not a vulnerability report.

## Issues named in the assignment

### #725 — closed, and the control that landed was later shortened

[Issue #725](https://github.com/OWASP/AISVS/issues/725), opened 2026-04-28 by vatsalgupta (contributor), closed 2026-05-11 as completed. It asked for continuous access evaluation of delegated user sessions, preferably with CAEP. Otto Sulin questioned whether agent frameworks implement that. Rico Komenda suggested Level 3. Jim Manico rejected a CAEP dependency and wrote one backend requirement: re-evaluate current policy for the agent's identity on every privileged action, reject the action when policy no longer allows it, and do so even if the presented token is still valid.

[PR #805](https://github.com/OWASP/AISVS/pull/805) added that sentence as `9.6.7` at Level 3. Jim Manico approved it on 2026-05-11 and it merged the same minute. No separate review comment body was retrieved.

On 2026-06-15, [PR #934](https://github.com/OWASP/AISVS/pull/934) by Jim Manico replaced that sentence with the current `9.5.6` text. The PR body is empty and no review is recorded. The current row, in `1.02-dev/en/0x10-C09-Orchestration-and-Agentic-Action.md`, is:

> **9.5.6** Verify that long-running agent sessions re-evaluate current backend authorization policy on every privileged action. Level 3.

The same wording is in locked 1.0 and 1.01. The dropped predicates are "reject the action when current policy no longer authorizes it" and "even if the presented token remains valid."

### #1196 — closed, no specification change, example not to be resubmitted

[Issue #1196](https://github.com/OWASP/AISVS/issues/1196), opened 2026-10-24 by mahfzal87, assigned to mahfzal87 and jmanico, label `1.02`. Closed 2026-11-08 with GitHub reason `not_planned`.

Jim Manico agreed that an enqueue-time allow does not show the action is authorized when it runs, asked for the example to be written in the issue, and on 2026-11-08 told the author to open a PR into `1.02-dev/research`. Later the same evening he withdrew that request: #1211 and #1212 removed the research pages. He said the example should stay in the issue, that it would also fit the OWASP AI Testing Guide, and that no change to `9.5.6` was needed. mahfzal87 accepted that on 2026-11-18. No pull request references #1196.

The queued-action procedure, the three evidence claims, and the approval-gate variant already have an owner and a maintainer decision. Filing them again against AISVS repeats a closed proposal. Using AISVS already points testing procedure to the [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/). That guide was not audited here.

## Occupied or declined work

Six issues are open. None carry `help wanted`.

| Issue | Owner signal | Why it is not a candidate |
| --- | --- | --- |
| [#1226](https://github.com/OWASP/AISVS/issues/1226) `8.3.1` wording | sydseter, assigned. Otto Sulin agreed on 2026-11-15. | Wording is already under discussion. #1229 was closed so the assignee could submit it. |
| [#1220](https://github.com/OWASP/AISVS/issues/1220) agent skills | Jim Manico asked cvas22 to draft rows. [PR #1227](https://github.com/OWASP/AISVS/pull/1227) is open. | Assigned feature work. |
| [#1217](https://github.com/OWASP/AISVS/issues/1217) rollback restoring revoked authority | Mayur021. On 2026-11-17 Otto Sulin said C3.3 is about model deployment, not agents. | Live placement dispute. |
| [#1195](https://github.com/OWASP/AISVS/issues/1195) `5.1.1` and `5.1.2` levels | Decision recorded 2026-11-10: retire `5.1.1` as overlapping ASVS 7.5.3; lower `5.1.2` to Level 2. [PR #1221](https://github.com/OWASP/AISVS/pull/1221) is open. | Decided, and the PR exists. |
| [#1187](https://github.com/OWASP/AISVS/issues/1187) physical actuation | Jim Manico asked sattyamjjain on 2026-11-08 to open a C13 chapter. | Large, already invited. |
| [#1122](https://github.com/OWASP/AISVS/issues/1122) locale and case folding | Assigned to jmanico, ottosulin, and the original author. #1228 closed 2026-11-17. | Waiting on the issue owner. |

Also declined, and not recommended for revival as the same proposal:

- #1152, stale reversibility classification. Otto Sulin closed it 2026-09-16 as too aspirational for 1.01. MCP tool-definition binding was later handled separately by `10.4.8`.
- #1214, agent-writable logs. Closed 2026-11-17 as general log protection, deferred to ASVS.
- #1215 and #1216, kill-switch exercise and reach. Closed 2026-11-18 with a request that those contributors restart concisely. `C9.6` still ends at `9.6.3`. The technical point was not merged. It also was not left unowned.

## Review history used for timing

GitHub `authorAssociation` is the role recorded below. Merger identity is stated only where the review or PR view showed it. These are examples, not an acceptance rate.

| Item | Opened | First maintainer response | Merged or closed | Role | Result |
| --- | --- | --- | --- | --- | --- |
| [PR #683](https://github.com/OWASP/AISVS/pull/683) fail-closed row, from #676 | 2026-04-13 | Rico Komenda commented 2026-04-13 | Merged 2026-04-13 | CONTRIBUTOR (emmanuelgjr) | One agreed row merged the same day. Later removed by #934. |
| [PR #1117](https://github.com/OWASP/AISVS/pull/1117) adds `9.5.7`, from #1104 | PR 2026-07-23. Issue discussion visible from 2026-07-13 | Otto Sulin approved 2026-07-24 | Merged 2026-07-30 | CONTRIBUTOR (Mayur021) | Narrow authorization row after issue agreement. |
| [#1201](https://github.com/OWASP/AISVS/issues/1201) / [PR #1204](https://github.com/OWASP/AISVS/pull/1204) restore `10.4.8` to Level 2 | Issue 2026-10-21. PR 2026-10-25 | Jim Manico 2026-10-24. Otto Sulin the same day called the Level 3 move an editing mistake | Merged 2026-11-04. No pull-request review object was returned | CONTRIBUTOR (paolocostanzo) | Maintainers do restore a requirement lost in an edit. |
| [#1190](https://github.com/OWASP/AISVS/issues/1190) / [PR #1219](https://github.com/OWASP/AISVS/pull/1219) secure aggregation | Issue 2026-10-04. PR 2026-11-09 | Jim Manico 2026-10-24 | Jim Manico merged 2026-11-11 | CONTRIBUTOR (nikhilred2619) | About five weeks from first response to merge, after scope was cut back on the issue. |
| [#1202](https://github.com/OWASP/AISVS/issues/1202) / [PR #1218](https://github.com/OWASP/AISVS/pull/1218) MCP launch approval | Issue 2026-10-21. PR 2026-11-09 | Rico Komenda commented on the PR 2026-11-10 and approved 2026-11-10 | Jim Manico merged 2026-11-11 | CONTRIBUTOR (paolocostanzo) | Fast once the issue text was settled. |
| [PR #1209](https://github.com/OWASP/AISVS/pull/1209) split C2.2 | 2026-10-28 | Otto Sulin closed it 2026-10-31 | Not merged | Author AnimeshShaw | Rejected because the split added new requirement content. |
| [PR #1228](https://github.com/OWASP/AISVS/pull/1228) and [#1229](https://github.com/OWASP/AISVS/pull/1229) | 2026-11-14 | Otto Sulin 2026-11-17 | Closed, not merged | cvas22 | Rejected for process: the assigned issue was not finished. |

Maintainer pull requests, including #934, #1212, and #1225, often show no review. That pattern is not evidence that an external one-line change will merge unreviewed.

## Candidates

### 1. Block the action when the authorization decision does not arrive

1. **Gap.** No current requirement says what happens when the policy decision point is unreachable or returns nothing. The glossary still states a requirement that the tables do not contain. In `1.02-dev/en/0x90-Appendix-A_Glossary.md`, the Fail-Closed entry says: "AISVS requires AI components with safety or authorization responsibilities to fail closed." A search of `1.02-dev/en/0x10-*.md` found no "fail closed", "fails closed", or "unavailable". `5.2.5` isolates the decision point. `9.5.3` says a returned decision is not made by the model. `9.6.2` blocks an action whose human approval times out. None of those covers a missing authorization decision.

2. **Evidence it is open.** [Issue #676](https://github.com/OWASP/AISVS/issues/676) described this distinction. Rico Komenda wrote on 2026-04-11 that the gap was real and that Level 2 was appropriate. [PR #683](https://github.com/OWASP/AISVS/pull/683) merged the control on 2026-04-13. At commit `19e6410889` it was still present as `9.7.4`: when the PDP is unavailable, agent execution fails closed by blocking the action, and the event is logged. [PR #934](https://github.com/OWASP/AISVS/pull/934) removed it on 2026-06-15 with no stated reason. Locked 1.0 and 1.01 shipped without the row and with the glossary sentence. No later issue in the searches for "fails closed", "policy decision point", or "9.7.4" reopens the loss. It is not one of the six open issues.

3. **Consequence.** A runtime that calls a policy engine and proceeds when that call times out can still match `9.5.1`, `9.5.3`, and `5.2.5`. Disrupting the decision point then disables authorization. The glossary tells an adopter the standard already forbids that.

4. **Proposed deliverable.** One appended Level 2 row in C9.5, next free ID `9.5.8`, plus the matching Appendix B row. Do not restore the old logging clause in the same row. Logging is a second test, and recent review rejects bundled rows. Proposed text:

   > **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the documented timeout, the runtime blocks the action. Level 2.

   The issue should quote `9.7.4` from commit `19e6410889`, quote the glossary sentence, and quote Rico Komenda's 2026-04-11 confirmation. It should not propose CAEP, a new chapter, or a revival of C9.7.

5. **D1, D2, incidents.** No. Those directories are absent. The evidence is the requirement history and the current text.

6. **Experiment.** No. The defect is that the normative sentence and the requirement table disagree. A runtime fixture is not needed to show that. If maintainers later want a test, the smallest one is a local stub that accepts connections and never returns a decision, then records whether the tool call changed a synthetic resource. That stub does not need a model API.

7. **Effort and cost.** Writing the issue is a few hours. No API cost. An adopter who already calls a policy engine on each action adds a timeout and a default deny. This audit did not measure how many agent frameworks already do that. #725 is the caution: do not claim broad framework support without checking it before the issue is finalized.

8. **Route and reception.** Issue first, against 1.02, then a PR only if a leader asks. AI use stays inside the contributor's own short text. Closest positive histories are #683 (same control, previously accepted) and #1204 (an editing loss restored after it was named as such). #934 deleted this row inside a much larger cut, so the issue must not describe the whole cut as accidental.

9. **Deadlines.** By 2026-11-30 the realistic product is an internally approved issue, not a merge. Same-day merges in this sample happened only after a leader had already agreed the exact row. By 2027-02-15 a merge into `1.02-dev` is realistic if the issue stays one sentence. No 1.02 release date is published, so inclusion in a numbered release is not a forecast.

10. **Accurate accomplishment, if it lands.** A Level 2 AISVS 1.02 requirement that an agent action is blocked when its policy decision point does not return a decision, restoring the property merged in #683 and aligning the requirement table with the glossary.

11. **Evidence to keep.** Links above, the quote from commit `19e6410889`, the current glossary sentence, and, later, the issue URL, PR URL, and merge commit. Acceptance means that merge, not a draft.

### 2. Say when "current authority" in 9.5.7 is current

1. **Gap.** `9.5.7`, added by #1117 and called out in the 1.01 release notes, says: "Verify that authority derived through delegation never exceeds the delegating agent's current authority." Level 2. "Current" is not defined. One reading compares authority at delegation. The other compares it when the delegated action is authorized for execution.

2. **Evidence it is open.** [Issue #1104](https://github.com/OWASP/AISVS/issues/1104) and the merged wording discuss narrowing across a delegation, not a later revocation. Searches for `9.5.7` did not find a follow-up about timing. #1196 tests revocation of the same principal's queued action under `9.5.6`, not derived authority under `9.5.7`.

3. **Consequence.** Two assessors can reach opposite results on one delegated call made after the parent agent's grant is reduced. The Level 2 control can be treated as either a one-time subset check or a continuing one. `9.5.6` is Level 3 and applies to privileged actions in long-running sessions, so it does not settle the Level 2 delegation row.

4. **Proposed deliverable.** A wording issue, not a new row. Ask the leaders which instant they intend, and offer two replacement sentences:

   - Execution: "Verify that authority derived through delegation does not exceed the delegating agent's authority at the time the delegated action is authorized for execution."
   - Delegation: "Verify that authority derived through delegation does not exceed the authority the delegating agent held when it delegated."

   The execution sentence is the one that matches the word "current" and the authorization theme. It may be rejected because it pulls a continuous check down to Level 2. The delegation-time sentence still removes the ambiguity and should be the fallback in the same issue. Do not file both as separate issues.

5. **D1, D2, incidents.** No.

6. **Experiment.** No. This is an ambiguity between two readings of one published sentence. A revocation fixture would illustrate the execution-time reading. It would not decide which reading the project intended.

7. **Effort and cost.** Shorter than candidate 1. No API cost. Adopter impact depends on which sentence is chosen. Delegation-time is a check the delegating runtime can do once. Execution-time requires the downstream decision to see the parent's authority again.

8. **Route and reception.** Issue first. This is the sort of single-sentence clarification that #1117 and #1204 show can move. The level collision with `9.5.6` is the foreseeable objection. AI assistance policy is the same as above. Keep the issue to the two sentences and the quote.

9. **Deadlines.** By 2026-11-30, an approved issue can be opened and may already have a leader's preference. A merge by that date is possible and not something to plan on. By 2027-02-15, a merged wording change in `1.02-dev` is a reasonable outcome. A numbered release is not.

10. **Accurate accomplishment, if it lands.** AISVS `9.5.7` names the instant at which delegated authority is compared with the delegating agent's authority, so an assessment no longer has two conforming answers.

11. **Evidence to keep.** Current row, [1.01 release note](https://github.com/OWASP/AISVS/releases/tag/v1.01) mentioning `C9.5.7`, #1104, #1117, and the eventual issue and merge.

### 3. Put the denial and the still-valid token back into 9.5.6

1. **Gap.** `9.5.6` requires re-evaluation and does not require a consequence. The row Jim Manico wrote, and approved in #805, also required rejection when current policy no longer authorizes the action, even if the presented token remains valid. Those two predicates are absent from 1.0, 1.01, and 1.02-dev. "Privileged action" is also undefined. The release notes for 1.01 say `9.2.1` applies to privileged or irreversible actions and no longer applies merely because an action is high-impact. They do not define privileged. This candidate does not try to add that definition.

2. **Evidence it is not already handled.** The predicates are absent from the three version folders. #1196 is not a fix: its maintainer comment says the requirement itself should not change, and the test example lives only in the closed issue. That comment is also the reason this candidate is not first. It may be a decision to keep the short sentence, recorded without saying so. No pull request after #934 restores the predicates. Appendix B's non-normative pitfall, "not re-checking authorization when context changes mid-session," is broader than `9.5.6` and does not create a requirement. Appendix B says the inventory is non-normative.

3. **Consequence.** An implementation can log a fresh read of token claims and continue a privileged call after the backend grant was revoked, and still point at a re-evaluation record. The #1196 procedure expects a denial. The requirement text does not.

4. **Proposed deliverable.** Only if candidate 1's reception shows appetite for restoring a lost predicate. Then one issue, quoting both sentences, with this proposed replacement and no new ID:

   > **9.5.6** Verify that long-running agent sessions re-evaluate current backend authorization policy on every privileged action, reject the action when current policy no longer authorizes it, and do so even if the presented token remains valid. Level 3.

   This is the #805 sentence without "for the agent's identity," which had narrowed the check to the agent rather than the delegated user. State that omission in the issue so it is a choice rather than a silent edit. Do not attach the queued-action procedure, the approval-gate variant, or a request to recreate `/research`.

5. **D1, D2, incidents.** No. #725 argued the property. It did not supply a measured incident.

6. **Experiment.** No, for the same reason as candidate 1. The smallest later fixture is the one already written in #1196: a still-valid credential, a revoked grant, and an effect record. Reproducing it would be a test of some product, not evidence that the AISVS sentence is short.

7. **Effort and cost.** A few hours to write. No API cost. Adopter impact is a deny on the execution-time check, which is larger than a log line and is why the original row was Level 3.

8. **Route and reception.** Issue first, and not before candidate 1 has a response. Positive precedent is #805 itself and the #1204 restoration of an edit. Negative precedent is Jim Manico's 2026-11-08 comment on #1196. Filing this as a repeat of #1196 or #725 is likely to be closed. Filing it as "these two predicates were in the merged sentence and are not in the current sentence" is the accurate framing. AI policy is unchanged.

9. **Deadlines.** By 2026-11-30 this should remain an internal draft unless candidate 1 has already drawn a favorable reply. By 2027-02-15 a merged wording change is possible and depends on that reply. It is not the default forecast.

10. **Accurate accomplishment, if it lands.** `9.5.6` again requires the privileged action to be rejected when current policy does not allow it, including when the presented token has not expired.

11. **Evidence to keep.** #725, #805 diff, #934 diff, current `9.5.6`, and #1196's "no change" comment. A later acceptance still needs its own merge commit.

### 4. Stop an agent from presenting the user's own credential

1. **Gap.** Before #934, `9.4.1` said the agent authenticates as a first-class principal and does not reuse end-user credentials. `9.6.2` said the delegation context is propagated without using the user's credentials. Current `9.4.1` keeps the separate identity and drops the parenthetical. Current `9.5.2` requires an integrity-protected, scope-limited token and does not forbid also presenting the user's own credential. Appendix B lists "reusing end-user credentials for agent-to-agent calls" as a common pitfall under AD.1. The appendix says it adds no requirements.

2. **Evidence it is open.** The parenthetical is in the removed half of the #934 diff and is absent from the current C9 file. Searches for "end-user credentials" and "without using the user" returned no issue. #1100 is a different, closed change: the 1.01 notes say `10.2.7` replaced a blanket prohibition on passing through client-received access tokens for MCP servers. This candidate must not reopen that MCP decision.

3. **Consequence.** An agent can satisfy `9.4.1` and `9.5.2` by holding its own identity and also forwarding the user's session or password. Downstream authorization then collapses to the user's full credential. That is a different failure from `10.2.7`, which is about tokens issued for some other audience.

4. **Proposed deliverable.** A new Level 2 row, `9.4.5`, only if the leaders treat candidate 1 as in scope. Proposed text:

   > **9.4.5** Verify that an agent calling a downstream system does not present an end user's own credential as the credential for that call. Level 2.

   The issue should say a scope-limited delegation token under `9.5.2` is the expected substitute, without turning this row into a second copy of `9.5.2`.

5. **D1, D2, incidents.** No. #1100 names the Supabase/Cursor incident for an MCP token problem. This audit did not re-verify that incident against a primary report, and it is not evidence for this row.

6. **Experiment.** No. A local two-credential stub could show the difference later. It is not required to establish that the clause is missing.

7. **Effort and cost.** A few hours. No API cost. Adopter impact is larger where products intentionally pass a user session into tools. That implementation debate is the main reason this is ranked last.

8. **Route and reception.** Issue first. Weaker than candidate 1 because the deletion sits inside Jim Manico's own condensation, and because 1.01 deliberately narrowed a related MCP prohibition. A leader can call the separate identity plus `9.5.2` sufficient. The pitfall line is not a normative promise. Same AI-assistance constraint.

9. **Deadlines.** Do not plan an external filing by 2026-11-30. By 2027-02-15 this is a possible second issue, not a likely merge, unless the reply to candidate 1 invites further restoration.

10. **Accurate accomplishment, if it lands.** AISVS distinguishes an agent's credential from the end user's own credential and verifies that the agent does not present the latter on a downstream call.

11. **Evidence to keep.** The removed `9.4.1` and `9.6.2` lines in #934, current `9.4.1` and `9.5.2`, Appendix B AD.1, and the 1.01 note on `C10.2.7` so the issue does not contradict it.

## Rank

| Rank | Candidate | Why this position |
| --- | --- | --- |
| 1 | PDP timeout blocks the action | Previously accepted, still contradicted by the glossary, one testable predicate, closest to the restorations maintainers already merge. |
| 2 | Define the instant in `9.5.7` | Smallest change and a real double reading. The Level 2 versus Level 3 argument is the known risk. |
| 3 | Restore the `9.5.6` denial and still-valid-token predicates | Highest tie to #725 and #1196, and a leader has already said not to change the row. Prepare it. Do not lead with it. |
| 4 | Do not present the user's own credential | Real deletion, easier to dismiss as already implied, and adjacent to an MCP decision that 1.01 narrowed on purpose. |

## What this audit did not verify

- Maintainer intent for each deletion inside #934. The PR records no explanation.
- Discussion on Slack. #1195 mentions a poll that was not found here.
- The OWASP AI Testing Guide's contents, beyond the pointer in Using AISVS.
- Whether current agent frameworks time out closed, re-check delegation at execution, or reject a still-valid token. Those facts would matter before promising that a level is implementable. They were not tested, and no paid model calls were made.
- Any commit on `main` after `092232f` . The last fetched commit is 2026-11-11. Issue comments after that date were read. The requirement files were not observed to change after that commit.
