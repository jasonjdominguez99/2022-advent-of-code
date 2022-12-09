# part1

# Python solution for part 1 of day 6 of 
# 2022 'Advent of Code'
#
# This code outputs length of the first sub-sequence of
# characters, before which the first occurance of four
# non-repeating characters occurs (inclusive of the four
# # chancarcter)

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    with open(input_fname) as file:
        for line in file:            
            end = 4
            for end in range(4, len(line)):
                if len(set(line[end - 4:end])) == len(line[end - 4:end]):
                    break
        
            print(len(line[:end]))

if __name__ == "__main__":
    main()
    