import subprocess
import sys
from pathlib import Path

from acw_symbolic_psychology import __version__


ROOT = Path(__file__).resolve().parents[1]


def test_package_imports() -> None:
    assert __version__ == "0.1.0"


def test_scaffold_required_paths_exist() -> None:
    required_paths = [
        "docs/index.md",
        "methods/annotation_codebook.md",
        "schemas/corpus_manifest.schema.json",
        "config/shared_taxonomy.yaml",
        "scripts/run_pipeline.py",
        "persons/lincoln/corpus_manifest.json",
        "groups/union_military/group_profile.md",
        "analyses/comparative/symbolic_worlds.md",
    ]

    for path in required_paths:
        assert (ROOT / path).exists(), path


def test_manifest_validator_runs() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_manifest.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
