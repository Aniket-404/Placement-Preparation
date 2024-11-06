def leftRotate(arr,d,n):
    if(d==0 or d==n):
        return
    i=d
    j=n-d
    while (i!=j):
        if i<j:
            swap(arr, d-i, d+j-i, i)
            j -= i
        else:
            swap(arr, d-i, d, j)
            i -= j
    swap(arr, d-i, d, i)

def swap(arr, fi, si, di):
    for i in range(di):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp

arr=[10,20,30,40,50,60,70]
n=len(arr)
d=2

leftRotate(arr, d, n)

for i in range(n):
    print(arr[i], end=" ")