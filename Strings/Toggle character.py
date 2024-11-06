char='Aniket Kamble'
str1=str()
for i in char:
    if i.isupper():
        i = i.lower()
        str1 += i
    else:
        i = i.upper()
        str1 += i

print(str1)