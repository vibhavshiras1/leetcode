# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        arr = []
        
        while(head is not None):
            arr.append(head.val)
            head = head.next
            
        def build(arr):
            if(len(arr)==0):
                return None
            
            mid = len(arr)//2
            
            root = TreeNode(arr[mid])
            
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            
            return root
        
        return build(arr)