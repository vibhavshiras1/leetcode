# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if(head is None):
            return None
        
        while(head is not None and head.val==val):
            head = head.next
            
        head1 = head
        prev = None
        
        while(head is not None):
            next1 = head.next
            if(head.val==val):
                prev.next = head.next
            else:
                prev = head
            head = next1
            
        return head1