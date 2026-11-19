Target: `1.02-dev` only. Released `1.0/` and `1.01/` stay locked.

## Missing predicate

No current requirement says what the runtime does when the policy decision point for an agent action does not return a decision.

Current text in `1.02-dev/en/0x10-C09-Orchestration-and-Agentic-Action.md` at `092232f`:

> **9.5.1** Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and which parameter values it may supply. Level 2.
>
> **9.5.3** Verify that all access control decisions are enforced by application logic or a policy engine, never by the AI model itself. Level 2.

`5.2.5` isolates that decision point from the agent. `9.6.2` blocks an action when a human-approval gate is not satisfied within the defined approval time. `7.1.3` blocks an action when the model response used to decide it cannot be read. A runtime can satisfy each of those and still invoke the tool when the authorization call times out, resets, or returns an error that is not a decision.

Appendix A still states the property. Fail-Closed / Fail-Open:

> AISVS requires AI components with safety or authorization responsibilities to fail closed.

## The row was accepted, then removed in a chapter rewrite

[#676](https://github.com/OWASP/AISVS/issues/676) separated a returned denial from no decision at all. [Rico Komenda, 2026-04-11](https://github.com/OWASP/AISVS/issues/676#issuecomment-4230240883): "The gap is real. ... No existing control explicitly requires fail-closed behavior on PDP timeout or network partition. ... Level 2 is appropriate."

[#683](https://github.com/OWASP/AISVS/pull/683) merged the control on 2026-04-13. At `19e6410889`, on the morning of 2026-06-15, it was still:

> **9.7.4** Verify that when the policy decision point (PDP) used for governance evaluation is unavailable (e.g., timeout, network partition, service failure), agent execution fails closed by blocking the proposed action, and the unavailability event is logged with sufficient detail for incident investigation. Level 2.

[#928](https://github.com/OWASP/AISVS/pull/928), merged that same morning, kept the level: "C9.7.4 | L2 | Fail-closed when PDP unavailable."

[#934](https://github.com/OWASP/AISVS/pull/934) merged later that day with an empty body and no review. It replaced the chapter and deleted `9.7.4` with the rest of C9.7. No comment on that pull request says this predicate was redundant or rejected. No later issue restores it.

## Why this is one AISVS row

ASVS 5.0 [`16.5.3`](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md) says the application fails securely when an exception occurs. It does not require a defined timeout on the policy decision point for an agent action, and a tool call can proceed because the decision call returned nothing and raised no exception. AISVS already states the timeout-and-block pattern for human approval in `9.6.2`. The authorization decision point has no matching row.

The former MCP requirement `10.6.1` denied a request when policy evaluation could not be completed. That row is gone from the released chapters and from `1.02-dev`, and it applied to MCP controls.

## Proposed requirement

Append one Level 2 row. Leave C9.7 retired. Do not reuse `9.7.4`. Leave the logging clause out; a log line is a second test.

> **9.5.8** Verify that when the policy decision point for an agent action does not return a decision within the defined timeout, the runtime blocks the action. Level 2.

For this row, a decision is an allow, a deny, or a referral to the human-approval gate in C9.2. An error, an empty result, a dropped connection, and silence are not decisions. The runtime may block as soon as it knows no decision is coming. The proposed action must not run.

Appendix B lists every active requirement once and adds no requirements of its own. The matching AD.2 line would be: "Runtime blocks an agent action when its policy decision point does not return a decision within the defined timeout | C9.5.8".

## Example

The defined timeout is 200 ms. The tool call would modify a synthetic resource.

Compliant: a local stub accepts the decision request and writes nothing. At 200 ms the tool has not run, and the resource is unchanged. The same block holds when the stub closes the connection or returns an error that is not an allow, a deny, or an approval referral.

Noncompliant: the stub writes nothing, the timeout fires, the runtime invokes the tool, and the resource changes. The same failure holds when the runtime treats a closed connection or an error response as permission to invoke the tool.

## Level

Level 2, the level merged in #683 and recorded for `9.7.4` in #928. `9.5.1`, `5.2.5`, and `9.6.2` are already Level 2. An adopter who already asks a policy engine for each agent action adds a timeout and blocks when no decision arrives.

[Envoy `ext_authz`](https://www.envoyproxy.io/docs/envoy/v1.35.11/intro/arch_overview/security/ext_authz_filter) is an existence proof for that behavior, not a required product. If its authorization service is unavailable, `failure_mode_allow` decides the result, and the default is false, so the request is denied. [NIST SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) §5.1 says no communication between enterprise resources occurs unless the policy engine and policy administrator approve it. §5.2 treats an unreachable policy engine as an availability problem, mitigated by redundancy.

I have not surveyed agent-framework defaults.

## Out of scope

No change to `9.5.6`. No queued-action test procedure. No logging clause on this row. No glossary edit. No edit to locked `1.0/` or `1.01/`.
