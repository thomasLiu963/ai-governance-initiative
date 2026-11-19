# Technical rationale

## The correction

In `#LEAST MODEL PRIVILEGE`, the Limitations paragraph currently ends:

> Per-action evaluation adds latency; policy engine outage requires an explicit fail-closed vs fail-open choice.

The patch replaces that clause with:

> Per-action evaluation adds latency; if the policy engine is unreachable, deny the action.

The implementation bullet is left as published:

> **Fail closed** if the policy engine is unreachable.

After the patch, the bullet and the Limitations paragraph name the same event and the same outcome. Deny means the enforcement point does not let that action proceed. It matches "permit/deny" and "default to **deny**" already in the same block.

## What was verified

Source: OWASP AI Exchange, repository `OWASP/www-project-ai-security-and-privacy-guide`, commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441`, committed 2026-11-16. That commit was `main` when this packet was checked on 2026-11-18. The page is community guidance, published at https://owaspai.org/go/leastmodelprivilege. The file is `content/ai_exchange/content/docs/1_general_controls.md`. On that commit the implementation sentence is line 747 and the Limitations sentence is line 760.

The phrase "fail-open" occurs once in the repository, in line 760. "Fail closed" in this control occurs in line 747. A GitHub issue search for `fail-open` on 2026-11-18 returned no issues and no pull requests.

History of the two sentences:

| Event | What it did to these sentences |
| --- | --- |
| `693d59d6f7` (2026-08-03), "Integrate agentic Section 12.4 multi-agent system security", on the branch merged by pull request [185](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/pull/185) | Added both sentences in one diff, inside the new agentic authorisation block. Author: Spyros Gasteratos (`northdpole`). |
| Merge `c3562e82` (2026-08-03) | Brought that block to `main`. Rob van der Veer's merge comment says the pull request had been under review and that he would tweak the result afterwards. The review thread does not discuss fail-open or fail-closed. |
| `e6679119` (2026-08-24), "switching to /go/ permalinks without trailing slashes" | Blame attributes line 760 to this commit because a permalink on that line lost its trailing slash. The fail-open clause is unchanged across the diff. |
| `f8dda544` (2026-11-15), pull request 275, a typo pass | Blame gives this commit the email-example line (764), not line 747 or line 760. |

The merge commit records `Co-authored-by: Cursor`. That trailer does not identify which sentences an assistant wrote. This packet does not treat the contradiction as an assistant error. It treats it as two published instructions.

Nearby work that is not this gap, and is not to be commented on or resubmitted:

- Issue 188 item 9 asks `#MONITOR USE` and `#OVERSIGHT` to halt consequential execution when detection, containment, and audit are jointly degraded. That is a different rule, and the issue is already open with the agentic workstream.
- Issue 222 proposes fail-closed retrieval for agent memory. Different control, already open.
- `#MODEL ACCESS CONTROL` revokes credentials and sessions. It does not say what an unreachable policy engine does.

## It is not a recorded distinction

A deliberate distinction would be a second rule with a stated boundary: for example, fail closed for state-changing actions, and an explicit documented exception for one named read. The page does not say that.

What the page does say, in the same block, is:

- Deny-by-default. Agents hold no permissions unless explicitly granted.
- Synchronous gate: no action proceeds until permit or deny returns.
- Fail closed if the policy engine is unreachable.
- When policy precedence is unresolved, default to deny.
- Read versus write shows up elsewhere as a privilege reduction: separate credentials, and narrower permissions when untrusted content arrives. Those bullets assume a decision can be made. They do not say a read may proceed when the engine is unreachable.

The Limitations paragraph is where this control lists residuals and costs: harm inside a granted scope, prompt injection before delegation, structurally valid delegation tokens, revocation-latency tolerance, and evaluation latency. Revocation-latency tolerance is a residual the sentence accepts in words. The fail-open clause is different. It instructs the reader to choose a mode, and one of the two modes reverses the implementation bullet. Nothing in pull request 185, and nothing in a later commit, says that reversal was intentional.

The grammatical neighbour is easy to over-read. "Explicit revocation-latency tolerance" and "explicit fail-closed vs fail-open choice" share the word "explicit." Sharing that word does not give fail-open a scope. The tolerance sentence says which residual is accepted. The choice sentence does not say which actions, if any, may fail open.

So the apparent contradiction is an unreconciled pair, not a distinction to preserve.

