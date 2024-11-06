char="12345"
sum=0
for i in char:
    if ord(i)>=48 and ord(i)<=57:
        sum+=int(i)

print(sum)