# pylint: disable=redefined-outer-name
import pytest

from pwa_pages.repo._gitlab import (
    get_first_commit_date,
    get_gitlab_repo,
    get_last_modified,
    get_latest_commit_date,
    split_gitlab_repo_url,
)


def test_get_gitlab_repo():
    repo = get_gitlab_repo(
        server_url="https://gitlab.cern.ch",
        project_path="poluekt/TensorFlowAnalysis",
    )
    # cspell:words poluekt
    assert repo.attributes["name"] == "TensorFlowAnalysis"


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        (
            "https://gitlab.cern.ch/poluekt/TensorFlowAnalysis",
            ("https://gitlab.cern.ch", "poluekt/TensorFlowAnalysis"),
        ),
        ("https://github.com/ComPWA/tensorwaves", None),
    ],
)
def test_split_gitlab_repo_url(url, expected):
    assert split_gitlab_repo_url(url) == expected


@pytest.fixture(scope="session")
def tfa_repo():
    return get_gitlab_repo(
        server_url="https://gitlab.cern.ch",
        project_path="poluekt/TensorFlowAnalysis",
    )


def test_get_first_commit_date(tfa_repo):
    date = get_first_commit_date(tfa_repo)
    assert date.strftime("%Y.%m.%d") == "2016.11.25"


def test_get_latest_commit_date(tfa_repo):
    date = get_latest_commit_date(tfa_repo)
    assert date.year >= 2020


def test_get_last_modified(tfa_repo):
    date = get_last_modified(tfa_repo)
    assert date.year >= 2021
