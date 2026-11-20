# W3C sprint ranking

Date: 2026-11-19. Nothing in this directory was filed, posted, or pushed. Acceptance means a merge, a published vocabulary change, or an approved rule update. An editor comment, a closed question, and a local file are not acceptance.

The admissions test used here is the one in the 13 November 2026 policy plan: say what document changed, who can act on it, and what status it has. A Web Platform Test is not a specification amendment. An editor's reply is not adoption. A Community Group report is not a W3C Recommendation.

## Submit after approval

These four have a local packet. They are ordered by how directly a maintainer can take the prepared text.

| Order | Item | Packet | What a maintainer can do | Status of the target |
| --- | --- | --- | --- | --- |
| 1 | GPC navigation-cache test | `gpc-navigation-cache/` | Merge two new files into `web-platform-tests/wpt` | W3C Working Draft, tested by WPT. The pull request does not edit the draft. |
| 2 | DPV ServiceOptimisation note | `dpv-495-service-optimisation/` | Replace one scope note from the spreadsheet | DPV Community Group vocabulary, published as a Final Community Group Report. Not a W3C Recommendation. |
| 3 | DPV performance-management parent | `dpv-501-performance-parent/` | Delete one parent link | Same Community Group vocabulary. The group still has to decide the parent was unintended. |
| 4 | ACT rendered-image definition | `act-0va7u6-rendered-image/` | Replace one glossary paragraph used by proposed rule 0va7u6 | ACT Rules Community Group text. Not WCAG. A merge does not approve the rule. |

### 1. GPC test

The Working Draft of 24 September 2026 says a Global Privacy Control choice is cached when a top-level page starts loading. A change during or after that load is not shown until the next navigation. The JavaScript flag and the `Sec-GPC` header both follow that cached value.

The tests already in `gpc/` set the choice and then open a new page. They never look at the page that was already open. The new test does only that. Chrome 157, in the official local run recorded on 2026-11-19, updated the open page immediately: the test expected false and got true. That is a real disagreement between Chrome and the draft. It is the reason to propose the test.

Sebastian Zimmeck, an editor, closed issue 165 on 2026-11-19 by quoting that cache rule. He did not change the specification. The close is enough to stop waiting for a spec edit before proposing a test of the published rule. It is not a Working Group decision, and it is not acceptance of the test. His added sentence, that implementers should make a best effort to follow the person's preference, is not a permission to ignore the cache. The test does not encode that sentence. It also does not require the reload prompt, which the draft only says the browser should offer.

A specification pull request on `w3c/gpc` is still out of bounds. That repository requires Working Group participation or a non-member patent commitment. This workspace has neither.

Ordinary language, if the pull request is later merged: "I added a browser test for the W3C Global Privacy Control draft. The test checks that a page keeps the do-not-sell choice from when it loaded. The specification text did not change. Chrome failed the test."

Do not say the specification was amended, that the editor adopted the test, or that the signal is now legally required.

### 2. DPV ServiceOptimisation

In DPV 2.3 and in `2.4-dev` at `aff91c29`, ServiceOptimisation sits under ServiceManagement. Its scope note still says it is a subclass of ServiceProvision. ServiceProvision's own note, changed in the same release, says that term must not be used for managing a service. Issue 495 states this, has no assignee, and has no comments.

The comment asks for one replacement sentence, the option the issue already prefers. The group regenerates the files from the spreadsheet. A comment is not the vocabulary change.

Ordinary language, if the sentence is later published: "In the Data Privacy Vocabulary, a Community Group list of privacy terms, a leftover note said optimising a service was part of providing it. The maintainers replaced that note so it matches the management category they had already assigned."

Do not call DPV a W3C Recommendation.

### 3. DPV performance parent

PersonnelPerformanceManagement is filed under both personnel management and personnel monitoring. Evaluating performance and predicting performance therefore count as monitoring. The vocabulary already has PersonnelPerformanceMonitoring for the overlap. Issue 501 has no assignee and no comments. The parent is still present in the RDFS file and the OWL file.

The comment asks the group to remove only the monitoring parent of the management term, and to leave the monitoring term's two parents in place. The issue asks whether the parent was intended. The group can say yes and keep it. That is a real decision, not a typo.

Ordinary language, if the parent is later removed: "A Community Group privacy vocabulary had classified evaluating or predicting an employee's performance as monitoring that person. I asked the maintainers to stop doing that, and to keep a separate term for performance monitoring. They made that change."

If they decline, the accurate sentence is that the question was asked and the group kept the parent. Do not describe a declined comment as a vocabulary change.

### 4. ACT rendered image

