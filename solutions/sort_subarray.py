"""
Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smalles subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return [-1,1]

"""

def sort_subarray(array):
   result = [-1, -1]
    
    acc_max = [array[0]] * len(array)
    for idx in range(1, len(array)):
        acc_max[idx] = max(acc_max[idx - 1], array[idx])
    
    acc_min = [array[-1]] * len(array)
    for idx in reversed(range(0, len(array) - 1)):
        acc_min[idx] = min(acc_min[idx + 1], array[idx])
    
    for idx in range(len(array)):
        if acc_max[idx] != acc_min[idx]:
            result[0] = idx
            break
    
    for idx in reversed(range(len(array))):i
        if acc_max[idx] != acc_min[idx]:
            result[1] = idx
            break
    
    # one is negative and the other not, this is not possible
    if result[0] * result[1] < 0:
        raise Exception("We did not expect this to happen")
    
    return result


# test
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

assert sort_subarray(array) == [3, 9]

print('OK')
