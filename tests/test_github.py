from typing import List

import pytest

from pwa_pages.github import get_last_contribution, get_main_languages


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
