def fun(arr, n):
    max_so_far = max(arr)
    for i  in range(n-1):
        s = arr[i]
        for j in range(1+i, n):
            s += arr[j]
            if s > max_so_far:
                max_so_far = s
    return max_so_far

arr=[-2,-2,4,-1,-2,1,5,-3]
n = len(arr)
print(fun(arr,n))