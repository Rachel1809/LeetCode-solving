# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l = []
        while (head):
            l.append(head.val)
            head = head.next
        
        def sortedToBST(l):
            if len(l) == 0:
                return None
            mid = len(l) // 2
            return TreeNode(l[mid], sortedToBST(l[:mid]), sortedToBST(l[mid+1:]))
            
        return sortedToBST(l)