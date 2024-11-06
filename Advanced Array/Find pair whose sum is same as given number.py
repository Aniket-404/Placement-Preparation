def find(arr,n,summ):
    for i in range(n):
        for j in range(i, n):
            if (arr[i] + arr[j])==summ:
                print(arr[i],arr[j])

arr=[5,2,3,4,1,6,7]
summ=7
find(arr,len(arr),summ)