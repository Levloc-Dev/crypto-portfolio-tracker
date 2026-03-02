#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


SEMVER_TAG_RE = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def sh(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


def read_pyproject_version() -> str:
    # Minimal parser: looks for `version = "X.Y.Z"` in [project]
    p = Path("pyproject.toml")
    if not p.exists():
        raise RuntimeError("pyproject.toml not found")

    txt = p.read_text(encoding="utf-8").splitlines()
    in_project = False
    for line in txt:
        line_stripped = line.strip()
        if line_stripped.startswith("[") and line_stripped.endswith("]"):
            in_project = line_stripped == "[project]"
            continue
        if in_project:
            m = re.match(r'version\s*=\s*"([^"]+)"\s*$', line_stripped)
            if m:
                return m.group(1)
    raise RuntimeError('Could not find project version in [project] section of pyproject.toml')


def main() -> int:
    ref = os.environ.get("GITHUB_REF", "")
    if not ref.startswith("refs/tags/"):
        return fail(f"Expected a tag ref; got {ref!r}")

    tag = ref.replace("refs/tags/", "")
    print(f"[semver] tag={tag}")

    if not SEMVER_TAG_RE.match(tag):
        return fail("Tag must match vMAJOR.MINOR.PATCH (e.g. v1.2.3)")

    tag_version = tag[1:]
    py_version = read_pyproject_version()
    print(f"[semver] pyproject.version={py_version}")

    if py_version != tag_version:
        return fail(f"pyproject.toml version ({py_version}) must match tag version ({tag_version})")

    # Ensure tag commit is reachable from origin/main
    # (prevents tagging a random detached commit not in main history)
    sh(["git", "fetch", "origin", "main", "--depth=1"])
    tag_commit = sh(["git", "rev-list", "-n", "1", tag])
    print(f"[semver] tag_commit={tag_commit}")

    try:
        # exit code 0 if tag_commit is ancestor of origin/main
        subprocess.check_call(["git", "merge-base", "--is-ancestor", tag_commit, "origin/main"])
    except subprocess.CalledProcessError:
        return fail("Tag commit must be reachable from origin/main")

    print("[semver] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
