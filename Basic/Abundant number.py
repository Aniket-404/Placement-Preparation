n = 12
sum = 1

for i in range(2, n):
    if(n%i==0):
        sum += i
    
if (sum>n):
    print("Abundant number")
else:
    print("Not abundant")