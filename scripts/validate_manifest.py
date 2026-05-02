from __future__ import annotations

import sys
from pathlib import Path

from _pipeline_common import PERSONS, ROOT, load_json, require_fields


REQUIRED_FIELDS = [
    "document_id",
    "actor_id",
    "title",
    "short_title",
    "date",
    "date_precision",
    "phase",
    "register",
    "genre",
    "authorship",
    "authorship_confidence",
    "source_repository",
    "source_url",
    "source_citation",
    "transcription_status",
    "risk_flags",
    "inclusion_rationale",
    "analytical_priority",
    "expected_cluster_priors",
    "notes",
]


def validate_file(path: Path, actor_id: str) -> list[str]:
    errors: list[str] = []
    data = load_json(path)
    if not isinstance(data, list):
        return [f"{path}: manifest must be a JSON array"]

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"{path}: item {index} must be an object")
            continue
        errors.extend(require_fields(item, REQUIRED_FIELDS, path))
        if item.get("actor_id") != actor_id:
            errors.append(f"{path}: item {index} actor_id must be `{actor_id}`")
    return errors


def main() -> int:
    errors: list[str] = []
    for actor_id in PERSONS:
        manifest = ROOT / "persons" / actor_id / "corpus_manifest.json"
        if not manifest.exists():
            errors.append(f"{manifest}: missing manifest")
            continue
        errors.extend(validate_file(manifest, actor_id))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("All corpus manifests are structurally valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

