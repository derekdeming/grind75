# 199. Binary Tree Right Side View

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        res = []
        dfs(root, 0)
        return res
    
'''
dfs approach to traverse the tree. DFS is used to see as far down a branch as possible before backtracking, which is suitable for this problem because we want to see the rightmost node at each level first.

dfs function is used to check to see if the curr node is None. If it is, the function returns immediately. This check is necessary to handle leaf nodes and ensure the recursion terminates properly.

*****the key part of this is the condition if level == len(res).... this checks whether the current level is being visited for the first time. If it is, the value of the current node (node.val) is appended to the res list. DFS first visits the right child (dfs(node.right, level + 1)), the first node encountered at each level is the rightmost node

call right child first because we want to see the rightmost node at each level first

'''