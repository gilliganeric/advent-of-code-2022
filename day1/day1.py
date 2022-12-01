"""
Solution for https://adventofcode.com/2022/day/1
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="day1",
        description="Outputs AdventOfCode 2022 Day 1 solution "
                    "for provided input.",
    )
    parser.add_argument("input", help="Input file to process.")
    args = parser.parse_args()

    with open(args.input) as f:
        data = [line.rstrip() for line in f]

    elves = []
    calories_total = 0
    for el in data:
        if not el:
            # we are about to move onto a new elf. save this elf's data and
            # move on
            elves.append(calories_total)
            calories_total = 0
            continue
        calories_total += int(el)
    elves.sort(reverse=True)

    print(
        f"Part1: The elf carrying the most is carrying "
        f"{max(elves)} Calories"
    )
    print(
        f"Part2: The top three elves are carrying "
        f"{sum(elves[0:3])} Calories"
    )


if __name__ == "__main__":
    main()
