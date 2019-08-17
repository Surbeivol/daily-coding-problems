"""
Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that is written the same forward and backward. Assume that there will only be one longest palindromic substring. 

"""

def longest_palindromic_substring(string):
    if len(string) <= 1:
        return string
    
    # starting and ending index (non inclusive) of the max palindrome sofar
    max_sofar = [0, 1]
    for idx in range(1, len(string)):
        pair_max = _get_max_palindrome(string, idx - 1, idx)
        odd_max = _get_max_palindrome(string, idx - 1, idx + 1)
        max_sofar = max(max_sofar, pair_max, odd_max, key = lambda x: x[1] - x[0])
    
    return string[max_sofar[0]:max_sofar[1]]
    
def _get_max_palindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left]!=string[right]:
            break
        left -= 1
        right += 1    
    return [left + 1, right]

#test
string = 'abaxyzzyxf'
assert longest_palindromic_substring(string) == 'xyzzyx'
print('OK')
