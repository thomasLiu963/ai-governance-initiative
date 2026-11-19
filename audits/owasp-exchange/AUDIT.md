# OWASP AI Exchange — technical audit

**Decision.** Prepare three narrow edits. Do not open a new control family, and do not take over work that already has an author. If one external submission is approved before 30 November 2026, send only the fail-closed correction. The other two are internal-review drafts for a December submission, with a realistic decision window before 15 February 2027.

**Rank, for substance, maintainer behaviour, time, review path, and institutional fit:**

1. **OX-1 — Show the untrusted input behind a human approval.** Highest substance. Fits the oversight edits this project already merges.
2. **OX-2 — Remove the fail-closed / fail-open contradiction.** Smallest change and the only one with a same-week review path.
3. **OX-3 — Re-check authority when a deferred or staged action fires.** Real authorization gap, slowest path, because a broader version has sat with the agentic workstream since August 2026.

Local research tracks `research/D1/`, `research/D2/`, and `research/incident-evidence/` are not in this workspace. None of the three candidates is supported by those files.

## What was read

| Item | Status | Locator |
| --- | --- | --- |
| Repository `main` | Living community guidance. Commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441`, committed 2026-11-16. | https://github.com/OWASP/www-project-ai-security-and-privacy-guide |
| Project page | Says flagship documentation, "Version 1.0". The repository itself is updated continuously. | `info.md`, `index.md` in that commit |
| Contribution rules | Read. | `CONTRIBUTING.md`; `content/ai_exchange/content/contribute.md`; https://owaspai.org/contribute/ |
| AI-assistance rule | Read. "Label AI use" on the contribute page. | Same contribute source |
| Controls and threats | Read on that commit: overview, general controls, threats through use, runtime threats, testing, privacy. | `content/ai_exchange/content/docs/` |
| Issues and pull requests | 29 open issues, none with a `help-wanted` label and none with an assignee. Pull-request sample below. | GitHub issue and pull-request APIs, 2026-11-18 |
| Site | https://owaspai.org/ is the published rendering of this repository. This audit used source and `firebase.json` redirects, not a full click-through of the live site. | |

This is **community guidance**, not a de jure standard. The project's own pages say the material feeds ISO/IEC work and the EU AI Act. Those partnerships were not independently checked.

The published roadmap still says "Priority content workstreams to deliver major update before summer 2026" (`ai_security_overview.md`, permalink https://owaspai.org/go/roadmap). That date has passed. Agentic controls, testing, and privacy edits have continued since. The stale date is context, not a proposed contribution.

## Rules that govern a contribution

`CONTRIBUTING.md` sends people to https://owaspai.org/contribute/ and says small clarifications and doc fixes may be pull requests without an issue. The contribute page also offers an issue, a direct edit, or the authors group (a closed Slack). External contributors are merged without that group. See OX-1's comparison case, pull request 235.

Writing rule that matters here: a non-specialist should get the point, in as few words as the point allows. Pull request 192 was praised and also called slightly too detailed to maintain. Issue 244 drew an explicit request for plainer language and a clearer statement of what the current text fails to cover.

**AI assistance.** Anyone submitting work to OWASP that used material AI assistance must say that AI was used, what it was used for, and to what extent. Commercial promotion is out. A tool or article the author is affiliated with must be disclosed. Pull request 181 was closed on 2026-07-26 because a single tool does not get a listing without a fair selection procedure.

## Pull request 187

https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/187

| Field | Record |
| --- | --- |
| Title | Add AI engineering primer for security professionals |
| Author | `3nesdeniz` (Enes Deniz). Association on the comments: `CONTRIBUTOR`. |
| Opened | 2026-07-14 |
| First maintainer response | 2026-07-26, Rob van der Veer (`COLLABORATOR`), in the merge comment. No earlier maintainer comment and no review object before merge. |
| Merged | 2026-07-26, merge commit `601d67e8eb02e1bcde58df5edc436aa41edd1570`. Closes issue 182. |
| Size | +48 / −0 across 3 files. |
| AI disclosure | Commit `7918235d` has `Co-authored-by: OpenAI Codex <codex@openai.com>`. The pull-request body does not state what the assistant did or how much of the text it wrote. The written policy asks for both. The commit trailer was enough for this merge. |
| What the maintainer said | "this is solid work. Approved and merged! I wil tweak some of the content shortly but that's just details." |
| Process fact | The author twice asked for approval of a GitHub Actions preview that was stuck at `action_required`. Fork previews do not run until a maintainer allows them. |

The primer is now in `ai_security_overview.md` under "AI engineering primer for security professionals" (https://owaspai.org/go/aiengineeringprimer). It maps delivery models and lifecycle artifacts to existing controls. It does not add the safeguards below.

## How review actually behaves

Dates are from the GitHub API. "First maintainer response" means the first comment or review by `robvanderveer`. Role is the association shown on that interaction, not an inferred title. Collaborator permission for `wolfspace099` returned HTTP 403, so that account is described only as a frequent author of editorial pull requests.

| PR | Opened | First maintainer response | Merged or closed | Author | What it shows |
| --- | --- | --- | --- | --- | --- |
| [192](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/192) | 2026-08-03 12:56Z | 2026-08-03 12:59Z, merge comment | Merged 2026-08-03 12:59Z | `fevziegeyurtsevenler` | Issue 191, "excellent! make it so", then a docs-only pull request merged in about three minutes. Later review comments on 14–20 August did not revert it. |
| [225](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/225) | 2026-09-29 | Approval 2026-09-30 06:28Z | Merged the same minute | `ninadphalak` | A few lines on streamed-output filtering. About 14 hours. |
| [235](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/235) | 2026-10-12 | Non-maintainer thanks 2026-10-15; Rob approved 2026-10-28 | Merged 2026-10-28 | `Dimchik1990` | One `#OVERSIGHT` paragraph (staged commit). Sixteen days. The pattern OX-1 should copy. |
| [213](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/213) | 2026-08-28 | 2026-08-31 | Merged 2026-09-27 | `vishnu-77`, `CONTRIBUTOR` | Testing methodology accepted only after the executable tester was moved to an external repository. About 30 days. |
| [210](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/210) | 2026-08-21 | Merge comment the same morning | Merged 2026-08-21 | `onurcangnc` | Large RAG overview, same-day merge. Rob called the fit with the existing reference frame the reason. Not a typical wait. |
| [187](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/187) | 2026-07-14 | 2026-07-26 | Merged 2026-07-26 | `3nesdeniz`, `CONTRIBUTOR` | Twelve days, one maintainer comment, at merge. |
| [181](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/181) | 2026-06-15 | 2026-06-16, "under review of the Red teaming group" | Closed unmerged 2026-07-26 | `eeee2345` | Rejected as a single-tool listing. Forwarded to the red-team roadmap. About 41 days. |
| [189](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/189) | 2026-07-21 | None | Closed 2026-07-26 by author `BlainerIP` | `BlainerIP` | Not a maintainer rejection. No review text. Reason for the author's close is not in the record. |
| [247](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/247) | 2026-10-28 | Same day: "deserves review by the redteaming work stream" | Still open on 2026-11-18 | `AUTHENSOR` | Testing additions are routed to a workstream and then wait. |
| [216](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/216) | 2026-09-03 | None in the pull-request comments | Still open on 2026-11-18 | `deepango` | "Named vs enforceable" text for issue 202. No review after eleven weeks. |

