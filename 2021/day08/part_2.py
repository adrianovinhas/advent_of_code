from collections import Counter
import sys

segments_used: dict[int, str] = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg"
}

inputs: list[list[str]] = list(map(lambda x: x[:-1].split(" | "), sys.stdin.readlines()))
entries: list[list[str]] = list(map(lambda x: x[0].split(" "), inputs))
displays: list[list[str]] = list(map(lambda x: x[1].split(" "), inputs))


def detect_easy_numbers(pattern: str) -> str:
    if len(pattern) == 2:
        return "1"
    elif len(pattern) == 3:
        return "7"
    elif len(pattern) == 4:
        return "4"
    elif len(pattern) == 7:
        return "8"
    else:
        None

final_sum: int = 0
for patterns, display in zip(entries, displays):

    sorted_patterns: list[str] = list(map(lambda x: "".join(sorted(x)), patterns))
    sorted_display: list[str] = list(map(lambda x: "".join(sorted(x)), display))

    easy_patterns: list[str] = list(filter(lambda x: len(x) in [2,3,4,7], sorted_patterns))
    easy_numbers: list[str] = list(map(lambda p: detect_easy_numbers(p), easy_patterns))
    new_segments_used: dict[str, str] = dict(zip(easy_patterns, easy_numbers))

    hard_patterns: list[str] = list(filter(lambda x: x not in easy_patterns, sorted_patterns))
    counter: Counter = Counter("".join(hard_patterns))
    
    # find 9 (the segment missing in 9 has only 3 counts across all the hard digits)
    segment_with_3_counts: str = list(filter(lambda x: counter[x]==3, counter.keys()))[0]
    nine: str = list(filter(lambda x: len(x) == 6 and segment_with_3_counts not in x, hard_patterns))[0]
    new_segments_used[nine] = "9"

    # find 2 (the only 5-length digit that is NOT contained in 9)
    two: str = list(filter(
        lambda x: len(x) == 5 and not set(x).issubset(set(nine)), hard_patterns)
    )[0]
    new_segments_used[two] = "2"

    # find 5 (the only 5-digit length with 3 segments in common with digit 2)
    five: str = list(filter(
        lambda x: len(x) == 5 and len(set(x).intersection(set(two)))==3, hard_patterns)
    )[0]
    new_segments_used[five] = "5"

    # find 3 (the remaining 5-digit length)
    three: str = list(filter(
        lambda x: len(x) == 5 and x not in [two,five], hard_patterns)
    )[0]
    new_segments_used[three] = "3"

    # find 6 (the remaining 6-digit length that is a superset of 5)
    six: str = list(filter(
        lambda x: len(x) == 6 and set(five).issubset(set(x)) and x != nine, hard_patterns)
    )[0]
    new_segments_used[six] = "6"

    # find 0 (the remaining 6-digit length)
    zero: str = list(filter(
        lambda x: len(x) == 6 and x not in [six,nine], hard_patterns)
    )[0]
    new_segments_used[zero] = "0"

    digits_produced: list[str] = list(map(lambda x: new_segments_used[x], sorted_display))
    final_sum += int("".join(digits_produced))

print(final_sum)