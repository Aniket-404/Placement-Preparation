a=[1,2,3,4,5]
maxa=a[0]
mina=a[0]

for i in range(len(a)):
    if a[i]>maxa:
        maxa=a[i]

    if a[i]<mina:
        mina=a[i]

print(maxa)
print(mina)