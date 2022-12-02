"""
Solution for https://adventofcode.com/2022/day/2
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="day2",
        description="Outputs AdventOfCode 2022 Day 2 solution "
                    "for provided input.",
    )
    parser.add_argument("input", help="Input file to process.")
    args = parser.parse_args()

    with open(args.input) as f:
        data = [line.rstrip() for line in f]

    shape_score = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    LOSE = 0
    DRAW = 3
    WIN = 6
    outcome_score = {
        'A X': DRAW,
        'A Y': WIN,
        'A Z': LOSE,

        'B X': LOSE,
        'B Y': DRAW,
        'B Z': WIN,

        'C X': WIN,
        'C Y': LOSE,
        'C Z': DRAW,
    }

    total_score = 0
    for round in data:
        player = round.split(' ')[1]
        score = shape_score[player] + outcome_score[round]
        total_score += score

    print(total_score)


if __name__ == "__main__":
    main()
