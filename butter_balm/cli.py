from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import List

import yaml

from .content_fetcher import ContentFetcher
from .plan_builder import PlanBuilder


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble a launch blueprint for the Butter lip balm brand from web sources.",
    )
    parser.add_argument(
        "--sources",
        type=Path,
        required=True,
        help="Path to a YAML file containing a list of URLs to pull research from.",
    )
    parser.add_argument(
        "--brand",
        type=str,
        default="Butter",
        help="Brand name used throughout the plan.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("butter_launch_plan.md"),
        help="Where to write the launch plan (Markdown).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Seconds to wait for each HTTP request.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging for troubleshooting.",
    )
    return parser.parse_args(argv)


def load_sources(path: Path) -> List[str]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, list):
        raise ValueError("Sources YAML must contain a list of URLs.")
    return [str(url) for url in data]


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    urls = load_sources(args.sources)
    fetcher = ContentFetcher(timeout=args.timeout)
    articles = fetcher.fetch(urls)

    planner = PlanBuilder(args.brand)
    plan = planner.build(articles)

    args.output.write_text(plan)
    logging.info("Launch plan written to %s", args.output)


if __name__ == "__main__":  # pragma: no cover
    main()
