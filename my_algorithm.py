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

2.  If there are factors of x in A, pick one.
    * Prefer 1 as a factor of x, and then prefer smaller factors
    a)  See if the other n - 1 numbers can make the other factor of x
        i)  If so, then yes
        ii) If not, then pick another factor

3.  If there are no more factors of x in A, then for each number a in A:
    a)  SUBTRACT a from x
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, try the next number

4.  If that fails, then for each number a in A:
    a)  ADD a to x
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, try the next number

5.  If that fails, then for each number a in A:
    a)  MULTIPLY x by a
    b)  See if the other n - 1 numbers can form the result
        i)  If so, then yes
        ii) If not, then no solution
"""

