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


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size or 1

    def update(self, node):

    def insertKeyValuePair(self, key, value):

    def remove_least_recent(self):

    def getValueFromKey(self, key):

    def getMostRecentKey(self):

