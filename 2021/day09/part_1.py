from more_itertools import sliding_window
import sys
from typing import Iterable

def find_mins(height_map: list[list[int]]) -> list[tuple[int]]:
    return list(
                map(lambda row:
                    list(
                        map(lambda x:
                            x[0] if x[1][0]>x[1][1] and x[1][2]>x[1][1] else None,
                            enumerate(sliding_window(row, 3))
                        )
                    ),
                    height_map)
            )

def get_low_points(horizontal_mins: list[list[int]],
                   vertical_mins_t: list[list[int]]) -> Iterable[tuple[int]]:
    for row_h, row_v in zip(horizontal_mins, vertical_mins_t):
        for i,j in zip(row_h, row_v):
            if i is not None and j is not None:
                yield (j,i)

inputs: list[list[int]] = list(map(lambda x: list(map(int, x[:-1])), sys.stdin.readlines()))
n_rows: int = len(inputs)
n_columns: int = len(inputs[0])
amended_inputs: list[list[int]] = list(map(lambda x: [10] + x + [10], inputs))

final_inputs: list[list[int]] = [[10] * (n_columns+2)] + amended_inputs + [[10] * (n_columns+2)]
final_inputs_t: list[list[int]] = list(map(list, zip(*final_inputs)))

horizontal_mins = find_mins(final_inputs)[1:-1]

vertical_mins = find_mins(final_inputs_t)[1:-1]
vertical_mins_t = list(map(list, zip(*vertical_mins)))

low_points: list[tuple[int]] = list(get_low_points(horizontal_mins, vertical_mins_t))
print(sum(list(map(lambda x: inputs[x[0]][x[1]] + 1, low_points))))
