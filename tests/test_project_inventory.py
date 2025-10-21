# cspell:ignore subproject
from pathlib import Path
from textwrap import dedent

import pytest
import yaml
from pydantic import ValidationError

from pwa_pages.project_inventory import (
    Project,
    ProjectInventory,
    SubProject,
    _checkmark_language,
    _create_project_entry,
    _fetch_languages,
    _get_subproject_timestamps,
    export_json_schema,
    load_yaml,
    to_markdown_table,
)

__MAX_PROJECTS = 6


class TestProjectInventory:
    def test_collaboration_undefined(self):
        yaml_content = dedent(
            """
            projects:
              - name: MyProject
                url: "https://www.w3.org/Provider/Style/dummy.html"
                collaboration: SSC

            collaborations:
              CERN: "https://home.cern"
            """
        )
        config = yaml.safe_load(yaml_content)
        with pytest.raises(ValidationError, match=r"No collaboration defined for SSC"):
            ProjectInventory(**config)


@pytest.fixture(scope="session")
def this_dir() -> Path:
    return Path(__file__).parent


@pytest.fixture(scope="session")
def docs_dir(this_dir) -> Path:
    return this_dir / "../docs"


@pytest.fixture(scope="session")
def project_inventory(docs_dir: Path) -> ProjectInventory:
    inventory_path = docs_dir / "software/amplitude-analysis-projects.yml"
    inventory_dict = load_yaml(inventory_path)
    inventory_dict["projects"] = inventory_dict["projects"][:__MAX_PROJECTS]
    return ProjectInventory(**inventory_dict)


@pytest.fixture(scope="session")
def fitter_packages(docs_dir: Path) -> ProjectInventory:
    inventory_path = docs_dir / "software/fitter-packages.yml"
    inventory_dict = load_yaml(inventory_path)
    return ProjectInventory(**inventory_dict)


def test_load_project_inventory(project_inventory: ProjectInventory):
    inventory = project_inventory
    assert len(inventory.projects) == __MAX_PROJECTS
    assert inventory.projects[0].name == "AmpGen"
    assert "BESIII" in inventory.collaborations
    assert inventory.collaborations["BESIII"] == "http://bes3.ihep.ac.cn"


def test_load_fitter_packages(fitter_packages: ProjectInventory):
    assert len(fitter_packages.projects) > 1
    # cspell:words zfit
    assert "zfit" in {p.name for p in fitter_packages.projects}
    assert "GooFit" in {p.name for p in fitter_packages.projects}


def test_create_project_entry():
    project = Project(
        name="name",
        url="url",
        sub_projects=[
            SubProject(name="sub1", url="url"),
            SubProject(name="sub2", url="url"),
        ],
    )
    assert (
        _create_project_entry(project)
        == '<a href="url">name</a><li><a href="url">sub1</a><li><a href="url">sub2</a>'
    )


def test_checkmark_language():
    project = Project(name="name", url="url", languages=["C++"])
    assert _checkmark_language(project, "c++", min_percentage=0) == "✓"
    assert _checkmark_language(project, "Python", min_percentage=0) == ""  # noqa: PLC1901


@pytest.mark.parametrize("fetch", [False, True])
def test_to_markdown_table(project_inventory: ProjectInventory, fetch: bool):
    src = to_markdown_table(
        project_inventory,
        selected_languages=["C++", "Python"],
        fetch=fetch,
    )
    if fetch:
        assert "| 2020 |" in src
    # cspell: ignore thead
    assert src.startswith("| Project | Collaboration | Since | Latest commit |")
    assert src.count(" |\n") == __MAX_PROJECTS + 2


def test_to_markdown_table_hide_columns(fitter_packages):
    src = to_markdown_table(
        fitter_packages,
        selected_languages=["C++", "Python"],
        fetch=False,
        hide_columns=["Collaboration"],
    )
    assert src.startswith("| Project | Since | Latest commit | C++ | Python |")
    assert "Collaboration" not in src


def test_export_export_json_schema(this_dir, docs_dir):
    output_path = str(this_dir / "exported-schema.json")
    assert export_json_schema([output_path]) == 0
    with open(output_path) as stream:
        exported = stream.read()
    with open(docs_dir / "software/project-inventory-schema.json") as stream:
        existing = stream.read()
    assert exported == existing


@pytest.mark.parametrize(
    ("url", "first_language"),
    [
        ("https://gitlab.cern.ch/bsm-fleet/Ipanema", "C"),
        ("https://github.com/ComPWA/PWA-Pages", "Python"),
        ("https://github.com/ComPWA/ComPWA/blob/master/README.md", "C++"),
        ("https://qrules.rtfd.io", None),
    ],
)
def test_fetch_languages(url, first_language):
    project = Project(name="dummy", url=url)
    languages = _fetch_languages(project, min_percentage=2.5)
    if first_language is None:
        assert len(languages) == 0
    else:
        assert len(languages) > 0
        assert languages[0] == first_language


def test_get_subproject_timestamps(project_inventory: ProjectInventory):
    project_name = "ComPWA project"
    for project in project_inventory.projects:
        if project.name == project_name:
            timestamps = _get_subproject_timestamps(
                project, date_getter=lambda p: p.latest_commit
            )
            assert len(timestamps) == 3
            return
    msg = f"Project {project_name} not found"
    raise ValueError(msg)
