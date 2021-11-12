"""Get information about a GitHub repository."""

import os
from datetime import datetime
from functools import lru_cache
from typing import List, Optional

from dateutil.parser import parse as parse_date
from github import Github
from github.Commit import Commit
from github.Repository import Repository


@lru_cache()
def get_main_languages(
    repo_name: str, min_percentage: float = 20
) -> List[str]:
    repo = _get_repo(repo_name)
    language_lines = repo.get_languages()
    total_lines = sum(language_lines.values())
    language_percentages = {
        language: 100 * lines / total_lines
        for language, lines in language_lines.items()
    }
    main_languages = [
        language
        for language, percentage in language_percentages.items()
        if percentage > min_percentage
    ]
    return main_languages


@lru_cache()
def get_first_contribution(repo_name: str) -> datetime:
    repo = _get_repo(repo_name)
    commits = repo.get_commits().reversed
    first_commit: Commit = commits[0]
    timestamp = first_commit.last_modified
    if timestamp is None:
        raise ValueError(
            f"First commit of GitHub repo {repo_name} has no timestamp"
        )
    return parse_date(timestamp)


@lru_cache()
def get_last_contribution(repo_name: str) -> datetime:
    repo = _get_repo(repo_name)
    default_branch = repo.default_branch
    latest_commit = repo.get_commit(default_branch)
    timestamp = latest_commit.last_modified
    if timestamp is None:
        raise ValueError(
            f"Last commit on default branch {default_branch} of"
            f" {repo.url} has no timestamp"
        )
    return parse_date(timestamp)


@lru_cache()
def _get_repo(repo_name: str) -> Repository:
    github = __get_github()
    return github.get_repo(repo_name)


@lru_cache()
def __get_github(token: Optional[str] = None) -> Github:
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")
    return Github(login_or_token=token)
