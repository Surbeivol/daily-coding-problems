"""
You are given a non-empty array of arrays. Each subarray holds three integers and represents a disk. These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other disk below it. Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. None that you cannot rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times. Assume that there will only be one stack with the greatest total height.

"""

def max_disk_stack(disks):
    pass

#test
disks = [
          [2, 1, 2],
          [3, 2, 3],
          [2, 2, 8],
          [2, 3, 4],
          [1, 2, 1],
          [4, 4, 5],
        ]

expected = [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

assert max_disk_stack(disks) == expected

print('OK')
