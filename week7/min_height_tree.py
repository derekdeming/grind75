# 310 

from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
    
    '''
    the intuition behind this approach is that the root of an MHT has to be the middle point (or two middle points) of the longest path of the tree.
    
    the idea is to trim out the leaves of the tree until one or two leaves are left. What's left is the answer. 
    
    the time complexity of this approach is O(n) because we trim the leaves in a BFS manner.
        
    '''