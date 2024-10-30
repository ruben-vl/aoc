year = 2021; day = 2
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

def part1():
    lines = [line.strip().split(' ') for line in open(input_file, 'r')]
    pos = 0
    depth = 0
    for line in lines:
        match line[0]:
            case 'forward':
                pos += int(line[1])
            case 'down':
                depth += int(line[1])
            case 'up':
                depth -= int(line[1])
    return pos * depth

def part2():
    lines = [line.strip().split(' ') for line in open(input_file, 'r')]
    pos = 0
    depth = 0
    aim = 0
    for line in lines:
        match line[0]:
            case 'forward':
                pos += int(line[1])
                depth += aim * int(line[1])
            case 'down':
                aim += int(line[1])
            case 'up':
                aim -= int(line[1])
    return pos * depth

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")