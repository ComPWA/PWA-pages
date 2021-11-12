# cspell:ignore Ipanema
from pwa_pages.repo import get_repo


def test_get_repo():
    repo = get_repo("https://gitlab.cern.ch/bsm-fleet/Ipanema")
    assert repo is not None
    assert repo.name == "Ipanema"
    assert repo.full_name == "bsm-fleet/Ipanema"
    assert repo.first_commit.year == 2017
    assert repo.languages[0] == "C"

    repo = get_repo("https://github.com/ComPWA/pycompwa")
    assert repo is not None
    assert repo.name == "pycompwa"
    assert repo.full_name == "ComPWA/pycompwa"
    assert repo.first_commit.year == 2018
    assert repo.languages == ["Python", "C++", "CMake"]
