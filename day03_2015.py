from utils.input_parse import (
    single_line_as_string,
    single_line_as_list,
    many_lines_as_list
)

def visited_locations(data):
    visited = set()
    santa_x = 0
    santa_y = 0
    visited.add((santa_x, santa_y))
    for instruction in data:
        match instruction:
            case 'v':
                santa_y -= 1
            case '>':
                santa_x += 1
            case '<':
                santa_x -= 1
            case '^':
                santa_y += 1
        visited.add((santa_x, santa_y))
    return visited

def part1(data):
    return len(visited_locations(data))

def part2(data):
    visited_santa = visited_locations(data[0::2])
    visited_robo_santa = visited_locations(data[1::2])
    return len(visited_santa | visited_robo_santa)

if __name__ == "__main__":
    day = "03"
    year = "2015"
    input_path = f"day{day}_{year}.txt"
    data = single_line_as_string(input_path)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
