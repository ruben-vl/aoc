from utils.input_parse import (
    single_line_as_string,
    single_line_as_list,
    many_lines_as_list
)

def paper_needed(l: int, w: int, h: int) -> int:
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def ribbon_needed(l: int, w: int, h: int) -> int:
    return 2*sum(sorted([l,w,h])[0:2]) + l*h*w

def part1(data):
    return sum(paper_needed(int(dims[0]), int(dims[1]), int(dims[2])) 
               for dims in (row.strip().split('x') for row in data))

def part2(data):
    return sum(ribbon_needed(int(dims[0]), int(dims[1]), int(dims[2]))
               for dims in (row.strip().split('x') for row in data))

if __name__ == "__main__":
    day = "02"
    year = "2015"
    input_path = f"day{day}_{year}.txt"
    data = many_lines_as_list(input_path)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
