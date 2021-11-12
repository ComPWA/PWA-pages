"""Get information about a GitHub and GitLab repositories."""

from datetime import datetime
from typing import Dict, List, Optional, Union

import attr

from . import _github, _gitlab
from ._github import (
    GithubRepository,
    extract_github_repo_name,
    get_github_repo,
)
from ._gitlab import GitlabProject, get_gitlab_repo, split_gitlab_repo_url


@attr.s(frozen=True, auto_attribs=True)
class Repo:
    name: str
    url: str
    full_name: str
    _languages: Dict[str, float]
    first_commit: datetime
    latest_commit: datetime

    @property
    def languages(self) -> List[str]:
        return list(self._languages)

    def filter_languages(self, min_percentage: float) -> List[str]:
        return [
            language
            for language, percentage in self._languages.items()
            if percentage > min_percentage
        ]


def get_repo(url: str) -> Optional[Repo]:
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
) -> Optional[Union[GitlabProject, GithubRepository]]:
    if extract_github_repo_name(url):
        return get_github_repo(url)
    gitlab_tuple = split_gitlab_repo_url(url)
    if gitlab_tuple is not None:
        server_url, project_path = gitlab_tuple
        return get_gitlab_repo(server_url, project_path=project_path)
    return None
