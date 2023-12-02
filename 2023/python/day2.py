from functools import reduce
from operator import mul

def part1(data: dict[int, list[dict[str, int]]]):
    available = {'red': 12, 'green': 13, 'blue': 14}
    game_id_count = 0
    for game, setlist in data.items():
        possible = True
        for s in setlist:
            for color, amount in s.items():
                if amount > available[color]:
                    possible = False
        if possible:
            game_id_count += game
    return game_id_count

def part2(data: dict[int, list[dict[str, int]]]):
    powers = []
    for setlist in data.values():
        minimum = dict()
        for s in setlist:
            for color, amount in s.items():
                if color in minimum.keys():
                    minimum[color] = max(amount, minimum[color])
                else:
                    minimum[color] = amount
        powers += [reduce(mul, minimum.values())]
    return sum(powers)

if __name__ == "__main__":
    
    day2_input = [l.strip() for l in open('2023/python/day2_input.txt', 'r')]
    game_split = [tuple(game.split(':')) for game in day2_input]
    games = {int(game[5:]): sets.split(';') for game, sets in game_split}
    games = {iden: map(lambda x: x.strip().split(','), set_arr) for iden, set_arr in games.items()}
    games = {iden: list(map(lambda y: {spl.strip().split(' ')[1]: int(spl.strip().split(' ')[0]) for spl in y}, x)) for iden, x in games.items()}
    print(games)
    print(part1(games))
    print(part2(games))