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
    # Write your code here.
    """
       5  11  3  50   10    60  90
    0  0   0   0  0    0    0
    1  0   6   6  47   47   57  87  
    2  0   6   6  53   53   97  127  
    3  0   6   6  53   53   103 127 
     
    
    max idxs - idxb + profits[row-1][idxb], profits[row][idxs-1]
    
    """

    if len(prices) == 0:
        return 0
    
    # profits with k-1
    prev = [0 for price in prices]
    # profits in iteration k
    current = list(prev)
    
    for k in range(1, k + 1):
        for idx_s in range(1, len(prices)):
            max_profit = float('-inf')
            for idx_b in range(idx_s):
                new_profit = prices[idx_s] - prices[idx_b] + prev[idx_b]
                max_profit = max(new_profit, current[idx_s - 1], max_profit)
            current[idx_s] = max_profit
        prev = list(current)            
    
    return current[-1]
        

# test
prices = [5, 11, 3, 50, 60, 90]

assert max_profit_with_k_transactions(prices, 2) == 93
print("OK")
