import sys

def generate_pairs(iterable: list[int],
                   sliding_window: int=3) -> list[tuple[int, int]]:
    return [
        (sum(iterable[i: i+sliding_window]),
         sum(iterable[i+1: i+1+sliding_window]))
         for i in range(len(inputs_as_int)-sliding_window)
    ]


inputs: list[str] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

inputs_as_int: list[int] = list(map(int, inputs))
pairs: list[tuple[int, int]] = generate_pairs(inputs_as_int)
increased_measurements: list[int] = list(filter(lambda x: x[1]>x[0], pairs))
print(len(increased_measurements))
