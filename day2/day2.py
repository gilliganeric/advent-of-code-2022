"""
Solution for https://adventofcode.com/2022/day/2
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="day1",
        description="Outputs AdventOfCode 2022 Day 2 solution "
                    "for provided input.",
    )
    parser.add_argument("input", help="Input file to process.")
    args = parser.parse_args()

    with open(args.input) as f:
        data = [line.rstrip() for line in f]

    print(data)


if __name__ == "__main__":
    main()
