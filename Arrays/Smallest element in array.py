a=[1,2,3,4,5]
min_element=a[0]

for i in range(len(a)):
    if a[i]<min_element:
        min_element=a[i]

print(min_element)