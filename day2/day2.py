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
        'A': 1,
        'B': 2,
        'C': 3,
    }
    LOSE = 0
    DRAW = 3
    WIN = 6
    player_shape = {
        'A X': 'Z',
        'A Y': 'X',
        'A Z': 'Y',

        'B X': 'X',
        'B Y': 'Y',
        'B Z': 'Z',

        'C X': 'Y',
        'C Y': 'Z',
        'C Z': 'X',
    }
    outcome_score_part1 = {
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
    outcome_score_part2 = {
        'X': LOSE,
        'Y': DRAW,
        'Z': WIN
    }

    total_score_part1 = total_score_part2 = 0
    for round in data:
        player = round.split(' ')[1]
        score_part1 = shape_score[player] + outcome_score_part1[round]
        score_part2 = shape_score[player_shape[round]] + outcome_score_part2[player]
        total_score_part1 += score_part1
        total_score_part2 += score_part2

    print(total_score_part1)
    print(total_score_part2)


if __name__ == "__main__":
    main()
