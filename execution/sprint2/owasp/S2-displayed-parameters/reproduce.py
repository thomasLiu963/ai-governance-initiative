#!/usr/bin/env python3
"""Level 2 can pass when the executed parameters differ from the displayed ones.

Rows are the C9.2 sentences at AISVS main abcb870. 9.2.8 is Level 3 and is
not part of a Level 2 assessment. No model is called.
"""

DISPLAYED = {"recipient": "alice", "amount": "10"}
EXECUTED = {"recipient": "bob", "amount": "10"}


def level2(displayed, executed, approval_received, display_complete):
    row_9_2_1 = approval_received
    row_9_2_2 = display_complete
    return {"9.2.1": row_9_2_1, "9.2.2": row_9_2_2}


def row_9_2_8(displayed, executed):
    return displayed == executed


def row_9_2_12(displayed, executed):
    return displayed == executed


def main():
    current = level2(DISPLAYED, EXECUTED, True, True)
    assert all(current.values()), current
    assert row_9_2_8(DISPLAYED, EXECUTED) is False
    assert row_9_2_12(DISPLAYED, EXECUTED) is False
    assert row_9_2_12(DISPLAYED, DISPLAYED) is True

    print("commit: abcb87056c2a39ae04422abef90c278f43cb4ac8")
    print("displayed:", DISPLAYED)
    print("executed:", EXECUTED)
    print("level2:", current)
    print("9.2.8_level3_passes:", False)
    print("proposed_9.2.12_passes:", False)
    print("result: pass")


if __name__ == "__main__":
    main()
