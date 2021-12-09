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

def find_basin(low_point: tuple[int], height_map: list[list[int]]) -> list[int]:
    nearby_points: list[tuple[int]] = [(low_point[0]+1, low_point[1]),
                                       (low_point[0]-1, low_point[1]),
                                       (low_point[0], low_point[1]+1),
                                       (low_point[0], low_point[1]-1)]
    height_lowest: int = height_map[low_point[0]][low_point[1]]

    filtered_nearby_points: list[tuple[int]] = \
        list(filter(lambda x: height_map[x[0]][x[1]]>height_lowest and height_map[x[0]][x[1]]!=9,
                    nearby_points))

    if len(filtered_nearby_points) == 0:
        return [low_point]
    return sum(map(lambda x: [low_point] + find_basin(x, height_map),
                   filtered_nearby_points), [])
    

inputs: list[list[int]] = list(map(lambda x: list(map(int, x[:-1])), sys.stdin.readlines()))
n_rows: int = len(inputs)
n_columns: int = len(inputs[0])
amended_inputs: list[list[int]] = list(map(lambda x: [9] + x + [9], inputs))

final_inputs: list[list[int]] = [[9] * (n_columns+2)] + amended_inputs + [[9] * (n_columns+2)]
final_inputs_t: list[list[int]] = list(map(list, zip(*final_inputs)))

horizontal_mins = find_mins(final_inputs)[1:-1]

vertical_mins = find_mins(final_inputs_t)[1:-1]
vertical_mins_t = list(map(list, zip(*vertical_mins)))

low_points: list[tuple[int]] = list(get_low_points(horizontal_mins, vertical_mins_t))

length_basins: list[int] = list(
    map(lambda x: len(set(find_basin((x[0]+1, x[1]+1), final_inputs))), low_points)
)

sorted_basins: list[int] = sorted(length_basins, reverse=True)
print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])