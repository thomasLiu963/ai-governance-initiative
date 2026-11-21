# ACT rule 0va7u6, rendered image resource

Status: rechecked 2026-11-20, including the rule examples. Ready as a comment on issue 2408. Not posted. A pull request waits for a separate approval after the comment, or for an approval that explicitly includes the pull request.

The comment no longer says the rule has both a passed and a failed example for every non-`img` case. `object` and the SVG `image` have passed examples. `input type="image"` and `background-image` have passed and failed examples. That distribution is not the defect.

## Source

| Item | Locator |
| --- | --- |
| Issue | https://github.com/act-rules/act-rules.github.io/issues/2408. Opened 2026-04-16 by `Jym77`. No assignee. Zero comments. Still true on 2026-11-20. |
| Rule | `_rules/image-no-text-0va7u6.md` on `develop` `50d2bede1ee705be6840d06f356a6ae2fd94cb2c`. Published proposed rule: https://www.w3.org/WAI/standards-guidelines/act/rules/0va7u6/proposed |
| Glossary | `pages/glossary/rendered-image-resource.md` and `pages/glossary/embedded-image.md` at that commit. `develop` was still `50d2bede` on 2026-11-20. The glossary sentence still limits the resource to HTML's image-source list. The embedded-image definition still lists the five cases. |
| HTML | https://html.spec.whatwg.org/multipage/images.html#image-source defines an image source for `img` and `link`, not for `input`, `object`, `svg`, or CSS. |
| Document status | ACT Rules Community Group source. A proposed rule on the WAI site is W3C accessibility testing guidance maintained with the ACT Task Force. It is not WCAG, and it is not a W3C Recommendation. Merging a glossary edit does not approve the rule. The repository says an ACT Task Force facilitator sets a rule to approved with a separate action. |

## What is wrong

The rule says it applies to rendered image resources. The glossary defines those as resources named in HTML's image-source list of an embedded image. HTML's image-source list does not exist for an image button, an `object`, an SVG `image`, or a CSS background. The rule's own examples use all four. Read strictly, those examples are outside the rule.

The `img` case is already correct. The proposed text leaves that case on the HTML list and names the resource pointer for each other case the embedded-image definition already lists.

A repository search for the phrase found it only in the glossary page and in this rule. The edit does not retarget other rules.

## Contribution rules

The README says contributing is open and pull requests are welcome, and it asks active contributors to join the ACT Rules Community Group. This workspace has no record of that membership. `github-guidelines.md` says a change that alters the meaning of a rule states a final-call period: two weeks for a major change, one week for a smaller one. This edit changes written applicability and does not add or remove examples. The comment says to state a final-call period and does not pick a length the group has not used for this file.

No AI-assistance rule was found in the README or the GitHub guidelines. The comment discloses the drafting anyway.

## Ordinary-language significance

WCAG says a page should use real text rather than a picture of text, with some exceptions. This ACT rule is one shared way to test that. The rule's examples include a picture used as a button, a picture in an SVG, and a picture painted as a background. The definition those examples depend on only describes ordinary `img` elements, because it borrows a term HTML defines for `img`.

The proposed paragraph makes the definition name the button, the SVG image, the embedded object, and the background image. Testers and test tools that follow the written definition would then be testing the cases the examples already show.

That is a correction to a Community Group test rule. It does not change WCAG. It does not, by itself, move the rule from proposed to approved.

## Claims that would be false

- "I changed WCAG." The success criteria are untouched.
- "The rule is now a W3C-approved test." Approval is a separate facilitator action.
- "Browsers were fixed." This is a definition of a test, not a browser change.

## What would count

A merge to `act-rules/act-rules.github.io` `develop` of this glossary wording, or wording the group adopts for the same five cases. A later approved publication of rule 0va7u6 is a second result. The comment is not either result.

## Not verified

The ACT test runner was not executed. Implementations of rule 0va7u6 were not surveyed. Whether an `svg` `image` with only `xlink:href`, and no `href`, is already covered by the embedded-image definition was not re-checked; the proposed bullet follows that definition and uses `href`. The final-call length is for the group to set.
