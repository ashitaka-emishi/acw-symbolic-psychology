from __future__ import annotations

import sys

from _pipeline_common import ROOT, load_json


REQUIRED_FIELDS = [
    "annotation_id",
    "segment_id",
    "metaphor_present",
    "source_domain",
    "target_domain",
    "cluster",
    "magical_object",
    "violence_logic",
    "action_orientation",
    "confidence",
    "uncertainty_notes",
]


def main() -> int:
    files = sorted((ROOT / "data" / "annotated").glob("*/*.json"))
    if not files:
        print("No annotation files found yet.")
        return 0

    errors: list[str] = []
    for path in files:
        data = load_json(path)
        rows = data if isinstance(data, list) else [data]
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                errors.append(f"{path}: row {index} must be an object")
                continue
            for field in REQUIRED_FIELDS:
                if field not in row:
                    errors.append(f"{path}: row {index} missing `{field}`")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} annotation file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

