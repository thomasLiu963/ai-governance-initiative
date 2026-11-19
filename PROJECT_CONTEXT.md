# AI Governance Initiative

Local workspace for coordinated technical research and public-interest work on AI governance. The aim is substantive, externally verifiable contributions to existing technical standards, AI security guidance, research infrastructure, and university or government policy.

This file is the working context for the project. It does not authorize external action. No finding, citation, statistic, experiment, or acceptance claim in this workspace is valid unless it is recorded with a checkable source.

## Goals

1. Produce technically grounded contributions that an external reviewer can verify against a published source.
2. Improve existing standards, security guidance, research infrastructure, and institutional policy where a concrete gap, error, or missing requirement can be shown.
3. Keep human agency, reliability, transparency, privacy, authorization, and human oversight as the tests for whether a change is worth making.
4. Prefer fewer contributions with clear technical value over a larger count of superficial ones.
5. Leave a local evidence trail that separates what was read, what was tested, what was proposed, and what an external body actually accepted.

## Deadlines

| Horizon | Date | Purpose |
| --- | --- | --- |
| Immediate | 2026-11-30 | First set of candidate contributions that are sourced, scoped, and ready for internal review. |
| Longer term | 2027-02-15 | Contributions that have completed internal review and, only where explicitly approved, external submission and follow-up. |

Dates are targets for the quality of the work, not a reason to file an unready proposal.

## Research themes

Every candidate contribution should state which of these themes it serves, and how:

- **Human agency.** People can understand and choose whether and how an AI system acts for them.
- **AI reliability.** Claims about model or system behavior are bounded, testable, and fail in observable ways.
- **Transparency.** Disclosures match what the system actually does, at a level a reviewer can check.
- **Privacy.** Data collection, inference, retention, and sharing are specified and limited.
- **Authorization.** Actions that affect a person, an account, or a system require a clear grant of permission.
- **Human oversight.** A person can intervene, review, or stop a consequential automated action.

A change that does not connect to at least one theme should not be pursued.

## Workspace map

Investigative work stays inside the directory assigned to that audit. Shared material lives only in the directories listed as shared.

| Path | Role |
| --- | --- |
| `research/D1/` | Research track D1. |
| `research/D2/` | Research track D2. |
| `research/incident-evidence/` | Local notes on publicly documented incidents. |
| `audits/owasp-exchange/` | OWASP AI Exchange audit. |
| `audits/owasp-testing/` | OWASP testing guidance audit. |
| `audits/owasp-aisvs/` | OWASP AI security verification audit. |
| `audits/w3c-dpv/` | W3C Data Privacy Vocabulary audit. |
| `audits/w3c-gpc/` | W3C Global Privacy Control audit. |
| `audits/w3c-ai-disclosure/` | W3C AI disclosure work audit. |
| `audits/research-reuse/` | Research-reuse infrastructure and practice audit. |
| `audits/university-policy/` | University AI policy audit. |
| `audits/fcc/` | FCC-related policy audit. |
| `references/` | Shared source notes and bibliographic records. |
| `experiments/` | Local, non-billable experiments and their raw outputs. |
| `contributions/` | Draft contributions after an audit recommends one. |
| `evidence/` | Proof of review, submission, and disposition. Shared. |

Directory names identify the assignment. They do not establish whether a document is a published standard, a draft, community guidance, or a proposed change. That status is recorded only after the source is read.

## Execution rules

1. **Work locally.** Drafting, note-taking, and experiments stay in this workspace.
2. **One owner per audit.** Each investigative agent writes only in its assigned audit directory, plus material it is explicitly asked to place in `references/`, `contributions/`, or `evidence/`.
3. **No external changes without approval.** Do not open public issues, pull requests, messages, submissions, or commits to upstream repositories, and do not make any other external change, unless Thomas explicitly approves that specific action.
4. **No paid inference.** Do not make paid external API calls or run billable experimental inference.
5. **Public reading is allowed.** Ordinary reading of public repositories and public web research is permitted.
6. **No fabricated records.** Do not invent findings, citations, experiments, statistics, or claims that a contribution was accepted.
7. **Check contribution rules first.** Before proposing a change to a project, read and record that project's contribution policy and its policy on AI assistance.
8. **Label document status.** Distinguish a published standard from a draft, from community guidance, and from a change this project proposes.
9. **Protect unpublished material.** Do not send unpublished research files or sensitive information to third-party services without explicit approval.
10. **Reuse existing research accurately.** When prior work is used, cite it as published and do not alter its claims.
11. **Value over volume.** Prioritize a genuine technical improvement. Do not add a candidate because it would increase a count.

## Contribution bar

A candidate is ready for internal review only when `MASTER_TRACKER.md` has all of the following:

- The exact source: title, version or date, and a stable URL or other locator.
- Document status: published standard, draft, community guidance, or proposed change.
- The project's contribution policy and AI-assistance policy, with locators.
- The gap or error, stated so a reviewer can confirm it in the source.
- The themes served, and the concrete requirement or text being proposed.
- Implementation requirements, including what an adopter would have to do.
- What was not verified.

External submission is a separate step. It requires an explicit approval recorded in the tracker. Acceptance is recorded only with evidence of the external body's actual decision.

## Status

Initialized locally on 2026-11-18. No audits have been started, no repositories have been cloned, and no external submissions exist.
