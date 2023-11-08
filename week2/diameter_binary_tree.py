# 543
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            leftH = dfs(node.left)
            rightH = dfs(node.right)
        
            self.diameter = max(self.diameter, leftH + rightH)
            return max(leftH, rightH) + 1
        
        self.diameter = 0 
        dfs(root)
        return self.diameter
    
    '''
    update the diameter if the current node's diameter is greater
    
    return the height of the current subtree (maximum of left and right subtree heights)
    
    then initialize diameter to 0
    
    start DFS traversal from the root
    '''