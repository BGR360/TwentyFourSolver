"""
This is the brute-force way of finding a solution to a 24 Card.
It just tries every possible combination to find a solution.
"""

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
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            left = result
            right = self.numbers[i]
            operator = self.operations[i - 1]
            result = operator.evaluate(left, right)
        return result

    def to_string(self):
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


def is_correct(solution, value=24):
    """
    Checks if solution evaluates to value
    :param solution: The Solution instance that should be checked
    :param value: The number that we expect solution to evaluate to
    :return: True if solution evaluates to value, False if otherwise
    """
    return solution.evaluate() == value


# Constants for the different Operators
MUL = Operator('*')
ADD = Operator('+')
SUB = Operator('-')
DIV = Operator('/')
OPS = [MUL, ADD, SUB, DIV]

# The 24 card. It's an array of 4 numbers
card = []

# Get the card's numbers from the user
user_input = raw_input("Please enter 4 numbers separated by a space: ")
split_input = user_input.split()
for num_str in split_input:
    card.append(int(num_str))

# The number of different combinations we've tried to find the answer
num_attempts = 0
solution_found = False
current_attempt = Solution()

# First, try multiplying all four numbers
num_attempts += 1
current_attempt.numbers = card
current_attempt.operations = [MUL, MUL, MUL]
if is_correct(current_attempt):
    solution_found = True

# Second, try adding all four numbers
num_attempts += 1
current_attempt.operations = [ADD, ADD, ADD]
if is_correct(current_attempt):
    solution_found = True

# If nothing worked, no solution was found
# Print results
if solution_found:
    print "Solution: %s" % current_attempt.to_string()
else:
    print "No solution found."

print "Number of attempts: %s" % num_attempts