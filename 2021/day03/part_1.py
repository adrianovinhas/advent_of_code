from collections import Counter
import sys

inputs: list[str] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

inputs_transformed: list[list[str]] = list(map(list, inputs))
inputs_transposed: list[list[str]] = list(map(list, zip(*inputs_transformed)))

bits_counts: list[list[tuple[str, int]]] = list(map(lambda x: Counter(x).most_common(), inputs_transposed))
gamma_rate: int = int("".join(list(map(lambda x: x[0][0], bits_counts))), 2)
epsilon_rate: int = int("".join(list(map(lambda x: x[-1][0], bits_counts))), 2)

print(gamma_rate * epsilon_rate)
