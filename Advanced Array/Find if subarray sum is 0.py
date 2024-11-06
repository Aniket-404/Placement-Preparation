def sunArray(arr,n):
    for i in range(n):
        s=arr[i]
        for j in range(i+1,n):
            s+=arr[j]
            if s==0:
                return True
    return False

arr=[4,2,-3,1,6]
n=len(arr)
print(sunArray(arr,n))