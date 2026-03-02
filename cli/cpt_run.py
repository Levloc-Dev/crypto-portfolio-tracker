#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CPT_ENGINE_VERSION = "0.1.0"
TAX_ENGINE_VERSION = "0.1.0"
PRICING_ENGINE_VERSION = "0.1.0"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def stable_json(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


@dataclass(frozen=True)
class RunManifest:
    created_at_utc: str
    run_id: str
    command: str
    args: dict[str, Any]
    engine_versions: dict[str, str]
    input_hash: str
    output_hash: str


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def make_run_dir(date_str: str, run_id: str) -> Path:
    root = Path("runs") / date_str / f"run-{run_id}"
    ensure_dir(root / "inputs")
    ensure_dir(root / "outputs")
    return root


def compute_run_id(command: str, args: dict[str, Any]) -> str:
    # Deterministic run id from command+args+engine versions (not from wall time)
    payload = {
        "command": command,
        "args": args,
        "versions": {
            "cpt": CPT_ENGINE_VERSION,
            "pricing": PRICING_ENGINE_VERSION,
            "tax": TAX_ENGINE_VERSION,
        },
    }
    return sha256_bytes(stable_json(payload))[:12]


def cmd_ping(ns: argparse.Namespace) -> int:
    args = {"message": ns.message}
    run_id = compute_run_id("ping", args)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run_dir = make_run_dir(date_str, run_id)

    # inputs
    write_json(run_dir / "inputs" / "args.json", args)

    # outputs (example)
    output = {"ok": True, "message": ns.message, "timestamp_utc": utc_now_iso()}
    write_json(run_dir / "outputs" / "ping.json", output)

    input_hash = sha256_bytes(stable_json(args))
    output_hash = sha256_bytes(stable_json(output))

    manifest = RunManifest(
        created_at_utc=utc_now_iso(),
        run_id=run_id,
        command="ping",
        args=args,
        engine_versions={
            "cpt": CPT_ENGINE_VERSION,
            "pricing": PRICING_ENGINE_VERSION,
            "tax": TAX_ENGINE_VERSION,
        },
        input_hash=input_hash,
        output_hash=output_hash,
    )
    write_json(run_dir / "run.json", asdict(manifest))

    print(f"[cpt] run_id={run_id}")
    print(f"[cpt] wrote {run_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cpt_run.py", description="CPT CLI (deterministic, audit-ready)")
    sub = p.add_subparsers(dest="cmd", required=True)

    ping = sub.add_parser("ping", help="Create a deterministic run manifest (smoke test)")
    ping.add_argument("--message", default="hello", help="Message to echo into outputs")
    ping.set_defaults(func=cmd_ping)

    return p


def main() -> int:
    # Basic guard: ensure repo structure expectation
    if not Path("governance").exists():
        raise SystemExit("Expected to run from repo root (missing ./governance).")

    parser = build_parser()
    ns = parser.parse_args()
    return int(ns.func(ns))


if __name__ == "__main__":
    raise SystemExit(main())
