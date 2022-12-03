# part1

# Python solution for part 2 of day 1 of 2022 'Advent of Code'
#
# This code outputs the total calories of the top three
# elves with the most calories from an input file where
# different elf calories are separated an empty line

def main():
    elf_calories = []
    # input_fname = "test_input.txt"
    input_fname = "input.txt"
    with open(input_fname) as file:
        calorie_count = 0
        for line in file:
            if line == "\n":
                elf_calories.append(calorie_count)
                calorie_count = 0
            else:
                calorie_count += int(line.replace("\n", ""))
        elf_calories.append(calorie_count)
    
    # print(elf_calories)
    # print(sorted(elf_calories)[-3:])
    print(sum(sorted(elf_calories)[-3:]))

if __name__ == "__main__":
    main()
    