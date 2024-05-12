def calculate_score(file_path):
    # Scores for each shape and outcome
    shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'Win': 6, 'Draw': 3, 'Lose': 0}

    # Read file and calculate score
    total_score = 0
    with open('AY.txt', 'r') as file:
        for line in file:
            opponent_play, desired_outcome = line.strip().split()
            your_shape = ''
            round_score = 0

            # Determine your shape based on the desired outcome and opponent's play
            if desired_outcome == 'Y':  # Draw
                if opponent_play == 'A':
                    your_shape = 'Rock'
                elif opponent_play == 'B':
                    your_shape = 'Paper'
                elif opponent_play == 'C':
                    your_shape = 'Scissors'
                round_score = shape_score[your_shape] + outcome_score['Draw']

            elif desired_outcome == 'X':  # Lose
                if opponent_play == 'A':
                    your_shape = 'Scissors'
                elif opponent_play == 'B':
                    your_shape = 'Rock'
                elif opponent_play == 'C':
                    your_shape = 'Paper'
                round_score = shape_score[your_shape] + outcome_score['Lose']

            elif desired_outcome == 'Z':  # Win
                if opponent_play == 'A':
                    your_shape = 'Paper'
                elif opponent_play == 'B':
                    your_shape = 'Scissors'
                elif opponent_play == 'C':
                    your_shape = 'Rock'
                round_score = shape_score[your_shape] + outcome_score['Win']

            total_score += round_score

    return total_score

# Input file path
input_file_path = 'AY.txt'
total_score = calculate_score(input_file_path)
print(f"the total score is: {total_score}")
