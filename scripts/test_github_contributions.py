"""Regression checks for GitHub calendar parsing and generated chart data."""

import unittest
import xml.etree.ElementTree as ET
from datetime import date, timedelta

from update_github_contributions import build_svg, parse_contributions


TODAY = date(2026, 10, 9)


def calendar_html(*, omit=None, latest_tooltip="1,234 contributions on October 9th.", latest_level=4):
    cells = []
    for offset in range(366):
        day = TODAY - timedelta(days=offset)
        if day == omit:
            continue
        level, tooltip = 0, "No contributions on this day."
        if day == TODAY:
            level, tooltip = latest_level, latest_tooltip
        elif day == date(2025, 12, 1):
            level, tooltip = 1, "2 contributions on December 1st."
        cells.append(
            f'<td id="day-{day}" class="ContributionCalendar-day" '
            f'data-date="{day}" data-level="{level}"></td>'
            f'<tool-tip for="day-{day}">{tooltip}</tool-tip>'
        )
    return "\n".join(cells)


class ContributionCalendarTests(unittest.TestCase):
    def test_parses_and_sorts_full_calendar_with_comma_counts(self):
        days = parse_contributions(calendar_html(), today=TODAY)
        self.assertEqual(len(days), 366)
        self.assertEqual(days[0].day, TODAY - timedelta(days=365))
        self.assertEqual(days[0].count, 0)
        self.assertEqual(days[-1].day, TODAY)
        self.assertEqual(days[-1].count, 1234)

    def test_unrecognized_tooltip_is_not_silently_counted_as_zero(self):
        with self.assertRaisesRegex(ValueError, "incomplete"):
            parse_contributions(calendar_html(latest_tooltip="Activity unavailable"), today=TODAY)

    def test_count_must_agree_with_heatmap_level(self):
        with self.assertRaisesRegex(ValueError, "disagree"):
            parse_contributions(calendar_html(latest_level=0), today=TODAY)

    def test_missing_day_is_rejected_even_with_full_year_length(self):
        with self.assertRaisesRegex(ValueError, "missing dates"):
            parse_contributions(calendar_html(omit=TODAY - timedelta(days=10)), today=TODAY)

    def test_duplicate_day_is_rejected(self):
        source = calendar_html()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            parse_contributions(source + source.splitlines()[0], today=TODAY)

    def test_only_current_or_previous_day_calendar_is_accepted(self):
        source = calendar_html()
        parse_contributions(source, today=TODAY + timedelta(days=1))
        for reference_day in (TODAY - timedelta(days=1), TODAY + timedelta(days=2)):
            with self.subTest(reference_day=reference_day):
                with self.assertRaisesRegex(ValueError, "outdated or future"):
                    parse_contributions(source, today=reference_day)

    def test_chart_and_metadata_preserve_recent_activity(self):
        days = parse_contributions(calendar_html(), today=TODAY)
        svg, metadata = build_svg(days, "Ryannnice", 8)
        cells = ET.fromstring(svg).findall(".//{*}rect")
        latest = cells[-1]
        self.assertEqual(latest.get("data-date"), TODAY.isoformat())
        self.assertEqual(latest.get("data-count"), "1234")
        self.assertEqual(latest.get("data-level"), "4")
        self.assertEqual(metadata["period_start"], "2026-03-01")
        self.assertEqual(metadata["period_end"], "2026-10-09")
        self.assertEqual(metadata["year_total"], 1236)
        self.assertEqual(metadata["display_total"], 1234)

    def test_same_day_activity_change_invalidates_image_cache(self):
        days = parse_contributions(calendar_html(), today=TODAY)
        _, before = build_svg(days, "Ryannnice", 8)
        _, unchanged = build_svg(days, "Ryannnice", 8)
        self.assertEqual(before["chart_version"], unchanged["chart_version"])
        days[-1].count += 1
        _, after = build_svg(days, "Ryannnice", 8)
        self.assertEqual(before["updated_at"], after["updated_at"])
        self.assertNotEqual(before["chart_version"], after["chart_version"])


if __name__ == "__main__":
    unittest.main()
