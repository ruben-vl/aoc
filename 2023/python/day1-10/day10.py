from functools import reduce
from operator import concat
import math

def part1(new_map: list[str], ) -> tuple[int, list[str]]:
    original = new_map.copy()
    old_map = []
    while old_map != new_map:
        old_map = new_map.copy()
        for idx, e in enumerate(new_map):
            if e.isnumeric():
                original_shape = '|' if e == '0' else original[idx]
                for i in accessible_neighbours(idx, new_map, int(math.sqrt(len(new_map))), original_shape):
                    if new_map[i].isnumeric():
                        new_map[i] = min(new_map[i], str(int(e)+1))
                    else:
                        new_map[i] = str(int(e)+1)
    return max([int(c) for c in new_map if c.isnumeric()]), new_map

def accessible_neighbours(idx: int, map: list[str], dim: int, original_shape: str) -> set[int]:
    res = set()
    if original_shape in ['|', 'L', 'J'] and idx >= dim and map[idx-dim] in ['T', 'F', '|']:
        res.add(idx-dim)
    if original_shape in ['|', 'T', 'F'] and idx < dim*dim-dim and map[idx+dim] in ['L', 'J', '|']:
        res.add(idx+dim)
    if original_shape in ['-', 'J', 'T'] and idx % dim != 0 and map[idx-1] in ['L', 'F', '-']:
        res.add(idx-1)
    if original_shape in ['-', 'L', 'F'] and idx % dim != (dim-1) and map[idx+1] in ['J', 'T', '-']:
        res.add(idx+1)
    return res

def part2(loop_map: list[str], original_map: list[str]) -> int:
    in_count = 0
    out = True
    last_bend = None
    for idx, e in enumerate(loop_map):
        if e.isnumeric() and original_map[idx] == '|':
            out = not out
        elif e.isnumeric() and original_map[idx] == 'L':
            last_bend = 'L'
        elif e.isnumeric() and original_map[idx] == 'J':
            if last_bend == 'F':
                out = not out
            elif last_bend == 'L':
                last_bend = None
        elif e.isnumeric() and original_map[idx] == 'F':
            last_bend = 'F'
        elif e.isnumeric() and original_map[idx] == 'T':
            if last_bend == 'L':
                out = not out
            elif last_bend == 'F':
                last_bend = None
        elif not e.isnumeric() and not out:
            in_count += 1
    return in_count


if __name__ == "__main__":
    data = list(reduce(concat, [l.strip() for l in open("2023/python/day10_input.txt", 'r')]).replace('7','T').replace('S', '0'))
    original = data.copy()
    result, loop_map = part1(data)
    print(f"Part 1: {result}")
    original = list(map(lambda x: '|' if x == '0' else x, original))
    print(f"Part 2: {part2(loop_map, original)}")
