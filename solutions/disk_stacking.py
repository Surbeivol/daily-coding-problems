"""
You are given a non-empty array of arrays. Each subarray holds three integers
and represents a disk. These integers denote each disk's width,d epth and
height, respectively. Your goal is to stack up the disk and to maximize the
total height of the stack. A disk must have a strictly smaller width, depth,
and height than any other disk below it. Write a function that returns an array
of the disks in the final stack, starting with the top disk and ending with the
bottom disk. Note that you cannot rotate disks; in other words, the itnegers in
each subarray mus represent [width, depth, height] at all times. Assume only
one stack with greatest total height.


"""


def disk_stacking(disks):
    
    stack_he_i = 0
    stack_di_i = 1
    di_he_i = 2
    # sort disks by height
    disks.sort(key=lambda disk: disk[di_he_i])
    # we will store here the cum max height of all possible stacks 
    # up to each disk and the indexes of the disks to build this stack
    # initially we assume at least we could build a stack of a single disk
    # for every disk
    max_stack = [[disk[di_he_i], [idx]] for idx, disk in enumerate(disks)]
    
    # For every disk, we look if we could stack previous stacks with
    # their corresponding biggest base disk and its max height
    for bot in range(1, len(disks)):
        for top in range(bot):
            if _can_stack(disks[top], disks[bot]):
                # combine prev max stack with current disk
                new_stack = [max_stack[top][stack_he_i] + disks[bot][di_he_i],
                             max_stack[top][stack_di_i] + [bot]]
                max_stack[bot] = max(max_stack[bot], new_stack)
    return [disks[idx] for idx in max(max_stack)[1]]
               
def _can_stack(top_disk, bottom_disk):
    """ Checks if top_disk could be stacked upon bottom_disk
        based on their dimensions
    """
    return all([top < bot for top, bot in zip(top_disk, bottom_disk)])

# Sample test

disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5]]
assert disk_stacking(disks) == [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
