"""
make a funtion that given a simple linked list it reverses it

head -> node1 -> node2 -> node3
head -> node3 -> node2 -> node1

"""

def reverse_linked_list(linked_list):


class LinkedList:

	def __init__(self):
		self.head = None
	
	def append(self, node):
		if self.head is None:
			self.head = node
		else:
			cur_node = self.head
			while cur_node.next is not None:
				cur_node = cur_node.next
			cur_node.next = node

class Node:

	def __init__(self, value):
		self.value = value
		self.next = None


# TESTS
linked_list = LinkedList()
for i in range(10):
	node = Node(i)
	linked_list.append(node)

reverse_linked_list(linked_list)

assert linked_list.head.value == 9
print("OK")


	
