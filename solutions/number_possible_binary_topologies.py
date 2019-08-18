"""
Write a function that takes in a non-negative integer n and that returns the number of possible Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2: a root node with a left node, and a root node with a right node. Note than wen n is equal to 0, there is one topology that can be created: the None node.
"""

def num_binary_tree_topologies(numb):
    memo = {}
    return _helper(n, memo)
    
def _helper(n, memo):
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1
    if n == 2:
        return 2
    
    result = 0
    for give_left in range(0, n):
        result += _helper(give_left, memo) * _helper(n - 1 - give_left, memo)

    memo[n] = result
    return result

# test
assert num_binary_tree_topologies(3) == 5
print('OK')
