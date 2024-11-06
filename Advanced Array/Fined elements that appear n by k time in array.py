from collections import Counter

def find(arr,k):
    n=len(arr)
    threshold = n//k
    frequency = Counter(arr)

    result = [num for num, count in frequency.items() if count> threshold]
    return result

arr=[3,1,2,2,3,3,4,4,4,4]
k=4

print(find(arr,k))