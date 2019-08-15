"""
Write a function that takes in an array of unique integers and returns an array
of all permutations of those integers. If the input array is empty, your
function should return an empty array"

"""

def permutations(array):
    pass


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
