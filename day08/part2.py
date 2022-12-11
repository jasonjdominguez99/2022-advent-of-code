# part2

# Python solution for part 2 of day 8 of 
# 2022 'Advent of Code'
#
# This code outputs the maximum scenic score of trees in a 
# grid, which is calculated from the distances between a
# a given tree and a tree of the same of greater height
# in each direction

from part1 import get_trees, get_idx

def main():
    # input_fname = "input.txt"
    input_fname = "test_input.txt"
    trees, width, depth = get_trees(input_fname)
    max_scenic_score = 0

if __name__ == "__main__":
    main()
