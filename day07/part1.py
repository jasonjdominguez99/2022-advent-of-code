# part1

# Python solution for part 1 of day 7 of 
# 2022 'Advent of Code'
#
# This code outputs the total size of all directories
# in a computer filesystem (each less than 100000), given
# the terminal output after exploring the filesystem

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    with open(input_fname) as file:
        filesystem = {}
        get_prev_dir = {}
        curr_dir = ""
        for line in file:
            line = line.replace("\n", "").split(" ")
            
            if line[0] == "$":
                if line[1] == "cd":
                    directory = line[-1]
                    if directory == "..":
                        curr_dir = get_prev_dir[curr_dir]
                    elif directory not in get_prev_dir:
                        filesystem[directory] = []
                        get_prev_dir[directory] = curr_dir
                        curr_dir = directory
                
            elif len(line) == 2 and line[0] != "dir":
                print(line)
                directory = curr_dir
                while True:
                    filesystem[directory].append(int(line[0]))
                    directory = get_prev_dir[directory]
                    
                    if directory == "":
                        break
    
    total = 0
    for directory in filesystem.values():
        size = sum(directory)
        if size <= 100000:
            total += size
    
    print(total)

if __name__ == "__main__":
    main()
