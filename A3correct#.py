def read_input():
    # Replace 'input.txt' with the path to your actual input file
    file_path = 'input_7_cap1.txt'
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def calculate_score(lines):
    total_score = 0
    # Scores for each shape and outcome
    scores = {'A': 1, 'B': 2, 'C': 3, 'Win': 6, 'Draw': 3, 'Lose': 0}
    # Winning conditions
    win_conditions = {'A': 'C', 'B': 'A', 'C': 'B'}

    for line in lines:
        opponent_choice, desired_outcome = line.split()
        # Determine your choice based on the desired outcome
        if desired_outcome == 'Y':  # Draw
            your_choice = opponent_choice
            outcome = 'Draw'
        elif desired_outcome == 'X':  # Lose
            your_choice = win_conditions[opponent_choice]
            outcome = 'Lose'
        else:  # Win
            your_choice = next(key for key, value in win_conditions.items() if value == opponent_choice)
            outcome = 'Win'

        # Calculate the score for this round
        round_score = scores[your_choice] + scores[outcome]
        total_score += round_score

    return total_score

# Main execution
lines = read_input()
if lines:
    print(f"The total score is: **{calculate_score(lines)}**")
else:
    print("No lines to process or file not found.")
