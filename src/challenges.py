# src/challenges.py

from typing import Optional


def count_evidence(evidence: list[str]) -> dict[str, int]:
    counts = {}

    for item in evidence:
        counts[item] = counts.get(item, 0) + 1

    return counts


def first_repeated_id(ids: list[str]) -> Optional[str]:
    seen = set()

    for case_id in ids:
        if case_id in seen:
            return case_id
        seen.add(case_id)

    return None


def valid_tags(tags: str) -> bool:
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in tags:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            if stack[-1] != matching[char]:
                return False

            stack.pop()

    return len(stack) == 0


def lookup_alias(aliases: dict[str, str], alias: str) -> Optional[str]:
    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    return list(reports)


def largest_time_gap(times: list[int]) -> int:
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)

    largest_gap = 0
    for i in range(1, len(sorted_times)):
        gap = sorted_times[i] - sorted_times[i - 1]
        if gap > largest_gap:
            largest_gap = gap

    return largest_gap