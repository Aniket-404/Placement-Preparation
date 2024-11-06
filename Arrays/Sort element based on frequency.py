arr=[10,20,30,30,40,40,40,40,40,50,50,50]
result = sorted(arr, key = arr.count, reverse=True)
print(result)