year = 2022; day = 4
input_file = f"{str(year)}_{'0'+str(day) if day < 10 else str(day)}.txt"

def part1():
    lines = [line.strip().split(',') for line in open(input_file, 'r')]
    
    full_overlap_cnts = 0
    for line in lines:
        elf1 = line[0].split('-')
        elf1_sections = set(range(int(elf1[0]), int(elf1[1])+1))
        
        elf2 = line[1].split('-')
        elf2_sections = set(range(int(elf2[0]), int(elf2[1])+1))
        
        if len(elf1_sections & elf2_sections) == len(elf1_sections) \
            or len(elf1_sections & elf2_sections) == len(elf2_sections):
            full_overlap_cnts += 1
    
    return full_overlap_cnts


def part2():
    lines = [line.strip().split(',') for line in open(input_file, 'r')]
    
    overlap_cnts = 0
    for line in lines:
        elf1 = line[0].split('-')
        elf1_sections = set(range(int(elf1[0]), int(elf1[1])+1))
        
        elf2 = line[1].split('-')
        elf2_sections = set(range(int(elf2[0]), int(elf2[1])+1))
        
        if len(elf1_sections | elf2_sections) < len(elf1_sections) + len(elf2_sections):
            overlap_cnts += 1
    
    return overlap_cnts

if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")