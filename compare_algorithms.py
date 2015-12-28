"""
This script runs a multitude of tests on both algorithms to compare their performance.
"""

import sys
from subprocess import call
from itertools import combinations_with_replacement

# Callable command line statements
execute_brute_force = ['python', 'brute_force_algorithm.py']
execute_my_algorithm = ['python', 'my_algorithm.py']
defer_brute_force_output = ['>', 'brute_force_output.txt']
defer_my_output = ['>', 'my_output.txt']

# Test all possible 24 Cards
for card in combinations_with_replacement(range(1, 14), 4):
    # Convert to an array of strings
    card_as_str = []
    for num in card:
        card_as_str.append(str(num))

    # Solve the card with both algorithms
    call(execute_brute_force + card_as_str)
    call(execute_my_algorithm + card_as_str)

    break
