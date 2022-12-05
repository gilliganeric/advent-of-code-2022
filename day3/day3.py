"""
Solution for https://adventofcode.com/2022/day/2
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="day3",
        description="Outputs AdventOfCode 2022 Day 3 solution "
                    "for provided input.",
    )
    parser.add_argument("input", help="Input file to process.")
    args = parser.parse_args()

    with open(args.input) as f:
        data = [line.rstrip() for line in f]

    print("Hello, world!")


if __name__ == "__main__":
    main()
