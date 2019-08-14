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
    pass


# tests

array = [10, 70, 20, 30, 50, 11, 30]

output = [110, [10, 20, 30, 50]]

assert output == max_sum_subsequence(array)

print('OK')
