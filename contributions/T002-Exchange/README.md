# T002 — one rule when the policy engine is unreachable

Status: **ready for internal review, not submitted.** Opening the pull request needs an explicit approval. Nothing in this directory has been filed.

Document being changed: OWASP AI Exchange, community guidance, commit `c68371ed56051a3d7c894e36c20c3bcbc22eb441` (2026-11-16). Permalink: https://owaspai.org/go/leastmodelprivilege

This packet is a proposed change to that guidance.

## What to send

A docs-only pull request, no issue. The exact title and body are in `pull-request.md`. The exact diff is `0001-unreachable-policy-engine-denies-the-action.patch`.

The whole change is the last clause of the Limitations paragraph under the agentic authorisation block in `#LEAST MODEL PRIVILEGE`:

- Published: "policy engine outage requires an explicit fail-closed vs fail-open choice."
- Patched: "if the policy engine is unreachable, deny the action."

The implementation bullet already says "Fail closed if the policy engine is unreachable." It stays. The two sentences then agree.

## Before opening the pull request

1. Confirm `main` still has the published clause above. If it does not, do not open this pull request against a sentence that has moved.
2. Apply `0001-unreachable-policy-engine-denies-the-action.patch` and confirm the diff is still that one clause.
3. Read the patch. The AI-assistance paragraph in `pull-request.md` says the opener has read it. Send that paragraph only if that is true.
4. Do not add a hall-of-fame row, a new control name, a tool link, or the examples in `examples.md`. The examples are for review of this packet and, if useful, a short comment. They are not page text.
5. Do not mention AISVS, issue 188, or issue 222 in the pull request. The coordination note is in `rationale.md`. Those issues are someone else's open work.

## Why the patch is this small

The two sentences were introduced together on 2026-08-03 and were not later distinguished. There is no recorded rule that fail-open is allowed for reads, or for any other named class. Adding that exception would be new guidance. Deleting the clause and saying nothing would leave the outage undiscussed in the paragraph that raised it. The clause above repeats the rule the implementation bullet already gives.

Themes: authorization, AI reliability. An action the policy engine did not decide does not proceed, so the failure is observable as a deny.

## Separate from the approval-screen candidate

`contributions/OX-1-Exchange/` is a different candidate, about showing the untrusted input behind a human approval. It is not part of this pull request and should not be attached to it.

## Not verified

Listed in `rationale.md`. The short version: no submission has been made, `main` was last checked at `c68371ed`, and no runtime experiment was run.
