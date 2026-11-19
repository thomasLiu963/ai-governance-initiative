# T001 — Block the agent action when its policy decision point returns no decision

Status of this packet: proposed change, prepared for internal review. Not submitted. No pull request has been opened, and `9.5.8.patch` has not been sent anywhere.

Inspected source: OWASP AISVS `1.02-dev`, commit `092232f012ec10d654c1ca345fa10d5a5a8be12a` (merge of #1225, 2026-11-11). That commit was still `main` on 2026-11-18. `1.0/` and `1.01/` are locked published releases. The requirement text below is from the draft. The issue and the patch are local proposals.

Decision: the gap survives. File the issue in `ISSUE.md` after you have read it and can defend every sentence. Do not file a pull request with the patch unless a project leader asks for one.

## Comprehension brief

AISVS tells an adopter, in the glossary, that authorization components fail closed. The requirement tables no longer say what happens when the component that decides an agent action does not answer.

That missing sentence was a real requirement. It was discussed in #676, merged in #683 on 2026-04-13, and was still requirement `9.7.4` on the morning of 2026-06-15. The levels review merged that morning, #928, kept it at Level 2. Later the same day, #934 rewrote the chapter and deleted the whole C9.7 section, including `9.7.4`. The pull request body is empty and there is no review. I cannot point to a comment that says this particular failure was rejected. I also cannot call the whole rewrite an accident. The accurate claim is narrower: the predicate disappeared inside that rewrite, and nothing since puts it back.

The rows that remain do a different job. `9.5.1` and `9.5.3` require a runtime policy decision that the model does not make. `5.2.5` requires that decision point to sit outside the agent. `9.6.2` blocks an action when a person does not approve in time. None of them says the runtime blocks the action when the policy decision point itself is silent, errors, or drops the connection. A runtime can pass those checks and still run the tool after the decision call times out. That is the bypass: disrupting the decision point disables authorization.

The proposed fix is one new Level 2 requirement, `9.5.8`, in the draft only: if that decision does not arrive within the defined timeout, the runtime blocks the action. It does not revive the old section, the old identifier, or the logging clause that used to share the row. It does not change `9.5.6`, and it does not resubmit the queued-action test from #1196.

Level 2 is the level a collaborator already accepted and the level of the neighboring controls. The implementation, for a runtime that already calls a policy engine per action, is a timeout and a default block. Availability of the policy engine is a separate problem, handled by redundancy, which is what NIST SP 800-207 §5.2 says. I have not checked whether current agent frameworks already time out closed, and I should not claim that they do.

## What was re-read

Public GitHub only. No issue, pull request, or other external change was made. No paid model call was made.

| Item | What it shows |
| --- | --- |
| `CONTRIBUTING.md`, `AGENTS.md`, `RELEASE.md` on `main` | Issue before pull request for a non-maintainer. Work targets `1.02-dev/` only. A minor release may append a requirement. It may not renumber, reuse a retired identifier, or reopen a removed section. |
| `1.02-dev/en` chapter files, glossary, Appendix B, and Using AISVS, at `092232f` | No requirement contains "fail closed", "fails closed", or a missing authorization decision. The glossary sentence is still present. |
| Locked `1.0/` and `1.01/` C9 and glossary | Same glossary sentence. Neither release contains `9.5.8` or `9.7.4`. |
| #676 and #683 | The missing-decision case was accepted as its own Level 2 control. |
| Commit `19e6410889` and #928 | `9.7.4` was still the full fail-closed sentence, and the levels review merged by Jim Manico that morning kept it at Level 2. |
| #934, merge `068b541832`, 2026-06-15 14:24 UTC | Jim Manico's chapter replacement deleted `9.7.4` with the rest of C9.7. Empty body. No review. No comment. |
| #764, merged 2026-05-08 | Rico Komenda added the glossary sentence while `9.7.4`'s predecessor was still in the standard. The sentence was not revised when the row disappeared. |
| ASVS 5.0.0 V8 and V16 | V8 has no fail-closed-on-unavailable-PDP requirement. V16.5.3 is the general "fail securely when an exception occurs" requirement. |
| Open issues #1226, #1220, #1217, #1195, #1187, #1122, and open PRs #1227 and #1221 | None proposes this row. #1227 adds C9.3 skill requirements and also edits Appendix B. It does not take `9.5.8`. |
| #1196 | Closed `not_planned` on 2026-11-08. Jim Manico's last comment says no change to `9.5.6`, and the worked example stays in that issue. |

Issue search on 2026-11-18 for "fail closed", "fails closed", "9.7.4", and "policy decision point" found #676 and #683 as the history of this control. It did not find a later proposal to restore the row.

## Was the removal intentional?

The chapter rewrite was an intentional edit by the project leader. A decision that this failure mode should stop being a requirement is not in the record.

The sequence on 2026-06-15 is the evidence:

1. At 11:16 UTC Jim Manico merged #928. The pull request's levels table includes "C9.7.4 | L2 | Fail-closed when PDP unavailable. Aligns with C10.6.1 (L2), C14.2.2 (L2)." The merged tree, `19e6410889`, still contains the full `9.7.4` sentence, including the block and the separate logging clause.
2. At 14:24 UTC he merged #934, which deletes C9.5 through C9.9 as they then stood and writes a shorter chapter. `9.7.4` is in the deleted lines. No replacement sentence says the runtime blocks when the decision point is unavailable.

#928's "aligns with" note is a level comparison, not a claim that another row already tested this failure. The two neighbors were different controls:

- `14.2.2` was the human-approval timeout. It survives as `9.6.2`: when the approval gate is not satisfied within the defined approval time, the system blocks the pending action.
- `10.6.1` was MCP-only: if schema validation, protocol negotiation, authentication, or policy evaluation fails or cannot be completed, deny the request. That row is absent from `1.0/`, `1.01/`, and `1.02-dev`.

#709, the April 2026 reduction pass, removed C9 requirements the author classified as generic ASVS coverage. This control was added on 2026-04-13, the reduction merged on 2026-04-23, and the control was still present afterward as `9.7.4`. The reduction pass is not the deletion.

## What current requirements actually check

| Requirement | What an assessor can verify | The missing-decision case |
| --- | --- | --- |
| `9.5.1` | Agent actions are authorized against a runtime policy that limits tools and parameter values. | A policy that is consulted when the engine answers. Silence is unspecified. |
| `9.5.3` | The model is not the access-control decision maker. | Says who decides when a decision exists. |
| `5.2.5` | The policy decision point is isolated from the agent. | Isolation creates the call that can fail. It does not define the failure result. |
| `5.2.1` | AI resources use allow-lists and default-deny. | Datasets, endpoints, indexes, and compute. An agent tool call whose decision call returned nothing. |
| `9.6.2` | Human approval that misses its defined time blocks the action. | The approval gate, not the policy decision point. This is the pattern `9.5.8` copies. |
| `7.1.3` | An unreadable, refusing, or failed model response does not trigger the action. | `9.5.3` forbids the model from being the authorization decision. |
| `10.4.15` | An MCP schema that fails validation because an external `$ref` is unresolved is rejected. | One MCP schema case. |
| ASVS 5.0 `16.5.3` | The application fails securely when an exception occurs, and does not process a transaction because validation logic errored. | A tool invocation that continues after an empty authorization result, with no exception, can sit outside that sentence. |
| Glossary, Fail-Closed | States that AISVS requires safety or authorization components to fail closed. | Appendix A defines terms. The requirement tables are the normative list. The sentence has no requirement id behind it. |

`9.5.6` re-evaluates backend policy on every privileged action in a long-running session. It does not say the action is rejected, and it does not say what happens when the re-evaluation produces no decision. #1196 already owns a testing discussion of `9.5.6`. Jim Manico wrote on 2026-11-08 that `9.5.6` itself should not change. This proposal leaves that row alone.

## Proposed requirement

`ISSUE.md` is the text to paste. The requirement is:

> **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2.

Wording choices, if you are asked:

- "Defined timeout" matches `9.6.2` ("defined approval time"). The audit draft said "documented timeout". Both are testable. "Defined" is the word the chapter already uses.
- A decision, explained in the issue and not stuffed into the row, is an allow, a deny, or a referral to the C9.2 human-approval gate. An error, an empty body, a dropped connection, and silence are not decisions. Putting "allow or deny" into the row would also treat an approval referral as a failure, which collides with `9.2.1` and `9.6.2`.
- The old `9.7.4` also required a log entry. `CONTRIBUTING.md` says a control that bundles two tests should be split. The log is omitted on purpose. `12.1.2` logs safety-filtering and policy decisions for content moderation. It does not require a record of a missing agent-authorization decision. If a leader wants that record, it is a second issue.
- `9.5.8` is the next unused id in C9.5. `9.5.7` is the last row in `1.01` and `1.02-dev`. A repository search on 2026-11-18 found no `9.5.8` and no remaining `9.7.4`. Reusing `9.7.4` would reopen a removed section and reuse a retired identifier. `RELEASE.md` forbids both in a minor release.
- The Appendix B line is inventory only. Appendix B says it adds no requirements and that every active requirement appears once. The patch adds that one line under AD.2.

The patch does not edit the glossary. The glossary sentence also covers safety components. `9.5.8` supports the authorization half for this one failure. It does not make the sentence true for every safety component. A glossary edit would be a second change. If the leaders reject the row, the honest follow-up is to narrow that sentence. That follow-up is not part of this filing.

## Why the gap matters

An agent runtime that calls a policy engine and proceeds when the call times out still matches `9.5.1`, `9.5.3`, and `5.2.5` on the path where the engine answers. Anyone who can delay or drop that call, and any outage of the engine, then gets the tool call with no allow and no deny. The glossary tells an adopter the standard already forbids that result.

The concrete pair is in the issue. With a 200 ms timeout and a stub that accepts the connection and never answers, a compliant runtime has not invoked the tool when the timeout fires, and the synthetic resource is unchanged. A noncompliant runtime invokes the tool and the resource changes. Closing the connection, or returning an error that is not an allow, a deny, or an approval referral, has the same split.

## Level and release rules

Level 2 is the right slot for four reasons you can say out loud.

1. Rico Komenda said Level 2 was appropriate, and #683 merged it there. #928 repeated Level 2 on the day the row was deleted.
2. The decision point this row depends on is introduced at Level 2 by `9.5.1` and `5.2.5`. #928 called per-parameter policy integration production engineering, above the Level 1 bar. A timeout around that call belongs with it.
3. `9.6.2` is the same shape, timeout then block, and it is Level 2.
4. Level 3 would leave a Level 2 system free to treat silence as allow. That is the failure the row exists to close.

What an adopter does: keep the existing per-action policy call, give it a defined timeout, and block the action when no decision arrives. Blocking earlier on a hard error is fine. Waiting forever is not, because then there is no defined timeout at which the action is blocked. NIST SP 800-207 §5.1 is the security property: no approval, no communication. §5.2 is the availability property: replicate the policy service so an outage does not have to become an allow. Envoy's external-authorization filter is a working example of the default. `failure_mode_allow` defaults to false, so a communication failure or an HTTP 5xx denies the request. The default timeout on that filter is 200 ms. None of that is a requirement to use Envoy.

This packet does not claim that LangGraph, the OpenAI Agents SDK, or any other agent framework already does this. #725 is the caution against that claim: a leader will ask, and an unchecked "frameworks support this" sentence is how a Level 2 row gets pushed to Level 3 or closed.

## Submission instructions

Do this only after you approve this exact issue text.

1. Re-read `1.02-dev/en/0x10-C09-Orchestration-and-Agentic-Action.md` on `main` if `main` has moved past `092232f`. Confirm `9.5.7` is still the last C9.5 row and that `9.5.8` is still unused. On 2026-11-18, `main` was still `092232f`.
2. Open one issue: <https://github.com/OWASP/AISVS/issues/new>
3. Title: `[1.02] C9.5: block the agent action when its policy decision point returns no decision`
4. Body: paste `ISSUE.md` unchanged. It is the whole issue.
5. Apply the `1.02` label if the issue form lets you. The label's description is "Active release: work targets 1.02-dev; proposals require review before inclusion."
6. Stop. `CONTRIBUTING.md` says a non-maintainer opens an issue before a pull request. `AGENTS.md` says the same. Wait for a leader to ask for a pull request.
7. Do not open a pull request, do not push the patch, and do not comment the patch onto the issue unless a leader asks for the text. If they ask, the patch is `contributions/T001-AISVS/9.5.8.patch`. It applies to `1.02-dev/` at `092232f`. It was checked locally against the C9 and Appendix B files from that commit, and both hunks applied. It must not be applied to `1.0/` or `1.01/`. If #1227 or any other change to those two files has merged, regenerate the patch against current `main` before sending it. The requirement sentence stays the same.
8. Do not mail jim@owasp.org. `SECURITY.md` is for vulnerabilities. A missing requirement is an issue.
9. Do not attach the queued-action procedure, the three evidence claims, or the approval-gate variant from #1196. Do not propose a change to `9.5.6`. Do not ask to recreate `/research`.

## AI-assistance disclosure

Read on 2026-11-18 from `CONTRIBUTING.md`, section "AI-Assisted Contributions", and from `AGENTS.md`.

AI assistance is allowed, including for drafting an issue. The project does not require a disclosure banner, a model name, or a generated-by line. What it requires is that you can defend every sentence and that the control is concrete and testable. On 2026-11-17 and 2026-11-18 the maintainers closed #1215 and #1216 because long generated discussion was not readable. They asked for a concise human restart.

So: no disclosure paragraph in the issue. If you want to say you used a tool, one sentence in a comment is enough, and it is not what the policy demands. Do not add background sections, a second proposal, or a restatement of the diff. If a reviewer asks you to explain a sentence and you cannot, delete that sentence before you file.

`MODELS.md` describes a maintainer review lineup that would require paid inference. It was not run.

## What this packet does not do

- It does not file the issue or the patch.
- It does not take #1226, #1220, #1217, #1195, #1187, or #1122.
- It does not reopen #1196, and it does not restore the denial and still-valid-token predicates that #934 removed from what is now `9.5.6`.
- It does not restore `10.6.1`, the end-user-credential parenthetical, or section C9.7.
- It does not change the glossary.

## Not verified

- Slack, maintainer meetings, and any discussion outside GitHub. #934 has no written reason, so intent for this one predicate is inferred from the absence of a reason plus the same-day levels review. That is not a quote of intent.
- Agent-framework defaults. No framework was executed.
- The OWASP AI Testing Guide, beyond the pointer in Using AISVS.
- Any commit on `main` after this check. The last push observed on 2026-11-18 was `092232f` on 2026-11-11.
- Page layout of the NIST PDF. The §5.1 and §5.2 citations were checked against the table of contents and the section text in the public NIST SP 800-207 record at <https://doi.org/10.6028/NIST.SP.800-207>. The sentences used are in those sections.

## Local tracker

`MASTER_TRACKER.md` records this packet as C-001, provisional label T001, status `in-review`. Submission and acceptance are `none`. Filing still requires your approval of `ISSUE.md`.
