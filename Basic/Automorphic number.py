num = 376
a = str(num)

num1 = num ** 2
b = str(num1)

if b.endswith(a):
    print("Automorphic")
else:
    print("Not Automorphic")