import pytest

from pwa_pages.repo._github import (
    extract_github_repo_name,
    get_first_commit_date,
    get_github_repo,
    get_languages,
    get_last_modified,
    get_latest_commit_date,
)


def test_get_first_commit_date():
    repo = get_github_repo("https://github.com/ComPWA/ComPWA")
    first_commit_date = get_first_commit_date(repo)
    assert first_commit_date.year == 2012
    assert repo.created_at.year == 2013


def test_get_latest_commit_date():
    repo = get_github_repo("https://github.com/ComPWA/expertsystem")
    last_commit = get_latest_commit_date(repo)
    assert last_commit.strftime("%Y.%m.%d") == "2021.05.03"


def test_get_last_modified():
    repo = get_github_repo("https://github.com/ComPWA/expertsystem")
    last_commit = get_latest_commit_date(repo)
    last_edit = get_last_modified(repo)
    diff = last_edit - last_commit
    assert diff.days > 100


@pytest.mark.parametrize(
    ("repo_name", "url"),
    [
        (
            "ComPWA/PWA-pages",
            "https://github.com/ComPWA/PWA-pages",
        ),
        (
            "ComPWA/ComPWA",
            "https://github.com/ComPWA/ComPWA/blob/master/README.md",
        ),
    ],
)
def test_extract_github_repo_name(repo_name, url):
    assert extract_github_repo_name(url) == repo_name


@pytest.mark.parametrize(
    "url",
    [
        "https://github.com/ComPWA",
        "https://gitlab.cern.ch/bsm-fleet/Ipanema",
    ],
)
def test_extract_github_repo_name_error(url):
    assert extract_github_repo_name(url) == ""


def test_get_github_repo():
    repo = get_github_repo("https://github.com/ComPWA/ComPWA")
    languages = list(repo.get_languages())
    assert languages[0] == "C++"


@pytest.mark.parametrize(
    ("repo_name", "first_language"),
    [
        ("ComPWA/ComPWA", "C++"),
        ("ComPWA/PWA-pages", "Python"),
        ("GooFit/GooFit", "C++"),
    ],
)
def test_get_languages(repo_name: str, first_language: str):
    url = f"https://github.com/{repo_name}"
    repo = get_github_repo(url)
    languages = list(get_languages(repo))
    assert len(languages) > 0
    assert languages[0] == first_language
