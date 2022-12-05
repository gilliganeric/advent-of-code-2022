"""
Solution for https://adventofcode.com/2022/day/4
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="day4",
        description="Outputs AdventOfCode 2022 Day 4 solution "
                    "for provided input.",
    )
    parser.add_argument("input", help="Input file to process.")
    args = parser.parse_args()

    with open(args.input) as f:
        data = [line.rstrip() for line in f]

    total_part1_val = 0
    total_part2_val = 0

    print(f"Part1: {total_part1_val}")
    print(f"Part2: {total_part2_val}")


if __name__ == "__main__":
    main()
