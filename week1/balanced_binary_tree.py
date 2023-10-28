from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# must dos: 

# a balanced tree is the following: 
# the depth (or height) of the two subtrees of every node never differs by more than 1.
# Both the left and right subtrees are also balanced.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance_check(node):
            if not node:
                return True, -1
            
            balancedL, heightL = balance_check(node.left)
            if not balancedL:
                return False, 0
            
            balancedR, heightR = balance_check(node.right)
            if not balancedR:
                return False, 0
            
            return abs(heightL - heightR) < 2, max(heightL, heightR) + 1 
        
        bal, _ = balance_check(root)
        return bal

        