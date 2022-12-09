# part2

# Python solution for part 2 of day 4 of 
# 2022 'Advent of Code'
#
# This code outputs the number of elf pairs
# in which one of the elves have been
# assigned a range of section that overlaps
# with the other elf's sections

def overlap(elf1, elf2):
    start1, end1 = elf1
    start2, end2 = elf2
    
    overlap_condition = (
        (start1 >= start2 and end1 <= end2)
        or (start2 >= start1 and end2 <= end1)
        or (start1 <= start2 and end1 >= start2)
        or (start2 <= start1 and end2 >= start1)
    )
    
    return overlap_condition

def to_int_list(list):
    return [int(val) for val in list]

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    total_overlapping = 0
    with open(input_fname) as file:
        for pair in file:
            elf1, elf2 = pair.replace("\n", "").split(",")
            elf1, elf2 = elf1.split("-"), elf2.split("-")
            elf1 = to_int_list(elf1)
            elf2 = to_int_list(elf2)
            
            if overlap(elf1, elf2):
                total_overlapping += 1
              
    print(total_overlapping)  
    
if __name__ == "__main__":
    main()
    