def printDivisors(n, factors):
    i =1
    while i <= n:
        if (n%1==0):
            factors.append(i)
        i += i
    return sum(factors)-n

n1=6
n2=28
if int(printDivisors(n1, [])/n1) == int(printDivisors(n1, [])/n2):
    print("Friendly pair")
else:
    print("Not a friendly pair")