def countFrequency(arr,n):
    arr.sort()

    i=0
    while i<n:
        count = 1
        while i<n-1 and arr[i] == arr[i+1]:
            i += 1
            count +=1

        print("{} : {}".format(arr[i],count))
        i+=1

arr=[2,4,4,4,6,6,6,6,6]
n=len(arr)

countFrequency(arr,n)