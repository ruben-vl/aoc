year = 2022; day = 1
input_file = f"day{'0'+str(day) if day < 10 else str(day)}_{str(year)}.txt"

def part1():
    with open(input_file, 'r') as f:
        input_data = f.read()

    elves = input_data.split('\n\n')
    calorie_counts = [sum(map(int, elf.strip().split('\n'))) for elf in elves]

    return max(calorie_counts)

def part2():
    with open(input_file, 'r') as f:
        input_data = f.read()

    elves = input_data.split('\n\n')
    calorie_counts = [sum(map(int, elf.strip().split('\n'))) for elf in elves]

    calorie_counts.sort(reverse=True)
    return sum(calorie_counts[:3])

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")