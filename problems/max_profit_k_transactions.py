"""
You are given an array of integers representing the prices of a single stock on
various days (each index in the array represents a different day). You are also
given an integer k, which represents the number of transactions you are allowed
to make. One transactions of buying the stock on a given day and selling it on
another, later day. Write a function that returns the maximum profit that you
can make buying and selling the stock, given k transactions. Note that you can
only hold 1 share of the stock at a time; in other words, you cannot buy more
than 1 share of the stock on any given day, and you cannot buy a share of the
stock if you are still holding another share. 

"""
def max_profit_with_k_transactions(prices, k):


# test
prices = [5, 11, 3, 50, 60, 90]

assert max_profit_with_k_transactions(prices, 2) == 93
print("OK")
