from functools import reduce
import sys
from typing import Iterator

def calculate_trees(map: list[list[str]], slopes: list[tuple[int]]) -> Iterator[int]:
    n_columns: int = len(inputs[0])
    n_rows: int = len(inputs)
    for slope in slopes:
        stops: list[tuple[int]] = [(slope[1]*row, (slope[0]*row)%n_columns)
                                   for row in range(len(inputs))]
        
        filtered_stops: list[tuple[int]] = \
            list(filter(lambda x: x[0]<n_rows, stops))
        n_trees: int = len(list(filter(lambda x: inputs[x[0]][x[1]] == "#", filtered_stops)))
        yield n_trees

inputs: list[list[str]] = list(map(lambda x: x[:-1], sys.stdin.readlines()))
slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

n_trees: list[int] = calculate_trees(inputs, slopes)
print(reduce(lambda x,y: x*y, n_trees))