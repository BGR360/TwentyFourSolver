"""
This is the brute-force way of finding a solution to a 24 Card.
It just tries every possible combination to find a solution.
"""

import sys
from itertools import permutations
from itertools import product

class Operator(object):
    """
    Represents an operator ('*', '+', '-', '/') used in solving a 24 Card.
    """
    def __init__(self, op):
        self.op = op

    def evaluate(self, left, right):
        """
        Evaluates the result of multiplying/adding/subtracting/dividing left and right
        :param left: The left operand
        :param right: The right operand
        :return: The result of executing the operator on the two operands
        """
        if self.op == '*':
            return left * right
        elif self.op == '+':
            return left + right
        elif self.op == '-':
            return left - right
        elif self.op == '/':
            return left / right
        else:
            return "Error"

    def __repr__(self):
        return str(self.op)

class Solution(object):
    """
    Represents a potential solution to a 24 Card.
    Has an array of 4 numbers and an array of 3 operations.
    A Solution does not necessarily have to be correct.
    """
    numbers = []
    operations = []

    def __init__(self):
        pass

    def evaluate(self):
        """
        Evaluates the result of this Solution.
        Executes the 3 operations (in order) on the 4 numbers (in order).
        num1 <op1> num2 <op2> num3 <op3> num4
        :return: The result of evaluating the Solution.
        """
        if len(self.numbers) > 0:
            result = self.numbers[0]
            for i in range(1, len(self.numbers)):
                left = result
                right = self.numbers[i]
                operator = self.operations[i - 1]
                result = operator.evaluate(left, right)
            return result
        else:
            return False

    def __repr__(self):
        """
        Makes a human-readable string to represent this Solution
        :return The string representation of this Solution
        """
        result = str(self.numbers[0])
        for i in range(1, len(self.numbers)):
            op = self.operations[i - 1].op
            num = self.numbers[i]
            result += " " + op + " " + str(num)
        return result


def is_numeric(string):
    """
    Checks if a string is numeric (as in alphanumeric without the alpha)
    :param string: The string we want to check
    :return: True if the string is numeric, False if not
    """
    return string.isalnum() and not string.isalpha()

def is_correct(solution, value=24):
    """
    Checks if solution evaluates to value
    :param solution: The Solution instance that should be checked
    :param value: The number that we expect solution to evaluate to
    :return: True if solution evaluates to value, False if otherwise
    """
    return solution.evaluate() == value



def solve_card(card):
    """
    This is the big cahuna; it solves the 24 Card using the brute-force algorithm
    :param card: An array representing the 24 Card
    :return: Returns an array where the first element is a Solution instance if a solution was found, and False if no
    solution was found. The second element is always the number of attempts that were made to solve it.
    """

    # Constants for the different Operators
    MUL = Operator('*')
    ADD = Operator('+')
    SUB = Operator('-')
    DIV = Operator('/')
    OPS = [MUL, ADD, SUB, DIV]

    # The number of different combinations we've tried to find the answer
    num_attempts = 0
    current_attempt = Solution()

    # The brute force algorithm simply tests all possible permutations of the numbers
    # and the operators between them
    for number_perm in permutations(card):
        for operator_perm in product(OPS, repeat=3):
            num_attempts += 1
            current_attempt.numbers = number_perm
            current_attempt.operations = operator_perm
            # print "Testing: %s" % current_attempt
            if is_correct(current_attempt):
                return [current_attempt, num_attempts]

    # If nothing worked, no solution was found
    return [False, num_attempts]



# The 24 card. It's an array of 4 numbers
card = []

# Get the card's numbers from the user (or from the program's arguments)
if len(sys.argv) <= 1:
    user_input = raw_input("Please enter 4 numbers separated by a space: ")
    split_input = user_input.split()
    for num_str in split_input:
        card.append(int(num_str))
else:
    for arg in sys.argv[1:]:
        if is_numeric(arg):
            card.append(int(arg))

# Solve the card
result = solve_card(card)
solution = result[0]
num_attempts = result[1]

# Print results
if solution != False:
    print "Solution: %s" % solution
else:
    print "No solution found."

print "Number of attempts: %s" % num_attempts