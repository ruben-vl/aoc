from tqdm import tqdm

def part1(seed_numbers: list[int], maps: dict[str, list[list[int]]]):
    locations = []
    pbar = tqdm(total=len(seed_numbers))
    for seed in seed_numbers:
        pbar.update(1)
        for r in maps["seed-to-soil"]:
            soil = get_destination(seed, r)
            if soil is not None:
                break
        if soil is None:
            soil = seed
        for r in maps["soil-to-fertilizer"]:
            fertilizer = get_destination(soil, r)
            if fertilizer is not None:
                break
        if fertilizer is None:
            fertilizer = soil
        for r in maps["fertilizer-to-water"]:
            water = get_destination(fertilizer, r)
            if water is not None:
                break
        if water is None:
            water = fertilizer
        for r in maps["water-to-light"]:
            light = get_destination(water, r)
            if light is not None:
                break
        if light is None:
            light = water
        for r in maps["light-to-temperature"]:
            temperature = get_destination(light, r)
            if temperature is not None:
                break
        if temperature is None:
            temperature = light
        for r in maps["temperature-to-humidity"]:
            humidity = get_destination(temperature, r)
            if humidity is not None:
                break
        if humidity is None:
            humidity = temperature
        for r in maps["humidity-to-location"]:
            location = get_destination(humidity, r)
            if location is not None:
                break
        if location is None:
            location = humidity
        locations.append(location)
    return min(locations)
        
        
def get_destination(number: int, range_list: list[int]):
    if number is None:
        return None
    if number >= range_list[1] and number < range_list[1] + range_list[2]:
        return range_list[0] + (number - range_list[1])
    else:
        return None

def part2(seed_numbers: list[int], maps: dict[str, list[list[int]]]):
    seed_range_minima = []
    for i in range(0,20,2):
        print(f"Range {i}")
        seed_range_minima.append(part1(list(range(seed_numbers[i], seed_numbers[i]+seed_numbers[i+1])), maps))
    return min(seed_range_minima)

if __name__ == "__main__":
    seed_numbers = [
        768975, 36881621, 
        56868281, 55386784, 
        1828225758, 1084205557, 
        2956956868, 127170752, 
        1117192172, 332560644, 
        357791695, 129980646, 
        819363529, 9145257, 
        993170544, 70644734, 
        3213715789, 312116873, 
        3107544690, 59359615
    ]

    maps: dict[str, list[list[int]]] = dict()
    current_map = ""
    for line in open("2023/python/day5_input.txt", "r"):
        if not line[0].isnumeric() and not line[0] == '\n':
            map_name = line.split(' ')[0]
            maps[map_name] = []
            current_map = map_name
        elif line[0].isnumeric():
            maps[current_map].append(list(map(lambda x: int(x), line.strip().split(' '))))
    
    print(part1(seed_numbers, maps))
    print(part2(seed_numbers, maps))