Among the 80 most recently closed pull requests, the unmerged ones were mostly empty or superseded by the same author (`250`, `203`, `173`, `158`, `154`, `152`), plus `181` and author-closed `189`. That sample is too small, and too skewed toward merged editorial work, to estimate an acceptance rate. The open queue is the relevant caution: substantive drafts from August and September are still open.

## Already covered, so not proposed again

The 2026 agentic expansion already states, in `1_general_controls.md` and `2_threats_through_use.md`:

- Human and automated `#OVERSIGHT`, including approval tokens bound to parameters and expiry, a kill switch the agent cannot operate, a static capability manifest, and a ban on agent-written consent text.
- Staged commit (pull request 235): the reviewer sees the pending object, and the agent should not hold the commit permission.
- `#LEAST MODEL PRIVILEGE`: deny-by-default, task-bound tokens, delegation-chain checks, scope non-expansion, and re-authorization when scope grows.
- `#MODEL ACCESS CONTROL`: real-time credential revocation and session invalidation on revocation.
- `#PROMPT INJECTION I/O HANDLING`: locale-independent case-folding and Unicode confusable skeletons. Issue 191 is still open, but pull request 192 merged that text on 2026-08-03. Do not resubmit it.
- Hidden instructions in text, images, and tool output, including the indirect-injection examples.
- Retrieval-time permission revocation as a RAG test (`5_testing.md`).

