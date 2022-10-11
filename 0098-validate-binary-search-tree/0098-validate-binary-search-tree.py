# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isVal(root, min_key, max_key):
            if root is None:
                return True
            
            if (min_key is not None and min_key >= root.val) or (max_key is not None and max_key <= root.val):
                return False
            
            return isVal(root.left, min_key, root.val) and isVal(root.right, root.val, max_key)
        return isVal(root, None, None)