from itertools import zip_longest
import sys

Vent = list[tuple[int, int]]


def build_vent(vent: Vent) -> set[Vent]:

    horizontal_step: int = 1 if vent[0][0] < vent[1][0] else -1
    vertical_step: int = 1 if vent[0][1] < vent[1][1] else -1
    horizontal_range: list[int] = list(range(vent[0][0], vent[1][0], horizontal_step)) + [vent[1][0]]
    vertical_range: list[int] = list(range(vent[0][1], vent[1][1], vertical_step)) + [vent[1][1]]
    
    filler_value: int = vent[0][0] if len(horizontal_range)==1 else vent[0][1]
    return set([(i,j) for i,j in zip_longest(horizontal_range,
                                             vertical_range,
                                             fillvalue=filler_value)])


str_to_tuple_int = lambda string: tuple(map(int, string.split(",")))

inputs: list[list[str]] = list(map(lambda x: x[:-1].split(" -> "), sys.stdin.readlines()))
vents: list[Vent] = list(map(lambda i: list(map(str_to_tuple_int, i)), inputs))
straight_vents: list[Vent] = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], vents))

extended_vents: list[set[tuple[int, int]]] = [build_vent(vent) for vent in straight_vents]

intersections: set[tuple[int, int]] = set()
for i in range(len(extended_vents)-1):
    for j in range(i+1, len(extended_vents)):
        intersections.update(list(extended_vents[i].intersection(extended_vents[j])))

print(len(intersections))