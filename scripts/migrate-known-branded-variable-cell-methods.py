"""Normalize known-branded-variable ``cell_methods`` values to lists."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--collection-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "known_branded_variable",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite affected entries. Without this option, only report the count.",
    )
    return parser.parse_args()


def load_changes(collection_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    changes = []
    for path in sorted(collection_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        value = payload.get("cell_methods")
        if value is None or isinstance(value, list):
            continue
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Invalid cell_methods value in {path}: {value!r}")
        payload["cell_methods"] = [value]
        changes.append((path, payload))
    return changes


def main() -> None:
    args = parse_args()
    changes = load_changes(args.collection_dir)
    if args.write:
        for path, payload in changes:
            path.write_text(
                json.dumps(payload, indent=4, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        print(f"Updated {len(changes)} known branded variable entries.")
    else:
        print(f"Would update {len(changes)} known branded variable entries; use --write to apply.")


if __name__ == "__main__":
    main()
