year = 2022; day = 6
input_file = f"day{'0'+str(day) if day < 10 else str(day)}_{str(year)}.txt"

def part1():
    with open(input_file, 'r') as f:
        input_data = f.read()

def part2():
    with open(input_file, 'r') as f:
        input_data = f.read()

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")