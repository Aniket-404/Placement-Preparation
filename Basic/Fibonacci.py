num = 10
n1, n2 = 0, 1
print("Fibonacci series: ", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")


# def fibSeries(i):
#     if i<=1:
#         return i
#     else:
#         return(fibSeries(i-1)+fibSeries(i-2))
    
# num = 10
# print("Fibonacci Series:", end=" ")

# for i in range(num):
#     print(fibSeries(i), end=" ")