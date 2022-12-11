# part1

# Python solution for part 1 of day 8 of 
# 2022 'Advent of Code'
#
# This code outputs the number of trees that are visible
# from outside a grid of trees, given the trees heights
# from 0 (shortest) to 9 (tallest)

def get_trees(input_fname):
    trees = []
    width = 0
    depth = 0
    with open(input_fname) as file:
        first_line = True
        for line in file:
            line = line.replace("\n", "")
            
            if first_line:
                width = len(line)
                first_line = False
                
            for tree in line:
                trees.append(int(tree))
            
            depth += 1
            
    return trees, width, depth

def get_idx(row_num, col_num, width):
    return row_num*width + col_num

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    trees, width, depth = get_trees(input_fname)
    number_visible = 2*width + 2*depth - 4
    
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
            is_visible = (
                trees[curr_idx] > max(row_left)
                or trees[curr_idx] > max(row_right)
                or trees[curr_idx] > max(col_up)
                or trees[curr_idx] > max(col_down)
            )
            if is_visible:
                number_visible += 1
            
    print(number_visible)

if __name__ == "__main__":
    main()
