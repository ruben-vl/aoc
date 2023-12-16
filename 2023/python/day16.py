from enum import Enum
from tqdm import tqdm
from multiprocessing import Process, Pool
from functools import partial
import dill

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Beam:

    def __init__(self, row: int, col: int, direction: Direction):
        self.row = row
        self.col = col
        self.direction = direction
    
    def change_direction(self, new_direction: Direction):
        self.direction = new_direction
    
    def change_location(self, new_location: tuple[int, int]):
        self.row = new_location[0]
        self.col = new_location[1]
    
    def next_location(self) -> tuple[int, int]:
        match(self.direction):
            case Direction.UP:
                return (self.row - 1, self.col)
            case Direction.RIGHT:
                return (self.row, self.col + 1)
            case Direction.DOWN:
                return (self.row + 1, self.col)
            case Direction.LEFT:
                return (self.row, self.col - 1)

def part1(grid: list[str], initial_beam: Beam, convergence: int = 25):
    energized_tiles: set[tuple[int, int]] = set()
    beams: set[Beam] = set()

    beams.add(initial_beam)
    
    energized_amount = []
    
    while len(energized_amount) < convergence or energized_amount[-1] > energized_amount[-convergence]:
        for beam in beams.copy():
            next_tile = beam.next_location()
            if outside_grid(next_tile, len(grid), len(grid[0])):
                beams.remove(beam)
            else:
                energized_tiles.add(next_tile)
                beam.change_location(next_tile)
                match beam.direction, grid[next_tile[0]][next_tile[1]]:
                    case Direction.UP, "\\":
                        beam.change_direction(Direction.LEFT)
                    case Direction.UP, "/":
                        beam.change_direction(Direction.RIGHT)
                    case Direction.UP, "-":
                        beam.change_direction(Direction.LEFT)
                        beams.add(Beam(beam.row, beam.col, Direction.RIGHT))
                    case Direction.RIGHT, "\\":
                        beam.change_direction(Direction.DOWN)
                    case Direction.RIGHT, "/":
                        beam.change_direction(Direction.UP)
                    case Direction.RIGHT, "|":
                        beam.change_direction(Direction.UP)
                        beams.add(Beam(beam.row, beam.col, Direction.DOWN))
                    case Direction.DOWN, "\\":
                        beam.change_direction(Direction.RIGHT)
                    case Direction.DOWN, "/":
                        beam.change_direction(Direction.LEFT)
                    case Direction.DOWN, "-":
                        beam.change_direction(Direction.LEFT)
                        beams.add(Beam(beam.row, beam.col, Direction.RIGHT))
                    case Direction.LEFT, "\\":
                        beam.change_direction(Direction.UP)
                    case Direction.LEFT, "/":
                        beam.change_direction(Direction.DOWN)
                    case Direction.LEFT, "|":
                        beam.change_direction(Direction.UP)
                        beams.add(Beam(beam.row, beam.col, Direction.DOWN))
        energized_amount.append(len(energized_tiles))
    
    return len(energized_tiles)

def outside_grid(tile: tuple[int, int], nrows: int, ncols: int):
    return tile[0] >= nrows or tile[0] < 0 or tile[1] >= ncols or tile[1] < 0

def part2(grid: list[str]):
    pbar = tqdm(total = 4*110)
    energized_amounts = []
    for row in range(110):
        start_beam = Beam(row, -1, Direction.RIGHT)
        energized_amounts.append(part1(grid, start_beam))
        pbar.update(1)
        start_beam = Beam(row, 110, Direction.LEFT)
        energized_amounts.append(part1(grid, start_beam))
        pbar.update(1)
    for col in range(110):
        start_beam = Beam(-1, col, Direction.DOWN)
        energized_amounts.append(part1(grid, start_beam))
        pbar.update(1)
        start_beam = Beam(110, col, Direction.UP)
        energized_amounts.append(part1(grid, start_beam))
        pbar.update(1)
    return max(energized_amounts)

def part2_parallel(grid: list[str]):
    input_beams = []
    for i in range(110):
        input_beams.append(Beam(i, -1, Direction.RIGHT))
        input_beams.append(Beam(i, 110, Direction.LEFT))
        input_beams.append(Beam(-1, i, Direction.DOWN))
        input_beams.append(Beam(110, i, Direction.UP))
    with Pool(processes=8) as pool:
        result = pool.map(partial(part1, grid), input_beams)
    return max(result)


if __name__ == "__main__":
    with open("2023/python/day16_input.txt", 'r') as f:
        day16_input = [l.strip() for l in f]
    print(f"Part 1: {part1(day16_input, Beam(0, -1, Direction.RIGHT))}")
    print(f"Part 2: {part2_parallel(day16_input)}")
