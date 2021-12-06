import sys
    
lanternfish_timers: list[int] = list(map(int, sys.stdin.readline().split(",")))

days: int = 80
for day in range(days):
    tmp_timers: list[int] = list(map(lambda x: x-1, lanternfish_timers))
    offspring_counts: int = tmp_timers.count(-1)
    new_lanternfish_timers = list(map(lambda x: x if x > -1 else 6, tmp_timers)) + \
        [8] * offspring_counts

    lanternfish_timers = new_lanternfish_timers

print(len(lanternfish_timers))