#!/usr/bin/env python3
"""Append complete Renyuan_Log.md source coverage to existing tech posts."""

from __future__ import annotations

import re
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Renyuan_Log.md"
POSTS = ROOT / "_posts"
TECH_LOG = ROOT / "_data" / "tech_log.yml"
COVERAGE = ROOT / "_data" / "post_source_coverage.yml"

DATE_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2})\s*$")
START_MARKER = "<!-- source-log-coverage:start -->"
END_MARKER = "<!-- source-log-coverage:end -->"


ASSIGNMENTS: dict[str, list[str]] = {
    "2025-03-22-onlyspecs-workshop-integration.md": [
        "preamble",
        "2025-03-19",
        "2025-03-20",
        "2025-03-21",
        "2025-03-22",
    ],
    "2025-03-24-workshop-cloud-runtime.md": [
        "2025-03-23",
        "2025-03-24",
        "2026-03-30",
        "2026-04-27",
    ],
    "2026-03-26-coding-agent-workflow.md": [
        "2025-03-25",
        "2026-03-26",
        "2026-03-27",
    ],
    "2026-03-28-agent-ux-sse-jsonl.md": [
        "2026-03-28",
    ],
    "2026-04-03-agent-do-mvp-refactor.md": [
        "2026-03-29",
        "2026-04-01",
        "2026-04-02",
        "2026-04-03",
    ],
    "2026-04-07-llm-router-design-space.md": [
        "2026-04-07",
        "2026-04-08",
    ],
    "2026-04-09-routellm-gsm8k-reproduction.md": [
        "2026-04-09",
    ],
    "2026-04-10-router-evaluation-pipeline.md": [
        "2026-04-10",
    ],
    "2026-04-11-semantic-router-override.md": [
        "2026-04-11",
    ],
    "2026-04-13-cs336-transformer-training-basics.md": [
        "2026-04-05",
        "2026-04-06",
        "2026-04-12",
        "2026-04-13",
    ],
    "2026-04-14-vllm-semantic-router-architecture.md": [
        "2026-04-14",
        "2026-04-15",
        "2026-04-22",
    ],
    "2026-04-17-rope-geometry-implementation.md": [
        "2026-04-16",
        "2026-04-17",
        "2026-04-29",
    ],
    "2026-04-20-encoder-z-memory-kv.md": [
        "2026-04-20",
    ],
    "2026-05-04-vllm-request-lifecycle.md": [
        "2026-04-04",
        "2026-04-30",
        "2026-05-04",
        "2026-05-12",
    ],
    "2026-05-11-parallelism-tp-fsdp-zero.md": [
        "2026-05-01",
        "2026-05-05",
        "2026-05-07",
        "2026-05-08",
        "2026-05-09",
        "2026-05-10",
        "2026-05-11",
    ],
    "2026-05-16-deepseek-v4-flash-ascend.md": [
        "2026-05-13",
        "2026-05-14",
        "2026-05-15",
        "2026-05-16",
    ],
    "2026-05-16-npu-cluster-scheduling.md": [
        "2026-05-16",
    ],
    "2026-05-17-cuda-kernel-llm-optimization.md": [
        "2026-04-26",
        "2026-04-28",
        "2026-05-17",
    ],
    "2026-05-21-operator-fusion-softmax.md": [
        "2026-05-20",
        "2026-05-21",
    ],
    "2026-05-22-layernorm-rmsnorm-geometry.md": [
        "2026-05-22",
    ],
}


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def escape_source_line(line: str) -> str:
    suffix_start = len(line)
    while suffix_start > 0 and line[suffix_start - 1] in (" ", "\t"):
        suffix_start -= 1
    suffix = line[suffix_start:]
    escaped = escape(line[:suffix_start])
    return escaped + "".join("&#9;" if char == "\t" else "&#32;" for char in suffix)


def post_url(post_name: str, anchor: str) -> str:
    slug = post_name.removesuffix(".md")[11:]
    return f"/tech-blog/{slug}/#{anchor}"


def parse_sections(lines: list[str]) -> tuple[int, dict[str, tuple[int, int]]]:
    date_positions: list[tuple[str, int]] = []
    for index, line in enumerate(lines, start=1):
        match = DATE_RE.match(line)
        if match:
            date_positions.append((match.group(1), index))
    if not date_positions:
        raise ValueError("No dated sections found in Renyuan_Log.md")

    preamble_end = date_positions[0][1] - 1
    sections: dict[str, tuple[int, int]] = {}
    for idx, (date, start) in enumerate(date_positions):
        end = date_positions[idx + 1][1] - 1 if idx + 1 < len(date_positions) else len(lines)
        sections[date] = (start, end)
    return preamble_end, sections


