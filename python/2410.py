def part1() -> int:
    topographic_map = [[int(e) for e in line.strip()] for line in open("2410.txt")]
    trailhead_score = 0
    for row_idx, row in enumerate(topographic_map):
        for col_idx, height in enumerate(row):
            if height == 0:
                all_path_positions = reachable_positions((row_idx, col_idx), topographic_map)
                for pos_row, pos_col in all_path_positions:
                    if topographic_map[pos_row][pos_col] == 9:
                        trailhead_score += 1
    return trailhead_score

def reachable_positions(
        starting_position: tuple[int, int],
        topographic_map: list[list[int]]
) -> set[tuple[int, int]]:
    visited_locations = set()
    locations_to_visit = {starting_position}
    while len(locations_to_visit) > 0:
        next_position = locations_to_visit.pop()
        visited_locations.add(next_position)
        neighbors = reachable_neighbors(next_position, topographic_map)
        locations_to_visit.update(neighbors.difference(visited_locations))
    return visited_locations

def reachable_neighbors(
        position: tuple[int, int],
        topographic_map: list[list[int]]
) -> set[tuple[int, int]]:
    row, col = position
    rows, cols = len(topographic_map), len(topographic_map[0])
    neighbors = {
        (row - 1, col) if row > 0 else None,
        (row + 1, col) if row < rows - 1 else None,
        (row, col - 1) if col > 0 else None,
        (row, col + 1) if col < cols - 1 else None
    }
    reachable_height = topographic_map[row][col] + 1
    return {
        neighbor for neighbor in neighbors
        if neighbor and topographic_map[neighbor[0]][neighbor[1]] == reachable_height
    }


def part2():
    topographic_map = [[int(e) for e in line.strip()] for line in open("2410.txt")]



if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
