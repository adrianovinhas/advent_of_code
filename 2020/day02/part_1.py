import sys

inputs: list[list[str]] = list(map(lambda x: x[:-1].split(": "), sys.stdin.readlines()))
passwords: list[str] = list(map(lambda x: x[1], inputs))
hints_list: list[tuple[str]] = list(map(lambda x: tuple(x[0].split()), inputs))
hints: list[str, tuple[int]] = list(
    map(lambda x: (x[1], [int(x[0].split("-")[0]), int(x[0].split("-")[1])]), hints_list)
)

valid_passwords = list(
    filter(lambda x: x[0].count(x[1][0]) >= x[1][1][0] and \
                x[0].count(x[1][0]) <= x[1][1][1],
           zip(passwords, hints))
)

print(len(valid_passwords))
