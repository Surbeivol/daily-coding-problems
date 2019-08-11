"""
You are given a two-dimensiona array(matrix) of potentially unequal height and
width containing letters.

This matrix repreents a boggle board. You are also given a list of words. Write
a fucntion that returns an array of all the words contained in the boggle
board. A word is constructed in the boggle board by connecting adjacent
(horizontal, vertical or diagonal) letters, without using any single letter at
a given position more than once. 

While words can of course have repeated letters, those repetead letters mus
come from different positions in the boggle board in order for the word to be
contained in the board. Nonte that two or more words are allowed to overlap and
use the same letters in the boggle board.

"""

def boggle_board(board, words):
    # Write your code here.
    final_words = {}
    visited = [[False for el in row] for row in board]
    tree = Tree()
    for word in words:
        tree.add(word)
    for row in range(len(board)):
        for col in range(len(board[0])):
            explore_neighbor(row, col, board, tree.root, visited, final_words)
    return list(final_words.keys())

def explore_neighbor(row, col, board, tree, visited, final_words):
    if visited[row][col]:
        return

    char = board[row][col]
    if char not in tree:
        return
    next_node = tree[char]
    if '*' in next_node:
        final_words[next_node['*']] = True

    visited[row][col] = True
    neighbors = get_neighbors(row, col, board)
    for neigh in neighbors:
        explore_neighbor(neigh[0], neigh[1], board, next_node, visited, final_words)
    visited[row][col] = False

def get_neighbors(row, col, board):
    neighbors = []
    width = len(board[0])
    height = len(board)
    if row > 0 and col > 0:
        neighbors.append([row - 1, col - 1])
    if row > 0:
        neighbors.append([row - 1, col])
    if row > 0 and col < width - 1:
        neighbors.append([row - 1, col + 1])
    if col > 0:
        neighbors.append([row, col - 1])
    if col < width -1:
        neighbors.append([row, col + 1])
    if row < height - 1 and col > 0:
        neighbors.append([row + 1, col - 1])
    if row < height -1:
        neighbors.append([row + 1,col])
    if row < height -1 and col < width -1:
        neighbors.append([row + 1, col + 1])
    return neighbors


class Tree:

    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node[self.end_symbol] = word

board = [
         ['t', 'h', 'i', 's', 'i', 's', 'a'],
         ['s', 'i', 'm', 'p', 'l', 'e', 'x'],
         ['b', 'x', 'x', 'x', 'x', 'e', 'b'],
         ['x', 'o', 'g', 'g', 'l', 'x', 'o'],
         ['x', 'x', 'x', 'D', 'T', 'r', 'a'],
         ['R', 'E', 'P', 'E', 'A', 'd', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
         ['N', 'O', 'T', 'R', 'E', '-', 'P'],
         ['x', 'x', 'D', 'E', 'T', 'A', 'E'],
        ]

words = ['this', 'is', 'not', 'a', 'simple', 'boggle',
        'board', 'test', 'REPEATED', 'NOTRE-PEATED']

output = ['this', 'is', 'a', 'simple', 'boggle',
          'board', 'NOTRE-PEATED']

result = boggle_board(board, words)
output_set = set(output)
assert len(output) == len(result)
for res in result:
    assert res in output_set

print('OK')
