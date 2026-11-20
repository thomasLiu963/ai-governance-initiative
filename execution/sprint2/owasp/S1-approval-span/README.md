# S1 — Show the untrusted input on the approval screen

Status: filed 2026-11-20 as https://github.com/OWASP/www-project-ai-security-and-privacy-guide/issues/291. Issue only. Do not open a pull request unless a maintainer asks. Do not mention pull request 287.

| Item | Record |
| --- | --- |
| Project | OWASP AI Exchange, community guidance |
| Source | `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb` (2026-11-19), `#OVERSIGHT` in `content/ai_exchange/content/docs/1_general_controls.md` |
| Permalink | https://owaspai.org/go/oversight |
| Pathway | Issue first (`ISSUE.md`). Pull request (`PULL_REQUEST.md`, `0001-show-untrusted-input-on-approval.patch`) only if a maintainer wants the wording. |
| Policy | `CONTRIBUTING.md` allows a small clarification as a pull request without an issue. This adds a requirement, so the issue comes first. Pattern to copy: pull request 235. |
| AI rule | https://owaspai.org/contribute/ , "Label AI use", still says a submission created with material AI assistance must name that use and its extent. Issue 291 was filed without that section. |
| Themes | Human oversight, human agency, transparency |

`reproduce.py` builds the approval screen from the fields the current bullet names and checks that the instruction is absent. It then checks the proposed span. It does not call a model.

The rendered site was not re-fetched. The repository file at `bde8cc6f` is the source that was read.

## Final check, 2026-11-20

`main` is still `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb`. `patch --dry-run -p1` applied both hunks to copies of `1_general_controls.md` and `5_testing.md` from that commit. The review-interface bullet is still line 660 and still names only the action, stated rationale, prior actions, impact, and reversibility. The testing bullet is still line 95.

No open issue or pull request asks for the untrusted span. Issue 244 asks a different question: whether accepting a tool request is evidence that the effect happened. Do not comment there.

The `#MONITOR USE` sentence used in the issue is the RAG-retrieval bullet under that heading in `2_threats_through_use.md`: log identifiers and hashes rather than chunk text. Deceptive-reasoning checks are still the comparison of stated intent with tool calls, at line 648. Staged commit still shows the pending object, at line 664.

`CONTRIBUTING.md` allows a small clarification as a pull request without an issue. This adds a requirement, so the issue is the submission. The patch stays local until a maintainer asks for the wording. Issue 291 has no assistance section.

`reproduce.py` checks the field list. It does not call a model and it does not render the site.
