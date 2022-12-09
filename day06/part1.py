# part1

# Python solution for part 1 of day 6 of 
# 2022 'Advent of Code'
#
# This code outputs length of the first sub-sequence of
# characters, before which the first occurance of four
# non-repeating characters occurs (inclusive of the four
# # chancarcter)

def num_char_before_distinct(input_fname, num_distinct):
    with open(input_fname) as file:
        for line in file:            
            end = num_distinct
            for end in range(num_distinct, len(line)):
                if (len(set(line[end - num_distinct:end]))
                    == len(line[end - num_distinct:end])):
                    break
        
            print(len(line[:end]))

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    num_char_before_distinct(input_fname, 4)

if __name__ == "__main__":
    main()
