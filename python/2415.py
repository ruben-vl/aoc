test = False
MAP = "2415testmap.txt" if test else "2415map.txt"
MOVES = "2415testmoves.txt" if test else "2415moves.txt"

def get_warehouse_map() -> list[str]:
    return [line.strip() for line in open(MAP)]

def get_robot_moves() -> str:
    return "".join([line.strip() for line in open(MOVES)])

def initial_robot_location(warehouse_map: list[str]) -> tuple[int, int]:
    return {
        (row_index, column_index)
        for row_index, row in enumerate(warehouse_map)
        for column_index, ch in enumerate(row)
        if ch == "@"
    }.pop()

def initial_box_locations(warehouse_map: list[str]) -> set[tuple[int, int]]:
    return {
        (row_index, column_index)
        for row_index, row in enumerate(warehouse_map)
        for column_index, ch in enumerate(row)
        if ch == "O"
    }

def wall_locations(warehouse_map: list[str]) -> set[tuple[int, int]]:
    return {
        (row_index, column_index)
        for row_index, row in enumerate(warehouse_map)
        for column_index, ch in enumerate(row)
        if ch == "#"
    }

def get_object_locations(warehouse_map: list[str]) -> dict[str, tuple[int, int] | set[tuple[int, int]]]:
    return {
        "robot": initial_robot_location(warehouse_map),
        "boxes": initial_box_locations(warehouse_map),
        "walls": wall_locations(warehouse_map)
    }

def move_vector(move: str) -> tuple[int, int]:
    return {"^": (-1,0), "v": (1,0), "<": (0,-1), ">": (0,1)}[move]

def move_object(location: tuple[int, int], vector: tuple[int, int], obj_loc) -> bool:
    next_location = location[0] + vector[0], location[1] + vector[1]
    if next_location in obj_loc["walls"]:
        return False
    if next_location in obj_loc["boxes"]:
        if move_object(next_location, vector, obj_loc):
            if location == obj_loc["robot"]:
                obj_loc["robot"] = next_location
                return True
            elif location in obj_loc["boxes"]:
                obj_loc["boxes"].add(next_location)
                obj_loc["boxes"].remove(location)
                return True
            else:
                raise RuntimeError("Normally this doesn't happen 1")
        return False
    if location == obj_loc["robot"]:
        obj_loc["robot"] = next_location
        return True
    elif location in obj_loc["boxes"]:
        obj_loc["boxes"].add(next_location)
        obj_loc["boxes"].remove(location)
        return True
    else:
        raise RuntimeError("Normally this doesn't happen 2")

def part1():
    warehouse_map = get_warehouse_map()
    object_locations = get_object_locations(warehouse_map)
    robot_moves = get_robot_moves()
    for move in robot_moves:
        move_object(object_locations["robot"], move_vector(move), object_locations)
    return sum([100*box_row + box_col for box_row, box_col in object_locations["boxes"]])


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
