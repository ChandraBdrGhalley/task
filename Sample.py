#It is the function to read input from a file and return a list of lines that are ABC and XYZ.
def read_input():
    required_file = 'input_7_cap1.txt'
    with open(required_file, 'r') as f:
        return [line.strip() for line in f]#strip(); removes any leading and trailing whitespaces from the string


def calculate_score(line):
    total_score_point = 0
    # Assigning score for each shape and outcome. 'A' represents Rock, 'B' represents Paper, and 'C' represents Scissor
    scores_point = {'A': 1, 'B': 2, 'C': 3, 'Win': 6, 'Draw': 3, 'Lose': 0}
    # Winning conditions; Rock defeats Scissors, Scissors defeats Paper, Paper defeats Rock, and Same shape = draw.
    win_conditions = {'A': 'C', 'B': 'A', 'C': 'B'}

    for line in lines:#The for loop helps for iterating over the sequence
        opponent_choice, preferred_outcome = line.split()
        # Determining based on the desired outcome; Y means have to make choice: draw, X means have to make choice: lose, and Z means have to make choice: win
        if preferred_outcome == 'Y':  # If preferred outcome should be Y than it means we should make choice to draw.
            your_choice = opponent_choice
            outcome = 'Draw'
        elif preferred_outcome == 'X':  # If preferred outcome should be X than it means we should make choice to lose.
            your_choice = win_conditions[opponent_choice]
            outcome = 'Lose'
        else:  # If preferred outcome should be Y than it means we should make choice to win.
            your_choice = next(key for key, value in win_conditions.items() if value == opponent_choice)#The next() function is used to retrieve the next item from an iterator.
            outcome = 'Win'

        # Calculating the total score for the round
        collective_score_point = scores_point[your_choice] + scores_point[outcome]
        total_score_point += collective_score_point

    return total_score_point

# Main execution or calling the function 
lines = read_input()
print(f"The total score point is: **{calculate_score(lines)}**")

'''Time complexity of the code is Big O(n) because the code iterates over each line in the file once.
   Space complexity is Big O(n) because the code stores each line from the file as a separate string in a list
'''

