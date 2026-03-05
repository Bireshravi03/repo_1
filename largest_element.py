def largest_ele(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element 


arr =  [1,2,3,4,5,66]
print("Largest_element", largest_ele(arr))

# print("largest_element", max(arr))

