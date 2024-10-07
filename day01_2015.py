from utils.input_parse import (
    single_line_as_string,
    single_line_as_list
)

def part1(data):
    return data.count('(') - data.count(')')

def part2(data):
    position = 0
    for index, item in enumerate(data):
        if item == "(":
            position += 1
        elif item == ")":
            position -= 1
        if position < 0:
            return index + 1

if __name__ == "__main__":
    day = "01"
    year = "2015"
    input_path = f"day{day}_{year}.txt"
    data = single_line_as_string(input_path)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
