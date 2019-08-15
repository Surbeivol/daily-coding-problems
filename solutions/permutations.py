"""
Write a function that takes in an array of unique integers and returns an array
of all permutations of those integers. If the input array is empty, your
function should return an empty array"

"""
# Time complexity is O(n²*n!) | space complexity is O(n*n!)
def permutations(array):
    result = []
    if not array:
        return array

    _rec_permutations(array, [], result)
    return result

def _rec_permutations(subarray, perms, result):
    if len(subarray) == 1:
        result.append(perms + subarray)
        return

    for idx in range(len(subarray)):
        if idx < len(subarray) - 1:
            next_subset = subarray[:idx] + subarray[idx+1:]
        else:
            next_subset = subarray[:idx]
        _rec_permutations(next_subset, perms + [subarray[idx]], result)


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
