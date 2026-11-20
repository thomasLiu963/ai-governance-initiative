Do not post this without an explicit approval. The pathway is a comment on issue 188, not a new issue and not a pull request. Issue 188 has had no maintainer reply since 2026-08-03.

**Where:** https://github.com/OWASP/www-project-ai-security-and-privacy-guide/issues/188

**Body:**

This is only the residual on deferred release, not a new control and not the rest of the list.

Staged commit (https://owaspai.org/go/oversight, read at `bde8cc6f`) lets the agent create the pending email, pull request, or payment batch, and it says the approval binds to that object if the agent cannot edit it afterward. It does not say what happens when the human principal's role, account, consent, or task grant ends before send, merge, or release.

`#MODEL ACCESS CONTROL` revokes the live session. A pending object in another system is not a session. Short token lifetime does not cancel an object that is not a token. Privacy item 8 says consent withdrawal deletes associated data and retrains the model. It does not cancel a send that was already staged. "Genuine opt-out mid-task" is not tied to that object.

Proposed bullet, after the staged-commit bullet, no new control name:

> Before a staged object is sent, merged, or released, check that the human principal who authorized it still holds that authorization. If the role, the account, the consent, or the task grant has ended, freeze or cancel the object in the system that holds it. Do not ask the agent to do this check.

Pull request 235 added staged commit and did not add this check.

### AI assistance

AI was used. Cursor, using Grok 4.7, read the staged-commit bullet and privacy item 8 at `bde8cc6f` and drafted this comment. I have read both against that commit.
