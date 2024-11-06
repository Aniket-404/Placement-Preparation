def changeArr(arr):
    newArr = arr.copy()
    newArr.sort()

    for i in range(len(arr)):
        for j in range(len(newArr)):
            if arr[i]==newArr[j]:
                arr[i]=j+1
                break

arr=[100,2,70,12,90]
changeArr(arr)
print(arr)