# S2 — Execute the parameters the approval displayed

Status: packet complete. Do not file while AISVS pull request 1236 is open. No pull request unless a maintainer asks.

| Item | Record |
| --- | --- |
| Project | OWASP AISVS, draft `1.02-dev` |
| Source | `abcb87056c2a39ae04422abef90c278f43cb4ac8` (2026-11-19) |
| Rows | `9.2.1` Level 1, `9.2.2` Level 2, `9.2.8` Level 3. Next free ID `9.2.12`. |
| Pathway | GitHub issue (`ISSUE.md`). `0001-9.2.12-displayed-parameters.patch` stays local until a maintainer asks for it. |
| Policy | Issue before a pull request. Append identifiers. Do not reuse a retired one. https://github.com/OWASP/AISVS/blob/main/CONTRIBUTING.md |
| AI rule | Same file, "AI-Assisted Contributions". The issue states the tool, the commit, and that the author will defend every sentence. |
| Themes | Human oversight, authorization |

`9.2.12` was the number proposed in closed issues #1125 and #1131 for a liveness control that was withdrawn and never merged. It is unused on this commit. The issue says so, so the number is not a silent revival.

`reproduce.py` is a fixture of one parameter swap. It is not a test of a product.

Pull request 1236 edits the same two files, at `9.5.7` and the C9.5 inventory lines. This patch edits `9.2.11` and the AD.19 inventory line. Both hunks still apply after 1236's diff. Re-read C9.2 if `main` moves past `abcb870` for any other reason before filing.
