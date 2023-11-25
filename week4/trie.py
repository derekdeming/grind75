# 208

class TrieNode:
    def __init__(self):
        self.children = {} #dict for child nodes
        self.endOfWord = False #use as flag if a word ends at the node

class Trie:
    def __init__(self):
        self.root = TrieNode() #root = empty 

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # if char is not already a child of curr node, add new node as child for char
            node = node.children[char]
        node.endOfWord = True # after inserting all char of word, mark end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: # if char not found in curr nodes children, word doesnt exist
                return False
            node = node.children[char]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix: # find prefix -- if not found = false but if found = true 
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
