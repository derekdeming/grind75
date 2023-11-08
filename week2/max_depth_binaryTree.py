# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftDep = self.maxDepth(root.left)
        rightDep = self.maxDepth(root.right)
        return max(leftDep, rightDep) + 1

# max depth of the current subtree is the max of left and right depths plus 1 for the current node