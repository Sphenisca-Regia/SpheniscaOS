#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
"""Check or add the SPDX licence line at the top of every first-party source file.

    python3 scripts/spdx.py --check    # exit 1 and list files whose line is missing or wrong
    python3 scripts/spdx.py --write    # add missing lines (never rewrites a different existing id)

First-party code is MPL-2.0. Files ported from GPL projects keep GPL-3.0-or-later (EXCEPTIONS below,
also listed in THIRD_PARTY_NOTICES.md). xx-keyboard/ is a fork of Stevia and keeps its own headers.
Covered: .py .rs .sh .js .css and extensionless scripts with a python or sh shebang, as tracked by git.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = "MPL-2.0"
EXCEPTIONS = {
    "common/xx_phone/mmi.py": "GPL-3.0-or-later",  # ported from GNOME Calls
}
SKIP_PREFIXES = ("xx-keyboard/",)
HASH = {".py", ".sh"}
SLASH = {".rs", ".js"}
BLOCK = {".css"}
TAG = "SPDX-License-Identifier:"


def style(path: Path, first: str) -> str | None:
    ext = path.suffix
    if ext in HASH:
        return "hash"
    if ext in SLASH:
        return "slash"
    if ext in BLOCK:
        return "block"
    if ext == "" and first.startswith("#!") and any(s in first for s in ("python", "sh")):
        return "hash"
    return None


def line_for(kind: str, licence: str) -> str:
    if kind == "hash":
        return f"# {TAG} {licence}"
    if kind == "slash":
        return f"// {TAG} {licence}"
    return f"/* {TAG} {licence} */"


def tracked() -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [p for p in out.splitlines() if not p.startswith(SKIP_PREFIXES)]


def main(argv: list[str]) -> int:
    write = "--write" in argv
    bad: list[str] = []
    added = 0
    for rel in tracked():
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lines = text.splitlines(keepends=True)
        first = lines[0] if lines else ""
        kind = style(path, first)
        if kind is None:
            continue
        want = EXCEPTIONS.get(rel, DEFAULT)
        head = "".join(lines[:5])
        if TAG in head:
            found = head.split(TAG, 1)[1].split()[0].rstrip("*/").strip()
            if found != want:
                bad.append(f"{rel}: has {found}, expected {want}")
            continue
        if not write:
            bad.append(f"{rel}: missing SPDX line ({want})")
            continue
        at = 0
        if first.startswith("#!"):
            at = 1
            if len(lines) > 1 and "coding" in lines[1] and lines[1].startswith("#"):
                at = 2
        newline = "\n" if not lines or lines[0].endswith("\n") or len(lines) > 1 else "\n"
        lines.insert(at, line_for(kind, want) + newline)
        path.write_text("".join(lines), encoding="utf-8")
        added += 1
    if write:
        print(f"spdx: added {added} line(s)")
    for b in bad:
        print(b)
    if bad:
        print(f"spdx: {len(bad)} file(s) need attention; run python3 scripts/spdx.py --write")
        return 1
    if not write:
        print("spdx: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
