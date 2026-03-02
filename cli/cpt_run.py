#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


CPT_ENGINE_VERSION = "0.1.0"
NORMALIZATION_ENGINE_VERSION = "0.1.0"
PRICING_ENGINE_VERSION = "0.1.0"
TAX_ENGINE_VERSION = "0.1.0"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def stable_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n")


def compute_run_id(command: str, args: dict[str, Any], versions: dict[str, str]) -> str:
    payload = {"command": command, "args": args, "versions": versions}
    return sha256_bytes(stable_json_bytes(payload))[:12]


def make_run_dir(date_str: str, run_id: str) -> Path:
    root = Path("runs") / date_str / f"run-{run_id}"
    ensure_dir(root / "inputs")
    ensure_dir(root / "outputs")
    return root


@dataclass(frozen=True)
class RunManifest:
    created_at_utc: str
    run_id: str
    command: str
    args: dict[str, Any]
    engine_versions: dict[str, str]
    input_hash: str
    output_hash: str
    outputs: dict[str, str]  # logical name -> relative path


def write_manifest(run_dir: Path, manifest: RunManifest) -> None:
    write_json(run_dir / "run.json", asdict(manifest))


def cmd_ping(ns: argparse.Namespace) -> int:
    args = {"message": ns.message}
    versions = {
        "cpt": CPT_ENGINE_VERSION,
        "normalization": NORMALIZATION_ENGINE_VERSION,
        "pricing": PRICING_ENGINE_VERSION,
        "tax": TAX_ENGINE_VERSION,
    }
    run_id = compute_run_id("ping", args, versions)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run_dir = make_run_dir(date_str, run_id)

    write_json(run_dir / "inputs" / "args.json", args)

    output = {"ok": True, "message": ns.message, "timestamp_utc": utc_now_iso()}
    out_rel = Path("outputs") / "ping.json"
    write_json(run_dir / out_rel, output)

    manifest = RunManifest(
        created_at_utc=utc_now_iso(),
        run_id=run_id,
        command="ping",
        args=args,
        engine_versions=versions,
        input_hash=sha256_bytes(stable_json_bytes(args)),
        output_hash=sha256_bytes(stable_json_bytes(output)),
        outputs={"ping": str(out_rel)},
    )
    write_manifest(run_dir, manifest)

    print(f"[cpt] run_id={run_id}")
    print(f"[cpt] wrote {run_dir}")
    return 0


def cmd_ingest(ns: argparse.Namespace) -> int:
    """
    Minimal deterministic ingest:
    - creates a raw JSONL file containing 1 record with declared metadata
    - later: replace with real chain ingestion adapters
    """
    date_str = ns.date
    wallet = ns.wallet
    chain = ns.chain
    source = ns.source

    args = {"date": date_str, "wallet": wallet, "chain": chain, "source": source}
    versions = {
        "cpt": CPT_ENGINE_VERSION,
        "normalization": NORMALIZATION_ENGINE_VERSION,
        "pricing": PRICING_ENGINE_VERSION,
        "tax": TAX_ENGINE_VERSION,
    }
    run_id = compute_run_id("ingest", args, versions)
    run_dir = make_run_dir(date_str, run_id)

    # input args
    write_json(run_dir / "inputs" / "args.json", args)

    # output raw
    out_dir = Path("data") / "raw" / date_str
    ensure_dir(out_dir)
    out_file = out_dir / f"{wallet}_{chain}.jsonl"

    record = {
        "source": source,
        "chain": chain,
        "wallet": wallet,
        "tx_hash": ns.tx_hash,
        "timestamp_utc": ns.timestamp_utc,
    }
    write_jsonl(out_file, [record])

    # manifest output hash includes the produced file bytes
    out_bytes = out_file.read_bytes()
    manifest = RunManifest(
        created_at_utc=utc_now_iso(),
        run_id=run_id,
        command="ingest",
        args=args,
        engine_versions=versions,
        input_hash=sha256_bytes(stable_json_bytes(args)),
        output_hash=sha256_bytes(out_bytes),
        outputs={"raw_jsonl": str(out_file)},
    )
    write_manifest(run_dir, manifest)

    print(f"[cpt] run_id={run_id}")
    print(f"[cpt] wrote {out_file}")
    print(f"[cpt] wrote {run_dir/'run.json'}")
    return 0


