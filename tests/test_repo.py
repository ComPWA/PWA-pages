from typing import List

import pytest

from pwa_pages.repo import (
    get_first_contribution,
    get_last_contribution,
    get_main_languages,
)


def test_get_first_contribution():
    first_commit_date = get_first_contribution("ComPWA/ComPWA")
    assert first_commit_date.year == 2012


def test_get_last_contribution():
    last_edit = get_last_contribution("ComPWA/PWA-pages")
    assert last_edit.year >= 2021


@pytest.mark.parametrize(
    ("repo_name", "expected"),
    [
        ("ComPWA/ComPWA", ["C++"]),
        ("ComPWA/PWA-pages", ["Python"]),
        ("GooFit/GooFit", ["C++", "Cuda", "Jupyter Notebook"]),
    ],
)
def test_get_main_languages(repo_name: str, expected: List[str]):
    languages = get_main_languages(repo_name)
    assert languages == expected
