year = 2021; day = 7
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

def part1():
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    
    positions = [int(p) for p in input_data.split(',')]
    fuel_costs = [fuel_cost(align, positions) for align in range(min(positions), max(positions)+1)]

    return min(fuel_costs)

def fuel_cost(align, pos):
    fuel = 0
    for p in pos:
        fuel += abs(p - align)
    return fuel
    
def part2():
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    
    positions = [int(p) for p in input_data.split(',')]
    fuel_costs = [non_linear_fuel_cost(align, positions) for align in range(min(positions), max(positions)+1)]

    return min(fuel_costs)

def non_linear_fuel_cost(align, pos):
    fuel = 0
    for p in pos:
        fuel += (abs(p - align) * (abs(p - align) + 1)) // 2
    return fuel

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")