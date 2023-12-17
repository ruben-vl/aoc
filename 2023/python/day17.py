from queue import PriorityQueue

def get_neighbors(row: int, col: int, nrows: int, ncols: int) -> set[tuple[int, int, int]]:
    neighbors = set()
    if row > 0: neighbors.add((row-1, col, 0))
    if row < nrows-1: neighbors.add((row+1, col, 2))
    if col > 0: neighbors.add((row, col-1, 3))
    if col < ncols-1: neighbors.add((row, col+1, 1))
    return neighbors

def can_continue(path: list[int], nb_dir: int) -> bool:
    return len(path) < 3 or not all(dir == nb_dir for dir in path[-3:])

def part1(heat_loss: list[str]):
    nrows = len(heat_loss)
    ncols = len(heat_loss[0])

    total_loss: list[list[tuple[int, list[list[int]]]]] = [[(float('inf'), []) for _ in range(ncols)] for _ in range(nrows)]
    total_loss[0][0] = (0,[[]])
    to_expand = PriorityQueue()
    to_expand.put((0, (0,0)))
    
    # Flood the total_loss matrix to find the shortest heat loss to any tile
    while not to_expand.empty():
        
        _, (row, col) = to_expand.get()
        
        for nb_row, nb_col, nb_dir in get_neighbors(row, col, nrows, ncols):

            # Only consider neighbor if at least one path can continue to neighbor
            if not all(not can_continue(path, nb_dir) for path in set(map(lambda x: tuple(x),total_loss[row][col][1]))):

                new_loss = total_loss[row][col][0] + int(heat_loss[nb_row][nb_col])

                if new_loss < total_loss[nb_row][nb_col][0]:
 
                    new_dirs = [list(path).copy() for path in set(map(lambda x: tuple(x), total_loss[row][col][1])) if can_continue(path, nb_dir)]
                    for path in new_dirs:
                        path.append(nb_dir)

                    total_loss[nb_row][nb_col] = (new_loss, new_dirs)
                    to_expand.put((new_loss, (nb_row, nb_col)))
                    
                elif new_loss == total_loss[nb_row][nb_col][0]:

                    continuable_paths = [list(path).copy() for path in set(map(lambda x: tuple(x), total_loss[row][col][1])) if can_continue(path, nb_dir)]
                    nb_paths = [list(path).copy() for path in set(map(lambda x: tuple(x), total_loss[nb_row][nb_col][1]))]
                    for path in continuable_paths:
                        path.append(nb_dir)
                    all_paths = list(map(lambda x: list(x), set(map(lambda x: tuple(x), continuable_paths + nb_paths))))
                    total_loss[nb_row][nb_col] = (new_loss, all_paths)
                    to_expand.put((new_loss, (nb_row, nb_col)))
                    
    for row in total_loss:
        print(list(map(lambda x: x[0], [x for x in row])))
    
    # current_loc = (0,0)
    # map_copy = [list(row) for row in heat_loss]
    # for e in total_loss[nrows-1][ncols-1][1]:
    #     match e:
    #         case 0:
    #             current_loc = (current_loc[0]-1, current_loc[1])
    #             map_copy[current_loc[0]][current_loc[1]] = '^'
    #         case 1:
    #             current_loc = (current_loc[0], current_loc[1]+1)
    #             map_copy[current_loc[0]][current_loc[1]] = '>'
    #         case 2:
    #             current_loc = (current_loc[0]+1, current_loc[1])
    #             map_copy[current_loc[0]][current_loc[1]] = 'v'
    #         case 3:
    #             current_loc = (current_loc[0], current_loc[1]-1)
    #             map_copy[current_loc[0]][current_loc[1]] = '<'
    #         case _:
    #             raise RuntimeError("Oeps")
    # for row in map_copy:
    #     print(row)
    
    return total_loss[nrows-1][ncols-1][0]
    

    
    
    
    



def part2(data):
    pass


if __name__ == "__main__":
    input_data = [l.strip() for l in open("2023/python/day17_test.txt", 'r')]
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")