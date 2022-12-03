# part1

# Python solution for part 1 of day 1 of 2022 'Advent of Code'
#
# This code outputs the highest calorie count for elves
# from an input file where different elf calories are
# separated an empty line

def main():
    max_calorie_count = 0
    with open("input.txt") as file:
        calorie_count = 0
        for line in file:
            if line == "\n":
                max_calorie_count = max(max_calorie_count, calorie_count)
                calorie_count = 0
            else:
                calorie_count += int(line.replace("\n", ""))
        max_calorie_count = max(max_calorie_count, calorie_count)
    
    print(max_calorie_count)

if __name__ == "__main__":
    main()
    