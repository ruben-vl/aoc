import random


def aoc_problem() -> tuple[int, int]:
    return random.randint(2015, 2024), random.randint(1, 25)


if __name__ == "__main__":
    year, day = aoc_problem()
    print(f"Year {year}, day {day}")
