# pylint: disable=no-name-in-module, no-self-argument, no-self-use
"""Helper tools for writing tables."""

import argparse
import re
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Union

import yaml
from pydantic import BaseModel, root_validator
from pytablewriter import HtmlTableWriter

from .repo import Repo, get_repo


def load_yaml(path: Union[Path, str]) -> dict:
    with open(path) as stream:
        return yaml.load(stream, Loader=yaml.SafeLoader)


def to_html_table(
    inventory: "ProjectInventory",
    selected_languages: List[str],
    *,
    fetch: bool = False,
    min_percentage: float = 2.5,
    hide_columns: Optional[Iterable[str]] = None,
) -> str:
    header_to_formatters: Dict[str, Callable[[Project], str]] = {
        "Project": _create_project_entry,
        "Collaboration": partial(_format_collaboration, inventory=inventory),
        "Since": _fetch_first_commit_year if fetch else lambda _: "",
        "Lastest commit": _fetch_lastest_commit_date
        if fetch
        else lambda _: "",
    }
    for language in selected_languages:
        header_to_formatters[language] = partial(
            _checkmark_language,
            language=language,
            fetch=fetch,
            min_percentage=min_percentage,
        )
    if hide_columns is not None:
        for hide in hide_columns:
            del header_to_formatters[hide]

    writer = HtmlTableWriter(
        headers=list(header_to_formatters),
        value_matrix=[
            tuple(
                formatter(project)
                for formatter in header_to_formatters.values()
            )
            for project in inventory.projects
        ],
    )
    return writer.dumps()


def fix_html_alignment(src: str) -> str:
    left_align_style = 'style="text-align:left; vertical-align:top"'
    center_align_style = 'style="text-align:center; vertical-align:top"'
    src = src.replace(
        '<td align="left">✓</td>',
        f"<td {center_align_style}>✓</td>",
    )
    src = re.sub(
        r'<td align="right">([0-9]{4})</td>',
        fr"<td {center_align_style}>\1</td>",
        src,
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
    since: int = 0


class ProjectInventory(BaseModel):
    projects: List[Project]
    collaborations: Dict[str, str] = {}

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


def _checkmark_language(
    project: Project,
    language: str,
    *,
    fetch: bool = False,
    min_percentage: float,
) -> str:
    languages = project.languages
    if not languages and fetch:
        languages = _fetch_languages(project, min_percentage)
        if project.sub_projects is not None:
            for sub_project in project.sub_projects:
                sub_languages = _fetch_languages(sub_project, min_percentage)
                languages.extend(sub_languages)
    normalized_languages = map(
        lambda s: __replace_language(s).lower(), languages
    )
    if language.lower() in normalized_languages:
        return "✓"
    return ""


def __replace_language(language: str) -> str:
    replacements = {
        "C": "C++",
    }
    for old, new in replacements.items():
        if old.lower() == language.lower():
            return new
    return language


def _fetch_languages(
    project: Union[Project, SubProject], min_percentage: float
) -> List[str]:
    repo = get_repo(project.url)
    if repo is None:
        return []
    return repo.filter_languages(min_percentage)


def _fetch_lastest_commit_date(project: Project) -> str:
    return _get_date(
        project,
        date_getter=lambda p: p.latest_commit,
        min_or_max=max,
        date_format="%m/%Y",
    )


def _fetch_first_commit_year(project: Project) -> str:
    if project.since != 0:
        return str(project.since)
    return _get_date(
        project,
        date_getter=lambda p: p.first_commit,
        min_or_max=min,
        date_format="%Y",
    )


def _get_date(
    project: Project,
    date_getter: Callable[[Repo], datetime],
    date_format: str,
    min_or_max: Callable[[Iterable[datetime]], datetime],
) -> str:
    repo = get_repo(project.url)
    time_stamps = []
    if repo is not None:
        main_timestamp = date_getter(repo)
        time_stamps.append(main_timestamp)
    sub_time_stamps = _get_subproject_timestamps(project, date_getter)
    time_stamps.extend(sub_time_stamps)
    if time_stamps:
        return min_or_max(time_stamps).strftime(date_format)
    return ""


def _get_subproject_timestamps(
    project: Project, date_getter: Callable[[Repo], datetime]
) -> List[datetime]:
    if project.sub_projects is None:
        return []
    timestamps = []
    for sub_project in project.sub_projects:
        repo = get_repo(sub_project.url)
        if repo is None:
            continue
        date = date_getter(repo)
        timestamps.append(date)
    return timestamps


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


def export_json_schema(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        "Create a JSON validation schema for a software project inventory"
        " file\n"
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default="docs/software/project-inventory-schema.json",
        help="Output path to write the JSON schema to",
    )
    args = parser.parse_args(argv)
    schema = ProjectInventory.schema_json(indent=2)
    schema += "\n"
    with open(args.path, "w") as stream:
        stream.write(schema)
    return 0


if __name__ == "__main__":
    raise SystemExit(export_json_schema())
