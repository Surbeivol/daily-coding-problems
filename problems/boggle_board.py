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

output = ['this', 'is', 'a', 'simple', 'boggle'
          'board', 'NOTRE-PEATED']

result = boggle_board(board, words)
output_set = set(output)

assert len(output) == len(result):
for res in result:
    assert res in output_set

print('OK')
