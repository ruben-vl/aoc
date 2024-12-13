import alphashape

def get_garden_map() -> list[str]:
    return [line.strip() for line in open("2412test.txt")]

def part1():
    garden_map = get_garden_map()
    checked: set[tuple[int, int]] = set()
    regions: set[tuple[tuple[int,int],...]] = set()
    perimeters: dict[tuple[int, int], int] = dict()
    for ri in range(len(garden_map)):
        for ci in range(len(garden_map[0])):
            if (ri, ci) not in checked:
                symbol = garden_map[ri][ci]
                new_region: set[tuple[int,int]] = set()
                to_check: set[tuple[int,int]] = {(ri, ci)}
                while len(to_check) > 0:
                    next_plot = to_check.pop()
                    new_region.add(next_plot)
                    neighbors = get_neighbors(next_plot, garden_map)
                    relevant_neighbors = {(nr, nc) for nr, nc in neighbors
                                          if (nr, nc) not in new_region and garden_map[nr][nc] == symbol}
                    perimeters[next_plot] = 4-len({(nr, nc) for nr, nc in neighbors if garden_map[nr][nc] == symbol})
                    to_check.update(relevant_neighbors)
                checked.update(new_region)
                regions.add(tuple(new_region))
                # print(f"A region of {symbol} plants with price {len(new_region)} * {sum([perimeters[plot] for plot in new_region])}")
    return sum([len(region)*sum([perimeters[plot] for plot in region]) for region in regions])


def get_neighbors(
        coordinates: tuple[int, int],
        garden_map: list[str]
) -> set[tuple[int, int]]:
    row, col = coordinates
    return {neighbor for neighbor in {
        (row-1, col) if row != 0 else None,
        (row+1, col) if row != len(garden_map)-1 else None,
        (row, col-1) if col != 0 else None,
        (row, col+1) if col != len(garden_map[0])-1 else None
    } if neighbor is not None}

def part2():
    garden_map = get_garden_map()
    checked: set[tuple[int, int]] = set()
    regions: set[tuple[tuple[int, int], ...]] = set()
    perimeters: dict[tuple[int, int], int] = dict()
    for ri in range(len(garden_map)):
        for ci in range(len(garden_map[0])):
            if (ri, ci) not in checked:
                symbol = garden_map[ri][ci]
                new_region: set[tuple[int, int]] = set()
                to_check: set[tuple[int, int]] = {(ri, ci)}
                while len(to_check) > 0:
                    next_plot = to_check.pop()
                    new_region.add(next_plot)
                    neighbors = get_neighbors(next_plot, garden_map)
                    relevant_neighbors = {(nr, nc) for nr, nc in neighbors
                                          if (nr, nc) not in new_region and garden_map[nr][nc] == symbol}
                    perimeters[next_plot] = 4 - len({(nr, nc) for nr, nc in neighbors if garden_map[nr][nc] == symbol})
                    to_check.update(relevant_neighbors)
                checked.update(new_region)
                regions.add(tuple(new_region))
    return sum([len(region) * sides(region) for region in regions])

def sides(region: tuple[tuple[int,int],...]) -> int:
    alpha = alphashape.optimizealpha([(float(x), float(y)) for x, y in region])
    hull = alphashape.alphashape(list(region), alpha)
    s = len(hull.exterior.coords)
    interiors = hull.interiors
    for interior in interiors:
        s += len(interior)
    # return len(hull.exterior.coords) + len(hull.interiors)
    return s

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
