import json
from pathlib import Path

import pytest

from pwa_pages.inventory_data import collect_repo_urls, export_inventory_data
from pwa_pages.project_inventory import ProjectInventory, load_yaml
from pwa_pages.repo import is_repo_url


@pytest.fixture(scope="session")
def docs_dir() -> Path:
    return Path(__file__).parent / "../docs"


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://github.com/ComPWA/qrules", True),
        ("https://gitlab.cern.ch/bsm-fleet/Ipanema", True),
        ("https://gitlab.ep1.rub.de/pwa/Pawian", True),
        ("https://compwa.github.io", False),
        ("https://root.cern/manual/roofit", False),
        ("https://doi.org/10.1016/j.cpc.2018.04.017", False),
    ],
)
def test_is_repo_url(url: str, expected: bool):
    assert is_repo_url(url) is expected


def test_collect_repo_urls(docs_dir: Path):
    inventory_path = docs_dir / "software/amplitude-analysis-projects.yml"
    inventory = ProjectInventory(**load_yaml(inventory_path))
    urls = collect_repo_urls(inventory)
    assert urls == sorted(set(urls))
    assert "https://github.com/GooFit/AmpGen" in urls
    assert "https://github.com/ComPWA/qrules" in urls  # sub-project
    assert "https://compwa.github.io" not in urls  # not a repository


def test_inventory_json_is_valid(docs_dir: Path):
    with open(docs_dir / "software/inventory.json") as stream:
        data = json.load(stream)
    assert set(data) == {"generated", "repositories"}
    assert len(data["repositories"]) > 0
    for url, entry in data["repositories"].items():
        assert is_repo_url(url)
        assert set(entry) == {"latest_commit", "languages"}
        assert len(entry["latest_commit"]) == len("YYYY-MM-DD")


def test_export_inventory_data_without_repos(tmp_path: Path):
    """Exiting with a non-zero code prevents the workflow from committing junk."""
    inventory_path = tmp_path / "inventory.yml"
    inventory_path.write_text(
        "projects:\n  - name: RooFit\n    url: https://root.cern/manual/roofit\n"
    )
    output_path = tmp_path / "out.json"
    assert export_inventory_data([str(inventory_path), "-o", str(output_path)]) == 1
    assert not output_path.exists()
