# num = 5
# flag = 0
# for i in range(2,num):
#     if num % i ==0:
#         flag = 1
#         break
# if flag == 1:
#     print(num,"is not a prime number")
# else:
#     print(num,"is a prime number")


def isPrime(num):
    if num<2:
        return 0
    else:
        for j in range(2,num):
            if num % j == 0:
                return 0
    return 1

a,b=1,100
for i in range(1, b+1):
    if isPrime(i):
        print(i, end=" ")