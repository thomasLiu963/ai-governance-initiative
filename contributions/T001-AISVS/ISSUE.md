Target: `1.02-dev` only. Released `1.0/` and `1.01/` stay locked.

This asks to restore a failure behavior the project already accepted. It was merged in #683 and removed when #934 rewrote the chapter. I am not proposing it as a requirement I originated.

## Missing requirement

No current requirement says what the runtime does when the policy decision point for an agent action does not return a decision.

`9.5.1` requires agent actions to be authorized against a runtime policy that limits tools and parameter values. `9.5.3` requires application logic or a policy engine, not the model, to enforce access-control decisions. `5.2.5` isolates that decision point from the agent. `9.6.2` blocks an action when a human-approval gate is not satisfied within the defined approval time. A runtime can satisfy each of those and still invoke the tool when the authorization call returns no decision.

Appendix A still says: "AISVS requires AI components with safety or authorization responsibilities to fail closed."

## History

#676 separated a returned denial from no decision at all. On 2026-04-11 Rico Komenda wrote: "The gap is real. ... No existing control explicitly requires fail-closed behavior on PDP timeout or network partition. ... Level 2 is appropriate." #683 merged the control on 2026-04-13.

At `19e6410889` (merge of #928, 2026-06-15 11:16 UTC), `1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md` still contained:

> **9.7.4** Verify that when the policy decision point (PDP) used for governance evaluation is unavailable (e.g., timeout, network partition, service failure), agent execution fails closed by blocking the proposed action, and the unavailability event is logged with sufficient detail for incident investigation. Level 2.

#928's levels table kept "C9.7.4 | L2 | Fail-closed when PDP unavailable." #934 merged later that day with an empty body and no review. It replaced the chapter and deleted `9.7.4` with the rest of C9.7. No comment on that pull request says this predicate was rejected. No later issue restores it.

## Proposed wording

Append one Level 2 row. Leave C9.7 retired. Do not reuse `9.7.4`. Leave the logging clause out.

> **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2.

A decision is an allow, a deny, or a referral to the C9.2 approval gate. An error, an empty result, a dropped connection, and silence are not decisions. On `main` at `092232f` (re-read 2026-11-18), `9.5.7` is the last C9.5 row and `9.5.8` is unused. Open pull request #1227 adds C9.3 skill rows and does not take `9.5.8`.

Appendix B lists active requirements and adds none of its own. The matching line would be: "Runtime blocks an agent action when its policy decision point does not return a decision within the defined timeout | C9.5.8".

I will not open a pull request unless a maintainer asks for one.

## Example

The defined timeout is 200 ms. The tool call would modify a synthetic resource.

Compliant: a stub accepts the decision request and returns nothing. At 200 ms the tool has not run, and the resource is unchanged. The same block holds when the stub closes the connection or returns an error that is not an allow, a deny, or an approval referral.

Noncompliant: the timeout fires, the runtime invokes the tool, and the resource changes. Treating a closed connection or a non-decision error as permission is the same failure.
