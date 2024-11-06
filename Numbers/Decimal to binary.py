def convertBinary(num):
    binaryArray = []
    while num > 0:
        binaryArray.append(num%2)
        num = num//2
    for i in binaryArray:
        print(i, end="")

num = 21
convertBinary(num)