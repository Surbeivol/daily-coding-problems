"""
Write a Binary Search Tree (BST) class. The class should have a "value" property set to be an integer, as wel as left and right properties, both of which should point to either the None value or to another BST. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None values. The BST class should support insertion, searching, and removal of values. The removal method should only remove the first instance of the target value.

"""
class BST:
    def __init__(self, value):
        self.value = valuede
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.        
        current = self
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BST(value)
                    break
            else: # ge
                if current.right:
                    current =  current.right
                else:
                    current.right = BST(value)
                    break
        return self

    def contains(self, value):
        # Write your code here.
        current = self
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
        return False
            

    def remove(self, value, parent = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        current = self
        while current is not None:
            if value > current.value:                
                parent = current
                current = current.right                
            elif value < current.value:
                parent = current
                current = current.left
            else: # == 
                # has 2 childs
                if current.left is not None and current.right is not None:
                    current.value = current.right.get_min_value()
                    current.right.remove(current.value, current)
                # has no parent node
                elif parent is None:
                    if current.left:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right: 
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        current.value = None
                # has 1 child or no childs
                elif parent.left == current:
                    parent.left = current.left if current.left else current.right
                elif parent.right == self:
                    parent.right = current.left if current.left else current.right
                break
        return self
    
    # time avg O(log(n)) worst O(n) | space O(1)
    def get_min_value(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

