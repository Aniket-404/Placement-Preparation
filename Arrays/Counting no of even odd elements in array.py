arr=[1,2,3,4,5]
n=len(arr)
countEven = 0
countOdd = 0

for i in range(n):
    if arr[i]%2==0:
        countEven += 1
    else:
        countOdd += 1

print("No or Even elements:", countEven)
print("No of Odd elements:", countOdd)