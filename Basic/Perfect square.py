from math import sqrt

def isPerfectSquare(n):
    if n>=0:
        sr = int(sqrt(n))
        return (sr * sr) == n
    return False

n = 49
if (isPerfectSquare(n)):
    print(n,"is a perfect square")
else:
    print(n,"is not a perfect square")