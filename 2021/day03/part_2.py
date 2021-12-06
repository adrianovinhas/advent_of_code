from collections import Counter
from enum import Enum
import sys

class Rating(Enum):
    OXYGEN = 0
    CO2 = 1

def apply_bit_criteria(inputs: list[list[str]],
                       bit_index: int,
                       rating_type: Rating) -> list[list[str]]:

    if len(inputs) <= 1:
        return inputs

    inputs_transformed: list[list[str]] = list(map(list, inputs))
    inputs_transposed: list[list[str]] = list(map(list, zip(*inputs_transformed)))
    bits_counts: list[list[tuple[str, int]]] = list(map(lambda x: Counter(x).most_common(), inputs_transposed))

    tie_breaker_bit: str = "1" if rating_type == Rating.OXYGEN else "0"
    bit_counts: list[str] = bits_counts[bit_index]
    bit_to_pick: str = bit_counts[rating_type.value][0] if bit_counts[0][1] != bit_counts[1][1] else tie_breaker_bit
    filtered_inputs: list[list[str]] = list(filter(lambda x: x[bit_index] == bit_to_pick, inputs))

    return apply_bit_criteria(filtered_inputs, bit_index+1, rating_type)


inputs: list[str] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

oxygen_generator_rating: int = int(apply_bit_criteria(inputs, 0, Rating.OXYGEN)[0], 2)
co2_scrubber_rating: int = int(apply_bit_criteria(inputs, 0, Rating.CO2)[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)
