year = 2022; day = 6
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

def part1():
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
        
    for i in range(4,len(input_data)):
        if len(set(input_data[i-4:i])) == 4:
            return i
    
    return None

def part2():
    with open(input_file, 'r') as f:
        input_data = f.read()
        
    for i in range(14,len(input_data)):
        if len(set(input_data[i-14:i])) == 14:
            return i
    
    return None

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")