num = input("Enter number: ")
intnum = int(num)
sum = 0

for i in num:
    sum += int(i)

if intnum % sum == 0:
    print("True")
else:
    print("False")