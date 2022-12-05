"""
Solution for https://adventofcode.com/2022/day/4
"""
import argparse

def a_contains_b(a, b):
    a_range = range(int(a[0]), int(a[1]) + 1)
    b_range = range(int(b[0]), int(b[1]) + 1)
    a_set = set(a_range)
    b_set = set(b_range)
    if a_set.issuperset(b_set):
        return True
    return False


def a_overlaps_b(a, b):
    a_range = range(int(a[0]), int(a[1]) + 1)
    b_range = range(int(b[0]), int(b[1]) + 1)

    a_set = set(a_range)
    b_set = set(b_range)

    return not a_set.isdisjoint(b_set)


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
    for d in data:
        pair = d.split(",")
        pair[0] = pair[0].split("-")
        pair[1] = pair[1].split("-")
        if a_contains_b(pair[0], pair[1]):
            total_part1_val += 1
            print(f"{pair[0]} contains {pair[1]}")
        elif a_contains_b(pair[1], pair[0]):
            total_part1_val += 1
            print(f"{pair[1]} contains {pair[0]}")

        if a_overlaps_b(pair[0], pair[1]):
            total_part2_val += 1
        else:
            print(f"{pair[0]} doesn't overlap {pair[1]}")

    print(f"Part1: {total_part1_val}")
    print(f"Part2: {total_part2_val}")


if __name__ == "__main__":
    main()
