a = [1,2,3,4,5,6,7,8,9,10]
max_element = a[0]

for i in range(len(a)):
    if a[i]> max_element:
        max_element = a[i]

print(max_element)