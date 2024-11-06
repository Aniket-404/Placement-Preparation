arr1=[1,2,6,3,7]
arr2=[10,7,45,3,7]
n=len(arr1)

arr1.sort()
arr2.sort()
product = 0

for i in range(n):
    product += arr1[i]*arr2[i]

print(product)