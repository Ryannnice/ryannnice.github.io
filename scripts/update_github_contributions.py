#!/usr/bin/env python3
"""Generate a self-hosted GitHub contribution chart from GitHub's public page."""

from __future__ import annotations

import argparse
import html
import json
import re
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


CELL_SIZE = 10
CELL_STEP = 12
LEFT_MARGIN = 28
TOP_MARGIN = 20
CHART_HEIGHT = 104
COLORS = ("#eef2f7", "#dcecff", "#9fc5f1", "#5b96da", "#1468b7")
COUNT_PATTERN = re.compile(r"([\d,]+)\s+contributions?", re.IGNORECASE)


@dataclass
class ContributionDay:
    day: date
    level: int
    count: int | None = None


class ContributionHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.days: list[ContributionDay] = []
        self._days_by_id: dict[str, ContributionDay] = {}
        self._tooltip_target: str | None = None
        self._tooltip_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "td" and "ContributionCalendar-day" in (attributes.get("class") or "").split():
            element_id = attributes.get("id")
            raw_date = attributes.get("data-date")
            raw_level = attributes.get("data-level")
            if not element_id or not raw_date or raw_level is None:
                return
            contribution = ContributionDay(date.fromisoformat(raw_date), int(raw_level))
            self.days.append(contribution)
            self._days_by_id[element_id] = contribution
        elif tag == "tool-tip" and attributes.get("for") in self._days_by_id:
            self._tooltip_target = attributes["for"]
            self._tooltip_text = []

    def handle_data(self, data: str) -> None:
        if self._tooltip_target:
            self._tooltip_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "tool-tip" or not self._tooltip_target:
            return
        tooltip = "".join(self._tooltip_text)
        match = COUNT_PATTERN.search(tooltip)
        self._days_by_id[self._tooltip_target].count = (
            int(match.group(1).replace(",", "")) if match else 0
        )
        self._tooltip_target = None
        self._tooltip_text = []


def fetch_contributions(username: str) -> str:
    url = f"https://github.com/users/{username}/contributions"
    request = Request(
        url,
        headers={
            "Accept": "text/html",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "ryannnice.github.io contribution chart updater",
        },
    )
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except (HTTPError, URLError, TimeoutError) as error:
            if attempt == 2:
                raise RuntimeError(f"Could not fetch {url}: {error}") from error
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def parse_contributions(source: str) -> list[ContributionDay]:
    parser = ContributionHTMLParser()
    parser.feed(source)
    days = sorted(parser.days, key=lambda item: item.day)
    if len(days) < 350:
        raise ValueError(f"Expected a full contribution year; found only {len(days)} days")
    if len({item.day for item in days}) != len(days):
        raise ValueError("GitHub returned duplicate contribution dates")
    if any(item.level not in range(5) or item.count is None for item in days):
        raise ValueError("GitHub returned an incomplete contribution calendar")
    return days


def first_day_of_period(last_day: date, months: int) -> date:
    month_index = last_day.year * 12 + last_day.month - months
    return date(month_index // 12, month_index % 12 + 1, 1)


def next_month(day: date) -> date:
    return date(day.year + (day.month == 12), day.month % 12 + 1, 1)


def build_svg(days: list[ContributionDay], username: str, months: int) -> tuple[str, dict[str, object]]:
    generated_at = datetime.now(timezone.utc)
    last_day = days[-1].day
    period_start = first_day_of_period(last_day, months)
    days_since_sunday = (period_start.weekday() + 1) % 7
    grid_start = period_start - timedelta(days=days_since_sunday)
    visible_days = [item for item in days if grid_start <= item.day <= last_day]
    column_count = (last_day - grid_start).days // 7 + 1
    chart_width = LEFT_MARGIN + (column_count - 1) * CELL_STEP + CELL_SIZE + 1

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{chart_width}" height="{CHART_HEIGHT}" viewBox="0 0 {chart_width} {CHART_HEIGHT}" role="img">',
        f"  <title>{html.escape(username)} GitHub contributions</title>",
        f"  <desc>Contribution calendar from {period_start.isoformat()} to {last_day.isoformat()}.</desc>",
        '  <g font-family="Arial, sans-serif" font-size="9" fill="#7d8590">',
    ]

    month = period_start
    while month <= last_day:
        column = (month - grid_start).days // 7
        lines.append(f'    <text x="{LEFT_MARGIN + column * CELL_STEP}" y="9">{month.strftime("%b")}</text>')
        month = next_month(month)
    for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        lines.append(f'    <text x="0" y="{TOP_MARGIN + row * CELL_STEP + 8}">{label}</text>')
    lines.append("  </g>")
    lines.append('  <g shape-rendering="geometricPrecision">')

    for item in visible_days:
        column = (item.day - grid_start).days // 7
        sunday_first_row = (item.day.weekday() + 1) % 7
        x = LEFT_MARGIN + column * CELL_STEP
        y = TOP_MARGIN + sunday_first_row * CELL_STEP
        lines.append(
            f'    <rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" rx="2" '
            f'fill="{COLORS[item.level]}" data-date="{item.day.isoformat()}" '
            f'data-count="{item.count}" data-level="{item.level}" />'
        )
    lines.extend(("  </g>", "</svg>", ""))

    display_total = sum(item.count or 0 for item in days if period_start <= item.day <= last_day)
    metadata: dict[str, object] = {
        "username": username,
        "profile_url": f"https://github.com/{username}",
        "updated_at": generated_at.date().isoformat(),
        "updated_label": f"{generated_at:%b} {generated_at.day}, {generated_at.year}",
        "year_total": sum(item.count or 0 for item in days),
        "display_total": display_total,
        "period_start": period_start.isoformat(),
        "period_end": last_day.isoformat(),
        "chart_width": chart_width,
        "chart_height": CHART_HEIGHT,
    }
    return "\n".join(lines), metadata


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(content, encoding="utf-8")
    temporary_path.replace(path)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="Ryannnice")
    parser.add_argument("--months", type=int, default=8)
    parser.add_argument("--output", type=Path, default=Path("images/github-contributions.svg"))
    parser.add_argument("--metadata", type=Path, default=Path("_data/github_contributions.json"))
    args = parser.parse_args()
    if not 1 <= args.months <= 12:
        parser.error("--months must be between 1 and 12")

    source = fetch_contributions(args.username)
    days = parse_contributions(source)
    svg, metadata = build_svg(days, args.username, args.months)
    svg_changed = write_if_changed(args.output, svg)
    metadata_changed = write_if_changed(
        args.metadata,
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
    )
    status = "updated" if svg_changed or metadata_changed else "already current"
    print(f"Contribution chart {status}: {metadata['year_total']} contributions in the last year")


if __name__ == "__main__":
    main()
