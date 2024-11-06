def remove_duplicates(arr):
    unique_element=[]
    for element in arr:
        if element not in unique_element:
            unique_element.append(element)
    return unique_element

arr=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print(remove_duplicates(arr))