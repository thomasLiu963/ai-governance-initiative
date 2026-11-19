# W3C AI Content Disclosure — technical audit

Audit date: 2026-11-18. Reader: internal review. No external submission, issue comment, pull request, or maintainer contact was made.

## Recommendation

Prepare one future-version erratum, and do not submit it yet. Lead with the research-use clarification already deferred in issue #46, and include two one-paragraph consistency fixes in the same sections: the `human-only` definition, and the overlap between template output and automated reporting. Those three changes do not add a value, a parser rule, or a consumer API.

Hold two further items for the same revision only if the chairs open one: a security note on positive assertions leaking through stripped markup and shadow trees, and a short privacy note split out of issue #49. Do not propose a new contribution-type attribute, a non-HTML specification, or an HTML Living Standard change in this round.

By 2026-11-30 the realistic product is this audited text, ready for internal review. A merge is not a realistic outcome. By 2027-02-15 a single pull request is realistic only if the chairs open a new report version and Thomas approves the submission. The public record says later substantive changes, including issues #46–#49, are a new version. It does not show that version being drafted.

## Document status

| Item | Finding |
| --- | --- |
| Title | AI Content Disclosure for HTML |
| Status | Final Community Group Report, 9 October 2026. The report states that it is not a W3C Standard and is not on the W3C Standards Track. |
| Published URL | https://www.w3.org/community/reports/ai-content-disclosure/CG-FINAL-ai-content-disclosure-20261009/ |
| Live checksum | SHA-256 `95e10d97dce7e7463cd6e2e2a14043e81efedcc058fd10f2c2a97243ecacda9f`, fetched 2026-11-18. This matches the checksum in `reports/README.md` and the byte length of the archived export (132,094 bytes). |
| Maintained source | `index.html` on `main` at `351c0a68e4460b0ce242470395adeac5fcf5ceb9` (merge of PR #50, 2026-10-09). Editor's draft: https://w3c-cg.github.io/ai-content-disclosure/ |
| Group | AI Content Disclosure Community Group, created 3 February 2026. Chairs named on the group page: Sydney Cohen and David Weekly. https://www.w3.org/groups/cg/ai-content-disclosure/ |
| Repository | https://github.com/w3c-cg/ai-content-disclosure — not archived. Last push 2026-10-09. 0 open pull requests. 5 open issues, none assigned, none labeled help-wanted. |

The 21 September 2026 call for decision said approval covered that technical text, that a substantive change would return to the group, and that publication was not a decision to close the group. `reports/README.md` says W3C treats the published URL as immutable and that issues #46–#49 are for a new version. Paola Di Maio's support message says the same: the 21 September text was frozen, and those four issues were opened for a future revision or an appendix. https://lists.w3.org/Archives/Public/public-ai-content-disclosure/2026Sep/0013.html

No new-version draft, milestone, or open pull request exists. The only issue opened after publication is #51 (11 October 2026), a related-work request. Its only comment is from the opener on 17 October 2026. No chair has replied to #46–#49 or #51.

## Maintenance after publication

Verified as done:

- The call for decision opened 21 September 2026. The publication record lists support and no objections or abstentions. https://lists.w3.org/Archives/Public/public-ai-content-disclosure/2026Sep/0011.html
- `w3c/cg-reports` PR #90, opened 2026-10-09 by `dweekly`, merged 2026-10-12 by `ianbjacobs`. https://github.com/w3c/cg-reports/pull/90
- The live report body is byte-identical to the archived export.

Not done in the public record read for this audit:

- The repository README still says the report will be published once W3C merges it.
- `CLAUDE.md` still says a final-report candidate remains a draft pending the vote.
- There is no `minutes/20261005/` file. The publication record says the chairs confirmed the outcome at the 5 October meeting. The October mailing list has two messages, both 5 October meeting notices, and no minutes. The archive index fetched 2026-11-18 has no November 2026 period.
- Two support rows in `reports/README.md` are still marked as private mail, with a note to replace them once list copies arrive. September has 18 archived messages and no later confirmation from those two participants was found.
- WHATWG HTML #9479 is still open, labeled `addition/proposal` and `needs implementer interest`. The last comment from `dweekly` is 23 February 2026. No post-publication comment is on that issue. https://github.com/whatwg/html/issues/9479

The group page still describes an active community group and still features the 5 October 2026 meeting notice. The fetched HTML does not say the group is closed. A script-rendered badge was not inspected.

## Contribution and AI-assistance rules

Read:

- https://github.com/w3c-cg/ai-content-disclosure/blob/main/CONTRIBUTING.md
- https://github.com/w3c-cg/ai-content-disclosure/blob/main/charter.md (Contribution Mechanics and Decision Process; charter last modified 2026-09-21)
- https://github.com/w3c-cg/ai-content-disclosure/blob/main/LICENSE.md
- https://github.com/w3c-cg/ai-content-disclosure/blob/main/CLAUDE.md

Substantive specification contributions can be made only by Community Group participants who have agreed to the W3C Community Contributor License Agreement. Contributions are made in this repository by issue or pull request. Specifications use the W3C Software and Document License. Test-suite contributions use the W3C 3-clause BSD License. Decisions are by consensus, with a 7-day formal-objection period after a recorded decision. The charter puts content-policy instructions and regulatory interpretation out of scope.

No file states an AI-assistance policy. Observable practice is a `Co-Authored-By` trailer for Claude on chair commits, including the 9 October publication commit `146994678` and the 21 September minutes commit `202949871`. `CLAUDE.md` is editor guidance for Claude Code, and it is stale. Issue #47 treats that trailer as the record that Claude took part. A future submission should name the human CG participant as the contributor of record and disclose assistance in the pull request. This audit does not decide whether the CLA accepts an AI-assisted draft.

## How to read the review sample

Dates below are from the GitHub pull-request and comment APIs. "First review" means the earliest review object or substantive comment by someone other than the author. A blank means none was stored. Chair pull requests were often self-merged the same day; the group review of that text was the mailing-list vote, not a review object on the pull request. Successful merges are not an acceptance rate. The rejected pull request is included for that reason.

| PR | Opened | First review | Merged or closed | Author role | Result |
| --- | --- | --- | --- | --- | --- |
| [#20](https://github.com/w3c-cg/ai-content-disclosure/pull/20) Author decision guide | 2026-05-26 | 2026-06-08, `dweekly` (Collaborator, co-chair) | Merged 2026-09-21 by `dweekly` | `dcondrey`, Contributor | Merged after vocabulary rebases. July 13 minutes show a live discussion and a request for a final revision. |
| [#21](https://github.com/w3c-cg/ai-content-disclosure/pull/21) `ai-evidence-url` | 2026-05-26 | 2026-06-08, `dweekly`, initially recommending merge | Closed 2026-09-21 by `dweekly`, not merged | `dcondrey`, Contributor | Rejected. July 13 minutes defer it. The close comment says the target specifications were still drafts, so the link stays unstructured. |
| [#30](https://github.com/w3c-cg/ai-content-disclosure/pull/30) Deterministic content | 2026-06-14 | None stored before merge | Merged 2026-07-07 by `dweekly` | `dcondrey`, Contributor | Merged with no review comment. July 13 minutes discuss the draft after the merge. |
| [#36](https://github.com/w3c-cg/ai-content-disclosure/pull/36) Deterministic, computer-science sense | 2026-08-10 | None stored | Merged 2026-09-21 by `dweekly` | `dcondrey`, Contributor | Merged during the 21 September session. The minutes record the merge and not a separate review. |
| [#39](https://github.com/w3c-cg/ai-content-disclosure/pull/39) Remove `mixed` | 2026-09-21 16:05Z | None stored | Merged 2026-09-21 16:14Z by `dweekly` | `dweekly`, Collaborator | Self-merged in about nine minutes. |
| [#40](https://github.com/w3c-cg/ai-content-disclosure/pull/40) Human review required; percentages dropped | 2026-09-21 16:17Z | None stored | Merged 2026-09-21 16:41Z by `dweekly` | `dweekly`, Collaborator | Self-merged the same hour. The vote then covered the resulting text. |
| [#44](https://github.com/w3c-cg/ai-content-disclosure/pull/44) Minutes note on `meta` versus `body` | 2026-09-21 18:52Z | None stored | Closed 2026-09-21 19:35Z by `dweekly`, not merged | `dweekly`, Collaborator | Not merged. No comment records why. The body proposed a minutes note only. |
| [#50](https://github.com/w3c-cg/ai-content-disclosure/pull/50) Final-report export | 2026-10-09 17:14Z | None stored | Merged 2026-10-09 17:16Z by `dweekly` | `dweekly`, Collaborator | Self-merged in about two minutes. Staff merge of the W3C copy is PR #90 above. |

External contributors who received a written review waited from the June 8 comment to the September 21 session, and one of those two pull requests was rejected. There is no open external pull request to compare with current response time.

## Local check

On 2026-11-18 the illustrative consumer at that commit was served locally and opened in headless Chrome. All 13 checks in `tests/disclosure.js` passed. A separate probe on the same consumer returned:

- a paragraph inside `ai-disclosure="ai-autonomous"`, with page default `human-only`: `ai-autonomous`
- the same paragraph after the section attribute was removed: `human-only`
- an undeclared paragraph in a shadow tree whose host was `ai-autonomous`, on that same page: `human-only`

That matches the specification and the existing shadow check. It is evidence of the inheritance consequence, not of a consumer bug. No model API was called.

## Prior local research

`research/D1/`, `research/D2/`, and `research/incident-evidence/` are not in this workspace. No D1 finding, D2 finding, or incident note is available to support any candidate.

## Ranked candidates

### 1. State the research-use case the group already deferred

1. **Gap.** Boundary guidance lists "Search engines used for research" as no generative-AI involvement, and lists "AI summarization of human-written text" as `ai-assisted` when that text is the reviewed content. It does not say how to classify text a person writes after using a generative model to find, read, or summarize sources. Issue #46 asks for that case in the boundary list and in the author-guide scenario table. Source: `index.html` boundary list around the research and summarization items; sections "Boundary guidance" and "Scenarios". Published anchors: [#boundary-guidance](https://www.w3.org/community/reports/ai-content-disclosure/CG-FINAL-ai-content-disclosure-20261009/#boundary-guidance) and the author decision guide. Issue: https://github.com/w3c-cg/ai-content-disclosure/issues/46
2. **Evidence it is open.** #46 was opened 2026-09-22 by `Starborn`, GitHub association `NONE`, zero comments, no assignee. Paola Di Maio's vote message identifies these as her four issues for a later revision. The publication record repeats that and says they do not change the approved text. The 21 September minutes, under the #34 resolution, say that using an AI research assistant to produce a brief and then writing the text yourself is `human-only`. The #34 close comment by `dweekly` says that if you use tools and are still typing everything yourself, that is outside AI-produced text. Neither sentence appears in `index.html`. The minutes were compiled from Grain notes and co-authored with Claude; the transcript is not in the repository, so the spoken sentence is not independently checked. The close comment and the missing spec text are checked.
3. **Consequence.** Authors and tools can mark the same reported article `human-only` or `ai-assisted`. The machine-readable value then stops distinguishing published model wording from a human article that had a model in the research file. Themes: transparency, human agency.
4. **Proposed change.** In a new version, add one boundary bullet and two scenario rows. Bullet: a generative model used to find or summarize sources, where a person writes the published wording and does not insert model-written wording, is no generative-AI involvement in that published text. Rows: that case recommends `human-only`; publishing the model's summary is classified by the existing two questions, so reviewed publication is `ai-assisted` and unreviewed publication is `ai-autonomous`. Do not add a test about how much the model influenced the author's ideas. The report already rejected percentages and uses a binary question about producing the content.
5. **D1/D2 or incidents.** None available.
6. **Experiment.** None. The change is a classification note. The smallest check is a worksheet of six cases — search engine, unread research brief, human article after a research brief, published reviewed summary, published unreviewed summary, and AI wording pasted into the article — scored only against the two published questions and the #34 comment.
7. **Effort and cost.** Under a day to draft the sentences and the worksheet. No API cost. No parser or consumer change. Adopters who copied the old examples update their authoring guidance.
8. **Route, AI policy, review history.** Comment on #46 with the proposed sentences, then a pull request to `index.html` only after the chairs open a new version. Join the CG and sign the CLA first. Disclose assistance in the pull request. Review history for a comparable external wording change is PR #20: first chair comment in 13 days, merge 118 days later on the ratification day, after requested revisions. Current chair response time is not shown by that sample. #46 has had no reply since 22 September.
9. **Deadlines.** 2026-11-30: proposed wording ready for internal review, not submitted. 2027-02-15: a pull request is possible if a revision is opened and submission is approved. A merge by either date is not supported by current activity.
10. **Accurate accomplishment if the group adopts it.** The report's boundary guidance and scenario table state that a human-written article informed by an AI research brief, without model wording in the published text, is `human-only`, and that publishing the brief is a separate disclosure.
11. **Evidence to retain.** Issue #46, the 23 September vote message, `reports/README.md` future-revision paragraph, minutes `minutes/20260921/README.md` item #34, issue #34 close comment, and the two lists in `index.html`.

### 2. Make the `human-only` definition match the classification procedure

1. **Gap.** The value table says its definitions govern classification. The `human-only` cell says "no AI was involved." The attribute definition and the first classification question say "no generative AI." Boundary guidance excludes deterministic tools, including dictionary spell-check, and says non-generative tools are not covered. Source: `index.html` in "Disclosure values," the attribute definition, and "Boundary guidance." Published anchor: [#disclosure-values](https://www.w3.org/community/reports/ai-content-disclosure/CG-FINAL-ai-content-disclosure-20261009/#disclosure-values). The `ai-assisted` and `ai-autonomous` cells also say "AI was involved" rather than "generative AI."
2. **Evidence it is open.** Both wordings are in the published report, whose checksum matches the archive. No issue states this conflict. It is not assigned. Related closed work shows the group treats the boundary as generative AI: issues #9 and #34, and merged PRs #30 and #36. The 21 September minutes record an editorial heading change to "`human-only` (no AI was used…)", while the published heading says "No generative AI involvement." The table cell still has the broader wording.
3. **Consequence.** A reader who applies the governing table can refuse `human-only` for deterministic spell-check or a template feed because those tools are marketed as AI. The procedure and the boundary list accept `human-only`. The same token then means two things. Themes: transparency, AI reliability.
4. **Proposed change.** In the table only, say "generative AI" in all three meanings. `human-only`: a positive assertion that no generative AI was involved in producing this content. `ai-assisted` and `ai-autonomous`: generative AI was involved, with the existing review distinction left as written. Point the table at Boundary guidance for non-generative tools. No new value.
5. **D1/D2 or incidents.** None available.
6. **Experiment.** None. A reading check is enough: dictionary spell-check, a template scoreboard, and an LLM rewrite, each scored once under the table cell and once under the two questions.
7. **Effort and cost.** About an hour. No API cost. Consumers that compare the three keywords do not change. Authoring docs that quoted the table cell do.
8. **Route, AI policy, review history.** New issue, then the same new-version pull request as candidate 1. CLA, membership, and assistance disclosure as above. Closest merged analogues are PRs #30 and #36, both from `dcondrey`. #30 had no stored pre-merge review and was merged in 23 days. #36 had no stored review and waited 42 days for the ratification session. Both were boundary clarifications the chairs already wanted. This fix is the same kind of edit, but it is not yet requested.
9. **Deadlines.** 2026-11-30: the table sentence is ready to review internally. 2027-02-15: it can ride with candidate 1 if a revision opens. It should not be sent alone to the frozen report.
10. **Accurate accomplishment if adopted.** The normative value table and the two-question procedure use the same generative-AI boundary.
11. **Evidence to retain.** The three cited passages in the checksum-matched report, plus PRs #30 and #36 and the #9 closure, to show the proposed wording follows the group's boundary rather than a new one.

### 3. Separate template feeds from generative automated reports

1. **Gap.** The no-generative-AI list includes a weather-station reading "Temperature: 62°F" and template-rendered stock tickers, sports scoreboards, and server-generated tables. The `ai-autonomous` list then includes "Automated reporting systems (weather, sports scores, financial summaries)" with no qualifier. The later use case "Automated weather feed" is an LLM (`weather-llm-v2`) marked `ai-autonomous`. Source: `index.html` boundary lists and "Automated weather feed."
2. **Evidence it is open.** Both lists are in the published text. No open or closed issue quotes this overlap. Issue #9 and PR #30 established the deterministic exclusion and did not remove or qualify the autonomous reporting bullet. Not assigned.
3. **Consequence.** A template weather or scores page can be marked `human-only` from one list and `ai-autonomous` from the other. Those values make opposite claims about generative-AI involvement. Themes: transparency, AI reliability.
4. **Proposed change.** Qualify the autonomous bullet: automated reports whose published prose is produced by a generative model, as distinct from the sensor readings and template rendering listed above. Add two scenario rows, one for a template scoreboard (`human-only` if no generative model wrote the text) and one for an unreviewed model-written forecast (`ai-autonomous`). Leave the existing LLM weather example as it is.
5. **D1/D2 or incidents.** None available.
6. **Experiment.** None. The worksheet in candidate 2 can add these two rows.
7. **Effort and cost.** About an hour. No API cost. No parser change.
8. **Route, AI policy, review history.** Same new-version pull request and CLA path as candidates 1 and 2. Same review analogues, PRs #30 and #36. No maintainer has flagged this sentence.
9. **Deadlines.** Same as candidate 2. Internal text by 2026-11-30. External review by 2027-02-15 only inside an opened revision.
10. **Accurate accomplishment if adopted.** Boundary guidance no longer lists the same weather and sports output under both no-generative-AI involvement and `ai-autonomous`.
11. **Evidence to retain.** The two bullets and the LLM weather example in the published report.

### 4. Record the positive-assertion leak through transforms and shadow trees

1. **Gap.** There is no token for unknown. Empty and unrecognized values continue inheritance. The security section warns that a sanitizer can drop a local override and expose an inherited `human-only` page default. The inheritance rules also say a shadow tree does not consult its host, but a connected shadow tree still uses the document page default. Source: `index.html` "Cascading rules" and "Security considerations"; algorithm in `examples/resolve-disclosure.js`; checks in `tests/disclosure.js`, including "Shadow ancestry stops at the root" and "Invalid declarations do not mask a valid ancestor."
2. **Evidence it is open as a hazard and closed as an algorithm.** The shadow result is specified and tested: on a `human-only` page, undeclared shadow text is `human-only` even when the host is `ai-assisted`. The 2026-11-18 probe reproduced the sanitizer case and the shadow case with an `ai-autonomous` host. The security section states the sanitizer consequence and stops at publisher testing. It does not say there is no markup that restores unknown, and it does not mention shadow trees. The minutes say the DOM processing rules were not deliberated in the 21 September transcript and were written in the publication sprint; the group then approved the candidate that contains them. A proposal to change the algorithm would reverse ratified, tested text. No issue is assigned to that change.
3. **Consequence.** After a CMS, sanitizer, or syndication step drops `ai-disclosure`, AI text under a `human-only` page default becomes a positive human-only assertion. The same assertion appears for undeclared text inside a component, and the page author cannot reach into the shadow tree to correct it. Unknown would have preserved the absence of a claim. Themes: transparency, human agency.
4. **Proposed change.** Do not change the algorithm in the first submission. File an issue whose proposed text is a note after the sanitizer paragraph and a sentence beside the shadow rule: removing a local declaration does not restore unknown when a page default exists; an undeclared connected shadow tree takes that page default, not the host value. Ask whether a later version should add a declaration that stops inheritance. Add a consumer check that records the strip result as the current conforming result, so a later algorithm change has a failing test to edit on purpose. Do not add a fourth value until the group answers.
5. **D1/D2 or incidents.** None available. The local probe is the supporting demonstration.
6. **Experiment.** The probe already run is the smallest rigorous check. No further experiment, and no model API.
7. **Effort and cost.** Half a day for the issue text and one consumer check. No API cost. A note does not change adopters' parsers. A future stopping token would be a new processing rule for every consumer.
8. **Route, AI policy, review history.** A new issue is the whole first step. An algorithm pull request is appropriate only after a group decision, because the vote froze this processing model. PR #21 is the relevant negative sample: a polished extra attribute was closed when it bound the report to an unsettled external design. PR #41, merged 2026-09-21, is where this processing model was added, by the chair, in the ratification sprint.
9. **Deadlines.** 2026-11-30: issue text and the recorded probe ready internally. 2027-02-15: a note could be accepted inside a revision. An `unknown` token by that date is unlikely without a chair reopening the vocabulary, which they narrowed on 21 September by removing `mixed`.
10. **Accurate accomplishment if the note is adopted.** The report warns that attribute loss and undeclared shadow content can inherit a positive page-level `human-only` assertion, and the consumer checks record that result.
11. **Evidence to retain.** Security paragraph, shadow paragraph, `tests/disclosure.js` shadow check, and the 2026-11-18 probe result in this audit.

### 5. Narrow issue #49 to a privacy note the charter allows

1. **Gap.** Issue #49 asks for three additions: consumers should not treat absence as a reason to rank or distrust content; the accessibility section should discuss authors who use AI as support for disability, neurodivergence, or language; and a standing methodology page should be recognized, including as an `ai-prompt-url` target. The privacy and accessibility sections discuss optional model and provider names, prompt-link fetching, and readers. They do not discuss authors whose disclosure reveals assistive use. The words for assistive use, disability, and negative inference are absent from `index.html`. Issue: https://github.com/w3c-cg/ai-content-disclosure/issues/49
2. **Evidence it is open, and which part is already decided.** #49 was opened 2026-09-22 by `Starborn`, zero comments, no assignee, and is one of the four future-revision issues. The scope section already says the report does not determine how platforms act on disclosure signals. The charter's out-of-scope list includes content policy and interpreting regulation. Issue #16 was closed on 21 September with the decision that `ai-prompt-url` prescribes nothing about the target page. A standing methodology page is already allowed by that decision and does not need a new attribute.
3. **Consequence.** The part that is still unspecified is author privacy. A person who uses a model as writing or reading support and marks the result `ai-assisted` publishes a fact about that support. The report gives optional metadata as the privacy valve and does not mention this one. Themes: privacy, human agency, transparency.
4. **Proposed change.** Comment on #49 with a reduced note, not the whole request. Proposed privacy sentence: declaring `ai-assisted` for writing or reading support can reveal that the author used a tool, including use that is assistive; absence stays unknown and is not a statement that the author avoided such tools. Point platform ranking back to the existing non-goal instead of adding a ranking rule. Do not add Equality Act or GDPR conclusions. One optional sentence can say that a site-level methodology page may be the target of `ai-prompt-url`, without requiring a schema, which keeps the #16 decision.
5. **D1/D2 or incidents.** None available.
6. **Experiment.** None.
7. **Effort and cost.** About an hour. No API cost. No consumer change.
8. **Route, AI policy, review history.** Comment on the existing issue. Do not open a duplicate. Same CLA path if it later becomes a pull request. No chair reply since 22 September. The ranking half of the issue conflicts with a recorded non-goal, so a full implementation of #49 has a weaker prospect than the privacy sentence. PR #21 shows that scope conflicts are closed even after an encouraging first review.
9. **Deadlines.** 2026-11-30: the reduced comment is ready internally. 2027-02-15: it can be added to a revision if #49 is triaged. It should not be the first external comment unless the chairs invite text on the open issues.
10. **Accurate accomplishment if adopted.** The privacy section says `ai-assisted` disclosure can reveal assistive use of a writing tool, and that omission remains unknown.
11. **Evidence to retain.** Issue #49, the scope non-goal, charter out-of-scope items 4 and 7, the #16 minutes entry, and the privacy section of the published report.

## Not recommended now

- **Issue #47, an `ai-contribution` attribute.** Open, with comments from `arsentev-ai` (25 September) and `sanjana658` (29 September, offering to draft it). No chair reply and no assignment. The 21 September minutes closed #7 by putting every human-plus-AI case in `ai-assisted`, and closed #25 by rejecting percentages. A new closed vocabulary reopens both decisions. `sanjana658` has already asked for the task, so a parallel draft would collide.
- **Issue #48, a non-HTML pointer.** Open, no comments. The cited Publishing CG issue is real and open: https://github.com/w3c-cg/publ-a11y/issues/814. The report's scope is HTML text, and #37 was closed on that boundary. A cross-format note is a liaison sentence, not a repair of this processing model.
- **Issue #51, AI Usage Scale citation.** The vocabulary maintainer opened it on 11 October and commented again on 17 October. No chair reply. Adding the citation does not fix a gap in this report, and the requester is already driving it.
- **WHATWG adoption.** HTML #9479 remains a page-level proposal with `needs implementer interest`. The CG's element-level design is the group's own liaison item. Filing it again is not a narrow erratum, and this audit found no post-publication comment on that issue.
- **README refresh.** The chairs' publication checklist already includes linking the live report from the README. That is housekeeping left after the 12 October staff merge. It is not one of the disclosure gaps above.

## What this audit did not verify

- The Grain transcript behind `minutes/20260921/README.md`. The research-assistant sentence is cited as minutes text, with the #34 close comment as the GitHub record.
- Script-rendered portions of the W3C group page, including any badge this fetch did not receive.
- Whether liaison mail listed in `reports/README.md` was sent anywhere other than WHATWG HTML #9479, which was checked.
- A W3C-wide generative-AI contribution rule beyond this repository's files.
- Whether the two privately recorded supporters later confirmed on a channel that is not in the public list archive.
- Any implementation other than the repository's illustrative consumer.
