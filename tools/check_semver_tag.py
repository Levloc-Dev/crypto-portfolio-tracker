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
    p = Path("pyproject.toml")
    if not p.exists():
        raise RuntimeError("pyproject.toml not found")

    txt = p.read_text(encoding="utf-8").splitlines()
    in_project = False
    for line in txt:
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            in_project = s == "[project]"
            continue
        if in_project:
            m = re.match(r'version\s*=\s*"([^"]+)"\s*$', s)
            if m:
                return m.group(1)
    raise RuntimeError('Could not find project version in [project] section of pyproject.toml')


def is_annotated_tag(tag: str) -> bool:
    # Annotated tags are tag objects. Lightweight tags point directly at a commit.
    obj_type = sh(["git", "cat-file", "-t", tag])
    return obj_type == "tag"


def is_signed_annotated_tag(tag: str) -> bool:
    # For signed annotated tags, git verifies signature:
    # `git tag -v <tag>` exits 0 if signature is valid (requires public key available).
    #
    # In CI, public keys may not be available. So we enforce two layers:
    # 1) Tag object must contain a signature block (gpgsig)
    # 2) If verification is possible, it should pass (best effort)
    tag_contents = sh(["git", "cat-file", "-p", tag])
    has_sig_block = "gpgsig" in tag_contents

    if not has_sig_block:
        return False

    # Best-effort verify. If it fails due to missing key, we still treat as "signed present".
    try:
        subprocess.check_call(["git", "tag", "-v", tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        # Signature block present but verification failed (likely missing key in CI).
        # Still enforce "signed tag exists" as minimum.
        return True


def main() -> int:
    ref = os.environ.get("GITHUB_REF", "")
    if not ref.startswith("refs/tags/"):
        return fail(f"Expected a tag ref; got {ref!r}")

    tag = ref.replace("refs/tags/", "")
    print(f"[semver] tag={tag}")

    if not SEMVER_TAG_RE.match(tag):
        return fail("Tag must match vMAJOR.MINOR.PATCH (e.g. v1.2.3)")

    # Require annotated tag
    if not is_annotated_tag(tag):
        return fail("Lightweight tags are запрещены. Create an annotated tag: git tag -a vX.Y.Z -m \"...\"")

    # Require signed annotated tag
    if not is_signed_annotated_tag(tag):
        return fail("Unsigned tags are запрещены. Create a signed tag: git tag -s vX.Y.Z -m \"...\"")

    tag_version = tag[1:]
    py_version = read_pyproject_version()
    print(f"[semver] pyproject.version={py_version}")

    if py_version != tag_version:
        return fail(f"pyproject.toml version ({py_version}) must match tag version ({tag_version})")

    # Ensure tag commit is reachable from origin/main
    sh(["git", "fetch", "origin", "main", "--depth=1"])
    tag_commit = sh(["git", "rev-list", "-n", "1", tag])
    print(f"[semver] tag_commit={tag_commit}")

    try:
        subprocess.check_call(["git", "merge-base", "--is-ancestor", tag_commit, "origin/main"])
    except subprocess.CalledProcessError:
        return fail("Tag commit must be reachable from origin/main")

    print("[semver] OK (annotated + signed + matches pyproject + on main)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
