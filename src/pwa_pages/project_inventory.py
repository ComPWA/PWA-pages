# pylint: disable=no-name-in-module, no-self-argument, no-self-use
"""Helper tools for writing tables."""

from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple, Union

import yaml
from pydantic import BaseModel, root_validator
from pytablewriter import HtmlTableWriter


def load_yaml(path: Union[Path, str]) -> dict:
    with open(path) as stream:
        return yaml.load(stream, Loader=yaml.SafeLoader)


def to_html_table(
    inventory: "ProjectInventory", selected_languages: List[str]
) -> str:
    def create_row(project: "Project") -> Tuple[str, ...]:
        language_checkmarks = [
            _checkmark_language(project, language)
            for language in selected_languages
        ]
        return (
            _create_project_entry(project),
            _format_collaboration(project, inventory),
            *language_checkmarks,
        )

    writer = HtmlTableWriter(
        headers=["Project", "Collaboration", *selected_languages],
        value_matrix=map(create_row, inventory.projects),
    )
    return writer.dumps()


def fix_html_alignment(src: str) -> str:
    left_align_style = 'style="text-align:left; vertical-align:top"'
    center_align_style = 'style="text-align:center; vertical-align:top"'
    src = src.replace(
        '<td align="left">✓</td>', f"<td {center_align_style}>✓</td>"
    )
    src = src.replace('align="left"', left_align_style)
    src = src.replace("<th>", f"<th {left_align_style}>")
    return src


class SubProject(BaseModel):
    name: str
    url: str


class Project(BaseModel):
    name: str
    url: str
    collaboration: Optional[Union[List[str], str]] = None
    languages: List[str] = []
    sub_projects: Optional[List[SubProject]] = None


class ProjectInventory(BaseModel):
    projects: List[Project]
    collaborations: Dict[str, str]

    @root_validator()
    def _check_collaboration_exists(cls, values: dict) -> dict:  # noqa: N805
        defined_collaborations = set(values["collaborations"])
        project: Project
        for project in values["projects"]:
            if project.collaboration is None:
                continue
            if isinstance(project.collaboration, str):
                collaborations = [project.collaboration]
            else:
                collaborations = project.collaboration
            for collab in collaborations:
                if collab not in defined_collaborations:
                    raise ValueError(f"No collaboration defined for {collab}")
        return values


def _create_project_entry(project: Project) -> str:
    html = _form_html_link(name=project.name, url=project.url)
    if project.sub_projects is not None:
        sub_project_links = map(
            lambda s: _form_html_link(name=s.name, url=s.url),
            project.sub_projects,
        )
        enumerated_projects = _enumerate_html_links(list(sub_project_links))
        html += enumerated_projects
    return html


def _checkmark_language(project: Project, language: str) -> str:
    languages = set(map(lambda s: s.lower(), project.languages))
    if language.lower() in languages:
        return "✓"
    return ""


def _format_collaboration(
    project: Project, inventory: "ProjectInventory"
) -> str:
    collaborations = project.collaboration
    if collaborations is None:
        return ""
    if isinstance(collaborations, str):
        collaborations = [collaborations]
    collaborations_links = map(
        lambda c: _form_collaboration_link(inventory, c), collaborations
    )
    return " / ".join(collaborations_links)


def _form_collaboration_link(inventory: ProjectInventory, name: str) -> str:
    collaboration_url = inventory.collaborations.get(name)
    if collaboration_url is None:
        raise KeyError(f'Collaboration entry "{name}" not found')
    return _form_html_link(name=name, url=collaboration_url)


def _form_html_link(url: str, name: str) -> str:
    return f'<a href="{url}">{name}</a>'


def _enumerate_html_links(list_of_entries: Sequence[str]) -> str:
    if not list_of_entries:
        return ""
    if len(list_of_entries) == 1:
        return list_of_entries[0]
    html = "<li>".join(list_of_entries)
    html = "<li>" + html
    return html