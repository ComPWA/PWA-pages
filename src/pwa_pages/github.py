"""Get information about a GitHub repository."""

import os
from datetime import datetime
from typing import List, Optional

from dateutil.parser import parse as parse_date
from github import Github
from github.Repository import Repository


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
    last_edited = parse_date(timestamp)
    return last_edited


def _get_repo(repo_name: str, token: Optional[str] = None) -> Repository:
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")
    github = Github(login_or_token=token)
    return github.get_repo(repo_name)
