# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def inorder(node):
            if(node is None):
                res.append('n')
                return
            
            res.append(str(node.val))
            inorder(node.left)
            inorder(node.right)
            
        inorder(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
            
        self.i = 0
        
        def build():
            
            if(arr[self.i]=='n'):
                self.i += 1
                return None
            
            node = TreeNode(int(arr[self.i]))
            self.i += 1
            node.left = build()
            node.right = build()
            
            return node
        
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))