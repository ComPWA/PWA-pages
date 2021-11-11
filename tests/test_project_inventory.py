# pylint: disable=no-self-use, redefined-outer-name
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
    export_json_schema,
    fix_html_alignment,
    load_yaml,
    to_html_table,
)

__MAX_PROJECTS = 3


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
        with pytest.raises(
            ValidationError, match=r"No collaboration defined for SSC"
        ):
            ProjectInventory(**config)


@pytest.fixture(scope="session")
def this_dir() -> Path:
    return Path(__file__).parent


@pytest.fixture(scope="session")
def docs_dir(this_dir) -> Path:
    return this_dir / "../docs"


@pytest.fixture(scope="session")
def project_inventory(docs_dir: Path) -> ProjectInventory:
    inventory_path = docs_dir / "software/framework-inventory.yml"
    inventory_dict = load_yaml(inventory_path)
    inventory_dict["projects"] = inventory_dict["projects"][:__MAX_PROJECTS]
    return ProjectInventory(**inventory_dict)


def test_load_project_inventory(project_inventory: ProjectInventory):
    inventory = project_inventory
    assert len(inventory.projects) == __MAX_PROJECTS
    assert inventory.projects[0].name == "AmpGen"
    assert "BESIII" in inventory.collaborations
    assert inventory.collaborations["BESIII"] == "http://bes3.ihep.ac.cn"


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
        == '<a href="url">name</a>'
        + '<li><a href="url">sub1</a>'
        + '<li><a href="url">sub2</a>'
    )


def test_checkmark_language():
    project = Project(name="name", url="url", languages=["C++"])
    assert _checkmark_language(project, "c++", min_percentage=0) == "✓"
    assert _checkmark_language(project, "Python", min_percentage=0) == ""


@pytest.mark.parametrize("fix_alignment", [False, True])
@pytest.mark.parametrize("fetch_languages", [True, False])
def test_to_html_table(project_inventory, fetch_languages, fix_alignment):
    src = to_html_table(
        project_inventory,
        selected_languages=["C++", "Python"],
        fetch_languages=fetch_languages,
    )
    if fix_alignment:
        src = fix_html_alignment(src)
    # cspell: ignore thead
    assert src.startswith("<table>")
    assert src.count("<thead>") == 1
    assert src.count("<tr>") == __MAX_PROJECTS + 1


def test_export_export_json_schema(this_dir, docs_dir):
    output_path = str(this_dir / "exported-schema.json")
    assert export_json_schema([output_path]) == 0
    with open(output_path) as stream:
        exported = stream.read()
    with open(docs_dir / "software/project-inventory-schema.json") as stream:
        existing = stream.read()
    assert exported == existing


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        (
            "https://github.com/ComPWA/PWA-Pages",
            ["Python", "JavaScript"],
        ),
        (
            "https://github.com/ComPWA/ComPWA/blob/master/README.md",
            ["C++", "CMake"],
        ),
        ("https://qrules.rtfd.io", []),
    ],
)
def test_fetch_languages(url, expected):
    languages = _fetch_languages(url, min_percentage=2.5)
    assert languages == expected
