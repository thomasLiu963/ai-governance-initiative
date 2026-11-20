# DPV parent of PersonnelPerformanceManagement

Status: rechecked 2026-11-20. Do not post. The extra parent is still present, and issue 501 already asks the chair whether to remove it.

## Source

| Item | Locator |
| --- | --- |
| Issue | https://github.com/w3c-cg/dpv/issues/501, opened 2026-11-16 by `Daham-Mustaf`. Open, no assignee, zero comments. The issue already proposes removing this parent and asks the chair whether the placement was intended. |
| Published vocabulary | DPV 2.3, `master` `689d32c0`. |
| Development tree | `dev` `aff91c29`, `2.4-dev`. |
| Document status | Community-group vocabulary. Not a W3C Standard and not on the Standards Track. |

## What is wrong

`dpv:PersonnelPerformanceManagement` has two parents: personnel management and personnel monitoring. Its children are evaluation, monitoring, and prediction. Evaluation and prediction therefore count as kinds of monitoring, even though the vocabulary already has `dpv:PersonnelPerformanceMonitoring` for the case that is both.

A policy that forbids personnel monitoring and allows performance evaluation is inconsistent under that hierarchy. The issue states that consequence. This comment does not add a new one. It checks that the parent is still there, in the RDFS file and the OWL file, and it asks for one parent to be removed.

The issue cites EU AI Act Annex III point 4(b), which names monitoring and evaluating as two activities. This comment does not claim the Act requires a DPV edit. The reason to remove the parent is the vocabulary's own split: monitoring of performance already has its own term.

## Proposed change

Delete one broader link. `COMMENT.md` is the text. The group edits the Purpose spreadsheet and regenerates. Do not send a Turtle pull request.

## Ordinary-language significance

The vocabulary is used to describe why an employer or a service processes someone's data. As written, evaluating an employee's performance, and predicting it, are classified as monitoring that person. A rule written as "monitoring is not allowed, evaluation is allowed" cannot be applied consistently, because the list says evaluation is a kind of monitoring.

The proposed change leaves performance monitoring in both categories and stops treating every performance-management purpose as monitoring. People who record workplace processing would then be able to name evaluation without also claiming they are monitoring.

If the group makes the change, it is a change to a Community Group vocabulary. It is not a W3C Recommendation, and it does not itself prohibit workplace monitoring.

## Claims that would be false

- "The group decided this." The issue asks whether the parent was intended. The comment recommends an answer. The group can keep the parent.
- "This implements the EU AI Act." The Act is cited by the issue as a comparison. The comment does not map the Act.
- "I edited the vocabulary." No pull request is proposed.

## What would count

A `dev` or published commit in which `dpv:PersonnelPerformanceManagement` no longer has `PersonnelMonitoring` as a parent, and `dpv:PersonnelPerformanceMonitoring` still has both parents. If the group documents that the current parent is intentional, that decision closes the issue the other way. The comment is not acceptance either way.

## Not verified

The online spreadsheet. The generator. An OWL reasoner. The subclass consequence was read from the direct parent triples, not inferred by a reasoner. The 25 November 2026 meeting names parent changes as a topic. It does not name this issue.
