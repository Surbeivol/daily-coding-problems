"""
Write a function that takes in an array of integers and returns a sorted
version of that array. Use the Heap Sort algorithm to sort the array.

"""

def heap_sort(array):
    # O(n)
    build_heap(array)

    # O(n * log(n))
    for sorted_border in reversed(range(1, len(array))):
        swap(0, sorted_border, array)
        shift_down(0, sorted_border - 1, array)

    return array

# O(n)
def build_heap(array):
    first_parent = (len(array) -2) // 2
    for parent in reversed(range(first_parent + 1)):
        shift_down(parent, len(array) - 1, array)

# log(n)
def shift_down(start_idx, end_idx, array):
    while True:
        child_left = 2 * start_idx + 1
        child_right = child_left + 1
        if child_right <= end_idx:
            max_val, max_idx  = max((array[child_left], child_left),
                                (array[child_right], child_right))
        elif child_left <= end_idx:
            max_val, max_idx = array[child_left], child_left
        else:
            return
        if array[start_idx] < max_val:
            swap(max_idx, start_idx, array)
        start_idx = max_idx

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

