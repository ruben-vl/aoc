import re

def get_input_parsed():
    day = ""
    raw_lines = [line.strip() for line in open(f"{day}.txt", 'r')]
    pattern = r""
    parsed_data = [re.match(pattern, entry).groups() for entry in raw_lines]
    typed_data = [int(elem) for elem in parsed_data]
    return typed_data

def part1():
    pass

def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")