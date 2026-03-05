def bruteForce(arr):
    max_element = sorted(arr, reverse=True)
    return max_element[1]


def secondLargestOptimal(arr):
    largest = secondLargest = float("-inf")
    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
    if secondLargest != float("-inf"):
        return secondLargest
    return secondLargest  

             
arr = [-1, -2, 0]
# print("Second_largest_element", bruteForce(arr))
print("Second_largest_element", secondLargestOptimal(arr))