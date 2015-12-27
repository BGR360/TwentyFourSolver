"""
This is my custom algorithm for finding a solution to a 24 Card (or to any card).
Hopefully it should be smarter than the brute-force algorithm.


Theory behind the algorithm:

When humans try to solve a 24 Card, they don't think in a brute-force way. Humans are smart.
When I try to solve a 24 Card, I think of FACTORS. Factors are very important. Normally, I'll try to find a factor
of 24 on my card and see if I can arrange the other 3 numbers to make the other factor (e.g. my card has a 4 in
it, can I use the other 3 numbers to make 4 so that I can multiply 4 * 6?).


Generalizing:

I figured that I could make this algorithm recursive. What I imagined was this: I'd pick one number from the
card, and then see if the other 3 numbers can make the other number that I need. What this inherently necessitates is
a general function which can answer this question:
        > Given n numbers, can you use arithmetic to arrive at an answer x?

Or more programmatically written as:
        > solution(array, x)    # array has size n


My algorithm in a nutshell:

Given n numbers (stored in array A), can you use arithmetic to arrive at x?

1.  If n = 1:
    a)  If A[0] = x, then yes
    b)  If A[0] != x, then no

2.  Try adding all the numbers in A together.

3.  Try multiplying all the numbers in A together.

4.  If there are factors of x in A, pick one.
    * Prefer 1 as a factor of x, and then prefer smaller factors
    a)  See if the other n - 1 numbers can make the other factor of x
        i)  If so, then yes
        ii) If not, then pick another factor

5.  If there are no more factors of x in A, then for each number a in A:
    a)  SUBTRACT a from x
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, try the next number

6.  If that fails, then for each number a in A:
    a)  ADD a to x
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, try the next number

7.  If that fails, then for each number a in A:
    a)  MULTIPLY x by a
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, then no solution
"""

from math import sqrt

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
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            left = result
            right = self.numbers[i]
            operator = self.operations[i - 1]
            result = operator.evaluate(left, right)
        return result

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


# Constants for the different Operators
MUL = Operator('*')
ADD = Operator('+')
SUB = Operator('-')
DIV = Operator('/')
OPS = [MUL, ADD, SUB, DIV]

# The number of different combinations we've tried to find the answer
num_attempts = 0
current_attempt = Solution()
final_solution = None


def get_factors(n):
    """
    Returns all the factors of n.
    Code for this method can be attributed to user agf on StackExchange
    :param n: An integer
    :return: A list of whole-number factors of n
    """
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))

def exclude(lst, value):
    """
    Returns lst excluding the first occurrence of value. Performs a deep copy in doing so.
    This is useful when we want to pass the n - 1 "other" numbers to another recursion of our solve() method.
    :param lst: The list we want to exclude value from
    :param value: The value we want to exclude
    :return: lst with the first occurrence of value excluded from it.
    """
    other_lst = lst[:]  # Perform a deep copy so we can safely modify it
    other_lst.remove(value)
    return other_lst


def is_correct(solution, value=24):
    """
    Checks if solution evaluates to value
    :param solution: The Solution instance that should be checked
    :param value: The number that we expect solution to evaluate to
    :return: True if solution evaluates to value, False if otherwise
    """
    return solution.evaluate() == value


def solve(numbers, value):
    """
    Uses arithmetic (*, +, -, /) to arrive at value, using my custom recursive algorithm
    :param numbers: The list of numbers we're going to use to arrive at value
    :param value: The value that we want to arrive at using all of the
    :return: If solvable, returns a Solution instance. If not, returns False.
    """
    # Referring to the global variables we want to modify
    global num_attempts
    global current_attempt

    # Begin my algorithm
    solution = Solution()
    n = len(numbers)

    # 1. If n = 1
    if n < 1:
        return False
    if n == 1:
        if numbers[0] == value:
            solution.numbers = [value]
            solution.operations = []
            return solution
        else:
            return False

    # 2.  Try adding all the numbers together.
    num_attempts += 1
    if sum(numbers) == value:
        solution.numbers = numbers
        for i in range(n - 1):
            solution.operations.append(ADD)
        return solution

    # 3.  Try multiplying all the numbers together.
    num_attempts += 1
    product = 1
    for num in numbers:
        product *= num
    if product == value:
        solution.numbers = numbers
        for i in range(n - 1):
            solution.operations.append(MUL)
        return solution


    # 4.  If there are factors of value in numbers, pick one.

    # Find the factors
    if (value >= 0):
        factors = get_factors(value)
        factors_in_list = []
        for num in numbers:
            if num in factors and num not in factors_in_list:
                factors_in_list.append(num)

        # Prefer smaller factors
        factors_in_list.sort()

        # Make an attempt for each factor in the list
        for factor in factors_in_list:
            num_attempts += 1
            other_factor = value / factor
            # See if the other n - 1 numbers can arrive at the other_factor
            other_numbers = exclude(numbers, factor)
            solution = solve(other_numbers, other_factor)
            # If so, append a '*' operation to the end of the solution
            if solution:
                solution.numbers.append(factor)
                solution.operations.append(MUL)
                return solution


    # 5.  Try subtracting from value
    # Try it for each number in numbers
    for num in numbers:
        num_attempts += 1
        result = value - num
        # See if the other n - 1 numbers can arrive at the result
        other_numbers = exclude(numbers, num)
        solution = solve(other_numbers, result)
        # If so, append a '+' operation to the end of the solution
        if solution:
            solution.numbers.append(num)
            solution.operations.append(ADD)
            return solution

    # 6.  Try adding to value
    # Try it for each number in numbers
    for num in numbers:
        num_attempts += 1
        result = value + num
        # See if the other n - 1 numbers can arrive at the result
        other_numbers = exclude(numbers, num)
        solution = solve(other_numbers, result)
        # If so, append a '+' operation to the end of the solution
        if solution:
            solution.numbers.append(num)
            solution.operations.append(SUB)
            return solution

    # 7.  Try multiplying value
    # Try it for each number in numbers
    for num in numbers:
        num_attempts += 1
        result = value * num
        # See if the other n - 1 numbers can arrive at the result
        other_numbers = exclude(numbers, num)
        solution = solve(other_numbers, result)
        # If so, append a '/' operation to the end of the solution
        if solution:
            solution.numbers.append(num)
            solution.operations.append(DIV)
            return solution

    return False


def solve_card(card):
    """
    This method solves the 24 Card using my custom algorithm
    :param card: A list representing the 24 Card
    :return: Returns a Solution instance if a solution was found, and False if no solution was found.
    """
    return solve(card, 24)


# The 24 card. It's an array of 4 numbers
card = []

# Get the card's numbers from the user
user_input = raw_input("Please enter 4 numbers separated by a space: ")
split_input = user_input.split()
for num_str in split_input:
    card.append(int(num_str))

# Solve the card
solution = solve_card(card)

# Print results
if solution:
    print "Solution: %s" % solution
else:
    print "No solution found."

print "Number of attempts: %s" % num_attempts