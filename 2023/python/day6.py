from functools import reduce
from operator import mul
from tqdm import tqdm

def part1(records: list[tuple[int, int]]):
    ways_to_win = {time: 0 for time, _ in records}
    for time, record in records:
        for hold in range(1, time+1):
            distance = (time-hold)*hold
            if distance > record:
                ways_to_win[time] += 1
    return reduce(mul, ways_to_win.values())

def part2(time, record):
    pbar = tqdm(total=time+1)
    wins = 0
    for hold in range(1, time+1):
        pbar.update(1)
        distance = (time-hold)*hold
        if distance > record:
            wins += 1
    return wins

if __name__ == "__main__":
    
    records1 = [(61, 430), (67, 1036), (75, 1307), (71, 1150)]
    print(f"Part 1: {part1(records1)}")
    print(f"Part 2: {part2(61677571, 430103613071150)}")