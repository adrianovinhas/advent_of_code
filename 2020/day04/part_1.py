from itertools import combinations
from functools import reduce
import sys


for input in sys.stdin.readline():
    d = input[:-1].split(" ")
inputs: list[list[str]] = list(map(lambda x: x[:-1].split(" "), sys.stdin.readlines()))
print(inputs)
passports = list(
    map(lambda i: list(map(lambda x: tuple(x.split(":")), i)),
        inputs)
)
print(passports)
