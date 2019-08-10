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

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def setHead(self, node):
        # head > node <> node2
        # head > node < tail
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # node.prev <> nodeToInsert <> node
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return            
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node is self.head:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        
    def insertAfter(self, node, nodeToInsert):
        # node <> nodeToInsert <> node.next
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)        
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node is self.tail:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert        

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        self.remove(nodeToInsert)
        if position == 1:
            self.setHead(nodeToInsert)
            return

        cur_pos = 1
        cur_node = self.head
        while cur_pos != position and cur_node is not None:
            cur_node = cur_node.next
            cur_pos += 1

        if cur_node is not None:
            self.insertBefore(cur_node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        cur_node = self.head
        while cur_node is not None:
            node_to_rm = cur_node
            cur_node = cur_node.next
            if node_to_rm.value == value:
                self.remove(node_to_rm)
        
    def remove(self, node):
        # Write your code here.
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        cur_node = self.head
        while cur_node is not None:
            if value == cur_node.value:
                return True
            else:
                cur_node = cur_node.next
        return False



