# part2

# Python solution for part 2 of day 3 of 
# 2022 'Advent of Code'
#
# This code outputs the sum of the priorities of
# items which are the badges for groups of three
# elves from their rucksacks

def get_priority(item):
    return (
        ord(item) - 38 if item.upper() == item 
        else ord(item) - 96
    )

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    with open(input_fname) as file:
        priority_total = 0
        group = []
        for rucksack in file:
            rucksack = rucksack.replace("\n", "")
            group.append(set(rucksack))
            
            if len(group) == 3:
                badge = ""
                for item in group[0]:
                    if item in group[1] and item in group[2]:
                        badge = item
                        break
                
                priority_total += get_priority(badge)
                group = []

    print(priority_total)

if __name__ == "__main__":
    main()
    