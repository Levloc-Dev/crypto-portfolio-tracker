#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


def main() -> int:
    schemas_dir = Path("schemas")
    if not schemas_dir.exists():
        print("[validate_schemas] schemas/ does not exist; nothing to validate.")
        return 0

    schema_files = sorted(p for p in schemas_dir.glob("*.schema.json"))
    if not schema_files:
        print("[validate_schemas] No *.schema.json files found; skipping.")
        return 0

    for fp in schema_files:
        data = json.loads(fp.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(data)
        print(f"[validate_schemas] OK: {fp}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
