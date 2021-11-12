import os
import re
from datetime import datetime
from functools import lru_cache
from typing import Dict, Optional

from dateutil.parser import parse as parse_date
from github import Github
from github.Commit import Commit
from github.Repository import Repository as GithubRepository


@lru_cache()
def get_github_repo(url: str) -> GithubRepository:
    github = __get_github()
    repo_name = extract_github_repo_name(url)
    if not repo_name:
        raise ValueError(f"Not a GitHub repo URL: {url}")
    return github.get_repo(repo_name)


@lru_cache()
def extract_github_repo_name(url: str) -> str:
    github_url = "https://github.com"
    match = re.match(fr"^{github_url}/([^/]+)/([^/]+).*$", url)
    if match is None:
        return ""
    return f"{match[1]}/{match[2]}"


@lru_cache()
def get_first_commit_date(repo: GithubRepository) -> datetime:
    commits = repo.get_commits().reversed
    first_commit: Commit = commits[0]
    timestamp = first_commit.last_modified
    if timestamp is None:
        raise ValueError(
            f"First commit on of GitHub repo {repo.full_name} has no timestamp"
        )
    return parse_date(timestamp)


@lru_cache()
def get_latest_commit_date(repo: GithubRepository) -> datetime:
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
def get_languages(repo: GithubRepository) -> Dict[str, float]:
    languages = repo.get_languages()
    total_lines = sum(languages.values())
    return {
        language: 100 * lines / total_lines
        for language, lines in languages.items()
    }


@lru_cache()
def __get_github(token: Optional[str] = None) -> Github:
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")
    return Github(login_or_token=token)
