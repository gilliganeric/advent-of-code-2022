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

    print(f"The elf carrying the most Calories is carrying {max(elves)} Calories")


if __name__=="__main__":
    main()