from itertools import product

def get_input_raw() -> list[str]:
    return [line.strip() for line in open("2408test.txt")]

def get_all_char_positions() -> set[tuple[int, int, str]]:
    return {(row_idx, col_idx, character)
            for row_idx, row in enumerate(get_input_raw())
            for col_idx, character in enumerate(row)
            if character != '.'}

def antinodes(character1, character2) -> set[tuple[int, int]]:
    row_idx1, col_idx1, char1 = character1
    row_idx2, col_idx2, char2 = character2
    row_diff, col_diff = abs(row_idx1 - row_idx2), abs(col_idx1 - col_idx2)
    if (row_idx1 >= row_idx2 and col_idx1 >= col_idx2) or (row_idx2 >= row_idx1 and col_idx2 >= col_idx1):
        antinode1 = min(row_idx1, row_idx2) - row_diff, min(col_idx1, col_idx2) - col_diff
        antinode2 = max(row_idx1, row_idx2) + row_diff, max(col_idx1, col_idx2) + col_diff
    else:
        antinode1 = min(row_idx1, row_idx2) - row_diff, max(col_idx1, col_idx2) + col_diff
        antinode2 = max(row_idx1, row_idx2) + row_diff, min(col_idx1, col_idx2) - col_diff
    return {node for node in {antinode1, antinode2} if 0 <= node[0] < 12 and 0 <= node[1] < 12}

def part1():
    all_antinodes = set()
    chars = get_all_char_positions()
    for char1, char2 in [(char1, char2) for char1, char2 in product(chars, chars)
                        if char1[2] == char2[2] and char1 != char2]:
        comb_antinodes = antinodes(char1, char2)
        all_antinodes |= comb_antinodes
    return len(all_antinodes)


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
