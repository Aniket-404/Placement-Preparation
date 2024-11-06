arr=[4,-2,0,6,-4]
ans = -1
for i in range(1, len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        ans = i
        break

print(ans)