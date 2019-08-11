"""
Write a class for a Double Linked List. The class should have a 'head' and
'tail' properties, both of which shuld point to either the None (null) value or
to a Linked List node. Every node will have a 'value' property as well as
'next' and 'prev' properties, both of which can point to either the None value
or another node. The class should support setting the head and tail of the
linked list, inserting nodes before and after other nodes as well as at certain
positions, removing given nodes and removing nodes with specific values, and
searching for ndoes with values. Only the searchign method should regturn a
boolean value.

"""

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.

    def setTail(self, node):
        # Write your code here.

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.

    def removeNodesWithValue(self, value):
        # Write your code here.

    def remove(self, node):
        # Write your code here.

    def containsNodeWithValue(self, value):
      # Write your code here.


