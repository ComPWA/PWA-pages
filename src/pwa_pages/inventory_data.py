"""Generate a JSON file with live data about the projects in the inventory.

The tables on the software page are rendered from the inventory YAML files at build
time, but the columns that change over time (latest commit and languages) are left
empty. They are filled in by :file:`docs/software/live-inventory.js`, which loads the
JSON file that this module writes. That way, the tables stay up to date without the
documentation having to be rebuilt, and the build itself does not have to hit the GitHub
and GitLab APIs.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from .project_inventory import ProjectInventory, get_repo_urls, load_yaml
from .repo import get_repo_snapshot

if TYPE_CHECKING:
    from collections.abc import Sequence


def collect_repo_urls(inventory: ProjectInventory) -> list[str]:
    """Get the URLs of all projects and sub-projects that are Git repositories."""
    urls: list[str] = []
    for project in inventory.projects:
        urls.extend(get_repo_urls(project))
    return sorted(set(urls))


def fetch_repository_data(urls: Sequence[str]) -> dict[str, dict]:
    """Fetch the live data for each repository URL.

    Repositories that cannot be reached are skipped with a warning: a single renamed or
    deleted repository should not invalidate the entire JSON file.
    """
    repositories: dict[str, dict] = {}
    for url in urls:
        try:
            snapshot = get_repo_snapshot(url)
        except Exception as exception:  # ruff: ignore[blind-except]
            print(f"WARNING: could not fetch {url}: {exception}", file=sys.stderr)  # ruff: ignore[print]
            continue
        if snapshot is None:
            continue
        repositories[url] = {
            "latest_commit": snapshot.latest_commit.strftime("%Y-%m-%d"),
            "languages": {
                language: round(percentage, 2)
                for language, percentage in snapshot.languages.items()
            },
        }
    return repositories


def export_inventory_data(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch live data for the projects in one or more inventory files"
    )
    parser.add_argument(
        "inventory_files",
        nargs="+",
        type=str,
        help="Paths to the project inventory YAML files",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="docs/software/inventory.json",
        help="Output path to write the JSON data to",
    )
    args = parser.parse_args(argv)

    urls: list[str] = []
    for path in args.inventory_files:
        inventory = ProjectInventory(**load_yaml(path))
        urls.extend(collect_repo_urls(inventory))
    repositories = fetch_repository_data(sorted(set(urls)))
    if not repositories:
        print("ERROR: could not fetch data for any repository", file=sys.stderr)  # ruff: ignore[print]
        return 1

    data = {
        "generated": datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repositories": repositories,
    }
    with open(args.output, "w") as stream:
        json.dump(data, stream, indent=2, sort_keys=False)
        stream.write("\n")
    print(f"Wrote data for {len(repositories)} repositories to {args.output}")  # ruff: ignore[print]
    return 0


if __name__ == "__main__":
    raise SystemExit(export_inventory_data())
