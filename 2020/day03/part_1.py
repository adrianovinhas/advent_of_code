from itertools import combinations
from functools import reduce
import sys

inputs: list[list[str]] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

move_right: int = 3
move_down: int = 1

n_columns: int = len(inputs[0])
stops = [(move_down*row, (move_right*row)%n_columns) for row in range(len(inputs))]

print(len(list(filter(lambda x: inputs[x[0]][x[1]] == "#", stops))))