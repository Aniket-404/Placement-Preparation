def longestSequence(arr,n):
    val = []
    a = 0
    for i in range(n):
        b=1
        while arr[i] + n in arr:
            a+=1
            b+=1
        val.append(a+1)
        a=0
    return max(val)

arr=[7,8,1,5,4,3]
n=len(arr)
print(longestSequence(arr,n))