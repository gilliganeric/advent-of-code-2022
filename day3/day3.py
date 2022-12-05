"""
Solution for https://adventofcode.com/2022/day/2
"""
import argparse


def item_value(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1

    if ord(item) >= ord('A') and ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27

    return 0

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

    total_part1_val = 0
    total_part2_val = 0
    rucksacks = []
    for rid, rucksack in enumerate(data):
        rucksacks.append({
            "raw": rucksack,
            "item_set": set(),
            "common": set(),
            "common_val": 0,
            "compartment_sets": [set(), set()]
        })
        for iid, item in enumerate(rucksack):
            rucksacks[rid]["item_set"].add(item)
            cid = 1 if iid >= len(rucksack)/2 else 0
            rucksacks[rid]["compartment_sets"][cid].add(item)
        rucksacks[rid]["common"] = rucksacks[rid]["compartment_sets"][0].\
            intersection(rucksacks[rid]["compartment_sets"][1])

        #for cid in range(0, 2):
            #print(f"R{rid}C{cid}: {rucksacks[rid]['compartment_sets'][cid]}")

        #print(f"R{rid} common: {rucksacks[rid]['common']}")

        assert len(rucksacks[rid]["common"]) == 1
        for el in rucksacks[rid]["common"]:
            rucksacks[rid]["common_val"] = item_value(el)
        total_part1_val += rucksacks[rid]["common_val"]

        if rid > 0 and (rid + 1) % 3 == 0:
            group_badge = rucksacks[rid]["item_set"].intersection(
                rucksacks[rid-1]["item_set"].intersection(
                    rucksacks[rid-2]["item_set"]
                    )
                )
            assert len(group_badge) == 1
            total_part2_val += item_value(group_badge.pop())

    print(f"Part1: {total_part1_val}")
    print(f"Part2: {total_part2_val}")


if __name__ == "__main__":
    main()
