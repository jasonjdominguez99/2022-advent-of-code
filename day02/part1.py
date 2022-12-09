# part1

# Python solution for part 1 of day 2 of 
# 2022 'Advent of Code'
#
# This code outputs the total score from rounds of
# rock-paper-scissors games

get_score = {"X": 1, "Y": 2, "Z": 3}
get_same = {"X": "A", "Y": "B", "Z": "C"}
beaten_by = {"X": "C", "Y": "A", "Z": "B"}

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    with open(input_fname) as file:
        total_score = 0
        for line in file:
            [opp_move, user_move] = line.replace("\n", "").split(" ")
            
            total_score += get_score[user_move]
            
            if opp_move == beaten_by[user_move]:
                total_score += 6
            elif opp_move == get_same[user_move]:
                total_score += 3
    
    print(total_score)

if __name__ == "__main__":
    main()
    