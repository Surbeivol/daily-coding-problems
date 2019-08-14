"""
Given an non-empy array of integers, write a function that returns an array of
length 2. The first element in the output array should be an integer value
representing the greates tsum taht can be generated from a strictly-increasing
subsequence in the array. The second element shuld be an array of the numbers
in that subsequence. A subsequence is defined as a set of numbers that are not
necessarily adjacent but that are in the same order as they appear in the
array. Assume that there will only be one increasing subsequence with the
greatest sum. 

"""

def max_sum_subsequence(array):
    if not array:
        return [0, []]
    
    max_sum = [[val, [val]] for val in array]
    abs_max = max_sum[0]
    for right in range(1, len(array)):
        for left in range(right):
            prev_max_seq = max_sum[left][1][-1] if max_sum[left][1] else float('-inf')
            pot_max = [max_sum[left][0] + array[right],
                       max_sum[left][1] + [array[right]]]
            if pot_max[0] > max_sum[right][0]:
                if array[right] > prev_max_seq:
                    max_sum[right] = pot_max
        abs_max = max(abs_max, max_sum[right])
    
    return abs_max
            

# tests

array = [10, 70, 20, 30, 50, 11, 30]

output = [110, [10, 20, 30, 50]]

assert output == max_sum_subsequence(array)

print('OK')
