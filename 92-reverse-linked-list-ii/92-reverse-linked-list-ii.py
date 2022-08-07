# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        left1 = head
        right1 = head
        l_prev = None
        diff = (right-left)
        
        while(left>1):
            l_prev = left1
            left1 = left1.next
            left -= 1
            
        l = left1
            
        while(right>1):
            right1 = right1.next
            right -= 1
        
        r_front = right1.next
        
        prev = ListNode(-501)
        c = 0
        
        while(c<=diff):
            next1 = left1.next
            left1.next = prev 
            prev = left1
            left1 = next1
            c += 1
            
        if(l_prev is not None):
            l_prev.next = right1
        else:
            head = right1
            
        l.next = r_front
        
        return head
        
            
        