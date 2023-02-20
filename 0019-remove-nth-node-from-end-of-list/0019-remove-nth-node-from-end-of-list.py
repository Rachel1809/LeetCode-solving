# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        sz = 0
        while cur:
            cur = cur.next
            sz += 1
        
        if n == sz:
            return head.next
        
        j = sz - n
        
        
        cur = head
        
        for i in range(j-1):
            cur = cur.next
            
        if not cur.next:
            return None
        
        cur.next = cur.next.next
        return head
        
        
        
            