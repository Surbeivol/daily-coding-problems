"""
You are given a two.dimensiona array(matrix) of distinct integers where each
row is sorted and each column is also sorted.The matrix does not necessarily
have the same height and width. Your are also given a target number, and you
must write a function that returns an array of the row and column indices of
the target number if it is contained in the matrix and [-1, -1] if it is not.if

"""

def search_sorted_matrix(matrix, target):
    # Write your code here.
    """
    1 4 7 12 15  1000
    2     50 500 1001
    3            1002
    4

    """

    result = [-1, -1]
    row = 0
    if len(matrix) == 0:
        return result
    col = len(matrix[0]) - 1

    while col >= 0 and row < len(matrix):
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            result = [row, col]
            break

    return result


matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]

assert search_sorted_matrix(matrix, 44) == [3, 3]
print("OK")
