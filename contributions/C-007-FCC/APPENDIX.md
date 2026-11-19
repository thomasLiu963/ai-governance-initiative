# Technical appendix: local specification fixture for revocation operations

This appendix is a description of a local fixture. It is not a measurement of a commercial voice platform, messaging provider, dialer, handset, or campaign tool, and it is not a study of consumers. The fixture source is `audits/fcc/sim_revocation.py`. It was not modified for this appendix. Regenerate the machine-readable report with:

```bash
python3 contributions/C-007-FCC/reproduce.py
```

The command uses the Python standard library only. It does not call a model, a network service, or a paid API. The report is written to `contributions/C-007-FCC/results/report.txt`. If this narrative and a fresh report disagree, the fresh report controls, and this narrative should be corrected before anyone relies on it.

A passing assertion means the objects in that case matched the assertion. It does not mean a provider accepted or rejected a message.

## What the four functions do

The script keeps four operations apart.

- `recognize` returns a label for one fixed string. It does not write the permission store.
- `apply_scope` writes the store only when a case calls it. The key is the called number, the caller name, and a category. The category `*` matches every category for that number and caller. The script has no channel field.
- `cancel_controlled` changes a pending message to `cancelled` only when the store blocks that message and the case set `in_caller_control` to true. A message with that flag set to false stays `pending`. The flag is assigned in the case. It is not an observation of a handoff to a carrier.
- `decide_send` either reads the store at send time or trusts `cleared_at_schedule`. A pending message whose `kind` is `confirmation` is marked sent even when the store blocks the number. The function does not count earlier confirmations. Any other blocked message is marked `suppressed` when the chosen read says it is blocked.

The labels are exact matches, after the string is stripped and internal whitespace is collapsed:

| Input fixed in the script | Label |
| --- | --- |
| `stop`, `quit`, `end`, `revoke`, `opt out`, `cancel`, `unsubscribe` | `standardized` |
| `stop all` | `revoke_all` |
| `stop the payment reminders but keep fraud alerts` | `keep_fraud` |
| `please don't call me anymore`, `stop bothering me` | `ordinary_language` |
| empty string | `silence` |
| `thanks` | `not_revocation` |
| any other string | `unclassified` |

These labels are not a reasonable-person finding under 47 CFR 64.1200. No automatic speech recognizer and no language model assigned them.

## What each case constructs

`results/report.txt` is the fixture's own stdout from `reproduce.py`, with a limitations header. The paragraphs below describe the code path. They do not add results the script did not compute.

1. `recognition_without_write`. `recognize("stop")` returns `standardized`. The store is empty. `decide_send` on a pending informational message returns `sent`. The acknowledgement in the assertion is the label comparison. Nothing writes the store.

2. `write_cancels_local_and_suppresses_later`. `apply_scope` is called with `narrow_default` false, so `stop` writes category `*`. `cancel_controlled` cancels the message whose `in_caller_control` flag is true and leaves the message whose flag is false in state `pending`. A later informational message is `suppressed`.

3. `confirmation_once_then_suppress`. One pending message of kind `confirmation` is sent while the store blocks the number. Two later informational messages are suppressed. The case does not construct a second confirmation, so it does not show that a second confirmation would be refused.

4. `scope_follows_policy_not_the_word_stop`. With `narrow_default` true, `stop` writes the prompted category `payment`. The payment message is suppressed and the fraud message is sent. On a second store, `stop all` writes `*`, and the fraud message is suppressed. The string `stop` does not contain the category. The write uses `narrow_default` and `prompted_category`.

5. `exclusive_means_label_does_not_write`. `please don't call me anymore` is labeled `ordinary_language`. The case writes only when the label is `standardized`, so it does not write. The queued informational message is sent. This is a branch in the fixture. It is not a finding that any caller refused a revocation.

6. `silence_writes_only_if_a_policy_says_so`. `recognize("")` returns `silence`, and that path does not write. A different `Store` is then revoked by a direct call, `revoke(number, caller, "*")`, which does not receive the empty string. That second store blocks a fraud message. The printed detail `forced_policy_blocks_fraud` is the literal `True` inside the script. The assertion itself calls `blocks`.

7. `number_scope_is_not_account_scope`. A store revoked for `+15550001` does not block `+15550002`. A store revoked for both numbers does. The case does not contain an account object. The two stores are two sets of number keys.

8. `affiliate_follows_stored_caller_key`. A write for `Card Division` suppresses a Card Division message and does not suppress a Retail Bank message. A store revoked for both names suppresses the Retail Bank message. The names are strings chosen in the case.

9. `send_time_reread_not_schedule_time_clearance`. After `unsubscribe` is written with `narrow_default` false, a message with `cleared_at_schedule` true is sent when `reread` is false and suppressed when `reread` is true. The clearance flag is set by the case. It is not a timestamp from a scheduler.

## What this fixture can support in a comment

The comment may use the fixture for one point: the label, the permission write, the local cancellation flag, and the later send decision are separate operations, and a rule that names only the outcome "honored" does not say which of them has occurred. The same point can be stated without the fixture. The fixture is an illustration of that separation on objects this repository created.

## What this fixture cannot support

- How any named carrier, vendor, dialer, or campaign product behaves, or how often any of these splits occur.
- Whether a consumer's words were a revocation, or whether a method was reasonable.
- How speech recognition or a language model labels speech, noise, or paraphrase.
- What a provider does after it accepts a message. The handed-off object only stays pending because the local function skips it.
- Whether seven or ten business days is enough time, or what either period costs. The script has no clock and no cost.
- What a person intended by saying nothing. The silence case shows a store that was not written and a second store that was written by a direct call.
- That the sentences in `COMMENT.md` are the least burdensome choice under the Regulatory Flexibility Act.
