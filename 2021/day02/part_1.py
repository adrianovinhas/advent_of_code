from dataclasses import dataclass
from enum import Enum
import sys

class Command(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

@dataclass
class Submarine:
    horizontal: int = 0
    depth: int = 0

def transform_input(line: str) -> tuple[Command, int]:
    split_line: list[str] = line.split(" ")
    return Command(split_line[0]), int(split_line[1])

inputs: list[str] = list(map(lambda x: x[:-1], sys.stdin.readlines()))

inputs_transformed: list[tuple[Command, int]] = list(map(transform_input, inputs))
submarine: Submarine = Submarine()

for input in inputs_transformed:
    if input[0] is Command.FORWARD:
        submarine.horizontal += input[1]
    elif input[0] is Command.DOWN:
        submarine.depth += input[1]
    elif input[0] is Command.UP:
        submarine.depth -= input[1]

print(submarine.horizontal * submarine.depth)