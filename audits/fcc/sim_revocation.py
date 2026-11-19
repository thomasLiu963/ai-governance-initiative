"""Deterministic checks for revocation handling.

This script does not call a model. It compares a fixed rule with a
permission record, a local queue, and a later send decision.
"""

from __future__ import annotations

from dataclasses import dataclass, field


STANDARDIZED = (
    "stop",
    "quit",
    "end",
    "revoke",
    "opt out",
    "cancel",
    "unsubscribe",
)


@dataclass
class Message:
    mid: str
    number: str
    caller: str
    category: str
    kind: str
    in_caller_control: bool
    state: str = "pending"
    cleared_at_schedule: bool = False


@dataclass
class Store:
    """Permission rows. A missing row means the number is still allowed."""

    revoked: set[tuple[str, str, str]] = field(default_factory=set)

    def revoke(self, number: str, caller: str, category: str) -> None:
        self.revoked.add((number, caller, category))

    def blocks(self, number: str, caller: str, category: str) -> bool:
        return (number, caller, category) in self.revoked or (
            number,
            caller,
            "*",
        ) in self.revoked


def recognize(text: str) -> str:
    """Return a label only. This function does not change permission state."""
    normalized = " ".join(text.lower().strip().split())
    if normalized == "":
        return "silence"
    if normalized in STANDARDIZED:
        return "standardized"
    if normalized == "stop all":
        return "revoke_all"
    if normalized == "stop the payment reminders but keep fraud alerts":
        return "keep_fraud"
    if normalized in {"please don't call me anymore", "stop bothering me"}:
        return "ordinary_language"
    if normalized == "thanks":
        return "not_revocation"
    return "unclassified"


def apply_scope(
    store: Store,
    number: str,
    caller: str,
    prompted_category: str,
    label: str,
    *,
    narrow_default: bool,
) -> str:
    """Write a scope chosen by an explicit policy. Return the scope name."""
    if label == "silence" or label == "not_revocation" or label == "unclassified":
        return "none"
    if label == "revoke_all":
        store.revoke(number, caller, "*")
        return "all"
    if label == "keep_fraud":
        store.revoke(number, caller, "payment")
        return "payment_only"
    if label in {"standardized", "ordinary_language"}:
        if narrow_default:
            store.revoke(number, caller, prompted_category)
            return prompted_category
        store.revoke(number, caller, "*")
        return "all"
    return "none"


def cancel_controlled(queue: list[Message], store: Store) -> list[str]:
    cancelled = []
    for item in queue:
        if item.state != "pending":
            continue
        if not item.in_caller_control:
            continue
        if store.blocks(item.number, item.caller, item.category):
            item.state = "cancelled"
            cancelled.append(item.mid)
    return cancelled


def decide_send(item: Message, store: Store, *, reread: bool) -> str:
    if item.state == "cancelled":
        return "cancelled"
    allowed_then = item.cleared_at_schedule or not store.blocks(
        item.number, item.caller, item.category
    )
    allowed_now = not store.blocks(item.number, item.caller, item.category)
    allowed = allowed_now if reread else allowed_then
    if item.kind == "confirmation" and item.state == "pending":
        item.state = "sent"
        return "sent_confirmation"
    if allowed:
        item.state = "sent"
        return "sent"
    item.state = "suppressed"
    return "suppressed"


