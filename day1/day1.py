def main():
    with open("input/input") as f:
        data = [line.rstrip() for line in f]
        
    elves = []
    calories_total = 0
    for el in data:
        if not el:
            elves.append(calories_total)
            calories_total = 0
            continue
        calories_total += int(el)

    elves.sort(reverse=True)
    print(f"Part1: The elf carrying the most Calories is carrying {max(elves)} Calories")
    print(f"Part2: The top three elves are carrying {sum(elves[0:3])} Calories")


if __name__=="__main__":
    main()