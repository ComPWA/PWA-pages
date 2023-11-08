"""Get information about a GitHub and GitLab repositories."""

from __future__ import annotations

from typing import TYPE_CHECKING

import attr

from . import _github, _gitlab
from ._github import GithubRepository, extract_github_repo_name, get_github_repo
from ._gitlab import GitlabProject, get_gitlab_repo, split_gitlab_repo_url

if TYPE_CHECKING:
    from datetime import datetime


@attr.s(frozen=True, auto_attribs=True)
class Repo:
    name: str
    url: str
    full_name: str
    _languages: dict[str, float]
    first_commit: datetime
    latest_commit: datetime

    @property
    def languages(self) -> list[str]:
        return list(self._languages)

    def filter_languages(self, min_percentage: float) -> list[str]:
        return [
            language
            for language, percentage in self._languages.items()
            if percentage > min_percentage
        ]


def get_repo(url: str) -> Repo | None:
    repo = _fetch_repository(url)
    if isinstance(repo, GithubRepository):
        return Repo(
            url=url,
            name=repo.name,
            full_name=repo.full_name,
            languages=_github.get_languages(repo),
            first_commit=_github.get_first_commit_date(repo),
            latest_commit=_github.get_latest_commit_date(repo),
        )
    if isinstance(repo, GitlabProject):
        return Repo(
            url=url,
            name=repo.attributes["name"],
            full_name=repo.attributes["path_with_namespace"],
            languages=repo.languages(),
            first_commit=_gitlab.get_first_commit_date(repo),
            latest_commit=_gitlab.get_latest_commit_date(repo),
        )
    return None


def _fetch_repository(
    url: str,
) -> GitlabProject | GithubRepository | None:
    if extract_github_repo_name(url):
        return get_github_repo(url)
    gitlab_tuple = split_gitlab_repo_url(url)
    if gitlab_tuple is not None:
        server_url, project_path = gitlab_tuple
        return get_gitlab_repo(server_url, project_path=project_path)
    return None
