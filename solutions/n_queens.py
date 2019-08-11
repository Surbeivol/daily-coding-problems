"""

We have discussed Knight’s tour and Rat in a Maze problems in Set 1 and Set 2 respectively. Let us discuss N Queen as another example problem that can be solved using Backtracking.
The N Queen is the problem of placing N chess queens on an N×N chessboard so
that no two queens attack each other. For example, following is a solution for
4 Queen problem.

1  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0

q[0]==1 idx==0,2
q[0]==2 idx==1,2
 
  

queen[0] +-  (idx - queen[1])
"""



def get_n_queens(n_queens):
    
    solutions = []
    for row in range(n_queens):
        _helper(1, [[row, 0]], solutions)

    result = []
    for solution in solutions:
        board = [[0 for i in range(n_queens)] for j in range(n_queens)]
        for queen in solution:
            board[queen[0]][queen[1]] = 1
        result.append(board)

    return result

def attacked(row, col, queens):
    for queen in queens:
        if queen[0] == row:
            return True
        elif row == queen[0] + (col - queen[1]):
            return True
        elif row == queen[0] - (col - queen[1]):
            return True
    return False

def _helper(col, queens, solutions):
    for row in range(n_queens):
        if not attacked(row, col, queens):
            new_queens = queens + [[row, col]]
            if col == n_queens - 1:
                solutions.append(new_queens)
                return 
            else:            
                _helper(col + 1, new_queens, solutions)
    


# test

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
