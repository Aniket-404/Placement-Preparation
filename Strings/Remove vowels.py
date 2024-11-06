char="Aniket"
n=len(char)
vowles=['a','e','i','o','u','A','E','I','O','U']

for i in range(n):
    if char[i] not in vowles:
        print(char[i],end=" ")