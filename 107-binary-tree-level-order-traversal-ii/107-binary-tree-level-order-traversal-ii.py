# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node,c):
            if(node is None):
                return
            
            if(c<len(res)):
                res[c].append(node.val)
            else:
                res.append([node.val])
            
            l = dfs(node.left,c+1)
            r = dfs(node.right,c+1)
            
        
        dfs(root,0)
        
        return res[::-1]