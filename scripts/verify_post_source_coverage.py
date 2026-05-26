#!/usr/bin/env python3
"""Verify that existing _posts contain complete Renyuan_Log.md source coverage."""

from __future__ import annotations

import re
from collections import Counter
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Renyuan_Log.md"
POSTS = ROOT / "_posts"
ARTIFACTS = ROOT / "_data" / "tech_log_artifacts.yml"

DATE_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
SOURCE_LINE_RE = re.compile(r"^(\d{4}) \|(.*)$")
TABLE_RE = re.compile(r"^\s*\|.*\|\s*$")
FENCE_RE = re.compile(r"^```")
START_MARKER = "<!-- source-log-coverage:start -->"
END_MARKER = "<!-- source-log-coverage:end -->"


def collect_post_source_lines(source_lines: list[str]) -> tuple[dict[int, Counter[str]], int]:
    seen: dict[int, Counter[str]] = {}
    marker_blocks = 0
    for post in POSTS.glob("*.md"):
        in_block = False
        for line in post.read_text(encoding="utf-8").splitlines():
            if line == START_MARKER:
                in_block = True
                marker_blocks += 1
                continue
            if line == END_MARKER:
                in_block = False
                continue
            if not in_block:
                continue
            match = SOURCE_LINE_RE.match(line)
            if not match:
                continue
            line_no = int(match.group(1))
            content = unescape(match.group(2))
            seen.setdefault(line_no, Counter())[content] += 1
    return seen, marker_blocks


def parse_artifacts() -> list[dict[str, object]]:
    if not ARTIFACTS.exists():
        return []
    items: list[dict[str, object]] = []
    item: dict[str, object] = {}
    for line in ARTIFACTS.read_text(encoding="utf-8").splitlines():
        if line.startswith("- type: "):
            if item:
                items.append(item)
            item = {"type": line.split('"', 2)[1]}
        elif line.startswith("  date: "):
            item["date"] = line.split('"', 2)[1]
        elif line.startswith("  start_line: "):
            item["start_line"] = int(line.rsplit(" ", 1)[1])
        elif line.startswith("  end_line: "):
            item["end_line"] = int(line.rsplit(" ", 1)[1])
    if item:
        items.append(item)
    return items


def main() -> None:
    source_lines = SOURCE.read_text(encoding="utf-8").splitlines()
    seen, marker_blocks = collect_post_source_lines(source_lines)

    missing_lines = []
    mismatched_lines = []
    for line_no, source_line in enumerate(source_lines, start=1):
        if line_no not in seen:
            missing_lines.append(line_no)
            continue
        if source_line not in seen[line_no]:
            mismatched_lines.append(line_no)

    source_text = "\n".join(source_lines)
    dates = DATE_RE.findall(source_text)
    post_text = "\n".join(post.read_text(encoding="utf-8") for post in POSTS.glob("*.md"))
    missing_date_anchors = [date for date in dates if f'id="source-log-{date}"' not in post_text]

    table_lines = [idx for idx, line in enumerate(source_lines, start=1) if TABLE_RE.match(line)]
    fence_lines = [idx for idx, line in enumerate(source_lines, start=1) if FENCE_RE.match(line)]
    artifacts = parse_artifacts()
    missing_artifacts = []
    for item in artifacts:
        start = int(item["start_line"])
        end = int(item["end_line"])
        uncovered = [line_no for line_no in range(start, end + 1) if line_no in missing_lines]
        if uncovered:
            missing_artifacts.append((item, uncovered[:5]))

    print(f"posts_with_coverage_blocks={marker_blocks}")
    print(f"source_lines={len(source_lines)}")
    print(f"covered_source_lines={len(seen)}")
    print(f"missing_source_lines={len(missing_lines)}")
    print(f"mismatched_source_lines={len(mismatched_lines)}")
    print(f"date_anchors={len(dates) - len(missing_date_anchors)}/{len(dates)}")
    print(f"table_lines_covered={sum(1 for line_no in table_lines if line_no in seen)}/{len(table_lines)}")
    print(f"fence_lines_covered={sum(1 for line_no in fence_lines if line_no in seen)}/{len(fence_lines)}")
    print(f"artifacts_covered={len(artifacts) - len(missing_artifacts)}/{len(artifacts)}")

    failures = []
    if marker_blocks != len(list(POSTS.glob("*.md"))):
        failures.append(f"Expected one coverage block per post, found {marker_blocks}")
    if missing_lines:
        failures.append(f"Missing source lines: {missing_lines[:20]}")
    if mismatched_lines:
        failures.append(f"Mismatched source lines: {mismatched_lines[:20]}")
    if missing_date_anchors:
        failures.append(f"Missing date anchors: {missing_date_anchors}")
    if missing_artifacts:
        failures.append(f"Missing artifact ranges: {missing_artifacts[:5]}")

    if failures:
        print("status=FAIL")
        for failure in failures:
            print(f"failure={failure}")
        raise SystemExit(1)
    print("status=PASS")


if __name__ == "__main__":
    main()
