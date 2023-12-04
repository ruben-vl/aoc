def part1(data: dict[int, tuple[list[int], list[int]]]):
    return sum(0 if len(set(winning) & set(yours)) == 0 else 2**(len(set(winning) & set(yours))-1) for _, (winning, yours) in data.items())

def part2(data: dict[int, tuple[list[int], list[int]]]):
    card_amount = dict()
    for i in range(1,len(data.keys())+1):
        card_amount[i] = 1
    for card_number, (winning, yours) in data.items():
        matches = len(set(winning) & set(yours))
        for i in range(card_number+1, min(len(data.keys())+1,card_number+matches+1)):
            card_amount[i] += card_amount[card_number]
    return sum(card_amount.values())

if __name__ == "__main__":
    
    data = [l.strip().split(':') for l in open("2023/python/day4_input.txt", 'r')]
    cards = {int(card.split(' ')[-1]): (numbers.split('|')[0], numbers.split('|')[1]) for card, numbers in data}
    cards = {
        card_number: (
            list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), winning.strip().split(' ')))),
            list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), yours.strip().split(' '))))
        ) for card_number, (winning, yours) in cards.items()
    }
    print(f"Part 1: {part1(cards)}")
    print(f"Part 2: {part2(cards)}")
