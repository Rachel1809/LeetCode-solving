# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDia = 0
    def getDia(self, root):
        if root is None:
            return 0
        
        left = self.getDia(root.left)
        right = self.getDia(root.right)
        
        dia = left + right
        
        self.maxDia = max(dia, self.maxDia)
        
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDia(root)
        return self.maxDia
        
        
