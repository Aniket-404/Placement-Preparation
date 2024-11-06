def printOrder(a,n):
    a.sort()

    i=0
    j=n-1
    while i<n/2:
        print(a[i], end=" ")
        i=i+1
    while j>=n/2:
        print(a[j], end=" ")
        j=j-1

a=[1,2,3,4,5,6]
n=len(a)

printOrder(a,n)