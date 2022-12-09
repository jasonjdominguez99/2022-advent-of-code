# part2

# Python solution for part 2 of day 6 of 
# 2022 'Advent of Code'
#
# This code outputs length of the first sub-sequence of
# characters, before which the first occurance of 14
# non-repeating characters occurs (inclusive of the 14
# # chancarcter)

from part1 import num_char_before_distinct

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    num_char_before_distinct(input_fname, 14)

if __name__ == "__main__":
    main()
