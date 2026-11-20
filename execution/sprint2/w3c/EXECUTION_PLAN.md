# Execution plan

Written 2026-11-19. Checkpoint 2026-11-30. Deadline 2027-02-15. No issue, comment, pull request, or external repository was changed while this plan was written.

## What is ready

1. **GPC test.** `gpc-navigation-cache/` is a two-file Web Platform Tests pull request. Lint and `./wpt run chrome` were recorded on 2026-11-19 against `master` `221a7fea`. That commit was still `master` on 2026-11-20. Chrome 157 with `GlobalPrivacyControlApi` failed the cache assertion. The pull request is not a change to the Global Privacy Control specification.
2. **DPV issue 495.** `dpv-495-service-optimisation/COMMENT.md` asks for one scope-note sentence. The stale sentence and the contradicting ServiceProvision note were re-read in 2.3 and in `2.4-dev`.
3. **DPV issue 501.** `dpv-501-performance-parent/COMMENT.md` asks to remove one parent. Both serialisations still have it.
4. **ACT rule 0va7u6.** `act-0va7u6-rendered-image/` has the comment and the glossary diff. The first external step is the comment. The pull request is a second approval.

## Approval gate

Each item stays local until Thomas approves that item. Approval of one does not approve the others.

When an item is approved, the human who sends it uses the paste-ready text, keeps the disclosure line, and does not add a second thread for the same change. Re-read the cited lines immediately before sending. If the target commit has moved and the defect is already gone, do not send.

## Order

If only one send is approved before 30 November, send the GPC pull request. It is the item the editor's close of issue 165 unblocked, it has an official run, and it is the only prepared change to a conformance suite browsers already execute.

If more than one is approved:

1. Open the WPT pull request from `gpc-navigation-cache/PULL_REQUEST.md`. Request the five reviewers named in `gpc/META.yml`. Do not open a Chromium bug in the same step.
2. Post the issue 495 comment. It is the DPV change that does not ask the group to reconsider an intentional parent.
3. Post the issue 501 comment as a separate comment. Do not combine it with 495, with the existing comment on 484, or with issue 486.
4. Post the ACT comment. Wait for `Jym77` or another maintainer before opening the glossary pull request, unless the approval explicitly includes that pull request.

Do not comment again on GPC issue 165, DPV issue 484, or DPV issue 486.

## What not to file

- A pull request on `w3c/gpc`. Substantive specification edits require Working Group participation or a non-member patent commitment. Neither is in this workspace.
- A Chromium bug for `PrefChangeIsReflectedImmediately`, unless a WPT reviewer asks for one.
- A DPV pull request that edits generated Turtle, HTML, or CSV.
- A repeat of issue 496, issue 485, or issue 500. The first already contains the preferred fix. The second already has Beatriz Esteves's proposed predicate split. The third already proposes `rdfs:label`.
- An ACT change that marks the whitespace-`alt` example as passing, while issue 2412 says Chrome and Firefox have not implemented that mapping and HTML-AAM issue 605 is open.
- Any edit to the frozen AI Content Disclosure report. The chairs have not opened a new version.
- A WCAG or COGA issue that restates an exploratory Web & AI thread. No bounded, unowned patch met the bar.

## How to describe a result

Use these only when the event has happened.

| Event | Sentence that is accurate | Sentence that is not |
| --- | --- | --- |
| Pull request or comment sent | "I submitted a test" or "I asked the maintainers to change one sentence." | "The group adopted it." |
| WPT file merged | "A test was added to the Web Platform Tests suite for the Global Privacy Control Working Draft. The draft text did not change." | "I amended the W3C specification." |
| Chrome still fails that test | "Chrome does not yet keep the cached choice on an already open page." | "Chrome was fixed" or "sites must now behave differently." |
| DPV triple or note changes in a published or `dev` commit | "The Data Privacy Vocabulary Community Group changed this term." Name the term. | "A W3C Recommendation now requires this." |
| ACT glossary merged | "The proposed ACT rule's definition was updated in the Community Group repository." | "WCAG changed" or "the rule is now W3C-approved." |
| Editor closed issue 165 | "An editor quoted the existing cache rule and closed the question." | "The Working Group adopted the test." |

The 13 November policy plan's sample line, "accepted into a named W3C draft," fits a merged edit of a draft specification. It does not fit a WPT merge, a DPV Community Group commit, or an ACT glossary merge. Use the sentences in the table instead.

## Dates

**By 30 November 2026.** The four packets exist. Sending any of them is an approval decision, not a further research task. A merged test, a vocabulary commit, and an ACT merge are not established for this date. The 25 November DPV meeting is a scheduled discussion of parent changes. It is not a channel this project can attend: the join link is login-restricted, and no agenda mail is to be sent.

**By 15 February 2027.** Follow review on whatever was sent. Answer a reviewer's question with a new commit or a short comment. Do not open a replacement proposal while a reviewer is still on the first one. A GPC pull request can still be in review at that date. A DPV commit can fall inside the v2.4 window the 18 November minutes describe, which is a proposal and not a promised release date. An ACT final call of one or two weeks can finish inside this window if the comment is accepted early. None of those outcomes is established, and none of them is a W3C Recommendation.

## If a check fails before sending

- GPC: if `w3c/gpc` `index.html` is edited so a loaded document must update immediately, delete the pull request and do not file it. If `navigation-cache.https.html` appears on `wpt` `master`, do not file a second copy.
- DPV 495: if the scope note no longer mentions ServiceProvision, do not post.
- DPV 501: if `PersonnelPerformanceManagement` no longer has `PersonnelMonitoring` as a parent, do not post.
- ACT: if the glossary on `develop` already names `input`, `object`, `svg`, and `background-image`, do not post.
