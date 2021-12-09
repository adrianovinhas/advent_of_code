import sys

def is_password_valid(password: str, positions: list[int], char: str) -> bool:
    return (password[positions[0]-1] == char) ^ (password[positions[1]-1] == char)

inputs: list[list[str]] = list(map(lambda x: x[:-1].split(": "), sys.stdin.readlines()))
passwords: list[str] = list(map(lambda x: x[1], inputs))
hints_list: list[tuple[str]] = list(map(lambda x: tuple(x[0].split()), inputs))
hints: list[str, tuple[int]] = list(
    map(lambda x: (x[1], [int(x[0].split("-")[0]), int(x[0].split("-")[1])]), hints_list)
)

valid_passwords = list(
    filter(lambda x: is_password_valid(x[0], x[1][1], x[1][0]), zip(passwords, hints))
)

print(len(valid_passwords))
