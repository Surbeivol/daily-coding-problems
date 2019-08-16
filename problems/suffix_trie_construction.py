"""
Write a class from a suffix-trie-like data structure. The class should have a "root" property set to be root node of the trie. The class should support creation froma a string and the searching of strings. The creation method will be called when the class is instantiated and shuld populate the root property of the class. Note that every string added to the trie should end with the special "endSymbol" chracter *

"""

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):

    def add_substring(self, string, idx):

    def contains(self, string):
