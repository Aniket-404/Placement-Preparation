def count(arr):
    ans=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j]<arr[i]:
                ans+=1
    return ans

arr=[6,3,5,2,7]
print(count(arr))