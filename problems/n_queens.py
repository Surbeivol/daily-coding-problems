"""

We have discussed Knight’s tour and Rat in a Maze problems in Set 1 and Set 2 respectively. Let us discuss N Queen as another example problem that can be solved using Backtracking.
The N Queen is the problem of placing N chess queens on an N×N chessboard so
that no two queens attack each other. For example, following is a solution for
4 Queen problem.

"""

def get_n_queens(n_queens):
    pass


n_queens = 4

expected = [
             [
              [0, 1, 0, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 0, 1, 0],
             ],
             [
              [0, 0, 1, 0],
              [1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 1, 0, 0],
             ],
            ]

result = get_n_queens(n_queens)
result1 = result == expected
result2 = result[0] == expected[1] and result[1] == expected[0]
assert result1 or result2

print("OK")

