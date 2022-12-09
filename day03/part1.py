# part1

# Python solution for part 1 of day 3 of 
# 2022 'Advent of Code'
#
# This code outputs the sum of the priorities of
# items which have been placed in the wrong
# compartments in rucksacks

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
        for rucksack in file:
            rucksack = rucksack.replace("\n", "")
            size = len(rucksack)
            comp1, comp2 = set(rucksack[:size//2]), set(rucksack[size//2:])
            
            misplaced_item = ""
            for item in comp1:
                if item in comp2:
                    misplaced_item = item
                    break
            
            priority_total += get_priority(misplaced_item)
    
    print(priority_total)        

if __name__ == "__main__":
    main()
    