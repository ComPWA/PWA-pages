"""Get information about a GitHub and GitLab repositories."""

from datetime import datetime
from typing import Dict, List, Optional

import attr

from . import _github
from ._github import extract_github_repo_name, get_github_repo


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
    if extract_github_repo_name(url):
        repo = get_github_repo(url)
        return Repo(
            url=url,
            name=repo.name,
            full_name=repo.full_name,
            languages=_github.get_languages(repo),
            first_commit=_github.get_first_commit_date(repo),
            latest_commit=_github.get_latest_commit_date(repo),
        )
    return None