## Why this clause, and not a larger edit

Three larger edits were considered and not used.

**Delete the choice and leave the Limitations paragraph silent on outages.** That removes the contradiction. It also removes the only Limitations words about the outage, so a later reader can treat the deletion as "outage behaviour was left to the implementer." The paragraph that used to discuss the outage should state the rule the implementation bullet already states.

**Allow fail-open for a named read-only action, recorded as residual risk.** That would be new guidance. The history does not support it. A read during an outage is still data access the engine did not decide. The email example under this paragraph limits a summarizer to read-only so it cannot send mail. It does not authorise the read when the engine is down. Adding a read exception would also cut against the property the sibling AISVS draft is being asked to restore: when the decision does not arrive, block the action. See the coordination note below. A general residual-risk step does exist in the Exchange overview ("Residual risk acceptance"). This patch does not link to it. A link from this sentence would put the choice back inside the control.

**Rename "unreachable" to "does not return a decision within a timeout."** That closes a real further hole: a peer that accepts the connection and never answers. It is a second change, it edits the sentence that is already the rule, and it is the shape of a verification requirement rather than of this wording fix. It is recorded as out of scope in `examples.md`, example 4.

The patch therefore changes one clause. It keeps British spelling and the existing semicolon. It does not add a control identifier, a permalink, a hall-of-fame row, or a tool name.

## Coordination with the AISVS proposal

The AISVS candidate C-001 (`contributions/T001-AISVS/ISSUE.md`) asks for one new Level 2 row:

> **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2.

That requirement was merged in April 2026 as `9.7.4` and removed in the June 2026 condensation, while the AISVS glossary still says authorisation components fail closed. AISVS is a verification standard. A missing row is restored by an issue against `1.02-dev`, with an identifier, a level, and a "verify that" sentence.

This packet does not copy that proposal.

| | AISVS candidate | This Exchange patch |
| --- | --- | --- |
| Document | Draft verification standard | Community guidance, prose under an existing control |
| Defect | The requirement table no longer contains a rule the glossary still states | Two sentences in the same control contradict each other |
| Form | New requirement ID, Level 2, testable predicate, timeout | One clause, no ID, no level, no test procedure |
| Trigger | No decision within the defined timeout | The word the Exchange already uses: unreachable |
| Outcome | Block the action | Deny the action |

The shared property is the one worth keeping aligned: if the authorisation decision does not arrive, the action does not proceed. The Exchange already says that in the implementation bullet. The submission should stand on the Exchange text alone. It should not cite AISVS, the glossary sentence, or an unfiled requirement ID. Those belong to the other project's issue, if that issue is later approved.

## What an adopter has to do

A deployment that already denies the action when the policy engine is unreachable does nothing. A deployment that proceeds, and that cites the Limitations sentence, stops doing so for every action this control already puts through the engine: tool calls, data access, inter-agent messages, and outbound communication. The gate is the enforcement point outside the agent, which the same section already requires. This patch does not design that gate.

## Contribution process

- `CONTRIBUTING.md`: small clarifications may be a pull request without an issue. https://github.com/OWASP/www-project-ai-security-and-privacy-guide/blob/c68371ed56051a3d7c894e36c20c3bcbc22eb441/CONTRIBUTING.md
- The contribute page, also stored as `content/ai_exchange/content/contribute.md`, heading "Label AI use": anyone submitting work to OWASP that used material AI assistance must say that AI was used, what it was used for, and to what extent. https://owaspai.org/contribute/
- The pull-request body in `pull-request.md` carries that disclosure. A commit trailer alone is not the disclosure. Pull request 187 was merged with a trailer and without the fuller statement. The written rule still asks for the fuller statement, so this body includes it.
- Commercial promotion is out. Nothing affiliated is linked.
- Fork preview checks stay at `action_required` until a maintainer allows them. That was the case on pull request 187. A red preview check is not a review.

## Not verified

- `main` after `c68371ed`. Re-read line 760 before opening the pull request.
- Private Slack, the authors group, and the agentic workstream. No public issue owns this sentence. That is not proof that nobody has discussed it off GitHub.
- Whether any particular product fails open on this path. No runtime was built, and no model API was called.
- ISO/IEC 27002 control 8.2, which this control's references say covers least privilege. That standard was not re-read. The patch does not depend on it.
- The live HTML page was not clicked. The sentence was read from the file at `c68371ed`.
