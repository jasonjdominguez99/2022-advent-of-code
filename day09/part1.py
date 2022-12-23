# part1

# Python solution for part 1 of day 9 of 
# 2022 'Advent of Code'
#
# This code outputs the number of positions visted once
# by the tail of a rope which much stay adjacent to the
# head of the rope as it moves

def move(curr_pos, direction):
    if direction == "R":
        return (curr_pos[0] + 1, curr_pos[1])
    elif direction == "L":
        return (curr_pos[0] - 1, curr_pos[1])
    elif direction == "U":
        return (curr_pos[0], curr_pos[1] + 1)
    elif direction == "D":
        return (curr_pos[0], curr_pos[1] - 1)
    
def move_tail(tail_pos, head_pos, direction):
    if ((tail_pos[0] != head_pos[0]) and (tail_pos[1] != head_pos[1])):
        if abs(tail_pos[0] - head_pos[0]) == 1:
            tail_pos = (head_pos[0], tail_pos[1])
        else:
            tail_pos = (tail_pos[0], head_pos[1])
            
    return move(tail_pos, direction)
    
def is_touching(head_pos, tail_pos):
    is_touching = (
        (head_pos == tail_pos)
        or (head_pos == (tail_pos[0], tail_pos[1] + 1))
        or (head_pos == (tail_pos[0] + 1, tail_pos[1]))
        or (head_pos == (tail_pos[0], tail_pos[1] - 1))
        or (head_pos == (tail_pos[0] - 1, tail_pos[1]))
        or (head_pos == (tail_pos[0] + 1, tail_pos[1] + 1))
        or (head_pos == (tail_pos[0] + 1, tail_pos[1] - 1))
        or (head_pos == (tail_pos[0] - 1, tail_pos[1] - 1))
        or (head_pos == (tail_pos[0] - 1, tail_pos[1] + 1))
    )
    
    return is_touching

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    
    with open(input_fname) as file:
        positions_visited = {(0, 0)}
        head_position = (0, 0)
        tail_position = (0, 0)
        for line in file:
            line = line.replace("\n", "").split(" ")
            
            direction = line[0]
            n_steps = int(line[1])
            
            for i in range(n_steps):
                head_position = move(head_position, direction)
                if not is_touching(head_position, tail_position):
                    tail_position = move_tail(tail_position, head_position, direction)
                    if tail_position not in positions_visited:
                        positions_visited.add(tail_position)
            
    print(len(positions_visited))        

if __name__ == "__main__":
    main()
