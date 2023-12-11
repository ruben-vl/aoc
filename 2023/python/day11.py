from functools import reduce
from operator import concat

def part1(sky: list[str], part2: bool = False):
    empty_rows = [idx for idx, row in enumerate(sky) if not '#' in row]
    columns = [''.join([row[i] for row in sky]) for i in range(len(sky[0]))]
    empty_cols = [idx for idx, col in enumerate(columns) if not '#' in col]
    
    stars_idx_2d = [(row_idx, col_idx) 
                   for row_idx, row in enumerate(sky) 
                   for col_idx, ch in enumerate(row) if ch == '#']
    
    return sum([distance(s1_idx, s2_idx, empty_rows, empty_cols, part2)
                for s1_idx in stars_idx_2d for s2_idx in stars_idx_2d]) // 2

def distance(star1_idx, star2_idx, empty_rows, empty_cols, part2: bool):
    dist = abs(star1_idx[0] - star2_idx[0]) + abs(star1_idx[1] - star2_idx[1])
    row_expansions = [idx for idx in empty_rows if (idx > star1_idx[0] and idx < star2_idx[0]) or (idx < star1_idx[0] and idx > star2_idx[0])]
    col_expansions = [idx for idx in empty_cols if (idx > star1_idx[1] and idx < star2_idx[1]) or (idx < star1_idx[1] and idx > star2_idx[1])]
    return dist + (999999 if part2 else 1)*len(row_expansions) + (999999 if part2 else 1)*len(col_expansions)


if __name__ == "__main__":
    sky = [l.strip() for l in open("2023/python/day11_input.txt", 'r')]
    print(f"Part 1: {part1(sky)}")
    print(f"Part 2: {part1(sky, True)}")