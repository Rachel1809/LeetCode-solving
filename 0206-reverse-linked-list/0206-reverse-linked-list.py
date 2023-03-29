# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        tmp, ne = head, head.next
        while tmp != None:
            ne = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = ne
        return prev