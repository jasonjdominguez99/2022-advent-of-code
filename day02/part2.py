# part2

# Python solution for part 2 of day 2 of 
# 2022 'Advent of Code'
#
# This code outputs the total score from rounds of
# rock-paper-scissors games, given that the second
# column tells you the outcome of the round

outcome_to_score = {"X": 0, "Y": 3, "Z": 6}
get_user_move_score = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

def main():
    input_fname = "input.txt"
    # input_fname = "test_input.txt"
    with open(input_fname) as file:
        total_score = 0
        for line in file:
            [opp_move, outcome] = line.replace("\n", "").split(" ")
            
            total_score += outcome_to_score[outcome]
            total_score += get_user_move_score[opp_move][outcome]
            
    print(total_score)

if __name__ == "__main__":
    main()
    