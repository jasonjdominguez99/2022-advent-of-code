# part1

# Python solution for part 1 of day 10 of 
# 2022 'Advent of Code'
#
# This code outputs ...

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    # input_fname = "short_test_input.txt"
    
    cycle_num = 1
    X = 1
    signal_strengths = []
    with open(input_fname) as file:
        for line in file:
            line = line.replace("\n", "").split()
            
            if line[0] == "noop":
                if (cycle_num == 20) or ((cycle_num - 20)%40 == 0):
                    signal_strengths.append(cycle_num*X)
                # print(str(cycle_num) + ": " + str(X))
                cycle_num += 1
            elif line[0] == "addx":
                for i in range(2):
                    if (cycle_num == 20) or ((cycle_num - 20)%40 == 0):
                        signal_strengths.append(cycle_num*X)
                    # print(str(cycle_num) + ": " + str(X))
                    cycle_num += 1
                    
                X += int(line[1])
                
                # print(str(cycle_num) + ": " + str(X))
                
        if (cycle_num == 20) or ((cycle_num - 20)%40 == 0):
            signal_strengths.append(cycle_num*X)
            
    # print(signal_strengths)
    print(sum(signal_strengths))

if __name__ == "__main__":
    main()
