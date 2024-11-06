"""
How to Attempt?


Mango Distribution


Given a number of mangoes and number of persons. Find the number of ways to
distribute identical mangoes among identical persons,


Input Specification:
input1: the number of mangoes
input2: the number of persons


Output Specification:
Return the number of ways to distriblste identical mangoes among identical
persons,


Example 1:
input1: 2
input2: 2


Output: 3
"""

import math

def distribution(m,p):
    return math.comb(m + p - 1, p - 1)

m = int(input())
p = int(input())

print(distribution(m,p))