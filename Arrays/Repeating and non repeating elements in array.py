def repeatingElement(arr,n):
    mp=dict()
    
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    print("Repeating elements:", end=" ")
    for x in mp:
        if mp[x]!=1:
            print(x, end=",")

    print("\nNon repeating elements:", end=" ")
    for y in mp:
        if mp[y]!=1:
            print(y, end=",")

arr=[10,20,30,40,50,10,20]
n=len(arr)
repeatingElement(arr,n)