def parse_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    current_date = ""
    for line in TECH_LOG.read_text(encoding="utf-8").splitlines():
        date_match = re.match(r'- date: "([^"]+)"', line)
        if date_match:
            current_date = date_match.group(1)
            continue
        title_match = re.match(r'  title: "([^"]+)"', line)
        if current_date and title_match:
            titles[current_date] = title_match.group(1)
    return titles


def remove_existing_block(text: str) -> str:
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return text.rstrip()
    end += len(END_MARKER)
    return (text[:start].rstrip() + "\n" + text[end:].lstrip("\n")).rstrip()


def section_for_key(key: str, preamble_end: int, sections: dict[str, tuple[int, int]]) -> tuple[str, int, int]:
    if key == "preamble":
        return "Preamble", 1, preamble_end
    start, end = sections[key]
    return key, start, end


def build_coverage_block(
    keys: list[str],
    lines: list[str],
    preamble_end: int,
    sections: dict[str, tuple[int, int]],
    titles: dict[str, str],
) -> tuple[str, list[dict[str, object]]]:
    entries: list[dict[str, object]] = []
    block = [
        START_MARKER,
        "",
        "## Source Log Coverage",
        "",
        "The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.",
        "",
        "| Source | Lines | Title |",
        "| --- | ---: | --- |",
    ]
    for key in keys:
        label, start, end = section_for_key(key, preamble_end, sections)
        title = "稔远学习日志" if key == "preamble" else titles.get(key, "原文")
        anchor = "source-log-preamble" if key == "preamble" else f"source-log-{key}"
        entries.append(
            {
                "source": label,
                "anchor": anchor,
                "start_line": start,
                "end_line": end,
                "title": title,
            }
        )
        block.append(f"| [{label}](#{anchor}) | {start}-{end} | {title.replace('|', '/')} |")

    for entry in entries:
        block.extend(
            [
                "",
                f'<a id="{entry["anchor"]}"></a>',
                f'### Source Log: {entry["source"]}',
                "",
                f'Source lines: `Renyuan_Log.md:{entry["start_line"]}-{entry["end_line"]}`',
                "",
                '<pre class="tech-log-source"><code>',
            ]
        )
        for line_no in range(int(entry["start_line"]), int(entry["end_line"]) + 1):
            block.append(f"{line_no:04d} |{escape_source_line(lines[line_no - 1])}")
        block.extend(["</code></pre>", ""])
    block.append(END_MARKER)
    return "\n".join(block).rstrip() + "\n", entries


def validate_assignments(preamble_end: int, sections: dict[str, tuple[int, int]]) -> None:
    if preamble_end <= 0:
        raise ValueError("Expected a non-empty preamble before the first dated section")
    all_dates = set(sections)
    assigned_dates = [key for keys in ASSIGNMENTS.values() for key in keys if key != "preamble"]
    missing = sorted(all_dates - set(assigned_dates))
    extra = sorted(set(assigned_dates) - all_dates)
    if missing or extra:
        raise ValueError(f"Date assignment mismatch: missing={missing}, extra={extra}")
    for post_name in ASSIGNMENTS:
        if not (POSTS / post_name).exists():
            raise FileNotFoundError(POSTS / post_name)


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    preamble_end, sections = parse_sections(lines)
    validate_assignments(preamble_end, sections)
    titles = parse_titles()

    coverage_lines = ["# Generated by scripts/update_post_source_coverage.py from Renyuan_Log.md"]
    total_entries = 0
    for post_name, keys in ASSIGNMENTS.items():
        post_path = POSTS / post_name
        coverage_block, entries = build_coverage_block(keys, lines, preamble_end, sections, titles)
        original = post_path.read_text(encoding="utf-8")
        updated = remove_existing_block(original) + "\n\n" + coverage_block
        post_path.write_text(updated, encoding="utf-8")
        total_entries += len(entries)

        coverage_lines.append(f"- post: {yaml_quote('_posts/' + post_name)}")
        coverage_lines.append("  entries:")
        for entry in entries:
            coverage_lines.extend(
                [
                    f"    - source: {yaml_quote(str(entry['source']))}",
                    f"      anchor: {yaml_quote(str(entry['anchor']))}",
                    f"      url: {yaml_quote(post_url(post_name, str(entry['anchor'])))}",
                    f"      start_line: {entry['start_line']}",
                    f"      end_line: {entry['end_line']}",
                    f"      title: {yaml_quote(str(entry['title']))}",
                ]
            )

    COVERAGE.write_text("\n".join(coverage_lines) + "\n", encoding="utf-8")
    print(f"posts={len(ASSIGNMENTS)}")
    print(f"entries={total_entries}")
    print(f"source_lines={len(lines)}")
    print(f"coverage={COVERAGE}")


if __name__ == "__main__":
    main()
