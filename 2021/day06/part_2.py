from collections import Counter
import sys

lanternfish_timers: list[int] = list(map(int, sys.stdin.readline().split(",")))
lanternfishes: Counter = Counter(lanternfish_timers)

days: int = 256
for day in range(days):
    older_lanternfishes: Counter = Counter({timer-1: counts for (timer, counts) in lanternfishes.items()})
    lanternfishes_not_to_breed: Counter = Counter(dict(filter(lambda x: x[0]>-1, older_lanternfishes.items())))
    lanternfishes_to_breed: Counter = Counter(dict(filter(lambda x: x[0]==-1, older_lanternfishes.items())))
    lanternfishes_to_breed_updated: Counter = Counter(dict(map(lambda x: (6, x[1]), lanternfishes_to_breed.items())))

    new_lanternfishes: Counter = Counter(dict(map(lambda x: (8, x[1]), lanternfishes_to_breed.items())))

    # ffs python...
    lanternfishes = Counter()
    lanternfishes.update(lanternfishes_not_to_breed)
    lanternfishes.update(lanternfishes_to_breed_updated)
    lanternfishes.update(new_lanternfishes)

print(sum(lanternfishes.values()))