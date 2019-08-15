"""
Write a function that takes in an array of unique integers and returns an array
of all permutations of those integers. If the input array is empty, your
function should return an empty array"

"""
# time complexity O(n*n!) | space complexity O(n*n!)
def permutations(array):
    """
     1 2 3 
     1 3 2
     2 1 3
     2 3 1
     3 2 1
     3 1 2

     1 2 3 4 append
     1 2 4 3 swap append
     1 2 3 4 unswap dont append
     1 2 3 4
     1 2 3 4
    """
    result = []
    _helper(0, array, result)
    return result


def _helper(idx, array, result):
    if idx == len(array) - 1:
        result.append(array)

    for right in range(idx, len(array)):
        _swap(idx, right, array)
        _helper(idx + 1, array, result)
        _swap(idx, right, array)

def _swap(idx1, idx2, array):
    array[idx1], array[idx2] = array[idx2], array[idx1]


# test

array = [1, 2, 3]

expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
           ]

results = permutations(array) 
assert len(results) == len(expected)
for result in results:
    assert result in expected

print("OK")
