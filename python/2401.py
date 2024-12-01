import re


def get_input_parsed():
    day = "2401"
    raw_lines = [line.strip() for line in open(f"{day}.txt", 'r')]
    pattern = r"(\d+)   (\d+)"
    parsed_data = [re.match(pattern, entry).groups() for entry in raw_lines]
    typed_data = [(int(e1), int(e2)) for e1, e2 in parsed_data]
    return typed_data


def part1():
    data = get_input_parsed()
    first_numbers = sorted([f for f, _ in data])
    second_numbers = sorted([f for _, f in data])
    return sum(abs(first_numbers[i] - second_numbers[i]) for i in range(len(first_numbers)))


def part2():
    data = get_input_parsed()
    first_numbers = [f for f, _ in data]
    second_numbers = [f for _, f in data]
    return sum(num * second_numbers.count(num) for num in first_numbers)


if __name__ == "__main__":
    print(f"Part 1: {part1()} (1580061)")
    print(f"Part 2: {part2()} (23046913)")
