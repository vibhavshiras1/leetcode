# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode   1(2(4))
        :rtype: str
        """
        
        def preorder(node):
            if(node is None):
                return ""
            
            if(node.left is None and node.right is None):
                return str(node.val)
            
            l = preorder(node.left)
            r = preorder(node.right)
            
            if(node.right is None):
                return str(node.val) + "(" + l + ")"
            
            return str(node.val) + "(" + l + ")(" + r + ")"
            
            
            
        return preorder(root)
            
        