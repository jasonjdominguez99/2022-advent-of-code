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
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    trees, width, depth = get_trees(input_fname)
    max_scenic_score = 0
    
    for i in range(1, width - 1):
        row_start = get_idx(i, 0, width)
        row_end = get_idx(i, width - 1, width)
        
        for j in range(1, depth - 1):
            col_start = get_idx(0, j, width)
            col_end = get_idx(depth - 1, j, width)
            
            curr_idx = get_idx(i, j, width)
            
            row_left = trees[row_start:curr_idx]
            row_right = trees[curr_idx + 1:row_end + 1]
            col_up = trees[col_start:curr_idx:width]
            col_down = trees[curr_idx + width:col_end + width:width]
            
            directions = [row_left[::-1], row_right, col_up[::-1], col_down]
            
            scenic_score = 1
            for direction in directions:
                viewing_distance = 0
                
                for tree in direction:
                    viewing_distance += 1
                    if tree >= trees[curr_idx]:
                        break
                
                scenic_score *= viewing_distance
            
            max_scenic_score = max(max_scenic_score, scenic_score)
           
    print(max_scenic_score)     

if __name__ == "__main__":
    main()
