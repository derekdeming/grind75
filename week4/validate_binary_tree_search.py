#  98 

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node: #empty node
                return True
            # current node value must be between low and high
            if not (low < node.val < high):
                return False

            '''recursively check the left and right subtree
            for the left child, update the high value and then for the right child, update the low value
            '''
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)
