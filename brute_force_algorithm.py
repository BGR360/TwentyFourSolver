"""
This is the brute-force way of finding a solution to a 24 Card.
It just tries every possible combination to find a solution.
"""

# The 24 card. It's an array of 4 numbers
card = []

# Get the card's numbers from the user
user_input = raw_input("Please enter 4 numbers separated by a space: ")
split_input = user_input.split()
for num_str in split_input:
    card.append(int(num_str))

# The number of different combinations we've tried to find the answer
num_attempts = 0

