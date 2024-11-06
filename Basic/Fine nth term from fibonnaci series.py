def fibSeries(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibSeries(n-1)+fibSeries(n-2))
    
n = 8
print(fibSeries(n))