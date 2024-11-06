from math import ceil

def medianArray(arr,n):
    if (n%2)==0:
        medium = n//2
        median = (arr[medium] + arr[medium - 1]) / 2
        return median
    else:
        medium = ceil(n/2)
        return arr[medium-1]

arr1=[1,12,15,26,38]
arr2=[2,13,17,30,45]

arr3 = arr1+arr2
n=len(arr3)
arr3.sort()
ans=medianArray(arr3,n)
print(int(ans))