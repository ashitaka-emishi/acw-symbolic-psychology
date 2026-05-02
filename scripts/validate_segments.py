from __future__ import annotations

import sys
from pathlib import Path

from _pipeline_common import ROOT, load_json


def validate_segment_file(path: Path) -> list[str]:
    errors: list[str] = []
    data = load_json(path)
    if not isinstance(data, dict):
        return [f"{path}: segmented document must be an object"]
    for field in ["document_id", "actor_id", "segments"]:
        if field not in data:
            errors.append(f"{path}: missing `{field}`")
    if not isinstance(data.get("segments"), list):
        errors.append(f"{path}: `segments` must be an array")
    return errors


def main() -> int:
    files = sorted((ROOT / "data" / "segmented").glob("*/*.json"))
    if not files:
        print("No segmented documents found yet.")
        return 0
    errors = [error for path in files for error in validate_segment_file(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} segmented document(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

