#!/usr/bin/env python3
"""One delegated write has two conforming answers under the current 9.5.7.

AISVS main abcb870, row 9.5.7. No model is called.
"""


def delegation_time(child_action, authority_at_delegation):
    return child_action in authority_at_delegation


def execution_time(child_action, authority_at_execution):
    return child_action in authority_at_execution


def main():
    at_delegation = {"read", "write"}
    at_execution = {"read"}
    action = "write"
    first = delegation_time(action, at_delegation)
    second = execution_time(action, at_execution)
    assert first is True
    assert second is False
    print("commit: abcb87056c2a39ae04422abef90c278f43cb4ac8")
    print("row: 9.5.7")
    print("action:", action)
    print("delegation_time_passes:", first)
    print("execution_time_passes:", second)
    print("result: pass")


if __name__ == "__main__":
    main()
