from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        result, queue = [], [root]
        while queue: 
            branch = []
            branch_level = len(queue)
            for i in range(branch_level):
                node = queue.pop(0)
                branch.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result.append(branch)
        
        return result 
    
'''
- check if empty, initialize the queue w/ root 
- for each branch we take all nodes in queue (within the same level) and store the values
- children nodes are added to queue for next level 

time comp: O(n) for the traversal
space comp: O(n) for the queue
'''