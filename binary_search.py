# binary_search takes a sorted array and an item. If the item is in the array, the function returns its position.

def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+ high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


# Notes
# For any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n steps.