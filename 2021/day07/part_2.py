from collections import Counter
import sys
from typing import Iterator


def calculate_fuel_costs(crab_counters: Counter) -> Iterator[int]:
    max_crab_position: int = max(crab_counters.keys())
    for position in range(max_crab_position):
        # Alternative 1 (slower)
        #fuel_costs = {k: sum([i for i in range(1, abs(k-position)+1)]) for k in crab_counters.keys()}
        # Alternative 2 (triangular number)
        fuel_costs = {k: abs(k-position)*(abs(k-position)+1)//2 for k in crab_counters.keys()}
        total_fuels = sum([crab_counters[k] * fuel_costs[k] for k in crab_counters.keys()])
        yield total_fuels

crab_positions: list[int] = list(map(int, sys.stdin.readline().split(",")))
crab_counters: Counter = Counter(crab_positions)

print(min(calculate_fuel_costs(crab_counters)))

