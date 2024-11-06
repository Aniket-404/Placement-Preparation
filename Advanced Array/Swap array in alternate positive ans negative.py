def arrange(arr,n):
    p=0
    b=0
    for i in range(n):
        if b ==1:
            b-=1
        elif arr[i]<0:
            arr[i],arr[p]=arr[p],arr[i]
            if p>i:
                b += 1
            p += 2
    return arr

arr=[2,3,-4,-1,6,-9]
n=len(arr)
print(arrange(arr,n))