# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        leaf = False
        while queue:
            node = queue.pop(0)
            if node is None:
                leaf = True
            else:
                if leaf:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True