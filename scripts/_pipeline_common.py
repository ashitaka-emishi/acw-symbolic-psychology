from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERSONS = [
    "lincoln",
    "douglass",
    "davis",
    "stephens",
    "brown",
    "lee",
    "jackson",
    "longstreet",
    "grant",
    "mcclellan",
    "sherman",
    "whitman",
]
GROUPS = [
    "union_political",
    "union_military",
    "abolitionist_prophetic",
    "confederate_political",
    "confederate_military",
    "literary_cultural_witness",
]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def require_fields(item: dict[str, object], fields: list[str], source: Path) -> list[str]:
    return [f"{source}: missing `{field}`" for field in fields if field not in item]


def placeholder(stage: str) -> None:
    print(f"{stage}: scaffolded entry point; populate data before production use.")

