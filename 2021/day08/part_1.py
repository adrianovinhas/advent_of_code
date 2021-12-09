import sys

segments_used: dict[int, str] = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

inputs: list[list[str]] = list(map(lambda x: x[:-1].split(" | "), sys.stdin.readlines()))
signal_patterns: list[list[str]] = list(map(lambda x: x[0].split(" "), inputs))
displays: list[list[str]] = list(map(lambda x: x[1].split(" "), inputs))

easy_digits_lengths: list[int] = [len(segments_used[1]),
                                  len(segments_used[4]),
                                  len(segments_used[7]),
                                  len(segments_used[8])]

flatten_digits: list[str] = sum(displays, [])

print(len(list(filter(lambda x: len(x) in easy_digits_lengths,
                      flatten_digits))))