Issue 188 (opened 2026-07-17 by `apeiris-ai`) asked for ten new or extended controls, including confused deputy, approval-object binding, and deferred-action authority. Rob van der Veer replied on 2026-08-03 that it was with the agentic workstream, then "between iterations." Much of that list is now in the pages above. The issue is still open, unassigned, and has no pull request. The last comment is 2026-08-21. OX-3 is only the residual, not that catalogue.

## Do not take these

- **Issue 244** (`kiranyenaganti9`, 2026-10-25). Asks `#OVERSIGHT` to separate "the tool accepted the call" from "the effect happened." Rob asked the same day for a plainer account of what is missing. `CSOAI-ORG` answered on 2026-11-06. No maintainer reply and no Exchange pull request as of 2026-11-18. Occupied.
- **Issue 191 / pull request 192.** Already merged. See above.
- **Pull request 276** (`3nesdeniz`, opened 2026-11-15). Already corrects the `/go/disclosureuseoutput` redirect, which currently points at `#231-disclosure-of-sensitive-data-in-output` while the heading is "in model output."
- **Issues 177, 202, 216, 222, 246, 247.** Provenance receipts, enforceability labels, and memory-integrity or evaluation-integrity testing. Each has an author. None is the gap below.

## OX-1 — The approval screen hides the instruction that caused the action

**1. Gap.** `#OVERSIGHT`, human-oversight implementation, `content/ai_exchange/content/docs/1_general_controls.md`, permalink https://owaspai.org/go/oversight.

The review interface must show "the action requested, stated rationale, relevant prior actions in the session, estimated impact, and reversibility classification." It must sanitize urgency framing. It does not require the untrusted input that led to the proposal: the retrieved passage, tool output, or agent message, taken from the system trace rather than from the model's summary.

Two nearby sentences do not close this. Automated "deceptive reasoning" checks compare stated intent with tool calls. A hidden instruction that produces a matching rationale and a matching call passes that check. Staged commit shows the object that will be sent or merged. It does not show why the agent drafted it. `#MONITOR USE` tells operators to log retrieval IDs and hashes rather than chunk text, so the audit log is also not the approval screen.

**2. Not already owned.** Issue search for the review-interface field list and for "stated rationale" found no matching issue or pull request. Issue 244 is about completion versus acknowledgement. Issue 188 item 6 is about binding approval to the action digest, which the approval-token paragraph now does. No assignee on either.

**3. Consequence.** A person can approve a payment, email, or merge while the only explanation on screen was written by the same model that followed a hidden instruction. The human oversight gate then ratifies the manipulation. Sanitizing urgency words does not reveal the cause.

**4. Change.** One short paragraph under human oversight, plus one sentence in the testing bullet at `5_testing.md` §5.3.2 ("Human oversight as a social surface"). Require the approval screen to include the recorded untrusted inputs that preceded the proposal, or a source link resolved at review time, bounded and labelled as untrusted. Do not copy those bodies into the long-term retrieval log. The agent's stated rationale stays on screen and is labelled as model output.

**5. D1/D2 or incident files.** None locally. The Exchange already uses its own examples of hidden instructions (white-on-white text in a job application; instructions in a retrieved page). This audit did not re-investigate those external write-ups. They show hidden instructions changing model behaviour. They are not a recorded case of a human approver being the deceived party.

**6. Experiment.** No model experiment and no paid API. The gap is a missing required field. The smallest check is a local fixture of two packets for one proposed action: packet A has only today's required fields; packet B adds the retrieved text that contains the instruction. A reviewer of packet A cannot see the instruction. That fixture is for internal review, not a prerequisite for the wording.

**7. Effort and cost.** About one day to draft in the Exchange's plain style, including the testing sentence. No API cost. An adopter must change the approval UI and keep chunk text out of retained logs.

**8. Route and policy.** Open a short issue, then a docs-only pull request, in the style of pull request 235. State AI use and extent in the issue and the pull request, not only a commit trailer. No new control name. Do not attach an external product.

**9. Dates.** 30 November 2026: sourced draft ready for internal review. An external merge by that date is not a reasonable expectation; pull request 235 took sixteen days after it was opened, and only after it reached Rob. 15 February 2027: a merge is realistic if the text is short, plain, and submitted in December, and if it is not diverted to the red-team queue. The testing sentence should stay one sentence so it travels with the control edit. A new testing section would join pull request 247 in that queue.

