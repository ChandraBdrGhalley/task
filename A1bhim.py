def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def calculate_score(lines):
    # Mapping of opponent's play to the corresponding shape
    opponent_map = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
    # Mapping of the desired outcome to the shape you need to play
    outcome_map = {'X': {'A': 'Scssor', 'B': 'Rock', 'C': 'Paper'},  # To lose
                   'Y': {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'},   # To draw
                   'Z': {'A': 'Paper', 'B': 'Scissor', 'C': 'Rock'}}   # To win
    # Scores for each shape and outcome
    shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

    total_score = 0
    for line in lines:
        opponent_play, desired_outcome = line.split()
        your_shape = outcome_map[desired_outcome][opponent_play]
        # Calculate the score for the shape and the outcome
        round_score = shape_score[your_shape] + outcome_score[desired_outcome]
        total_score += round_score

    return total_score

# Replace 'input_9_cap1.txt' with your actual input file name
input_file_path = 'AY.txt'
lines = read_input(input_file_path)
total_score = calculate_score(lines)
print(f"the total score is: {total_score}")
