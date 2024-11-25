import re

def get_input_parsed():
    day = "1502"
    raw_lines = [line.strip() for line in open(f"{day}.txt", 'r')]
    pattern = r"(\d+)x(\d+)x(\d+)"
    parsed_data = [re.match(pattern, entry).groups() for entry in raw_lines]
    typed_data = [(int(l), int(w), int(h)) for l, w, h in parsed_data]
    return typed_data

def surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def smallest_side(l, w, h):
    return min({l*w, w*h, h*l})

def part1():
    data = get_input_parsed()
    return sum(surface_area(l,w,h)+smallest_side(l,w,h) for l,w,h in data)

def smallest_perimeter(l,w,h):
    sorted_sides = sorted([l,w,h])
    return sorted_sides[0]*2 + sorted_sides[1]*2

def ribbon_length(l,w,h):
    return l*w*h

def part2():
    data = get_input_parsed()
    return sum(smallest_perimeter(l,w,h) + ribbon_length(l,w,h) for l,w,h in data)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")