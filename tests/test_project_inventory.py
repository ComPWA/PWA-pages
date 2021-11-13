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
def project_inventory() -> ProjectInventory:
    this_dir = Path(__file__).parent
    inventory_path = this_dir / "../docs/software/framework-inventory.yml"
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
    assert _checkmark_language(project, "c++") == "✓"
    assert _checkmark_language(project, "Python") == ""


@pytest.mark.parametrize("fix_alignment", [False, True])
def test_to_html_table(project_inventory, fix_alignment):
    src = to_html_table(
        project_inventory, selected_languages=["C++", "Python"]
    )
    if fix_alignment:
        src = fix_html_alignment(src)
    # cspell: ignore thead
    assert src.startswith("<table>")
    assert src.count("<thead>") == 1
    assert src.count("<tr>") == __MAX_PROJECTS + 1
