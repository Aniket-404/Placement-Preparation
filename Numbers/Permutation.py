def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

n = 10
r = 6

p = factorial(n)//factorial(n-r)
print(p)