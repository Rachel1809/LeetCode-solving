# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        
        x = l1.val + l2.val
        output = ListNode(x%10)
        output_tail = output
        odd = x // 10
        l1 = l1.next
        l2 = l2.next
        
        while (l1 != None or l2 != None):
            i = 0
            j = 0
            if (l1 != None):
                i = l1.val
                l1 = l1.next
            if (l2 != None):
                j = l2.val
                l2 = l2.next
            x = odd + i + j
            output_tail.next = ListNode(x%10)
            odd = x // 10
                
            output_tail = output_tail.next
            
        output_tail.next = ListNode(odd) if odd != 0 else None
        return output
            
            
            
        