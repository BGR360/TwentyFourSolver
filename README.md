# 24 Card Solving Algorithm
My very first Python project. An algorithm to solve 24-Cards (a math game).

## Current Stats

My algorithm is **4.4 times** as fast as the brute-force algorithm.

My algorithm outperforms the brute-force **78.2%** of the time.

See [findings.txt](findings.txt) for more details.

## The 24 Game
If you are unfamiliar with 24 Cards, here is a brief explanation:

![A simple 24 Card. The numbers are {1, 2, 3, 4}](https://www.learningforallages.com/images/Math24SD1d.jpg) ![A simple 24 Card. The numbers are {5, 1, 5, 10}](https://www.learningforallages.com/images/34676.gif) ![A more difficult 24 Card. The numbers are {4, 2, 3, 4}](http://www.sbu.edu/images/default-source/school-of-arts-and-sciences-math/24game_card.gif?sfvrsn=2)

The goal of the game is to make 24 using arithmetic. You must use all four numbers that appear on the card, and you can use addition, subtraction, multiplication, and division as many times as you want and in any order that you want.

For example, the first card shown above is easily solved: 1 * 2 * 3 * 4 = 24

For the second card, we can do: (10 - 5) * 5 - 1 = 24

And for the third card, we can do: (4 - 2) * 4 * 3 = 24

### Grouping

Another rule that I was not aware of when I first designed my algorithm is that you are allowed to group numbers together, rather than just doing 3 operations in a row.

<img src="http://randallreedjr.com/images/24gamecard.jpg" width="142">

For example, this card is not solvable without grouping. Here is the solution: (8 - 4) * (3 - 1) = 24

Currently, my algorithm does not account for this rule, but **stay tuned!** In the future I plan to improve the algorithm to include this possibility.

## Brute-Force Approach

The obvious solution to coding a 24 Card solver is to test *all possible combinations* of numbers and operations until you find a solution. This is, as I call it, the "brute-force" algorithm. The implementation for this algorithm can be found in [brute_force_algorithm.py](brute_force_algorithm.py).

## My Approach

My idea was to create a more algorithmic approach to the problem. How can I make the computer think more like a human? When humans are trying to solve a 24 Card, they don't just try every possible combination at random. They think of the **factors** of 24 and how they can form them. They break the problem down into smaller ones. For example, if a card has a 6 in it, a smart human might think, "How can I use the other three numbers to make 4? Then I could do 4 * 6 = 24." My ultimate goal was to develop an algorithm that could drastically outperform the brute-force algorithm.

### Generalizing

Remember the example of the smart human. He sees that he has a 6 in his card, and wonders how to make 4 out of the other three numbers. Let's say that there's an 8 in the other three numbers. The smart human will think, "How can I make 2 out of the remaining two numbers?" This human is revealing to us an inherently *recursive* algorithm. In order to implement this, we need a general algorithm which can answer the question:

**How can I make _x_ out of a list of _n_ numbers?**

That is the question that my algorithm answers. You can find the implementation of this algorithm in [my_algorithm.py](my_algorithm.py)

### My Algorithm in Full

**Given _n_ numbers (stored in array _A_), can you use arithmetic to arrive at _x_?**

1.  **If n = 1:**
    1.  If A[0] = x, then yes
    2.  If A[0] != x, then no
2.  **If n = 2:**
    1.  Try multiplying the two numbers
    2.  Try adding the two numbers
    3.  If x >= 0
        1.  Try subtracting the smaller from the larger
        2.  Else try subtracting the larger from the smaller
    4.  Try dividing the larger by the smaller
    5.  If any of those work, then yes. If not, then no solution.
3.  **Try adding all the numbers in A together.**
4.  **Try multiplying all the numbers in A together.**
5.  **If there are factors of x in A, pick one.**
    * Prefer 1 as a factor of x, and then prefer smaller factors
    1.  See if the other n - 1 numbers can make the other factor of x
        1.  If so, then yes
        2.  If not, then pick another factor
6.  **If there are no more factors of x in A, then for each number a in A:**
    1.  SUBTRACT a from x
    2.  See if the other n - 1 numbers can form the result
        1.  If so, then yes
        2.  If not, try the next number
7.  **If that fails, then for each number a in A:**
    1.  ADD a to x
    2.  See if the other n - 1 numbers can form the result
        1.  If so, then yes
        2.  If not, try the next number
8.  **If that fails, then for each number a in A:**
    1.  MULTIPLY x by a
    2.  See if the other n - 1 numbers can form the result
        1.  If so, then yes
        2.  If not, then no solution
