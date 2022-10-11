# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    balanced = True
    def getDepth(self, root):
        if root is None:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        
        if (abs(left - right) > 1):
            self.balanced = False
        
        return 1 + max(left, right)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.getDepth(root)
        return self.balanced
