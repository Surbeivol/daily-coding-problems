"""
Given an array of positive integers representing coin denominations and a
single non-negative integer representing a target amount of money, implement a
function that returns the smallest number of coins needed to make change for
that target amount using the given coin denominations. Nonte that an
unlimited amount of coins is at your disposal. If it is impossible to make
change for the target amount, return -1.

"""


def min_number_of_coins(n, denoms):
    min_change = [float('inf') for i in range(n+1)]
    min_change[0] = 0
    for coin in denoms:
        for amount in range(1, n+1):    
            if coin <= amount:
                cur_min = min(min_change[amount], 1 + min_change[amount - coin])
                min_change[amount] = cur_min
                
    return min_change[-1] if min_change[-1] != float('inf') else -1

# test
assert min_number_of_coins(7, [1, 5, 10]) == 3
print("OK")