**10. Accurate accomplishment, only after a merge.** The Exchange's human-oversight control required the approval screen to show the recorded untrusted inputs behind a proposed action, not only the agent's stated rationale.

**11. Evidence to keep.** The issue, the pull request, the merge commit, and the rendered permalink https://owaspai.org/go/oversight quoting the new sentence. Until then, evidence is this file plus commit `c68371ed`.

**Themes.** Human oversight, human agency, transparency.

## OX-2 — Fail closed and fail open are both instructed

**1. Gap.** `#LEAST MODEL PRIVILEGE`, `content/ai_exchange/content/docs/1_general_controls.md`, permalink https://owaspai.org/go/leastmodelprivilege.

Runtime policy validation says: "Fail closed if the policy engine is unreachable." The limitations paragraph says: "policy engine outage requires an explicit fail-closed vs fail-open choice."

**2. Not already owned.** Issue 188 item 9 is a different rule (halt when detection, containment, and audit are jointly degraded). Issue 222 is fail-closed retrieval for memory. No issue or pull request states this contradiction. Confirmed by reading both sentences on commit `c68371ed` and by searching issues for "fail closed" and "fail-open."

**3. Consequence.** An implementer can fail open on an unreachable policy engine and point at the limitations sentence, while another team fails closed and points at the implementation sentence. For an agent that can change state, fail open means the authorization gate is absent exactly when it cannot be evaluated.

**4. Change.** Keep one rule. State-changing actions, outbound communication, and any action that crosses a trust boundary are denied when the policy engine does not return a decision. A fail-open exception has to be a named, documented residual risk for a named read-only action, not a free choice. Delete the sentence that presents the choice as open.

**5. D1/D2 or incident files.** None. Not required. The two sentences are the evidence.

**6. Experiment.** None. No API.

**7. Effort and cost.** About two hours. No API cost. Adopters who already fail closed change nothing. Adopters who fail open must either stop doing so for state-changing actions or record the exception as accepted residual risk.

**8. Route and policy.** `CONTRIBUTING.md` allows this as a pull request without an issue. That matches pull requests 192 and 225. Disclose AI assistance in the pull-request body: what was used and how much. This is the candidate to send first if external submission is approved.

**9. Dates.** 30 November 2026: the text can be internally ready within a day. An external decision by 30 November is possible and not promised. Pull request 225 was approved in about fourteen hours; pull request 216 has had no review in eleven weeks. Same-day merges are concentrated on very small, plain diffs that Rob looks at. 15 February 2027: if it is submitted in November or December and is still this small, a decision before February is the normal case, not the optimistic case.

**10. Accurate accomplishment, only after a merge.** The Exchange no longer tells implementers both to fail closed and to choose fail open when the agent policy engine is unreachable. State-changing actions fail closed.

**11. Evidence to keep.** Pull request, merge commit, and the two edited sentences at https://owaspai.org/go/leastmodelprivilege.

**Themes.** Authorization, AI reliability.

## OX-3 — A revoked principal can still release a staged or deferred action

**1. Gap.** Split across three places on commit `c68371ed`:

