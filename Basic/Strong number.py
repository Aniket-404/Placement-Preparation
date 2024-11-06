import math
def is_strong(num):
    original = num
    sum = 0

    while num>0:
        digit= num % 10
        sum += math.factorial(digit)
        num //=10

    return sum == original

num =145
if (is_strong(num)):
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")