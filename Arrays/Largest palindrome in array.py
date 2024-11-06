def isPalindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
    
def largestPalindrome(arr,n):
    arr.sort(reverse=True)

    for i in range(n):
        if isPalindrome(arr[i]):
            return arr[i]
        
    return -1

arr = [1, 232, 5545455, 909090, 161]
n=len(arr)

print(largestPalindrome(arr,n))