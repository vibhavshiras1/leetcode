# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if(node in visited or node is None):
                return 0
            
            visited.add(node)
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            return (l+r+1)
        
        visited = set()
        return dfs(root)