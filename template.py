year = 2022; day = 6
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

with open(input_file, 'r') as f:
    input_data = f.read()
lines = [line.strip() for line in open(input_file, 'r')]

def part1():
    pass

def part2():
    pass

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")