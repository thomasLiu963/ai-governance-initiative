# Submission route

Do not open the pull request, push a branch, or comment on a GitHub issue until Thomas approves that specific action. This file is the route and the requirements. It is not an approval.

## Destination

Repository: [web-platform-tests/wpt](https://github.com/web-platform-tests/wpt), branch `master`.

Directory: `gpc/`. This is not a change to [w3c/gpc](https://github.com/w3c/gpc). A specification edit would be a different contribution. `w3c/gpc` `CONTRIBUTING.md` requires Working Group participation or a non-member patent licensing commitment for substantive specification changes. The WPT contributing file that was read does not state that patent commitment. This patch has no specification text.

Checked base: `fa74da28dbe155bf65dc0b16cfdef8e6fb396153`. The patch only adds files, so it applies on a later `master` unless those paths have since been added.

## Steps, from the WPT submission document

Source: [`docs/writing-tests/submission-process.md`](https://github.com/web-platform-tests/wpt/blob/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/docs/writing-tests/submission-process.md), which points at [`docs/writing-tests/github-intro.md`](https://github.com/web-platform-tests/wpt/blob/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/docs/writing-tests/github-intro.md).

1. Fork `https://github.com/web-platform-tests/wpt`.
2. Create a feature branch from current `master`.
3. Add the three files from `patch/gpc/`, or run `git apply patch/0001-gpc-navigation-cache.patch` from the checkout root.
4. Run the repository `lint` script on the new files. This packet did not run it.
5. Run the test with `./wpt run` in a browser that implements the testdriver commands. The local execution in [local-results.md](local-results.md) used Chrome's DevTools methods through a shim. It is not a substitute for `./wpt run`, because that run is what shows whether ChromeDriver accepts `POST /session/{id}/privacy`.
6. Commit as the human who will answer review. Suggested message, for that person to edit:

    ```
    Test that a GPC preference change waits for the next top-level load.

    Existing gpc tests only observe documents opened after the preference
    is set. The Working Draft already requires the loaded document to keep
    gpcAtNavigation.

    LLM use: an LLM drafted the test from the Working Draft and the current
    gpc files. The human author is responsible for the change.
    ```

7. Push the branch to the fork and open a pull request against `master` with the GitHub UI.
8. Review comments are answered by new commits on that branch. Merge is done by the project after review.

`gpc/META.yml` lists suggested reviewers: `AramZS`, `bvandersloot-mozilla`, `j-br0`, `pes10k`, `SebastianZimmeck`. The WPT review bot uses that file. The patch does not change it. There is no need to file a separate review request for the pull request to be noticed; the submission document says GitHub informs interested parties when the pull request is opened.

The pull request should cite Working Draft § 3.2, § 3.3, and § 3.4. It should say that workers are omitted because [w3c/gpc#146](https://github.com/w3c/gpc/issues/146) has no decision. It should not say that the pull request fixes #146 or #114.

Expect the same-document assertion to fail on a Chrome build that matches `PrefChangeIsReflectedImmediately`. Say that in the pull request so the failure is read as the conformance result, not as a broken harness. If the editors change the caching sentence to require an immediate update, withdraw the patch.

## License

[CONTRIBUTING.md](https://github.com/web-platform-tests/wpt/blob/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/CONTRIBUTING.md) says all contributions are licensed under the [3-clause BSD license](https://github.com/web-platform-tests/wpt/blob/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/LICENSE.md). The license notice read from that file:

- Copyright © web-platform-tests contributors.
- Source redistributions must keep the copyright notice, the conditions, and the disclaimer.
- Binary redistributions must reproduce them in the documentation or other materials.
- The copyright holder's name and the contributors' names may not be used to endorse or promote products derived from the software without specific prior written permission.

The new files follow the existing `gpc/` tests and do not add a separate copyright header. The repository license covers them. `CONTRIBUTING.md` also points to `CODE_OF_CONDUCT.md`. This packet does not restate that document.

## AI assistance

WPT [`docs/writing-tests/ai-policy.md`](https://github.com/web-platform-tests/wpt/blob/fa74da28dbe155bf65dc0b16cfdef8e6fb396153/docs/writing-tests/ai-policy.md), "Policy for LLM (AI) Use", was read. It allows LLMs as tools for commits under these conditions:

- If an LLM was a significant input to a commit, the commit message should say how it was used.
- Every commit is attributed to the human responsible for it.
- One human opens the pull request, writes the pull request description, understands every change, and answers technical discussion.
- Human-authored pull request text, issue text, and review replies do not include model-generated prose in the main text. Model-generated prose goes in a `<details>` element, or in a `<blockquote>` when it is a single paragraph.
- Repeated failure to follow the policy can get a contributor banned.

An LLM drafted this test and this packet. The human who submits has to be able to defend the assertions against § 3.2–§ 3.4 and against the Chrome result below. The pull request description should be that person's own text. A draft they can mine, and must not paste as the main pull request body, follows.

<details>
<summary>AI-assisted draft, not a pull request body</summary>

Test that GPC stays cached until the next top-level document load.

Working Draft section 3.2 caches the preference for a top-level document until the next navigation. `navigator.globalPrivacyControl` and `Sec-GPC` both follow `gpcAtNavigation`. `navigation-cache.https.html` records the loaded document, sets the opposite session preference, and checks that the attribute and a same-document subresource stay as they were. A document opened after the set must show the new preference. The test does not create a worker; issue 146 has not decided worker updates.

On Chrome 157.0.8103.79 with GlobalPrivacyControlApi enabled, the loaded document changed from false to true immediately, and the new document passed with Sec-GPC: 1. Chromium's PrefChangeIsReflectedImmediately browser test expects that immediate update. This test follows the Working Draft.

</details>

## What was not sent

No fork was created, no branch was pushed, and no pull request or issue comment was opened.
