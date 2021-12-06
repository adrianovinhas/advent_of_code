import sys

inputs: list[str] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

inputs_as_int: list[int] = list(map(int, inputs))
pairs: list[tuple[int, int]] = [(inputs_as_int[i], inputs_as_int[i+1]) for i in range(len(inputs_as_int)-1)]
increased_measurements: list[int] = list(filter(lambda x: x[1]>x[0], pairs))
print(len(increased_measurements))