def cmd_normalize(ns: argparse.Namespace) -> int:
    """
    Minimal deterministic normalize:
    - reads all raw JSONL files for date
    - emits normalized events JSONL with a simple mapping
    """
    date_str = ns.date
    raw_dir = Path("data") / "raw" / date_str
    if not raw_dir.exists():
        raise SystemExit(f"No raw data found for date={date_str} at {raw_dir}")

    args = {"date": date_str}
    versions = {
        "cpt": CPT_ENGINE_VERSION,
        "normalization": NORMALIZATION_ENGINE_VERSION,
        "pricing": PRICING_ENGINE_VERSION,
        "tax": TAX_ENGINE_VERSION,
    }
    run_id = compute_run_id("normalize", args, versions)
    run_dir = make_run_dir(date_str, run_id)

    write_json(run_dir / "inputs" / "args.json", args)

    normalized_rows: list[dict[str, Any]] = []
    for fp in sorted(raw_dir.glob("*.jsonl")):
        for row in read_jsonl(fp):
            normalized_rows.append(
                {
                    "event_type": "RAW_TX",
                    "chain": row.get("chain"),
                    "wallet": row.get("wallet"),
                    "timestamp_utc": row.get("timestamp_utc"),
                    "source": row.get("source"),
                    "tx_hash": row.get("tx_hash"),
                }
            )

    out_dir = Path("data") / "normalized" / date_str
    ensure_dir(out_dir)
    out_file = out_dir / "normalized.jsonl"
    write_jsonl(out_file, normalized_rows)

    out_bytes = out_file.read_bytes()
    manifest = RunManifest(
        created_at_utc=utc_now_iso(),
        run_id=run_id,
        command="normalize",
        args=args,
        engine_versions=versions,
        input_hash=sha256_bytes(stable_json_bytes(args)),
        output_hash=sha256_bytes(out_bytes),
        outputs={"normalized_jsonl": str(out_file)},
    )
    write_manifest(run_dir, manifest)

    print(f"[cpt] run_id={run_id}")
    print(f"[cpt] wrote {out_file}")
    print(f"[cpt] wrote {run_dir/'run.json'}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cpt_run.py", description="CPT CLI (deterministic, audit-ready)")
    sub = p.add_subparsers(dest="cmd", required=True)

    ping = sub.add_parser("ping", help="Create a deterministic run manifest (smoke test)")
    ping.add_argument("--message", default="hello", help="Message to echo into outputs")
    ping.set_defaults(func=cmd_ping)

    ing = sub.add_parser("ingest", help="Write a minimal raw JSONL record (bootstrap ingest)")
    ing.add_argument("--date", required=True, help="YYYY-MM-DD (UTC)")
    ing.add_argument("--wallet", required=True, help="Wallet address or label")
    ing.add_argument("--chain", required=True, help="Chain identifier (e.g., avalanche)")
    ing.add_argument("--source", default="manual-bootstrap", help="Ingestion source identifier")
    ing.add_argument("--tx-hash", dest="tx_hash", default="0xBOOTSTRAP", help="Transaction hash (placeholder)")
    ing.add_argument(
        "--timestamp-utc",
        dest="timestamp_utc",
        default=utc_now_iso(),
        help="Timestamp in UTC ISO format (default: now)",
    )
    ing.set_defaults(func=cmd_ingest)

    norm = sub.add_parser("normalize", help="Normalize raw JSONL into deterministic events JSONL")
    norm.add_argument("--date", required=True, help="YYYY-MM-DD (UTC)")
    norm.set_defaults(func=cmd_normalize)

    return p


def main() -> int:
    if not Path("governance").exists():
        raise SystemExit("Expected to run from repo root (missing ./governance).")

    ns = build_parser().parse_args()
    return int(ns.func(ns))


if __name__ == "__main__":
    raise SystemExit(main())
