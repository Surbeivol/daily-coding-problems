"""
Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smalles subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return [-1,1]

"""
# time complexity O(n) | space complexity O(1)
def sort_subarray(array):
    min_unordered = float('inf')
    max_unordered = float('-inf')
    for idx, num in enumerate(array):
        if is_out_of_order(array, idx):
            min_unordered = min(min_unordered, num)
            max_unordered = max(max_unordered, num)
    
    if min_unordered == float('inf'):
        return [-1, -1]

    start_idx = 0
    while array[start_idx] <= min_unordered:
        start_idx += 1
    
    end_idx = len(array) - 1
    while array[end_idx] >= max_unordered:
        end_idx -= 1

    return [start_idx, end_idx]

def is_out_of_order(array, idx):
    if idx == 0:
        return array[idx] > array[idx + 1]
    elif idx == len(array) - 1:
        return array[idx] < array[idx - 1]
    else:
        is_smaller = array[idx] < array[idx - 1]
        is_bigger = array[idx] > array[idx + 1] 
        return is_smaller or is_bigger

# test
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

assert sort_subarray(array) == [3, 9]

print('OK')
