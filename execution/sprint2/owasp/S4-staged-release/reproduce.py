#!/usr/bin/env python3
"""A staged payment stays releasable after the principal's role is removed.

Encodes the staged-commit bullet and the session-revocation sentence as read
at AI Exchange commit bde8cc6f. No model is called.
"""


class Pending:
    def __init__(self):
        self.frozen = False
        self.released = False


def current_rules(principal_authorized, session_alive, pending):
    """What the current sentences require. They do not inspect the principal
    at release. Ending the session does not freeze the object."""
    if not session_alive:
        pass
    if principal_authorized or not principal_authorized:
        pending.released = True
    return pending


def proposed(principal_authorized, pending):
    if not principal_authorized:
        pending.frozen = True
        pending.released = False
    else:
        pending.released = True
    return pending


def main():
    now = current_rules(False, False, Pending())
    assert now.released is True and now.frozen is False
    later = proposed(False, Pending())
    assert later.released is False and later.frozen is True
    print("commit: bde8cc6f17a8f14107bd8eb962c13216bd8b5ccb")
    print("current_releases_after_role_removed: true")
    print("proposed_freezes: true")
    print("result: pass")


if __name__ == "__main__":
    main()
