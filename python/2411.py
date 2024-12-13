from functools import lru_cache

def get_starting_stones():
    return ["7725", "185", "2", "132869", "0", "1840437", "62", "26310"]

@lru_cache(maxsize=None)
def next_number(current_number: str) -> tuple[str, ...]:
    if current_number == "0":
        return "1",
    length = len(current_number)
    if length % 2 == 0:
        return str(int(current_number[:length//2])), str(int(current_number[length//2:]))
    return str(int(current_number)*2024),

def part1():
    stones = get_starting_stones()
    for i in range(25):
        new_stones = []
        for stone in stones:
            new_stones += list(next_number(stone))
        stones = new_stones
    return len(stones)

@lru_cache(maxsize=None)
def len_after_n_iterations(num, it):
    if it == 0:
        return 1

    count = 0
    next_num = next_number(num)
    for n in next_num:
        count += len_after_n_iterations(n, it-1)
    return count

def part2():
    stones = get_starting_stones()
    count = 0
    for stone in stones:
        count += len_after_n_iterations(stone, 75)
    return count


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")