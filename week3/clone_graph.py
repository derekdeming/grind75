
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_nodes = {}

        def dfs(node): # using depth first search
            # in the case wehere the nodes is already cloned, return its clone
            if node in cloned_nodes:
                return cloned_nodes[node]

            clone = Node(node.val, [])
            cloned_nodes[node] = clone
            # recursion for neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
    
'''
DFS -- traverse the graph and for each node, create new node w/ same value
dict used to store mapping of original nodes to clones 
use recursion to clone neighbors of each node

time comp: O(N)
space comp: O(N)
'''