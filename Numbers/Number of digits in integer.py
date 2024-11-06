def digitCount(n):
    digit = 0
    while n!=0:
        n= n//10
        digit +=1
    return digit

n = 12345
print(digitCount(n))

# import math
# digit1=math.floor(math.log10(n)+1)
# print(digit1)