from collections import Counter
import sys
from typing import Iterator


def calculate_fuel_costs(crab_counters: Counter) -> Iterator[int]:
    max_crab_position: int = max(crab_counters.keys())
    for position in range(max_crab_position):
        fuel_costs = {k: abs(k-position) for k in crab_counters.keys()}
        total_fuels = sum([crab_counters[k] * fuel_costs[k] for k in crab_counters.keys()])
        yield total_fuels

crab_positions: list[int] = list(map(int, sys.stdin.readline().split(",")))
crab_counters: Counter = Counter(crab_positions)

print(min(calculate_fuel_costs(crab_counters)))

