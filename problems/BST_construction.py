"""
Write a Binary Search Tree (BST) class. The class should have a "value" property set to be an integer, as wel as left and right properties, both of which should point to either the None value or to another BST. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None values. The BST class should support insertion, searching, and removal of values. The removal method should only remove the first instance of the target value.

"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        pass

    def contains(self, value):
        pass

    def remove(self, value, parent=None):
        pass

