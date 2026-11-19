"""Reproduce the local revocation fixture and write a labeled report.

The fixture is audits/fcc/sim_revocation.py. This runner does not modify it,
does not call a model, and does not use the network.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SIM_PATH = ROOT / "audits" / "fcc" / "sim_revocation.py"
REPORT_PATH = Path(__file__).resolve().parent / "results" / "report.txt"

LIMITATIONS = """\
LIMITATIONS
This report is the output of a local specification fixture. Each case
constructs Python objects and checks them against assertions written in
audits/fcc/sim_revocation.py. A passing assertion means those objects
matched that case. It does not mean a carrier, a messaging provider, a
dialer, a handset, a campaign platform, or a person was observed.

The recognizer is an exact match on strings fixed in the script. It is
not a reasonable-person test and it is not a model. The script does not
call a network service or a paid API. The flag in_caller_control is set
by the case. It is not a report from a provider. The store key is the
called number, the caller name, and the category. The script has no
channel field. The detail field forced_policy_blocks_fraud is the
literal True in the script's report dictionary. The assertion for that
case calls blocks(); the printed literal is not a second measurement.

The empty string is labeled silence and does not change the store. The
blocking store in that case is a separate object revoked by a direct
function call. The empty string is not the input to that call. A
pending message whose kind is confirmation is sent even when the store
blocks the number. The confirmation case sends one such message. It
does not contain a second confirmation, so it does not show a one-message
limit.
"""


def main() -> int:
    if not SIM_PATH.is_file():
        print(f"missing fixture: {SIM_PATH}", file=sys.stderr)
        return 2
    digest = hashlib.sha256(SIM_PATH.read_bytes()).hexdigest()
    proc = subprocess.run(
        [sys.executable, str(SIM_PATH)],
        check=False,
        capture_output=True,
        text=True,
    )
    output = proc.stdout
    if proc.stderr:
        output += "\nstderr:\n" + proc.stderr
    failed_line = ""
    for line in proc.stdout.splitlines():
        if line.startswith("cases="):
            failed_line = line
            break
    failed = proc.returncode != 0 or "failed=0" not in failed_line
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        LIMITATIONS.rstrip(),
        "",
        f"utc={stamp}",
        f"python={sys.version.split()[0]}",
        f"command={sys.executable} {SIM_PATH}",
        f"sha256={digest}",
        f"fixture_exit={proc.returncode}",
        "",
        "FIXTURE STDOUT",
        output.rstrip(),
        "",
    ]
    text = "\n".join(lines) + "\n"
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
