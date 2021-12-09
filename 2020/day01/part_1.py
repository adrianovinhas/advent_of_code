from itertools import combinations
from functools import reduce
import sys

inputs: list[int] = list(map(lambda x: int(x[:-1]), sys.stdin.readlines()))

for candidate in combinations(inputs, 2):
    if sum(candidate) == 2020:
        print(reduce(lambda x,y: x*y, candidate))
