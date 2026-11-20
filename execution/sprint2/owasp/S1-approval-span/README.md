# S1 — Show the untrusted input on the approval screen

Status: packet complete. Not sent. Do not attach it to AI Exchange pull request 287.

| Item | Record |
| --- | --- |
| Project | OWASP AI Exchange, community guidance |
| Source | `bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb` (2026-11-19), `#OVERSIGHT` in `content/ai_exchange/content/docs/1_general_controls.md` |
| Permalink | https://owaspai.org/go/oversight |
| Pathway | Issue first (`ISSUE.md`). Pull request (`PULL_REQUEST.md`, `0001-show-untrusted-input-on-approval.patch`) only if a maintainer wants the wording. |
| Policy | `CONTRIBUTING.md` allows a small clarification as a pull request without an issue. This adds a requirement, so the issue comes first. Pattern to copy: pull request 235. |
| AI rule | https://owaspai.org/contribute/ , "Label AI use". The issue and the pull-request body both say what was used and how much. |
| Themes | Human oversight, human agency, transparency |

`reproduce.py` builds the approval screen from the fields the current bullet names and checks that the instruction is absent. It then checks the proposed span. It does not call a model.

The rendered site was not re-fetched. The repository file at `bde8cc6f` is the source that was read.
