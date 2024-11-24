import re

def get_input_parsed():
    raw_lines = [line.strip() for line in open("2002.txt", 'r')]
    pattern = r"(\d+)-(\d+) (\w): (.+)"
    parsed_data = [re.match(pattern, entry).groups() for entry in raw_lines]
    typed_data = [(int(lower), int(upper), char, string) for lower, upper, char, string in parsed_data]
    return typed_data

def part1():
    data = get_input_parsed()
    valid_count = 0
    for lower, upper, char, string in data:
        char_count = string.count(char)
        if lower <= char_count <= upper:
            valid_count += 1
    return valid_count

def part2():
    data = get_input_parsed()
    valid_count = 0
    for idx1, idx2, char, string in data:
        if (string[idx1-1] == char) ^ (string[idx2-1] == char):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")