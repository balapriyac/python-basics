#!/usr/bin/env python3
"""
log_file_analyzer.py

Scan a log file and filter lines by severity level, keyword, and/or date
range, then print a summary: total matches, a breakdown by level, and
the most recent matching lines.

Expects log lines that start with a timestamp and a level, e.g.:
    2026-09-20 14:03:11 ERROR Connection timed out after 30s
    2026-09-20 14:03:12 INFO  Retrying connection...

Usage:
    python 05_log_file_analyzer.py app.log --level ERROR
    python 05_log_file_analyzer.py app.log --keyword timeout
    python 05_log_file_analyzer.py app.log --since 2026-09-20 --until 2026-09-21
    python 05_log_file_analyzer.py app.log --level WARNING --keyword disk --tail 10
"""

import argparse
import re
from collections import Counter
from datetime import datetime

LINE_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+(?P<message>.*)$"
)


def parse_line(line):
    match = LINE_PATTERN.match(line.strip())
    if not match:
        return None
    try:
        timestamp = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    return {
        "timestamp": timestamp,
        "level": match.group("level"),
        "message": match.group("message"),
        "raw": line.rstrip("\n"),
    }


def matches_filters(entry, level=None, keyword=None, since=None, until=None):
    if level and entry["level"].upper() != level.upper():
        return False
    if keyword and keyword.lower() not in entry["message"].lower():
        return False
    if since and entry["timestamp"] < since:
        return False
    if until and entry["timestamp"] > until:
        return False
    return True


def analyze_log(path, level=None, keyword=None, since=None, until=None):
    matched = []
    unparsed_count = 0

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            entry = parse_line(line)
            if entry is None:
                if line.strip():
                    unparsed_count += 1
                continue
            if matches_filters(entry, level, keyword, since, until):
                matched.append(entry)

    return matched, unparsed_count


def parse_date_arg(value):
    if value is None:
        return None
    return datetime.strptime(value, "%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser(description="Filter and summarize a log file.")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("--level", default=None, help="Filter by severity level, e.g. ERROR")
    parser.add_argument("--keyword", default=None, help="Filter by keyword in the message")
    parser.add_argument("--since", default=None, help="Only include lines on/after this date (YYYY-MM-DD)")
    parser.add_argument("--until", default=None, help="Only include lines on/before this date (YYYY-MM-DD)")
    parser.add_argument("--tail", type=int, default=20,
                         help="Number of most recent matching lines to print (default: 20)")
    args = parser.parse_args()

    since = parse_date_arg(args.since)
    until = parse_date_arg(args.until)

    matched, unparsed_count = analyze_log(
        args.log_file, level=args.level, keyword=args.keyword, since=since, until=until
    )

    print(f"Matched {len(matched)} line(s) in {args.log_file}")
    if unparsed_count:
        print(f"({unparsed_count} line(s) did not match the expected log format and were skipped)")

    if matched:
        level_counts = Counter(e["level"] for e in matched)
        print("\nBreakdown by level:")
        for level, count in level_counts.most_common():
            print(f"  {level:<10} {count}")

        print(f"\nMost recent {min(args.tail, len(matched))} matching line(s):")
        for entry in matched[-args.tail:]:
            print(f"  {entry['raw']}")
    else:
        print("No lines matched the given filters.")


if __name__ == "__main__":
    main()


