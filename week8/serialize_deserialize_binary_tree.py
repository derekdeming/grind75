#  297

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else: 
                vals.append('#')
        vals = []
        preorder(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        vals = iter(data.split())
        
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer env. Deserialization is the reverse process.

Serialization: use a pre-order traversal to serialize the tree. A pre-order traversal visits the root node first, followed by the left subtree, and finally the right subtree. The pre-order traversal of a null node is represented by a sentinel value such as '#'.

Deserialization: use a queue to store the pre-order traversal and then construct the binary tree from the pre-order traversal. During deserialization, we use a queue to store the pre-order traversal. The reason we use a queue is because we always insert the children nodes of a node before its sibling nodes. Since we process the nodes in the same order as the pre-order traversal, we can use a queue to store the pre-order traversal and then construct the binary tree from the pre-order traversal.

basically we use a preorder traversal to serialize the tree. A preorder traversal visits the root node first, followed by the left subtree, and finally the right subtree. The preorder traversal of a null node is represented by a sentinel value such as '#'. 
'''