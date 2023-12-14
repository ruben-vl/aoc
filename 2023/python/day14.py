from tqdm import tqdm

def part1(data: list[str]):
    data = roll_north(data)
    return compute_load(data)

def roll_north(data: list[str]) -> list[str]:
    do = True
    while do or previous_data != data:
        do = False
        previous_data = data.copy()
        for row in range(1,len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 'O':
                    if data[row-1][col] == '.':
                        data[row] = data[row][:col] + '.' + data[row][col+1:]
                        data[row-1] = data[row-1][:col] + 'O' + data[row-1][col+1:]
    return data

def compute_load(data: list[str]) -> int:
    total_load = 0
    for row in range(len(data)):
        rock_count = data[row].count('O')
        total_load += (len(data) - row)*rock_count
    return total_load

def part2(data: list[str]):
    pbar = tqdm(total=1000000000)
    for _ in range(1000000000):
        pbar.update(1)
        data = roll_north(data)
        for _ in range(3):
            data = rotate_clockwards(data)
            data = roll_north(data)
    return compute_load(data)

def rotate_clockwards(data: list[str]):
    return list(map("".join, zip(*reversed(data))))


if __name__ == "__main__":
    data = [l.strip() for l in open("2023/python/day14_input.txt", 'r')]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")