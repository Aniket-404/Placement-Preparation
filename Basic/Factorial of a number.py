num = 6
fact = 1

if num<0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num+1):
        fact = fact * i

print("Factorial of", num, "is", fact)