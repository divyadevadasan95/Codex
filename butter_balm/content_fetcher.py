from __future__ import annotations

import dataclasses
import logging
from typing import Iterable, List, Optional

import requests
from bs4 import BeautifulSoup


@dataclasses.dataclass
class FetchedArticle:
    """Simplified representation of content pulled from the web."""

    source_url: str
    title: str
    summary: str


class ContentFetcher:
    """Fetches and lightly processes articles from the web."""

    def __init__(self, timeout: int = 10) -> None:
        self.timeout = timeout
        self.logger = logging.getLogger(self.__class__.__name__)

    def fetch(self, urls: Iterable[str]) -> List[FetchedArticle]:
        articles: List[FetchedArticle] = []
        for url in urls:
            article = self._fetch_single(url)
            if article:
                articles.append(article)
        return articles

    def _fetch_single(self, url: str) -> Optional[FetchedArticle]:
        self.logger.debug("Fetching url: %s", url)
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            self.logger.warning("Skipping url %s due to error: %s", url, exc)
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        title = (soup.title.string if soup.title and soup.title.string else "Untitled").strip()
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
        summary = " ".join(paragraphs[:3])
        return FetchedArticle(source_url=url, title=title, summary=summary)
