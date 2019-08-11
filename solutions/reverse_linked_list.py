"""
make a funtion that given a simple linked list it reverses it

head -> node1 -> node2 -> node3
head -> node3 -> node2 -> node1

"""
# Using stack O(n) time and O(n) space
def reverse_linked_list(linked_list):
	stack = []
	current_node = linked_list.head
	linked_list.head = None

	while current_node.next is not None:
		stack.append(current_node)
		del_link = current_node
		current_node = current_node.next
		del_link.next = None

	linked_list.head = current_node
	while len(stack) > 0:
		next_node = stack.pop()
		current_node.next = next_node
	
	next_node.next = None

"""
head -> node1 -> node2 -> node3 -> node4

head -> prev <- next 
                temp_pointer

                        <- prev   next
                                temp_pointer



"""
# Using pointers O(n) time and O(1) space
def reverse_linked_list(linked_list):
    prev_node = linked_list.head
    if prev_node.next is None:
        return

    next_node = prev_node.next
    prev_node.next = None

    while next_node.next is not None:
        next_next_pointer = next_node.next
        next_node.next = prev_node
        prev_node = next_node
        next_node = next_next_pointer
        
    linked_list.head = next_node
    next_node.next = prev_node
    next_next_pointer = None




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
print("OK \n")

print("Reversed linked list values:")
next_node = linked_list.head
while next_node is not None:
    print(next_node.value)
    next_node = next_node.next


	
