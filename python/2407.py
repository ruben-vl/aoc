def get_input_parsed():
    raw_lines = [line.strip().split(':') for line in open("2407.txt", 'r')]
    return [(int(agg), [int(e) for e in items.split()]) for agg, items in raw_lines]

def possible_calcs(nums: list[int], intermediate_res: set[int], concat_enabled: bool) -> set[int]:
    if len(nums) == 0: return intermediate_res
    new_intermediates = set()
    next_elem = nums.pop(0)
    for res in intermediate_res:
        new_intermediates.add(res + next_elem)
        new_intermediates.add(res * next_elem)
        if concat_enabled:
            new_intermediates.add(int(str(res) + str(next_elem)))
    return possible_calcs(nums, new_intermediates, concat_enabled)

def solve(concat_enabled: bool) -> int:
    data = get_input_parsed()
    sum_test_values = 0
    for agg, nums in data:
        possible_res = possible_calcs(nums[1:], {nums[0]}, concat_enabled)
        if agg in possible_res:
            sum_test_values += agg
    return sum_test_values

if __name__ == "__main__":
    print(f"Part 1: {solve(concat_enabled=False)}")
    print(f"Part 2: {solve(concat_enabled=True)}")
