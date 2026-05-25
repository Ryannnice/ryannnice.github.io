#!/usr/bin/env python3
"""Generate the full tech-log archive page and block coverage manifest."""

from __future__ import annotations

import re
from pathlib import Path
from html import escape


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Renyuan_Log.md"
ARCHIVE = ROOT / "tech-log-full.md"
MANIFEST = ROOT / "_data" / "tech_log_blocks.yml"
ARTIFACTS = ROOT / "_data" / "tech_log_artifacts.yml"

DATE_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2})\s*$")
HEADING_RE = re.compile(r"^#{2,6}\s+")
FENCE_RE = re.compile(r"^```")
TABLE_RE = re.compile(r"^\s*\|.*\|\s*$")
DIAGRAM_CHARS = ("┌", "┐", "└", "┘", "│", "─", "→", "↓", "↑", "←")


def section_fence_ranges(start: int, end: int, lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    """Return complete fenced ranges and local orphan fence markers for one date section."""
    fence_lines = [line_no for line_no in range(start, end + 1) if FENCE_RE.match(lines[line_no - 1])]
    ranges: list[tuple[int, int]] = []
    orphans: list[int] = []
    index = 0
    while index < len(fence_lines):
        current = fence_lines[index]
        if index + 1 >= len(fence_lines):
            orphans.append(current)
            break

        next_line = fence_lines[index + 1]
        remaining = len(fence_lines) - index
        current_text = lines[current - 1].strip()
        next_text = lines[next_line - 1].strip()
        if remaining % 2 == 1 and current_text == "```" and next_text != "```":
            orphans.append(current)
            index += 1
            continue

        ranges.append((current, next_line))
        index += 2

    return ranges, orphans


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def section_stats(date: str, start: int, end: int, lines: list[str]) -> dict[str, object]:
    section = lines[start - 1 : end]
    heading_count = sum(1 for line in section if HEADING_RE.match(line))
    fence_ranges, _orphans = section_fence_ranges(start, end, lines)
    code_blocks = len(fence_ranges)
    table_rows = sum(1 for line in section if TABLE_RE.match(line))
    diagram_blocks = 0
    for block_start, block_end in fence_ranges:
        block = "\n".join(lines[block_start:block_end - 1])
        if any(ch in block for ch in DIAGRAM_CHARS) or "->" in block or "流程图" in block:
            diagram_blocks += 1
    first_subheading = ""
    for line in section[1:]:
        if HEADING_RE.match(line):
            first_subheading = re.sub(r"^#{2,6}\s+", "", line).strip()
            break
    return {
        "date": date,
        "start_line": start,
        "end_line": end,
        "line_count": end - start + 1,
        "heading_count": heading_count,
        "code_blocks": code_blocks,
        "table_rows": table_rows,
        "diagram_blocks": diagram_blocks,
        "first_subheading": first_subheading,
    }


def collect_artifacts(date_positions: list[tuple[str, int]], lines: list[str]) -> list[dict[str, object]]:
    artifacts: list[dict[str, object]] = []
    sections: list[tuple[str, int, int]] = []
    for idx, (date, start) in enumerate(date_positions):
        end = date_positions[idx + 1][1] - 1 if idx + 1 < len(date_positions) else len(lines)
        sections.append((date, start, end))

    for date, start, end in sections:
        fence_ranges, orphan_fences = section_fence_ranges(start, end, lines)
        for block_start, block_end in fence_ranges:
            opening = lines[block_start - 1].strip()
            info = opening.removeprefix("```").strip()
            block = "\n".join(lines[block_start:block_end - 1])
            item = {
                "type": "code",
                "date": date,
                "start_line": block_start,
                "end_line": block_end,
                "label": f"fenced block: {info}" if info else "fenced block",
            }
            artifacts.append(item)
            if any(ch in block for ch in DIAGRAM_CHARS) or "->" in block or "流程图" in block:
                artifacts.append(
                    {
                        "type": "diagram",
                        "date": date,
                        "start_line": block_start,
                        "end_line": block_end,
                        "label": "ASCII / flow diagram inside fenced block",
                    }
                )
        for orphan_line in orphan_fences:
            artifacts.append(
                {
                    "type": "orphan_fence",
                    "date": date,
                    "start_line": orphan_line,
                    "end_line": orphan_line,
                    "label": "unpaired code fence marker within date section",
                }
            )

        table_start: int | None = None
        for index in range(start, end + 2):
            line = lines[index - 1] if index <= end else ""
            if index <= end and TABLE_RE.match(line):
                if table_start is None:
                    table_start = index
            else:
                if table_start is not None:
                    artifacts.append(
                        {
                            "type": "table",
                            "date": date,
                            "start_line": table_start,
                            "end_line": index - 1,
                            "label": "Markdown table",
                        }
                    )
                    table_start = None

    type_order = {"code": 0, "diagram": 1, "table": 2, "orphan_fence": 3}
    artifacts.sort(key=lambda item: (int(item["start_line"]), type_order.get(str(item["type"]), 9)))
    return artifacts


def main() -> None:
    source_text = SOURCE.read_text(encoding="utf-8")
    lines = source_text.splitlines()

    date_positions: list[tuple[str, int]] = []
    for index, line in enumerate(lines, start=1):
        match = DATE_RE.match(line)
        if match:
            date_positions.append((match.group(1), index))
    preamble_end = date_positions[0][1] - 1 if date_positions else len(lines)

    stats: list[dict[str, object]] = []
    for idx, (date, start) in enumerate(date_positions):
        end = date_positions[idx + 1][1] - 1 if idx + 1 < len(date_positions) else len(lines)
        stats.append(section_stats(date, start, end, lines))
    artifacts = collect_artifacts(date_positions, lines)

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    manifest_lines = [
        "# Generated by scripts/generate_tech_log_archive.py from Renyuan_Log.md",
    ]
    for item in stats:
        manifest_lines.extend(
            [
                f"- date: {yaml_quote(str(item['date']))}",
                f"  anchor: {yaml_quote('log-' + str(item['date']))}",
                f"  start_line: {item['start_line']}",
                f"  end_line: {item['end_line']}",
                f"  line_count: {item['line_count']}",
                f"  heading_count: {item['heading_count']}",
                f"  code_blocks: {item['code_blocks']}",
                f"  table_rows: {item['table_rows']}",
                f"  diagram_blocks: {item['diagram_blocks']}",
                f"  first_subheading: {yaml_quote(str(item['first_subheading']))}",
            ]
        )
    MANIFEST.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    artifact_lines = [
        "# Generated by scripts/generate_tech_log_archive.py from Renyuan_Log.md",
    ]
    for item in artifacts:
        artifact_lines.extend(
            [
                f"- type: {yaml_quote(str(item['type']))}",
                f"  date: {yaml_quote(str(item['date']))}",
                f"  start_line: {item['start_line']}",
                f"  end_line: {item['end_line']}",
                f"  label: {yaml_quote(str(item['label']))}",
            ]
        )
    ARTIFACTS.write_text("\n".join(artifact_lines) + "\n", encoding="utf-8")

    archive_lines = [
        "---",
        'permalink: /tech-blog/full-log/',
        'title: "Full Learning Log"',
        "author_profile: true",
        "---",
        "",
        "This archive is generated from `Renyuan_Log.md` so every original date section, table, code block, ASCII diagram, and explanation remains findable from the tech blog.",
        "",
        "The original log is rendered as line-numbered source blocks on purpose. This avoids a malformed code fence in the source from swallowing later Markdown while still preserving every table, code block, flow diagram, link, command, and explanation in original order.",
        "",
        "## Coverage Index",
        "",
        "| Date | Source Lines | Code Blocks | Table Rows | Diagram Blocks | First Subheading |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    if preamble_end > 0:
        preamble_title = next((line.lstrip("# ").strip() for line in lines[:preamble_end] if line.strip()), "Source Preamble")
        archive_lines.append(
            "| "
            f"[Preamble](#log-preamble) | "
            f"1-{preamble_end} | "
            "0 | "
            "0 | "
            "0 | "
            f"{preamble_title.replace('|', '/')} |"
        )
    for item in stats:
        archive_lines.append(
            "| "
            f"[{item['date']}](#log-{item['date']}) | "
            f"{item['start_line']}-{item['end_line']} | "
            f"{item['code_blocks']} | "
            f"{item['table_rows']} | "
            f"{item['diagram_blocks']} | "
            f"{str(item['first_subheading']).replace('|', '/') or '原文'} |"
        )
    archive_lines.extend(
        [
            "",
            "## Artifact Index",
            "",
            "| Type | Date | Source Lines | Label |",
            "| --- | --- | ---: | --- |",
        ]
    )
    for item in artifacts:
        archive_lines.append(
            "| "
            f"{item['type']} | "
            f"[{item['date']}](#log-{item['date']}) | "
            f"{item['start_line']}-{item['end_line']} | "
            f"{str(item['label']).replace('|', '/')} |"
        )

    archive_lines.extend(["", "## Original Log", ""])

    if preamble_end > 0:
        archive_lines.append('<a id="log-preamble"></a>')
        archive_lines.append("### Preamble")
        archive_lines.append("")
        archive_lines.append(f"Source lines: `1-{preamble_end}`")
        archive_lines.append("")
        archive_lines.append('<pre class="tech-log-source"><code>')
        for line_no in range(1, preamble_end + 1):
            archive_lines.append(f"{line_no:04d}  {escape(lines[line_no - 1])}")
        archive_lines.append("</code></pre>")
        archive_lines.append("")

    for idx, (date, start) in enumerate(date_positions):
        end = date_positions[idx + 1][1] - 1 if idx + 1 < len(date_positions) else len(lines)
        archive_lines.append(f'<a id="log-{date}"></a>')
        archive_lines.append(f"### {date}")
        archive_lines.append("")
        archive_lines.append(f"Source lines: `{start}-{end}`")
        archive_lines.append("")
        archive_lines.append('<pre class="tech-log-source"><code>')
        for line_no in range(start, end + 1):
            archive_lines.append(f"{line_no:04d}  {escape(lines[line_no - 1])}")
        archive_lines.append("</code></pre>")
        archive_lines.append("")
    ARCHIVE.write_text("\n".join(archive_lines) + "\n", encoding="utf-8")

    print(f"dates={len(stats)}")
    print(f"archive={ARCHIVE}")
    print(f"manifest={MANIFEST}")
    print(f"artifacts={ARTIFACTS}")


if __name__ == "__main__":
    main()
