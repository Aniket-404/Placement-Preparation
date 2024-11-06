def duplicate(arr):
    dup=set()
    for i in arr:
        if i in dup:
            return i
        dup.add(i)
    return -1

arr=[1,2,3,4]
print(duplicate(arr))