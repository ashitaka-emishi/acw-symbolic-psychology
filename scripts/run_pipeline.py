from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_STEPS = [
    "validate_manifest.py",
    "validate_segments.py",
    "validate_annotations.py",
]


def main() -> int:
    for step in VALIDATION_STEPS:
        script = ROOT / "scripts" / step
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode != 0:
            return result.returncode
    print("Pipeline scaffold checks completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

