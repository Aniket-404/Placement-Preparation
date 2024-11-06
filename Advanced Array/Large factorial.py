def factorialfun(n):
    ans = 1
    while n>1:
        ans *= n
        n -= 1
    return ans

n=5
print(factorialfun(n))

from math import factorial
ans2 = factorial(n)

print(ans2)