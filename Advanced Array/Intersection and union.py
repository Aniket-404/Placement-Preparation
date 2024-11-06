a=[1,2,3,4,5]
b=[5,6,7,8,9]

intersect=list(set(a) & set(b))
union=list(set(a) | set(b))

print(intersect)
print(union)