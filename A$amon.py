# Function to read input from a file and return a list of lines.
def read_input(file_path):
    with open(file_path, 'r') as file:
        # Strip each line of any leading/trailing whitespace and return as a list
        return [line.strip() for line in file]

# Function to calculate the total score from the input lines.
def calculate_score(lines):
    # Scores for each shape and outcome
    shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'Win': 6, 'Draw': 3, 'Lose': 0}

    # Initialize the total score
    total_score = 0

    # Iterate over each line in the input
    for line in lines:
        opponent_play, desired_outcome = line.split()
        your_shape = ''
        round_score = 0

        # Determine your shape based on the desired outcome and opponent's play
        if desired_outcome == 'Y':  # Draw
            your_shape = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}[opponent_play]
            round_score = shape_score[your_shape] + outcome_score['Draw']

        elif desired_outcome == 'X':  # Lose
            your_shape = {'A': 'Scissors', 'B': 'Rock', 'C': 'Paper'}[opponent_play]
            round_score = shape_score[your_shape] + outcome_score['Lose']

        elif desired_outcome == 'Z':  # Win
            your_shape = {'A': 'Paper', 'B': 'Scissors', 'C': 'Rock'}[opponent_play]
            round_score = shape_score[your_shape] + outcome_score['Win']

        # Add the round score to the total score
        total_score += round_score

    # Return the final total score
    return total_score

# Main execution: Read the input, calculate the score, and print it
input_file_path = 'AY.txt'
lines = read_input(input_file_path)
print(f"The total score is: {calculate_score(lines)}")