Proposed rule 0va7u6 tests images of text for WCAG 1.4.5 and 1.4.9. Its examples include image buttons, SVG images, objects, and CSS backgrounds. The definition of "rendered image resource" only points at HTML's image-source list, which HTML defines for `img` and `link`. Strictly read, the button and background examples are outside the rule. Issue 2408, opened by `Jym77` on 2026-04-16, says this and has no comments and no assignee.

The local file names the resource each of the five cases already listed under "embedded image" actually uses. The `img` case stays on the HTML list. No example is added or removed. A search of `develop` found the definition used only by this rule and its glossary page.

Ordinary language, if the glossary change is later merged: "I corrected a W3C accessibility test rule so its definition covers image buttons, SVG images, and background images, which its examples already used. The change is in the Community Group's proposed rule. It does not change WCAG, and it does not by itself mark the rule as approved."

## Credible, and not prepared as a submission

These were checked against current files or current issues. They are real. They are not the next thing to send.

| Item | Why it is real | Why it is not in a packet |
| --- | --- | --- |
| DPV issue 496, CommercialPurpose and NonCommercialPurpose | The two definitions use "or" in a way that lets one activity match both. Still the same sentences in `2.4-dev` purposes. Unassigned, zero comments. | The issue already prefers a specific replacement and gives the examples. A second essay would repeat it. Send something only if a maintainer asks which option to apply. |
| DPV issue 485, `skos:sameAs` | SKOS has no `sameAs`. `2.3/loc/modules/locations.ttl` and `2.4-dev/loc/modules/locations.ttl` still contain the predicate 57 times each. | Beatriz Esteves already proposed `skos:exactMatch` for RDFS+SKOS and `owl:sameAs` for OWL, on 2026-09-09, and asked the chair. A second recommendation is not a new repair. |
| ACT issue 2412, whitespace `alt` | HTML-AAM now treats `alt` of only whitespace as decorative, so failed example 4 of rule 23a2a8 is the wrong outcome under that mapping. | The issue says Chrome and Firefox have not implemented it. `w3c/html-aam` issue 605 is still open, last updated 2026-05-22. Changing the example to a pass would disagree with current browsers before that question is settled. |
| AI Content Disclosure, `human-only` and the research-use case | The value table says "no AI was involved" where the classification questions say "no generative AI." The research-use case the group discussed is not in the published boundary list. | The 9 October 2026 report is a frozen Final Community Group Report. Issues 46 and the related wording fixes wait on a new version. The chairs have not opened one. `main` was still `351c0a68` on 2026-11-19. A Community Group report is not a Recommendation even after a future edit. |
| GPC issue 114, combined `Sec-GPC` | The receiver text and the combined-field comment still disagree. Peter Snyder's 22 October 2026 comment schedules the work after version 1. | A specification change needs the patent commitment this workspace does not have. A comment-only approval is not recorded. Do not attach it to the navigation-cache pull request. |
| WCAG, COGA, and the Web & AI Interest Group | ACT issues 2472 and 2473 are the group's own open wording and AI-implementation items, with maintainers already writing. Web & AI issues are exploratory discussion, not a test or a spec patch. No open `w3c/silver` issue in the 2026-11-19 search was an unowned AI requirement. | There is no bounded text a maintainer can merge from an outside patch this month. COGA's March 2026 minutes treat the AI threads as discussion without a deadline. |

## Already handled, and not repeated

- GPC issue 165 is the question. The test packet is the follow-up. Do not comment on 165 again.
- DPV issue 484 already has the membership comment. Do not add another.
- DPV issue 486 is the parent the 9 September minutes already chose. A comment that repeats that choice was deprioritized on 2026-11-19. It is still not this sprint's work.
- DPV issue 500 already proposes the `rdfs:label` fix. Do not restate it.
- GPC issue 146, workers, has no editor choice. The test leaves workers out on purpose.
- Purpose-conditional GPC, an AI-training meaning for GPC, and a GDPR rewrite stay out. Those are new policy proposals, not repairs.

## What November 30 and February 15 can mean

| Item | By 2026-11-30 | By 2027-02-15 |
| --- | --- | --- |
| GPC test | The run and the pull-request text exist. A merge is not established. Opening the pull request depends on approval. | The pull request can be in review. The closest recorded WPT sample, pull request 54446, took about a month for a Mozilla author and was not re-fetched today. A test Chrome fails can take longer. A merge is not established. |
| DPV 495 and 501 | Comments can be posted if approved. The 25 November meeting is scheduled to discuss parent changes. That is not a promise these two issues will be called. | A vocabulary commit can be part of the v2.4 work described in the 18 November minutes: December commits, a January beta, a final release at the end of January. That schedule is a chair's proposal, not a resolution. No v2.4 date was published as a commitment. |
| ACT glossary | The comment and the diff exist. | A merge is possible for a one-file definition fix after the group's final-call period. Approval of rule 0va7u6 is a later Task Force action. Neither date is established. |
