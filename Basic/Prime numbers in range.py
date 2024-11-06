low,high = 2,10
prime= []

for i in range(low, high+1):
    flag = 0

    if i<2:
        continue
    if i == 2:
        prime.append(2)
        continue

    for x in range(2,i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        prime.append(i)

print(prime)