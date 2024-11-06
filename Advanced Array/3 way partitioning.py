def part(arr, l, h):
    lm=[]
    hm=[]
    mm=[]

    for i in arr:
        if i<l:
            lm.append(i)
        elif i>h:
            hm.append(i)
        else:
            mm.append(i)
    return lm + mm + hm

arr=[1,17,22,16,13,5,43,18,3,10]
lowval=14
highval=20
print(part(arr,lowval,highval))