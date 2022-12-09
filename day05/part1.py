# part1

# Python solution for part 1 of day 5 of 
# 2022 'Advent of Code'
#
# This code outputs the letters of the crates
# at the top of the stacks after rearranging
# with the given instructions

def read_stacks(file):
    stacks = {}
    num_stacks = 0
    first_line = True
    for line in file:
        if line == "\n" or line[:2] == " 1":
            break
        
        line = line.replace("\n", "")
        
        if first_line:
            num_stacks = len(line)//3
            for i in range(1, num_stacks + 1):
                stacks[i] = []
            first_line = False
           
        stack_num = 1      
        for i in range(0, len(line), 4):
            if line[i + 1] != " ":
                stacks[stack_num].append(line[i + 1])
            
            stack_num += 1
            
    for i in stacks.keys():
        stacks[i] = stacks[i][::-1]
            
    return stacks

def parse_instruction(instruction):
    ins = instruction.replace("\n", "").split(" ")
    return {
        ins[0]: int(ins[1]),
        ins[2]: int(ins[3]),
        ins[4]: int(ins[5])
    }
    
def read_instructions(file):
    instructions = []
    for line in file:
        if line == "\n":
            continue
        instructions.append(parse_instruction(line))
    
    return instructions

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    stacks = {}
    instructions = []
    with open(input_fname) as file:
        stacks = read_stacks(file)
        instructions = read_instructions(file)
        
    for ins in instructions:
        for i in range(ins["move"]):
            stacks[ins["to"]].append(stacks[ins["from"]].pop())
           
    output = "" 
    for stack in stacks.values():
        if stack != []:
            output += stack[-1]
        
    print(output)

if __name__ == "__main__":
    main()
    