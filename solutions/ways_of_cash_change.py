"""
Given an array of positive integers representing coin denominations and a
single non-negative integer representing a target amount of money, impolement a
function that returns the number of ways to make change for that target amount
using the given coin denominations. Note that an unlimited amount of coins is
at your disposal.
"""

def number_of_ways_to_make_change(n, denoms):
    ways = [0 for i in range(n+1)]
    ways[0] = 1
    
    for coin in denoms:
        for amount in range(1, len(ways)):
            if amount >= coin:
                ways[amount] += ways[amount - coin]    
    
    return ways[-1]


assert number_of_ways_to_make_change(6, [1, 5]) == 2
print("OK")


