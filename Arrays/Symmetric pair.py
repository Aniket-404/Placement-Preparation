def findPair(arr):
    s=set()
    for (x,y) in arr:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))

arr=[(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
findPair(arr)