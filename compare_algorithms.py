"""
This script runs a multitude of tests on both algorithms to compare their performance.
"""

import sys
import subprocess
from itertools import combinations_with_replacement

# Callable command line statements
execute_brute_force_algorithm = ['python', 'brute_force_algorithm.py']
execute_my_algorithm = ['python', 'my_algorithm.py']

brute_force_attempts = []
my_attempts = []
brute_force_victories = 0
my_victories = 0

total_to_test = len(list(combinations_with_replacement(range(1, 14), 4)))
current_test = 0
print "Total cards to test: %s" % total_to_test

# Test all possible 24 Cards
for card in combinations_with_replacement(range(1, 14), 4):
    current_test += 1
    if current_test % 100 == 0:
        print "%s Cards tested" % current_test

    # print card

    # Convert card to an array of strings
    card_as_str = []
    for num in card:
        card_as_str.append(str(num))

    # Solve the card with both algorithms
    # Defer the output to two separate strings

    s = " "
    brute_force_command = execute_brute_force_algorithm + card_as_str
    my_command = execute_my_algorithm + card_as_str

    brute_force_output = subprocess.check_output(brute_force_command)
    my_output = subprocess.check_output(my_command)

    # Extract data from the output of the scripts
    brute_force_attempt_str = brute_force_output.splitlines()[1]
    my_attempt_str = my_output.splitlines()[1]

    brute_force_attempt = -1
    my_attempt = -1
    if brute_force_attempt_str.find("attempts") > -1:
        brute_force_attempt = int(brute_force_attempt_str.split(' ')[3])
    if my_attempt_str.find("attempts") > -1:
        my_attempt = int(my_attempt_str.split(' ')[3])

    if brute_force_attempt and my_attempt:
        if my_attempt < brute_force_attempt:
            my_victories += 1
        else:
            brute_force_victories += 1

    brute_force_attempts.append(brute_force_attempt)
    my_attempts.append(my_attempt)

# Print out the averages
brute_force_average = sum(brute_force_attempts) / len(brute_force_attempts)
my_average = sum(my_attempts) / len(my_attempts)

print "Average number of attempts for brute-force: %s" % brute_force_average
print "Average number of attempts for my algorithm: %s" % my_average
print "Brute-force victories: %s" % brute_force_victories
print "My algorithm victories: %s" % my_victories