- `#OVERSIGHT` staged commit (https://owaspai.org/go/oversight). The pending email, pull request, or payment batch is left for a later commit. Nothing says to cancel or freeze that object when the human principal's role, account, or consent ends, or when the task is cancelled.
- `#OVERSIGHT` user-facing disclosure. "Genuine opt-out mid-task" is required. It is not tied to descendant tokens or pending objects.
- `#LEAST MODEL PRIVILEGE` (https://owaspai.org/go/leastmodelprivilege). Delegation tokens expire and must be re-issued when scope changes. The limitations paragraph accepts "revocation-latency tolerance." It does not require a use-time check that the human principal is still authorized, including for an action that was queued earlier.
- Privacy §7.8, `6_privacy.md` (https://owaspai.org/go/aiprivacy). Consent withdrawal deletes associated data and retrains the model. It does not stop an agent already acting under that consent.

`#MODEL ACCESS CONTROL` does revoke agent credentials and invalidate the session. That stops a live session. It does not say what happens to an object already staged in another system, or to a job that will fire after the session is gone.

**2. Not already owned.** Issue 188 item 7 asked for fire-time re-authorization of deferred actions on 2026-07-17. Rob sent the whole ten-item list to the agentic workstream on 2026-08-03. There is no assignee and no pull request. Pull request 235 later added staged commit and did not add the revocation check. A new control ID, or a resubmission of the ten-item list, would collide with that issue. A paragraph that only closes the residual does not.

**3. Consequence.** Someone can lose the right to send a payment or merge a change, while a draft they, or their agent, already created remains releasable by a scheduler, a teammate's commit right, or a still-unexpired delegation token. Opt-out and consent withdrawal have the same hole. Short token lifetime limits the window. It does not cover a pending object that is not a token.

**4. Change.** Two short additions, no new control name.

- Under staged commit and delegation: before a deferred or staged action is released, check that the human principal's authorization still covers that action. If the role, account, consent, or task grant has ended, freeze or cancel the pending object and reject descendant tokens. Do this at the system that holds the object, not by asking the agent.
- Under privacy consent withdrawal and under mid-task opt-out: name those events as the same revocation. One cross-link each. Do not expand the privacy page into an agentic design chapter.

**5. D1/D2 or incident files.** None locally. Do not cite the unsanitized enterprise anecdotes in the issue 177 and 188 threads. Those comments describe private incidents this audit has not seen.

**6. Experiment.** No model API. The smallest check is a state trace on paper or in a local script: at T0 the principal may stage a payment batch; at T1 the principal's role is removed; at T2 the batch is still releasable under the current sentences. That demonstrates the missing obligation. It is not a product test. Build it only if internal review wants a figure. The missing sentences are already the evidence.

**7. Effort and cost.** About one day for the two paragraphs and the cross-links. No API cost. Adopters must re-check the principal at release time and must be able to cancel pending objects. That is an integration change, which is why the Exchange text should stay a requirement and not a design for each target system.

**8. Route and policy.** Comment on issue 188 with the residual wording and the note that pull request 235 did not close item 7. Ask whether the workstream wants that paragraph. Do not open a parallel control catalogue and do not import apeiris.ai text. Disclose AI assistance. If there is no maintainer answer by early January 2027, a docs-only pull request that only edits the staged-commit and delegation paragraphs is still in bounds, and the pull request should link issue 188.

**9. Dates.** 30 November 2026: the comment text can be ready for internal review. An external merge by then is unlikely. The workstream has not answered since August, and a comment is not a merge. 15 February 2027: a merge is possible if the workstream treats the residual as a small edit in the pull-request 235 pattern. It is equally possible that the comment waits out the winter. Do not count this one as a February acceptance.

**10. Accurate accomplishment, only after a merge.** The Exchange required a fresh check of the human principal's authority before a staged or deferred agent action is released, and treated consent withdrawal and mid-task opt-out as that revocation.

**11. Evidence to keep.** The issue 188 comment, any pull request, the merge commit, and the sentences at https://owaspai.org/go/oversight and https://owaspai.org/go/leastmodelprivilege.

**Themes.** Authorization, human agency, human oversight.

## Recommendation

Write all three drafts in `audits/owasp-exchange/` only after this audit is accepted for drafting. Do not submit, and do not comment on issue 188, until that approval is explicit.

Order of external action, once approved:

1. **OX-2**, pull request, no issue. It is the inconsistency with a real chance of review before 30 November and a boring path to a decision before 15 February.
2. **OX-1**, issue then pull request, in December. This is the contribution worth the project's time. Keep it shorter than pull request 192 and as plain as Rob asked in issue 244.
3. **OX-3**, comment on issue 188 first. Escalate to a pull request only if the workstream does not take the residual.

Skip anything that adds a control identifier, a tool listing, a taxonomy, or an enforceability scale. Those are the submissions that are either still open after months or were closed for scope.

## Not verified

- The live site was not clicked through. Redirect targets were read from `firebase.json` on this commit.
- ISO/IEC 42001, 27002, and the EU AI Act were not re-read. Gap notes inside the Exchange that cite them were left as the project's claims.
- No claim is made about who will merge a future pull request, or about a probability of acceptance.
- Private Slack, the authors group, and the agentic and red-team workstreams are not visible here. "No public assignee" is not "nobody is working on it" beyond the public issue and pull-request record.
- `wolfspace099`'s repository role is not visible without push access.
- Pull request 189's author closed it. Why was not recorded.
- External incident articles cited by the Exchange were not re-fetched for this audit.
- D1, D2, and the incident-evidence directory are absent, not empty-with-negative-results.
