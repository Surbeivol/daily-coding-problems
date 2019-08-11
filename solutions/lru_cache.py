"""
Implement a class for a Least Recently Used (LRU) Cache. The cache should
support inserting key/value paris, retrieving a key's value and retrieving the
most recently active key. 

Each of these methods should run in constant time. When a key/value pair is
inserted or a key's value is retrieved, the key in question should become the
most recenty key. Also, the LRUCache class should store a max_size property set
to the size of the cache, which is passed in as an argument during
instantiation. This size represents the maximum numebr of key/value pairs that
the cache can hold at onece. If a key/value pair is added to che cache when it
has reached maximum capcacity, teh least recently used (active) key/value pair
should be evicted from the cache and no loger retrievable. The newly added
key/value pair shuld effectively replace it. Inserting a key/pari with an
already existing key should simply replace the key's value in the cache with
the new value and should not evict a key/value pair if  the cache is full.
Attempting to retrieve a value from a key that is not in the cache should
return the None value.

"""

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
"""
doubly linked list
node class
hash table with nodes
"""

class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size or 1
        self.lru_dict = {}
        self.lru_dll = DoublyLinkedList()
        self.cur_size = 0
        
    def update(self, node):
        self.lru_dll.setHead(node)
    
    def insertKeyValuePair(self, key, value):
        if key in self.lru_dict:
            node = self.lru_dict[key]
            node.value = value
            self.update(node)
            return
        elif self.cur_size == self.max_size:
            self.remove_least_recent()
        else:
            self.cur_size += 1
        
        node = DoublyLinkedListNode(key, value)
        self.lru_dll.setHead(node)
        # we know key is not in lru_dict
        self.lru_dict[key] = node
        
    def remove_least_recent(self):
        if self.cur_size < 1:
            return
        rem_key = self.lru_dll.tail.key
        self.lru_dll.remove_tail()
        del self.lru_dict[rem_key]
    
    def getValueFromKey(self, key):
        if key not in self.lru_dict:
            return None
        else:
            node = self.lru_dict[key]
            self.update(node)
            return node.value
    
    def getMostRecentKey(self):
        # Write your code here.
        return self.lru_dll.head.key

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if node is self.head:
            return
        self.remove(node)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head is self.tail:
            node.next = self.tail
            node.prev = None # not really necessary but for clarity
            self.tail.prev = node
            self.head = node
        else:
            self.remove(node)
            node.next = self.head.next
            self.head.prev = node
            self.head = node
    
    def remove_tail(self):
        self.remove(self.tail)
    
    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        node.remove_bindings()

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def remove_bindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.next = None
        self.prev = None
