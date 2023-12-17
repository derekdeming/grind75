#  230 Kth Smallest Element in a BST

# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        res = []
        inorder(root)
        return res[k-1]
    
'''
use inorder traversal to get the kth smallest element in a BST

inorder traversal of BST is an array sorted in the ascending order

inorder traversal of a Binary Search Tree (BST) == a method where we first visit the left subtree, then the root node, and finally the right subtree. When performed on a BST, it visits the nodes in ascending order (i.e., from the smallest to the largest key). This property makes inorder traversal particularly useful for this problem, as it allows us to easily find the kth smallest element.

The reason we visit the left subtree first, then the root node, and finally the right subtree (left -> root -> right) is because of the properties of a Binary Search Tree (BST). In a BST, all nodes to the left of a node have values less than the node, and all nodes to the right have values greater than the node. Therefore, visiting the nodes in this order (left -> root -> right) ensures that we visit the nodes in ascending order. This is why we use this order for inorder traversal.

'''

