def turn_on(grid: set[tuple[int, int]], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid.add((x,y))
    return grid

def turn_off(grid: set[tuple[int, int]], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x,y) in grid:
                grid.remove((x,y))
    return grid

def toggle(grid: set[tuple[int, int]], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x,y) in grid:
                grid.remove((x,y))
            else:
                grid.add((x,y))
    return grid

def parse_instruction(instruction: str):
    parts = instruction.split()
    
    action = parts[0]
    if action == "turn":
        action = parts[1]
        x1, y1 = map(int, parts[2].split(','))
        through = parts.index("through")
        x2, y2 = map(int, parts[through + 1].split(','))
    else:
        x1, y1 = map(int, parts[1].split(','))
        through = parts.index("through")
        x2, y2 = map(int, parts[through + 1].split(','))
    
    return action, x1, y1, x2, y2

def apply_instruction(grid, instruction):
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    if action == "on":
        grid = turn_on(grid, x1, y1, x2, y2)
    elif action == "off":
        grid = turn_off(grid, x1, y1, x2, y2)
    elif action == "toggle":
        grid = toggle(grid, x1, y1, x2, y2)
    return grid

def increase_brightness_by_1(grid: dict[tuple[int, int], int], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x,y) in grid.keys():
                grid[(x,y)] += 1
            else:
                grid[(x,y)] = 1
    return grid

def decrease_brightness_by_1(grid: dict[tuple[int, int], int], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x,y) in grid.keys() and grid[(x,y)] > 0:
                grid[(x,y)] -= 1
    return grid

def increase_brightness_by_2(grid: dict[tuple[int, int], int], x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x,y) in grid.keys():
                grid[(x,y)] += 2
            else:
                grid[(x,y)] = 2
    return grid

def apply_instruction_part_2(grid: dict[tuple[int, int], int], instruction: str):
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    if action == "on":
        grid = increase_brightness_by_1(grid, x1, y1, x2, y2)
    elif action == "off":
        grid = decrease_brightness_by_1(grid, x1, y1, x2, y2)
    elif action == "toggle":
        grid = increase_brightness_by_2(grid, x1, y1, x2, y2)
    return grid

if __name__ == "__main__":
    path = "2015/python/day6_input.txt"
    with open(path) as f:
        data = [s.rstrip() for s in f.readlines()]

    grid = set()

    for instruction in data:
        grid = apply_instruction(grid, instruction)
    
    print(f"Part one: {len(grid)}")

    grid_new = dict()

    for instruction in data:
        grid_new = apply_instruction_part_2(grid_new, instruction)

    total_brightness = 0
    for _, v in grid_new.items():
        total_brightness += v
    
    print(f"Part two: {total_brightness}")