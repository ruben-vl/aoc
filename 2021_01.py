year = 2021; day = 1
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

def part1():
    lines = [int(line.strip()) for line in open(input_file, 'r')]
    increase_count = 0
    for i in range(1,len(lines)):
        if lines[i] > lines[i-1]:
            increase_count += 1
    return increase_count

def part2():
    lines = [int(line.strip()) for line in open(input_file, 'r')]
    increase_count = 0
    for i in range(3,len(lines)):
        if sum(lines[i-2:i+1]) > sum(lines[i-3:i]):
            increase_count += 1
    return increase_count

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")