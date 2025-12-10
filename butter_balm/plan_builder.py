from __future__ import annotations

import collections
import textwrap
from typing import Iterable, List

from .content_fetcher import FetchedArticle

STOP_WORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "your",
    "their",
    "about",
    "into",
    "while",
    "have",
    "are",
    "you",
    "our",
    "but",
    "was",
    "has",
    "had",
    "will",
    "can",
    "they",
    "them",
    "its",
    "we",
    "their",
    "of",
    "a",
    "an",
    "in",
    "on",
    "at",
    "to",
    "is",
    "it",
}


class PlanBuilder:
    """Turns fetched articles into a brand launch blueprint."""

    def __init__(self, brand_name: str) -> None:
        self.brand_name = brand_name

    def build(self, articles: Iterable[FetchedArticle]) -> str:
        articles_list = list(articles)
        keywords = self._extract_keywords(articles_list)

        outline = textwrap.dedent(
            f"""
            # {self.brand_name} Launch Blueprint

            ## Positioning and Brand Story
            - Lead with sustainability: highlight certified organic ingredients and transparent sourcing.
            - Emphasize softness: connect the butter concept to lip nourishment and comfort.
            - Build trust: communicate testing, dermatologist alignment, and clean-label simplicity.

            ## Product Messaging
            - Core promise: glide-on lip butter made with planet-friendly botanicals and recyclable packaging.
            - Hero ingredients surfaced from research: {', '.join(keywords) if keywords else 'update once content is fetched'}.
            - Claims to validate: hydration longevity, feel-on-lips, and environmental footprint reduction.

            ## Campaign Concepts
            - "Spread the Softness": customer stories showing daily moments where {self.brand_name} fits naturally.
            - "Traceable Butter": interactive content tracing each ingredient back to its sustainable source.
            - "Pocket-sized Planet Care": highlight refill or recycling incentives to close the loop.

            ## Launch Checklist
            - Content curation: publish summaries of {len(articles_list)} reference articles to demonstrate category fluency.
            - Partnerships: line up sustainable suppliers and eco-certifications before main campaign.
            - Channels: focus on TikTok/Instagram for education and TikTok Shop for conversion; support with email nurture.
            - Measurement: track engagement rate, repeat purchase, and subscription opt-ins.
            """
        ).strip()

        if articles_list:
            outline += "\n\n" + self._format_articles(articles_list)
        return outline

    def _format_articles(self, articles: List[FetchedArticle]) -> str:
        lines = ["## Reference Articles"]
        for article in articles:
            summary = article.summary or "No summary available."
            lines.append(f"- **{article.title}** — {summary} (Source: {article.source_url})")
        return "\n".join(lines)

    def _extract_keywords(self, articles: Iterable[FetchedArticle], *, top_n: int = 6) -> List[str]:
        counter: collections.Counter[str] = collections.Counter()
        for article in articles:
            words = [w.lower() for w in article.summary.split()] + [w.lower() for w in article.title.split()]
            for word in words:
                cleaned = "".join(ch for ch in word if ch.isalpha())
                if cleaned and cleaned not in STOP_WORDS and len(cleaned) > 3:
                    counter[cleaned] += 1
        return [word for word, _ in counter.most_common(top_n)]
