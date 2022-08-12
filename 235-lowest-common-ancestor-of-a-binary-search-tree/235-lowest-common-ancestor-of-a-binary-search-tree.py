# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if(node is None):
                return
            
            if((p.val<=node.val and q.val>=node.val) or (p.val>=node.val and q.val<=node.val)):
                return node
            
            if(node.val>q.val and node.val>p.val):
                return dfs(node.left)
            else:
                return dfs(node.right)
            
        return dfs(root)