def run() -> list[dict[str, object]]:
    results = []

    def check(name: str, ok: bool, detail: dict[str, object]) -> None:
        results.append({"case": name, "passed": ok, **detail})

    # 1. Recognition and acknowledgement without a permission write.
    label = recognize("stop")
    store = Store()
    queued = Message(
        "q1",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    acknowledged = label == "standardized"
    sent = decide_send(queued, store, reread=True)
    check(
        "recognition_without_write",
        label == "standardized"
        and acknowledged
        and not store.blocks("+15550001", "Card Division", "payment")
        and sent == "sent",
        {"label": label, "store_blocks": False, "send": sent},
    )

    # 2. Write, cancel a message still in caller control, leave a handed-off message.
    store = Store()
    local = Message(
        "local",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    handed = Message(
        "handed",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        False,
    )
    scope = apply_scope(
        store,
        "+15550001",
        "Card Division",
        "payment",
        recognize("stop"),
        narrow_default=False,
    )
    cancelled = cancel_controlled([local, handed], store)
    later = Message(
        "later",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    later_result = decide_send(later, store, reread=True)
    check(
        "write_cancels_local_and_suppresses_later",
        scope == "all"
        and cancelled == ["local"]
        and handed.state == "pending"
        and later_result == "suppressed",
        {
            "scope": scope,
            "cancelled": cancelled,
            "handed_state": handed.state,
            "later": later_result,
        },
    )

    # 3. One confirmation can be sent. A second covered message cannot.
    store = Store()
    apply_scope(
        store,
        "+15550001",
        "Card Division",
        "payment",
        recognize("stop"),
        narrow_default=False,
    )
    confirmation = Message(
        "confirm",
        "+15550001",
        "Card Division",
        "payment",
        "confirmation",
        True,
    )
    follow = Message(
        "follow",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    follow_text = Message(
        "anything_else",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    check(
        "confirmation_once_then_suppress",
        decide_send(confirmation, store, reread=True) == "sent_confirmation"
        and decide_send(follow, store, reread=True) == "suppressed"
        and decide_send(follow_text, store, reread=True) == "suppressed",
        {
            "confirmation": confirmation.state,
            "follow": follow.state,
            "session_followup": follow_text.state,
        },
    )

    # 4. Category-limited policy and an explicit all-categories utterance.
    store = Store()
    apply_scope(
        store,
        "+15550001",
        "Card Division",
        "payment",
        recognize("stop"),
        narrow_default=True,
    )
    payment = Message(
        "pay",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    fraud = Message(
        "fraud",
        "+15550001",
        "Card Division",
        "fraud",
        "informational",
        True,
    )
    narrow_ok = (
        decide_send(payment, store, reread=True) == "suppressed"
        and decide_send(fraud, store, reread=True) == "sent"
    )
    store_all = Store()
    apply_scope(
        store_all,
        "+15550001",
        "Card Division",
        "payment",
        recognize("stop all"),
        narrow_default=True,
    )
    fraud_all = Message(
        "fraud2",
        "+15550001",
        "Card Division",
        "fraud",
        "informational",
        True,
    )
    check(
        "scope_follows_policy_not_the_word_stop",
        narrow_ok and decide_send(fraud_all, store_all, reread=True) == "suppressed",
        {"narrow_fraud_sent": fraud.state, "stop_all_fraud": fraud_all.state},
    )

    # 5. Exclusive keyword channel: ordinary language is labeled and not written.
    label = recognize("please don't call me anymore")
    store = Store()
    written = label == "standardized"
    if written:
        apply_scope(
            store,
            "+15550001",
            "Card Division",
            "payment",
            label,
            narrow_default=False,
        )
    queued = Message(
        "q5",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    check(
        "exclusive_means_label_does_not_write",
        label == "ordinary_language"
        and not written
        and decide_send(queued, store, reread=True) == "sent",
        {"label": label, "written": written, "send": queued.state},
    )

    # 6. Silence does not write. A different policy could, and the script shows that fork.
    store = Store()
    silence = recognize("")
    if silence != "silence":
        apply_scope(
            store,
            "+15550001",
            "Card Division",
            "payment",
            silence,
            narrow_default=False,
        )
    silence_blocks = store.blocks("+15550001", "Card Division", "payment")
    forced = Store()
    forced.revoke("+15550001", "Card Division", "*")
    check(
        "silence_writes_only_if_a_policy_says_so",
        silence == "silence"
        and not silence_blocks
        and forced.blocks("+15550001", "Card Division", "fraud"),
        {
            "default_blocks": silence_blocks,
            "forced_policy_blocks_fraud": True,
        },
    )

    # 7. Number key and account key are different writes.
    by_number = Store()
    by_number.revoke("+15550001", "Card Division", "*")
    by_account = Store()
    for number in ("+15550001", "+15550002"):
        by_account.revoke(number, "Card Division", "*")
    other = Message(
        "other",
        "+15550002",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    other_account = Message(
        "other2",
        "+15550002",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    check(
        "number_scope_is_not_account_scope",
        decide_send(other, by_number, reread=True) == "sent"
        and decide_send(other_account, by_account, reread=True) == "suppressed",
        {"number_policy": other.state, "account_policy": other_account.state},
    )

    # 8. Disclosed caller identity, with and without a listed affiliate.
    disclosed = Store()
    disclosed.revoke("+15550001", "Card Division", "*")
    card = Message(
        "card",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
    )
    retail = Message(
        "retail",
        "+15550001",
        "Retail Bank",
        "payment",
        "informational",
        True,
    )
    listed = Store()
    for caller in ("Card Division", "Retail Bank"):
        listed.revoke("+15550001", caller, "*")
    retail_listed = Message(
        "retail2",
        "+15550001",
        "Retail Bank",
        "payment",
        "informational",
        True,
    )
    check(
        "affiliate_follows_stored_caller_key",
        decide_send(card, disclosed, reread=True) == "suppressed"
        and decide_send(retail, disclosed, reread=True) == "sent"
        and decide_send(retail_listed, listed, reread=True) == "suppressed",
        {
            "same_caller": card.state,
            "unlisted_affiliate": retail.state,
            "listed_affiliate": retail_listed.state,
        },
    )

    # 9. A clearance cached before revocation is stale if the sender does not reread.
    store = Store()
    apply_scope(
        store,
        "+15550001",
        "Card Division",
        "payment",
        recognize("unsubscribe"),
        narrow_default=False,
    )
    stale = Message(
        "cached",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
        cleared_at_schedule=True,
    )
    fresh = Message(
        "fresh",
        "+15550001",
        "Card Division",
        "payment",
        "informational",
        True,
        cleared_at_schedule=True,
    )
    check(
        "send_time_reread_not_schedule_time_clearance",
        decide_send(stale, store, reread=False) == "sent"
        and decide_send(fresh, store, reread=True) == "suppressed",
        {"cached_clearance": stale.state, "reread": fresh.state},
    )

    return results


if __name__ == "__main__":
    rows = run()
    failed = [row["case"] for row in rows if not row["passed"]]
    for row in rows:
        print(f"{'PASS' if row['passed'] else 'FAIL'}\t{row['case']}\t{row}")
    print(f"cases={len(rows)} failed={len(failed)}")
