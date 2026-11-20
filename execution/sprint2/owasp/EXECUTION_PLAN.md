# Execution plan

Nothing here is approved for sending. Do not open an issue, a pull request, or a comment from this directory until Thomas approves that specific item.

The first-person disclosure in each packet is accurate only after the person who sends it has read the quoted upstream sentences and the proposed sentences. The tool that drafted them was Cursor, using Grok 4.7.

## Do not touch

- AISVS issue 1232 and pull request 1236. Do not push to that branch. Do not comment unless a reviewer asks a question.
- AI Exchange pull request 287. Do not add commits. Do not reply.

## Order

1. **S1, when approved.** Open the issue in `S1-approval-span/ISSUE.md` on `OWASP/www-project-ai-security-and-privacy-guide`. Do not open it on the same day as pull request 287, and do not mention 287. If a maintainer asks for the patch, open `PULL_REQUEST.md` with `0001-show-untrusted-input-on-approval.patch`. Re-read the review-interface bullet at the then-current `main` first. If the bullet already requires the span, do not send.

2. **S2, only after 1236 has merged.** Open `S2-displayed-parameters/ISSUE.md` on `OWASP/AISVS`. Confirm `9.2.12` is still unused and that `9.2.1`, `9.2.2`, and `9.2.8` still say what the issue quotes. Do not open a pull request unless a maintainer asks. The patch is the one to send if they ask. It applied on `abcb870` and on a copy that already contained 1236's two lines.

3. **S3, only after S2 has a reply that is not a refusal of another C9 issue.** Open `S3-delegation-instant/ISSUE.md`. One sentence, their choice of the two. The held patch is the execution-time sentence only. Drop it if they choose the delegation-time sentence. Do not file S2 and S3 the same week.

4. **S4, do not send in this sprint.** The comment is in `S4-staged-release/COMMENT.md`. Post it only under a separate approval, and only if issue 188 is still without a maintainer answer. A pull request that edits staged commit while 188 is the workstream's list is the step the August reply did not ask for.

## Pathways

| Packet | Document status | First send | Pull request |
| --- | --- | --- | --- |
| S1 | Community guidance | Issue | After a maintainer wants the wording. `CONTRIBUTING.md` would allow a small fix without an issue. This is a new requirement, so the issue is first |
| S2 | Draft, `1.02-dev` only | Issue | Only if a maintainer asks. Append `9.2.12`. Do not renumber |
| S3 | Draft, `1.02-dev` only | Issue | Only if a maintainer asks. Edit `9.5.7` in place |
| S4 | Community guidance | Comment on issue 188 | Not unless later approval says the one bullet may go up alone |

## What "accepted" means

A merge into Exchange `main`, or into AISVS `1.02-dev`, whose text contains the sentence that was proposed. A comment that agrees is not acceptance. Pull request 1236 merging is acceptance of issue 1232, which is already filed, and it is not acceptance of S2 or S3.

## Disposition

| Proposal | Disposition | Why |
| --- | --- | --- |
| S1 approval span | Ready to submit now | Issue, pull-request text, and patch checked against `bde8cc6`. Send only with approval, and not on the same day as pull request 287 |
| S2 displayed parameters | Needs more work | The issue and the patch are finished. The missing step is the merge of 1236, then a re-read of C9.2. Filing beside 1236 is the wrong step |
| S3 delegation instant | Needs more work | The issue is finished. It waits on 1236 and on the reception of S2. The Level 2 versus Level 3 objection is unresolved |
| S4 staged release | Needs more work | The comment is finished. Issue 188 has had no maintainer reply since 2026-08-03. Do not send it to create a second thread |
| Glossary TLS 1.3 versus the ASVS scope sentence | Discard | One false sentence. It does not add a safeguard, and transport security is the section AISVS already assigns to ASVS |
| Testing Guide APP-13 and APP-14 | Discard | The undefined scores are real. Nothing in that repository has merged since 2026-06-01 |
| Agent Control Standard issues 613 and 614 | Discard | Filed, with reproductions, by `MK023`, who has the open host pull request |
| AI Agent Security Cheat Sheet | Discard | The parameter-binding control is already in the sheet. Five updates on that file are open |
| AISVS `9.5.6` predicate restoration | Discard | Jim Manico wrote on 2026-11-08 that the row needs no change |
| End-user credential row | Discard | The deletion is real, and a leader can treat `9.4.1` plus `9.5.2` as enough |
| GenAI LLM Top 10 errata | Discard | The open errata already have authors |
| New Exchange control family | Discard | Those drafts are the ones that stay open for months |
