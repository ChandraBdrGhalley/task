################################
# Tandin Wangchuk
# 1. Electrical
# 02230079
################################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
################################
# SOLUTION
# Your Solution Score:47075
# CSF101_CAP/input_7_cap1.txt
################################# Read the input.txt file
def read_input(Input_your_file_name): # We define a fucntion "read_input"
    x = [] # We simply create an empty list
    with open(Input_your_file_name, 'r') as files: # For each line in the file
        for y in files: # Split the lines into two parts using whitespace as the delimiter
            opposition_picked, outcome = y.split() # Create a tuple containing the two parts and append it to the above list
            x.append((opposition_picked, outcome)) # Create a tuple containing the values of 'opposition_picked' and 'outcome', and append it to the list
    return x # Return the list containing 'opposition_picked' and 'outcome'

# Calculating the point for each game/round
def calculate_score(Overall_Games_Played): # Calculates a score based on "Overall_Games_Played"
    Point = 0 # The starting point for each round is 0
    for opposition_picked, outcome in Overall_Games_Played: # Iterate through each game in "Overall_Games_Played" 
# and reveal the values of 'opposition_picked' and 'outcome'
        if outcome == 'X':  # We need to LOSE
            if opposition_picked == 'A': # Opponent chose Rock
                Point += 3 #  Scissor is defeated by Rock
            elif opposition_picked == 'B': # Opponent chose Paper
                Point += 1  # Rock is defeated by paper
            elif opposition_picked == 'C': # Opponent chose Scissors
                Point += 2 # Paper is defeated by Scissors
        elif outcome == 'Y':  # We need to produce a DRAW
            if opposition_picked == 'A': # He/She chose Rock
                Point += 4  # Rock gives draw against Rock
            elif opposition_picked == 'B': # He/She chose Paper
                Point += 5  # Paper gives draw against Paper
            elif opposition_picked == 'C': # He/She chose Scissors
                Point += 6  # Scissors gives draw against Scissors
        elif outcome == 'Z':  # We need to WIN
            if opposition_picked == 'A': # He/She chose Rock
                Point += 8  # Paper wins against Rock
            elif opposition_picked == 'B': # He/She chose Paper
                Point+= 9 # Scissors wins against Paper
            elif opposition_picked == 'C': # He/She chose Scissors
                Point += 7 # Rock wins against Scissor
    print(f"The final accumulation of points is:{Point}") #Printing out the total sum of the points from the input file

# Running the program
Input_your_file_name = "AY.txt"  # The respected Index Number for the students
calculate_score(read_input(Input_your_file_name)) # Calculate the score using the data obtained from reading the input file