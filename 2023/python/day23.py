from functools import lru_cache
from queue import PriorityQueue

def part1(map: list[str]):
    start_tile = (0, map[0].index('.'))
    end_tile = (len(map)-1, map[len(map)-1].index('.'))
    
    longest_path = dict()
    
    queue = PriorityQueue()
    queue.put((0, [start_tile]))
    
    while not queue.empty():
        
        length, path = queue.get()
        neighbors = get_neighbors(path[-1], tuple(map), tuple(path))
        
        for neighbor in neighbors:
            if neighbor not in longest_path.keys():
                longest_path[neighbor] = (0, None)
            if length-1 <= longest_path[neighbor][0]:
                longest_path[neighbor] = (length-1, path.copy() + [neighbor])
                queue.put((length-1, path.copy() + [neighbor]))
    
    for row, col in longest_path[end_tile][1]:
        map[row] = map[row][:col] + 'O' + map[row][col+1:]
    for row in map:
        print(row)
    return -longest_path[end_tile][0]

@lru_cache
def get_neighbors(loc, map, visited):
    row, col = loc
    neighbors = set()
    if row > 0 and map[row-1][col] in ['.', '^'] and (row-1, col) not in visited:
        neighbors.add((row-1, col))
    if row < len(map)-1 and map[row+1][col] in ['.', 'v'] and (row+1, col) not in visited:
        neighbors.add((row+1, col))
    if col > 0 and map[row][col-1] in ['.', '<'] and (row, col-1) not in visited:
        neighbors.add((row, col-1))
    if col < len(map[0])-1 and map[row][col+1] in ['.', '>'] and (row, col+1) not in visited:
        neighbors.add((row, col+1))
    return neighbors

def part2(map: list[str]):
    for row in range(len(map)):
        map[row] = map[row].replace('^', '.').replace('<', '.').replace('>', '.').replace('v', '.')
    return part1(map)

if __name__ == "__main__":
    
    input_data = [l.strip() for l in open("2023/python/day23_test.txt")]
    print(f"Part 1: {part1(input_data.copy())}")
    print(f"Part 2: {part2(input_data.copy())}")