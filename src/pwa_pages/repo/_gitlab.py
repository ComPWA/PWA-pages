import re
from datetime import datetime
from functools import lru_cache
from typing import Optional, Tuple

from dateutil.parser import parse as parse_date
from gitlab import Gitlab
from gitlab.v4.objects import Project as GitlabProject
from gitlab.v4.objects import ProjectCommitManager


@lru_cache()
def get_gitlab_repo(server_url: str, project_path: str) -> GitlabProject:
    gitlab = __get_gitlab(server_url)
    return gitlab.projects.get(project_path)


def split_gitlab_repo_url(url: str) -> Optional[Tuple[str, str]]:
    match = re.match(r"^(https?://)([^/]*gitlab[^/]+)/(.*)$", url)
    if match is None:
        return None
    server_url = match[1] + match[2]
    project_path = match[3]
    return server_url, project_path


@lru_cache()
def get_first_commit_date(repo: GitlabProject) -> datetime:
    commits: ProjectCommitManager = repo.commits
    all_commits = commits.list(all=True)
    assert isinstance(all_commits, list)  # noqa: S101
    first_commit = all_commits[-1]
    commit_info = first_commit._attrs
    return parse_date(commit_info["created_at"])


@lru_cache()
def get_latest_commit_date(repo: GitlabProject) -> datetime:
    default_branch = repo.attributes["default_branch"]
    commits: ProjectCommitManager = repo.commits
    latest_commit = commits.get(default_branch)
    commit_info = latest_commit._attrs
    return parse_date(commit_info["created_at"])


def get_last_modified(repo: GitlabProject) -> datetime:
    date_str = repo.attributes["last_activity_at"]
    return parse_date(date_str)


@lru_cache()
def __get_gitlab(url: str) -> Gitlab:
    return Gitlab(url)
