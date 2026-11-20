# S3 — Name the instant in 9.5.7

Status: packet complete. Do not file while pull request 1236 is open. Do not file it beside the C9.2 issue. No pull request unless a maintainer asks.

| Item | Record |
| --- | --- |
| Project | OWASP AISVS, draft `1.02-dev` |
| Source | `abcb87056c2a39ae04422abef90c278f43cb4ac8`, row `9.5.7` |
| Pathway | GitHub issue (`ISSUE.md`). The patch replaces the row with the execution-time sentence and is not the submission. |
| Policy | Issue before a pull request. This edits an existing row. It does not add an identifier. https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md |
| AI rule | Same file. Disclosure is in the issue. |
| Themes | Authorization, human oversight |

The known objection is the Level 2 versus Level 3 collision with `9.5.6`. The issue states it by offering the delegation-time sentence as the alternative. Jim Manico's comment on issue 1232 accepted the missing policy-decision rule. It did not mention `9.5.7`.

Pull request 1236 inserts `9.5.8` on the line after `9.5.7`. The held patch is a one-line replacement of `9.5.7` and still applies after that insertion. If `main` changes the `9.5.7` sentence itself, drop the patch and re-read the row.
